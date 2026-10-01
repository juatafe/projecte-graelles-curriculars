# Informe de validació · graella del mòdul `3016`

| Camp | Contingut |
|---|---|
| Objecte validat | `sortides/graelles/graella-3016.md` (714 línies) |
| Mòdul | `3016 «Instalación y mantenimiento de redes para transmisión de datos»` |
| Cicle | T.P.B. Informàtica d'oficina · grau bàsic · **2n curs** · Comunitat Valenciana |
| Fase | **Fase 4** · validació **independent** · agent `verificador` |
| Branca | `issue/3-graella-3016` · **cap operació de git** feta pel verificador |
| Data | **2026-10-01** |
| Skill aplicada | `.opencode/skills/validation-report/SKILL.md` |
| Mètode | contrast directe caràcter per caràcter de la graella amb `sortides/esborranys/extraccion-3016.md`, amb `sortides/esborranys/relacions-3016-sabers.md`, amb `fonts/registre-fonts.md`, amb `dades/estat-catalogs.md`, amb `dades/ods-i-temes-transversals.md` i amb l'informe de fonts. **Cap fitxer validat no s'ha modificat.** |

> **Abisme de funcions, dit clar.** Aquest **sí** és l'informe de validació
> independent. L'anterior (`informe-fonts-3016.md`) és l'informe de fonts. Aquest
> document **no repara res**: detecta, documenta ijudica.

---

## 1. Veredicte

# `READY FOR HUMAN REVIEW`

**Justificació del veredicte.** No he trobat **cap defecte bloquejant**:

- **Cap norma inventada ni alterada.** Els 6 resultats d'apreneatge i els 44
  criteris de la taula §3 són **idèntics caràcter per caràcter** al text oficial
  transcrit, i el bloc literal de l'Annex C és **byte-idèntic** (SHA-256
  `92a65b0f8e6f4d505be1…`, 109 línies) al de l'extracció de la fase 1 i al de
  l'annex de la fase 2.
- **Cap criteri perdut, fusionat ni renumerat:** 44 de 44, i el recompte per RA
  (6 / 8 / 7 / 8 / 7 / 8) coincideix amb el de la norma.
- **Cap relació d'ODS ni de tema transversal figura com a exigència curricular ni
  com a `VERIFICADA`:** les 14 (4 ODS + 10 TT) són `PROPOSTA` i la categoria
  `VERIFICADA` aplicada al mòdul `3016` és buida (0).
- **Les hores quadren:** 55 + 77 + 66 + 77 + 39 + 18 = **332**, que és
  exactament la càrrega horària curricular de **F-032** (10 h/setmana · 332 h/any).
  El camp `Duración: 115 horas.` **ha quedat exclòs** de tot el calendari i
  consta com a `PENDENT` (I-7 / P-6).
- **Traçabilitat present** en tots els elements exigibles (font, apartat i data a
  §1, §2, §5.1, §6.1 i Annex C).
- **La graella no se declara `READY FOR HUMAN REVIEW`** per la seva compte.

Hi ha **4 reserves i 7 defectes no bloquejants**, tots documentats amb evidència
i cap d'ells introdueix dada falsa ni deixa fora cap element exigible. Les
reserves i els `PENDENT` coneguts **sí que permeten** el pas a revisió humana:
allò que es documenta és exactament allò que el professorat ha de revisar.

**Reserva que el professorat ha d'atendre abans de resoldre la graella:** dos
continguts bàsics oficials i una vinyeta d'orientacions pedagògiques **no tenen
cap itinerari d'integració** a la graella (vegeu el defecte **D-1**, el més
important dels no bloquejants). No és una dada falsa ni un criteri perdut, però
és una omissió d'integració que cal resoldre o declarar explícitament.

### 1.1 Reconciliació amb la llista de pendents «que bloquegen el tancament» de la fase 3

L'informe de fonts (§4.3) deixa constància de **7 pendents que bloquejarien el
tancament**: `P-1`, `P-2`, `P-3`, `P-19`, `P-20`, `P-21` i, «fora de la meva
decisió», `P-16`. Aquest informe **no pot ignorar-la**, així que la resolc una
a una. El mateix informe deixa escrit, al costat, que els pendents que
bloquejen el **contingut curricular** de la graella són **0**, i això sí que l'he
verificat.

