# Informe de validació de l'exportació visual · F4

| Camp | Valor |
|---|---|
| Fitxer validat | `sortides/graelles/graella-3016.md` (font única) |
| sha256 del fitxer font | `454a3b4a5d5723bc6fd0b36d4d1ce8744f87c9d3a23e6d0ef4826c38a9776997` · 94.115 B · 1.005 línies |
| Artefactes avaluats | `sortides/graelles/graella-3016.xlsx`, `sortides/graelles/graella-3016.pdf`, `/tmp/opencode/exp-3016/graella-3016.html` |
| sha256 XLSX | `7805775a36072ef89956b3314ffba4623d146721b1c446809f0a6780e272ed91` · 58.184 B |
| sha256 PDF | `86296da17c4f102a8d3f4afdf9bf37666693be874f8686aa3fea7af629114185` · 1.252.883 B · 20 pàgines |
| sha256 HTML | `c4cd917918a52b55595fd5161ae4975f44d0ce1510c7c31aa939a9a6940f1026` |
| Naturalesa de la revisió | **No curricular.** Fidelitat de l'exportació, traçabilitat i presentació. No s'avalua cap criteri, hora, saber ni relació. |
| Data de la revisió | 2026-10-02 |

## 1. Mètode i independència

- Es va escriure un **analitzador Markdown propi** (`/tmp/opencode/f4/mdlib.py`), amb gramàtica diferent de la de la skill, per no heredar-ne els possibles errors. No importa res de `exportacio-visual`.
- Totes les xifres d'aquest informe s'han **recalculat des del l'XLSX reimportat**, no copiades del resum del generador.
- `comparar_export.py` del generador s'ha executat com a **creu** i retorna 61/61. No s'ha usat com a base del veredicte: el mateix script declara textualment que «la cobertura de regions es calcula a la taula de traçabilitat» i, per tant, **no comprova la cobertura de regions**. Els defectes que es troben cauen precisament en aquesta acotació.
- **No s'ha modificat cap fitxer** de la font ni de l'exportació. Els quatre hashos de font coincideixen amb `sha256-fonts-ABANS.txt` i `git status --porcelain` no mostra cap fitxer font modificat.

## 2. Capa A · comprovacions de fidelitat

### A1 · Integritat i identitat de l'exportació — **PASS**

Els tres hashos coincideixen amb els declarats. L'XLSX té exactament 14 pestanyes, numerades `00`–`13`, en l'ordre expected i sense cap pestanya 14. Reimportat amb `openpyxl 3.1.5` sense errors.

### A2 · Regions copiades — **FAIL**

Comparador regional propi: **297 blocs igualtats, 1 diferència**, més una **omissió de secció** que el comparador de blocs no pot veure.

- **Diferència F2** — `12 Text oficial (Annex C)!B4`. El valor concatena tres regions amb `" ".join(...)`, cosa que elimina els salts de paràgraf:
  - L871–874, introducció del §Annex C — 315 caràcters (22 %)
  - L988–993, «Procedència i reserva» — 484 caràcters (34 %)
  - L997–1005, peu del document — 632 caràcters (44 %)

  L'etiqueta de la fila diu «Procedència del bloc (text literal del §Annex C)». **El 78 % del text no prové del §Annex C.** Hi ha, dins d'una cel·la etiquetada com a text de l'Annex C, el peu del document amb els recomptes globals i la declaració «Document **en revisió, no validat**». Un docent que llegeixi la fila hi atribuiria a la font oficial unes xifres i un estat documental que no hi són. La pèrdua dels salts de paràgraf fa, a més, que no es pugui traçar cap frase del valor fins a una línia origen inequívoca.
- **Omissió F1** — **§5.2 no s'exporta.** La pestanya `10 Distribució temporal` salta de `5.1` (files 3–6) a `5.3` (files 8–18) a `5.4` (files 20–29). Els 5 blocs de §5.2 (títol, paràgraf aritmètic i 3 vinyetes, 926 caràcters) no apareixen en **cap** cel·la del llibre. És a dir, l'omissió no es detecta comparant blocs sinó mesurant cobertura.
  - *Mitigació parcial, verificada*: la substància de §5.2 sí que hi arriba per dues altres vies del **mateix full** — el paràgraf 2 de §5.3 (`10!B10`: «Són indicatives perquè **cap font curricular distribueix les 332 h** (P-7, P-18) […] L'equip docent ha d'adaptar-les al calendari real del centre») i l'advertiment 4 de §5.4 (`10!B25`: «332 h ÷ 10 h/setmana = 33,2 setmanes-equivalent […] 32 h quedarien sense col·locar»). P-16 consta a `11!A19` amb el seu motiu. **No es perden hores, criteris ni sabers.**
  - *Residu*: tres cel·les del llibre remeten a «§5.2» (`10!B25`, `11!C19`, `13!B27`) i la secció **no existeix al llibre**. L'omissió **no es declara** ni a la pestanya 00 ni a la 10, malgrat que la llegenda declara que «qualsevol dada que no hi fos, es quedaria PENDENT i es declararia» (`00!B5`).

