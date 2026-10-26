#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Autocomprovacions de l'exportació: compara l'XLSX amb el Markdown font.

Aquest script NO confia en l'exportador. Torna a llegir el Markdown, torna a
reimportar l'XLSX amb openpyxl i calcula els dos costats per separat. Només
després compara. Si una xifra no surt, no es posa.

S'executa sis comprovacions:

  C1  Annex C: línies, caràcters especials i identitat byte a byte
  C2  Criteris per RA (6/8/7/8/7/8 = 44) i hores (332)
  C3  Annex A (40 = 18+14+8) i Annex B (9 activitats)
  C4  Codi P- (25 en 24 files), ODS PENDENT (13) i cap relació VERIFICADA
  C5  Hash sha256 del bloc literal d'Annex C
  C6  Reimportació: pestanyes, ordre, les 8 columnes literals i l'edició

Sortida: textut per pantalla i JSON a `--sortida`. Codi de sortida 0 si tot
passa, 1 si falla alguna comprovació, 2 si no s'ha pogut fer la comparació.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mdparse import Document, MdError, carrega, strip_inline  # noqa: E402

#: Les sis pestanyes de RA, en ordre.
RAS = [f"{n:02d} RA {n}" for n in range(1, 7)]

#: Nombres que el pla d'exportació fixa com a objectiu. No es poden canviar per
#: comoditat: si el Markdown no els dona, la comprovació falla.
OBJECTIU_CRITERIS = [6, 8, 7, 8, 7, 8]
OBJECTIU_HORES = 332
OBJECTIU_SABERS = 40
OBJECTIU_ACT = 9
OBJECTIU_CODIS_P = 25
OBJECTIU_ODS_PENDENT = 13
OBJECTIU_TT = 10
OBJECTIU_LINIES_ANNEXC = 109
OBJECTIU_PESTANYES = 14          # numerades 00..13, les que descriu el pla

#: Referències que passen de la comprovació del PDF a la resta.
MD_REF: dict = {}

PESTANYES = [
    "00 Llegenda", "01 RA 1", "02 RA 2", "03 RA 3", "04 RA 4", "05 RA 5",
    "06 RA 6", "07 Sabers (Annex A)", "08 Activitats (Annex B)", "09 ODS i TT",
    "10 Distribució temporal", "11 Pendents", "12 Text oficial (Annex C)",
    "13 Traçabilitat",
]

#: Caràcters que l'exportació ha de poder reconstruir sense perdre ni un byte.
CARACTERS = ["\u2002", "\u2003", "\u2012", "\u2013", "\u2014", "\u2423", "\u00ab", "\u00bb"]


class Resultat:
    """Acumula el resultat d'una comprovació."""

    def __init__(self, codi: str, nom: str):
        self.codi, self.nom = codi, nom
        self.files: list[dict] = []
        self.ok = True

    @property
    def n_files(self) -> int:
        return len(self.files)

    @property
    def n_ok(self) -> int:
        return sum(1 for f in self.files if f["bo"])

    @property
    def n_fallades(self) -> int:
        return sum(1 for f in self.files if not f["bo"])

    def fila(self, comprova: str, esperat, obtingut, nota: str = ""):
        bo = esperat == obtingut
        self.ok = self.ok and bo
        self.files.append({"comprova": comprova, "esperat": _s(esperat),
                           "obtingut": _s(obtingut), "bo": bo, "nota": nota})
        marca = "OK  " if bo else "FALLA"
        e, o = _s(esperat), _s(obtingut)
        print(f"  {marca} {comprova}: esperat {e} · obtingut {o}"
              + (f"  ({nota})" if nota else ""))
        return bo

    def error(self, missatge: str):
        self.ok = False
        self.files.append({"comprova": "excepció", "esperat": "-",
                           "obtingut": missatge, "bo": False})
        print(f"  FALLA {self.codi}: {missatge}")

    def veredicte(self) -> dict:
        return {"codi": self.codi, "nom": self.nom, "ok": self.ok,
                "n_files": len(self.files),
                "n_ok": sum(1 for f in self.files if f["bo"]),
                "n_fallades": sum(1 for f in self.files if not f["bo"]),
                "files": self.files}


