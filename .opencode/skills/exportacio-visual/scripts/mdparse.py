#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Analitzador de Markdown per a l'exportació visual de graelles curriculars.

Conté només codi de lectura i mecànic:

* llegeix un fitxer Markdown i el divideix en blocs identificats
  (encapçalament, taula, codi, paràgraf, citació, llista, separador);
* situa regions mitjançant el número d'encapçalament (`3.1`, `AnnexA`, …);
* treu el marcatge en línia **sense reescriure el text**: només desfà
  l'envoltament Markdown (`**`, `*`, `` ` ``, `<br>`, `\|`) i conserva
  intactes tots els caràcters del document original, inclosos `U+2003`,
  `U+2012`, `U+2002`, `U+2423`, `U+2013`, `U+2014`, `«»` i les etiquetes
  entre corxets.

No genera, completa ni infereix cap contingut curricular. Si una regió
no existeix o no té la forma esperada, s'atura amb codi d'error.
"""

from __future__ import annotations

import hashlib
import re
import sys

# --------------------------------------------------------------------------
# Errors
# --------------------------------------------------------------------------


class MdError(Exception):
    """Error de lectura o de forma del Markdown. Atura l'exportació."""


# --------------------------------------------------------------------------
# Marques reconeixibles (porta de qualitat, línia vermella 3 del pla)
# --------------------------------------------------------------------------

#: Etiquetes declarades al §0.1 i §0.2 del propi document font.
MARQUES_ETIQUETES = (
    "[TEXT EXTRET (parcial)]",
    "[TEXT EXTRET]",
    "[RESUM]",
    "[INTERPRETACIÓ]",
    "[PROPOSTA]",
)

#: Estat de dada, literal del document font.
MARQUES_ESTAT = ("PENDENT", "RESOLT", "VERIFICADA")

#: Marca de «no intervé» del §3.0.
MARQUES_NO_INTERV = (":—",)

#: Marca de cobertura parcial del §3.0.
MARQUES_RESERVA = ("amb reserva",)

#: Codi literal del sistema de codificació declarat al §0.2. La mera
#: presència del codi és marca literal: acredita que la fila parla d'un
#: element del catàleg i no d'un valor per defecte.
RE_CODIS = re.compile(
    r"SB-\d{4}-\d{2}"          # SB-3016-nn
    r"|ACT-\d+"                # ACT-n
    r"|CB b\d+\.i\d+"          # CB b#.i#
    r"|OP v\d+"                # OP v#
    r"|P-\d+"                  # P-n
    r"|V-3016-[A-Z]+"          # V-3016-ODS / V-3016-TT
    r"|ODS-\d+"                # ODS-nn
    r"|TT-\d+"                 # TT-nnn
    r"|I-\d+"                  # I-n
    r"|F-\d{3}"                # F-032, F-037… codi de font del registre
    r"|§\d+(?:\.\d+)*"         # remissió literal a un apartat del document
    r"|SB-\d{2}\b"             # abreviatures SB-01…SB-40 de l'Annex B
    r"|\b[1-6][a-h]\b"         # codi compost criteri
    r"|\bRA [1-9]\b"           # resultat d'aprenentatge
    r"|D-\d+"                  # defecte de l'informe
)

#: Marques literals de fila d'estructura (capçalera de taula, fila TOTAL).
#: No són dades curriculars; la seva existència es detecta pel text.
RE_ESTRUCTURA = re.compile(
    r"^\s*Total RA \d+\s*$" r"|^Criteri\s*\|" r"|^\|?\s*ID\s*\|"
)


#: Cita literal entre crases: el text entre ` i ` es transcriu tal qual de
#: la font, i la seva presència és marca literal de la fila. Serveix per a
#: les files d'advertiment (§4.1, §5.4, §6.5), que no afirmen cap valor
#: curricular sinó que declaren què s'ha comprovat i on.
RE_CITA_LITERAL = re.compile(r"`[^`\n]+`")


def marques_reconeixibles(text: str, raw: str | None = None) -> list[str]:
    """Retorna les marques reconeixibles presents a `text`, sense ordenar.

    `raw` és el text amb el marcatge Markdown, si es disposa del original:
    es consulta per detectar les cites literals entre crases.
    """
    trobades: list[str] = []
    for m in MARQUES_ETIQUETES + MARQUES_ESTAT + MARQUES_NO_INTERV + MARQUES_RESERVA:
        if m in text and m not in trobades:
            trobades.append(m)
    if not trobades:
        codis = sorted(set(RE_CODIS.findall(text)))
        if codis:
            trobades.append("codi literal: " + ", ".join(codis[:6]))
    if not trobades and raw:
        cites = RE_CITA_LITERAL.findall(raw)
        if cites:
            trobades.append("cita literal: " + ", ".join(c[:40] for c in cites[:4]))
    return trobades


def fila_te_marca(text: str, raw: str | None = None) -> bool:
    return bool(marques_reconeixibles(text, raw))


# --------------------------------------------------------------------------
# Blocs
# --------------------------------------------------------------------------


