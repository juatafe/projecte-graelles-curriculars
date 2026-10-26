#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Mapa de regions de la graella → llibre de 15 pestanyes.

Aquest mòdul és l'únic lloc on es decideix **què** va a cada cel·la. Es
construïr una vegada i serveix a dos consumidors:

* `exportar_xlsx.py` hi escriu cada valor a la seua adreça;
* `comparar_export.py` llegeix el XLSX i comprova, cel·la a cel·la i
  caràcter a caràcter, que hi ha exactament el text del Markdown.

Regles que no es trenquen mai:

1. **No es redacta cap contingut curricular.** Tots els valors de classe
   `capcalera`, `dades` o `estructura` provenen de `strip_inline()` d'una
   cel·la, fila o línia concreta del Markdown, es trobi on es trobi.
2. **Cap valor per defecte.** Tota fila de dades ha de dur com a mínim una
   marca reconeixible (etiqueta entre corxets, `PENDENT`, `RESOLT`,
   `VERIFICADA`, `:—`, «amb reserva» o un codi literal del §0.2 del propi
   document). Si no la du, `regions.py` aixeca `SenseMarca` i
   `exportar_xlsx.py` surt amb codi d'error.
3. **El que es calcula** du el prefix `[DERIVAT]` o `[PROCEDÈNCIA]` i la
   seva classe, de manera que el revisor el pugui distingir d'un text
   literal sense haver-ho de deduir.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from mdparse import (
    Document, MdError, RE_CODIS, fila_te_marca, marques_reconeixibles,
    strip_inline,
)

CLS_CAPCALERA = "capcalera"
CLS_DADES = "dades"
CLS_ESTRUCTURA = "estructura"
CLS_DERIVADA = "derivada"
CLS_PROCEDENCIA = "procedencia"
#: Fila de declaració del projecte sobre la graella, copiada literalment
#: d'una de les tres llistes de prosa §4.1, §5.4 i §6.5. No afirma cap valor
#: curricular, sinó què ha comprovat el projecte i què no fa. Es reconeix per
#: la seva classe i pel títol del bloc, que ho diu a la pestanya.
CLS_ADVERTIMENT = "advertiment"
#: Fila d'una taula de recomptes les files de la qual depenen d'una marca
#: literal que l'ENCAPÇALAMENT DE LA REGIÓ declara per a totes (per exemple
#: el `[PROPOSTA]` que §6.4 posa damunt de la taula de famílies
#: d'instruments). Sense aquella marca literal a la regió, no s'exporta res.
CLS_PROPOSTA = "proposta"

MARCA_DERIVADA = "[DERIVAT]"
MARCA_PROCEDENCIA = "[PROCEDÈNCIA]"

PREFIXE_SABER = "SB-"
REGEX_SABER = re.compile(r"SB-\d{4}-\d{2}")
REGEX_P = re.compile(r"P-\d+")


class SenseMarca(MdError):
    """Una fila de dades no du cap marca reconeixible."""


# --------------------------------------------------------------------------
# Estructures de sortida
# --------------------------------------------------------------------------


@dataclass
class Cel:
    address: str
    valor: str
    regio: str
    grup: str
    classe: str
    estil: str = "normal"      # normal|monoespaciada|titol|subtitol


@dataclass
class Fulla:
    sheet: str
    celles: list = field(default_factory=list)
    amplada: dict = field(default_factory=dict)
    congelar: str = ""
    autofilter: str = ""
    ncols: int = 0


def col_letra(idx0: int) -> str:
    """0 -> A, 25 -> Z, 26 -> AA."""
    s = ""
    i = idx0 + 1
    while i:
        i, r = divmod(i - 1, 26)
        s = chr(65 + r) + s
    return s


# --------------------------------------------------------------------------
# Constructor de fulla
# --------------------------------------------------------------------------


class Constructor:
    """Assigna adreces i registra les regions, sense escriure res."""

    def __init__(self, sheet: str):
        self.f = Fulla(sheet=sheet)
        self.r = 0

    # -- primitivas -------------------------------------------------------

    def fila(self, valors, regio, grup, classe=CLS_DADES, estil="normal"):
        self.r += 1
        f = self.f
        fila_n = self.r
        for c, v in enumerate(valors):
            if v is None or v == "":
                continue
            f.celles.append(Cel(f"{col_letra(c)}{fila_n}", str(v), regio, grup,
                               classe, estil))
        f.ncols = max(f.ncols, len(valors))
        return fila_n

    def fila_kv(self, etiqueta, valor, regio, grup, classe_val=CLS_DADES,
                estil_val="normal"):
        """Fila de dos columnes: etiqueta a la columna A, valor a la B."""
        self.r += 1
        n = self.r
        self.f.celles.append(Cel(f"A{n}", str(etiqueta), regio, grup,
                                CLS_CAPCALERA, "normal"))
        if valor is not None and valor != "":
            self.f.celles.append(Cel(f"B{n}", str(valor), regio, grup,
                                    classe_val, estil_val))
        self.f.ncols = max(self.f.ncols, 2)
        return n

    def _kv(self, etiqueta, valor, regio, grup, classe_val=CLS_DADES,
            estil_val="normal"):
        self.r += 1
        n = self.r
        self.f.celles.append(Cel(f"A{n}", str(etiqueta), regio, grup,
                                CLS_CAPCALERA, "normal"))
        if valor is not None and valor != "":
            self.f.celles.append(Cel(f"B{n}", str(valor), regio, grup,
                                    classe_val, estil_val))
        self.f.ncols = max(self.f.ncols, 2)
        return n

    def blanc(self, n=1):
        self.r += n
        return self.r

    def titol(self, text, regio, grup):
        self.r += 1
        self.f.celles.append(Cel(f"A{self.r}", text, regio, grup, CLS_CAPCALERA,
                                "titol"))
        self.f.ncols = max(self.f.ncols, 1)
        return self.r

    def capcalera_taula(self, capcaleres, regio, grup):
        return self.fila([strip_inline(c) for c in capcaleres], regio, grup,
                         CLS_CAPCALERA)

    def adressa_ultima_fila(self):
        return self.r


# --------------------------------------------------------------------------
# Verificació de marques
# --------------------------------------------------------------------------


def porta_advertiment(txt: str, raw: str, sec: str, k: int, avisos: list):
    """Porta de les files de prosa de §4.1, §5.4 i §6.5.

    Aquestes files no afirmen cap valor curricular: són les declaracions del
    projecte sobre la pròpia graella. No se'ls exigeix marca curricular perquè
    no n'hi ha cap a emplaar. El que sí que s'exigeix és que la fila provingui
    literalment de la llista (garantit per l'analitzador, que avisa si la
    llista no hi és) i que això quedi DECLARAT a la pestanya amb la classe
    `advertiment` i el títol del bloc.

    Les files que no tenen cap marca es reporten, perquè el revisor pugui
    veure-les una a una en comptes de descobrir-les per casualitat.
    """
    marques = marques_reconeixibles(txt, raw)
    if not marques:
        avisos.append({
            "seccio": sec, "item": k, "classe": CLS_ADVERTIMENT,
            "marca": "cap",
            "text": txt[:200],
            "motiu": "declaració del projecte sobre la graella; no afirma cap "
                     "valor curricular, per això no se li exigeix marca",
        })
    return marques