| Pendent | Per què queda resolt o transferit | Veredicte |
|---|---|---|
| `P-1`, `P-2` | No hi ha cap vinculació acreditable d'ODS ni de TT al mòdul, i això **no és un defecte** sinó un fet comprovat: F-037, bloc `3016`, té 0 coincidències de tots els termes, i l'art. 10.3 s'adreça al centre i al cicle. La solució correcta és la que ja hi ha: 4 ODS i 10 TT en `PROPOSTA`, cap de `VERIFICADA`. Un ODS no es pot acreditar per exigència quan el RD no l'assigna a cap mòdul. | **Resolt.** El `PENDENT` de partida es manté com a `PENDENT` real, però no bloqueja res. |
| `P-3` | El contingut bàsic de `4g` **no existeix** a la norma: cap dels 29 ítems parla d'embelleidors, tapes ni decoració. No hi ha res a verificar ni que decidir. La graella no hi inventa cap i ho diu a §3.8. | **Resolt per inexistència.** |
| `P-19` | Les hores de `4g` són 0 perquè no hi ha contingut ni criteri avualable amb fonament curricular. Assignar-les seria inventar. | **Resolt.** |
| `P-20` (i `P-13`) | Reverificació directa de F-032 i F-037 per una altra fase. L'impacte sobre el contingut és **nul**, perquè el registre acredita identitat caràcter per caràcter (109 línies, `diff` sense diferències, I-8) i el text que la graella transcriu és el del registre. **Sí** que es transfereix com a **reserva de lletra petita** al professorat: se li afirma que el text és la versió consolidada vigent sense que aquesta fase l'haja tornat a obrir. | **Transferit** a revisió humana (reserva A). |
| `P-21` | Per definició, la revisió docent de tot allò `[PROPOSTA]` **es fa ara**, en la revisió humana que aquest veredicte obri. No es resol abans: es resol *en*. El seu propi text ho diu: «Cap no es pot dona per validada sense `READY FOR HUMAN REVIEW`». | **Es resol en aquesta porta**, no abans. |
| `P-16` | Divergència entre el DOGV (10 h / 332 h) i les fitxes CEICE (8 h / 266 h). Prevaleix F-032 per la regla 1 del registre i la divergència **es deixa oberta a propòsit**, no per oblit. El risc real no és curricular: és que el centre contracte amb uns hores que no són les curriculars. | **Transferit** a revisió humana, amb el risc explicitat (§6.3). |

**Conclusió de la reconciliació.** Cap dels 7 no deixa res sense resoldre i cap
no amaga una dada falsa. Quatre són fets comprovats que no es poden canviar, un
és el pas mateix que estic obrint, i dos es transfereixen al professorat com a
reserva declarada. Per aixè el veredicte pot ser `READY FOR HUMAN REVIEW`
**però no pot ser** «tot validat»: res del que és `[PROPOSTA]` està validat, i
`P-20`/`P-16` continuen oberts.

---

## 2. Taula de comprovacions