### A3 · Reimportació i hash del bloc oficial — **PASS**

- Bloc oficial de l'Annex C: 109 línies. `sha256` calculat de tres maneres independents — des de la font, des de la cel·la `12!B7` i des del `<pre>` de l'HTML — **tots donen `92a65b0f8e6f4d505be189595d6351dac5cf5cc44c9853036f7d8679596e1a7f`**, que és el valor declarat a `00!B54` i a `12!C3`.
- Els 8 caràcters especials del bloc hi són amb el recompte exacte de la font.

### A4 · Caràcters especials — **FAIL**

Recompte per regió, font contra llibre. Criteris que han fallat:

- **F3 · Els 2 caràcters `U+2423` no són a l'XLSX.** La font en té exactament 2: L727 (§7.2) i L754 (§7.3). El PDF en té 2. **El llibre en té 0**, perquè §7.2 i §7.3 no s'exporten a cap pestanya. La pròpia llegenda hi remet: `00!B97` declara que les 2 aparicions «cal conservar-les» i que són «el nom del caràcter, citat dins de dos trams de codi a §7.2 i a §7.3». És a dir, **el llibre remet a dues seccions que no conté**.
- **F4 · `00!B34` afirma una cosa falsa.** La llegenda declara que «l'espai fi U+2003, l'espai fi fi U+2002 i **el guion fi U+2012 NO es recuperen de manera fiable**» del PDF. Mesurat: **`U+2012` es recupera 40 de 40** (font 40, text extret 40), incloses les vinyetes de l'Annex C i de §2.1. La pèrdua és real només per a `U+2002` (37 → 0) i `U+2003` (100 → 0). Una declaració d'incorrectitud dins de l'artefacte lliurat és un defecte, no una nota de estil.