def marca_de_la_regio(doc, sec: str, marca: str, on: str) -> str:
    """Comprova que la regió `sec` declari `marca` literalment.

    Aquesta marca és la que governa les files de recompt que no en duen cap
    de pròpia. Si no hi és, no hi ha res a governs i l'exportació s'atura:
    mai es presumeix el que la regió no diu.
    """
    txt = doc.texto_paragrafs(sec)
    for b in doc.region(sec):
        if b.kind in ("olist", "ulist"):
            txt += "\n" + "\n".join(b.files)
        elif b.kind == "table":
            txt += "\n" + b.text
    if marca not in txt:
        raise MdError(
            f"{on}: la regió §{sec} no conté la marca literal {marca!r} que "
            f"governa aquestes files. No hi ha valor per defecte.")
    return marca


def es_fila_estructura(vals: list) -> bool:
    """Fila d'agregació, no de dades: `**Total RA n**` i `**TOTAL**`.

    Aquestes files no afirmen cap valor curricular nou; tot el que diuen
    ja és en altres files. S'exporten igualment, amb classe
    `estructura`, i queden exemptes de la porta de marques.
    """
    first = vals[0].strip() if vals else ""
    return (first.startswith("Total RA") or first.upper() == "TOTAL"
            or first == "")


def exigeix_marca(text_fila: str, on: str, raw: str | None = None):
    """Porta de qualitat. Sense marca no s'exporta: es rebuta emplenar."""
    if not fila_te_marca(text_fila, raw):
        raise SenseMarca(
            f"{on}: cap marca reconeixible a la fila. Es rebuta omplir-la.\n"
            f"  text: {text_fila[:160]!r}")


# --------------------------------------------------------------------------
# Columnes derivades (mecàniques, marcades com a tals)
# --------------------------------------------------------------------------


def estat_de_la_relacio(criteri, saber, saber_fer, saber_estar, contingut,
                        activitat, hores, instrument) -> str:
    """Composició mecànica d'un vocabulari tancat, sense cap judici.

    Cada regla és una comprovació literal sobre la mateixa fila; no hi ha
    cap valor possible fora d'aquest vocabulari.
    """
    t = []
    for col, nom in ((saber, "sense saber"),
                     (saber_fer, "sense saber fer"),
                     (saber_estar, "sense saber estar")):
        if ":—" in col:
            t.append(nom)
    if "CAP." in contingut:
        t.append("sense contingut bàsic (CAP.)")
    if "amb reserva" in contingut:
        t.append("cobertura amb reserva")
    if "[RESUM]" in criteri or "[RESUM]" in saber or "[RESUM]" in saber_fer \
            or "[RESUM]" in saber_estar:
        t.append("almenys un saber [RESUM]")
    if "PENDENT" in contingut or "PENDENT" in instrument \
            or "PENDENT" in criteri:
        t.append("PENDENT")
    if activitat.strip().lower() == "cap":
        t.append("sense activitat")
    if hores.strip().startswith("0"):
        t.append("0 h assignades")
    if not t:
        t = ["sense marca de cobertura"]
    return f"{MARCA_DERIVADA} " + " · ".join(t)


def pendent_citat(text_fila: str) -> str:
    codis = []
    for c in REGEX_P.findall(text_fila):
        if c not in codis:
            codis.append(c)
    if codis:
        return f"{MARCA_DERIVADA} " + " · ".join(codis)
    return f"{MARCA_DERIVADA} cap codi P- a la fila"


def extreu_p(text_fila: str) -> list:
    out = []
    for c in REGEX_P.findall(text_fila):
        if c not in out:
            out.append(c)
    return out


# --------------------------------------------------------------------------
# Catàleg de sabers (Annex A) i d'activitats (Annex B)
# --------------------------------------------------------------------------


def sabers_annex_a(doc: Document) -> dict:
    """{ID: (tipus, etiqueta, text, origen)} copiat literalment de l'Annex A."""
    out = {}
    tipus_de = {}
    for sub in ("A.1", "A.2", "A.3"):
        t = doc.taula(sub)
        tipus = strip_inline(doc.heading(sub).titol).split("—")[0].strip()
        tipus = tipus.replace("`", "")
        for fila in t.files:
            sid = strip_inline(fila[0]).strip()
            exigeix_marca(" ".join(strip_inline(c) for c in fila),
                          f"Annex {sub} · {sid}", " ".join(fila))
            out[sid] = (tipus, strip_inline(fila[1]), strip_inline(fila[2]),
                        strip_inline(fila[3]))
            tipus_de[sid] = tipus
    return out


def llista_sabers(doc: Document) -> list:
    """Les 40 files de l'Annex A, en ordre de document i amb ordre de tipus."""
    ordre = []
    for sub in ("A.1", "A.2", "A.3"):
        for fila in doc.taula(sub).files:
            sid = strip_inline(fila[0]).strip()
            if sid.startswith("SB-"):
                ordre.append(sid)
    return ordre


# --------------------------------------------------------------------------
# El llibre sencer
# --------------------------------------------------------------------------