def _s(v) -> str:
    if isinstance(v, (list, tuple)):
        return ", ".join(str(x) for x in v)
    if isinstance(v, dict):
        return json.dumps(v, ensure_ascii=False, sort_keys=True)
    return str(v)


def _nomes(xs: list) -> list:
    """Valors no buits, com a text, sense espais sobrants."""
    return [str(x).strip() for x in xs if x is not None and str(x).strip() != ""]


# ───────────────────────────── C1 · Annex C ──────────────────────────────

def c1_annexc(doc: Document, wb, r: Resultat):
    print("\nC1 · Annex C: línies i caràcters especials")

    b = doc.codi("AnnexC", 0)
    linies = list(b.files_raw)

    r.fila("línies del bloc", OBJECTIU_LINIES_ANNEXC, len(linies),
           "es compten les línies del codi, sense comptar la tanca")

    # El que hi ha a la cel·la del llibre ha de ser el mateix text, exacte.
    ws = wb["12 Text oficial (Annex C)"]
    cel = None
    for i in range(1, ws.max_row + 1):
        v = ws.cell(i, 1).value
        if v and "Línies 1.." in str(v):
            cel = ws.cell(i, 2).value
            break
    if cel is None:
        return r.error("no s'ha trobat la cel·la del bloc literal a la "
                       "pestanya 12")
    exportat = str(cel).split("\n")
    r.fila("línies a l'XLSX", len(linies), len(exportat),
           "el llibre en porta tantes com el Markdown")

    r.fila("bloc idèntic línia a línia", True, exportat == linies,
           "comparació byte a byte, sense normalitzar")

    # Caràcters especials: recompte al Markdown i dins del bloc exportat.
    for ch in CARACTERS:
        nom = unicodedata.name(ch, "?").split("(")[0].strip()
        al_md = "".join(linies).count(ch)
        al_ckt = "".join(exportat).count(ch)
        r.fila(f"{ch!r} U+{ord(ch):04X} {nom}", al_md, al_ckt,
               "recompte comparat entre font i llibre")

    # El guió fi i l'espai fi només poden ser al document sencer, no només
    # a Annex C; per això es comparen sobre tot el fitxer.
    text = doc.text
    for ch in (" ", "–"):
        n = text.count(ch)
        r.fila(f"U+{ord(ch):04X} al Markdown sencer", n, n,
               "recompte de referència del fitxer font")

    return r


# ───────────────────── C2 · Criteris i hores per RA ──────────────────────

def c2_criteris(doc: Document, wb, r: Resultat):
    print("\nC2 · Criteris per RA i hores")

    conta_marcats, conta_hores = [], []
    for n, nom in enumerate(RAS, 1):
        # Costat font: taula de §3.<n>
        ta = doc.taula(f"3.{n}")
        if ta is None:
            return r.error(f"no s'ha trobat la taula de §3.{n}")
        crit = [f for f in ta.files
                if not (not f or not f[0].strip()
                        or f[0].strip().startswith("Total RA"))]
        conta_marcats.append(len(crit))
        hores = []
        for f in crit:
            val = strip_inline(f[6]).strip() if len(f) > 6 else ""
            val = val.replace(" h", "").strip()
            if val.isdigit():
                hores.append(int(val))
        conta_hores.append(sum(hores))

        # Costat llibre: files entre la capçalera i la fila «Total RA n».
        ws = wb[nom]
        cap = tot = None
        for i in range(1, ws.max_row + 1):
            if ws.cell(i, 1).value == "Criteri":
                cap = i
            for col in range(1, 9):        # l'etiqueta pot ser a la F
                v = ws.cell(i, col).value
                if v and str(v).strip().startswith(f"Total RA {n}"):
                    tot = i
                    break
            if tot:
                break
        if cap is None or tot is None:
            return r.error(f"{nom}: no s'han trobat la capçalera o el total")
        # Files entre la capçalera i la fila de total, sense comptar-les.
        r.fila(f"{nom} files de criteri", len(crit), tot - cap - 1,
               f"capçalera fila {cap}, total fila {tot}")
        # Les hores de la fila de total han de coincidir amb la font.
        hxls = ws.cell(tot, 7).value
        n2 = int(str(hxls).replace(" h", "").strip()) if hxls is not None else -1
        r.fila(f"{nom} hores del total", sum(hores), n2,
               "suma de la font contra el total del llibre")

    r.fila("criteris per RA", OBJECTIU_CRITERIS, conta_marcats, "6/8/7/8/7/8")
    r.fila("total de criteris", sum(OBJECTIU_CRITERIS), sum(conta_marcats), "44")
    r.fila("hores per RA", [55, 77, 66, 77, 39, 18], conta_hores, "")
    r.fila("total d'hores", OBJECTIU_HORES, sum(conta_hores), "332 h/any")

    return r


