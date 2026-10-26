# Exportació visual de graelles curriculars

Converteix una graella curricular escrita en Markdown en **XLSX** i **PDF**
auditable, sense redactar res i sense perdre ni un caràcter del text oficial.

Aquesta skill **no valida la graella**. Només la transporta. Si un valor és
incorrecte al Markdown, sortirà incorrecte al llibre i al PDF, i això no es
detecta aquí: ho detecta el verificador, en una fase separada.

---

## Regla que governa tota la skill

> **Exportar, no redactar.**

Conseqüències no negociables:

- Cap contingut curricular nou. Cap valor «per defecte». Cap correcció
  editorial d'un text que sembli equivocat. Si un apartat sembla incomplet,
  s'exporta incomplet i s'hi deixa el `PENDENT` que hi hagi.
- Cap fila es pot emplenar «perquè hauria de tenir-hi alguna cosa». Una fila
  sense marca recognescible **atura l'exportació**.
- Els fitxers d'entrada són de **només lectura**. L'skill no els obre per
  escriure-hi mai.
- Els intermedis van a un directori de treball **fora del repositori**. No es
  toca `.gitignore` i no es deixen residus dins del projecte.
- Sense dades personals, secrets ni tokens, ni a les sortides ni als
  intermedis.

---

## Què fa

| Script | Sortida | Què garanteix |
|---|---|---|
| `scripts/mdparse.py` | — | Analitza el Markdown i retorna blocs amb la seva línia. Dessembrague **mecànic**, mai editorial. |
| `scripts/regions.py` | — | Decideix què va a cada pestanya i quina classe té cada fila. Comparteix el model amb els dos exportadors. |
| `scripts/exportar_xlsx.py` | `.xlsx` | Llibre editable, 14 pestanyes, sense protecció. |
| `scripts/comparar_export.py` | text + JSON | Sis autocomprovacions, recalculades des del Markdown. |
| `scripts/exportar_pdf.py` | `.pdf` | Markdown → HTML5 → PDF, amb peu de procedència. |
| `assets/graella.css` | — | A3 apaisat, `thead` repetit, espais especials preservats. |

---

## Ús

### F2 · XLSX

```bash
python .opencode/skills/exportacio-visual/scripts/exportar_xlsx.py \
  --md    sortides/graelles/graella-3016.md \
  --xlsx  sortides/graelles/graella-3016.xlsx \
  --informe sortides/informes-validacio/informe-validacio-3016.md \
  --data  2026-10-01 \
  --resum /tmp/treball/resum-export.json
```

Codi de sortida: `0` correcte · `2` error d'estructura · `3` fila sense marca.

### F3 · PDF

```bash
python .opencode/skills/exportacio-visual/scripts/exportar_pdf.py \
  --md    sortides/graelles/graella-3016.md \
  --pdf   sortides/graelles/graella-3016.pdf \
  --treball /tmp/treball \
  --data  2026-10-01 \
  --informe sortides/informes-validacio/informe-validacio-3016.md \
  --resum /tmp/treball/resum-pdf.json
```

L'HTML intermedi queda a `--treball`, i el `--resum` hi registra l'**ordre
exacte** de les comandes i els hash. Un PDF que no se sabe reproduir no és
auditable.

### Autocomprovacions

```bash
python .opencode/skills/exportacio-visual/scripts/comparar_export.py \
  --md   sortides/graelles/graella-3016.md \
  --xlsx sortides/graelles/graella-3016.xlsx \
  --pdf  sortides/graelles/graella-3016.pdf \
  --data 2026-10-01 \
  --sortida /tmp/treball/autocomprovacions.json
```

Codi de sortida `0` només si passen les sis.

---

## Les sis autocomprovacions

| | Comprova |
|---|---|
| **C1** | Annex C: línies i caràcters especials, bloc idèntic línia a línia |
| **C2** | Criteris per RA (6/8/7/8/7/8 = 44) i hores (332) |
| **C3** | Annex A (40 sabers = 18+14+8) i Annex B (9 activitats) |
| **C4** | Codi P-, ODS `PENDENT` i que cap relació sigui `VERIFICADA` |
| **C5** | `sha256` del bloc literal d'Annex C |
| **C6** | Reimportació: pestanyes, ordre, les 8 columnes literals, llibre editable |

El comparador **no confia en l'exportador**: torna a llegir el Markdown i torna
a reimportar el XLSX, i calcula cada xifra dues vegades per separat abans de
comparar-les.

Amb `--pdf` s'hi afegeix **C7**, que no compta en les sis. Hi queda
constància del que el PDF conserva i del que no.

---

## Classes de fila i marques