class Bloc:
    """Un bloc del Markdown amb la seva posició al fitxer (1-based)."""

    __slots__ = ("kind", "lineno", "nivell", "num", "titol", "capcaleres",
                 "files", "files_raw", "text", "lang")

    def __init__(self, kind, lineno, nivell=0, num="", titol="", capcaleres=None,
                 files=None, text="", lang=""):
        self.kind = kind          # heading|table|code|para|quote|olist|ulist|hrule
        self.lineno = lineno      # línia inicial, 1-based
        self.nivell = nivell      # nivell d'encapçalament (0 si no n'és)
        self.num = num            # '3.1', 'AnnexA', ...
        self.titol = titol
        self.capcaleres = capcaleres or []
        self.files = files or []          # files ja netes (taula, llista)
        self.files_raw = []               # línies de codi en brut
        self.text = text
        self.lang = lang

    def __repr__(self):  # pragma: no cover
        return f"<Bloc {self.kind} L{self.lineno} {self.num!r}>"


# --------------------------------------------------------------------------
# Desmarcatge en línia (mecànic, no editorial)
# --------------------------------------------------------------------------

RE_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
RE_NUM_HEADING = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+(.*)$")
# Subapartats d'annex: `A.1 saber — coneixement (18)`, `B.2 ...`
RE_SUBANNEX_HEADING = re.compile(r"^([A-Z]\.\d+)\s+(.*)$")
RE_ANNEX_HEADING = re.compile(r"^Annex\s+([A-Z])\b", re.IGNORECASE)
RE_HRULE = re.compile(r"^\s*(-{3,}|\*{3,}|_{3,})\s*$")
RE_TABLE_SEP = re.compile(r"^\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*$")
RE_OLIST = re.compile(r"^(\d+)\.\s+(.*)$")
RE_ULIST = re.compile(r"^[-*]\s+(.*)$")


def strip_inline(s: str) -> str:
    r"""Desfà l'envoltament Markdown conservant el text interior literal.

    Es transformen només:
      <br> i <br/>  -> salt de línia
      crases        -> res
      ** i __       -> res
      *cursiva*     -> cursiva
      barra invertida escapada -> barra

    No es toca cap altre caràcter. Els espais especials oficials
    (U+2002, U+2003), el guion U+2012, les comilles angulars,
    els guions U+2013 i U+2014 i les etiquetes entre corxets
    hi sobreviuen intactes.
    """
    if not s:
        return s
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.IGNORECASE)
    s = s.replace("\\|", "|")
    s = s.replace("`", "")
    s = s.replace("**", "").replace("__", "")
    # cursiva: un únic * que envolta text sense cap altre *
    s = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"\1", s)
    return s


def _split_taula(linia: str) -> list[str]:
    """Divideix una fila de taula en cel·les, sense_DESCARTAR res."""
    s = linia.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|") and not s.endswith("\\|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def neteja(text: str) -> str:
    """Aplica `strip_inline` i recorda què s'ha desfet (per a l'informe)."""
    return strip_inline(text)


# --------------------------------------------------------------------------
# Analitzador
# --------------------------------------------------------------------------