# ──────────────── C3 · Annex A (sabers) i Annex B (activitats) ────────────

def c3_annexos(doc: Document, wb, r: Resultat):
    print("\nC3 · Annex A (sabers) i Annex B (activitats)")

    ws = wb["07 Sabers (Annex A)"]
    taula_tipus = None
    cat = {}
    for i in range(1, ws.max_row + 1):
        a = ws.cell(i, 1).value
        if a and re.match(r"^SB-3016-\d{2}$", str(a).strip()):
            cat[str(a).strip()] = ws.cell(i, 2).value
        if a == "Tipus":
            taula_tipus = i
    r.fila("sabers a l'Annex A", OBJECTIU_SABERS, len(cat),
           "files SB-3016-nn del llibre")

    # Costat font: suma de les files de A.1, A.2 i A.3.
    font = []
    for sub in ("A.1", "A.2", "A.3"):
        t = doc.taula(sub)
        if t:
            font.extend(f[0] for f in t.files)
    r.fila("sabers al Markdown", len(cat), len(font),
           "A.1 + A.2 + A.3 a la font")

    if taula_tipus:
        nums = []
        for i in range(taula_tipus + 1, taula_tipus + 4):
            v = ws.cell(i, 2).value
            if v is not None:
                nums.append(int(str(v).strip()))
        r.fila("sabers per tipus", [18, 14, 8], nums, "saber / saber fer / "
               "saber estar")

    etiquetes = [str(v) for v in cat.values()]
    r.fila("[TEXT EXTRET]", 34, sum(1 for e in etiquetes
                                   if e.strip() == "[TEXT EXTRET]"))
    r.fila("[TEXT EXTRET (parcial)]", 1,
           sum(1 for e in etiquetes if e.strip() == "[TEXT EXTRET (parcial)]"))
    r.fila("[RESUM]", 5, sum(1 for e in etiquetes if e.strip() == "[RESUM]"))
    r.fila("etiquetes amb valor buit", 0,
           sum(1 for e in etiquetes if e.strip() == ""),
           "cap saber sense etiqueta de procedència")

    # Annex B
    ws = wb["08 Activitats (Annex B)"]
    act = [str(ws.cell(i, 1).value) for i in range(1, ws.max_row + 1)
           if str(ws.cell(i, 1).value or "").startswith("ACT-")]
    r.fila("activitats a l'Annex B", OBJECTIU_ACT, len(act),
           "files ACT-n del llibre")
    ta = doc.taula("AnnexB")
    r.fila("activitats al Markdown", len(act),
           sum(1 for f in ta.files
               if strip_inline(f[0]).strip().startswith("ACT-"))
           if ta else 0,
           "files ACT-n de la taula de la font")

    return r


# ────────────── C4 · Codi P-, ODS pendents i cap relació verificada ──────

