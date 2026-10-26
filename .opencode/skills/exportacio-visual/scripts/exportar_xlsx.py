#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""Exportador de graelles curriculars Markdown → XLSX.

Copia regions identificades del Markdown a un llibre de 15 pestanyes.
**No redacta.** Si una dada no és al fitxer font, no la posa: s'atura amb
codi d'error.

Ús:

    exportar_xlsx.py --md GRAELLA.md --xlsx SORTIDA.xlsx \
                     --informe INFORME.md [--data YYYY-MM-DD]

Sortides:
* el XLSX demanat;
* un resum JSON a la sortida estàndir amb les xifres de control i l'inventari
  de regions (surt per stderr si es demana `--resum -`).

Codi de sortida:
* 0 — tot correcte;
* 2 — error d'arguments o de forma del Markdown;
* 3 — una fila no du cap marca reconeixible (**no s'omple**).
"""

from __future__ import annotations

import argparse
import datetime
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from mdparse import MdError, carrega          # noqa: E402
from regions import (                         # noqa: E402
    CLS_ADVERTIMENT, CLS_CAPCALERA, CLS_DERIVADA, CLS_DADES, CLS_ESTRUCTURA,
    CLS_PROCEDENCIA, CLS_PROPOSTA,
    Llibre, SenseMarca, col_letra,
)

E_ARGS = 2
E_SENSE_MARCA = 3


# --------------------------------------------------------------------------
# Estil del llibre
# --------------------------------------------------------------------------

#: Gradient de fons per classe. Només ajuda visual: **mai** substitueix el
#: text literal de l'etiqueta, i mai s'escriu res que no hi fos.
FONS = {
    CLS_CAPCALERA: "DCE6F1",
    CLS_ESTRUCTURA: "EDEDED",
    CLS_DERIVADA: "FFF2CC",
    CLS_PROCEDENCIA: "E2EFDA",
    CLS_ADVERTIMENT: "F2E6FF",
    CLS_PROPOSTA: "E8F4F8",
    CLS_DADES: None,
}

ALINEACIÓ = {"titol": "left"}

TOP_GUIA = {
    1: "FF8080", 2: "FFFF80", 3: "80FF80",
    4: "80FFFF", 5: "8080FF", 6: "FF80FF",
}


def aplica_estil(ws, cel):
    """Estil d'una cel·la. **Només aspecte**: cap valor, cap text i cap ordre
    de lectura no depèn d'aquí."""
    from openpyxl.styles import Alignment, Font, PatternFill

    c = ws[cel.address]
    f = FONS.get(cel.classe)
    if f:
        c.fill = PatternFill(fill_type="solid", start_color=f, end_color=f)
    if cel.estil == "titol":
        c.font = Font(bold=True, size=13)
    elif cel.estil == "monoespaciada":
        c.font = Font(name="DejaVu Sans Mono", size=9)
    elif cel.classe == CLS_CAPCALERA:
        c.font = Font(bold=True)
    elif cel.classe in (CLS_DERIVADA,):
        # itàlica només per distingir el derivat del literal; el text és intacte
        c.font = Font(italic=True)
    c.alignment = Alignment(wrap_text=True, vertical="top", horizontal="left")


def configura_fulla(ws, fulla):
    from openpyxl.utils import get_column_letter
    from openpyxl.worksheet.properties import PageSetupProperties

    for letra, amplada in fulla.amplada.items():
        ws.column_dimensions[letra].width = amplada
    if fulla.ncols:
        ws.column_dimensions[get_column_letter(max(fulla.ncols, 1))].width = \
            fulla.amplada.get(get_column_letter(max(fulla.ncols, 1)), 14)
    if fulla.congelar:
        ws.freeze_panes = fulla.congelar
    if fulla.autofilter:
        ws.auto_filter.ref = fulla.autofilter

    # Sense protecció i sense contrasenya: el llibre ha de ser editable.
    # No s'assigna cap valor a `password`: a openpyxl l'assignació crida
    # `set_password`, que genera un hash i activa la protecció del full
    # (amb `""` fins i tot acaba posant l'hash "CE4B"). El fitxer ha de
    # quedar amb cap element `<sheetProtection>`.
    for attr in ("password", "hashValue", "saltValue", "spinCount",
                 "algorithmName"):
        try:
            setattr(ws.protection, attr, None)
        except (TypeError, ValueError):
            pass
    ws.protection.enabled = False
    ws.protection.sheet = False
    ws.protection.objects = False
    ws.protection.scenarios = False

    # Impressió en paisatge, ajustat a l'amplada d'una pàgina.
    ws.page_setup.orientation = "landscape"
    ws.page_setup.paperSize = ws.PAPERSIZE_A3
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    ws.print_options.horizontalCentered = False
    ws.print_title_rows = None
    # Amplada per al bloc oficial (pestanya 12)
    try:
        if ws.title == "12 Text oficial (Annex C)":
            ws.column_dimensions["B"].width = 180
    except Exception:
        pass


def format_condicional(ws, fulla):
    """Només ajuda visual: fila de colors segons l'estat literal de les
    columnes de criteri. No escriu, no mou i no substitueix cap text."""
    from openpyxl.formatting.rule import FormulaRule
    from openpyxl.styles import PatternFill

    if not re.match(r"^\d\d RA \d$", fulla.sheet):
        return 0

    cap = total = None
    for cel in fulla.celles:
        n = int(cel.address[1:])
        if cel.regio.endswith("/capcalera") and cel.address.startswith("A"):
            cap = n
        elif cel.regio.endswith("/total"):
            total = n
    if cap is None:
        return 0
    primera = cap + 1
    ultima = (total - 1) if total else cap + 1
    if ultima < primera:
        return 0
    rng = f"A{primera}:J{ultima}"
    regles = 0
    for sufix, color in (("PENDENT", "FFF2CC"), ("amb reserva", "FDE9D9"),
                         ("[RESUM]", "EDEDED")):
        parts = [f'ISNUMBER(SEARCH("{sufix}",${col}{primera}&""))'
                 for col in ("A", "B", "C", "D", "E", "F", "H")]
        ws.conditional_formatting.add(rng, FormulaRule(
            formula=["=" + "+".join(parts) + ">0"],
            fill=PatternFill(fill_type="solid", start_color=color,
                             end_color=color),
            stopIfTrue=True))
        regles += 1
    return regles


# --------------------------------------------------------------------------
# Exportació
# --------------------------------------------------------------------------


def exporta(md_path: str, xlsx_path: str, informe: str = "", data: str = "",
            resum_path: str = "") -> dict:
    from openpyxl import Workbook
    from openpyxl.styles import Alignment, Font, PatternFill

    doc = carrega(md_path)
    if not data:
        data = datetime.date.today().isoformat()
    llibre = Llibre(doc, informe_path=informe, data_exportacio=data)

    # ordre de construcció: 01..06, 07..13 i, al final, 00 (que conté les
    # xifres de control i, per tant, s'ha de poder llegir després).
    ra_info = {}
    for n in range(1, 7):
        _, info = llibre.fulla_ra(n)
        ra_info[n] = info
    llibre.fulla_07()
    llibre.fulla_08()
    _, s09 = llibre.fulla_09()
    _, s10 = llibre.fulla_10()
    _, s11 = llibre.fulla_11()
    _, s12 = llibre.fulla_12()
    llibre.fulla_13()
    llibre.calcula_xifres(ra_info, s09, s10, s11, s12)
    llibre.fulla_00()

    wb = Workbook()
    wb.remove(wb.active)

    ordre = ["00 Llegenda"] + [f"{n:02d} RA {n}" for n in range(1, 7)] + \
            ["07 Sabers (Annex A)", "08 Activitats (Annex B)", "09 ODS i TT",
             "10 Distribució temporal", "11 Pendents",
             "12 Text oficial (Annex C)", "13 Traçabilitat"]

    inventari = {}
    n_regles_cf = 0
    for nom in ordre:
        f = llibre.fulles.get(nom)
        if f is None:
            raise MdError(f"no s'ha construït la pestanya {nom!r}")
        ws = wb.create_sheet(title=nom)
        configura_fulla(ws, f)
        for cel in f.celles:
            ws[cel.address] = cel.valor
            aplica_estil(ws, cel)
        n_regles_cf += format_condicional(ws, f)
        inventari[nom] = len(f.celles)

    # Metadades del llibre (procedència, no contingut curricular).
    wb.properties.title = f"Graella {doc.path} · exportació no curricular"
    wb.properties.creator = "exportar_xlsx.py (skill exportacio-visual)"
    wb.properties.description = (
        f"Exportació NO curricular de {doc.path}. sha256 {doc.sha256}. "
        f"El contingut curricular prové índicament del fitxer font; cap valor "
        f"d'aquest llibre no hi és al Markdown. Llibre editable, sense "
        f"protecció ni contrasenya.")
    wb.properties.keywords = "no curricular; exportació; procedència; PENDENT"

    os.makedirs(os.path.dirname(os.path.abspath(xlsx_path)), exist_ok=True)
    wb.save(xlsx_path)

    resum = {
        "fitxer_font": md_path,
        "sha256_font": doc.sha256,
        "linies_font": len(doc.lines),
        "informe": informe,
        "xlsx": xlsx_path,
        "pestanyes": ordre,
        "cel_les_per_pestanya": inventari,
        "criteris_per_ra": {str(k): len(v["grups"]) for k, v in ra_info.items()},
        "criteris_total": sum(len(v["grups"]) for v in ra_info.values()),
        "sabers": len(llibre.ordre_sabers),
        "act": len(doc.taula("AnnexB").files),
        "codis_p": len(s11["codis"]),
        "annexc_linies": s12["linies"],
        "annexc_sha256": s12["sha256"],
        "regles_format_condicional": n_regles_cf,
        "avisos": llibre.avisos,
    }
    if resum_path:
        with open(resum_path, "w", encoding="utf-8") as fh:
            json.dump(resum, fh, ensure_ascii=False, indent=2)
    return resum


def main(argv=None):
    p = argparse.ArgumentParser(
        description="Exporta una graella curricular Markdown a XLSX. "
                    "Copia regions; no redacta.")
    p.add_argument("--md", required=True, help="graella Markdown (font única)")
    p.add_argument("--xlsx", required=True, help="fitxer XLSX de sortida")
    p.add_argument("--informe", default="",
                   help="informe de validació antecedent (per a la llegenda)")
    p.add_argument("--data", default="", help="data de l'exportació (AAAA-MM-DD)")
    p.add_argument("--resum", default="", help="camí del resum JSON")
    a = p.parse_args(argv)

    try:
        resum = exporta(a.md, a.xlsx, a.informe, a.data, a.resum)
    except SenseMarca as e:
        print(f"ERROR · cap marca reconeixible\n{e}", file=sys.stderr)
        return E_SENSE_MARCA
    except MdError as e:
        print(f"ERROR · {e}", file=sys.stderr)
        return E_ARGS
    except FileNotFoundError as e:
        print(f"ERROR · no hi ha el fitxer {e.filename}", file=sys.stderr)
        return E_ARGS

    print(f"OK · {a.xlsx}")
    print(f"  pestanyes            {len(resum['pestanyes'])}")
    print(f"  criteris (6 taules)  {resum['criteris_total']}")
    print(f"  sabers Annex A       {resum['sabers']}")
    print(f"  codis P-             {resum['codis_p']}")
    print(f"  Annex C              {resum['annexc_linies']} línies · "
          f"{resum['annexc_sha256']}")
    print(f"  sha256 font          {resum['sha256_font']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())