El que **sí que quadra**: `U+2002` (37), `U+2003` (100 a la font: 50 a l'Annex C + 44 als quadres + 6 a §2) i `U+2012` (40) es conserven al llibre amb el recompte exacte, i l'HTML intermedi els conserva tots (37 / 100 / 40 / 2 / 45 / 105 / 174 / 174). L'Annex C (`12!B7`) és elèctricament idèntic a la font en els quatre codis.

### A5 · Xifres de control recalculades des del llibre — **PASS**

58 comprovacions, totes correctes, recalculades cel·la a cel·la:

| Dada | Valor recalculat |
|---|---|
| Criteris per RA | 6 / 8 / 7 / 8 / 7 / 8 = **44** |
| Hores per RA (suma de la columna, no del total) | 55 / 77 / 66 / 77 / 39 / 18 = **332** |
| Files amb 0 h assignades | **1** (el criteri `4g`) |
| Sabers a l'Annex A | **40** (18 / 14 / 8) |
| Etiquetes dels sabers | **34** `[TEXT EXTRET]` + **1** `[TEXT EXTRET (parcial)]` + **5** `[RESUM]`, cap buida |
| El parcial és `SB-3016-06`; els `[RESUM]` són 05, 36, 37, 38, 39 | ✅ |
| Activitats `ACT-n` | **9**, totes `[PROPOSTA]` |
| Codi `P-` | **25** en **24** files (P-13 i P-20 comparteixen fila), sense perdre ni duplicar |
| ODS proposats / TT proposats | **4** / **10**, tots `[PROPOSTA]` |
| ODS en PENDENT, desplegats de la llista literal | **13** |
| Relacions `VERIFICADA` | **0** a §4.4 i a §6.1 |
| Advertiments §4.1 / §5.4 / files §7.1 | **5** / **8** / **24** |

Totes coincideixen amb la taula 5 de la llegenda, que a més declara que els recomptes es fan «sobre les regions copiades en aquest mateix llibre, no sobre el Markdown» (`00!B56`). El criteri es comprova, no s'importa.

### A6 · Origen de cada cel·la — **FAIL** (pels mateixos dos motius que A2)

- 1.601 de 1.926 cel·les amb text són literalment localitzables a la font o a l'informe que la llegenda cita. Les 325 restants s'han classificat una a una: 146 són metatext `[DERIVAT]`, 15 són capçaleres, 6 són les citacions literals de D-3 que la llegenda etiqueta com a tals, i 1 és `12!B4` (**F2**).
- Cap cel·la curricular (criteri, hora, saber, activitat, relació) queda sense origen. **La pèrdua de traçabilitat és nul·la en el contingut i falsa només a `12!B4`.**

### A7 · HTML intermedi — **PASS**

- `pandoc --from=markdown-smart → HTML5`, 39 taules, 332 files, 1.276 cel·les de dades, 188 capçaleres.
- Tots els caràcters especials hi són amb el recompte exacte de la font.
- El bloc de l'Annex C hi és en un `<pre>` de 109 línies amb el mateix `sha256` que la font i que el llibre.
- Hi consta el sha256 de la font, la ressalva D-3 i la declaració «no validat».

### A8 · Control negatiu — **PASS**

Còpia del Markdown a `/tmp`, tres mutacions mínimes, cap fitxer del repositori tocat:

| # | Mutació | Detectada per |
|---|---|---|
| M1 | `U+2003` → `U+3000` dins el criteri `1a` | comparador regional + recompte de caràcters (44 → 43) |
| M2 | «Total RA 1» de **55 h** a **56 h** | comparador regional |
| M3 | etiqueta de `SB-3016-01` de `[TEXT EXTRET]` a `[RESUM]` | comparador regional |

El comparador passa de *297 igualdades / 1 diferència* a **294 igualdades / 4 diferències**: les 3 mutacions Injectionades es detecten una per una i no hi ha falsos positius. L'instrument mesura el que diu que mesura.

### A9 · Etiquetes, estats i punts suspensius — **PASS**

- **4g** (`04 RA 4!A19`), fila completa: `Saber`/`Saber fer`/`Saber estar` = `:—`; contingut = «CAP. Cap dels 29 continguts bàsics parla d'embelleidors, tapes ni elements decoratius. PENDENT — vegeu §3.8»; activitat = `cap`; hores = `0 assignades`; instrument = `PENDENT`; cap `SB-3016-nn` a tota la fila; les columnes derivades diuen `[DERIVAT] sense saber · sense saber fer · sense saber estar · sense contingut bàsic (CAP.) · PENDENT · sense activitat · 0 h assignades`. **La incoherència no està emmascarada.**
- Els 40 sabers i les 9 activitats tenen etiqueta; cap buida. Els 14 ODS/TT són `[PROPOSTA]`; cap `VERIFICADA`. Els 25 codis `P-` tenen estat.
- Els dos eixos i el vocabulari de l'etiqueta estan íntegres a la pestanya 00 (§6, §7 i §8 de la llegenda).

### A10 · `4g` i el que la font declara sobre ell — **PASS**

La font (§3.8) i el llibre coincideixen. A més, l'avís de §3.5 sobre `CB b5.i6` **sí que arriba** al llibre per tres vies independents: `07!D45`, `13!A30` i `13!B61`. Aquestes no s'havien detectat com a absències perquè el text està reformulat, no copiat.

### A11 · Cap contingut nou a l'exportació — **PASS**

- Cap criteri, hora, saber, activitat, relació ni codi `P-` que no sigui a la font.
- Cap text curricular de fora de les fonts. Les 70 cel·les de text ≥ 40 caràcter que no són literals són totes metatext estructural de l'exportador («copiat literal», «copiat de l'Annex A», títols de pestanya, hashos) o les citacions de D-3 que la llegenda etiqueta com a tals.
- No s'ha perdut cap criteri ni cap hora. L'única pèrdua de contingut és F1 (§5.2), i la seva substància arriba duplicada per §5.3/§5.4.

## 3. Capa B · revisió visual i d'ús

### B1 · Format, geometria i capçaleres repetides — **PASS**

- **A3 apaisat confirmat per dues vies**: `pdfinfo` → 1191,12 × 841,92 pt; rasterització a 100 dpi → 1655 × 1170 px = 42,0 × 29,7 cm, a les 20 pàgines.
- **Capçalera repetida als punts de continuació**: les 6 taules de §3.1–§3.6 donen 9 línies de capçalera (pàgines 4, 5, 6, 7 i 8), és a dir 6 capçaleres inicials + 3 repeticions. El full d'estil ho fa explícit: `thead { display: table-header-group }`.
- **Cap columna tallada**: 0 de les 20 pàgines té cap paraula fora del límit de la pàgina. Marges drets entre 35,1 i 58,4 pt, marge esquerre constant de 33,7 pt, marge inferior ≥ 55 pt. Amplada útil de 1.112–1.122 pt sobre 1.191 pt.
- Mida de lletra mínima observada: 7,6 pt (cos de taula), la majoria a 10,2 pt. XLSX declarat en paper 8 (A3), orientació `landscape`.