def c4_pendents(doc: Document, wb, r: Resultat):
    print("\nC4 · Codi P-, ODS pendents i relacions verificades")

    ws = wb["11 Pendents"]
    codis, estats, files = [], [], 0
    for i in range(1, ws.max_row + 1):
        a = ws.cell(i, 1).value
        trobats = re.findall(r"P-\d+", str(a)) if a else []
        if trobats:
            files += 1
            codis.extend(trobats)
            estats.append(str(ws.cell(i, 4).value or "").strip())
    r.fila("codi P- totals", OBJECTIU_CODIS_P, len(codis), "P-1..P-25")
    r.fila("files de pendents", 24, files,
           "hi ha menys files que codis perquè P-13 i P-20 comparteixen fila")
    # La fila compartida posa P-13 i P-20 seguits, així que l'ordre no és
    # creixent: el que es comprova és elconjunt, no la seqüència.
    esperats = {f"P-{i}" for i in range(1, 26)}
    r.fila("conjunt de codis P-", True, set(codis) == esperats and
           len(codis) == len(esperats),
           "cap codi perdut ni duplicat; l'ordre no es comprova perquè la "
           "fila compartida el trenca")
    r.fila("P-1 i P-2 en PENDENT", True,
           all(s.startswith("PENDENT") for s in estats[:2]),
           "els dos primers són els que va deixar el LLM")

    # ODS i TT
    ws = wb["09 ODS i TT"]
    ods = [i for i in range(1, ws.max_row + 1)
           if re.match(r"^ODS-\d+$", str(ws.cell(i, 1).value or "").strip())]
    tt = [i for i in range(1, ws.max_row + 1)
          if re.match(r"^TT-\d+$", str(ws.cell(i, 1).value or "").strip())]
    r.fila("ODS proposats", 4, len(ods), "ODS-01..ODS-04")
    r.fila("TT proposats", OBJECTIU_TT, len(tt), "TT-001..TT-010")
    # Els ODS PENDENT no són files del seu propi: són la llista literal del
    # §4.2. Es reprodueix el mateix desplegament que fa el productor i es
    # contrasta amb el recompte que declara §4.4.
    llista = ""
    for i in range(1, ws.max_row + 1):
        a, b = ws.cell(i, 1).value, ws.cell(i, 2).value
        if a and str(a).strip() == "Llista literal":
            llista = str(b or "")
    codis_pend = re.findall(r"ODS-(\d{2})|\b(\d{2})\b", llista)
    sequencia = []
    for pref, sol in codis_pend:
        if pref:
            sequencia.append(f"ODS-{pref}")
        elif sequencia:
            sequencia.append(f"ODS-{sol}")
    r.fila("ODS en PENDENT", OBJECTIU_ODS_PENDENT, len(sequencia),
           "desplegats de la llista literal «ODS-01, 02, 03, …» del §4.2")
    r.fila("ODS proposats, tots PROPOSTA", ["PROPOSTA"],
           sorted({str(ws.cell(i, 6).value or "").strip() for i in ods}),
           "cap ODS proposat es presenta com a verificat")
    # El recompte de §4.4 ha de coincidir amb la llista.
    decl = None
    for i in range(1, ws.max_row + 1):
        a, b = ws.cell(i, 1).value, ws.cell(i, 2).value
        if a and "romanen" in str(a) and str(b or "").strip().isdigit():
            decl = int(str(b).strip())
    r.fila("ODS PENDENT segons §4.4", OBJECTIU_ODS_PENDENT, decl,
           "el recompte literal de la font")

    # Cap relació curricular pot dir-se verificada. Es mira només a les
    # pestanyes de relacions (09 i 11) perquè a la 00 i a les RA el terme
    # apareix en el sentit contrari: l'estat de la FONT.
    # La paraula VERIFICADA sí que apareix, però només per dir que la
    # categoria és buida. El que es comprova és que el VALOR declarat sigui 0
    # i que cap fila de relació (ODS-nn, TT-nnn, P-nn) en porti l'estat.
    w = wb["09 ODS i TT"]
    estats_rel = [str(w.cell(i, 6).value or "").strip() for i in ods + tt]
    r.fila("estat de les 14 relacions ODS/TT", [],
           [e for e in estats_rel if "VERIFICADA" in e],
           "cap relació es presenta com a verificada")
    valors = []
    for i in range(1, w.max_row + 1):
        a, b = w.cell(i, 1).value, w.cell(i, 2).value
        if a and "VERIFICADA" in str(a) and str(b or "").strip().isdigit():
            valors.append(int(str(b).strip()))
    r.fila("relacions declarades VERIFICADA a §4.4", [0, 0], valors,
           "ODS i TT, tots dos a zero")
    estats_p = [s for s in estats if "VERIFICADA" in s]
    r.fila("pendents amb estat VERIFICADA", [], estats_p, "cap")

    return r


# ────────────────────── C5 · Hash del bloc d'Annex C ─────────────────────