| # | Comprovació | Resultat | Evidència |
|---|---|---|---|
| **A** | **Fonts i traçabilitat** | `RESERVA` | Cada RA (§2), criteri (§3), contingut bàsic (§3, columna «Contingut bàsic literal (F-037)») i element exigible duu **F-037**, *Annex VII, apartat 3.3, bloc `Código: 3016.`*, consulta **2026-10-01**, estat `VERIFICADA` (§2 L118-121, §6.1 L437-444, Annex C L583-700). **F-037** és la font curricular citada (§0.2, §2, Annex C L702-707) i **F-027** apareix **només** com a «origen de la transcripció» (§2 L123-126, Annex C L703). **F-032** marca les hores amb apartat i pàgina (§1 L84, §5.1 L380-383). `Duración: 115 horas.` **exclòs** del calendari (§0.3 L45-57, §1.3 L101-112, §5.4). **Cap element exigible es presenta com a oficial sense que ho siga.** *Reserva:* l'atribució a F-037 prové del `diff` del registre, **no** d'una reverificació feta en les fases 2 i 3 (P-13 / P-20, declarades). |
| **B** | **Fidelitat al text oficial** | `PASS` (amb 1 reserva menor, **D-4**) | Contrast programàtic dels 44 criteris de la taula §3 contra el bloc literal: **44/44 coincideixen exactament**, 0 diferències, 0 criteris oficials absents, 0 criteris que no existesquen a la norma, 0 fusionats, 0 renumerats. Els 6 RA de §2 L130-135 coincideixen exacte amb els literals. El **bloc literal de l'Annex C és byte-idèntic** (SHA-256 `92a65b0f8e6f4d505be1…`, 109 línies) al de `extraccion-3016.md` §2 L63-172 i al de `relacions-3016-sabers.md` §11.3 L709-817. Es conserven els caràcters especials oficials (`U+2003` × 50, `U+2012` × 40, `U+2002` × 37). **Cap crematura detectada.** *Reserva menor:* als quadres de §2 i §3 el separador oficial `U+2003` se substituït per un **`␣␣` visible** (`U+2423` × 100) sense declaració-ho (**D-4**). |
| **C** | **Coherència de la integració** | `PASS` (amb 1 reserva, **D-1**) | Tots els sabers citats a la taula §3 **existeixen** a l'Annex A (0 orfans). 38 dels 39 sabers hi mobilitzen; el 39 (`SB-3016-38`) és transversal i s'assigna via `ACT-9` («tots els 39 sabers»), cosa declarada. Contraste **cel·la a cel·la** de les 44 files de §3 amb la taula de la fase 2 (`relacions-3016-sabers.md` §3.2-§3.7): **1 sola divergència**, la de `4g` (la fase 2 li donava `ACT-5`; la graella li treu l'activitat), que és **deliberada i declarada** (§3.8 L291, Annex B L572). La correspondència criteri → saber → RA → activitat **no presenta contradiccions** excepte la incoherència interna `6f` ↔ `ACT-7` (**D-2**). **Cap saber ni activitat sense origen literal es presenta com a curricular**: les 9 activitats són `[PROPOSTA]` (§3.0 L170, Annex B) i els 4 sabers `[RESUM]` porten reserva. |
| **D** | **ODS i temes transversals** | `PASS` | **Cap** relació figura com a exigència curricular ni com a `VERIFICADA`. Les **14 files** (ODS-04, 08, 10, 12 + TT-001…TT-010) tenen **totes** l'etiqueta `**\`PROPOSTA\`**` (14/14, verificat fila a fila, cap estat contradictori). La categoria `VERIFICADA` al mòdul hi és explícitament **buida** (§4.1.3 L325-327, §4.4 L368 i L370: `0` i `0`). **F-001 no s'usa com a justificació d'exigibilitat**: només com a font del text de la denominació (§4.1.5 L331-333, capçalera de §4.2 L337, informe de fonts §1.1 fila F-001) i així mateix a `dades/ods-i-temes-transversals.md` §Regla d'ús 3. Els textos literals d'ODS i de TT de la graella **coincideixen exactament** amb `dades/ods-i-temes-transversals.md` L33-62. La degradació de `VERIFICADA` (nivell cicle) a `PROPOSTA` (nivell mòdul) és el que exigeix la regla d'ús 2 d'aquell fitxer, i s'ha fet. `protección ambiental` **no** s'ha convertit en capçalera d'ODS (§4.2 ODS-12, §6.5 L489-490). |
| **E** | **Hores** | `PASS` (amb 1 reserva menor, **D-8**) | Suma per criteri verificada programàticament: **55 + 77 + 66 + 77 + 39 + 18 = 332**, i els totals per RA dels capçaleres §3.1-§3.6 (55/77/66/77/39/18) coincideixen amb el còmput fila a fila. Context curricular = **10 h/setmana · 332 h/any** (F-032, Anexo III-A, pàg. 34/58, 2026-10-01, `VERIFICADA`, §1 L84 i §5.1 L380-383). Les hores per criteri van totes marcades `[PROPOSTA]` (§3.0 L171, §5.4.3 L424-426, §6.4) amb remissió a P-18. El repàs aritmètic 332 ÷ 10 = 33,2 setmanes-equivalent **es fa explícitament** (§5.2 L387-401) i el calendari concret es deixa al centre. *Reserva menor:* els intervals de setmanes «indicatives» de §5.3 es toquen en els lindars 6, 14, 21 i 29 (**D-8**). |
| **F** | **Criteri `4g`** | `PASS` | Text literal correcte i **exacte**: `g)␣␣Se han colocado los embellecedores, tapas y elementos decorativos.` La fila `4g` de §3.4 L223 té els tres tipus de saber a `:—`, contingut bàsic `**CAP.** … \`PENDENT\``, activitat `cap`, hores `0 assignades` i instrument `PENDENT`. §3.8 L268-309 en fa l'exposició i declara textualment: «**Construeix un contingut decoratiu per omplir-lo: No.**». Cap dels 29 continguts bàsics parla d'embelleidors, tapes ni decoració (verificat sobre el bloc literal). **No se li ha inventat cap contingut, cap saber, cap activitat, cap hora ni cap instrument.** El criteri **sí** que consta com a exigible, amb la raó de l'art. 3.2 del Decret 117/2025 («prescriptivos») i les dues vies de tractament sense inventar. |
| **G** | **Estat del document** | `PASS` | §1 «Estat del document» L14-L16: la graella es declara **«EN REVISIÓ»** i diu literalment «Aquesta graella **no** està `READY FOR HUMAN REVIEW`» i «Cap graella val per al professorat fins que un informe independent de validació (fase 4) done el `READY FOR HUMAN REVIEW`». L'única menció de la porta al fitxer és a L16 i és per **negar-la**. El peu L711-714 acaba «Document **en revisió**, no validat». L'informe de fonts tampoc no s'autoaprova (§0 L15-19). **Coherència registre ↔ informe:** tots els 17 codis `P-` que cita la graella existeixen a l'informe de fonts (0 orfans); cap relació ODS/TT `VERIFICADA` al mòdul, cap font nova, coherència amb `fonts/registre-fonts.md` i `dades/estat-catalogs.md` en F-032/F-037/F-038 i en les incidències I-7 (`PENDENT`) i I-8 (`RESOLTA`). *Reserva menor:* P-6, P-8, P-9, P-14 i P-21 existeixen a l'informe i no són citats pel codi a la graella, tot i que el seu tema sí que s'hi tracta (**D-9**). |

### Vocabulari d'estats

La skill `validation-report` usa `PASS` / `FAIL` / `NOT TESTED`, i la petició
d'aquesta validació demana `PASS` / `FAIL` / `RESERVA`. Els dono el mateix sentit:

| Resultat | Skill | Significat |
|---|---|---|
| `PASS` | `PASS` | comprovació superada sense reserves |
| `RESERVA` | `NOT TESTED` + `PASS` parcial | comprovació superada amb una reserva que cal revisió humana, o part no verificada de manera independent |
| `FAIL` | `FAIL` | comprovació fallada · **0 en aquest informe** |

No hi ha cap `FAIL` i no hi ha cap element `NOT TESTED` sense identificar: les
tres reserves (A, E, G) estan explicades fila a fila.

### Recompte de comprovacions

| Resultat | Nombre |
|---|---|
| `PASS` | **4** (B, C, D, F) |
| `RESERVA` | **3** (A, E, G) |
| `FAIL` | **0** |
| **Total** | **7** (A a G) |

---

## 3. Defectes trobats, per gravetat

### 3.1 Defectes bloquejants

**Cap.**

### 3.2 Defectes no bloquejants

#### D-1 · Contingut oficial sense itinerari d'integració — gravitat **alta**, agent **`integrador-sabers`**

Dos continguts bàsics oficials i una vinyeta de les orientacions pedagògiques
**no apareixen mai** com a origen d'un saber, ni a la columna «Contingut bàsic
literal» de cap criteri, ni a la justificació de cap activitat. Només són al
bloc literal de l'Annex C.

| Contingut oficial (text literal, F-037) | On apareix | On **no** apareix |
|---|---|---|
| `CB b5.i6` «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» (bloc 5, ítem 6) | graella L677 (Annex C); fase 2 L795 | cap fila de §3.5, cap saber de l'Annex A. **És l'ítem més lligat al RA 5** («Realiza operaciones **básicas de configuración** en redes locales cableadas») i cap dels 7 criteris de RA 5 (`5a`-`5g`) se li atribueix: `5c` cita `CB b5.i1`–`CB b5.i5`, és a dir **s'atura just abans** |
| `OP v8` «La toma de medidas de las magnitudes típicas de las instalaciones.» (vinyeta 8 de 8) | graella L152 i L699; fase 2 L817 | cap criteri, cap saber, cap activitat. **Cap criteri del mòdul parla de prendre mesures** |
| `OP v7` «La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.» (vinyeta 7 de 8) | graella L151 i L698; fase 2 L816 | cap saber amb origen `OP v7`. El seu sentit literal **sí** queda cobert per `SB-3016-26` (`CB b4.i2` «Montaje de sistemas y elementos…»), de manera que és el menys greu dels tres |

**Per què importa.** De 29 ítems de continguts bàsics, **27** tenen
itinerari d'integració i **2** no. De 8 vinyetes d'orientacions pedagògiques,
**6** originen sabers i **2** no. En concret, el professorat **no té cap lloc a
la graella on introduir, ensenyar ni valorar** «configuració bàsica dels
dispositius d'interconnexió de xarxa cablejada i sense fil» ni «la tomada de
mesures de les magnituds típiques de les instal·lacions», tots dos continguts
**exigibles** del mòdul segons l'art. 3.2 del Decret 117/2025.

**Per què no és bloquejant.** No s'ha perdut cap criteri ni cap resultat
d'apreneatge (44/44 i 6/6 hi són), no s'ha introduït cap dada falsa, i el text
oficial es conserva verbatim a l'Annex C, de manera que la informació **no es
perd** del document. És una omissió d'**integració**, no d'**exigibilitat**, i
resol-la exigeix una decisió pedagògica i docent, no una correcció mecànica.

**Què hauria de fer l'agent responsable.** O bé crear la cobertura (saber +
criteri/activitat que sostinga aquests dos continguts, amb el mateitz tractament
de reserves que la resta), o bé **declarar-los explícitament** com a continguts
del mòdul **no integrats** a la graella, amb la raó, a l'Annex A i al recompte
de §3.7. El que no és admisible és deixar-ho silenciós.