Cada cel·la porta la seva classe, i la classe decideix el color. La classe
també declara **qui és responsable de la fila**:

| Classe | Vol dir |
|---|---|
| `capcalera` | Capçalera de taula, copiada literal. |
| `dades` | Contingut curricular amb marca reconeixible. |
| `estructura` | Fila de total, títol o separador. |
| `derivada` | **[DERIVAT]** — el llibre l'ha calculat. Prefix obligatori. |
| `procedencia` | **[PROCEDÈNCIA]** — explica d'on surt l'exportació, no què afirma. |
| `advertiment` | Declaració del projecte sobre la graella (§4.1, §5.4, §6.5). No afirma cap valor curricular, i el títol del bloc ho diu a la pestanya. |
| `proposta` | Fila de recompte governada per la marca literal que l'encapçalament de la regió declara. |

Cap valor per defecte vol dir que **una fila no pot posar-se sense marca**.
Hi ha tres vies, i totes tres s'han de veure:

1. Una marca curricular: `[TEXT EXTRET]`, `[RESUM]`, `PROPOSTA`, `PENDENT`,
   `amb reserva`, `P-…`, `I-…`, `F-…`, `V-…`, `ACT-…`, `SB-…`, `CB …`,
   `§…`.
2. Una citació literal entre crases.
3. Una classe declarada: `advertiment` o `proposta`, que existeixen perquè hi
   ha files que, per la seva naturalesa, no afirmen cap valor curricular.

Si cap d'aquestes vies no hi és, l'exportació s'atura amb codi `3` i **no
escriu el llibre**. Estovar el vocabulari de marques perquè passi és
exactament l'error que aquesta skill existeix per evitar.

---

## El que cal saber abans de tocar res

### El recompte de pestanyes

Aquest llibre té **14 pestanyes, de `00` a `13`**. El pla d'exportació que
l'originà deia «15 pestanyes» però només enumerava catorze. S'han fet les
catorce enumerades, perquè la numeració `00..13` és explícita i no hi ha cap
pestanya 14 descrita que es pugui construir sense inventar-ne el contingut. La
discrepància es declara dins el propi llibre, a la pestanya `00`.

### Els espais especials

`U+2002` (espai fi) i `U+2003` (espai em) no són decoració: són part del text
oficial que es vol conservar.

- **XLSX**: conservats byte a byte. Verificat per C1.
- **PDF**: **no conservats.** Chrome converteix tots els separadors Unicode
  a `U+0020`, tant en el dibuix com en la capa de text. Comprovat amb un
  HTML mínim a part: `U+0020`, `U+00A0`, `U+2002`, `U+2003`, `U+2009` i
  `U+205F` renderitzen tots amb la mateixa amplada. No és un problema de la
  CSS ni de la font, i no es pot arreglar des de l'HTML.

  Els altres caràcters (`U+2012`, `U+2013`, `U+2014`, `U+2423`, `«`, `»`)
  sí que es conserven al PDF.

  Per a la citació forense cal l'XLSX, no el PDF.

### Llibre editable

Sense protecció i **sense contrasenya**. A openpyxl, assignar `password`
—inclosa la cadena buida— calcula un hash i activa la protecció del full.
No s'assigna; es deixa explícitament desactivat.

### Format condicional

El color no decideix res i no altera cap valor. L'única regla és que
`[PENDENT]` i `P-` es veuen, i que cap altre text es colori.

---

## Dependències

| Eina | Versió comprovada | Sense ella |
|---|---|---|
| Python | 3.12.3 | F2 i les autocomprovacions no es poden executar |
| openpyxl | 3.1.5 | idem |
| pandoc | 3.1.3 | F3 no es pot executar |
| Chrome / Chromium | 152 | idem |
| `pdftotext`, `pdfinfo` | poppler | C7 no es pot executar |

Entorn virtual a `/tmp`, mai dins del repositori:

```bash
python3 -m venv /tmp/treball/venv
/tmp/treball/venv/bin/pip install openpyxl
```

---

## Si alguna cosa falla

| Situació | Què fer |
|---|---|
| Codi `3`, «cap marca reconeixible» | **No escrivis la marca.** Comprova si la fila és una declaració del projecte i, si en és, classifica-la com a `advertiment`. |
| Codi `2`, estructura inesperada | El Markdown ha canviat de forma. Torna a llegir la regió i ajusta `regions.py`; mai no «arreglis» el Markdown. |
| Codi `1`, autocomprovació fallada | No lliuris res. Mira el `JSON` a `--sortida`: diu quina xifra i quina era l'esperada. |
| Divergència entre el pla i la font | Exporta el que diu la font i **declara la divergència**. No triis un dels dos números en silenci. |