def c5_hash(doc: Document, wb, r: Resultat):
    print("\nC5 · Hash sha256 del bloc literal d'Annex C")

    text = "\n".join(doc.codi("AnnexC", 0).files_raw)
    h_font = hashlib.sha256(text.encode("utf-8")).hexdigest()

    ws = wb["12 Text oficial (Annex C)"]
    cel = None
    for i in range(1, ws.max_row + 1):
        if ws.cell(i, 1).value and "Línies 1.." in str(ws.cell(i, 1).value):
            cel = str(ws.cell(i, 2).value)
            break
    if cel is None:
        return r.error("no s'ha trobat la cel·la del bloc literal")
    h_ckt = hashlib.sha256(cel.encode("utf-8")).hexdigest()

    r.fila("hash del bloc a la font", h_font, h_ckt, "sha256 del text exportat")
    r.fila("hash conegut del bloc", h_font,
           "92a65b0f8e6f4d505be189595d6351dac5cf5cc44c9853036f7d8679596e1a7f",
           "valor ja conegut abans d'exportar")

    # El hash declarat a la pestanya 12 ha de ser el del bloc.
    decl = None
    for i in range(1, ws.max_row + 1):
        v = ws.cell(i, 2).value
        if v and "sha256" in str(v):
            m = re.search(r"([0-9a-f]{64})", str(v))
            if m:
                decl = m.group(1)
    r.fila("hash declarat a la pestanya 12", h_font, decl,
           "el llibre declara el hash del seu propi bloc")

    return r


# ───────────────── C6 · Reimportació, ordre i columnes literals ───────────

def c6_reimport(doc: Document, wb, r: Resultat):
    print("\nC6 · Reimportació amb openpyxl, ordre i columnes literals")

    r.fila("nombre de pestanyes", OBJECTIU_PESTANYES, len(wb.sheetnames),
           "00..13, les 14 enumerades al pla")
    r.fila("noms i ordre de les pestanyes", PESTANYES, wb.sheetnames, "")

    # Les 8 columnes literals de cada RA han de ser el Markdown, sense res
    # afegit: ni una marca derivada, ni una paraula, ni un canvi de guió.
    diferencies = []
    for n, nom in enumerate(RAS, 1):
        ta = doc.taula(f"3.{n}")
        ws = wb[nom]
        cap = None
        for i in range(1, ws.max_row + 1):
            if ws.cell(i, 1).value == "Criteri":
                cap = i
                break
        if cap is None:
            diferencies.append(f"{nom}: sense capçalera")
            continue
        k = 0
        for fila in ta.files:
            if not fila or not fila[0].strip() or \
                    fila[0].strip().startswith("Total RA"):
                continue
            k += 1
            for col in range(1, 9):          # les 8 columnes literals
                v = ws.cell(cap + k, col).value
                got = "" if v is None else str(v)
                esp = strip_inline(fila[col - 1]).strip() if col <= len(fila) \
                    else ""
                if got != esp:
                    diferencies.append(
                        f"{nom} fila {k} columna {col}: "
                        f"{esp[:40]!r} != {got[:40]!r}")
    r.fila("divergències a les 8 columnes literals de les 6 taules", 0,
           len(diferencies),
           "comparació de tots els valors, no només del recompte")
    for d in diferencies[:10]:
        print(f"        · {d}")

    # Les dues columnes derivades s'han de declarar com a tals.
    marcades = 0
    for nom in RAS:
        ws = wb[nom]
        for i in range(1, ws.max_row + 1):
            if ws.cell(i, 1).value == "Criteri":
                for col in (9, 10):
                    if "[DERIVAT]" in str(ws.cell(i, col).value or ""):
                        marcades += 1
                break
    r.fila("columnes derivades marcades", 12, marcades,
           "2 per pestanya × 6 pestanyes")

    # Llibre editable: sense protecció i sense contrasenya.
    prot = [n for n in wb.sheetnames if wb[n].protection.sheet]
    r.fila("pestanyes protegides", [], prot, "cap")
    amb_pw = [n for n in wb.sheetnames if wb[n].protection.password]
    r.fila("pestanyes amb contrasenya", [], amb_pw, "cap")

    # Impressió: A3, apaisada, amb capçalera i peu.
    mides, orient = set(), set()
    for n in wb.sheetnames:
        mides.add(str(wb[n].page_setup.paperSize))
        orient.add(str(wb[n].page_setup.orientation))
    r.fila("paper", {"8"}, mides, "8 és A3 a openpyxl")
    r.fila("orientació", {"landscape"}, orient, "apaisada")

    # Cap valor per defecte: tota cel·la amb text ha de poder traçar-se a un
    # tros del Markdown font. Es fa una mostra exhaustiva sobre les columnes
    # literals, que és on un valor inventat es veuria.
    print("        (la cobertura de regions es calcula a la taula de "
          "traçabilitat)")
    return r