#### D-2 · Incoherència interna sobre l'activitat del criteri `6f` — gravitat **mitjana**, agent **`generador-graelles`** (origen: `integrador-sabers`)

| Lloc | Què diu |
|---|---|
| graella §3.6, fila `6f` (L249) | Activitat = **`ACT-7, ACT-8`** |
| graella Annex B, fila `ACT-7` (L574) | ACT-7 avalua **`6a`–`6e`** |
| graella Annex B, fila `ACT-8` (L575) | ACT-8 avalua `6f`, `6g`, `6h` |

`6f` no és avaluat per cap activitat segons l'Annex B, però sí que en té una
assignada a la taula. A més, la fase 2 §7 (L549) declara que `ACT-7` avalua
`6a`…`6e` **i `6h`**, cosa que la graella no recull. El criteri `6f` queda
amb un buit: o bé hi afegeix `ACT-7` a l'Annex B, o bé la fila `6f` es queda
només amb `ACT-8`.

#### D-3 · Recompte d'instruments d'avaluació declarat no ajustat a la taula — gravitat **baixa**, agent **`generador-graelles`**

§6.4 L476 declara «Instruments d'avaluació de cada criteri · **8 tipus** ·
`[PROPOSTA]` (P-17)». La columna «Instrument» de §3 conté **43 assignacions** per
a **34 formulacions distintes** (rúbriques amb denominacions diferents, proves,
inspecions, diaris, lliurables, fitxes, ITTS…). El 8 es refereix evidentment a
**famílies** destruments, no a tipus. S'ha de deixar dit, perquè un recompte
equivocat en un apartat de «recompte» també és un defecte de documentació.