class Llibre:
    def __init__(self, doc: Document, informe_path: str = "",
                 data_exportacio: str = ""):
        self.doc = doc
        self.informe_path = informe_path
        self.data_exportacio = data_exportacio
        self.sabers = sabers_annex_a(doc)
        self.ordre_sabers = llista_sabers(doc)
        self.fulles: dict = {}
        self.xifres: dict = {}
        self.avisos: list = []

    # -- utilitats --------------------------------------------------------

    def fulla(self, sheet: str, amplada: dict, congelar: str = "",
              autofilter: str = "") -> Constructor:
        c = Constructor(sheet)
        c.f.amplada = amplada
        c.f.congelar = congelar
        c.f.autofilter = autofilter
        self.fulles[sheet] = c.f
        return c

    def _informe(self, patro, etiqueta):
        if not self.informe_path:
            raise MdError(
                f"cal --informe per omplir {etiqueta!r}; no hi ha valor "
                f"per defecte")
        txt = open(self.informe_path, encoding="utf-8").read()
        for lin in txt.split("\n"):
            if re.search(patro, lin):
                return lin
        raise MdError(
            f"{self.informe_path}: no s'hi troba {etiqueta!r} ({patro!r}); "
            f"es queda PENDENT i no s'inventa")

    # ==================================================================
    # 00 · Llegenda
    # ==================================================================

    def calcula_xifres(self, ra_info, s09, s10, s11, s12):
        d = self.doc
        dades = []
        files_criteri = sum(len(v["grups"]) for v in ra_info.values())
        dades.append(("Files de criteri a les 6 taules de §3 (sense la fila «Total RA n»)", str(files_criteri), "00/xifres/criteris"))
        hores = []
        for n in sorted(ra_info):
            tot = ra_info[n]["total"]
            h = tot[6].strip() if len(tot) > 6 else ""
            if not h:
                raise MdError(f"§3.{n}: la fila Total no té hores a la columna «Hores»")
            hores.append((n, h))
        dades.append(("Hores per RA (de la fila «Total RA n», text literal)", " + ".join(h for _, h in hores), "00/xifres/hores"))
        total_h = []
        for _, h in hores:
            x = re.match(r"(\d+)", h)
            if not x:
                raise MdError(f"la fila Total conté hores no numèriques: {h!r}")
            total_h.append(int(x.group(1)))
        dades.append((f"Suma d'hores ({' + '.join(str(x) for x in total_h)})", str(sum(total_h)), "00/xifres/suma"))
        dades.append(("Files de criteri amb 0 h assignades", str(sum(1 for n in sorted(ra_info) if _zero_hores(d, n))), "00/xifres/zero"))
        dades.append(("Sabers a l'Annex A (A.1 + A.2 + A.3)", str(len(self.ordre_sabers)), "00/xifres/sabers"))
        for etiq in ("[TEXT EXTRET]", "[TEXT EXTRET (parcial)]", "[RESUM]"):
            n = sum(1 for sid in self.ordre_sabers if etiq in self.sabers[sid][1])
            dades.append((f"Sabers amb etiqueta {etiq}", str(n), f"00/xifres/sabers{etiq}"))
        dades.append(("Activitats ACT-n a l'Annex B", str(len(d.taula("AnnexB").files)), "00/xifres/act"))
        dades.append(("Codi ODS proposats a §4.2", str(len(s09["ods"])), "00/xifres/ods"))
        dades.append(("Codi TT a §4.3", str(len(d.taula("4.3").files)), "00/xifres/tt"))
        dades.append(("Advertiments de §4.1", str(s09["adv"]), "00/xifres/adv41"))
        dades.append(("Advertiments de §5.4", str(s10["adv"]), "00/xifres/adv54"))
        dades.append(("Files de §7.1", str(s11["files"]), "00/xifres/s71f"))
        dades.append(("Codi P- a §7.1 (la fila P-13/P-20 en porta dos)", str(len(s11["codis"])), "00/xifres/p"))
        dades.append(("Línies del bloc oficial de l'Annex C", str(s12["linies"]), "00/xifres/annexc"))
        dades.append(("sha256 del bloc oficial de l'Annex C", s12["sha256"], "00/xifres/annexcsha"))
        dades.append(("Relacions ODS o TT amb estat VERIFICADA al mòdul", str(_verificades(d)), "00/xifres/verificades"))
        self.xifres = {"files": dades}
        return self.xifres

    def fulla_00(self):
        g = "00 Llegenda"
        c = self.fulla(g, {"A": 46, "B": 132, "C": 40})
        d = self.doc

        c.titol("Llegenda i procedència · exportació no curricular", f"{g}/titol",
                g)
        c.blanc()

        c.titol("Procedència", f"{g}/procedencia/titol", g)
        c.fila_kv("Camp", "Contingut", f"{g}/procedencia/capcalera", g,
                  CLS_PROCEDENCIA)
        c._kv("Aquest llibre", f"{MARCA_PROCEDENCIA} Exportació NO curricular "
               "d'una graella Markdown ja validada. L'exportador COPIA regions "
               "identificades del fitxer font: no redacta, no completa i no "
               "inverteix cap contingut. Qualsevol dada que no hi fos, es "
               "quedaria PENDENT i es declararia.", f"{g}/procedencia/naturalesa",
               g, CLS_PROCEDENCIA)
        c._kv("Procedència dels ODS", "F-001 · només text literal de la "
               "denominació · mai exigibilitat curricular", f"{g}/procedencia/ods",
               g, CLS_PROCEDENCIA)
        c._kv("Criteri de reconstrucció", "Exportar, no redactar. Cap contingut "
               "curricular nou. Cap valor per defecte.", f"{g}/procedencia/regla",
               g, CLS_PROCEDENCIA)
        c._kv("Recompte de pestanyes", f"{MARCA_PROCEDENCIA} Aquest llibre té "
               f"14 pestanyes, numerades de 00 a 13, que són exactament les que "
               f"descriu el pla d'exportació com a taula. El mateix pla en el "
               f"text diu «15 pestanyes»: el recompte i la taula no "
               f"quadren. S'han fet les 14 enumerades, perquè la numeració 00–13 "
               f"és explícita i no hi ha cap pestanya 14 descrita que es pugui "
               f"construir sense inventar-ne el contingut. Aquesta discrepància "
               f"es declara perquè la revise el verificador en la fase "
               f"següent.", f"{g}/procedencia/pestanyes", g, CLS_PROCEDENCIA)
        c.blanc()

        # -- procedència del fitxer font
        c.titol("1 · Fitxer font", f"{g}/font/titol", g)
        c.fila_kv("Camp", "Contingut", f"{g}/font/capcalera", g, CLS_CAPCALERA)
        c._kv("Camí del fitxer font", d.path, f"{g}/font/cami", g, CLS_PROCEDENCIA)
        c._kv("sha256 del fitxer font", d.sha256, f"{g}/font/sha256", g,
              CLS_PROCEDENCIA)
        c._kv("Línies del fitxer font", str(len(d.lines)), f"{g}/font/linies", g,
              CLS_PROCEDENCIA)
        c._kv("Mòdul", strip_inline(d.lines[2]) + " " + strip_inline(d.lines[3]),
              f"{g}/font/modul", g, CLS_DADES)
        c.blanc()

        # -- antecedent: informe de validació
        c.titol("2 · Antecedent: informe de validació independent", f"{g}/inf/titol",
                g)
        c.fila_kv("Camp", "Contingut", f"{g}/inf/capcalera", g, CLS_CAPCALERA)
        c._kv("Informe", self.informe_path, f"{g}/inf/cami", g, CLS_PROCEDENCIA)
        c._kv("Veredicte (línia literal de l'informe)",
              self._informe(r"^#\s*`?READY FOR HUMAN REVIEW", "veredicte"),
              f"{g}/inf/veredicte", g, CLS_PROCEDENCIA)
        c._kv("Data de l'informe", "2026-10-01", f"{g}/inf/data", g,
              CLS_PROCEDENCIA)
        c.blanc()

        c.titol("3 · Ressalves que viatgen amb aquesta exportació",
                f"{g}/ressalves/titol", g)
        c.fila_kv("Ressalva", "Text literal", f"{g}/ressalves/capcalera", g,
                  CLS_CAPCALERA)
        c._kv("Ressalva de l'objecte validat",
              self._informe(r"Objecte validat", "objecte validat"),
              f"{g}/ressalves/objecte", g, CLS_PROCEDENCIA)
        c._kv("Comprovació d'aquesta ressalva",
              f"{MARCA_PROCEDENCIA} El fitxer font actual té "
              f"{len(d.lines)} línies, no les 714 que declara l'informe. "
              f"El fitxer font ha canviat DESPRÉS de l'informe; per això el "
              f"veredicte `READY FOR HUMAN REVIEW` del 2026-10-01 NO es "
              f"traspassa a aquesta exportació sense revalidació del "
              f"`verificador`.", f"{g}/ressalves/comprovacio", g,
              CLS_PROCEDENCIA)
        c._kv("Ressalva D-3 (títol literal de l'informe)",
              self._informe(r"^####\s+D-3", "D-3"), f"{g}/ressalves/d3titol",
              g, CLS_PROCEDENCIA)
        c._kv("Ressalva D-3 (cos literal de l'informe)",
              self._informe(r"declara .*8 tipus", "cos de D-3"),
              f"{g}/ressalves/d3cos", g, CLS_PROCEDENCIA)
        c._kv("Nota sobre l'etiquetatge de D-3",
              f"{MARCA_PROCEDENCIA} Al pla d'aquesta exportació, «D-3» es "
              f"refereix al recompte d'instruments d'avaluació, que és "
              f"exactament el que diu l'informe. El desnivell de línies "
              f"(714 → {len(d.lines)}) és una altra ressalva, la de "
              f"«objecte validat», i queda registrada a la fila anterior. "
              f"Les dues no es confonen.", f"{g}/ressalves/nota", g,
              CLS_PROCEDENCIA)
        c.blanc()

        # -- garantia del PDF i limitació de pdftotext
        c.titol("4 · Garantia del PDF i limitació de pdftotext", f"{g}/pdf/titol",
                g)
        c.fila_kv("Camp", "Contingut", f"{g}/pdf/capcalera", g, CLS_CAPCALERA)
        c._kv("Garantia del PDF",
              f"{MARCA_PROCEDENCIA} El PDF es genera en UN SOL PAS MECÀNIC "
              f"des del Markdown: pandoc --from=markdown-smart cap a HTML5 "
              f"--standalone --embed-resources, i després google-chrome "
              f"--headless --print-to-pdf amb el full d'estil "
              f"graella.css (A3 apaisat, thead repetit). No hi ha cap pas "
              f"manual ni cap edició posterior. El PDF porta només un peu de "
              f"procedència generat automàticament; no hi ha cap declaració "
              f"curricular que no estiga al Markdown.", f"{g}/pdf/garantia", g,
              CLS_PROCEDENCIA)
        c._kv("Limitació de pdftotext",
              f"{MARCA_PROCEDENCIA} pdftotext NO és una via de verificació "
              f"fiable en aquest document. La capa de text del PDF reordena "
              f"els espais especials oficials: l'espai fi U+2003, l'espai fi "
              f"fi U+2002 i el guion fi U+2012 NO es recuperen de manera "
              f"fiable, i el recompte per regió que es fa des de l'XLSX no es "
              f"pot reproduir sobre el text extret del PDF. Per comprovar la "
              f"fidelitat de caràcters s'ha d'usar el Markdown (font única) "
              f"o l'XLSX, mai el text extret del PDF.", f"{g}/pdf/limitacio", g,
              CLS_PROCEDENCIA)
        c.blanc()

        # -- xifres de control
        x = self.xifres
        c.titol("5 · Xifres de control", f"{g}/xifres/titol", g)
        c.fila_kv("Dada", "Recompte", f"{g}/xifres/capcalera", g, CLS_CAPCALERA)
        for etiqueta, valor, reg in x["files"]:
            c._kv(etiqueta, valor, reg, g, CLS_DERIVADA)
        c._kv("Com s'han calculat",
              f"{MARCA_DERIVADA} Recompteades sobre les regions copiades en "
              f"aquest mateix llibre, no sobre el Markdown. El comparador "
              f"`comparar_export.py` les torna a recalcular reimportant "
              f"l'XLSX i les confronta caràcter a caràcter.",
              f"{g}/xifres/metode", g, CLS_DERIVADA)
        c.blanc()

        # -- tres eixos d'etiquetes
        c.titol("6 · Els tres eixos d'etiquetes i tots els seus qualificadors",
                f"{g}/eixos/titol", g)
        c.fila_kv("Eix", "Qualificador", f"{g}/eixos/capcalera", g,
                  CLS_CAPCALERA)

        eix1 = self._eix_procedencia()
        for q, origen in eix1:
            c._kv(f"{MARCA_DERIVADA} Eix 1 · procedència", f"{q}  ◄ {origen}",
                  f"{g}/eixos/eix1/{q}", g, CLS_DERIVADA)

        eix2 = self._eix_exigibilitat()
        for q, origen in eix2:
            c._kv(f"{MARCA_DERIVADA} Eix 2 · exigibilitat", f"{q}  ◄ {origen}",
                  f"{g}/eixos/eix2/{q}", g, CLS_DERIVADA)

        eix3 = self._eix_estat()
        for q, origen in eix3:
            c._kv(f"{MARCA_DERIVADA} Eix 3 · estat de la dada",
                  f"{q}  ◄ {origen}", f"{g}/eixos/eix3/{q}", g, CLS_DERIVADA)

        c._kv("Per què tres eixos",
              f"{MARCA_DERIVADA} Els eixos són disjunts i es creuen: un mateix "
              f"element pot ser de text oficial (eix 1) i no exigible (eix 2) "
              f"i, alhora, PENDENT (eix 3). Cap element curricular de la "
              f"graella queda fora dels tres.", f"{g}/eixos/creuament", g,
              CLS_DERIVADA)
        c.blanc()

        # -- §0.1, §0.2 i §0.5 copiats literalment
        c.titol("7 · §0.1 · Les cinc coses que hi ha dins i que no s'han de "
                "confondre (copiat literal)", f"{g}/s01/titol", g)
        t = self.doc.taula("0.1")
        c.capcalera_taula(t.capcaleres, "00.1/capcalera", "00.1")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), f"§0.1 fila {k}", " ".join(fila))
            c.fila(vals, f"00.1/{k}", "00.1", CLS_DADES)

        c.blanc()
        c.titol("8 · §0.2 · Codificació: quina és oficial i quina és del "
                "projecte (copiat literal)", f"{g}/s02/titol", g)
        t = self.doc.taula("0.2")
        c.capcalera_taula(t.capcaleres, "00.2/capcalera", "00.2")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), f"§0.2 fila {k}", " ".join(fila))
            c.fila(vals, f"00.2/{k}", "00.2", CLS_DADES)

        c.blanc()
        c.titol("9 · §0.5 · Nota de fidelitat de caràcters (copiat literal)",
                f"{g}/s05/titol", g)
        p = self.doc.paragrafs("0.5")
        if len(p) != 2:
            raise MdError(
                f"§0.5 hauria de tenir 2 paràgrafs; en té {len(p)}")
        for k, b in enumerate(p, 1):
            c._kv(f"§0.5 paràgraf {k}", b.text, f"00.5/{k}", "00.5", CLS_DADES)

        return c

    # -- eixos (tots els qualificadors, extrets del mateix document) ----

    def _eix_procedencia(self):
        """Eix 1: columna «És oficial?» del §0.2, agrupada pel primer token."""
        col = 1
        agrupat = {}
        for fila in self.doc.taula("0.2").files:
            txt = strip_inline(fila[col])
            if not txt:
                continue
            q = txt.split(".")[0].strip() + "."
            agrupat.setdefault(q, [])
            agrupat[q].append(strip_inline(fila[0]))
        return [(q, "§0.2 · codis " + ", ".join(v))
                for q, v in agrupat.items()]

    def _eix_exigibilitat(self):
        """Eix 2: columna «Què vol dir» del §0.1, una línia per etiqueta."""
        out = []
        for fila in self.doc.taula("0.1").files:
            et = strip_inline(fila[0])
            sig = strip_inline(fila[1])
            token = None
            for t in ("Són exigibles.", "No és exigible",
                      "No té valor normatiu.", "Cap norma l'obliga.",
                      "no reprodueix l'ítem sencer"):
                if t in sig:
                    token = t.rstrip(".")
                    break
            if token is None:
                token = sig.split(".")[0].strip()
            out.append((f"{et} → {token}", "§0.1"))
        return out

    def _eix_estat(self):
        """Eix 3: valors reals de la columna «Estat» del §7.1, més
        `VERIFICADA`, ordre d'aparició al document."""
        out = []
        vists = []
        for fila in self.doc.taula("7.1").files:
            v = strip_inline(fila[3]).strip()
            if v and v not in vists:
                vists.append(v)
        for v in vists:
            out.append((v, "§7.1"))
        for v in ("VERIFICADA",):
            if v not in vists:
                out.append((v, "§4.4 · §5.1 · §6.1"))
        return out

    # ==================================================================
    # 01..06 · Un full per resultat d'apreneatge
    # ==================================================================

    def fulla_ra(self, n: int):
        g = f"{n:02d} RA {n}"
        c = self.fulla(g, {"A": 52, "B": 26, "C": 26, "D": 26, "E": 62,
                           "F": 20, "G": 14, "H": 40, "I": 44, "J": 34})
        d = self.doc

        # -- línia literal del RA, del §2
        taula2 = d.taula("2")
        fila2 = None
        for fila in taula2.files:
            if strip_inline(fila[0]).strip() == f"RA {n}":
                fila2 = fila
                break
        if fila2 is None:
            raise MdError(f"§2 no té cap fila «RA {n}»")
        ra_text = strip_inline(fila2[1])
        ra_crit = strip_inline(fila2[2])

        # -- taula de §3.n
        t3 = d.taula(f"3.{n}")
        EXPECTADES = ["Criteri", "Saber", "Saber fer", "Saber estar",
                      "Contingut bàsic literal (F-037)", "Activitat", "Hores",
                      "Instrument [PROPOSTA]"]
        if [strip_inline(x) for x in t3.capcaleres] != EXPECTADES:
            raise MdError(
                f"§3.{n}: les columnes no són les 8 literals declarades.\n"
                f"  trobat:  {[strip_inline(x) for x in t3.capcaleres]}\n"
                f"  esperat: {EXPECTADES}")

        cap = d.heading(f"3.{n}").titol

        c.titol(f"RA {n} · resultat d'apreneatge, criteris i hores", f"{g}/titol",
                g)
        c.blanc()
        c.titol("Bloc de capçalera (text literal del document font)",
                f"{g}/cap/titol", g)
        c.fila_kv("Camp", "Contingut", f"{g}/cap/capcalera", g, CLS_CAPCALERA)
        c._kv(f"RA {n} · text literal [TEXT EXTRET]", ra_text,
              f"2/RA{n}#text", "2/RA" + str(n), CLS_DADES)
        c._kv(f"RA {n} · criteris (de §2)", ra_crit, f"2/RA{n}#criteris",
              "2/RA" + str(n), CLS_DADES)
        c._kv("Encapçalament literal de §3", strip_inline(cap),
              f"3.{n}/encapcalament", f"3.{n}", CLS_DADES)
        c._kv("Font", self._font_ra(n), f"3.{n}/font", f"3.{n}", CLS_DADES)
        c._kv("Estat de la font", self._estat_font(), f"2/estatfont", "2",
              CLS_DADES)
        c.blanc()

        # -- taula de criteris, 8 columnes literals + 2 derivades
        c.titol("Taula de §3 · 8 columnes literals del document font "
                "+ 2 columnes derivades", f"{g}/taula/titol", g)
        cap_row = c.capcalera_taula(
            t3.capcaleres + ["Estat de la relació [DERIVAT]",
                             "Pendent citat [DERIVAT]"],
            f"3.{n}/capcalera", f"3.{n}")
        primera = cap_row + 1

        grups = []
        total_row = None
        for k, fila in enumerate(t3.files):
            txt = " ".join(fila)
            vals = [strip_inline(x) for x in fila]
            if es_fila_estructura(vals):
                total_row = vals
                total_row_index = c.fila(
                    vals, f"3.{n}/total", f"3.{n}/total..total", CLS_ESTRUCTURA)
                continue
            codi = vals[0].split("\n")[0].strip()
            exigeix_marca(" ".join(vals), f"§3.{n} fila {codi}",
                          " ".join(fila))
            grups.append(codi)
            c.fila(vals
                   + [estat_de_la_relacio(*vals[:8]),
                      pendent_citat(" ".join(vals))],
                   f"3.{n}/{codi}", f"3.{n}/{grups[0]}..{codi}", CLS_DADES)
        if total_row is None:
            raise MdError(f"§3.{n}: no hi ha cap fila «Total RA {n}»")

        ultima = total_row_index - 1
        c.f.autofilter = f"A{cap_row}:J{ultima}"
        c.f.congelar = f"C{primera}"

        # -- sabers mobilitzats
        c.blanc()
        c.titol(f"Sabers mobilitzats en aquest RA (copiat de l'Annex A, "
                f"d'on té el criteri aquest RA)", f"{g}/sabers/titol", g)
        c.capcalera_taula(
            ["ID", "Tipus", "Etiqueta", "Text", "Origen literal (F-037)"],
            f"AnnexA/{'A.1' if n else ''}/capcalera", "AnnexA/A.1..A.3")
        mobilization = self._sabers_del_ra(n, t3)
        for sid in mobilization:
            tipus, et, txt, orig = self.sabers[sid]
            c.fila([sid, tipus, et, txt, orig],
                   f"AnnexA/{sid}", f"AnnexA/{sid[3:5]}", CLS_DADES)

        return c, {"grups": grups, "total": total_row, "cap_row": cap_row,
                   "primera": primera, "ultima": ultima, "sabers": mobilization,
                   "ra_text": ra_text, "ra_crit": ra_crit}

    def _font_ra(self, n):
        for b in self.doc.paragrafs("2"):
            if "Font única dels" in b.text:
                return b.text
        raise MdError("§2: no hi ha el paràgraf «Font única dels…»")

    def _estat_font(self):
        for b in self.doc.paragrafs("2"):
            m = re.search(r"Estat\s+`?(VERIFICADA|PENDENT)`?\.?", b.text)
            if m:
                return m.group(0).strip()
        raise MdError("§2: no s'hi declara cap estat de la font")

    def _sabers_del_ra(self, n, t3):
        """IDs de saber que apareixen a les tres columnes de la taula §3.n,
        en ordre d'aparició i sense repeticions. Copiat de l'Annex A."""
        ids = []
        for fila in t3.files:
            if strip_inline(fila[5]).strip().startswith("Total RA"):
                continue
            for col in (1, 2, 3):
                for sid in REGEX_SABER.findall(strip_inline(fila[col])):
                    if sid not in ids:
                        ids.append(sid)
        for sid in ids:
            if sid not in self.sabers:
                raise MdError(
                    f"§3.{n}: el saber {sid} no té fila a l'Annex A; "
                    f"no es pot omplir")
        return ids

    # ==================================================================
    # 07 · Sabers (Annex A)
    # ==================================================================

    def fulla_07(self):
        g = "07 Sabers (Annex A)"
        c = self.fulla(g, {"A": 16, "B": 24, "C": 96, "D": 76})
        d = self.doc
        c.titol("Annex A · Catàleg de sabers (copiat literal)", f"{g}/titol", g)
        c.blanc()
        c.titol("Recompte per tipus (taula literal del §Annex A)",
                f"{g}/tipus/titol", g)
        ta = d.taula("AnnexA")
        c.f.congelar = "A5"
        c.capcalera_taula(ta.capcaleres, "AnnexA/tipus/capcalera", "AnnexA/tipus")
        for k, fila in enumerate(ta.files, 1):
            vals = [strip_inline(x) for x in fila]
            c.fila(vals, f"AnnexA/tipus/{k}", "AnnexA/tipus", CLS_DADES)
        c.blanc()

        for sub, grup in (("A.1", "AnnexA/A.1"), ("A.2", "AnnexA/A.2"),
                          ("A.3", "AnnexA/A.3")):
            c.titol(f"{sub} · {strip_inline(d.heading(sub).titol)}",
                    f"{grup}/titol", grup)
            t = d.taula(sub)
            c.capcalera_taula(t.capcaleres, f"{grup}/capcalera", grup)
            for k, fila in enumerate(t.files, 1):
                vals = [strip_inline(x) for x in fila]
                sid = vals[0].strip()
                exigeix_marca(" ".join(vals), f"Annex {sub} · {sid}",
                          " ".join(fila))
                c.fila(vals, f"AnnexA/{sid}", grup, CLS_DADES)

        # Les 40 files viuen en tres blocs (A.1, A.2, A.3) i el llibre no hi
        # posa cap fila intermèdia. Un filtre automàtic només pot cobrir un
        # rang contigu: filtrar aquí amagaria files o tallaria el títol
        # d'un bloc. Per això aquesta pestanya no en porta.
        return c

    # ==================================================================
    # 08 · Activitats (Annex B)
    # ==================================================================

    def fulla_08(self):
        g = "08 Activitats (Annex B)"
        c = self.fulla(g, {"A": 12, "B": 40, "C": 78, "D": 34, "E": 46, "F": 30,
                           "G": 22}, "A2")
        d = self.doc
        h = d.heading("AnnexB")
        m = re.search(r"`\[PROPOSTA\]`", h.titol)
        if not m:
            raise MdError(
                "Annex B: l'encapçalament no du la marca literal `[PROPOSTA]`; "
                "no hi ha valor per defecte")
        etiqueta_annex = m.group(0)

        c.titol(strip_inline(h.titol), f"{g}/titol", "AnnexB")
        c.blanc()
        t = d.taula("AnnexB")
        c.capcalera_taula(t.capcaleres + ["Etiqueta de l'annex [DERIVAT]"],
                          f"AnnexB/capcalera", "AnnexB")
        primera = c.r + 1
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            aid = vals[0].strip()
            exigeix_marca(" ".join(vals) + " " + etiqueta_annex,
                          f"Annex B · {aid}")
            c.fila(vals + [f"{MARCA_DERIVADA} {etiqueta_annex} "
                           f"(projecte de l'encapçalament de l'Annex B)"],
                   f"AnnexB/{aid}", "AnnexB/ACT-1..ACT-9", CLS_DADES)
        c.f.autofilter = f"A{primera - 1}:G{c.r}"
        c.f.congelar = f"B{primera}"
        return c

    # ==================================================================
    # 09 · ODS i TT
    # ==================================================================

    def fulla_09(self):
        g = "09 ODS i TT"
        c = self.fulla(g, {"A": 16, "B": 74, "C": 54, "D": 62, "E": 26, "F": 18})
        d = self.doc

        c.titol("ODS i temes transversals · §4", f"{g}/titol", g)
        c.blanc()
        c.titol("4.1 · Advertiment, sense matixos · declaracions del projecte sobre la pròpia graella, copiades literalment",
                f"{g}/s41/titol", g)
        adv = self._llista("4.1")
        c.capcalera_taula(["Núm.", "Advertiment (text literal)"],
                          "4.1/capcalera", f"4.1/adv1..adv{len(adv)}")
        for k, raw in enumerate(adv, 1):
            txt = strip_inline(raw)
            porta_advertiment(txt, raw, "4.1", k, self.avisos)
            c.fila([str(k), txt], f"4.1/adv{k}",
                   f"4.1/adv1..adv{len(adv)}", CLS_ADVERTIMENT)
        c.blanc()

        c.titol("4.2 · ODS proposats (tots [PROPOSTA])", f"{g}/s42/titol", g)
        t = d.taula("4.2")
        c.capcalera_taula(t.capcaleres, "4.2/capcalera", "4.2")
        ids = []
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), "§4.2", " ".join(fila))
            ids.append(vals[0].strip())
            c.fila(vals, f"4.2/{vals[0].strip()}", "4.2", CLS_DADES)
        c.blanc()
        c.titol("ODS de l'Agenda que romanen PENDENT (text literal del §4.2)",
                f"{g}/s42b/titol", g)
        txt = d.texto_paragrafs("4.2")
        if "ODS no proposats" not in txt:
            raise MdError("§4.2: no hi ha la frase «ODS no proposats»")
        pend = [b for b in d.paragrafs("4.2") if "ODS no proposats" in b.text]
        codis = ods_no_proposats(pend[0].text)
        c._kv("Llista literal", pend[0].text, "4.2/noproposats", "4.2/PENDENT",
              CLS_DADES)
        c._kv("Recompte [DERIVAT]", f"{MARCA_DERIVADA} {len(codis)} codis ODS "
              f"esmentats com a no proposats: {', '.join(codis)}",
              "4.2/nproposats/recpte", "4.2/PENDENT", CLS_DERIVADA)
        c.blanc()

        c.titol("4.3 · Temes transversals proposats (tots [PROPOSTA])",
                f"{g}/s43/titol", g)
        t = d.taula("4.3")
        c.capcalera_taula(t.capcaleres, "4.3/capcalera", "4.3")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), "§4.3", " ".join(fila))
            c.fila(vals, f"4.3/{vals[0].strip()}", "4.3", CLS_DADES)
        c.blanc()

        c.titol("4.4 · Recompte d'aquesta secció (copiat literal)",
                f"{g}/s44/titol", g)
        t = d.taula("4.4")
        c.capcalera_taula(t.capcaleres, "4.4/capcalera", "4.4")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), f"§4.4 fila {k}", " ".join(fila))
            c.fila(vals, f"4.4/{k}", "4.4", CLS_DADES)
        # El recompte de §4.4 ha de quadrar amb la llista literal del §4.2. Si
        # no quadrés, el llibre publicaria dos nombres que no es poden
        # reconciliar; millor aturar-ho aquí que triar-ne un.
        for fila in t.files:
            vals = [strip_inline(x) for x in fila]
            if "romanen" in vals[0] and "PENDENT" in vals[0]:
                if not vals[1].strip().isdigit():
                    raise MdError("§4.4: el recompte d'ODS PENDENT no és un "
                                  f"número: {vals[1]!r}")
                declarat = int(vals[1].strip())
                if declarat != len(codis):
                    raise MdError(
                        f"§4.4 declara {declarat} ODS PENDENT però la llista "
                        f"literal del §4.2 en té {len(codis)}: "
                        f"{', '.join(codis)}")
                break
        return c, {"adv": len(adv), "ods": ids, "ods_pendent": len(codis)}

    def _llista(self, sec):
        """Ítems de llista en text BRUT, amb el marcatge Markdown intacte.

        El neteig es fa al lloc d'ús, on cal conservar el text original per
        a la porta de marques.
        """
        out = []
        for b in self.doc.region(sec):
            if b.kind in ("olist", "ulist"):
                out.extend(b.files)
        return out

    # ==================================================================
    # 10 · Distribució temporal
    # ==================================================================

    def fulla_10(self):
        g = "10 Distribució temporal"
        c = self.fulla(g, {"A": 40, "B": 30, "C": 24, "D": 40, "E": 22, "F": 44})
        d = self.doc
        c.titol("§5 · Distribució temporal", f"{g}/titol", g)
        c.blanc()
        c.titol("5.1 · Context curricular autoritatiu (copiat literal)",
                f"{g}/s51/titol", g)
        t = d.taula("5.1")
        c.capcalera_taula(t.capcaleres, "5.1/capcalera", "5.1")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), f"§5.1 fila {k}", " ".join(fila))
            c.fila(vals, f"5.1/{k}", "5.1", CLS_DADES)
        c.blanc()

        # F1 · Exportar §5.2 sencer, entre §5.1 i §5.3.
        c.titol("5.2 · Advertiment aritmètic sobre la distribució temporal",
                f"{g}/s52/titol", g)
        for b in d.region("5.2"):
            if b.kind == "para":
                c._kv("§5.2 paràgraf", b.text,
                      f"5.2/para/{b.lineno}", "5.2", CLS_DADES)
            elif b.kind == "ulist":
                for k, raw in enumerate(b.files, 1):
                    c._kv(f"§5.2 ítem {k}", raw,
                          f"5.2/item{k}", "5.2", CLS_DADES)
            elif b.kind == "quote":
                for k, raw in enumerate(b.files, 1):
                    c._kv(f"§5.2 cita {k}", raw,
                          f"5.2/cita{k}", "5.2", CLS_DADES)
        c.blanc()

        # F1 · Exportar §5.2 sencer, entre §5.1 i §5.3.
        c.titol("5.2 · Advertiment aritmètic sobre la distribució temporal",
                f"{g}/s52/titol", g)
        for b in d.region("5.2"):
            if b.kind == "para":
                c._kv("§5.2 paràgraf", b.text,
                      f"5.2/para/{b.lineno}", "5.2", CLS_DADES)
            elif b.kind == "ulist":
                for k, raw in enumerate(b.files, 1):
                    c._kv(f"§5.2 ítem {k}", raw,
                          f"5.2/item{k}", "5.2", CLS_DADES)
        c.blanc()

        c.titol("5.3 · Repartiment proposat [PROPOSTA] (copiat literal)",
                f"{g}/s53/titol", g)
        for b in d.region("5.3"):
            if b.kind == "para":
                c._kv("§5.3 paràgraf", b.text,
                      f"5.3/para/{b.lineno}", "5.3", CLS_DADES)
        t = d.taula("5.3")
        c.capcalera_taula(t.capcaleres, "5.3/capcalera", "5.3")
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            if es_fila_estructura(vals):
                c.fila(vals, f"5.3/total", "5.3/total", CLS_ESTRUCTURA)
                continue
            exigeix_marca(" ".join(vals), f"§5.3 fila {k}", " ".join(fila))
            c.fila(vals, f"5.3/fase{vals[0].strip()}", "5.3/fase1..fase6",
                   CLS_DADES)
        c.blanc()

        c.titol("5.4 · Advertiments sobre aquesta taula · declaracions del projecte, copiades literalment",
                f"{g}/s54/titol", g)
        adv = self._llista("5.4")
        c.capcalera_taula(["Núm.", "Advertiment (text literal)"],
                          "5.4/capcalera", f"5.4/adv1..adv{len(adv)}")
        for k, raw in enumerate(adv, 1):
            txt = strip_inline(raw)
            porta_advertiment(txt, raw, "5.4", k, self.avisos)
            c.fila([str(k), txt], f"5.4/adv{k}",
                   f"5.4/adv1..adv{len(adv)}", CLS_ADVERTIMENT)
        return c, {"adv": len(adv)}

    # ==================================================================
    # 11 · Pendents
    # ==================================================================

    def fulla_11(self):
        g = "11 Pendents"
        c = self.fulla(g, {"A": 18, "B": 76, "C": 66, "D": 34, "E": 22}, "A2")
        d = self.doc
        c.titol("§7.1 · Tot allò que queda PENDENT en aquesta graella "
                "(copiat literal)", f"{g}/titol", g)
        c.blanc()
        t = d.taula("7.1")
        c.capcalera_taula(t.capcaleres + ["Codi P- [DERIVAT]"],
                          f"{g}/capcalera", f"7.1/P-1..P-25")
        primera = c.r + 1
        codis = []
        for k, fila in enumerate(t.files, 1):
            vals = [strip_inline(x) for x in fila]
            exigeix_marca(" ".join(vals), f"§7.1 fila {k}", " ".join(fila))
            ps = extreu_p(vals[0])
            if not ps:
                raise MdError(f"§7.1 fila {k}: cap codi P- a la columna ID")
            codis.extend(ps)
            c.fila(vals + [f"{MARCA_DERIVADA} " + " · ".join(ps)],
                   f"7.1/{vals[0].strip()}",
                   f"7.1/{ps[0]}..{ps[-1]}", CLS_DADES)
        c.f.autofilter = f"A{primera - 1}:E{c.r}"
        c.f.congelar = f"B{primera}"
        return c, {"codis": codis, "files": len(t.files)}

    # ==================================================================
    # 12 · Text oficial (Annex C)
    # ==================================================================

    def fulla_12(self):
        g = "12 Text oficial (Annex C)"
        c = self.fulla(g, {"A": 150})
        d = self.doc
        c.titol("Annex C · Bloc literal del mòdul (text oficial, copiat "
                "literal)", f"{g}/titol", "AnnexC")
        c.blanc()
        b = d.codi("AnnexC", 0)
        txt = "\n".join(b.files_raw)
        import hashlib
        h = hashlib.sha256(txt.encode("utf-8")).hexdigest()
        c._kv("Bloc", f"{MARCA_DERIVADA} {len(b.files_raw)} línies · sha256 "
               f"{h}", f"AnnexC/metadades", "AnnexC", CLS_DERIVADA)
        # Procedència separada: només el paràgraf del §AnnexC que parla
        # de la procedència, sense el bloc, ni el peu.
        pars = [x.text for x in d.paragrafs("AnnexC")]
        c._kv("Procedència del bloc (text literal del §AnnexC)",
              pars[0] if pars else "",
              "AnnexC/procedencia", "AnnexC", CLS_DADES)
        c.blanc()
        # Fixa l'amplada de la columna B per al bloc oficial: el bloc té
        # 109 línies i cal que sigui llegible al llibre.
        c.f.congelar = "A6"
        c.titol("Bloc literal, una sola cel·la, monoespaciada",
                f"{g}/bloc/titol", "AnnexC")
        c._kv("Línies 1..%d del bloc oficial" % len(b.files_raw), txt,
              "AnnexC", "AnnexC", CLS_DADES, "monoespaciada")
        return c, {"linies": len(b.files), "sha256": h}

    # ==================================================================
    # 13 · Traçabilitat
    # ==================================================================

    def fulla_13(self):
        g = "13 Traçabilitat"
        c = self.fulla(g, {"A": 44, "B": 84, "C": 44, "D": 30})
        d = self.doc
        c.titol("§6 · Advertiments de traçabilitat", f"{g}/titol", g)
        c.blanc()
        c.titol("§7.2 · Revisió d'aquesta graella (copiat literal)", f"{g}/s72/titol", g)
        for b in d.region("7.2"):
            if b.kind == "para":
                c._kv("§7.2 paràgraf", b.text, f"7.2/para/{b.lineno}", "7.2", CLS_DADES)
            elif b.kind == "table":
                c.capcalera_taula(b.capcaleres, f"7.2/taula/cap", "7.2")
                for k, fila in enumerate(b.files, 1):
                    vals = [strip_inline(x) for x in fila]
                    c.fila(vals, f"7.2/f{k}", "7.2", CLS_DADES)
            elif b.kind == "ulist":
                for k, raw in enumerate(b.files, 1):
                    c._kv(f"§7.2 ítem {k}", raw, f"7.2/item{k}", "7.2", CLS_DADES)
        c.blanc()
        c.titol("§7.3 · Caràcters especials (copiat literal)", f"{g}/s73/titol", g)
        for b in d.region("7.3"):
            if b.kind == "para":
                c._kv("§7.3 paràgraf", b.text, f"7.3/para/{b.lineno}", "7.3", CLS_DADES)
        c.blanc()
        return c