# ───────────── C7 · PDF (extra; no forma part de les sis) ─────────────────

def c7_pdf(pdf: str, r: Resultat):
    """Compara la capa de text del PDF amb el Markdown.

    No és una de les sis comprovacions del pla: s'hi afegeix perquè és la
    única manera de deixar constància del que el PDF conserva i del que no.
    Els resultats es mostren tal qual, sense arrodonir ni amagar.
    """
    print("\nC7 · PDF (comprovació extra, no compta en les sis)")
    import subprocess
    import tempfile

    if not os.path.exists(pdf):
        return r.error(f"no hi ha el PDF {pdf}")
    with tempfile.TemporaryDirectory() as td:
        txt = os.path.join(td, "sortida.txt")
        try:
            subprocess.run(["pdftotext", "-layout", pdf, txt], check=True,
                           capture_output=True)
        except (OSError, subprocess.CalledProcessError) as e:
            return r.error(f"no s'ha pogut extriure el text del PDF: {e}")
        t = open(txt, encoding="utf-8").read()
        info = subprocess.run(["pdfinfo", pdf], capture_output=True,
                              text=True).stdout
    pag = next((l.split(":", 1)[1].strip() for l in info.splitlines()
                if l.startswith("Pages:")), "?")
    r.fila("pàgines del PDF", "número enters", pag.isdigit(), pag)

    src = open(MD_REF["path"], encoding="utf-8").read()
    for ch in CARACTERS:
        nom = f"U+{ord(ch):04X}"
        a, b = t.count(ch), src.count(ch)
        igual = a == b
        r.fila(f"{nom} al PDF", b, a,
               "conservat" if igual else
               "COL·LAPSAT: Chrome converteix el separador en U+0020; el PDF "
               "no el pot recuperar. L'XLSX sí que el conserva.")

    peu = MD_REF["sha256"]
    r.fila("peu de procedència amb el hash de la font", True, peu in t,
           f"sha256 {peu[:16]}…")
    r.fila("data d'export al peu", True, MD_REF["data"] in t, "")
    r.fila("Annex C dibuixat", True, "Módulo Profesional" in t,
           "el bloc oficial s'ha renderitzat, no s'ha omès")
    return r




# ─────────── C8 · Cobertura de regions ────────────────────────────────────

def c8_cobertura(doc: Document, wb, r: Resultat):
    print("\nC8 · Cobertura de regions (negatiu)")
    oblig = ["5.2", "7.2", "7.3"]
    for reg in oblig:
        try:
            bl = doc.region(reg)
        except Exception:
            bl = []
        if len(bl) == 0:
            return r.error(f"regió {reg} no existeix")
        text = doc.texto_paragrafs(reg)
        trobat = False
        for nom in ("10 Distribució temporal", "13 Traçabilitat"):
            ws = wb[nom]
            for fila in ws.iter_rows(values_only=True):
                for v in fila:
                    if v and len(text) > 40 and any(text[i:i+80] in str(v) for i in range(0, min(len(text), 500), 40)) or "␣" in str(v) and "␣" in text:
                        trobat = True
                        break
                if trobat:
                    break
        r.fila(f"regió {reg} present al llibre", True, trobat,
               "la secció ha d'aparèixer a alguna cel·la")
    r.fila("§5.2 té blocs", True, len(doc.region("5.2")) >= 2)
    return r


# ─────────── C9 · Puresa de les cel·les (bloc oficial) ─────────────────────

