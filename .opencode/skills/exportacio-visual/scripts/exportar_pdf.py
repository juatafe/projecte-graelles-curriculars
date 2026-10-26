#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F3 · Exporta la graella a PDF passant per HTML.

Ordre obligatori, sempre el mateix:

  1. sha256 del Markdown font
  2. escriptura del fragment HTML del peu de procedència
  3. pandoc  Markdown -> HTML5, autonomous i amb els recursos embuts
  4. Chrome headless  HTML -> PDF

L'HTML intermedi NO va al repositori: es queda al directori de treball, i
s'hi apunten l'ordre exacte de les comandes i el seu hash, perquè la
reproducció siga verificable sense haver de llegir res d'aquest script.

Cap valor curricular no s'escriu ni es modifica aquí. Aquest script només
calcula el hash de la font i encamina les comandes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

CSS_DEFALT = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    "assets", "graella.css")

PEU_HTML = """<div class="peu" role="contentinfo">
  <div class="peu-l1">Graella curricular 3016 · Instal·lació i manteniment de
  xarxes per a transmissió de dades · procedència de tot el document</div>
  <div class="peu-l2">font: {font} · sha256: {sha} · data: {data} ·
  {pagina}</div>
</div>
"""


class ErrorF3(Exception):
    pass


def _eina(nom: str) -> str:
    p = shutil.which(nom)
    if not p:
        raise ErrorF3(f"no s'ha trobat {nom!r} al PATH")
    return p


def _executa(cmd: list, pas: int) -> str:
    print(f"\n[{pas}] {' '.join(cmd)}")
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        raise ErrorF3(
            f"pas {pas} ha fallat amb codi {r.returncode}\n"
            f"  sortida: {r.stderr.strip()[:600]}")
    if r.stdout.strip():
        print(f"      {r.stdout.strip()[:300]}")
    return cmd_str(cmd)


def cmd_str(cmd: list) -> str:
    """Mateixa comanda en text, prou segura perquè la persona la copï."""
    return " ".join(
        f'"{c}"' if (" " in c or not c) else c for c in cmd)


def _chrome() -> str:
    """Ruta del navegador. Es provenen various noms perquè el de Chrome canvia
    segons la instal·lació, i perquè en alguns sistemes hi ha Chromium."""
    for nom in ("google-chrome", "google-chrome-stable", "chromium",
                "chromium-browser", "chrome"):
        p = shutil.which(nom)
        if p:
            return p
    raise ErrorF3("no s'ha trobat cap Chrome ni Chromium al PATH")


def html_a_pdf(html: str, pdf: str, treball: str) -> tuple[list, str]:
    """Converteix l'HTML en PDF amb Chrome headless i retorna l'ordre."""
    chrome = _chrome()

    perfil = os.path.join(treball, "chrome-profile")
    os.makedirs(perfil, exist_ok=True)
    url = "file://" + os.path.abspath(html)

    cmd = [
        chrome,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-extensions",
        "--disable-translate",
        "--run-all-compositor-stages-before-draw",
        "--virtual-time-budget=15000",
        f"--user-data-dir={perfil}",
        # A3 apaisat i capçalera del navegador: el peu el posa la nostra CSS.
        "--no-pdf-header-footer",
        f"--print-to-pdf={os.path.abspath(pdf)}",
        url,
    ]
    return [cmd], cmd_str(cmd)


def main() -> int:
    ap = argparse.ArgumentParser(description="Exporta la graella a PDF.")
    ap.add_argument("--md", required=True, help="Markdown font")
    ap.add_argument("--pdf", required=True, help="PDF de sortida")
    ap.add_argument("--treball", required=True,
                    help="directori per als intermedis (mai dins del repo)")
    ap.add_argument("--data", required=True, help="data de l'export, AAAA-MM-DD")
    ap.add_argument("--informe", help="informe antecedent, només per al peu")
    ap.add_argument("--css", default=CSS_DEFALT)
    ap.add_argument("--resum", help="JSON amb l'ordre de comandes i els hash")
    a = ap.parse_args()

    try:
        os.makedirs(a.treball, exist_ok=True)
        os.makedirs(os.path.dirname(os.path.abspath(a.pdf)), exist_ok=True)

        # 1 · hash de la font
        with open(a.md, "rb") as f:
            sha = hashlib.sha256(f.read()).hexdigest()
        print(f"font     {a.md}")
        print(f"sha256   {sha}")
        print(f"data     {a.data}")

        # 2 · peu de procedència
        html = os.path.join(a.treball,
                            os.path.splitext(os.path.basename(a.md))[0] + ".html")
        peu = os.path.join(a.treball, "peu.html")
        pag = f"{a.pdf.split('/')[-1]}"
        with open(peu, "w", encoding="utf-8") as f:
            f.write(PEU_HTML.format(
                font=os.path.basename(a.md), sha=sha, data=a.data, pagina=pag))
        print(f"peu      {peu}")

        pandoc = _eina("pandoc")
        cmds = []

        # 3 · Markdown -> HTML5
        c1 = [pandoc,
              "--from=markdown-smart",
              "--to=html5",
              "--standalone",
              "--embed-resources",
              "--css=" + os.path.abspath(a.css),
              "--include-in-header=" + peu,
              "--metadata", "lang=ca",
              "--metadata", "title=" + pag,
              f"--output={html}",
              a.md]
        cmds.append(_executa(c1, 1))

        # 4 · HTML -> PDF
        grup, txt = html_a_pdf(html, a.pdf, a.treball)
        cmds.append(_executa(grup[0], 2))

        if not os.path.exists(a.pdf):
            raise ErrorF3("Chrome ha sortit amb codi 0 però no hi ha PDF")
        if os.path.getsize(a.pdf) == 0:
            raise ErrorF3("el PDF és buit")

    except (ErrorF3, OSError) as e:
        print(f"\nERROR · {e}")
        return 2

    h_html = hashlib.sha256(open(html, "rb").read()).hexdigest()
    h_pdf = hashlib.sha256(open(a.pdf, "rb").read()).hexdigest()
    h_md = hashlib.sha256(open(a.md, "rb").read()).hexdigest()

    print(f"\nOK · {a.pdf}")
    print(f"  html intermedi  {html}")
    print(f"  sha256 html     {h_html}")
    print(f"  sha256 pdf      {h_pdf}")

    if a.resum:
        dades = {
            "font": a.md, "sha256_font": h_md,
            "informe": a.informe, "data": a.data,
            "css": os.path.abspath(a.css),
            "html_intermedi": html, "sha256_html": h_html,
            "pdf": a.pdf, "sha256_pdf": h_pdf,
            "ordre": [
                {"pas": 1, "que": "sha256 del Markdown font",
                 "comanda": f"sha256sum {a.md}"},
                {"pas": 2, "que": "escriptura del peu de procedència",
                 "comanda": f"(script intern) -> {peu}"},
                {"pas": 3, "que": "pandoc Markdown -> HTML5", "comanda": cmds[0]},
                {"pas": 4, "que": "Chrome headless HTML -> PDF", "comanda": cmds[1]},
            ],
            "eines": {"pandoc": _eina("pandoc"), "chrome": _chrome()},
        }
        with open(a.resum, "w", encoding="utf-8") as f:
            json.dump(dades, f, ensure_ascii=False, indent=2)
        print(f"  JSON  {a.resum}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