### B2 · XLSX editable i protecció — **PASS**

Cap pestanya protegida, cap contrasenya, cap `<sheetProtection>` a l'arquiu. El fitxer no conté `sharedStrings.xml` (openpyxl escriu strings en línia), cosa que és normal i no afecta l'edició.

### B3 · Llegibilitat de l'XLSX — **FAIL** (F5)

- El 100 % de les cel·les amb contingut té `wrap_text`, cosa que evita el desbordament. Les columnes estan dimensionades bé a 13 de 14 pestanyes.
- **F5 · La pestanya `12 Text oficial (Annex C)` és l'excepció i és la que més importa.** El generador dimensiona `{"A": 150}` i el codi genèric assigna a la columna B el valor de reserva `14`. El resultat: **el bloc oficial de 109 línies i 8.830 caràcters viu en una columna de 14 caràcters**.
  - Mesurat en el renderer real (LibreOffice headless): el text es renderitza a ~2 paraules per línia; el fitxer sencer ocupa **29 pàgines A3** i el valor de `B7` es desborda de la pàgina. A la pràctica el llibre està dissenyat perquè el bloc oficial — l'única dada que s'ha de poder llegir i citar — sigui incòmode de llegir i de copiar.

### B4 · Altres elements d'ús — **PASS amb observacions**

- Panos congelats a les 6 pestanyes de RA (`C13`), `07` (`A5`), `08` (`B4`), `11` (`B4`) i `12` (`A6`).
- Filtre automàtic a les 6 pestanyes de RA, `08` i `11`. **No n'hi ha a `00`, `07`, `09`, `10`, `12` ni `13`**, que són taules de 9 a 40 files. No és un defecte de fidelitat i és una decisió discutible: `07` té 40 files de sabers que són la llista de referència de la graella.
- Cap full ni fila oculta.

## 4. Declaracions del generador: verificació

| # | Declaració | Veredicte |
|---|---|---|
| 1 | «14 pestanyes, i el pla diu 15: el recompte i la taula no quadren» | **Confirmada.** 14 pestanyes, cap 14. La discrepància es declara amb honestitat a `00!B8` i no s'ha construït cap pestanya inventada. |
| 2 | Chrome perd `U+2002` i `U+2003` al PDF | **Confirmada amb matís.** En un HTML mínimo → Chrome → PDF, `U+2002` i `U+2003` desapareixen de la capa de text. Però en rasteritzar a 72 dpi (1 em = 40 px) les amplades renderitzades són **22 px per a `U+2002` i 42 px per a `U+2003`, davant 13 px d'un espai normal**: el PDF els **dibuixa** amb l'amplada correcta. La pèrdua és de la **capa de text** (copiar i enganxar, `pdftotext`), no visual. La formulació del resum és massa categòrica. |
| 3 | El text no és byte-reproduïble pel PDF | **Confirmada.** Dues execucions de Chrome sobre el mateix HTML → `57ab19e3…` i `e65ae8e5…`. Mateixa mida (1.252.883 B), només canvia `CreationDate`/`ModDate`. |
| 4 | Quatre files sense marca curricular | **Confirmada amb precisió.** Són els 3 avisos de §6.5 (ítems 2, 8 i 9, que no porten marca pròpia) i la taula de famílies d'instruments de §6.4 (11 files sense marca, governada pel títol). Al llibre els 10 ítems de §6.5 són sense marca, com a la font. |
| 5 | L'exportació no revalida res | **Confirmada.** `00!B26` declara que el fitxer font té 1.005 línies i no les 714 de l'objecte validat, i que el fitxer ha canviat **després** de l'informe. Es declara correctament. |
| 6 | El PDF el genera `pdftotext`? No és via fiable | **Parcialment falsa.** `00!B34` és correcta en dir que la **capa de text** reordena els espais, però és **incorrecta en incloure-hi `U+2012`** (vegeu F4). |

## 5. Defectes trobats

### Bloquejants

