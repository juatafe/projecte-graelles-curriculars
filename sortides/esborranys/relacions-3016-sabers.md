# Integració de sabers, ODS i temes transversals · mòdul `3016` · Fase 2

Mòdul: **3016 «Instalación y mantenimiento de redes para transmisión de datos»** ·
FP · família Informàtica i Comunicacions · grau bàsic · cicle **Informàtica d'oficina
(T.P.B.)** · **2n curs** · Comunitat Valenciana.

Aquest document **no crea cap contingut curricular**. Desglossa en sabers el que ja
està extret de la font, hi relates els 44 criteris d'avaluació i hi propos —
sempre com a **proposta pedagògica**, mai com a exigència — les relacions amb els
ODS i els temes transversals.

> **Regla de ferro d'aquest document.** Al mòdul `3016` **no hi ha cap vinculació
> acreditada d'ODS ni de temes transversals**. Per tant, **cap relació d'aquest
> tipus no pot tenir l'estat `VERIFICADA`**. La categoria `VERIFICADA` aplicada al
> mòdul és **buida** i no s'ha d'emplenar. El que sí que es proposa porta sempre
> l'etiqueta `PROPOSTA` i la remissió `V-3016-ODS` / `V-3016-TT`, que són
> `PENDENT`.

> **Correcció posterior a la validació independent (2026-10-01).** Aquest fitxer
> s'ha corregit després de l'informe de validació de la fase 4, que va detectar el
> defecte **D-1**: contingut oficial de F-037 sense cap itinerari
> d'integració (`CB b5.i6` i les vinyetes `OP v7` i `OP v8`). **Cap contingut nou no
> s'ha inventat** i **cap criteri oficial no s'ha creat, suprimit ni reescrit**.
> Per al que s'ha corregit, com i per què, vegeu **§12**.

---

## 1. Capçalera de traçabilitat

### 1.1 Fonts usades en aquest document