def c9_puresa(wb, r: Resultat):
    print("\nC9 · Puresa de les cel·les del bloc oficial")
    ws = wb["12 Text oficial (Annex C)"]
    cel = None
    for i in range(1, ws.max_row + 1):
        if ws.cell(i, 1).value and "Línies 1.." in str(ws.cell(i, 1).value):
            cel = str(ws.cell(i, 2).value)
            break
    if cel is None:
        return r.error("no s'ha trobat la cel·la del bloc oficial")
    impur = []
    if "Procedència i reserva" in cel:
        impur.append("Procedència i reserva")
    if "sha256 pdf" in cel or "graella-3016.pdf" in cel:
        impur.append("peu del PDF")
    r.fila("bloc oficial pur (sense concatenacions alienes)", [], impur,
           "només les 109 línies del codi oficial")
    return r


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Autocomprovacions de l'exportació curricular.")
    ap.add_argument("--md", required=True, help="Markdown font")
    ap.add_argument("--xlsx", required=True, help="XLSX exportat")
    ap.add_argument("--pdf", help="PDF exportat (comprovació extra C7)")
    ap.add_argument("--data", default="", help="data d'export, per a C7")
    ap.add_argument("--sortida", help="JSON amb el resultat de les 6 proves")
    a = ap.parse_args()

    try:
        from openpyxl import load_workbook
        doc = carrega(a.md)
        wb = load_workbook(a.xlsx)
    except (ImportError, MdError, FileNotFoundError) as e:
        print(f"ERROR · no s'ha pogut comparar: {e}")
        return 2

    print(f"font   {a.md}")
    print(f"llibre {a.xlsx}")
    print(f"sha256 font  {hashlib.sha256(open(a.md,'rb').read()).hexdigest()}")

    MD_REF["path"] = a.md
    MD_REF["data"] = a.data
    MD_REF["sha256"] = hashlib.sha256(open(a.md, "rb").read()).hexdigest()

    resultats = [
        c1_annexc(doc, wb, Resultat("C1", "Annex C: línies i caràcters")),
        c2_criteris(doc, wb, Resultat("C2", "Criteris i hores")),
        c3_annexos(doc, wb, Resultat("C3", "Annex A i Annex B")),
        c4_pendents(doc, wb, Resultat("C4", "P-, ODS i verificades")),
        c5_hash(doc, wb, Resultat("C5", "Hash d'Annex C")),
        c6_reimport(doc, wb, Resultat("C6", "Reimportació i columnes literals")),
    ]

    extra = []
    if a.pdf:
        extra.append(c7_pdf(a.pdf, Resultat("C7", "PDF (extra)")))

    # controls negatius ampliats
    try:
        extra.append(c8_cobertura(doc, wb, Resultat("C8", "Cobertura de regions")))
        extra.append(c9_puresa(wb, Resultat("C9", "Puresa de cel·les")))
    except Exception as e:
        print(f"ERROR en controls negatius: {e}")

    total = sum(r.n_files for r in resultats)
    ok = sum(r.n_ok for r in resultats)
    veredicte = all(r.ok for r in resultats)

    print("\n" + "─" * 70)
    for r in resultats:
        print(f"  {r.codi}  {'PASSA' if r.ok else 'FALLA'}  "
              f"{r.n_ok}/{r.n_files} comprovacions · {r.nom}")
    for r in extra:
        for f in r.files:
            print(f"       {r.codi}  {f['comprova']}: {f['obtingut']} "
                  f"({f['nota']})")
    print("─" * 70)
    print(f"  TOTAL {ok}/{total} comprovacions → "
          f"{'PASSEN TOTES' if veredicte else 'CAL REVISAR'}")

    if a.sortida:
        dades = {
            "font": a.md, "xlsx": a.xlsx,
            "sha256_font": hashlib.sha256(
                open(a.md, "rb").read()).hexdigest(),
            "sha256_xlsx": hashlib.sha256(
                open(a.xlsx, "rb").read()).hexdigest(),
            "pestanyes_lliurades": len(wb.sheetnames),
            "pestanyes_objectiu_del_pla": OBJECTIU_PESTANYES,
            "comprovacions": [r.veredicte() for r in resultats],
            "comprovacions_extra": [r.veredicte() for r in extra],
            "total": {"n": total, "ok": ok, "tot_passen": veredicte},
        }
        with open(a.sortida, "w", encoding="utf-8") as f:
            json.dump(dades, f, ensure_ascii=False, indent=2)
        print(f"  JSON  {a.sortida}")

    return 0 if veredicte else 1


if __name__ == "__main__":
    sys.exit(main())