- **F1 · §5.2 no s'exporta a l'XLSX i l'omissió no es declara.** `10 Distribució temporal` salta de §5.1 a §5.3. 926 caràcters i 5 blocs absents. La substància arriba duplicada per §5.3 i §5.4, de manera que **no es perden dades curriculars**, però tres cel·les del llibre remeten a un §5.2 que no hi és, i la llegenda que promet declarar qualsevol dada absent no ho fa.
- **F2 · `12!B4` concatena tres regions i en corrobora la procedència.** 78 % del valor (1.116 de 1.433 caràcters) prové de «Procedència i reserva» i del peu del document, no del §Annex C, sota una etiqueta que diu el contrari. Els salts de paràgraf s'han perdut en la concatenació.
- **F3 · Els 2 caràcters `U+2423` no són a l'XLSX.** La font en declara exactament 2 (§7.2 i §7.3) i el PDF els conserva; el llibre no en té cap, i la seva pròpia llegenda remet a §7.2/§7.3.
- **F4 · `00!B34` afirma que `U+2012` no es recupera del PDF.** Es recupera 40 de 40. Declaració falsa dins de l'artefacte lliurat.
- **F5 · El bloc oficial de 109 línies viu en una columna de 14 caràcters** (`12!B`). El llibre es comporta mal en el punt exacte on hauria de ser més usable.

### No bloquejants, perquè es declaren

- **N1** La fórmula de `00!B5` diu «una graella Markdown **ja validada**», mentre que `00!B26` declara que el fitxer font ha canviat després de la validació. S'han de llegir les dues; l'ordre pot induir a error.
- **N2** Referències creuades a seccions que el llibre no conté: §0.3, §1, §5.2, §7.2 i §7.3.
- **N3** Cap filtre automàtic a sis pestanyes, inclosa `07 Sabers (Annex A)` (40 files).
- **N4** La pèrdua de `U+2002`/`U+2003` al PDF és de la capa de text, no del dibuix; la formulació del generador no ho distingeix.

## 6. Què quedaVerified i correcte

Sense que això compensi els defectes de l'apartat 5, l'exportació és **exacta** en tot allò que és contingut curricular:

- Els **44 criteris**, les **8 columnes literals** de les 6 taules i totes les files «Total RA n» coincideixen caràcter a caràcter amb la font, amb els espais `U+2003` oficials al seu lloc.
- El **bloc oficial de l'Annex C** és idèntic a la font: 109 línies i `sha256` coincident, calculat per tres vies independents.
- Les **19 marques «amb reserva»**, els `:—`, els `[PROPOSTA]`, els `[RESUM]` i les declaracions `[INTERPRETACIÓ]` estan col·locades igual que a la font.
- L'instrument de comparació és eficaç: el control negatiu el posa a prova i el supera.

## 7. Límits d'aquesta revisió

- No s'ha avaluat **cap valor curricular**: ni si les hores són raonables, ni si els sabers cobreixen el text, ni si les relacions ODS/TT tenen sentit. Queda fora de l'abast de F4.
- La revisió visual s'ha fet per **geometria i extracció de text** (caixes delimitadores, amplades de renderització, amplada de columna, conversió a PDF), no per inspecció d'imatges: aquest model no accepta entrada visual. La correcció de l'amplada de columnes amb PIL no ha estat necessària perquè el problema de F5 s'ha pogut confirmar amb el renderer real.
- No s'ha tornat a revalidar el contingut contra les fonts primàries (F-032, F-035, F-037); això és feina de la fase de verificador.
- Les regions de la font que el llibre no exporta (§0.1–§0.4, §1, §2.1, §3.0, §3.7–§3.9, §7.2–§7.3) s'han auditat una a una: cap conté dades curriculars que el llibre perdi, excepte §5.2 (F1). La majoria són metatext de mètode que la llegenda substitueix.

## 8. Veredicte

Cinc defectes confirmats: dos d'omissió de contingut o de procedència (F1, F2), un d'omissió de caràcter (F3), una declaració falsa dins del llibre (F4) i un d'usabilitat sobre la dada més sensible (F5). Cap no s'ha reparat; tots queden descrits amb localització exacta perquè els tracti el `generador-graelles` i els torni a passar per F4.

Cap comprovació no s'ha deixat sense fer. La integritat de la font, les xifres de control, el bloc oficial, els criteris i el control negatiat hi passen nets; el que impedeix el lliurament és la pèrdua de §5.2, la procedència falsa de `12!B4`, els `U+2423` absents, la declaració errònia sobre `U+2012` i l'amplada de la columna del bloc oficial.

NOT READY