class Document:
    def __init__(self, path):
        self.path = path
        with open(path, "rb") as fh:
            self.bytes = fh.read()
        self.sha256 = hashlib.sha256(self.bytes).hexdigest()
        self.text = self.bytes.decode("utf-8")
        # El fitxer pot no acabar en salt de línia; `split` el conserva igual.
        self.lines = self.text.split("\n")
        self.blocks = self._analitza()
        self._index = {}
        for b in self.blocks:
            if b.kind == "heading" and b.num:
                self._index[b.num] = b

    # -- analitzi ---------------------------------------------------------

    def _analitza(self) -> list[Bloc]:
        L = self.lines
        blocs: list[Bloc] = []
        i = 0
        n = len(L)
        while i < n:
            lin = L[i]
            if not lin.strip():
                i += 1
                continue

            m = RE_HEADING.match(lin)
            if m:
                niv = len(m.group(1))
                cos = m.group(2).strip()
                num, titol = "", cos
                mn = RE_NUM_HEADING.match(cos)
                ms = RE_SUBANNEX_HEADING.match(cos)
                if mn:
                    num = mn.group(1)
                    titol = mn.group(2).strip()
                elif ms:
                    num = ms.group(1)
                    titol = ms.group(2).strip()
                else:
                    ma = RE_ANNEX_HEADING.match(cos)
                    if ma:
                        num = "Annex" + ma.group(1).upper()
                        titol = cos
                blocs.append(Bloc("heading", i + 1, niv, num, titol))
                i += 1
                continue

            if RE_HRULE.match(lin):
                blocs.append(Bloc("hrule", i + 1))
                i += 1
                continue

            # codi encerclat
            if lin.lstrip().startswith("```"):
                lang = lin.lstrip()[3:].strip()
                j = i + 1
                cos = []
                while j < n and not L[j].strip().startswith("```"):
                    cos.append(L[j])
                    j += 1
                if j >= n:
                    raise MdError(
                        f"{self.path}: codi sense tancar que comença a L{i+1}")
                b = Bloc("code", i + 1, lang=lang)
                b.files_raw = list(cos)
                b.files = cos
                blocs.append(b)
                i = j + 1
                continue

            # taula
            if lin.lstrip().startswith("|"):
                j = i
                while j < n and L[j].lstrip().startswith("|"):
                    j += 1
                if j - i < 2:
                    raise MdError(f"{self.path}: fila de taula solta a L{i+1}")
                if not RE_TABLE_SEP.match(L[i + 1]):
                    raise MdError(
                        f"{self.path}: taula sense fila separadora a L{i+1}")
                cap = _split_taula(L[i])
                files = []
                for k in range(i + 2, j):
                    files.append(_split_taula(L[k]))
                b = Bloc("table", i + 1)
                b.capcaleres = cap
                b.files = files
                b.text = "\n".join(L[i:j])
                blocs.append(b)
                i = j
                continue

            # citació
            if lin.lstrip().startswith(">"):
                j = i
                cr = []
                while j < n and (L[j].lstrip().startswith(">")
                                 or (cr and L[j].strip()
                                     and not L[j].lstrip().startswith(("|", "#", "`"))
                                     and not RE_HEADING.match(L[j]))):
                    if L[j].lstrip().startswith(">"):
                        cr.append(re.sub(r"^\s*>\s?", "", L[j]))
                    elif cr:
                        cr[-1] += " " + L[j].strip()
                    j += 1
                b = Bloc("quote", i + 1)
                b.files_raw = cr
                b.files = cr
                b.text = "\n".join(cr)
                blocs.append(b)
                i = j
                continue

            # llistes
            if RE_OLIST.match(lin) or RE_ULIST.match(lin):
                ordered = bool(RE_OLIST.match(lin))
                j = i
                items = []
                while j < n:
                    mo = RE_OLIST.match(L[j])
                    mu = RE_ULIST.match(L[j])
                    if ordered and mo:
                        items.append(mo.group(2).strip())
                    elif (not ordered) and mu:
                        items.append(mu.group(1).strip())
                    elif (L[j].strip() and L[j].startswith("  ")
                          and items):
                        items[-1] += " " + L[j].strip()
                    else:
                        break
                    j += 1
                b = Bloc("olist" if ordered else "ulist", i + 1)
                b.files = items
                b.text = "\n".join(items)
                blocs.append(b)
                i = j
                continue

            # paràgraf
            j = i
            cr = []
            while j < n and L[j].strip():
                if (L[j].lstrip().startswith(("|", "#", ">", "```"))
                        or RE_HRULE.match(L[j])
                        or RE_OLIST.match(L[j]) or RE_ULIST.match(L[j])):
                    break
                cr.append(L[j].rstrip())
                j += 1
            b = Bloc("para", i + 1)
            b.files_raw = cr
            b.files = cr
            b.text = "\n".join(cr)
            blocs.append(b)
            i = j
        return blocs

    # -- regions ----------------------------------------------------------

    def heading(self, num: str) -> Bloc:
        if num not in self._index:
            raise MdError(
                f"{self.path}: no hi ha cap encapçalament amb número {num!r}")
        return self._index[num]

    def region(self, num: str) -> list[Bloc]:
        """Blocs fills de l'encapçalament `num`, fins al següent del mateix
        nivell o més baix."""
        h = self.heading(num)
        out = []
        for b in self.blocks:
            if b.lineno <= h.lineno:
                continue
            if b.kind == "heading" and b.nivell <= h.nivell:
                break
            out.append(b)
        return out

    def taula(self, num: str, index: int = 0) -> Bloc:
        ts = [b for b in self.region(num) if b.kind == "table"]
        if index >= len(ts):
            raise MdError(
                f"{self.path}: §{num} té {len(ts)} taula/es; no hi ha la "
                f"número {index + 1}")
        return ts[index]

    def taules(self, num: str) -> list[Bloc]:
        return [b for b in self.region(num) if b.kind == "table"]

    def codi(self, num: str, index: int = 0) -> Bloc:
        cs = [b for b in self.region(num) if b.kind == "code"]
        if index >= len(cs):
            raise MdError(
                f"{self.path}: §{num} té {len(cs)} bloc/s de codi; no hi ha el "
                f"número {index + 1}")
        return cs[index]

    def paragrafs(self, num: str) -> list[Bloc]:
        return [b for b in self.region(num) if b.kind == "para"]

    def texto_paragrafs(self, num: str) -> str:
        return "\n\n".join(b.text for b in self.paragrafs(num))



def carrega(path: str) -> Document:
    return Document(path)


if __name__ == "__main__":  # pragma: no cover
    d = carrega(sys.argv[1])
    print(f"{d.path}  sha256={d.sha256}  línies={len(d.lines)}  "
          f"blocs={len(d.blocks)}")
    for b in d.blocks:
        if b.kind == "heading":
            print(f"  L{b.lineno:4d} h{b.nivell} {b.num!r:12s} {b.titol[:60]}")
        elif b.kind == "table":
            print(f"  L{b.lineno:4d} taula {len(b.capcaleres)} col · "
                  f"{len(b.files)} files")
        elif b.kind == "code":
            print(f"  L{b.lineno:4d} codi({b.lang}) {len(b.files)} línies")