#### D-4 · Substitució no declarada del separador oficial als quadres — gravitat **baixa**, agent **`generador-graelles`**

Als quadres de §2 (6 RA) i §3 (44 criteris), el separador oficial `U+2003`
(espai fi) **s'ha substituït pel caràcter visible `␣`** (`U+2423`, 100
aparicions). El text del criteri i del RA és idèntic al literal (verificat), de
 manera que **no hi ha cap crematura**, però la nota de l'Annex C (L586-588)
afirma que «Es conserven els espais especials del document oficial», cosa que
només és certa dins de l'Annex C i **no** als quadres. Cal declarar la
substitució o emprar el caràcter real.

#### D-5 · Etiqueta `[TEXT EXTRET]` sobre un text truncat — gravitat **baixa**, agent **`generador-graelles`**

Annex A.1, `SB-3016-06` (L514): `[TEXT EXTRET]` «Características y tipos de las
fijaciones.» L'ítem oficial `CB b4.i1` és **«Características y tipos de las
fijaciones. Técnicas de montaje.»** La fase 2 sí que ho declarava («primera part
de l'ítem», L123); la graella, no. No hi ha buit funcional perquè «Técnicas de
montaje» queda coberta per `SB-3016-20` i `SB-3016-28`, però l'etiqueta
`[TEXT EXTRET]` aplicada a una subfrase literal ha de dir-ho.

#### D-6 · Etiqueta `[TEXT EXTRET]` sobre una cel·la que inclou formulació del projecte — gravitat **baixa**, agent **`integrador-sabers`**

Annex A.3, `SB-3016-38` (L556): `[TEXT EXTRET]` «**Assumir l'abast de la funció
professional del mòdul:** «instalar canalizaciones, cableado y sistemas
auxiliares en instalaciones de redes locales en pequeños entornos».» El text
del saber és formulació del projecte; només el fragmente entre comilles
angulars és literal. Cal `[RESUM]` amb el literal entre comilles, o `[TEXT
EXTRET]` amb la part projectual fora de l'etiqueta.

#### D-7 · Recompte de sabers mobilitzats amb matís — gravitat **baixa**, agent **`generador-graelles`**

§3.7 L263 declara «Sabers mobilitzats · **39**». A la taula de §3 n'hi
aparèixen **38**; el 39 (`SB-3016-38`) només entra per `ACT-9`
(«tots els 39 sabers», Annex B L576). El recompte és defensable, però convé
distingir els 38 que sostenen un criteri del 39è, transversal.

#### D-8 · Intervals de setmanes «indicatives» que es toquen als lindars — gravitat **baixa**, agent **`generador-graelles`**

§5.3 L407-411: fase 1 = setmanes 1–6, fase 2 = 6–14, fase 3 = 14–21,
fase 4 = 21–29, fase 5 = 29–33. Les fases 1 i 2 es creuen a la setmana 6, la 2
i la 3 a la 14, la 3 i la 4 a la 21, la 4 i la 5 a la 29. Amb l'etiqueta
«indicatives» i el `[PROPOSTA]` de §5.2-§5.4 no hi ha contradicció, però cal
donar intervals disjunts (p. ex. 1–5, 6–13, 14–20, 21–28, 29–33) o dir
expressament que els lindars es comparteixen.

#### D-9 · Codi de pendent existent a l'informe de fonts que la graella no cita — gravitat **informativa**, agent **`generador-graelles`**

`P-6` (caràcter del camp `Duración`), `P-8` (calendari i dependència del RA 6),
`P-9` (equips disponibles), `P-14` (registre de F-001) i `P-21` (revisió docent
de tot allò `[PROPOSTA]`) consten a l'informe de fonts §4.1-§4.2 però no
s'han citat pel codi a la graella, tot i que el seu tema sí que s'hi tracta
(§0.3, §1.3, §5.4.1, Annex B, §6.4). A més, §6.4 hauria de remetre a
P-21, que és el pendent queè cobreix exactament allò que §6.4 enumera.

---

## 4. `PENDENT` acceptats

No són defectes. Són limitacions conegues, documentades correctament i assumides.
Enumerar-les **no** impedeix el pas a revisió humana; precisament el que el professorat ha
de revisar.

| ID | Què | Per què és un `PENDENT` correcte |
|---|---|---|
| `P-1` | Vinculació acreditada d'un ODS al mòdul (`V-3016-ODS`) | F-037, bloc `3016`: 0 coincidències de tots els termes. F-035: `ODS` 1 sola vegada, al preàmbul, i no assigna ODS a mòduls. **Correcte: no s'ha de colonzar.** |
| `P-2` | Vinculació acreditada d'un tema transversal al mòdul (`V-3016-TT`) | `transversal` = 0 al RD; l'art. 10.3 s'adreça al centre i al cicle. **Correcte.** |
| `P-3` | Criteri `4g` sense contingut bàsic | Verificat: cap dels 29 ítems parla d'embelleidors ni decoració. **Correcte, i és el tractament més honest possible.** |
| `P-4` | 19 criteris amb elements que els continguts bàsics no anomenen | Marca «amb reserva» a les 19 files, amb el codi `P-4`. **Correcte i exhaustiu** (comprovat fila a fila). |
| `P-5` | Criteri `3g` sense criteri d'avaluació propi | Literalment cert; marcat amb reserva. **Correcte.** |
| `P-6` | Caràcter del camp `Duración: 115 horas.` | El RD no el defineix (0 coincidències) i els 9 valors sumen 1.100 h davant de les 2.000 h de l'apartat 1. **Correcte, i no afecta la graella** perquè preval F-032. |
| `P-7` / `P-18` | Distribució de les 332 h | Cap font curricular distribueix les hores. Marcat `[PROPOSTA]` i el calendari es deixa al centre. **Correcte.** |
| `P-8` | Calendari i dependència del RA 6 | No verificat en cap font. **Correcte.** |
| `P-9` | Equips i proves disponibles al centre | Cap font ho acredita. **Correcte.** |
| `P-10` | Format i eina del «mapa físico» | Cap contingut ni cap vinyeta ho fixa. **Correcte.** |
| `P-11` | Quins RA del projecte intermodular toquen `3016` | Cal el currículum bàsic del projecte. **Correcte**, i TT-009 ho declara amb reserva. |
| `P-12` | Lletres de les competències de les orientacions | F-038 fixa la denominació, no el contingut de cada lletra. La graella **no assigna cap competència**. **Correcte.** |
| `P-13` / `P-20` | Reverificació directa de F-037 i F-032 | La comparació de versions prové del registre, no de les fases 2 i 3. **Correcte i declarat**; l'impacte sobre el contingut és nul perquè el registre acredita identitat caràcter per caràcter amb SHA-256. |
| `P-14` | Actualització del registre per a F-001 | Evidència de reverificació del 2026-10-01 sense atualizar al registre. **Correcte.** |
| `P-15` | Codificació pròpia (`SB-…`, `ACT-…`, `CB b#.i#`, `OP v#`) | La norma no assigna cap codi. **Declarada a §0.2 i Annex A. Correcte.** |
| `P-16` | Divergència DOGV (10 h/332 h) vs fitxes CEICE (8 h/266 h) | Prevaleix F-032 per regla de prevalència 1; la discrepància es deixa oberta. **Correcte.** |
| `P-17` | Instruments d'avaluació | Cap font curricular no fixa cap instrument. **Correcte en el fons** (el recompte «8 tipus» és el que cal corregir: **D-3**). |
| `P-19` | Hores del criteri `4g` | 0 h assignades sense fonament curricular. **Correcte.** |
| `P-21` | Revisió docent de tot allò `[PROPOSTA]` | **Correcte i indispensable:** 9 activitats, 44 files d'hores, 6 fases, 4 ODS i 10 TT. |
| `P-22` | Denominació literal de la família professional | Cap material de la fase 1 la transcriu; §1.2 la marca `PENDENT` de literal i ancora el mòdul a la taula de F-032. **Correcte.** |
| `I-7` | Caràcter del camp `Duración` al registre | `PENDENT`, sense resoldre. **Correcte.** |
| `I-8` | Versió del text del RD 356/2014 | `RESOLTA` al registre amb comparació de 109 línies i `diff` sense diferències; la graella la reprodueix amb la reserva corresponent. **Correcte.** |

---

## 5. Recompte final

| Dada | Recompte | Comprovació |
|---|---|---|
| **Resultats d'apreneatge** | **6** | Tots a la taula, text literal idèntic |
| **Criteris d'avaluació** | **44** | 44/44 a la taula; per RA 6 / 8 / 7 / 8 / 7 / 8 = 44. Cap omès, cap fusionat, cap inventat, cap renumerat |
| Criteris amb contingut bàsic literal que els sosté | **24** | Llista de §3.7 verificada fila a fila |
| Criteris coberts **amb reserva** (`P-4`) | **19** | Llista de §3.7 verificada fila a fila |
| Criteris **sense cobertura** (`PENDENT`) | **1** | `4g` |
| **Continguts bàsics** | **6 blocs / 29 ítems** | Tots transcrits literalment; **27/29 amb itinerari d'integració** (vegeu **D-1**) |
| **Orientacions pedagògiques** | **4 paràgrafs + 8 vinyetes** | Totes transcrites literalment; **6/8 originen saber** (vegeu **D-1**) |
| **Sabers** | **39** | 18 `saber` + 13 `saber fer` + 8 `saber estar`. 35 `[TEXT EXTRET]` + 4 `[RESUM]`. 38 a la taula de §3 + `SB-3016-38` transversal via `ACT-9` |
| **Activitats** | **9** | `ACT-1`…`ACT-9`, totes `[PROPOSTA]`. Cap criteri (menys `4g`) sense activitat |
| **Instruments** | **43 assignacions / 34 formulacions** | en ~8 famílies; tots `[PROPOSTA]` (`P-17`) |
| **Hores** | **332** | 55 + 77 + 66 + 77 + 39 + 18, recomptat fila a fila. Context: **10 h/setmana · 332 h/any** (F-032) |
| Criteris amb hores sense assignar | **1** | `4g` (0 h) |
| **Relacions ODS** | **4** `PROPOSTA` + **13** `PENDENT` | ODS-04, 08, 10, 12. `VERIFICADA` al mòdul: **0** |
| **Relacions TT** | **10** `PROPOSTA` | TT-001…TT-010. `VERIFICADA` al mòdul: **0** |
| **Tot allò `PENDENT`** | **22** codis (`P-1`…`P-22`) + `I-7` `PENDENT` (rellevant) i `I-6` `PENDENT` (no afecta aquesta graella: duplicació d'URL F-034 / F-036) | 17 dels 22 citats pel codi a la graella; tots 22 a l'informe de fonts |
| Fonts usades / noves | **6 / 0** | F-037, F-027, F-038, F-032, F-035, F-001. Cap font nova, d'acord amb el punt 9 de la regla de prevalència |

---

## 6. Què pot i què no pot fer el professorat amb aquesta graella

### 6.1 Sí que pot, tal com està

1. **Avaluar els 44 criteris** amb la formulació literal: són exigibles i el text
   es pot llegir directament del RD 356/2014 vigent (F-037, Annex VII 3.3).
   La numeració `1.`-`6.` i `a)`-`h)` és la de la norma; el codi compost
   `1a`, `2g`… és del projecte i s'ha declarat així.
2. **Recorrer qualsevol dada curricular de la taula fins al document oficial**,
   sense dependre de cap altre fitxer del projecte: l'Annex C reprodueix el
   bloc sencer de `3016`.
3. **Planificar les hores del mòdul** sobre **10 h/setmana · 332 h/any**, que és
   el que mana (F-032, Anexo III-A, pàg. 34/58), i veure el repartiment
   proposat per criteri (55/77/66/77/39/18) com a **proposta**, no com a ordre.
4. **Usar les 9 activitats i els instruments** com a material didàctic propi,
   sabent que cap font curricular els obliga.
5. **Proposar ODS i temes transversals** al centre, perquè estan marcats
   `PROPOSTA` i el text oficial de F-001 i de F-035 hi és correcte. **No** són
   exigibles del mòdul: no hi ha cap vinculació acreditada.
6. **Aplicar les 19 reserves**: són el mecanisme honest per tractar els 19
   criteris que parlen de coses que els continguts bàsics no diuen (tipus de
   caixa, guies passacables, panells de parcheo, «mapa físico»…). El criteri és
   exigible; el que cal buscar-ne és contingut curricular de referència.
7. **Decidir què es fa amb el criteri `4g`** per la via que la graella proposa
   (decisió documentada del centre o consulta a la conselleria), sabent que avui
   **no hi ha cap contingut oficial** amb què valorar-lo.

### 6.2 No pot, tal com està

1. **No pot presentar cap relació d'ODS o de tema transversal com a exigència
   curricular del mòdul.** No n'hi ha cap acreditada. Tampoc pot citar F-001
   (ONU) com a justificació d'una exigibilitat: només acredita el text de la
   denominació de l'objectiu.
2. **No pot valorar `4g` amb un contingut oficial**, ni inventar-ne un. El criteri
   és exigible; el contingut bàsic que l'ha de sostenir no existeix al mòdul.
3. **No pot fer servir les 115 h del camp `Duración`** com a horari del curs, ni
   com a alternativa ni com a suma: prevalen les 332 h de F-032 i el caràcter del
   camp `Duración` és `PENDENT` (I-7).
4. **No pot tractar les hores per criteri, la distribució en 6 fases, els 33
   setmanes-equivalent, els instruments ni les activitats com a exigibles.**
   Són `[PROPOSTA]` i depenen del calendari i dels recursos del centre (`P-7`,
   `P-9`, `P-17`, `P-18`, `P-21`).
5. **No pot assignar cap competència** a les lletres `a)`-`i)` de les
   orientacions pedagògiques: la correspondència lletra per lletra no està
   verificada (`P-12`).
6. **No pot extreure del bloc 5 «Configuración básica de los dispositivos…» ni
   de la vinyeta «La toma de medidas de las magnitudes típicas…» cap itinerary
   d'ensenyament o d'avaluació a partir de la graella**, perquè la graella no
   els ha integrat (**D-1**). Sí que en té el text literal a l'Annex C.
7. **No pot tancar la graella per la seva compte.** Aquesta fase 4 és la que
   posa `READY FOR HUMAN REVIEW`, i el que obri la porta és el **supervisor**,
   no aquest informe per si sol.

### 6.3 El que el professorat ha de revisar sí o sí

En ordre d'importància: **D-1** (dos continguts oficials sense itinerari);
l'horari real del centre i la divergència P-16; els 19 criteris amb reserva; el
criteri `4g`; i tota la columna d'hores i d'instruments.

---

## 7. Limitacions d'aquesta validació i canvis fora d'abast

- **No he consultat cap font a la web.** He validat el material del projecte
  contra el seu propi registre. La credibilitat de F-037 (consolidat vigent),
  F-032, F-035 i F-001 depèn de les evidències registrades
  (`fonts/registre-fonts.md`), inclosa la comparació de 109 línies sense `diff`
  entre F-027 i F-037 que acredita `I-8`. Aquesta comprovació **no és meua** i
  consta com a `P-13` / `P-20`.
- **He validat la *traçabilitat i la fidelitat*, no la *veritat del registre*.**
  Si el `diff` de `I-8` no s'ha fet de debò, la graella seria exacta però
  atribuïda a una versió equivocada del RD. Aquesta és la reserva de més abast
  del informe.
- **He tractat els 39 sabers i les 9 activitats com a material del projecte**,
  d'acord amb la regla de prevalència 15 del codi de sabers: no puc jutjar si un
  saber és *pedagògicament* bo, només si està **traçat** i **etiquetat** com el
  que és.
- **Fora d'abast i no comprovat:** l'existència real dels equips (`P-9`), el
  calendari del centre (`P-7`), els recursos del currículum bàsic del projecte
  (`P-11`) i la correspondència lletra per lletra de les competències (`P-12`).
- **Canvis fora d'abast:** **cap**. No he modificat `graella-3016.md`,
  `informe-fonts-3016.md`, cap esborrany, `fonts/registre-fonts.md` ni cap altre
  fitxer del projecte. L'**únic** fitxer creat és aquest informe. **Cap operació
  de git.**

---

*Fase 4 · `verificador` · branca `issue/3-graella-3016` · 2026-10-01 · 7
comprovacions (A-G): **4 `PASS`, 3 `RESERVA`, 0 `FAIL`** · **0 defectes
bloquejants**, 7 no bloquejants (D-1 a D-9, D-1 d'alta gravitat) · 22 `PENDENT`
acceptats · 6 RA · 44 criteris · 39 sabers · 9 activitats · 332 h · 14
relacions ODS/TT, totes `PROPOSTA`, 0 `VERIFICADA` al mòdul. Independent, la
graella **no** es valida per la seva compte i **no** s'ha reparat cap defecte.*

# `READY FOR HUMAN REVIEW`