| Font | Organisme i títol | Apartat consultat | Data de consulta | Què acredita ací | Estat |
|---|---|---|---|---|---|
| **F-037** | BOE · Reial decret 356/2014, de 16 de maig (BOE-A-2014-5591), **versió consolidada vigent** («Última actualización publicada el **28/05/2024**») · [URL](https://www.boe.es/eli/es/rd/2014/05/16/356/con) | **Annex VII**, apartat **3.3 «Desarrollo de los módulos»**, bloc **`Código: 3016.`** | **2026-10-01** | Els **6 resultats d'aprenentatge**, els **44 criteris d'avaluació**, els **6 blocs de continguts bàsics (29 ítems)** i les **orientacions pedagògiques (4 paràgrafs + 8 vinyetas)**. **És la font a citar per a RA, criteris i continguts.** | `VERIFICADA` |
| **F-027** | BOE · Reial decret 356/2014, **«TEXTO ORIGINAL» de 2014** · [URL](https://www.boe.es/eli/es/rd/2014/05/16/356) | Annex VII, apartat 3.3, bloc `Código: 3016.` | 2026-09-30 · reverificat 2026-10-01 | **Origen de la transcripció** dels blocs literals que es reprodueixen ací. **No s'hi atribueix cap valor normatiu** sobre el text vigent. | `VERIFICADA` (amb reserva de versió, vegeu I-8) |
| **F-038** | BOE · Reial decret 498/2024, de 21 de maig (BOE-A-2024-10683) | **Disposició addicional sisena** · article sisè (modificació de l'apartat 3.3 dels annexos) | 2026-10-01 | La denominació nova **«competencias profesionales y para la empleabilidad»** amb què s'han de llegir les orientacions pedagògiques de `3016`. Explica per què el mòdul no ha canviat. | `VERIFICADA` |
| **F-032** | DOGV · Decret 117/2025, de 5 d'agost, del Consell (DOGV núm. 10172 de 13.08.2025; CVE DOGV-C-2025-32763) | **Anexo III-A «Secuenciación y carga horaria»**, taula «Informática de oficina», **pàg. 34/58** (remissió a l'**art. 3.8**, pàg. 4/58) | 2026-10-01 | Les hores curriculars del mòdul: **10 h/setmana · 332 h/any**. | `VERIFICADA` |
| **F-035** | DOGV · Decret 117/2025 (mateix PDF oficial) | **Preàmbul, pàg. 2/58** (ODS) · **art. 4.1, pàg. 4/58** · **art. 5.2, pàg. 5/58** · **art. 10.3, pàg. 7/58** · **Anexo III-B, pàg. 45/58** (taula d'Informática de oficina, **pàg. 53/58**) | 2026-09-30 | Els **ODS** i els **continguts transversals** en l'àmbit valencià. **És la font curricular dels ODS i dels temes transversals**, però **no assigna cap dels dos a mòduls**. | `VERIFICADA` |
| **F-001** | ONU · catàleg d'ODS · [URL](https://sdgs.un.org/goals) | Objectius 4, 8, 10 i 12 | **2026-10-01 (reverificació feta en aquesta execució)** | **Només el text literal de la denominació de cada objectiu.** HTTP 200, 59.139 bytes, SHA-256 `4f0bcff7df8a74d305bc2c030f77389a5b6833531995431411cad1688a7e0a49`. | `VERIFICADA` **com a font del text, no com a font curricular** |

### 1.2 Regla de prevalència aplicada

S'aplica la regla resultant de `fonts/registre-fonts.md`, punt per punt:

| # | Regla | Aplicació en aquest document |
|---|---|---|
| 1 | Distribució de mòduls per curs i hores → **F-032**, Anexo III-A | **Aplicada.** Tota la secció 8 (hores) usa **10 h/setmana · 332 h/any**. |
| 2 | Identitat del títol, denominació i mòduls → Reial decret del títol | **Aplicada.** |
| 3 | RA i criteris d'avaluació → Reial decret del títol, **versió consolidada vigent** (**F-037**), Annex VII apartat 3.3, perquè l'**art. 3.2** del Decret 117/2025 els declara «prescriptivos» | **Aplicada.** Tots els RA i criteris es citen com a **F-037**. F-027 només com a origen de transcripció. |
| 4 | ODS i continguts transversals en l'àmbit valencià → **F-035** | **Aplicada.** Seccions 4 i 5. |
| 5 | Dosiers i fitxes de cicle a CEICE (F-033 / F-034 / F-036) → informació de consulta, mai normativa | **Aplicada.** **No s'ha usat cap d'aquestes fonts.** |
| 6 | Catàleg de les Nacions Unides (**F-001**) → acredita només el text de l'objectiu, mai la seua exigibilitat curricular | **Aplicada.** F-001 no justifica cap exigència. |
| 7 | Modificacions d'un reial decret de títol → **F-038** | **Aplicada** per a la disposició addicional sisena i per a l'estat del mòdul. |
| 8 | Caràcter del camp «Duración» dels mòduls professionals → `PENDENT` (I-7); per a les hores reals del curs preval F-032 | **Aplicada.** `Duración: 115 horas.` **no s'ofereix com a horari del curs.** |
| 9 | Cap dada dels punts 1, 2, 3 i 4 no s'ha d'extraure de cap altre document | **Aplicada.** No hi ha cap **font nova**. L'única consulta addicional ha estat la **reverificació de F-001** (font ja registrada), que no aporta cap dada curricular: només el text de la denominació dels objectius. Vegeu P-14. |

### 1.3 Advertiment sobre les orientacions pedagògiques (F-038)

Les orientacions pedagògiques de `3016` diuen literalment:

```text
y las competencias profesionales, personales y sociales a), b), c), d), e), f), g), h) e i), del título.
```

La **disposició addicional sisena** del RD 498/2024 (F-038) ordena literalment:

```text
En todos los reales decretos objeto de la presente norma, las referencias contenidas en los anexos a las «competencias profesionales, personales y sociales» deben entenderse hechas a «competencias profesionales y para la empleabilidad».
```

Per tant, **en aquest document les orientacions pedagògiques de `3016` es llegeixen com
a «competencias profesionales y para la empleabilidad»**. El text és el mateix, però
la denominació és la nova. Ho deixa nota.

### 1.4 Etiquetes usades

| Etiqueta | Significat |
|---|---|
| `[TEXT EXTRET]` | transcripció literal de F-037. **Citables com a text oficial.** Es conserven els espais especials del document oficial: espai fi `U+2003` (entre numeració i text), guion fi `U+2012` (vinyeta), espai fi fi `U+2002` (després de la vinyeta). |
| `[RESUM]` | síntesi meua de text literal. **No és text oficial.** Indico sempre de quins literals deriva. |
| `[INTERPRETACIÓ]` | lectura meua. No té valor normatiu. |
| `[PROPOSTA]` | relació pedagògica que **cap font obliga**. Ha de passar a la revisió docent. |
| `VERIFICADA` / `PROPOSTA` / `PENDENT` | estat d'una **relació**, segons la skill `integracio-sabers`. |

### 1.5 Criteri de codificació

La norma **no assigna cap codi als RA ni als criteris**. Els codis `SB-3016-nn`
(sabers), `ACT-n` (activitats) i les referències `CB b#.i#` / `OP v#` són **del
projecte** i es declaren com a tals. La numeració literal de la norma (`1.`–`6.` per
a RA, `a)`–`h)` per a criteris) es conserva intacta i és la que mana.

---

## 2. Desglossament de sabers

### 2.1 Regla de derivació aplicada

Tots i cadascun dels sabers de la secció **deriven de dos tipus de text literal de
F-037**, i de cap altre:

- els **29 continguts bàsics** (*contenidos básicos*), agrupats en 6 blocs amb
  capçalera literal (referència `CB b#.i#`); i
- les **orientacions pedagògiques** (*Orientaciones pedagógicas*), amb 8 vinyetas
  (referència `OP v#`) i els seus 4 paràgrafs.

**Cap saber nou sense origen literal.** Quan un criteri conté un element que els
continguts bàsics **no** anomenen (per exemple, els tipus de caixa del criteri `1d`),
el saber resultant es marca `[RESUM]` i **es deixa constància de la reserva** al
§3. Quan el criteri **no té cap suport** en cap contingut bàsic, es declara
`SENSE COBERTURA` i **no es crea cap saber**.

### 2.2 Recompte

| Tipus | Definició | Nombre |
|---|---|---|
| **Saber** | coneixement: què són les coses i com són | **18** |
| **Saber fer** | habilitat pràctica: fer-les amb una tècnica o una eina | **14** |
| **Saber estar** | actituds, valors i comportaments exigits en l'exercici de la funció | **8** |
| | **Total** | **40** |

**Recompte del 2026-10-01 (correcció D-1).** El recompte passa de 39 a **40** per
l'addició de `SB-3016-40`, que deriva de `CB b5.i6` (§12.1). Cap saber no s'ha
suprimit ni reanomenat: els codis `SB-3016-01` … `SB-3016-39` es mantenen tal com
estaven.

### 2.3 Sabers · tipus **SABER** (coneixement) — 18

| ID | Etiqueta | Text del saber | Origen literal (F-037, Annex VII 3.3) | RA | Criteris que avalua |
|---|---|---|---|---|---|
| **SB-3016-01** | `[TEXT EXTRET]` | «Instalaciones de infraestructuras de telecomunicación en edificios. Características.» | **CB bloc 1**, capçalera «Selección de elementos de redes de transmisión de voz y datos:», ítem 2 | RA 1 | `1a`, `1b` |
| **SB-3016-02** | `[TEXT EXTRET]` | «Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre otros.» | **CB bloc 1**, ítem 1 | RA 1 · RA 3 · RA 5 | `1c`, `3a`, `5d` |
| **SB-3016-03** | `[TEXT EXTRET]` | «Sistemas y elementos de interconexión.» | **CB bloc 1**, ítem 3 | RA 1 · RA 5 | `1b`, `5b`, `5c` |
| **SB-3016-04** | `[TEXT EXTRET]` | «Características y tipos de las canalizaciones: tubos rígidos y flexibles, canales, bandejas y soportes, entre otros.» | **CB bloc 2**, capçalera «Montaje de canalizaciones, soportes y armarios en redes de transmisión de voz y datos:», ítem 2 | RA 1 · RA 2 | `1b`, `2d`, `2e`, `2g` |
| **SB-3016-05** | `[RESUM]` | Característiques que permeten determinar la tipologia dels elements d'una instal·lació i, en particular, de les caixes: registres, armaris, «racks», caixes de superfície i de col·locar a obra. | Deriva de **CB bloc 1**, ítems 2 i 3 (característiques de les instal·lacions i sistemes d'interconnexió). **Reserva:** la llista literal de tipus de caixa (`registros, armarios, «racks», cajas de superficie, de empotrar`) només consta al **criteri `1d`**, no als continguts bàsics. | RA 1 | `1d` |
| **SB-3016-06** | `[TEXT EXTRET]` | «Características y tipos de las fijaciones.» (primera part de l'ítem) | **CB bloc 4**, capçalera «Instalación de elementos y sistemas de transmisión de voz y datos:», ítem 1 | RA 1 · RA 4 | `1e`, `1f`, `4e` |
| **SB-3016-07** | `[TEXT EXTRET]` | «Herramientas.» | **CB bloc 4**, ítem 3 | RA 2 · RA 4 | `2a`, `2h`, `4d`, `4h` |
| **SB-3016-08** | `[TEXT EXTRET]` | «Características. Ventajas e inconvenientes. Tipos. Elementos de red.» | **CB bloc 5**, capçalera «Configuración básica de redes locales:», ítem 1 | RA 5 | `5a`, `5b`, `5c` |
| **SB-3016-09** | `[TEXT EXTRET]` | «Identificación de elementos y espacios físicos de una red local.» | **CB bloc 5**, ítem 2 | RA 2 · RA 5 | `2c`, `5c`, `5e` |
| **SB-3016-10** | `[TEXT EXTRET]` | «Cuartos y armarios de comunicaciones.» | **CB bloc 5**, ítem 3 | RA 3 | `3e` |
| **SB-3016-11** | `[TEXT EXTRET]` | «Conectores y tomas de red.» | **CB bloc 5**, ítem 4 | RA 3 · RA 4 | `3f`, `4f` |
| **SB-3016-12** | `[TEXT EXTRET]` | «Dispositivos de interconexión de redes.» | **CB bloc 5**, ítem 5 | RA 1 · RA 5 | `1b`, `5c` |
| **SB-3016-13** | `[TEXT EXTRET]` | «Normas de seguridad. Medios y sistemas de seguridad.» | **CB bloc 6**, capçalera «Cumplimiento de las normas de prevención de riesgos laborales y de protección ambiental:», ítem 1 | RA 2 · RA 4 · RA 6 | `2h`, `4h`, `6b` |
| **SB-3016-14** | `[TEXT EXTRET]` | «Identificación de riesgos.» | **CB bloc 6**, ítem 3 | RA 6 | `6a`, `6c` |
| **SB-3016-15** | `[TEXT EXTRET]` | «Determinación de las medidas de prevención de riesgos laborales.» | **CB bloc 6**, ítem 4 | RA 6 | `6e` |
| **SB-3016-16** | `[TEXT EXTRET]` | «Sistemas de protección individual.» | **CB bloc 6**, ítem 6 | RA 6 | `6d`, `6e` |
| **SB-3016-17** | `[TEXT EXTRET]` | «La identificación de sistemas, elementos, herramientas y medios auxiliares.» | **OP**, vinyeta 1 de la llista «La definición de esta función incluye aspectos como:» | RA 1 · RA 2 · RA 4 | `1b`, `2a`, `4d` |
| **SB-3016-18** | `[TEXT EXTRET]` | «La identificación de los sistemas, medios auxiliares, sistemas y herramientas, para la realización del montaje y mantenimiento de las instalaciones.» | **OP**, vinyeta 1 de la llista «Las líneas de actuación en el proceso enseñanza aprendizaje… versarán sobre:» | RA 1 · RA 2 · RA 4 | `1b`, `2a`, `4d` |

### 2.4 Sabers · tipus **SABER FER** (habilitat pràctica) — 14

| ID | Etiqueta | Text del saber | Origen literal (F-037, Annex VII 3.3) | RA | Criteris que avalua |
|---|---|---|---|---|---|
| **SB-3016-19** | `[TEXT EXTRET]` | «Montaje de canalizaciones, soportes y armarios en las instalaciones de telecomunicación.» | **CB bloc 2**, ítem 1 | RA 2 | `2b`, `2c`, `2d`, `2f` |
| **SB-3016-20** | `[TEXT EXTRET]` | «Preparación y mecanizado de canalizaciones. Técnicas de montaje de canalizaciones y tubos.» | **CB bloc 2**, ítem 3 | RA 2 | `2d`, `2e`, `2g`, `4h` |
| **SB-3016-21** | `[TEXT EXTRET]` | «El montaje de las canalizaciones y soportes.» | **OP**, vinyeta 2 de la llista «La definición de esta función incluye aspectos como:» | RA 2 | `2b`, `2f` |
| **SB-3016-22** | `[TEXT EXTRET]` | «Recomendaciones en la instalación del cableado.» | **CB bloc 3**, capçalera «Despliegue del cableado:», ítem 1 | RA 3 | `3b`, `3g` |
| **SB-3016-23** | `[TEXT EXTRET]` | «Técnicas de tendido de los conductores.» | **CB bloc 3**, ítem 2 | RA 3 | `3b`, `3c` |
| **SB-3016-24** | `[TEXT EXTRET]` | «Identificación y etiquetado de conductores.» | **CB bloc 3**, ítem 3 | RA 3 · RA 4 | `3d`, `4b` |
| **SB-3016-25** | `[TEXT EXTRET]` | «El tendido de cables para redes locales cableadas.» | **OP**, vinyeta 3 de la llista «La definición de esta función incluye aspectos como:» | RA 3 | `3b`, `3c` |
| **SB-3016-26** | `[TEXT EXTRET]` | «Montaje de sistemas y elementos de las instalaciones de telecomunicación.» | **CB bloc 4**, ítem 2 | RA 4 | `4a`, `4c` |
| **SB-3016-27** | `[TEXT EXTRET]` | «Instalación y fijación de sistemas en instalaciones de telecomunicación.» | **CB bloc 4**, ítem 4 | RA 4 | `4c`, `4e` |
| **SB-3016-28** | `[TEXT EXTRET]` | «Técnicas de fijación: en armarios, en superficie.» | **CB bloc 4**, ítem 5 | RA 1 · RA 4 | `1f`, `4e` |
| **SB-3016-29** | `[TEXT EXTRET]` | «Técnicas de conexionados de los conductores.» | **CB bloc 4**, ítem 6 | RA 3 · RA 4 | `3f`, `4f` |
| **SB-3016-30** | `[TEXT EXTRET]` | «El montaje de los elementos de la red local.» | **OP**, vinyeta 4 de la llista «La definición de esta función incluye aspectos como:» | RA 4 · RA 5 | `4a`, `4c`, `5c` |
| **SB-3016-31** | `[TEXT EXTRET]` | «La integración de los elementos de la red.» | **OP**, vinyeta 5 de la llista «La definición de esta función incluye aspectos como:» | RA 5 | `5b`, `5c` |
| **SB-3016-40** | `[TEXT EXTRET]` | «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» | **CB bloc 5**, capçalera «Configuración básica de redes locales:», ítem 6 (el darrer del bloc) | RA 5 | **cap criteri de RA 5 el cobreix** — l'itinerari és a nivell de **RA 5** i d'**activitat** (`ACT-6`, `ACT-9`). Vegeu §3.10 i §12.1 |

> **`SB-3016-40` és l'únic saber d'aquest document sense criteri d'avaluació propi,
> i no és una casualitat de forma.** El motiu exacte és que **cap dels 44 criteris de
> F-037 avalua, ni tan sols amb el seu verb, una operació de configuració**: el
> motiu oficial és el **RA 5**, el text literal del qual és «Realiza operaciones
> básicas de configuración en redes locales cableadas relacionándolas con sus
> aplicaciones.». L'anàlisi criteri per criteri és a **§3.10** i la limitació que
> això genera, a **§9, `P-23`**.

### 2.5 Sabers · tipus **SABER ESTAR** (actituds i valors) — 8

| ID | Etiqueta | Text del saber | Origen literal (F-037, Annex VII 3.3) | RA | Criteris que avalua |
|---|---|---|---|---|---|
| **SB-3016-32** | `[TEXT EXTRET]` | «Cumplimiento de las normas de prevención de riesgos laborales y protección ambiental.» | **CB bloc 6**, ítem 2 | RA 6 | `6b`, `6h` |
| **SB-3016-33** | `[TEXT EXTRET]` | «Prevención de riesgos laborales en los procesos de montaje.» | **CB bloc 6**, ítem 5 | RA 2 · RA 4 · RA 6 | `2h`, `4h`, `6h` |
| **SB-3016-34** | `[TEXT EXTRET]` | «Cumplimiento de la normativa de prevención de riesgos laborales.» | **CB bloc 6**, ítem 7 | RA 6 | `6b`, `6h` |
| **SB-3016-35** | `[TEXT EXTRET]` | «Cumplimiento de la normativa de protección ambiental.» | **CB bloc 6**, ítem 8 | RA 6 | `6f`, `6g`, `6h` |
| **SB-3016-36** | `[RESUM]` | Actuar preventivament: identificar els riscos **abans** de manipulating materials, eines i màquines i relacionar-los amb les mesures que cal aplicar. | Deriva de **CB bloc 6**, ítems 3 i 4 («Identificación de riesgos.» + «Determinación de las medidas de prevención de riesgos laborales.»). | RA 6 | `6a`, `6c`, `6e` |
| **SB-3016-37** | `[RESUM]` | Fer servir els equips de protecció individual que corresponguin a cada operació de muntatge i manteniment, i relacionar-los amb la manipulació concreta. | Deriva de **CB bloc 6**, ítems 4 i 6 («Determinación de las medidas…» + «Sistemas de protección individual.»). **Reserva:** el llistat literal d'elements de seguretat de les màquines (`protecciones, alarmas, pasos de emergencia`) només consta al **criteri `6d`**, no als continguts bàsics. | RA 6 | `6d`, `6e` |
| **SB-3016-38** | `[RESUM]` | Assumir l'abast de la funció professional del mòdul, delimitat al literal següent: «instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos». **Reserva de etiqueta (D-6):** la formulació del saber és del projecte; **només el fragmente entre comilles angulars és literal**, i la primera part del text **no** és `[TEXT EXTRET]`. | **OP**, 1r paràgraf | tots els RA | (transversal a tots els RA) |
| **SB-3016-39** | `[RESUM]` | Treballar de manera segura, ordenada i neta en cada operació de muntatge i manteniment, com a **primer factor de prevenció de riscos**. | Deriva de **CB bloc 3**, ítem 1 («Recomendaciones en la instalación del cableado.») + **CB bloc 6**, ítems 5 i 7. **Reserva:** l'ordenança i la neteja com a primer factor de prevenció consten literalment al **criteri `6h`** i als continguts bàsics només com a normes de prevenció i de seguretat. | RA 2 · RA 3 · RA 4 · RA 6 | `2h`, `3g`, `4h`, `6h` |

### 2.6 Quin saber avalua quin criteri — visió ràpida

| RA | Criteris coberts | Sabers que els avaluen |
|---|---|---|
| RA 1 (6 criteris) | `1a`, `1b`, `1c`, `1d`, `1e`, `1f` — **6 de 6** | SB-01, SB-02, SB-03, SB-04, SB-05, SB-06, SB-12, SB-28 |
| RA 2 (8 criteris) | `2a` … `2h` — **8 de 8** | SB-04, SB-07, SB-09, SB-13, SB-17, SB-18, SB-19, SB-20, SB-21, SB-33, SB-39 |
| RA 3 (7 criteris) | `3a` … `3g` — **7 de 7** | SB-02, SB-04, SB-10, SB-11, SB-12, SB-22, SB-23, SB-24, SB-25, SB-29, SB-39 |
| RA 4 (8 criteris) | `4a`, `4b`, `4c`, `4d`, `4e`, `4f`, `4h` — **7 de 8**; `4g` **sense cobertura** | SB-03, SB-06, SB-07, SB-11, SB-13, SB-17, SB-18, SB-20, SB-24, SB-26, SB-27, SB-28, SB-29, SB-30, SB-33, SB-39 |
| RA 5 (7 criteris) | `5a` … `5g` — **7 de 7** | SB-02, SB-03, SB-08, SB-09, SB-12, SB-30, SB-31 · **+ SB-40**, que no avalua cap criteri (§3.10) |
| RA 6 (8 criteris) | `6a` … `6h` — **8 de 8** | SB-13, SB-14, SB-15, SB-16, SB-32, SB-33, SB-34, SB-35, SB-36, SB-37, SB-39 |

---

## 3. Taula de correspondència criteri → saber → RA → activitat

### 3.1 Com llegir la taula

- **Criteri**: codi literal de la norma (`1a` = RA 1, criteri `a)`). La numeració
  literal `a)`–`h)` no existeix al document oficial com a codi; el codi compost és del
  projecte.
- **Origen literal**: d'on surt el coneixement que fa possible avaluar el criteri
  (`CB b#.i#` = bloc i ítem de continguts bàsics; `OP v#` = vinyeta de les
  orientacions pedagògiques).
- **Estat de la relació**: el **contingut** és `VERIFICADA` (F-037). La **relació**
  criteri↔saber↔activitat és sempre `PROPOSTA`, perquè cap norma la determina.
  Les reserves assenyalen els punts on el criteri conté elements que els continguts
  bàsics **no** anomenen.
- **`:—`** vol dir que el tipus de saber no intervé en aquell criteri.

### 3.2 RA 1 — *Selecciona los elementos que configuran las redes para la transmisión de voz y datos…*

```text
1. Selecciona los elementos que configuran las redes para la transmisión de voz y datos, describiendo sus principales características y funcionalidad.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `1a` | tipus d'instal·lacions relacionats amb les xarxes de transmissió de veu i dades | SB-3016-01 | :— | :— | ACT-1 | CB b1.i2 | `PROPOSTA` |
| `1b` | elements d'una xarxa: canalitzacions, cablejats, antenes, armaris, «racks» i caixes | SB-3016-01, SB-03, SB-04, SB-12 | :— | :— | ACT-1, ACT-2 | CB b1.i2, b1.i3, b2.i2, b5.i5 | `PROPOSTA` |
| `1c` | classificació dels tipus de conductors (par de coure, cable coaxial, fibra òptica…) | SB-3016-02 | :— | :— | ACT-2 | CB b1.i1 | `PROPOSTA` |
| `1d` | tipologia de les caixes (registres, armaris, «racks», de superfície, d'empotrar…) | SB-3016-05 | SB-3016-19 | :— | ACT-1 | CB b1.i2 + b1.i3 | `PROPOSTA` **amb reserva**: la llista literal de tipus de caixa no consta als continguts bàsics |
| `1e` | tipus de fixacions (tacos, brides, tornills,illemats, grapes…) | SB-3016-06 | :— | :— | ACT-2 | CB b4.i1 | `PROPOSTA` **amb reserva**: el llistat literal de fixacions no consta als continguts bàsics |
| `1f` | relació de les fixacions amb l'element a subjectar | SB-3016-06 | SB-3016-28 | :— | ACT-2, ACT-5 | CB b4.i1 + b4.i5 | `PROPOSTA` |

### 3.3 RA 2 — *Monta canalizaciones, soportes y armarios…*

```text
2. Monta canalizaciones, soportes y armarios en redes de transmisión de voz y datos, identificando los elementos en el plano de la instalación y aplicando técnicas de montaje.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `2a` | tècniques i eines per a la instal·lació de canalitzacions i la seua adaptació | SB-3016-07, SB-17, SB-18 | SB-3016-19 | SB-3016-33 | ACT-3 | CB b4.i3 + OP v1/v6 | `PROPOSTA` |
| `2b` | fases típiques del muntatge d'un «rack» | :— | SB-3016-19, SB-3016-21 | :— | ACT-3 | CB b2.i1 + OP v2 | `PROPOSTA` **amb reserva**: la successió de fases no consta als continguts bàsics |
| `2c` | localització en un croquis dels llocs d'ubicació dels elements | SB-3016-09 | SB-3016-19 | :— | ACT-1, ACT-3 | CB b5.i2 + b1.i2 | `PROPOSTA` **amb reserva**: el croquis no consta als continguts bàsics |
| `2d` | preparació de la ubicació de caixes i canalitzacions | SB-3016-04 | SB-3016-19, SB-3016-20 | SB-3016-33 | ACT-3 | CB b2.i1, b2.i2 | `PROPOSTA` |
| `2e` | preparació i mecanització de canalitzacions i caixes | SB-3016-04 | SB-3016-20 | SB-3016-33 | ACT-3 | CB b2.i3 | `PROPOSTA` |
| `2f` | muntatge dels armaris («racks») interpretant el plànol | SB-3016-04 | SB-3016-19, SB-3016-21 | :— | ACT-3 | CB b2.i1 + OP v2 | `PROPOSTA` **amb reserva**: el plànol no consta als continguts bàsics |
| `2g` | muntatge de canalitzacions, caixes i tubs amb fixació mecànica assegurada | SB-3016-04 | SB-3016-20 | SB-3016-33 | ACT-3 | CB b2.i2 + b2.i3 | `PROPOSTA` |
| `2h` | aplicació de normes de seguretat en l'ús d'eines i sistemes | SB-3016-13 | SB-3016-20 | SB-3016-33, SB-3016-39 | ACT-3, ACT-7 | CB b6.i1 + b6.i5 | `PROPOSTA` |

### 3.4 RA 3 — *Despliega el cableado de una red de voz y datos…*

```text
3. Despliega el cableado de una red de voz y datos analizando su trazado.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `3a` | diferenciació dels mitjans de transmissió per a veu i dades | SB-3016-02 | :— | :— | ACT-4 | CB b1.i1 | `PROPOSTA` |
| `3b` | detalls del cablejat i del seu desplegament (categoria, espais, suport) | SB-3016-12 | SB-3016-22, SB-3016-23, SB-3016-25 | SB-3016-39 | ACT-4 | CB b3.i1 + b3.i2 + OP v3 | `PROPOSTA` |
| `3c` | ús de guies passacables i forma òptima de subjectar cable i guia | SB-3016-04 | SB-3016-23, SB-3016-25 | :— | ACT-4 | CB b3.i2 + b2.i2 | `PROPOSTA` **amb reserva**: les guies passacables no consten als continguts bàsics |
| `3d` | tall i etiquetatge del cable | SB-3016-24 | SB-3016-24 | SB-3016-39 | ACT-4 | CB b3.i3 | `PROPOSTA` |
| `3e` | muntatge dels armaris de comunicacions i els seus accessoris | SB-3016-10 | SB-3016-19 | :— | ACT-4 | CB b5.i3 | `PROPOSTA` **amb reserva**: els accessoris no consten als continguts bàsics |
| `3f` | muntatge i connexió de les preses d'usuari i els panells de parcheo | SB-3016-11 | SB-3016-29 | SB-3016-39 | ACT-4 | CB b5.i4 + b4.i6 | `PROPOSTA` **amb reserva**: els panells de parcheo no consten als continguts bàsics |
| `3g` | treball amb la qualitat i seguretat requerides | :— | :— | SB-3016-39 | ACT-4 | CB b3.i1 + b6.i5 | `PROPOSTA` **amb reserva**: criteri **sense criteri d'avaluació propi**; la qualitat i la seguretat només consten al contingut bàsic «Recomendaciones en la instalación del cableado.» |

### 3.5 RA 4 — *Instala elementos y sistemas de transmisión de voz y datos…*

```text
4. Instala elementos y sistemas de transmisión de voz y datos, reconociendo y aplicando las diferentes técnicas de montaje.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `4a` | ensamblatge dels elements formats per diverses peces | :— | SB-3016-26, SB-3016-30 | :— | ACT-5 | CB b4.i2 + OP v4 | `PROPOSTA` |
| `4b` | identificació del cablejat segons l'etiquetatge o els colors | SB-3016-24 | SB-3016-24 | :— | ACT-5 | CB b3.i3 | `PROPOSTA` **amb reserva**: els colors no consten als continguts bàsics |
| `4c` | col·locació dels sistemes o elements en el seu lloc d'ubicació | SB-3016-03 | SB-3016-26, SB-3016-27 | :— | ACT-5 | CB b4.i2 + b4.i4 | `PROPOSTA` |
| `4d` | selecció d'eines | SB-3016-07, SB-17, SB-18 | :— | SB-3016-33 | ACT-5, ACT-7 | CB b4.i3 + OP v1/v6 | `PROPOSTA` |
| `4e` | fixació dels sistemes o elements | SB-3016-06 | SB-3016-27, SB-3016-28 | SB-3016-33 | ACT-5 | CB b4.i1 + b4.i4 + b4.i5 | `PROPOSTA` |
| `4f` | connexió del cablejat amb els sistemes i elements, amb bon contacte | SB-3016-11 | SB-3016-29 | SB-3016-39 | ACT-5 | CB b4.i6 + b5.i4 | `PROPOSTA` |
| `4g` | col·locació d'embelleidors, tapes i elements decoratius | :— | :— | :— | ACT-5 | **cap** | **`SENSE COBERTURA`** — vegeu §3.8 |
| `4h` | aplicació de normes de seguretat en l'ús d'eines i sistemes | SB-3016-13 | SB-3016-20 | SB-3016-33, SB-3016-39 | ACT-5, ACT-7 | CB b6.i1 + b6.i5 | `PROPOSTA` |

### 3.6 RA 5 — *Realiza operaciones básicas de configuración en redes locales cableadas…*

```text
5. Realiza operaciones básicas de configuración en redes locales cableadas relacionándolas con sus aplicaciones.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `5a` | principis de funcionament de les xarxes locals | SB-3016-08 | :— | :— | ACT-6 | CB b5.i1 | `PROPOSTA` |
| `5b` | tipus de xarxes i les seues estructures alternatives | SB-3016-03, SB-3016-08 | SB-3016-31 | :— | ACT-6 | CB b5.i1 + b1.i3 + OP v5 | `PROPOSTA` |
| `5c` | elements de la xarxa local identificats amb la seua funció | SB-3016-03, SB-08, SB-12, SB-09 | SB-3016-30, SB-3016-31 | :— | ACT-6 | CB b5.i1–i5 + b1.i3 + OP v4/v5 | `PROPOSTA` |
| `5d` | descripció dels mitjans de transmissió | SB-3016-02 | :— | :— | ACT-6 | CB b1.i1 | `PROPOSTA` |
| `5e` | interpretació del mapa física de la xarxa local | SB-3016-09 | :— | :— | ACT-1, ACT-6 | CB b5.i2 | `PROPOSTA` **amb reserva**: el «mapa físico» no consta literalment als continguts bàsics |
| `5f` | representació del mapa física de la xarxa local | :— | SB-3016-31 | :— | ACT-6 | CB b5.i2 + OP v5 | `PROPOSTA` **amb reserva**: la representació del mapa no consta literalment als continguts bàsics |
| `5g` | ús d'aplicacions informàtiques per representar el mapa físicos | :— | SB-3016-31 | :— | ACT-6 | **cap** (cap capçalera d'eines informàtiques als continguts bàsics) | `PROPOSTA` **amb reserva**: l'eina no la fixa cap contingut del mòdul |

> **Contingut bàsic del mateix bloc que cap fila d'aquesta taula no pot
> reproduir: `CB b5.i6`.** L'ítem 6 del bloc 5, «Configuración básica de los
> dispositivos de interconexión de red cableada e inalámbrica.», **no s'ha
> atribuït a cap dels 7 criteris de RA 5 perquè cap dels 7 el cobreix** — ni
> `5c`, que és el més proper i al qual li toca, sinó que el seu verb és
> `reconocido` i el contingut li assignat és `CB b5.i5`. L'anàlisi completa, el
> `saber` que l'ha assumit (`SB-3016-40`) i la limitació que hi ha quedat
> declarada són a **§3.10**.

### 3.7 RA 6 — *Cumple las normas de prevención de riesgos laborales y de protección ambiental…*

```text
6. Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y sistemas para prevenirlos.
```

| Criteri | Text literal (resum fidel) | Saber | Saber fer | Saber estar | Activitat | Origen literal | Estat de la relació |
|---|---|---|---|---|---|---|---|
| `6a` | riscos i nivell de perillositat de la manipulació de materials, eines, útils, màquines i mitjans de transport | SB-3016-14 | SB-3016-36 | SB-3016-36 | ACT-7 | CB b6.i3 | `PROPOSTA` **amb reserva**: el «nivel de peligrosidad» i els mitjans de transport no consten als continguts bàsics |
| `6b` | operació de les màquines respectant les normes de seguretat | SB-3016-13 | :— | SB-3016-32, SB-3016-34 | ACT-7 | CB b6.i1, b6.i2, b6.i7 | `PROPOSTA` |
| `6c` | causes més freqüents d'accidents en la manipulació de materials, eines i màquines de tall i conformació | SB-3016-14 | SB-3016-36 | SB-3016-36 | ACT-7 | CB b6.i3 | `PROPOSTA` **amb reserva**: la llista de causes no consta als continguts bàsics |
| `6d` | elements de seguretat de les màquines (proteccions, alarmes, passos d'emergència) i EPI (calçat, protecció ocular, indumentària) | SB-3016-16 | SB-3016-37 | SB-3016-37 | ACT-7 | CB b6.i6 | `PROPOSTA` **amb reserva**: els elements de seguretat de les màquines no consten als continguts bàsics |
| `6e` | relació de la manipulació de materials, eines i màquines amb les mesures de seguretat i protecció personal | SB-3016-15, SB-3016-16 | SB-3016-37 | SB-3016-37 | ACT-7 | CB b6.i4 + b6.i6 | `PROPOSTA` |
| `6f` | possibles fonts de contaminació de l'entorn ambiental | SB-3016-35 | :— | SB-3016-35 | ACT-8 | CB b6.i8 | `PROPOSTA` **amb reserva**: el llistat de fonts de contaminació no consta als continguts bàsics · **corregit (§12.2)**: `ACT-7` se'n ha retirat perquè no l'avalua |
| `6g` | classificació dels residus generats per a la retirada selectiva | SB-3016-35 | :— | SB-3016-35 | ACT-8 | CB b6.i8 | `PROPOSTA` **amb reserva**: la tipologia de residus no consta als continguts bàsics |
| `6h` | valoració de l'ordre i la neteja com a primer factor de prevenció | :— | :— | SB-3016-32, SB-33, SB-34, SB-35, SB-39 | ACT-8 | CB b6.i2, b6.i5, b6.i7, b6.i8 + b3.i1 | `PROPOSTA` **amb reserva**: «primer factor de prevención» no consta als continguts bàsics |

### 3.8 Criteri **sense cobertura**: `4g`

**Ho dic de forma explícita i sense emmascarar-lo.**

El criteri `4g` diu literalment:

```text
g) Se han colocado los embellecedores, tapas y elementos decorativos.
```

**Cap dels 29 continguts bàsics de `3016` parla d'embelleidors, tapes ni elements
decoratius.** Els 6 blocs de continguts bàsics tracten — Bloc 4 inclòs — de
«Características y tipos de las fijaciones», «Montaje de sistemas y elementos de las
instalaciones de telecomunicación», «Herramientas», «Instalación y fijación de
sistemas», «Técnicas de fijación: en armarios, en superficie» i «Técnicas de
conexionados de los conductores». Cap parla de l'acabat estètic de la instal·lació.

**Conseqüència:** no he creat cap saber per a `4g`, perquè hauria estat **inventar un
contingut curricular**. El criteri queda **sense cobertura curricular verificable** i
passa a `PENDENT` (§9, **P-3**). Si l'equip docent vol avallar-lo, cal una font que el
sustente —cap font del RD 356/2014 en el mòdul `3016` la conté— o una decisió
expressa del centre, que s'haurà de declarar com a **material complementari del
projecte, no com a contingut curricular**.

### 3.9 Recompte de cobertura dels 44 criteris

**Recompte autoritatiu:**

| Estat de cobertura | Nombre de criteris |
|---|---|
| `COBERTA` amb origen literal suficient | **24** |
| `COBERTA AMB RESERVA` (el criteri conté elements que els continguts bàsics **no** anomenen) | **19** |
| `SENSE COBERTURA` amb contingut literal del mòdul (`4g`) | **1** |
| **Total** | **44** |

Criteris `COBERTA` amb origen literal suficient (24):

`1a`, `1b`, `1c`, `1f`, `2a`, `2d`, `2e`, `2g`, `2h`, `3a`, `3b`, `3d`, `4a`, `4c`, `4d`, `4e`, `4f`, `4h`, `5a`, `5b`, `5c`, `5d`, `6b`, `6e`.

Criteris `COBERTA AMB RESERVA` (19):

`1d`, `1e`, `2b`, `2c`, `2f`, `3c`, `3e`, `3f`, `3g`, `4b`, `5e`, `5f`, `5g`, `6a`, `6c`, `6d`, `6f`, `6g`, `6h`.

Criteri `SENSE COBERTURA` (1):

`4g` — vegeu §3.8.

**Cap altre criteri queda fora.** Els 44 criteris de la norma estan tots tractats,
cap no s'ha omès i cap no s'ha fusionat.

### 3.10 Contingut oficial **amb itinerari, però sense criteri que l'avalui**: `CB b5.i6`

Text literal de F-037 (Annex VII, apartat 3.3, bloc `Código: 3016.`,
capçalera `Configuración básica de redes locales:`, **ítem 6 de 6** del bloc):

```text
‒ Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.
```

**És l'ítem central del RA 5.** El resultat d'aprenentatge ho diu `[TEXT EXTRET]`:

```text
5. Realiza operaciones básicas de configuración en redes locales cableadas relacionándolas con sus aplicaciones.
```

**Reexamen dels 7 criteris, un per un.** La pregunta correcta no és «quin criteri
empara el que queda», sinó «quin criteri parla de configurar». Aplicada al text
literal de cadascun:

| Criteri | Verb i objecte literals | Per què **no** cobreix `CB b5.i6` |
|---|---|---|
| `5a` | «Se han **descrito** los principios de funcionamiento de las redes locales.» | És coneixement, no operació. El seu contingut és `CB b5.i1`. Cap relació amb la configuració d'un equip. |
| `5b` | «Se han **identificado** los distintos tipos de redes y sus estructuras alternativas.» | Classificar tipus i topologies. Continguts: `CB b5.i1` + `CB b1.i3`. No parla de cap dispositiu concret. |
| `5c` | «Se han **reconocido** los elementos de la red local identificándolos con su función.» | **És el més proper i, tanmateix, no el cobreix.** El seu contingut és `CB b5.i5` «Dispositivos de interconexión de redes.» (`SB-3016-12`), és a dir, conèixer el dispositiu i la seua funció. *Reconèixer* un dispositiu i *configurar-lo* són actes diferents, i `5c` s'atura just abans de `CB b5.i6`. Atribuir-hi l'ítem seria **estendre el criteri per omplir un buit**, i això no es fa. |
| `5d` | «Se han **descrito** los medios de transmisión.» | Contingut `CB b1.i1`. Cap relació amb la configuració. |
| `5e` | «Se ha **interpretado** el mapa físico de la red local.» | Representació de la instal·lació, no ajust de paràmetres d'un dispositiu. Contingut `CB b5.i2`. |
| `5f` | «Se ha **representado** el mapa físico de la red local.» | Representar, no configurar. Contingut `CB b5.i2`. |
| `5g` | «Se han utilizado aplicaciones informáticas para representar el mapa físico…» | L'eina hi és per a *representar*. A més, aquesta fila ja té la seua reserva pròpia: **cap contingut del mòdul no fixa cap eina**. |

**I la resta del mòdul?** Cap altre criteri dels 44 no serveix: `1a`–`1f` parlen
de seleccionar i descriure elements, `2a`–`2h` i `4a`–`4h` de muntar i fixar,
`3a`–`3g` de desplegar cablejat, `6a`–`6h` de riscos. **Cap dels 44 criteris de
`3016` avalua, amb el seu verb, una operació de configuració.** Això no és una
manca meua: és com la norma distribueix l'avaluació d'aquest RA.

**Decisió, i què fa exactament:**

1. **Es crea `SB-3016-40`** (§2.4), `[TEXT EXTRET]`, tipus **saber fer**, origen
   **`CB b5.i6`**, RA 5. Text literal, sense parafrasejar: el contingut oficial
   recuperat el seu propi `saber` i deixa de ser una línia morta de l'Annex C.
2. **L'itinerari és de RA i d'activitat, no de criteri:** `ACT-6` (§6) i `ACT-9`
   (§6) el mobilitzen, i les dues es valoren amb instrument `[PROPOSTA]`
   (`P-17`). El professorat **sí que té lloc on introduir, ensenyar i valorar** el
   contingut, que era el que es queixava l'informe de validació.
3. **No s'estén cap criteri** i **no es crea cap criteri nou**. És que el criteri
   oficial no hi ha: la norma no el redacta.
4. **Queda una limitació declarada, no un defecte meu** (`P-23`): el contingut
   oficial `CB b5.i6` és exigible perquè el cobreix el RA 5, però **no hi ha cap
   criteri oficial que en permeti valorar la corresponsència**. Qualsevol nota que
   el professorat hi posi serà **instrument `PROPOSTA` sobre una activitat**, no
   avaluació d'un criteri. S'ha de llegir així i no com un criteri estès.

### 3.11 Contingut oficial **sense itinerari possible amb el material del mòdul**: `OP v8`

Text literal de F-037 (vinyeta 8 de 8 de les orientacions pedagògiques, última de
la llista «Las líneas de actuación en el proceso enseñanza aprendizaje que permiten
alcanzar las competencias del módulo versarán sobre:»):

```text
‒ La toma de medidas de las magnitudes típicas de las instalaciones.
```

**Primer, de què parla.** Les orientacions pedagògiques **no són continguts**:
són línies d'actuació pedagògica, és a dir, el camí que la norma marca per
assolir les competències. Per això `OP v8` demana de tractar la mesura **dins de**
l'ensenyament i l'avaluació del que ja hi ha, no crea un resultat d'aprenentatge
nou. Això es diu de manera explícita **perquè la solució correcta ací és
`PENDENT`, i s'ha de poder defensar.**

**Segon, la cerca als 44 criteris. Resultat: cap.** Cap dels 44 criteris conté
`medir`, `medida` en el sentit de magnitud, `magnitud`, `cinta`, `calibr`,
`longitud`, `diámetro`, `señal`, `temperatura`, `cotas` ni `medidas` en sentit
metrològic. Els dos punts on un docent hi podria acostar-s'hi **no hi serveixen**:

| Punt on sembla poder-se recolzar | Per què **no** serveix |
|---|---|
| `2c` «identificado en un croquis del edificio… los lugares de ubicación» i `2f` «Se han montado los armarios («racks») interpretando el plano» | Un croquis o un plànol es traça, en la pràctica, mesurant. Però **el text literal no diu «mesurar»**. Atribuir-hi `OP v8` seria convertir un hàbit professionalitzant en exigència curricular: exactament l'estirament de criteri que no es fa ací. Es queda documentat com a **possibilitat pedagògica**, no com a cobertura. |
| `6a` «Se han identificado los riesgos y el **nivel** de peligrosidad…» | `nivel de peligrosidad` és una valoració del risc, **no una mesura d'una magnitud**. A més, aquesta fila ja té la reserva que el «nivel de peligrosidad» no consta als continguts bàsics. |

**Tercer, la cerca als 29 continguts bàsics. Resultat: cap.** Cap dels 29 ítems
nomena magnituds, instruments de mesura ni operació de mesurar. I ací hi ha un
**fals amic** que cal deixar dit perquè tempta: `CB b6.i4` diu literalment
«Determinación de las **medidas** de prevención de riesgos laborales.». Allà
`medidas` són **mesures de prevenció**, no mesures de magnituds. Aquest ítem ja
origina `SB-3016-15`, `SB-3016-36` i `SB-3016-37` i **no s'ha de reutilitzar per
donar cobertura a `OP v8`**; seria una falsificació de sentit.

**Conclusió: `PENDENT` (`P-24`), i no per comoditat sinó perquè no hi ha res.** Amb
el material de F-037 no es pot construir cap itinerari d'integració curricular de
`OP v8` que no exigís inventar un contingut, un criteri o una eina que la norma no
dona. **No es crea cap saber i no es crea cap criteri nou.**

**El que sí que es deixa al professorat, i el que no arregla el pendent.** Com que
les orientacions pedagògiques són línies d'actuació i no continguts, res no
impedeix que l'equip docent treballe la mesura de longituds i recorreguts com a
pràctica de taller dins d'`ACT-3` i `ACT-9`. Però això s'etiqueta **`[PROPOSTA]`**
i es declara **material complementari del projecte, no contingut curricular**: no
crea cap criteri, no dona cap nota oficial i **no resol `P-24`**, que continuarà
obert perquè el contingut oficial no té itinerari possible.

### 3.12 Contingut oficial **cobert de manera equivalent**: `OP v7`

Text literal de F-037 (vinyeta 7 de 8, mateixa llista que `OP v8`):

```text
‒ La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.
```

Aquesta vinyeta **no crea cap saber nou**, i això s'ha decidit de manera explícita,
no per omissió. El seu sentit literal està **ja cobert** per
`SB-3016-26` / `CB b4.i2`:

| | Text literal |
|---|---|
| `OP v7` | «La aplicación de técnicas de montaje de **sistemas y elementos** de **las instalaciones**.» |
| `CB b4.i2` | «**Montaje** de **sistemas y elementos** de **las instalaciones de telecomunicación**.» |

**Reserva de literalitat, i és la raó de no duplicar el saber:** els dos textos
**no són idèntics caràcter per caràcter** (`las instalaciones` /
`las instalaciones de telecomunicación`; `La aplicación de técnicas de` /
`Montaje de`). La cobertura és **de sentit equivalent, no de text idèntic**, i per
això `OP v7` **no pot figurar com el text d'un `saber` `[TEXT EXTRET]` propi**
sense que el mateix contingut quedi duplicat. El que sí que es fa, i que és el
tractament correcte:

- **`OP v7` queda declarat com a co-origin de `SB-3016-26`**, juntament amb
  `CB b4.i2` (§2.4), i com a origen equivalent al criteri `4a`
  («Se han ensamblado los elementos que consten de varias piezas») i al criteri
  `4c` («Se han colocado los sistemas o elementos… en su lugar de ubicación»), que
  és a dir, a través de la mateixa ruta que ja existia.
- **Es declara redundant.** Setena vinyeta de les vuit i setena de les que tenen
  itinerari: no afegeix cap contingut nou perquè el que diu ja s'ensenya, s'avalua
  i es traça.
- **Enllaç amb el que ja existia:** la justificació de `ACT-5` (§6) ja citava
  textualment aquesta vinyeta, però sense cap saber que la tingués com a origen.
  Ara el text de l'activitat i la taula de sabers **diuen el mateix**.

### 3.13 Recompte de cobertura del **contingut oficial** (i què queda fora)

| Contingut oficial de F-037 | Recompte | Notes i casos que no arriben al 29 o a la 8 |
|---|---|---|
| Ítems de continguts bàsics amb **cap saber** que en deriva | **28 de 29** | `CB b5.i6` **en té** (`SB-3016-40`, §3.10). L'única manera de pujar a 29 seria un altre saber que repetís el mateix contingut: no es fa. |
| Ítems de continguts bàsics amb **algún criteri que els avalui** | **27 de 29** | `CB b5.i6` (cap criteri) i `CB b4.i1` (parcial: només la primera part, «Características y tipos de las fijaciones.», és text de `SB-3016-06`; la segona, «Técnicas de montaje.», està coberta **en sentit** per `SB-3016-20` i `SB-3016-28` però no és el text de cap saber — vegeu l'incidència D-5 de l'informe de validació) |
| Vinyetes de les orientacions pedagògiques amb **cap saber** que en deriva | **7 de 8** | `OP v7` redundant (§3.12) · `OP v8` **`PENDENT`** (§3.11) |
| Ítems de continguts bàsics perduts | **0** | |
| Vinyetes de les orientacions perdudes | **0** | |

**Cap element del text oficial s'ha perdut ni ha quedat en silenci.** Els dos que
no tenen itinerari possible estan **nomenats, amb el motiu exacte i amb codi de
pendent** (`P-23` i `P-24`), i el tercer, el redundant, **consta com a tal**
(`P-25`). Això era exactament el que mancava.

---

## 4. Relació amb els ODS

### 4.1 Advertencia prèvia, sense matisos

1. **Les cerques de text complet al bloc del mòdul `3016` de F-037 donen 0
   coincidències** de `ODS`, `objetivos de desarrollo sostenible`, `Agenda 2030`,
   `desarrollo sostenible`, `sostenible`, `sostenibilidad` i `transversal`.
2. Al **Decret 117/2025 (F-035)**, `ODS` apareix **1 sola vegada** a tot el PDF
   oficial, i és al **preàmbul**. **El decret no assigna cap ODS a cap mòdul.**
3. Els quatre ODS de la taula següent estan `VERIFICADA` **a nivell de cicle**,
   **mai de mòdul**. La remissió que ho constata és **`V-3016-ODS`, que és
   `PENDENT`**.
4. Per tant: **totes quatre relacions són `PROPOSTA`** i **cap no pot pujar a
   `VERIFICADA`** amb les fonts disponibles. La categoria `VERIFICADA` és **buida** en
   aquesta secció.
5. **F-001 acredita el text de la denominació de l'objectiu i no la seua exigibilitat
   curricular.** No s'ha usat per justificar cap obligació.

### 4.2 Taula de relacions ODS

| ID | Text literal de l'objectiu (**F-001**, només font del text) · consulta 2026-10-01 | Denominació literal al Decret (**F-035**, preàmbul, pàg. 2/58) | Justificació pedagògica de la proposta | Víncul possible al mòdul | Font i apartat | Estat |
|---|---|---|---|---|---|---|
| **ODS-04** | *«Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.»* | «el objetivo **4 de educación de calidad**» | L'activitat `ACT-9` (projecte integrador) i la `ACT-1` (mapa de l'edifici) són escenaris on l'alumne aprén una professió tècnica de base i documenta el seu propi procés, cosa que aproxima l'aprenentatge al llarg de la vida. | `ACT-1`, `ACT-9` | F-035, preàmbul, pàg. 2/58 (2026-09-30) · F-001 (2026-10-01) | **`PROPOSTA`** |
| **ODS-08** | *«Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all.»* | «el objetivo **8 trabajo decente y crecimiento económico**» | `ACT-4` i `ACT-5` treuen profit de les orientacions pedagògiques literals —«instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos»— que són la porta d'entrada a l'ocupació tècnica en instal·lacions. | `ACT-4`, `ACT-5`, `ACT-9` | F-035, preàmbul, pàg. 2/58 (2026-09-30) · F-001 (2026-10-01) | **`PROPOSTA`** |
| **ODS-10** | *«Reduce inequality within and among countries.»* | «el objetivo **10, reducción de desigualdades, como reto global y actuación autonómica**» | Les tasques de `ACT-9` es plantegen sobre un «petit entorn» (paraula literal de les orientacions pedagògiques): el criteri d'avaluació es fa diagnòstic **dins del mateix grup i context**, amb rúbrica compartida, cosa que treballa l'equitat de l'experiència d'aprenentatge. | `ACT-9` | F-035, preàmbul, pàg. 2/58 (2026-09-30) · F-001 (2026-10-01) | **`PROPOSTA`** |
| **ODS-12** | *«Ensure sustainable consumption and production patterns.»* | «el objetivo **12, producción y consumo responsables**» | `ACT-8` (retirada selectiva de residus, neteja i ordre) connecta amb ODS-12 **només per via pedagògica**. **Ho deixo dit amb tot l'esclareixement:** l'única dada ambiental literal del mòdul és `protección ambiental` (4 vegades: títol del RA 6, capçalera del bloc 6 i 2 vinyetes), que és **contingut curricular de prevenció i protecció ambiental, no capçalera d'ODS ni declaració de sostenibilitat**. **No la converteixo en vincle d'ODS sense fonamentar-lo.** | `ACT-7`, `ACT-8` | F-035, preàmbul, pàg. 2/58 (2026-09-30) · F-001 (2026-10-01) | **`PROPOSTA`** |

### 4.3 ODS no proposats

| ID | Motiu | Estat |
|---|---|---|
| ODS-01, 02, 03, 05, 06, 07, 09, 11, 13, 14, 15, 16, 17 | F-035 **no els menciona** (cerca de text complet: `ODS` = 1 coincidència, només el preàmbul). F-035 acreditaria el text però no l'exigibilitat, i no hi ha cap vincle curricular raonable amb els continguts bàsics de `3016`. **No es proposen.** | `PENDENT` |

### 4.4 Recompte

- **Relacions ODS proposades: 4** (ODS-04, ODS-08, ODS-10, ODS-12).
- **Totes amb estat `PROPOSTA`. Cap amb estat `VERIFICADA`.**
- **Relacions ODS `PENDENT`: 13** (la resta de l'Agenda), per manca de font curricular que les mencione.
- **Relacions ODS `VERIFICADA` al mòdul `3016`: 0.**

---

## 5. Relació amb els temes transversals

### 5.1 Advertencia prèvia, sense matisos

1. **El Decret 117/2025 no conté cap llista de «temas transversales»** (cerca de text
   complet = 0 coincidències). El contingut transversal es configura via l'**art.
   10.3** (cultura transversal), l'**art. 5.2** (RA transversals del projecte) i
   l'**art. 4.1** (àmbits).
2. **L'art. 10.3 s'adreça al centre i al cicle, no a un mòdul concret.** El currículum
   de `3016` (F-037, Annex VII apartat 3.3) **no remet a cap d'aquests continguts**.
3. Els deu temes TT-001 … TT-010 són `VERIFICADA` **com a exigència al centre i al
   cicle, mai al mòdul**. La remissió és **`V-3016-TT`, que és `PENDENT`**.
4. Per tant: **les deu relacions són `PROPOSTA`** i cap no pot pujar a `VERIFICADA`.

### 5.2 Taula de relacions amb temes transversals

| ID | Contingut transversal | Text literal de **F-035** (Decret 117/2025) · apartat i pàgina | Vinculació pedagògica **proposada** al mòdul `3016` | Criteris implicats | Estat |
|---|---|---|---|---|---|
| **TT-001** | Prevenció de riscos laborals | «Se potenciará o creará la cultura de prevención de riesgos laborales en los espacios donde se impartan los diferentes módulos profesionales […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-7`: instruccions de treball segurs i identificació de riscos abans de la manipulació. Ancorada al **RA 6 sencer** i als continguts bàsics del bloc 6, que són **literals de F-037**. | `6a`, `6b`, `6c`, `6d`, `6e`, `6h` | **`PROPOSTA`** |
| **TT-002** | Respecte ambiental | «[…] así como una cultura de respeto ambiental […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-8`: separació i retirada selectiva de residus de l'obra. S'ancora en el contingut bàsic literal «Cumplimiento de la normativa de protección ambiental.» (bloc 6, ítem 8). **Advertiment:** `protección ambiental` és contingut curricular, **no** capçalera d'ODS. | `6f`, `6g`, `6h` | **`PROPOSTA`** |
| **TT-003** | Treball de qualitat i normes de qualitat | «[…] trabajo de calidad realizado conforme a las normas de calidad […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-3`: control de la fixació mecànica i del mecanitzat; s'ancra en «Preparación y mecanizado de canalizaciones. Técnicas de montaje…» i «Técnicas de fijación». | `2d`, `2e`, `2g` | **`PROPOSTA`** |
| **TT-004** | Creativitat i innovació | «[…] creatividad, innovación […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-5` i `ACT-6`: l'alumne tria solucions de muntatge i configura la xarxa dins els marges dels continguts bàsics, amb criteri propi documentat. | `4c`, `5f`, `5g` | **`PROPOSTA`** |
| **TT-005** | Igualtat de gènere | «[…] igualdad de género […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-9`: rols de rol (rotació de funcions) i avaluació amb rúbrica comuna, sense tractar el gènere com a eix curricular del mòdul. | tots els RA | **`PROPOSTA`** |
| **TT-006** | Respecte a la diversitat | «[…] respeto a la diversidad […]» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-2` i `ACT-4`: alternatives de material i de mètode (par trenat, coaxial, fibra) i varietat d'estudis de cas, amb el criteri literal «entre otros» que hi ha als continguts bàsics. | `1c`, `3a` | **`PROPOSTA`** |
| **TT-007** | Promoció de la igualtat d'oportunitats | «[…] promoción de la igualdad de oportunidades […]» · **art. 10.3, pàg. 7/58** (2026-09-30) · i preàmbul, **pàg. 3/58**: «Se proporcionarán los apoyos necesarios para avanzar en la supresión de cualquier tipo de barrera de aprendizaje, de acceso a la información y a la comunicación, garantizando así la igualdad de oportunidades» | `ACT-1` i `ACT-6`: representació del mapa de xarxa en formats oberts i documentació accessible de la instal·lació, de manera que tothom puga llegir i reutilitzar la memòria tècnica. | `2c`, `5e`, `5f`, `5g` | **`PROPOSTA`** |
| **TT-008** | Disseny per a totes les persones i accessibilitat universal | «[…] el diseño para todas las personas y la accesibilidad universal» · **art. 10.3, pàg. 7/58** (2026-09-30) | `ACT-1`: traçat d'itineraris de cablejat que no interfereixen amb el pas de les persones i ubicació de preses i armaris a altura accessible. Es proposa com a criteri de revisió de la memòria tècnica, **no com a criteri d'avaluació**, perquè el RD no el recull. | `2c`, `2f`, `3f` | **`PROPOSTA`** |
| **TT-009** | Projecte intermodular d'aprenentatge col·laboratiu: RA treballats transversalment | «Además de la selección concreta realizada por el equipo docente según la especialidad del ciclo, se trabajarán transversalmente los RA que figuran en el currículo del proyecto» · **art. 5.2, pàg. 5/58** (2026-09-30) | `ACT-9` és el Vehicle natural per connectar amb el **projecte intermodular `3160972` del 2n curs**. **Reserva:** no s'ha verificat **quin** RA del projecte de l'art. 5 toquen `3016`; cal el currículum bàsic del projecte (F-032, Annex I del RD 498/2024) per poder-ho determinar. Vegeu §9, P-11. | tots els RA | **`PROPOSTA`** |
| **TT-010** | Estructura en tres àmbits: Comunicació i Ciències Socials, Ciències Aplicades i Professional | El cicle «constará de tres ámbitos y el proyecto» · **art. 4.1, pàg. 4/58**; organització de matèries a l'**Anexo III-B, pàg. 45/58** (taula d'Informática de oficina a la **pàg. 53/58**) · (2026-09-30) | `3016` pertany a l'**àmbit Professional**. **Reserva:** l'Anexo III-B només organitza l'àmbit de Comunicació i Ciències Socials (mòduls `3161`/`3162`), **no** el professional. No hi ha res a tractar per a `3016` més enllà d'ubicar-lo a l'àmbit. | (estructural, sense criteri) | **`PROPOSTA`** |

### 5.3 Recompte

- **Relacions amb temes transversals: 10** (TT-001 … TT-010).
- **Totes amb estat `PROPOSTA`. Cap amb estat `VERIFICADA`.**
- **Relacions TT `VERIFICADA` al mòdul `3016`: 0.**

---

## 6. Propostes didàctiques

**Estat de totes les activitats: `PROPOSTA`.** Cap activitat no ve exigida per cap
font; totes deriven de sabers que, al seu torn, deriven de text literal de F-037.
Cada activitat indica el criteri que avalua.

### ACT-1 · Memòria tècnica de l'edifici i croquis d'ubicacions

- **Què fa:** l'alumne rep un croquis d'un edifici i hi situa els elements
  d'instal·lació, justificant cada decisió.
- **Justificació curricular:** exercita la identificació d'elements i espais física
  d'una xarxa (`SB-3016-09`) i les característiques de les instal·lacions
  d'infraestructures de telecomunicació en edificis (`SB-3016-01`).
- **Criteris que avalua:** `1a`, `1b`, `1d`, `2c`, `5e`.
- **ODS / TT (tots `PROPOSTA`):** ODS-04 · TT-007, TT-008.

### ACT-2 · Banc d'elements i conductors

- **Què fa:** catàleg de mitjans de transmissió (`SB-3016-02`), classificació de
  conductors (`SB-3016-02`) i fitxa de cada tipus de fixació amb l'element que
  subjecta (`SB-3016-06`).
- **Justificació curricular:** arrela els continguts bàsics literals del bloc 1
  («Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre
  otros.») i del bloc 4 («Características y tipos de las fijaciones.») amb la
  selecció que el RA 1 demana («Selecciona los elementos…»).
- **Criteris que avalua:** `1b`, `1c`, `1e`, `1f`.
- **ODS / TT (tots `PROPOSTA`):** TT-006.

### ACT-3 · Muntatge del «rack» i mecanització de canalitzacions

- **Què fa:** taller pràctic amb fases: preparació i mecanització de canalitzacions,
  muntatge d'armari seguint el plànol, fixació mecànica i tancament amb la revisió de
  seguretat.
- **Justificació curricular:** és el nucli literal de l'orientació pedagògica
  «El montaje de las canalizaciones y soportes.» i del contingut bàsic
  «Preparación y mecanizado de canalizaciones. Técnicas de montaje de canalizaciones
  y tubos.»
- **Sense cobertura curricular declarada (correcció D-1):** l'activitat **no**
  avalua cap criteri sobre «la toma de medidas de las magnitudes típicas de las
  instalaciones» (`OP v8`), perquè **cap criteri del mòdul la conté** (§3.11,
  `P-24`). Que es prenguen mesures de longituds i recorreguts en aquest taller és
  una pràctica **`[PROPOSTA]` de material complementari**, no un contingut
  curricular del RD ni una exigència avualable.
- **Criteris que avalua:** `2a` … `2h`.
- **ODS / TT (tots `PROPOSTA`):** TT-001, TT-003.

### ACT-4 · Tesa, etiquetatge i preses de la xarxa

- **Què fa:** desplegament dels conductors amb les tècniques de tendido literals,
  tall i etiquetatge, muntatge dels armaris de comunicacions i connexió de preses
  d'usuari.
- **Justificació curricular:** cobreix literalment l'orientació «El tendido de cables
  para redes locales cableadas.» i els continguts bàsics «Técnicas de tendido de los
  conductores.» i «Identificación y etiquetado de conductores.»
- **Criteris que avalua:** `3a` … `3g`.
- **ODS / TT (tots `PROPOSTA`):** ODS-08 · TT-006.

### ACT-5 · Muntatge i fixació d'antenes, amplificadors i accessoris

- **Què fa:** assemblatge, col·locació, fixació (en armari i en superfície) i
  connexió d'un sistema de transmissió, amb revisió de seguretat.
- **Justificació curricular:** correspon a la orientació pedagògica «La aplicación
  de técnicas de montaje de sistemas y elementos de las instalaciones.» (`OP v7`,
  vinyeta 7 de les orientacions) i als continguts bàsics «Montaje de sistemas y
  elementos…», «Instalación y fijación de sistemas…», «Técnicas de fijación: en
  armarios, en superficie» i «Técnicas de conexionados de los conductores.»
- **`OP v7` (correcció D-1):** aquesta vinyeta ja s'hi citava en el text de
  l'activitat però **no era origen de cap saber**. Ara `OP v7` és **co-origin
  declarat de `SB-3016-26`**, que és el mateix contingut que `CB b4.i2`
  (§2.4 i §3.12): es declara **redundant**, no crea cap saber nou i no s'hi
  assigna cap criteri nou.
- **Criteris que avalua:** `4a` … `4f`, `4h`. **`4g` queda fora** (§3.8).
- **ODS / TT (tots `PROPOSTA`):** ODS-08 · TT-004.

### ACT-6 · Configuració bàsica i representació del mapa física

- **Què fa:** descripció de la xarxa local, identificació d'elements amb funció,
  interpretació i **representació del mapa física** amb una eina informàtica triada
  per l'alumne.
- **Justificació curricular:** correspon al bloc 5 de continguts bàsics («Características.
  Ventajas e inconvenientes. Tipos. Elementos de red.», «Identificación de elementos y
  espacios físicos…», «Dispositivos de interconexión de redes.», «Configuración básica
  de los dispositivos de interconexión de red cableada e inalámbrica.») i a la
  orientació «La integración de los elementos de la red.»
- **Què hi ha de nou (correcció D-1):** l'activitat **executa la configuració
  bàsica** que demana `CB b5.i6`, a través de `SB-3016-40`. Abans de la correcció
  el text d'aquest contingut oficial apareixia només en aquesta justificació i
  al bloc literal de l'Annex C, sense cap saber ni cap criteri que el sostingués.
- **Criteris que avalua:** `5a` … `5g`. Els criteris `5f` i `5g` es valoren amb
  reserva (§3.6).
- **Limitació que s'ha de llegir amb el criteri** (§3.10): la configuració de
  `SB-3016-40` es pot **ensenyar i valorar com a part de l'activitat**, amb
  instrument `[PROPOSTA]` (`P-17`), però **no hi ha cap criteri oficial de RA 5 que
  l'avalui**: la nota que se li doni no és la nota d'un criteri exigible del RD.
- **ODS / TT (tots `PROPOSTA`):** TT-004, TT-007.

### ACT-7 · Instruccions de treball segurs

- **Què fa:** elaboració i aplicació d'una instrucció de treball: riscos i
  perillositat de cada operació, causes d'accident, proteccions de màquina, equips de
  protecció individual i mesures de prevenció.
- **Justificació curricular:** és el contingut bàsic literal del **bloc 6**, que
  inclou «Identificación de riesgos.», «Determinación de las medidas de prevención de
  riesgos laborales.», «Sistemas de protección individual.» i «Prevención de riesgos
  laborales en los procesos de montaje.»
- **Criteris que avalua:** `6a` … `6e`.
- **ODS / TT (tots `PROPOSTA`):** TT-001 · ODS-12 (amb l'esclareixement de §4.2).

### ACT-8 · Ordre, neteja i retirada selectiva

- **Què fa:** ordre i neteja de la instal·lació acabada, valoració de l'ordre i la
  neteja com a factor de prevenció, i classificació dels residus de l'obra per a la
  retirada selectiva.
- **Justificació curricular:** correspon al contingut bàsic literal «Cumplimiento de
  la normativa de protección ambiental.» i al criteri `6h`, que fa de l'ordre i la
  neteja el **primer factor de prevenció**.
- **Criteris que avalua:** `6f`, `6g`, `6h`.
- **ODS / TT (tots `PROPOSTA`):** TT-002 · ODS-12.

### ACT-9 · Projecte integrador: instal·lació completa d'una xarxa local en un «pequeño entorno»

- **Què fa:** l'alumne projecta, munta, connecta, configura, documenta i posa en
  servei una instal·lació completa, amb rols rotatius i rúbrica compartida.
- **Justificació curricular:** integra els sis RA. La denominació ve literalment de
  les orientacions pedagògiques: «instalar canalizaciones, cableado y sistemas
  auxiliares en **instalaciones de redes locales en pequeños entornos**». Aquesta és
  l'activitat que connecta amb el projecte intermodular `3160972` (F-032).
- **Criteris que avalua:** tots els criteris **excepte `4g`** (§3.8).
- **A més del criteri, avuala l'única part del mòdul que no té criteri propi:**
  la configuració bàsica de `SB-3016-40` (`CB b5.i6`, §3.10), amb instrument
  `[PROPOSTA]`. I en la mateixa línia, si el centre ho vol com a pràctica de
  taller, la mesura de longituds i recorreguts de `OP v8`: **material
  complementari del projecte, no contingut curricular**, i **no resol `P-24`**
  (§3.11).
- **ODS / TT (tots `PROPOSTA`):** ODS-04, ODS-08, ODS-10 · TT-005, TT-007, TT-009.

---

## 7. Traçabilitat inversa: criteri → activitat

| Activitat | Criteris que avalua | Sabers que mobilitza |
|---|---|---|
| ACT-1 | `1a`, `1b`, `1d`, `2c`, `5e` | SB-01, SB-05, SB-09, SB-19 |
| ACT-2 | `1b`, `1c`, `1e`, `1f` | SB-02, SB-03, SB-04, SB-06, SB-12, SB-28 |
| ACT-3 | `2a`, `2b`, `2c`, `2d`, `2e`, `2f`, `2g`, `2h` | SB-04, SB-07, SB-09, SB-13, SB-17, SB-18, SB-19, SB-20, SB-21, SB-33, SB-39 |
| ACT-4 | `3a`, `3b`, `3c`, `3d`, `3e`, `3f`, `3g` | SB-02, SB-04, SB-10, SB-11, SB-12, SB-19, SB-22, SB-23, SB-24, SB-25, SB-29, SB-39 |
| ACT-5 | `4a`, `4b`, `4c`, `4d`, `4e`, `4f`, `4h` | SB-03, SB-06, SB-07, SB-11, SB-13, SB-17, SB-18, SB-20, SB-24, SB-26, SB-27, SB-28, SB-29, SB-30, SB-33, SB-39 |
| ACT-6 | `5a`, `5b`, `5c`, `5d`, `5e`, `5f`, `5g` · **i `SB-40` sense criteri** (§3.10) | SB-02, SB-03, SB-08, SB-09, SB-12, SB-30, SB-31, **SB-40** |
| ACT-7 | `6a`, `6b`, `6c`, `6d`, `6e` | SB-13, SB-14, SB-15, SB-16, SB-32, SB-33, SB-34, SB-36, SB-37, SB-39 |
| ACT-8 | `6f`, `6g`, `6h` | SB-32, SB-33, SB-34, SB-35, SB-39 |
| ACT-9 | tots menys `4g` · i `SB-40` sense criteri | tots els 40 sabers |

**Comprovació:** cap criteri queda sense activitat. `4g` queda explícitament fora i
sense cobertura (§3.8). `SB-40` queda fora de la columna de criteris perquè
**no n'hi ha cap que el cobreixi** (§3.10), i això s'ha fet constar a la taula
en lloc de distribuir-lo per un criteri que no li escau.

---

## 8. Hores

### 8.1 Context curricular autoritatiu

| Dada | Valor | Font i apartat | Data | Estat |
|---|---|---|---|---|
| Carga horaria setmanal del mòdul `3016`, 2n curs | **10 h/setmana** | **F-032**, Decret 117/2025, **Anexo III-A**, taula «Informática de oficina», **pàg. 34/58** (remissió a l'art. 3.8, pàg. 4/58) | 2026-10-01 | `VERIFICADA` |
| Carga horària anual del mòdul `3016`, 2n curs | **332 h/any** | idem | 2026-10-01 | `VERIFICADA` |

Fila literal del mòdul a la taula `Familia / Código / Módulo / hrs-sem / hrs-año`:
`3016` · `Instalación y mantenimiento de redes para transmisión de datos` · `10` · `332`.

### 8.2 Advertiment sobre el camp `Duración` del RD

F-037, Annex VII apartat 3.3, bloc `Código: 3016.` conté el camp literal:

```text
Duración: 115 horas.
```

> **`Duración: 115 horas.` NO és l'horari del curs `3016` i no s'ofereix com a tal.**
> És un camp del RD 356/2014 **que el document no defineix** (incidència **I-7**,
> `PENDENT`): 0 coincidències de `Duración total`, `carga horaria`, `distribución
> horaria` o qualsevol definició del concepte. A més, els 9 valors `Duración` de
> l'Annex VII sumen **1.100 h** davant de la `Duración: 2.000 horas.` que declara
> l'apartat 1 del títol. **Per a tot el calendari preval F-032:** 10 h/setmana ·
> 332 h/any. Les 115 h **no** s'han de convertir en sessions, ni dividir entre
> setmanes, ni oferir com a alternativa.

### 8.3 Distribució temporal proposada `[PROPOSTA]`

**Estat `PROPOSTA`:** cap font no distribueix les 332 h en unitats didàctiques. El
repartiment següent **quadra amb 10 h/setmana · 332 h/any (F-032)** i és una proposta
per a la revisió docent. En 30 setmanes lectives, 10 h/setmana × 33,2 setmanes ≈ 332 h.

| Bloc | Contingut | Setmanes | Hores | Què hi treballa |
|---|---|---|---|---|
| **Fase 1** | RA 1 · Bloc 1 de continguts bàsics | 1–5 | **~55 h** | ACT-1, ACT-2 · criteris `1a`–`1f` |
| **Fase 2** | RA 2 · Bloc 2 | 6–12 | **~77 h** | ACT-3 · criteris `2a`–`2h` |
| **Fase 3** | RA 3 · Bloc 3 | 13–18 | **~66 h** | ACT-4 · criteris `3a`–`3g` |
| **Fase 4** | RA 4 · Bloc 4 | 19–25 | **~77 h** | ACT-5 · criteris `4a`–`4f`, `4h` |
| **Fase 5** | RA 5 · Bloc 5 | 26–30 | **~39 h** | ACT-6 · criteris `5a`–`5g` |
| **Fase 6** | RA 6 · Bloc 6 (transversal, tot el curs) | 1–30 | **~18 h** | ACT-7, ACT-8 · criteris `6a`–`6h` |
| | **TOTAL** | **30 setmanes** | **332 h** | 44 criteris (43 amb cobertura) |

**Advertiments sobre aquesta distribució:**

1. **El RA 6 travessa tot el curs** i no es redueix a les darreres setmanes: el
   criteri `6h` parla de l'ordre i la neteja com a factor de prevenció en cada
   operació, i els criteris `2h` i `4h` apliquen normes de seguretat **des del primer
   dia**. `[PROPOSTA]`
2. **El projecte integrador `ACT-9` s'avalua dins de la fase 5 i es lliura a finals
   de curs.** Com que el RA 6 ja s'ha avaluat al llarg del curs, el lliurament final
   no requereix una fase 6 separada. `[PROPOSTA]`
3. **Aquesta taula no substitueix el calendari del centre.** La discrepància entre el
   DOGV (F-032) i les fitxes de consulta a CEICE (F-034 / F-036, que donen 8 h/sem ·
   266 h) **continua oberta** en el registre (incidències I-2 i I-3). Per al mòdul
   preval **F-032**; el calendari concret l'ha de fixar l'equip docent.

---

## 9. Registre de tot allò que queda `PENDENT`

| ID | Què queda pendent | Per què | On l'he tocat | Estat |
|---|---|---|---|---|
| **P-1** | **Vinculació acreditada d'un ODS al mòdul `3016`** (`V-3016-ODS`) | F-037, bloc `3016`: 0 coincidències de `ODS`, `objetivos de desarrollo sostenible`, `Agenda 2030`, `desarrollo sostenible`, `sostenible`, `sostenibilidad`. F-035: `ODS` apareix 1 sola vegada, al preàmbul, i **no assigna ODS a mòduls**. | §4 | `PENDENT` |
| **P-2** | **Vinculació acreditada d'un tema transversal al mòdul `3016`** (`V-3016-TT`) | F-037: `transversal` = 0 al bloc i a tot el RD. F-035, art. 10.3, s'adreça al centre i al cicle. Cap llista de «temas transversales» al decret. | §5 | `PENDENT` |
| **P-3** | **Criteri `4g` sense contingut bàsic** | «Se han colocado los embellecedores, tapas y elementos decorativos.» Cap dels 29 continguts bàsics parla d'això. **No he creat cap saber perquè seria inventar contingut.** | §3.8 | `PENDENT` |
| **P-4** | **Elements dels criteris que els continguts bàsics no anomenen** | Són literalment als criteris i **no als continguts bàsics**: tipus de caixa (`1d`); llistat de fixacions (`1e`); guies passacables (`3c`); accessoris d'armari (`3e`); panells de parcheo (`3f`); colors del cablejat (`4b`); «mapa físico» i la seua representació (`5e`, `5f`); aplicacions informàtiques (`5g`); nivell de peligrositat i mitjans de transport (`6a`); causes d'accident (`6c`); proteccions, alarmes i passos d'emergència (`6d`); fonts de contaminació (`6f`); tipologia de residus (`6g`); «primer factor de prevención» (`6h`); fases típiques del muntatge d'un «rack» (`2b`); croquis i plànol (`2c`, `2f`). | §3, marques «amb reserva» | `PENDENT` |
| **P-5** | **Criteri `3g` sense criteri d'avaluació propi** | «Se ha trabajado con la calidad y seguridad requeridas.» No té cap criteri que el desplegue; la qualitat i la seguretat només consten com a contingut bàsic («Recomendaciones en la instalación del cableado.») i com a norma de seguretat (bloc 6). | §3.4 | `PENDENT` |
| **P-6** | **Caràcter del camp `Duración: 115 horas.`** | Cap frase del RD 356/2014 el defineix (0 coincidències de qualsevol definició). Els 9 valors sumen 1.100 h davant de les 2.000 h de l'apartat 1. **No afecta la graella: preval F-032.** | §8.2 | `PENDENT` (incidència I-7 del registre) |
| **P-7** | **Distribució de les 332 h en setmanes i sessions** | Cap font curricular no la fixa. La taula de §8.3 és `PROPOSTA` i **no substitueix el calendari del centre**. La discrepància DOGV (F-032) / fitxes CEICE (F-034, F-036) continua oberta. | §8.3 | `PROPOSTA` |
| **P-8** | **Calendari de fase 1 i fase 2 i dependència del RA 6** | El RA 6 travessa el curs; com s'ordena en el calendari i com es coordina amb els altres mòduls del 2n curs (`3030`, `3159`, `3162`, `3164`, `TU02CF`, `3160972`) no està verificat en cap font consultada. | §8.3 | `PENDENT` |
| **P-9** | **Eines, equips i proves pràctiques disponibles al centre** | Cap font consultada acredita quins equips, eines o espais hi ha a l'aula. De `ACT-3` a `ACT-6` depèn del material disponible. | §6 | `PENDENT` |
| **P-10** | **Format del «mapa físico» de la xarxa local** (criteris `5f` i `5g`) | Cap contingut bàsic ni cap orientació pedagògica fixa el format ni l'eina. L'activitat `ACT-6` proposa que l'alumne la trie. | §6 | `PENDENT` |
| **P-11** | **Quins RA del projecte intermodular toquen `3016`** | L'art. 5.2 de F-035 diu que es treballen transversalment els RA del «currículo del proyecto», però no s'ha consultat el **currículum bàsic del projecte** (Anexo I del RD 498/2024, via F-032 art. 5.1). Sense això, TT-009 no es pot concretejar. | §5.2 | `PENDENT` |
| **P-12** | **Lletres de les competències esmentades a les orientacions pedagògiques** | Les orientacions pedagògiques de `3016` remeten a «las competencias profesionales, personales y sociales a), b), c), d), e), f), g), h) e i), del título». F-038, disposició addicional sisena, en fixa la denominació nova («competencias profesionales y para la empleabilidad»), **però no s'ha verificat lletra per lletra** quina competència correspon a quina lletra a la versió vigent. Aquest document **no hi assigna cap competència**. | §1.3 | `PENDENT` |
| **P-13** | **Reverificació directa de F-037 en aquesta execució** | El text literal transcrit prové de **F-027** («TEXTO ORIGINAL» de 2014). El registre acredita que el bloc `3016` del **F-037** és **idèntic caràcter per caràcter** (109 línies, `diff` sense diferències, SHA-256 del bloc idèntic) i que el mòdul **no** ha canviat amb el RD 498/2024. **Jo no he tornat a baixar F-037 en aquesta fase**: he treballat sobre la transcripció validada. Impacte: nul sobre el contingut, però la comprovació directa **no** és meua. | §1.1 | `PENDENT` (de reverificació) |
| **P-14** | **Actualització del registre de fonts per a F-001** | He reverificat F-001 el **2026-10-01** (HTTP 200, 59.139 bytes, SHA-256 `4f0bcff7df8a74d3…0a49`) per disposar del text literal de les denominacions dels objectius. El registre en té la data **2026-09-29**. **Cal que el `gestor-fonts` hi afegeixi aquesta evidència.** | §1.1, §4.2 | `PENDENT` (de registre) |
| **P-15** | **Codis `SB-3016-nn`, `ACT-n`, `CB b#.i#`, `OP v#`** | Són **del projecte**. La norma no assigna cap codi als RA ni als criteris, i els blocs de continguts bàsics **no estan numerats** a la norma. Cal declarar-los com a codificació pròpia a la graella final. | §1.5 | `PENDENT` (de declaració a la graella) |
| **P-16** | **Divergència d'hores DOGV / fitxes CEICE** | F-032 (norma) dona `3016` = 10 h/sem · 332 h/any; F-034 i F-036 (consulta, no normativa) donen 8 h/sem · 266 h. **Prevaleix F-032**, però el calendari concret l'ha de fixar el centre amb la conselleria. | §8.3 | `PENDENT` (incidències I-2 i I-3 del registre) |
| **P-23** | **Contingut oficial exigible sense criteri que l'avalui: `CB b5.i6`** | «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» L'única frase del mòdul que parla de configurar és el **RA 5** («Realiza operaciones **básicas de configuración**…»), però **cap dels 7 criteris de RA 5 ni cap altre dels 44** avalua l'operació: `5c` (el més proper) s'atura a `reconocido`. S'ha creat `SB-3016-40` i li s'ha donat itinerari de RA i d'activitat (`ACT-6`, `ACT-9`), **però sense criteri**, perquè estendre `5c` seria falsejar el text oficial. La valoració que el professorat hi faci és **instrument `PROPOSTA`** sobre una activitat, no avaluació d'un criteri exigible. | §3.10, §2.4, §6 | `PENDENT` |
| **P-24** | **Contingut oficial sense itinerari possible: `OP v8`** | «La toma de medidas de las magnitudes típicas de las instalaciones.» Cap dels 44 criteris parla de prendre mesures i cap dels 29 continguts bàsics nomena magnituds ni instruments de mesura. **Fals amic descartat:** `CB b6.i4` «Determinación de las **medidas** de prevención de riesgos laborales» parla de mesures de *prevenció*, no de mesures de *magnituds*, i no es pot reutilitzar per cobrir-ho. **No es crea cap saber ni cap criteri nou** perquè seria inventar contingut. Es pot treballar com a pràctica de taller dins d'`ACT-3` i `ACT-9` **com a material complementari `[PROPOSTA]`**, cosa que **no resol** aquest pendent. | §3.11, §6 | `PENDENT` |
| **P-25** | **`OP v7` declarada redundant, no pendent** | «La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.» El seu sentit literal ja el cobreix `SB-3016-26` (`CB b4.i2`), i és **equivalent però no idèntic** (`las instalaciones` / `las instalaciones de telecomunicación`). S'ha resolt **donant-li itinerari explícit** com a co-origin de `SB-3016-26` → `4a`, `4c` → `ACT-5`, `ACT-9`, **sense crear cap saber nou** i sense duplicar contingut. No queda res obert. | §3.12, §2.4 | `RESOLT` |

### 9.1 Nota operativa

`sortides/esborranys/extraccion-3016.md` ha estat **intermitentment il·legible** en aquesta
màquina (l'inunciat del fitxer es resolia, però l'obertura retornava `ENOENT`; el
m mateix ha passat amb altres fitxers del directori de treball). He recuperat el
contingut d'aquest mateix fitxer del directori de treball i n'he verificat la
integritat amb SHA-256 `327dfbf7baede3f9…0d` i 41.899 bytes, abans de treballar-hi.
**Si el fitxer es torna a modificar o a perdre, cal tornar a l'extracció de la fase 1
contra F-037**, no reconstruir els sabers de memòria. Aquest fet **no afecta cap dada
curricular**: el contingut utilitzat és el mateix.

---

## 10. Declaració de conformitat

| Punt | Comprovació |
|---|---|
| Cap contingut curricular inventat | **Sí.** Els 40 sabers deriven dels 29 continguts bàsics i de les 8 vinyetes de les orientacions pedagògiques de F-037. Cap saber nou sense origen literal. |
| Cap ODS inventat | **Sí.** Només es proposen els 4 ODS que F-035 menciona al preàmbul, tots amb estat `PROPOSTA`. Els altres 13 queden `PENDENT`. |
| Cap relació exigible sense font | **Sí.** Cap relació ODS ni TT té estat `VERIFICADA` al mòdul. La categoria `VERIFICADA` és **buida** en §4 i §5. |
| Traçabilitat de qualsevol saber fins a un text literal | **Sí.** Cada saber porta origen literal (`CB b#.i#` o `OP v#`) i la taula §3 el connecta amb el criteri i l'activitat. **Excepció declarada, no silenciosa:** `SB-3016-40`, que deriva de `CB b5.i6` i que cap criteri avalua (§3.10, `P-23`). |
| Els 44 criteris tractats | **Sí.** 24 `COBERTA` + 19 `COBERTA AMB RESERVA` + 1 `SENSE COBERTURA` (`4g`), declarat explícitament. |
| **Cap contingut oficial sense itinerari en silenci** | **Sí.** Els dos que no tenen itinerari possible estan nomenats, amb el motiu exacte i amb codi: `CB b5.i6` → `SB-3016-40`, amb itinerari de RA i d'activitat i limitació declarada (`P-23`); `OP v8` → `PENDENT` (`P-24`); `OP v7` → redundant i en consta (`P-25`). Cap no s'ha deixat en blanc (§3.10-§3.13). |
| Hores coherents amb el context curricular | **Sí.** 10 h/setmana · 332 h/any (F-032). `Duración: 115 horas.` **no** s'ofereix com a horari. |
| Diferenciació text extret / resum / interpretació / proposta | **Sí.** Cada element porta etiqueta. |
| Resolució de la fase | Document complet i enviat a revisió docent. **Cap relació no es pot dono per validada sense `READY FOR HUMAN REVIEW`.** |

---

*Fase 2 · `integrador-sabers` · branca `issue/3-graella-3016` · 2026-10-01 ·
**40 sabers** (18 saber · 14 saber fer · 8 saber estar) · 44 criteris tractats ·
4 relacions ODS i 10 relacions TT, totes `PROPOSTA` · 0 relacions `VERIFICADA` al mòdul ·
`P-23` i `P-24` oberts per declaració, `P-25` resolt (§12).*

---

## 11. Annex · Bloc literal del mòdul `3016` (F-037, Annex VII, apartat 3.3) — TEXT EXTRET

### 11.1 Per què hi és

Perquè **qualsevol saber d'aquest document es pugui traçar fins al text literal**
sense dependre d'un altre fitxer. Els sabers `SB-3016-01` … `SB-3016-40` deriven
dels 29 ítems de continguts bàsics i de les 8 vinyetes de les orientacions
pedagògiques que són **al final d'aquest annex**, tots marcats `[TEXT EXTRET]`.

### 11.2 Procedència i reserva

- **Font a citar: F-037** — RD 356/2014, versió consolidada vigent (actualització
  publicada el 28/05/2024), Annex VII, apartat 3.3, bloc `Código: 3016.`
- **Origen de la transcripció: F-027** — el mateix RD en versió «TEXTO ORIGINAL» de
  2014. El registre acredita que el bloc `3016` és **idèntic caràcter per caràcter**
  en les dues versions (109 línies, `diff` sense diferències, SHA-256 del bloc
  idèntic) i que **el mòdul `3016` no ha canviat** amb el RD 498/2024 (F-038).
- **Reserva (P-13):** la comparació de versions prové del registre de fonts, no
  d'una reverificació feta per mi en aquesta fase.
- **Caràcters conservats:** espai fi `U+2003` entre la numeració i el text, guion fi
  `U+2012` de les vinyetes i espai fi fi `U+2002` després de la vinyeta, tal com
  apareixen al document oficial.
- **Recompte que conté el bloc:** 6 resultats d'aprenentatge, **44 criteris
  d'avaluació**, capçalera `Contenidos básicos.` amb **6 blocs i 29 ítems**,
  `Orientaciones pedagógicas.` amb 4 paràgrafs i 8 vinyetes, i el camp
  `Duración: 115 horas.`
- **Cerces negatives en aquest bloc:** `ODS`, `objetivos de desarrollo sostenible`,
  `Agenda 2030`, `desarrollo sostenible`, `sostenible`, `sostenibilidad` i
  `transversal` donen **0 coincidències**. L'única expressió ambiental és
  `protección ambiental` (4 vegades), que és **contingut curricular** del RA 6 i del
  bloc 6, **no** capçalera d'ODS.

### 11.3 Bloc literal

```text
Módulo Profesional: Instalación y mantenimiento de redes para transmisión de datos.
Código: 3016.
Resultados de aprendizaje y criterios de evaluación.
1. Selecciona los elementos que configuran las redes para la transmisión de voz y datos, describiendo sus principales características y funcionalidad.
Criterios de evaluación:
a) Se han identificado los tipos de instalaciones relacionados con las redes de transmisión de voz y datos.
b) Se han identificado los elementos (canalizaciones, cableados, antenas, armarios, «racks» y cajas, entre otros) de una red de transmisión de datos.
c) Se han clasificado los tipos de conductores (par de cobre, cable coaxial, fibra óptica, entre otros).
d) Se ha determinado la tipología de las diferentes cajas (registros, armarios, «racks», cajas de superficie, de empotrar, entre otros).
e) Se han descrito los tipos de fijaciones (tacos, bridas, tornillos, tuercas, grapas, entre otros) de canalizaciones y sistemas.
f) Se han relacionado las fijaciones con el elemento a sujetar.
2. Monta canalizaciones, soportes y armarios en redes de transmisión de voz y datos, identificando los elementos en el plano de la instalación y aplicando técnicas de montaje.
Criterios de evaluación:
a) Se han seleccionado las técnicas y herramientas empleadas para la instalación de canalizaciones y su adaptación.
b) Se han tenido en cuenta las fases típicas para el montaje de un «rack».
c) Se han identificado en un croquis del edificio o parte del edificio los lugares de ubicación de los elementos de la instalación.
d) Se ha preparado la ubicación de cajas y canalizaciones.
e) Se han preparado y/o mecanizado las canalizaciones y cajas.
f) Se han montado los armarios («racks») interpretando el plano.
g) Se han montado canalizaciones, cajas y tubos, entre otros, asegurando su fijación mecánica.
h) Se han aplicado normas de seguridad en el uso de herramientas y sistemas.
3. Despliega el cableado de una red de voz y datos analizando su trazado.
Criterios de evaluación:
a) Se han diferenciado los medios de transmisión empleados para voz y datos.
b) Se han reconocido los detalles del cableado de la instalación y su despliegue (categoría del cableado, espacios por los que discurre, soporte para las canalizaciones, entre otros).
c) Se han utilizado los tipos de guías pasacables, indicando la forma óptima de sujetar cables y guía.
d) Se ha cortado y etiquetado el cable.
e) Se han montado los armarios de comunicaciones y sus accesorios.
f) Se han montado y conexionado las tomas de usuario y paneles de parcheo.
g) Se ha trabajado con la calidad y seguridad requeridas.
4. Instala elementos y sistemas de transmisión de voz y datos, reconociendo y aplicando las diferentes técnicas de montaje.
Criterios de evaluación:
a) Se han ensamblado los elementos que consten de varias piezas.
b) Se han identificado el cableado en función de su etiquetado o colores.
c) Se han colocado los sistemas o elementos (antenas, amplificadores, entre otros) en su lugar de ubicación.
d) Se han seleccionado herramientas.
e) Se han fijado los sistemas o elementos.
f) Se ha conectado el cableado con los sistemas y elementos, asegurando un buen contacto.
g) Se han colocado los embellecedores, tapas y elementos decorativos.
h) Se han aplicado normas de seguridad, en el uso de herramientas y sistemas.
5. Realiza operaciones básicas de configuración en redes locales cableadas relacionándolas con sus aplicaciones.
Criterios de evaluación:
a) Se han descrito los principios de funcionamiento de las redes locales.
b) Se han identificado los distintos tipos de redes y sus estructuras alternativas.
c) Se han reconocido los elementos de la red local identificándolos con su función.
d) Se han descrito los medios de transmisión.
e) Se ha interpretado el mapa físico de la red local.
f) Se ha representado el mapa físico de la red local.
g) Se han utilizado aplicaciones informáticas para representar el mapa físico de la red local.
6. Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y sistemas para prevenirlos.
Criterios de evaluación:
a) Se han identificado los riesgos y el nivel de peligrosidad que suponen la manipulación de los materiales, herramientas, útiles, máquinas y medios de transporte.
b) Se han operado las máquinas respetando las normas de seguridad.
c) Se han identificado las causas más frecuentes de accidentes en la manipulación de materiales, herramientas, máquinas de corte y conformado, entre otras.
d) Se han descrito los elementos de seguridad (protecciones, alarmas, pasos de emergencia, entre otros) de las máquinas y los sistemas de protección individual (calzado, protección ocular, indumentaria, entre otros) que se deben emplear en las operaciones de montaje y mantenimiento.
e) Se ha relacionado la manipulación de materiales, herramientas y máquinas con las medidas de seguridad y protección personal requeridos.
f) Se han identificado las posibles fuentes de contaminación del entorno ambiental.
g) Se han clasificado los residuos generados para su retirada selectiva.
h) Se ha valorado el orden y la limpieza de instalaciones y sistemas como primer factor de prevención de riesgos.
Duración: 115 horas.
Contenidos básicos.
Selección de elementos de redes de transmisión de voz y datos:
‒ Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre otros.
‒ Instalaciones de infraestructuras de telecomunicación en edificios. Características.
‒ Sistemas y elementos de interconexión.
Montaje de canalizaciones, soportes y armarios en redes de transmisión de voz y datos:
‒ Montaje de canalizaciones, soportes y armarios en las instalaciones de telecomunicación.
‒ Características y tipos de las canalizaciones: tubos rígidos y flexibles, canales, bandejas y soportes, entre otros.
‒ Preparación y mecanizado de canalizaciones. Técnicas de montaje de canalizaciones y tubos.
Despliegue del cableado:
‒ Recomendaciones en la instalación del cableado.
‒ Técnicas de tendido de los conductores.
‒ Identificación y etiquetado de conductores.
Instalación de elementos y sistemas de transmisión de voz y datos:
‒ Características y tipos de las fijaciones. Técnicas de montaje.
‒ Montaje de sistemas y elementos de las instalaciones de telecomunicación.
‒ Herramientas.
‒ Instalación y fijación de sistemas en instalaciones de telecomunicación.
‒ Técnicas de fijación: en armarios, en superficie.
‒ Técnicas de conexionados de los conductores.
Configuración básica de redes locales:
‒ Características. Ventajas e inconvenientes. Tipos. Elementos de red.
‒ Identificación de elementos y espacios físicos de una red local.
‒ Cuartos y armarios de comunicaciones.
‒ Conectores y tomas de red.
‒ Dispositivos de interconexión de redes.
‒ Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.
Cumplimiento de las normas de prevención de riesgos laborales y de protección ambiental:
‒ Normas de seguridad. Medios y sistemas de seguridad.
‒ Cumplimiento de las normas de prevención de riesgos laborales y protección ambiental.
‒ Identificación de riesgos.
‒ Determinación de las medidas de prevención de riesgos laborales.
‒ Prevención de riesgos laborales en los procesos de montaje.
‒ Sistemas de protección individual.
‒ Cumplimiento de la normativa de prevención de riesgos laborales.
‒ Cumplimiento de la normativa de protección ambiental.
Orientaciones pedagógicas.
Este módulo profesional contiene la formación asociada a la función de instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos.
La definición de esta función incluye aspectos como:
‒ La identificación de sistemas, elementos, herramientas y medios auxiliares.
‒ El montaje de las canalizaciones y soportes.
‒ El tendido de cables para redes locales cableadas.
‒ El montaje de los elementos de la red local.
‒ La integración de los elementos de la red.
La formación del módulo se relaciona con los siguientes objetivos generales del ciclo formativo a), d), e), f), g), h), e i) y las competencias profesionales, personales y sociales a), b), c), d), e), f), g), h) e i), del título. Además se relaciona con los objetivos t), u), v), w), x), y) y z), y las competencias q), r), s), t), u), v), w) y x), que se incluirán en este módulo profesional, de forma coordinada, con el resto de módulos profesionales.
Las líneas de actuación en el proceso enseñanza aprendizaje que permiten alcanzar las competencias del módulo versarán sobre:
‒ La identificación de los sistemas, medios auxiliares, sistemas y herramientas, para la realización del montaje y mantenimiento de las instalaciones.
‒ La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.
‒ La toma de medidas de las magnitudes típicas de las instalaciones.
```

---

## 12. Correcció posterior a la validació (2026-10-01) · registre de canvis

**Qui i per què.** Correcció del defecte **D-1** de
`sortides/informes-validacio/informe-validacio-3016.md` (§3.2, gravitat **alta**,
agent responsable `integrador-sabers`), detectat per la fase 4 el **2026-10-01**.
Aquest fitxer és l'únic que s'ha modificat: **ni `sortides/graelles/graella-3016.md`
ni l'informe de validació no han estat tocats**, perquè no són de la competència
d'aquesta fase. **Cap operació de git.**

### 12.1 Els tres elements de D-1, un per un

| Element oficial | Text literal de F-037 | Decisió curricular | On ha quedat | Estat |
|---|---|---|---|---|
| **`CB b5.i6`** | «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» | **Cap dels 7 criteris de RA 5 no el cobreix** amb el seu verb (`5c` s'atura a `reconocido`). **No s'estén cap criteri.** Es crea el `saber fer` **`SB-3016-40`** amb origen `CB b5.i6` i se li dona itinerari de **RA 5** (el RA sí que diu «Realiza operaciones **básicas de configuración**…») i d'**activitat** (`ACT-6`, `ACT-9`). | §2.4 · §3.6 (nota) · §3.10 · §6 (`ACT-6`, `ACT-9`) · §7 · §9 `P-23` | itinerari creat, amb limitació declarada |
| **`OP v8`** | «La toma de medidas de las magnitudes típicas de las instalaciones.» | **Cap criteri dels 44 parla de prendre mesures i cap dels 29 continguts bàsics nomena magnituds o instruments de mesura.** Descartat el fals amic `CB b6.i4` («medidas» de *prevenció*, no de *magnituds*). **No es crea cap saber ni cap criteri nou.** | §3.11 · §6 (nota a `ACT-3`/`ACT-9`) · §9 `P-24` | **`PENDENT`** |
| **`OP v7`** | «La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.» | El sentit literal **ja el cobreix `SB-3016-26`** (`CB b4.i2`), de manera **equivalent però no idèntica**. Es declara **redundant** i es fa **co-origin explícit** de `SB-3016-26` → `4a`, `4c` → `ACT-5`, `ACT-9`, **sense crear cap saber nou**. | §2.4 · §3.12 · §6 (`ACT-5`) · §9 `P-25` | resolt, en consta |

### 12.2 Corrections de coherència interna que l'informe de validació va deixar a la fase 2

| Defecte | Què era inconsistent | Què s'ha fet aquí |
|---|---|---|
| **D-2** (origen en aquesta fase 2) | La fila `6f` de §3.7 assignava `ACT-7`, però ni §6 ni §7 declaraven que `ACT-7` avalués `6f`; i §7 declarava que `ACT-7` avalua `6h` quan la fila `6h` només hi posa `ACT-8`. | Fila `6f` → **`ACT-8` només** (que és l'activitat de residus i contaminació, i que ja el declarava), i `6h` **retirat** de la llista de `ACT-7` a §7. Els dos criteris **conserven activitat**; cap criteri no s'ha perdut. La correcció corresponent a l'Annex B de la graella li toca al `generador-graelles`. |
| **D-6** | `SB-3016-38` portava `[TEXT EXTRET]` sobre una formulació del projecte amb un literal entre comilles angulars. | Corregit a **`[RESUM]`**, amb el literal delimitat entre comilles. Vegeu §2.5. |

### 12.3 Codi nou registrat

| Codi | Tipus | Origen literal | Estat |
|---|---|---|---|
| **`SB-3016-40`** | saber fer (14 de 14) | `CB b5.i6` · `[TEXT EXTRET]` | itinerari de RA 5 i d'activitat; **sense criteri**, amb `P-23` |

### 12.4 Comprovació de pèrdues

| Dada | Abans | Ara | Veredicte |
|---|---|---|---|
| Resultats d'aprenentatge | 6 | **6** | cap perdut |
| Criteris d'avaluació | 44 | **44** | cap perdut, cap nou, cap reanomenat, cap text oficial modificat |
| Criteris amb cobertura | 24 + 19 reserva + 1 sense (`4g`) | **24 + 19 reserva + 1 sense (`4g`)** | idèntic |
| Sabers | 39 | **40** | **+1** (`SB-3016-40`); cap suprimit |
| Sabers per tipus | 18 / 13 / 8 | **18 / 14 / 8** | — |
| Activitats | 9 | **9** | cap suprimida |
| Criteris amb activitat | 43 de 44 | **43 de 44** | idèntic (`4g` continua fora, declarat) |
| Ítems de continguts bàsics amb itinerari | 28 de 29 (o 27 amb criteri) | **28 de 29 amb saber · 27 de 29 amb criteri** | `CB b5.i6` deixa de ser una línia morta |
| Vinyetes de les orientacions amb itinerari | 6 de 8 | **7 de 8** | `OP v7` resolt; `OP v8` queda `PENDENT` i **nomenat** |
| Relacions ODS / TT | 4 + 10, totes `PROPOSTA` | **4 + 10, totes `PROPOSTA`** | cap canvi |

### 12.5 Què queda obert per al professorat

- **`P-23`** — el contingut `CB b5.i6` és exigible perquè el cobreix el RA 5, però
  **cap criteri oficial no permet valorar-lo**. És una limitació **del text de la
  norma**, no d'aquest document. S'hi dona un itinerari honest (activitat) i no
  cap cobertura falsa.
- **`P-24`** — l'orientació `OP v8` **no té itinerari possible** amb el material de
  F-037. Treballar-la al taller és legítim com a material complementari `[PROPOSTA]`,
  però no resol el pendent curricular.
- **`4g` (`P-3`)**, **`3g` (`P-5`)**, les 19 reserves (`P-4`) i tota la columna
  `PROPOSTA` d'hores, instruments i activitats (`P-7`, `P-9`, `P-17`, `P-18`,
  `P-21`) continuen exactament igual que abans: **aquesta correcció no els toca**.