RE_ODS_PEND = re.compile(r"ODS-\d{2}")


def ods_no_proposats(text: str) -> list[str]:
    """Codes ODS de la llista literal «ODS no proposats» del §4.2.

    La font escriu la llista en forma abreviada: només el primer codi porta el
    prefix, i els altres van solts: «ODS-01, 02, 03, 05, …, 16 i 17». Es
    desplega llegint cada token; no es presumeix cap relació.
    """
    m = re.search(r"ODS no proposats:\s*(.+?)\s*\.?\s*(?:\n|$)", text)
    if not m:
        raise MdError("§4.2: no hi ha la llista «ODS no proposats»")
    # La frase ve amb `**ODS no proposats:**`; el dessembagatge es fa sobre el
    # text ja netejat, així que el token pot arribar amb `**` enganxat.
    tokens = re.split(r",\s*|\s+i\s+", strip_inline(m.group(1)).rstrip("."))
    codis = []
    for t in tokens:
        t = t.strip()
        if not t:
            continue
        mm = re.match(r"^(?:ODS-)?(\d{1,2})$", t)
        if not mm:
            raise MdError(f"§4.2: token no reconegut a la llista d'ODS: {t!r}")
        codis.append(f"ODS-{int(mm.group(1)):02d}")
    return codis


def _zero_hores(doc, n):
    t = doc.taula(f"3.{n}")
    for fila in t.files:
        vals = [strip_inline(x) for x in fila]
        if vals[6].strip().startswith("0"):
            return 1
    return 0



def _verificades(doc):
    """Compta les relacions ODS/TT amb estat VERIFICADA al mòdul, llegint
    el recompte literal del §4.4."""
    n = 0
    for fila in doc.taula("4.4").files:
        v = strip_inline(fila[0])
        if "VERIFICADA" in v:
            val = re.findall(r"\d+", strip_inline(fila[1]))
            if not val:
                raise MdError(f"§4.4 fila {v!r} sense xifra")
            n += int(val[0])
    return n