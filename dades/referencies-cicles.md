# Referències normatives dels cicles

Aquest fitxer és l’índex de fonts de veritat per als cicles del catàleg. Els
noms, codis, cursos, mòduls, hores i resultats d’aprenentatge s’han d’extraure
del Reial decret corresponent i de les seues actualitzacions. Les llistes de
`dades/moduls-fp.md` són només una còpia de consulta regenerable.

| Cicle | Nivell | Reial decret del títol | Apartat exacte consultada | Data | Estat |
|---|---|---|---|---|---|
| Informàtica i comunicacions | Grau bàsic | [RD 127/2014](https://www.boe.es/eli/es/rd/2014/02/28/127), annex IV | Annex IV, apartat **3.2 «Módulos profesionales»** | 2026-09-30 | `VERIFICADA` |
| Informàtica d’oficina | Grau bàsic | [RD 356/2014](https://www.boe.es/eli/es/rd/2014/05/16/356), annex VII | Annex VII, apartat **3.2 «Módulos profesionales»** i apartat **3.3 «Desarrollo de los módulos»** (RA i criteris dels 9 mòduls) | 2026-09-30 | `VERIFICADA` (reverificat el 30-09-2026; vegeu I-4) |
| Sistemes Microinformàtics i Xarxes | Grau mitjà | [RD 1691/2007](https://www.boe.es/eli/es/rd/2007/12/14/1691) | Pendent | 2026-09-29 | `VERIFICADA` (apartat `PENDENT`) |
| Administració de Sistemes Informàtics en Xarxa | Grau superior | [RD 1629/2009](https://www.boe.es/eli/es/rd/2009/10/30/1629) | Pendent | 2026-09-29 | `VERIFICADA` (apartat `PENDENT`) |
| Desenrotllament d’Aplicacions Multiplataforma | Grau superior | [RD 450/2010](https://www.boe.es/eli/es/rd/2010/04/16/450) | Pendent | 2026-09-29 | `VERIFICADA` (apartat `PENDENT`) |
| Desenrotllament d’Aplicacions Web | Grau superior | [RD 686/2010](https://www.boe.es/eli/es/rd/2010/05/20/686) | Pendent | 2026-09-29 | `VERIFICADA` (apartat `PENDENT`) |

**Nota sobre els reials decrets del títol:** l’apartat 3.2 del RD 127/2014 i
l’apartat 3.2 del RD 356/2014 **no distribueixen els mòduls per curs**; només
enumereixen els mòduls del títol. El RD 127/2014 enumera `3032. Formación en
centros de trabajo`; el RD 356/2014, `3033. Formación en centros de trabajo`.
Cap dels dos Reials decrets conté els codis `CV0006`, `3159` ni `3160`. Per a
aquest cicles, la comesesa curricular és autonòmica (vegeu la secció següent).

## Separació de fonts: què ve de l’estatal i què ve de l’autonòmic

Aquesta separació és deliberada i està verificada el 30-09-2026 amb cerques de
text complet als dos documents oficials. És la que ha generat la incidència
**I-4** de `fonts/registre-fonts.md`.

| Element | Font estatal (Reial decret del títol) | Font curricular valenciana (Decret 117/2025) |
|---|---|---|
| Identificació, durada total, competència general i competències del títol | **Sí** (F-026 RD 127/2014, Annex IV · F-027 RD 356/2014, Annex VII) | Remet al RD (art. 3.1 del Decret 117/2025) |
| Relació de mòduls del títol | **Sí** (apartat 3.2, sense ordre per curs) | Substitueix i amplia alguns codis (art. 3.2 i Anexo III-A) |
| **RA, criteris d’avaluació, continguts bàsics i orientacions pedagògiques** dels mòduls professionals | **Sí** (apartat 3.3 «Desarrollo de los módulos»). L’art. 3.2 del Decret 117/2025 els declara «prescriptivos» | No els reproduïx, excepte del mòdul `3159` (Annex I) |
| Distribució de mòduls **per curs** i hores anuals | **No** | **Sí** (Anexo III-A; hi remet l’art. 3.8, pàg. 4/58) |
| Mòduls de l’àmbit de Comunicació i Ciències Socials i de Ciències Aplicades | Codis **estatals** `3009`/`3019` i `3011`/`3012` | Codis **autonòmics** `3161`/`3162` i `3163`/`3164` (Anexo III-A) |
| ODS i continguts transversals | Cap capçalera ni cap relació d’ODS al RD 356/2014 | **Sí**: preàmbul (ODS 4, 8, 10, 12), art. 4.1, art. 5.2, art. 10.3 (F-035) |

**Cerces de text complet del 30-09-2026 al [RD 356/2014](https://www.boe.es/eli/es/rd/2014/05/16/356)** (HTTP 200, 1.658.749 bytes, SHA-256 `d9094c00…ac8c0b`): `3161` = **0** · `3162` = **0** · `3163` = **0** · `3164` = **0** · `desdoblamiento` = **0** · `3032` = **0** · `3033` = **5** · `CV0006` = 0 · `3159` = 0 · `3160` = 0.

**Conseqüència pràctica:** els codis `3161`, `3162`, `3163` i `3164` **no
provenen del RD 356/2014**, sinó del **Decret 117/2025, Anexo III-A, pàg. 34/58**
(Informática de oficina; `3162` i `3164` al 2n curs). El RD 356/2014, en canvi,
tracta les matèries equivalents amb `3009`/`3019` («Ciencias aplicadas I/II») i
`3011`/`3012` («Comunicación y sociedad I/II»), i el seu apartat 3.3 en detalla
l’única cosa que sí que hi consta: RA, criteris, continguts bàsics, orientacions
pedagògiques i una durada total per mòdul.

**Avís sobre les hores:** el camp «Duración» de l’apartat 3.3 del RD (p. ex.
`3016` = **115 h**) són hores totals del mòdul al cicle segons l’estatut
estatal. **No substitueixen** les hores anuals curriculars de la comesesa
valenciana: per a `3016` del 2n curs preval la taula de F-032 (10 h/sem ·
332 h/any). No s’han de barrejar les dues xifres.

## Desplegament curricular autonòmic (Comunitat Valenciana)

El Reial decret del títol **no distribueix els mòduls per curs**. Per als cicles de
grau bàsic, aquesta comesesa la fixa el Decret 117/2025, de 5 d’agost, del
Consell (DOGV núm. 10172, de 13.08.2025; CVE `DOGV-C-2025-32763`). L’**article 3.8**
del decret (pàg. 4/58) remet expressament a l’annex III-A: *«La secuenciación, duración y
distribución horaria de cada ciclo formativo está determinada en el anexo III-A de
este decreto»*.

| Cicle | Norma curricular valenciana | Apartat i pàgina exacta | Data | Estat |
|---|---|---|---|---|
| Informàtica d’oficina | [Decret 117/2025 (PDF oficial DOGV)](https://dogv.gva.es/datos/2025/08/13/pdf/2025_32763_es.pdf) (F-032) | **Anexo III-A «Secuenciación y carga horaria», pàgina 34 de 58** de l’edició DOGV (encapçalament de l’annex a la pàg. 17/58) | 2026-10-01 | `VERIFICADA` |
| Informàtica i comunicacions | [Decret 117/2025 (PDF oficial DOGV)](https://dogv.gva.es/datos/2025/08/13/pdf/2025_32763_es.pdf) (F-032) | **Anexo III-A «Secuenciación y carga horaria», pàgina 35 de 58** de l’edició DOGV (encapçalament de l’annex a la pàg. 17/58) | 2026-10-01 | `VERIFICADA` |

Les dues pàgines estan dins del mateix apartat «INFORMÁTICA Y COMUNICACIONES»
(nom de família professional), sota els epígrafs «Informática de oficina» i
«Informática y comunicaciones». Les dues taules tenen la capçalera literal
`Familia / Código / Módulo / hrs-sem / hrs-año` i inclouen les files `Total 1º`,
`Total 2º` i `Total ciclo`.

**Validesa:** el PDF oficial es va revalidar el 30-09-2026 i una altra vegada el
**1 d’octubre de 2026** (HTTP 200, 885.828 bytes, 58 pàgines, SHA-256
`10e95e822348f6120e64e794185b965bd021b745f0e4b599131512e69be9f5ef`, idèntic a
les còpies del 29 i del 30-09-2026). En vigor des del 14.08.2025 (disposició
final segona). La remissió a l’annex III-A és a l’**article 3.8, pàg. 4/58**
(vegeu la incidència I-5 de `fonts/registre-fonts.md`).

## ODS i continguts transversals (Comunitat Valenciana)

Per als **ODS** i els **temes transversals** dels cicles de grau bàsic
valencians, la font curricular és el mateix Decret 117/2025, però en uns altres
apartats dels de la comesesa horària. Es registra amb l’ID **F-035** a
`fonts/registre-fonts.md`.

| Contingut | Apartat i pàgina exacta del Decret 117/2025 | Data | Estat |
|---|---|---|---|
| ODS que el decret identifica per als cicles de grau bàsic: **ODS 4, 8, 10 i 12** | **Preàmbul, pàg. 2 de 58** | 2026-09-30 | `VERIFICADA` |
| Els tres àmbits del cicle (Comunicació i Ciències Socials / Ciències Aplicades / Professional) i el projecte anual | **Article 4.1, pàg. 4 de 58** | 2026-09-30 | `VERIFICADA` |
| RA que es treballen transversalment en el projecte intermodular | **Article 5.2, pàg. 5 de 58** | 2026-09-30 | `VERIFICADA` |
| Cultura transversal que s’ha de cultivar o crear (prevenció de riscos, respecte ambiental, qualitat, creativitat, innovació, igualtat de gènere, respecte a la diversitat, igualtat d’oportunitats, disseny per a totes les persones, accessibilitat universal) | **Article 10.3, pàg. 7 de 58** | 2026-09-30 | `VERIFICADA` |
| Organització de l’àmbit de Comunicació i Ciències Socials en matèries (aplica als mòduls `3161`/`3162`, **no** al professional `3016`) | **Anexo III-B, pàg. 45 de 58**; taula d’Informática de oficina a la **pàg. 53 de 58** | 2026-09-30 | `VERIFICADA` |
| Relació d’ODS o de temes transversals amb el mòdul `3016` en concret | **Cap** | 2026-09-30 | `PENDENT` |

**Resultat de les cerques al PDF oficial (30-09-2026):** `ODS` = 1 coincidència
(únicament el preàmbul); `2030` = 0; `temas transversales` = 0; `coeducaci` = 0;
`ciudadanía` = 0. El decret **no conté cap llista de «temes transversals»**, i
tampoc assigna ODS ni contingut transversal mòdul a mòdul. Als portals de la
Conselleria (F-011 «Cicles formatius de grau bàsic» i F-016 «Normativa») no s’hi
ha trobat cap document curricular sobre ODS ni temes transversals: tots dos van
donar 0 coincidències i cap enllaç a cap currículum de grau bàsic.

**Conseqüència:** la vinculació d’un ODS o d’un tema transversal al mòdul
`3016` continua sent `PENDENT`. La font de RA i criteris de `3016` és el
RD 356/2014 (F-027), que **no** conté cap capçalera ni cap relació d’ODS
(dins l’Annex VII, l’única menció a «desarrollo sostenible» és al mòdul `3019`).

**Informació de consulta (no normativa):** els dosiers de cicle del
[publicador de cicles](https://ceice.gva.es/es/web/formacion-profesional/publicador-de-cicles)
reprodueixen una taula de mòduls per curs que **no coincideix** amb l’annex III-A
en les hores. Hi ha dos incidències registrades: la pàgina del 1r curs (F-033)
assigna a `3031` hores que la norma dona a `3016` del 2n curs, i la pàgina del 2n
curs (F-034 i F-036, mateixa URL) dona hores pròpies d’Informática y
comunicaciones. Vegeu
`fonts/registre-fonts.md`, apartat «Incidències registrades». **Per a qualsevol
distribució per curs o hora, preval el Decret 117/2025, Anexo III-A.**

## Regla d’extracció

El `gestor-fonts` ha de consultar l’annex del títol i registrar la ubicació
concreta on apareixen la distribució per cursos i els mòduls. Si hi ha una
actualització posterior o una adaptació curricular valenciana, l’ha d’afegir al
registre sense substituir ni confondre la font estatal.
