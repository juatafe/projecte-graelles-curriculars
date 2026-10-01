# Graella curricular · mòdul `3016`

**Mòdul:** `3016 «Instalación y mantenimiento de redes para transmisión de datos» ·
T.P.B. Informàtica d'oficina · grau bàsic · **2n curs** · Comunitat Valenciana.

---

## Estat del document

| Camp | Contingut |
|---|---|
| Fase | **Fase 3** (`generador-graelles`) · branca `issue/3-graella-3016` · **revisió posterior a la validació independent** |
| Data | **2026-10-01** |
| Estat de la graella | **EN REVISIÓ.** Posa els resultats, els sabers i les hores damunt de la taula, i **no** valida res. |
| Fonts curriculars | **F-037** (RA, criteris, continguts bàsics, orientacions) i **F-032** (hores). Vegeu `sortides/informes-validacio/informe-fonts-3016.md`. |
| Validació | **Hi ha informe de validació i encara no s'ha tornat a validar.** La fase 4 (`verificador`) va emetre el **2026-10-01** l'informe independent `sortides/informes-validacio/informe-validacio-3016.md`, que va trobar **cap defecte bloquejant** i va retornar 9 defectes no bloquejants (D-1 … D-9) i 4 reserves. Aquesta revisió **sincronitza la graella amb les correccions que els han tornat** i **no substitueix** el veredicte: **corregir no és revalidar**, i la porta de revisió docent la torna a posar el `verificador` en la revalidació, no aquesta fase. **Aquesta graella no es declara validada per la seva compte** i no està en disposició de passar a revisió docent fins que l'informe de validació es torni a llegir i a actualitzar amb la revalidació corresponent. |
| Què s'ha corregit en aquesta revisió | Vegeu **§7.2**: D-2 (`6f` → `ACT-8` només), D-3 (recompte d'instruments), D-4 (separador oficial `U+2003` als quadres), D-5 (`SB-3016-06`), D-6 (`SB-3016-38` a `[RESUM]`), D-7 (recompte de sabers), D-8 (setmanes indicatives sense solapaments), D-9 (còdis de pendent citats) i D-1 (sincronització amb la fase 2 corregida: `SB-3016-40`, `P-23`, `P-24`, `P-25`). |

---

## 0. Com llegir aquesta graella

### 0.1 Les cinc coses que hi ha dins i que no s'han de confondre

| Etiqueta | Què vol dir | On pesa |
|---|---|---|
| **`[TEXT EXTRET]`** | Paraules copiades del document oficial. **Són exigibles.** Als quadres de §2 i §3 s'hi conserven els caràcters especials oficials: espai fi `U+2003` entre la numeració i el text. | Resultats d'aprenentatge, criteris d'avaluació, continguts bàsics, orientacions pedagògiques i **34** dels 40 sabers (Annex A) |
| **`[TEXT EXTRET (parcial)]`** | **Subfrase literal** d'un ítem oficial **més llarg**. El text que hi ha escrit **sí que és literal**, caràcter per caràcter, però **no reprodueix l'ítem sencer**, i l'etiqueta ho declara perquè no es pugui llegir com un `[TEXT EXTRET]` complet. **Reserva:** cal poder llegir l'ítem oficial **sencer** per saber què queda fora de la cèl·la, i cal dir-ho. La part que hi ha escrita **no es reformula**. | **1** dels 40 sabers: `SB-3016-06` (Annex A.1, §3.7, §6.2) |
| `[RESUM]` | Síntesi del projecte sobre text literal. **No és exigible** com a formulació. | 5 dels 40 sabers i alguns resums de criteri |
| `[INTERPRETACIÓ]` | Lectura del projecte. **No té valor normatiu.** | Advertiments i lectures |
| `[PROPOSTA]` | Decisió pedagògica del projecte. **Cap norma l'obliga.** | Activitats, instruments d'avaluació, hores per criteri, distribució temporal, ODS i temes transversals |

### 0.2 Codificació: quina és oficial i quina és del projecte

| Codi | És oficial? | Origen |
|---|---|---|
| `1.`–`6.` (resultats d'aprenentatge) i `a)`–`h)` (criteris) | **Sí.** És la numeració literal de la norma. | F-037, Annex VII, apartat 3.3 |
| `3016` (codi de mòdul) | **Sí.** | F-037 i F-032 |
| `SB-3016-nn` (sabers) | **No. És del projecte** (pendent P-15). | Fase 2, desglossament dels **40** sabers |
| `ACT-n` (activitats) | **No. És del projecte.** | Fase 2, §6 |
| `CB b#.i#` (bloc i ítem de continguts bàsics) | **No. És del projecte.** Els 6 blocs de continguts bàsics **no estan numerats** a la norma. | Fase 1 i 2 |
| `OP v#` (vinyeta de les orientacions pedagògiques) | **No. És del projecte.** Les 8 vinyetes **no estan numerades**. | Fase 1 i 2 |
| `1a`, `1b`, … `6h` (codi compost criteri) | **No. És del projecte.** | Fase 2, §1.5 |

### 0.3 Les hores: quina font mana i quina no

> **Advertiment, a la vista i sense matisos.** Les hores curriculars d'aquest mòdul
> són **10 h/setmana · 332 h/any**, i res més. Venen de **F-032**, Decret
>117/2025, **Anexo III-A**, taula «Informática de oficina», **pàgina 34 de 58**,
>consultada el **2026-10-01**. Aquesta font **preval** sobre qualsevol altra xifra
>d'hores.
>
> El camp `Duración: 115 horas.` que apareix al mòdul `3016` dins del RD 356/2014
>**no és l'horari del curs**, **no es substitueix** per les 332 h, **no se li
>suma** i **no s'ofereix com a alternativa**. El RD 356/2014 **no defineix** què
>significa aquest camp (incidència **I-7** del registre; pendent **P-6**, `PENDENT`), i la suma dels nou valors
>`Duración` de l'Annex VII (1.100 h) **no quadra** amb la `Duración: 2.000 horas.`
>de l'apartat 1 del títol. Per a tot el calendari de la graella usa **només** les
>332 h de F-032.

### 0.4 Les orientacions pedagògiques i la denominació nova (F-038)

Les orientacions pedagògiques de `3016` diuen literalment
`las competencias profesionales, personales y sociales`. La **disposició
addicional sisena** del **F-038** (RD 498/2024) ordena que eixe es llija com a
**«competencias profesionales y para la empleabilidad»**. En aquesta graella les
orientacions es llegeixen així. Lletra per lletra, quina competència correspon a
quina lletra a la versió vigent, és **pendent** (P-12) i **aquesta graella no
assigna cap competència** a cap lletra.

### 0.5 Nota de fidelitat de caràcters

Al text oficial es conserven els caràcters especials del document original: espai
fi `U+2003` entre la numeració i el text, guion fi `U+2012` de les vinyetes i espai
fi fi `U+2002` després de la vinyeta.

**Les 2 aparicions del caràcter visible `U+2423` (OPEN BOX) que hi ha en tot
aquest document són intencionades i es declaren com a tal.** No són cap
marcador d'espai ni cap substitut: són el **nom del caràcter**, citat dins de dos
trams de codi a §7.2 i a §7.3, on s'explica quina correcció es va fer (D-4, que
va restituir els 50 espais `U+2003` dels quadres de §2 i §3 al caràcter oficial).
**Cal conservar-les**: sense elles aquelles frases no dirien quin caràcter era, i
la nota de fidelitat deixaria de ser comprovable. No toquen cap resultat
d'aprenentatge, cap criteri, cap contingut bàsic ni cap vinyeta: són
**metatext del projecte sobre la seua pròpia correcció**, no text oficial ni text
exigible. Detall i compte exacte a §7.3.

---

## 1. Identificació

| Camp | Contingut | Font, apartat i data | Estat |
|---|---|---|---|
| Mòdul | `Instalación y mantenimiento de redes para transmisión de datos` | **F-037**, RD 356/2014 (consolidat vigent), Annex VII, apartat 3.3, capçalera literal del bloc. Consulta 2026-10-01 | `VERIFICADA` |
| Codi | `3016` | **F-037**, mateix apartat, línia literal `Código: 3016.` | `VERIFICADA` |
| Cicle | **Informàtica d'oficina** (denominació del cicle a la norma valenciana) | **F-032**, Decret 117/2025, Anexo III-A, taula «Informática de oficina», pàg. 34/58. Consulta 2026-10-01 | `VERIFICADA` |
| Títol professional | Técnico Básico en Informática de Oficina — RD 356/2014, de 16 de maig (BOE-A-2014-5591) | **F-037** / **F-027** (Annex VII, capçalera de l'annex) | `VERIFICADA` |
| Nivell | Tècnic bàsic (**grado básico**) — T.P.B. | **F-037**, capçalera de l'Annex VII | `VERIFICADA` |
| Curs | **2n curs** | **F-032**, Anexo III-A, pàg. 34/58 (el mòdul `3016` hi figura al 2n curs) | `VERIFICADA` |
| Etapa | Formació Professional de grau bàsic | **F-032** / **F-035** (Decret 117/2025, del Consell) | `VERIFICADA` |
| Comunitat | Comunitat Valenciana | **F-032** / **F-035** (Decret 117/2025, DOGV núm. 10172, de 13.08.2025; CVE `DOGV-C-2025-32763`) | `VERIFICADA` |
| Àmbit | **Àmbit Professional** | **F-035**, Decret 117/2025, art. 4.1, pàg. 4/58 | `VERIFICADA` |
| **Hores curriculars** | **10 h/setmana · 332 h/any** | **F-032**, **Anexo III-A**, taula «Informática de oficina», **pàg. 34/58** (remissió a l'**art. 3.8**, pàg. 4/58). Consulta **2026-10-01** | `VERIFICADA` |
| Hores setmanals i anuals del 2n curs on se situa `3016` | 30 h/setmana · 1.000 h/any (el cicle complet) | **F-032**, mateixa taula, fila de totals | `VERIFICADA` |

### 1.1 Fila literal d'hores (F-032, pàg. 34/58)

Capçalera literal de la taula: `Familia / Código / Módulo / hrs-sem / hrs-año`

| `Código` | `Módulo` | `hrs-sem` | `hrs-año` |
|---|---|---|---|
| `3016` | `Instalación y mantenimiento de redes para transmisión de datos` | **10** | **332** |

### 1.2 La denominació de la família professional

| Camp | Contingut | Estat |
|---|---|---|
| Família professional | **Informática y Comunicaciones** | **`PENDENT` de literal** (P-22). Cap material de la fase 1 no transcriu el nom de la família. El mòdul queda ancorat a la taula «Informática de oficina» de **F-032** (pàg. 34/58) i al títol del **F-037**. Si cal el literal, cal tornar a F-032. |

### 1.3 El camp `Duración` del RD, i què se'n fa

```text
Duración: 115 horas.
```

| | F-037 · camp `Duración` | F-032 · Anexo III-A |
|---|---|---|
| Valor per a `3016` | `115 horas` | `10` hrs-sem · `332` hrs-año |
| Què estableix la norma | un capçalera literal dins del bloc del mòdul, **sense cap definició del concepte** (pendent **P-6**, incidència **I-7** del registre) | la fila literal `3016` de la taula de comesesa i càrrega horària |
| Preval per a aquesta graella | **no** | **sí** (regla de prevalència 1 del registre) |
| Serveix per fixar el calendari del 2n curs | **no** | **sí** |

---

## 2. Resultats d'aprenentatge — text literal

**Font única dels sis resultats i dels quaranta-quatre criteris: F-037** — RD
356/2014, versió consolidada vigent («Última actualización publicada el
28/05/2024»), Annex VII, apartat **3.3 «Desarrollo de los módulos»**, bloc delimitat
per `Código: 3016.`. Consulta **2026-10-01**. Estat `VERIFICADA`.

**F-027** (el «TEXTO ORIGINAL» de 2014) és **només l'origen de la transcripció**.
El registre acredita que el bloc `3016` és **idèntic caràcter per caràcter** en
les dues versions (109 línies, `diff` sense diferències) i que el mòdul **no** ha
canviat amb el RD 498/2024. Però el text oficial **que mana** és el de F-037.

| RA | Text literal `[TEXT EXTRET]` | Criteris |
|---|---|---|
| **RA 1** | `1.` `Selecciona los elementos que configuran las redes para la transmisión de voz y datos, describiendo sus principales características y funcionalidad.` | `a)`–`f)` → **6** |
| **RA 2** | `2.` `Monta canalizaciones, soportes y armarios en redes de transmisión de voz y datos, identificando los elementos en el plano de la instalación y aplicando técnicas de montaje.` | `a)`–`h)` → **8** |
| **RA 3** | `3.` `Despliega el cableado de una red de voz y datos analizando su trazado.` | `a)`–`g)` → **7** |
| **RA 4** | `4.` `Instala elementos y sistemas de transmisión de voz y datos, reconociendo y aplicando las diferentes técnicas de montaje.` | `a)`–`h)` → **8** |
| **RA 5** | `5.` `Realiza operaciones básicas de configuración en redes locales cableadas relacionándolas con sus aplicaciones.` | `a)`–`g)` → **7** |
| **RA 6** | `6.` `Cumple las normas de prevención de riesgos laborales y de protección ambiental, identificando los riesgos asociados, las medidas y sistemas para prevenirlos.` | `a)`–`h)` → **8** |
| | | **44 criteris** |

### 2.1 Orientacions pedagògiques que regeixen el mòdul — text literal

```text
Este módulo profesional contiene la formación asociada a la función de instalar
canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales
en pequeños entornos.
```

I les línies d'actuació en el procés ensinament-aprenentatge:

```text
‒ La identificación de los sistemas, medios auxiliares, sistemas y herramientas,
  para la realización del montaje y mantenimiento de las instalaciones.
‒ La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.
‒ La toma de medidas de las magnitudes típicas de las instalaciones.
```

L'expressió **«en pequeños entornos»** és la que dona nom al projecte integrador
`ACT-9` i a l'activitat `ACT-1`. Vegeu §0.4 per la lectura de la denominació de
competències.

**Estat de les tres vinyetes d'aquest bloc** (la codificació `OP v#` és del
projecte, P-15):

| Vinyeta | Text literal | itinerari a la graella | Estat |
|---|---|---|---|
| **`OP v6`** | «La identificación de los sistemas, medios auxiliares, sistemas y herramientas, para la realización del montaje y mantenimiento de las instalaciones.» | origina `SB-3016-18` → `1b`, `2a`, `4d` → `ACT-1`, `ACT-3`, `ACT-5`, `ACT-9` | itinerari complet |
| **`OP v7`** | «La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.» | **co-origin declarat de `SB-3016-26`** (equivalent però **no idèntic** a `CB b4.i2`) → `4a`, `4c` → `ACT-5`, `ACT-9` | **redundant**, resolt, en consta (P-25) |
| **`OP v8`** | «La toma de medidas de las magnitudes típicas de las instalaciones.» | **cap itinerari curricular possible** amb el material del mòdul; la pràctica de taller que la pot introduir és `[PROPOSTA]` i **no resol** el pendent | **`PENDENT`** (P-24) |

La justificació completa dels dos darrers casos és a **§3.9**, i el registre
complet de pendents és a **§7.1**.

---

## 3. La graella

### 3.0 Com llegir cada fila

| Columna | Contingut i etiqueta |
|---|---|
| **Criteri** | Codi compost del projecte (`1a` = RA 1, criteri `a)`) + **text literal** del criteri. La formulació del criteri és exigible; el codi compost no ho és. |
| **Saber / Saber fer / Saber estar** | Codi `SB-3016-nn` de la fase 2. `:—` vol dir que aquell tipus de saber no intervé en el criteri. |
| **Contingut bàsic literal** | L'ítem textual del mòdul d'on surt el criteri, amb la referència `CB b#.i#` o `OP v#`. Si el criteri conté elements que els continguts bàsics **no** anomenen, s'hi marca **«amb reserva»**. |
| **Activitat** | `ACT-n`. **Totes `[PROPOSTA]`.** Vegeu l'Annex B. |
| **Hores** | `[PROPOSTA]`. Repartiment del bloc de 332 h de F-032 entre criteris. **Cap font curricular no el fixa** (P-18). |
| **Instrument** | `[PROPOSTA]`. **Cap font curricular no fixa cap instrument** (P-17). |

### 3.1 RA 1 · *Selecciona los elementos que configuran las redes…* — 6 criteris · **55 h**

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`1a`**<br>a) Se han identificado los tipos de instalaciones relacionados con las redes de transmisión de voz y datos. | SB-3016-01 | :— | :— | `CB b1.i2` «Instalaciones de infraestructuras de telecomunicación en edificios. Características.» | ACT-1 | 9 | Rúbrica d'identificació sobre croquis |
| **`1b`**<br>b) Se han identificado los elementos (canalizaciones, cableados, antenas, armarios, «racks» y cajas, entre otros) de una red de transmisión de datos. | SB-3016-01, SB-3016-03, SB-3016-04, SB-3016-12 | :— | :— | `CB b1.i2`, `CB b1.i3` «Sistemas y elementos de interconexión.», `CB b2.i2`, `CB b5.i5` «Dispositivos de interconexión de redes.» | ACT-1, ACT-2 | 10 | Banc d'elements + rúbrica |
| **`1c`**<br>c) Se han clasificado los tipos de conductores (par de cobre, cable coaxial, fibra óptica, entre otros). | SB-3016-02 | :— | :— | `CB b1.i1` «Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre otros.» | ACT-2 | 9 | Fitxa de materials i prova escrita |
| **`1d`**<br>d) Se ha determinado la tipología de las diferentes cajas (registros, armarios, «racks», cajas de superficie, de empotrar, entre otros). | SB-3016-05 `[RESUM]` | SB-3016-19 | :— | `CB b1.i2` + `CB b1.i3` — **amb reserva**: la llista literal de tipus de caixa només consta al criteri, no als continguts bàsics (P-4) | ACT-1 | 9 | Rúbrica de classificació |
| **`1e`**<br>e) Se han descrito los tipos de fijaciones (tacos, bridas, tornillos, tuercas, grapas, entre otros) de canalizaciones y sistemas. | SB-3016-06 | :— | :— | `CB b4.i1` «Características y tipos de las fijaciones. Técnicas de montaje.» — **amb reserva**: el llistat literal de fixacions només consta al criteri (P-4) | ACT-2 | 9 | Fitxa de materials i prova escrita |
| **`1f`**<br>f) Se han relacionado las fijaciones con el elemento a sujetar. | SB-3016-06 | SB-3016-28 | :— | `CB b4.i1` + `CB b4.i5` «Técnicas de fijación: en armarios, en superficie.» | ACT-2, ACT-5 | 9 | Rúbrica de cas pràctic |
| | | | | | **Total RA 1** | **55** | |

### 3.2 RA 2 · *Monta canalizaciones, soportes y armarios…* — 8 criteris · **77 h**

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`2a`**<br>a) Se han seleccionado las técnicas y herramientas empleadas para la instalación de canalizaciones y su adaptación. | SB-3016-07, SB-3016-17, SB-3016-18 | SB-3016-19 | SB-3016-33 | `CB b4.i3` «Herramientas.» + `OP v1` / `OP v6` «La identificación de los sistemas, medios auxiliares, sistemas y herramientas…» | ACT-3 | 9 | Rúbrica de preparació de l taller |
| **`2b`**<br>b) Se han tenido en cuenta las fases típicas para el montaje de un «rack». | :— | SB-3016-19, SB-3016-21 | :— | `CB b2.i1` «Montaje de canalizaciones, soportes y armarios en las instalaciones de telecomunicación.» + `OP v2` «El montaje de las canalizaciones y soportes.» — **amb reserva**: la successió de fases no consta als continguts bàsics (P-4) | ACT-3 | 10 | Rúbrica de procés (fases) |
| **`2c`**<br>c) Se han identificado en un croquis del edificio o parte del edificio los lugares de ubicación de los elementos de la instalación. | SB-3016-09 | SB-3016-19 | :— | `CB b5.i2` «Identificación de elementos y espacios físicos de una red local.» + `CB b1.i2` — **amb reserva**: el croquis no consta als continguts bàsics (P-4) | ACT-1, ACT-3 | 10 | Rúbrica sobre croquis |
| **`2d`**<br>d) Se ha preparado la ubicación de cajas y canalizaciones. | SB-3016-04 | SB-3016-19, SB-3016-20 | SB-3016-33 | `CB b2.i1`, `CB b2.i2` «Características y tipos de las canalizaciones: tubos rígidos y flexibles, canales, bandejas y soportes, entre otros.» | ACT-3 | 10 | Prova pràctica amb rúbrica |
| **`2e`**<br>e) Se han preparado y/o mecanizado las canalizaciones y cajas. | SB-3016-04 | SB-3016-20 | SB-3016-33 | `CB b2.i3` «Preparación y mecanizado de canalizaciones. Técnicas de montaje de canalizaciones y tubos.» | ACT-3 | 12 | Prova pràctica amb rúbrica |
| **`2f`**<br>f) Se han montado los armarios («racks») interpretando el plano. | SB-3016-04 | SB-3016-19, SB-3016-21 | :— | `CB b2.i1` + `OP v2` — **amb reserva**: el plànol no consta als continguts bàsics (P-4) | ACT-3 | 9 | Prova pràctica amb rúbrica |
| **`2g`**<br>g) Se han montado canalizaciones, cajas y tubos, entre otros, asegurando su fijación mecánica. | SB-3016-04 | SB-3016-20 | SB-3016-33 | `CB b2.i2`, `CB b2.i3` | ACT-3 | 8 | Inspecció de fixació (llista de verificació) |
| **`2h`**<br>h) Se han aplicado normas de seguridad en el uso de herramientas y sistemas. | SB-3016-13 | SB-3016-20 | SB-3016-33, SB-3016-39 | `CB b6.i1` «Normas de seguridad. Medios y sistemas de seguridad.» + `CB b6.i5` «Prevención de riesgos laborales en los procesos de montaje.» | ACT-3, ACT-7 | 9 | Diari de taller + revisió de seguretat |
| | | | | | **Total RA 2** | **77** | |

### 3.3 RA 3 · *Despliega el cableado de una red de voz y datos…* — 7 criteris · **66 h**

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`3a`**<br>a) Se han diferenciado los medios de transmisión empleados para voz y datos. | SB-3016-02 | :— | :— | `CB b1.i1` «Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre otros.» | ACT-4 | 7 | Prova escrita breu |
| **`3b`**<br>b) Se han reconocido los detalles del cableado de la instalación y su despliegue (categoría del cableado, espacios por los que discurre, soporte para las canalizaciones, entre otros). | SB-3016-12 | SB-3016-22, SB-3016-23, SB-3016-25 | SB-3016-39 | `CB b3.i1` «Recomendaciones en la instalación del cableado.» + `CB b3.i2` «Técnicas de tendido de los conductores.» + `OP v3` «El tendido de cables para redes locales cableadas.» | ACT-4 | 11 | Memòria tècnica de traçat |
| **`3c`**<br>c) Se han utilizado los tipos de guías pasacables, indicando la forma óptima de sujetar cables y guía. | SB-3016-04 | SB-3016-23, SB-3016-25 | :— | `CB b3.i2` + `CB b2.i2` — **amb reserva**: les guies passacables no consten als continguts bàsics (P-4) | ACT-4 | 9 | Rúbrica de subjecció del cable |
| **`3d`**<br>d) Se ha cortado y etiquetado el cable. | SB-3016-24 | SB-3016-24 | SB-3016-39 | `CB b3.i3` «Identificación y etiquetado de conductores.» | ACT-4 | 8 | Inspecció d'etiquetes |
| **`3e`**<br>e) Se han montado los armarios de comunicaciones y sus accesorios. | SB-3016-10 | SB-3016-19 | :— | `CB b5.i3` «Cuartos y armarios de comunicaciones.» — **amb reserva**: els accessoris no consten als continguts bàsics (P-4) | ACT-4 | 9 | Rúbrica de muntatge |
| **`3f`**<br>f) Se han montado y conexionado las tomas de usuario y paneles de parcheo. | SB-3016-11 | SB-3016-29 | SB-3016-39 | `CB b5.i4` «Conectores y tomas de red.» + `CB b4.i6` «Técnicas de conexionados de los conductores.» — **amb reserva**: els panells de parcheo no consten als continguts bàsics (P-4) | ACT-4 | 13 | Prova pràctica de connexió |
| **`3g`**<br>g) Se ha trabajado con la calidad y seguridad requeridas. | :— | :— | SB-3016-39 `[RESUM]` | `CB b3.i1` + `CB b6.i5` — **amb reserva**: criteri **sense criteri d'avaluació propi**; la qualitat i la seguretat només consten al contingut bàsic (P-5) | ACT-4 | 9 | Diari de qualitat i ordre |
| | | | | | **Total RA 3** | **66** | |

### 3.4 RA 4 · *Instala elementos y sistemas de transmisión de voz y datos…* — 8 criteris · **77 h**

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`4a`**<br>a) Se han ensamblado los elementos que consten de varias piezas. | :— | SB-3016-26, SB-3016-30 | :— | `CB b4.i2` «Montaje de sistemas y elementos de las instalaciones de telecomunicación.» + `OP v4` «El montaje de los elementos de la red local.» | ACT-5 | 9 | Rúbrica d'assemblatge |
| **`4b`**<br>b) Se han identificado el cableado en función de su etiquetado o colores. | SB-3016-24 | SB-3016-24 | :— | `CB b3.i3` «Identificación y etiquetado de conductores.» — **amb reserva**: els colors no consten als continguts bàsics (P-4) | ACT-5 | 9 | Inspecció d'identificació |
| **`4c`**<br>c) Se han colocado los sistemas o elementos (antenas, amplificadores, entre otros) en su lugar de ubicación. | SB-3016-03 | SB-3016-26, SB-3016-27 | :— | `CB b4.i2` + `CB b4.i4` «Instalación y fijación de sistemas en instalaciones de telecomunicación.» | ACT-5 | 11 | Rúbrica de col·locació |
| **`4d`**<br>d) Se han seleccionado herramientas. | SB-3016-07, SB-3016-17, SB-3016-18 | :— | SB-3016-33 | `CB b4.i3` «Herramientas.» + `OP v1` / `OP v6` | ACT-5, ACT-7 | 9 | Rúbrica de preparació de l taller |
| **`4e`**<br>e) Se han fijado los sistemas o elementos. | SB-3016-06 | SB-3016-27, SB-3016-28 | SB-3016-33 | `CB b4.i1` + `CB b4.i4` + `CB b4.i5` | ACT-5 | 13 | Prova pràctica amb rúbrica |
| **`4f`**<br>f) Se ha conectado el cableado con los sistemas y elementos, asegurando un buen contacto. | SB-3016-11 | SB-3016-29 | SB-3016-39 | `CB b4.i6` + `CB b5.i4` | ACT-5 | 13 | Prova pràctica de connexió |
| **`4g`**<br>g) Se han colocado los embellecedores, tapas y elementos decorativos. | :— | :— | :— | **CAP.** Cap dels 29 continguts bàsics parla d'embelleidors, tapes ni elements decoratius. **`PENDENT`** — vegeu §3.8 | **cap** | **0 assignades** | **`PENDENT`** |
| **`4h`**<br>h) Se han aplicado normas de seguridad, en el uso de herramientas y sistemas. | SB-3016-13 | SB-3016-20 | SB-3016-33, SB-3016-39 | `CB b6.i1` + `CB b6.i5` | ACT-5, ACT-7 | 13 | Diari de taller + revisió de seguretat |
| | | | | | **Total RA 4** | **77** | |

### 3.5 RA 5 · *Realiza operaciones básicas de configuración en redes locales cableadas…* — 7 criteris · **39 h**

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`5a`**<br>a) Se han descrito los principios de funcionamiento de las redes locales. | SB-3016-08 | :— | :— | `CB b5.i1` «Características. Ventajas e inconvenientes. Tipos. Elementos de red.» | ACT-6 | 6 | Prova escrita breu |
| **`5b`**<br>b) Se han identificado los distintos tipos de redes y sus estructuras alternativas. | SB-3016-03, SB-3016-08 | SB-3016-31 | :— | `CB b5.i1` + `CB b1.i3` + `OP v5` «La integración de los elementos de la red.» | ACT-6 | 5 | Rúbrica d'anàlisi |
| **`5c`**<br>c) Se han reconocido los elementos de la red local identificándolos con su función. | SB-3016-03, SB-3016-08, SB-3016-09, SB-3016-12 | SB-3016-30, SB-3016-31 | :— | `CB b5.i1`–`CB b5.i5` + `CB b1.i3` + `OP v4` / `OP v5` | ACT-6 | 6 | Rúbrica d'identificació i funció |
| **`5d`**<br>d) Se han descrito los medios de transmisión. | SB-3016-02 | :— | :— | `CB b1.i1` | ACT-6 | 4 | Prova escrita breu |
| **`5e`**<br>e) Se ha interpretado el mapa físico de la red local. | SB-3016-09 | :— | :— | `CB b5.i2` «Identificación de elementos y espacios físicos de una red local.» — **amb reserva**: el «mapa físico» no consta literalment als continguts bàsics (P-4) | ACT-1, ACT-6 | 6 | Rúbrica d'interpretació |
| **`5f`**<br>f) Se ha representado el mapa físico de la red local. | :— | SB-3016-31 | :— | `CB b5.i2` + `OP v5` — **amb reserva**: la representació del mapa no consta als continguts bàsics (P-4) | ACT-6 | 6 | Lliurable del mapa |
| **`5g`**<br>g) Se han utilizado aplicaciones informáticas para representar el mapa físico de la red local. | :— | SB-3016-31 | :— | **cap capçalera d'eines informàtiques als continguts bàsics** — **amb reserva**: cap contingut del mòdul fixa l'eina (P-4, P-10) | ACT-6 | 6 | Lliurable del mapa + revisió de l'eina |
| | | | | | **Total RA 5** | **39** | |

> **Ho llegiu tot seguit: el contingut oficial `CB b5.i6` NO té cap criteri que
> l'avalui.** L'ítem 6 del bloc 5 — «Configuración básica de los dispositivos de
> interconexión de red cableada e inalámbrica.» — és l'ítem central del RA 5 i
> **cap dels set criteris de RA 5 (`5a`–`5g`) el cobreix** amb el seu verb: el més
> proper, `5c`, s'atura a `reconocido` i el seu contingut és `CB b5.i5`
> (`SB-3016-12`). Cap altre criteri dels 44 tampoc no serveix. **Aquesta graella
> no estén cap criteri i no en crea cap de nou**: el criteri oficial no hi ha,
> perquè la norma no el redacta. El que fa la fase 2 és recuperar l'ítem oficial
> en el **`saber
> fer` `SB-3016-40`** (Annex A.2) i donar-li **itinerari de resultat
> d'aprenentatge i d'activitat** (`ACT-6`, `ACT-9`), de manera que el
> professorat **sí que té lloc on introduir, ensenyar i valorar** el contingut.
> **Limitació declarada (`P-23`):** el contingut és exigible perquè el cobreix el
> RA 5, però **cap criteri oficial permet valorar-lo**; la nota que se li done serà
> instrument `[PROPOSTA]` sobre una activitat, **no** avaluació d'un criteri
> exigible. Detall a §3.9.1.

### 3.6 RA 6 · *Cumple las normas de prevención de riesgos laborales y de protección ambiental…* — 8 criteris · **18 h** · transversal

| Criteri | Saber | Saber fer | Saber estar | Contingut bàsic literal (F-037) | Activitat | Hores | Instrument `[PROPOSTA]` |
|---|---|---|---|---|---|---|---|
| **`6a`**<br>a) Se han identificado los riesgos y el nivel de peligrosidad que suponen la manipulación de los materiales, herramientas, útiles, máquinas y medios de transporte. | SB-3016-14 | SB-3016-36 `[RESUM]` | SB-3016-36 `[RESUM]` | `CB b6.i3` «Identificación de riesgos.» — **amb reserva**: el «nivel de peligrosidad» i els mitjans de transport no consten als continguts bàsics (P-4) | ACT-7 | 3 | Instrucció de treball segur (ITTS) |
| **`6b`**<br>b) Se han operado las máquinas respetando las normas de seguridad. | SB-3016-13 | :— | SB-3016-32, SB-3016-34 | `CB b6.i1`, `CB b6.i2` «Cumplimiento de las normas de prevención de riesgos laborales y protección ambiental.», `CB b6.i7` | ACT-7 | 2 | Revisió de seguretat en taller |
| **`6c`**<br>c) Se han identificado las causas más frecuentes de accidentes en la manipulación de materiales, herramientas, máquinas de corte y conformado, entre otras. | SB-3016-14 | SB-3016-36 | SB-3016-36 | `CB b6.i3` — **amb reserva**: la llista de causes no consta als continguts bàsics (P-4) | ACT-7 | 2 | ITTS + anàlisi de casos |
| **`6d`**<br>d) Se han descrito los elementos de seguridad (protecciones, alarmas, pasos de emergencia, entre otros) de las máquinas y los sistemas de protección individual (calzado, protección ocular, indumentaria, entre otros) que se deben emplear en las operaciones de montaje y mantenimiento. | SB-3016-16 | SB-3016-37 `[RESUM]` | SB-3016-37 | `CB b6.i6` «Sistemas de protección individual.» — **amb reserva**: els elements de seguretat de les màquines no consten als continguts bàsics (P-4) | ACT-7 | 3 | Rúbrica d'EPI |
| **`6e`**<br>e) Se ha relacionado la manipulación de materiales, herramientas y máquinas con las medidas de seguridad y protección personal requeridos. | SB-3016-15, SB-3016-16 | SB-3016-37 | SB-3016-37 | `CB b6.i4` «Determinación de las medidas de prevención de riesgos laborales.» + `CB b6.i6` | ACT-7 | 2 | Rúbrica de correspondència |
| **`6f`**<br>f) Se han identificado las posibles fuentes de contaminación del entorno ambiental. | SB-3016-35 | :— | SB-3016-35 | `CB b6.i8` «Cumplimiento de la normativa de protección ambiental.» — **amb reserva**: el llistat de fonts de contaminació no consta als continguts bàsics (P-4) | **ACT-8** | 2 | Llistat de fonts de contaminació |
| **`6g`**<br>g) Se han clasificado los residuos generados para su retirada selectiva. | SB-3016-35 | :— | SB-3016-35 | `CB b6.i8` — **amb reserva**: la tipologia de residus no consta als continguts bàsics (P-4) | ACT-8 | 2 | Fitxa de classificació de residus |
| **`6h`**<br>h) Se ha valorado el orden y la limpieza de instalaciones y sistemas como primer factor de prevención de riesgos. | :— | :— | SB-3016-32, SB-3016-33, SB-3016-34, SB-3016-35, SB-3016-39 | `CB b6.i2`, `CB b6.i5`, `CB b6.i7`, `CB b6.i8` + `CB b3.i1` — **amb reserva**: «primer factor de prevención» no consta als continguts bàsics (P-4) | ACT-8 | 2 | Diari de taller (ordre i neteja) |
| | | | | | **Total RA 6** | **18** | |

### 3.7 Recompte de la graella

| Dada | Recompte | Comprovació |
|---|---|---|
| Resultats d'apreneatge | **6** | Tots els RA de F-037 hi són, en text literal |
| Criteris d'avaluació a la taula | **44** | 6 + 8 + 7 + 8 + 7 + 8. Cap omès, cap fusionat, cap inventat |
| Criteris amb contingut bàsic literal que els sosté | **24** | `1a`, `1b`, `1c`, `1f`, `2a`, `2d`, `2e`, `2g`, `2h`, `3a`, `3b`, `3d`, `4a`, `4c`, `4d`, `4e`, `4f`, `4h`, `5a`, `5b`, `5c`, `5d`, `6b`, `6e` |
| Criteris coberts **amb reserva** | **19** | `1d`, `1e`, `2b`, `2c`, `2f`, `3c`, `3e`, `3f`, `3g`, `4b`, `5e`, `5f`, `5g`, `6a`, `6c`, `6d`, `6f`, `6g`, `6h` |
| Criteris **sense cobertura** | **1** | **`4g`** — `PENDENT` (§3.8) |
| Sabers mobilitzats a la taula de §3 | **38** | Els 38 que sostenen almenys un criteri. Són `SB-3016-01` … `SB-3016-37` i `SB-3016-39` |
| Sabers del catàleg que **no** sostenen cap criteri | **2** | `SB-3016-38`, transversal a tots els RA (entra per `ACT-9`), i `SB-3016-40`, que cobreix `CB b5.i6` i **no** té cap criteri que l'avalui (§3.9.1, `P-23`) |
| **Sabers en total** | **40** | **18 `saber` + 14 `saber fer` + 8 `saber estar`** = 38 a la taula + els 2 anteriors. Annex A. **Cap saber sense origen literal** |
| Etiquetes dels 40 sabers | **34 `[TEXT EXTRET]` + 1 `[TEXT EXTRET (parcial)]` + 5 `[RESUM]`** | Els `[RESUM]` són `SB-3016-05`, `SB-3016-36`, `SB-3016-37`, `SB-3016-38` i `SB-3016-39`, tots amb la reserva corresponent (§6.2). `SB-3016-06` és l'**únic `[TEXT EXTRET (parcial)]`**: en la cel·la no hi ha cap formulació del projecte, sinó una **subfrase literal parcial** — «Características y tipos de las fijaciones.», la primera frase de l'ítem oficial «Características y tipos de las fijaciones. Técnicas de montaje.» —, i l'etiqueta ho diu perquè el fet no es pugui confondre amb un `[TEXT EXTRET]` sencer. **Reserves:** §0.1 (definició de l'etiqueta nova), §6.2 i Annex A.1 |
| Ítems de continguts bàsics amb **algun saber** que en deriva | **28 de 29** | `CB b5.i6` ja en té (`SB-3016-40`, §3.9.1) |
| Ítems de continguts bàsics amb **algun criteri** que els avalui | **27 de 29** | Sense criteri: `CB b5.i6` (cap dels 44 criteris avalua una operació de configuració, §3.9.1) i `CB b4.i1` (parcial: només en és text `SB-3016-06`, §6.2) |
| Vinyetes de les orientacions pedagògiques amb **algun saber** que en deriva | **7 de 8** | `OP v7` redundant i resolt (P-25); `OP v8` **`PENDENT`** (P-24, §3.9.2) |
| Activitats | **9** | `ACT-1`…`ACT-9`, totes `[PROPOSTA]`. Annex B |
| Instruments d'avaluació | **43 assignacions · 34 formulacions · 10 famílies** | 44 files, una de les quals (`4g`) és `PENDENT`. Tots `[PROPOSTA]` (P-17). Repartiment a §6.4 |
| Hores repartides | **332** | 55 + 77 + 66 + 77 + 39 + 18. Coherent amb F-032 |
| Criteris amb hores sense assignar | **1** | `4g` (0 h), perquè no hi ha contingut bàsic |
| Pendents registrats | **25** codis (`P-1` … `P-25`) | §7.1. Cap no amaga cap dada curricular falsa |

### 3.8 Criteri `4g` — `PENDENT`, sense emmascarar

El criteri diu literalment:

```text
g) Se han colocado los embellecedores, tapas y elementos decorativos.
```

**Cap dels 29 continguts bàsics de `3016` parla d'embelleidors, tapes ni elements
decoratius.** El bloc 4 de continguts bàsics del mòdul tracta de
«Características y tipos de las fijaciones», «Montaje de sistemas y elementos de las
instalaciones de telecomunicación», «Herramientas», «Instalación y fijación de
sistemas», «Técnicas de fijación: en armarios, en superficie» i «Técnicas de
conexionados de los conductores». Cap parla de l'acabat estètic de la instal·lació.
A la veïna, l'única expressió propera és `protección ambiental`, que és **contingut
de prevenció i protecció ambiental**, no un contingut d'acabat decoratiu.

**Què fa aquesta graella amb `4g`, i què NO fa:**

| | |
|---|---|
| Inclou el criteri a la taula | **Sí**, a §3.4, amb el text literal i marcat `PENDENT` |
| Li assigna un saber | **No.** Seria inventar contingut curricular |
| Li assigna una activitat | **No** |
| Li assigna hores | **No.** Queden **0 h assignades**; les 77 h de la fase 4 les cobrien els altres set criteris |
| Li assigna un instrument | **No.** L'instrument és `PENDENT` |
| Construeix un contingut decoratiu per omplir-lo | **No.** |

**Com tractar-lo a l'aula, sense inventar:** el criteri **sí que és exigible** —
està al RD vigent i el Decret 117/2025 declara els criteris «prescriptivos» (art.
3.2). Però **no hi ha cap contingut curricular del mòdul que ens diga què es
considera un embelleidor correcte col·locat**. Per tant, de moment **no es pot
valorar amb un contingut oficial**. Dues vies, i totes dues s'han de declarar com a
**material complementari, no com a contingut curricular**:

1. **Decisió expressa del centre**, documentada i sotmesa a revisió docent, que
   concrete què s'avalua en `4g` amb referència a la pràctica professional. Cal que
   quede per escrit amb el seu autor i la seva data.
2. **Consulta a la conselleria competent**, si es vol una base normativa.

Aquesta graella **no fa cap de les dues coses**. Deixa el criteri visible,
documentat i sense omplir. Vegeu P-3 i P-19.

### 3.9 Contingut oficial que cal llegir abans de tancar la graella

Tres elements del text oficial de F-037 requerixen una lectura especial, perquè
**no es tracten com la resta**: dos no tenien cap itinerari d'integració i un
és redundant amb un altre. La justificació curricular completa, criteri per
criteri, és de la fase 2 (`sortides/esborranys/relacions-3016-sabers.md`
**§3.10**, **§3.11**, **§3.12** i el registre de canvis **§12**); ací només es
recull el que el professorat necessita per usar la graella.

#### 3.9.1 `CB b5.i6` — contingut oficial exigible **sense criteri que l'avalui** (`P-23`)

| | |
|---|---|
| Text literal de F-037 (bloc 5, ítem 6 de 6) | «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» |
| Quin RA el cobreix | **RA 5**, literalment: «Realiza operaciones **básicas de configuración** en redes locales cableadas relacionándolas con sus aplicaciones.» |
| Quin criteri el cobreix | **cap.** Cap dels 7 criteris de RA 5 avalua, ni amb el seu verb, una operació de configuració; el més proper, `5c`, s'atura a `**reconocido**` i el seu contingut és `CB b5.i5`. Cap altre dels 44 criteris tampoc |
| Què s'ha creat | el **`saber fer` `SB-3016-40`** (`[TEXT EXTRET]`, Annex A.2), amb origen `CB b5.i6` i RA 5 |
| itinerari que rep | **activitat** `ACT-6` i `ACT-9`, valorades amb instrument `[PROPOSTA]` (P-17). **No rep criteri**, i no se n'estén ni se'n crea cap de nou |
| Conseqüència per al professorat | el contingut **sí que és exigible** (el cobreix el RA 5) i **sí que es pot ensenyar i valorar**, però **la valoració no serà la d'un criteri exigible del RD**, sinó instrument `[PROPOSTA]` sobre una activitat. La limitació és **del text de la norma**, no d'aquest document |

#### 3.9.2 `OP v8` — contingut oficial **sense itinerari possible** (`P-24`)

| | |
|---|---|
| Text literal de F-037 (vinyeta 8 de 8 de les línies d'actuació) | «La toma de medidas de las magnitudes típicas de las instalaciones.» |
| Per què no n'hi ha | **cap dels 44 criteris parla de prendre mesures** i **cap dels 29 continguts bàsics** nomena magnituds ni instruments de mesura. Fals amic descartat: `CB b6.i4` («Determinación de las **medidas** de prevención…») parla de mesures de *prevenció*, no de mesures de *magnituds*, i no es pot reutilitzar per cobrir-ho |
| Què **no** s'ha fet | **cap saber nou** i **cap criteri nou**, perquè seria inventar contingut. **Aquesta graella no li inventa cap itinerari** |
| El que sí que queda al taller | que es prenguen mesures de longituds i recorreguts dins d'`ACT-3` i `ACT-9` és **material complementari `[PROPOSTA]`**, **no contingut curricular**: no crea cap criteri, no dona cap nota oficial i **no resol `P-24`**, que continuarà obert |

#### 3.9.3 `OP v7` — contingut oficial **redundant**, resolt i en consta (`P-25`)

| | |
|---|---|
| Text literal de F-037 (vinyeta 7 de 8) | «La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.» |
| Equivalent ja cobert per | `SB-3016-26`, d'origen `CB b4.i2`: «**Montaje** de **sistemas y elementos** de **las instalaciones de telecomunicación**.» |
| Reserva de literalitat | els dos textos **no són idèntics caràcter per caràcter** (`La aplicación de técnicas de` / `Montaje de`; `las instalaciones` / `las instalaciones de telecomunicación`). La cobertura és **de sentit equivalent**, i per això `OP v7` **no pot ser el text d'un saber `[TEXT EXTRET]` propi** sense duplicar el contingut |
| Què s'ha fet | `OP v7` queda **co-origin declarat de `SB-3016-26`** (Annex A.2) i origen equivalent dels criteris `4a` i `4c` → `ACT-5`, `ACT-9`. **Es declara redundant**: no afegeix cap contingut nou perquè el que diu ja s'ensenya, s'avalua i es traça |
| Estat | **resolt**, no pendent (`P-25` a §7.1) |

#### 3.9.4 Recompte de cobertura del contingut oficial

| Contingut oficial de F-037 | Recompte | Què queda fora i per què |
|---|---|---|
| Ítems de continguts bàsics **dels quals en deriva algun saber** | **28 de 29** | Només en queda fora un, i és el que s'ha creat: `CB b5.i6`, que **ja en té** (`SB-3016-40`). Pujar a 29 exigiria un altre saber que repetís el mateix contingut: no es fa |
| Ítems de continguts bàsics **avaluat per algun criteri** | **27 de 29** | `CB b5.i6` (cap criteri, §3.9.1) i `CB b4.i1` (parcial: només la primera part, «Características y tipos de las fijaciones.», n'és text de `SB-3016-06`; la segona, «Técnicas de montaje.», queda coberta **en sentit** per `SB-3016-20` i `SB-3016-28`) |
| Vinyetes de les orientacions pedagògiques **de les quals en deriva algun saber** | **7 de 8** | `OP v7` redundant (§3.9.3) · `OP v8` **`PENDENT`** (§3.9.2) |
| Ítems de continguts bàsics perduts | **0** | |
| Vinyetes de les orientacions perdudes | **0** | |

**Cap element del text oficial s'ha perdut ni ha quedat en silenci.** Els que no tenen
itinerari possible estan **nomenats, amb el motiu exacte i amb codi de pendent**
(`P-23` i `P-24`), i el redundant **consta com a tal** (`P-25`).

*Nota de redacció:* a la fase 2 (§3.13) aquesta taula diu «amb cap saber que en
deriva» al costat del recompte «28 de 29», cosa que es llegeix al revés. Ací
s'ha corregit la formulació perquè el recompte i l'etiqueta diguen el mateix; els
**recomptes no canvien** i el fitxer de la fase 2 no s'ha tocat.

---

## 4. ODS i temes transversals

### 4.1 Advertiment, sense matisos

1. **Les cerques de text complet al bloc del mòdul `3016` de F-037 donen 0
   coincidències** de `ODS`, `objetivos de desarrollo sostenible`, `Agenda 2030`,
   `desarrollo sostenible`, `sostenible`, `sostenibilidad` i `transversal`.
2. **F-035** (Decret 117/2025) menciona `ODS` **1 sola vegada** a tot el PDF
   oficial, al **preàmbul**, i és una consideració **a escala de cicle**. **No
   assigna cap ODS a cap mòdul.** No conté cap llista de «temas transversales»
   (`temas transversales` = 0 coincidències); el contingut transversal es configura
   via l'art. 4.1, l'art. 5.2 i l'art. 10.3, tots adreçats al centre i al cicle.
3. Per tant: **la categoria `VERIFICADA` aplicada al mòdul `3016` és BUIDA.** Cap
   relació d'ODS ni de tema transversal figura com a exigència curricular d'aquest
   mòdul. **Totes són `[PROPOSTA]`.**
4. Les remissions `V-3016-ODS` i `V-3016-TT` que haurien de acreditar la vinculació
   al mòdul són **`PENDENT`** (P-1 i P-2). Mentre siguen `PENDENT`, cap relació no
   puja a exigible.
5. **F-001** (ONU) acredita **només el text literal de la denominació** de cada
   objectiu. **Mai no acredita l'exigibilitat curricular i aquí no s'ha usat per
   justificar cap exigència.** L'evidència de la reverificació del text
   (2026-10-01) encara no s'ha incorporat al registre de fonts: pendent **P-14**.

### 4.2 ODS proposats — tots `PROPOSTA`

| ID | Text literal de l'objectiu (**F-001** · només font del text · consulta 2026-10-01 · evidència pendent d'incorporar al registre, **P-14**) | Denominació literal al Decret (**F-035**, preàmbul, pàg. 2/58) | Justificació pedagògica de la proposta | Vincle a activitats | Estat |
|---|---|---|---|---|---|
| **ODS-04** | *«Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all.»* | «el objetivo **4 de educación de calidad**» | `ACT-9` (projecte integrador) i `ACT-1` (memòria tècnica de l'edifici) són escenaris on l'alumne aprén una professió tècnica de base i documenta el seu propi procés. | `ACT-1`, `ACT-9` | **`PROPOSTA`** |
| **ODS-08** | *«Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all.»* | «el objetivo **8 trabajo decente y crecimiento económico**» | `ACT-4` i `ACT-5` es recolzen en les orientacions pedagògiques literals —«instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos»—, que són la porta d'entrada a l'ocupació tècnica en instal·lacions. | `ACT-4`, `ACT-5`, `ACT-9` | **`PROPOSTA`** |
| **ODS-10** | *«Reduce inequality within and among countries.»* | «el objetivo **10, reducción de desigualdades, como reto global y actuación autonómica**» | Les tasques de `ACT-9` es plantegen sobre un «petit entorn» (paraula literal de les orientacions): el criteri s'avalua dins del mateix grup i context, amb rúbrica compartida. | `ACT-9` | **`PROPOSTA`** |
| **ODS-12** | *«Ensure sustainable consumption and production patterns.»* | «el objetivo **12, producción y consumo responsables**» | `ACT-8` (retirada selectiva de residus, neteja i ordre) connecta amb ODS-12 **només per via pedagògica**. L'única dada ambiental literal del mòdul és `protección ambiental` (títol del RA 6, capçalera del bloc 6 i dues vinyetes), que és **contingut de prevenció i protecció ambiental, no capçalera d'ODS**. **No la converteixo en vincle d'ODS sense fonamentar-ho.** | `ACT-7`, `ACT-8` | **`PROPOSTA`** |

**ODS no proposats:** ODS-01, 02, 03, 05, 06, 07, 09, 11, 13, 14, 15, 16 i 17.
F-035 **no els menciona** i no hi ha cap vincle curricular raonable amb els
continguts bàsics de `3016`. Romanen `PENDENT`.

### 4.3 Temes transversals proposats — tots `PROPOSTA`

| ID | Contingut transversal | Text literal de **F-035** · apartat i pàgina | Vinculació pedagògica **proposada** | Criteris implicats | Estat |
|---|---|---|---|---|---|
| **TT-001** | Prevenció de riscos laborals | «Se potenciará o creará la cultura de prevención de riesgos laborales en los espacios donde se impartan los diferentes módulos profesionales […]» · art. 10.3, pàg. 7/58 | `ACT-7`: instruccions de treball segur i identificació de riscos abans de la manipulació. Ancorada al **RA 6 sencer**, que és text literal de F-037. | `6a`–`6e`, `6h` | **`PROPOSTA`** |
| **TT-002** | Respecte ambiental | «[…] así como una cultura de respeto ambiental […]» · art. 10.3, pàg. 7/58 | `ACT-8`: separació i retirada selectiva de residus de l'obra. S'ancora en el contingut bàsic literal «Cumplimiento de la normativa de protección ambiental.» | `6f`, `6g`, `6h` | **`PROPOSTA`** |
| **TT-003** | Treball de qualitat i normes de qualitat | «[…] trabajo de calidad realizado conforme a las normas de calidad […]» · art. 10.3, pàg. 7/58 | `ACT-3`: control de la fixació mecànica i del mecanitzat. | `2d`, `2e`, `2g` | **`PROPOSTA`** |
| **TT-004** | Creativitat i innovació | «[…] creatividad, innovación […]» · art. 10.3, pàg. 7/58 | `ACT-5` i `ACT-6`: l'alumne tria solucions de muntatge i configura la xarxa dins dels marges dels continguts bàsics, amb criteri propi documentat. | `4c`, `5f`, `5g` | **`PROPOSTA`** |
| **TT-005** | Igualtat de gènere | «[…] igualdad de género […]» · art. 10.3, pàg. 7/58 | `ACT-9`: rols rotatius i avaluació amb rúbrica comuna, sense tractar el gènere com a eix curricular del mòdul. | tots els RA | **`PROPOSTA`** |
| **TT-006** | Respecte a la diversitat | «[…] respeto a la diversidad […]» · art. 10.3, pàg. 7/58 | `ACT-2` i `ACT-4`: alternatives de material i de mètode (par trenat, coaxial, fibra), recolzades en el criteri literal «entre otros» dels continguts bàsics. | `1c`, `3a` | **`PROPOSTA`** |
| **TT-007** | Promoció de la igualtat d'oportunitats | «[…] promoción de la igualdad de oportunidades […]» · art. 10.3, pàg. 7/58 · i preàmbul, pàg. 3/58: «Se proporcionarán los apoyos necesarios para avanzar en la supresión de cualquier tipo de barrera de aprendizaje, de acceso a la información y a la comunicación, garantizando así la igualdad de oportunidades» | `ACT-1` i `ACT-6`: representació del mapa de xarxa en formats oberts i documentació accessible de la instal·lació. | `2c`, `5e`, `5f`, `5g` | **`PROPOSTA`** |
| **TT-008** | Disseny per a totes les persones i accessibilitat universal | «[…] el diseño para todas las personas y la accesibilidad universal» · art. 10.3, pàg. 7/58 | `ACT-1`: traçat d'itineraris de cablejat que no interfereixen amb el pas de les persones i ubicació de preses i armaris a altura accessible. **Es proposa com a criteri de revisió de la memòria tècnica, no com a criteri d'avaluació**, perquè el RD no el recull. | `2c`, `2f`, `3f` | **`PROPOSTA`** |
| **TT-009** | Projecte intermodular d'aprenentatge col·laboratiu: RA treballats transversalment | «Además de la selección concreta realizada por el equipo docente según la especialidad del ciclo, se trabajarán transversalmente los RA que figuran en el currículo del proyecto» · art. 5.2, pàg. 5/58 | `ACT-9` és el vehicle natural per connectar amb el projecte intermodular `3160972` del 2n curs. **Reserva:** no s'ha verificat **quin** RA del projecte toca `3016`; cal el currículum bàsic del projecte (P-11). | tots els RA | **`PROPOSTA`** |
| **TT-010** | Estructura en tres àmbits | El cicle «constará de tres ámbitos y el proyecto» · art. 4.1, pàg. 4/58; organització de matèries a l'Anexo III-B, pàg. 45/58 (taula d'Informática de oficina, pàg. 53/58) | `3016` pertany a l'**àmbit Professional**. L'Anexo III-B només organitza l'àmbit de Comunicació i Ciències Socials (`3161`/`3162`), **no** el professional. | (estructural, sense criteri) | **`PROPOSTA`** |

### 4.4 Recompte d'aquesta secció

| Dada | Recompte |
|---|---|
| Relacions ODS proposades | **4** (ODS-04, 08, 10, 12), totes `PROPOSTA` |
| Relacions ODS `VERIFICADA` **al mòdul `3016`** | **0** |
| Relacions TT proposades | **10** (TT-001 … TT-010), totes `PROPOSTA` |
| Relacions TT `VERIFICADA` **al mòdul `3016`** | **0** |
| ODS de l'Agenda que romanen `PENDENT` | 13 |
| Vinculacions acreditades al mòdul | `V-3016-ODS` = `PENDENT` · `V-3016-TT` = `PENDENT` |

---

## 5. Distribució temporal

### 5.1 Context curricular autoritatiu

| Dada | Valor | Font i apartat | Data | Estat |
|---|---|---|---|---|
| Càrrega horària setmanal | **10 h/setmana** | **F-032**, Decret 117/2025, Anexo III-A, taula «Informática de oficina», **pàg. 34/58** (remissió a l'art. 3.8, pàg. 4/58) | 2026-10-01 | `VERIFICADA` |
| Càrrega horària anual | **332 h/any** | idem | 2026-10-01 | `VERIFICADA` |

### 5.2 Advertiment aritmètic, perquè la repartició no pot donar-se per feta

`332 h ÷ 10 h/setmana = 33,2` **setmanes-equivalent**. Això vol dir que
l'any lectiu del mòdul **no cabeix en 30 setmanes exactes de 10 h**: en un
calendari de 30 setmanes lectives quedarien 32 h sense col·locar. Aquest
`[INTERPRETACIÓ]` és aritmètica sobre les dades de F-032, i **no** resol el
problema:

- **Cap font curricular distribueix les 332 h en setmanes, sessions ni blocs.**
  La taula de §5.3 és `[PROPOSTA]`.
- El **calendari concret** (quines setmanes, quantes sessions de quantes hores i
  com s'ajusta la diferència) el fixa **l'equip docent del centre**, d'acord amb
  la conselleria competent. **Aquesta graella no el substitueix.**
- Hi ha una **divergència oberta** entre la norma (F-032: 10 h/sem · 332 h) i les
  fitxes i dosiers de consulta a CEICE (F-033 / F-034 / F-036: 8 h/sem · 266 h).
  **Preval F-032**, però la discrepància està registrada com a **P-16** (incidències
  I-2 i I-3 del registre).

### 5.3 Repartiment proposat `[PROPOSTA]`

**Els intervals de setmanes són indicatives i no se solapen.** Cadascuna de les
fases 1 a 5 ocupa un interval **disjunt** i, entre elles, cobrien les setmanes
1 a 30 sense cap setmana compartida. La fase 6 (RA 6) és **transversal** i, per
definició, no pot ser disjunta: ocupa tot el curs.

| Fase | Contingut (bloc de continguts bàsics de F-037) | Criteris | Hores | Setmanes **indicatives** | Què hi treballa |
|---|---|---|---|---|---|
| **1** | RA 1 · bloc 1 «Selección de elementos de redes de transmisión de voz y datos» | `1a`–`1f` | **55** | 1–5 | `ACT-1`, `ACT-2` |
| **2** | RA 2 · bloc 2 «Montaje de canalizaciones, soportes y armarios…» | `2a`–`2h` | **77** | 6–12 | `ACT-3` |
| **3** | RA 3 · bloc 3 «Despliegue del cableado» | `3a`–`3g` | **66** | 13–18 | `ACT-4` |
| **4** | RA 4 · bloc 4 «Instalación de elementos y sistemas…» | `4a`–`4f`, `4h` (**`4g` = `PENDENT`**) | **77** | 19–25 | `ACT-5` |
| **5** | RA 5 · bloc 5 «Configuración básica de redes locales» + lliurament de `ACT-9` | `5a`–`5g` | **39** | 26–30 | `ACT-6`, `ACT-9` |
| **6** | RA 6 · bloc 6 «Cumplimiento de las normas de prevención…» — **transversal, tot el curs** | `6a`–`6h` | **18** | 1–30 (≈ 0,6 h/setmana) | `ACT-7`, `ACT-8` |
| | **TOTAL** | **44 criteris** (43 amb cobertura curricular) | **332** | **setmanes 1–30, sense solapaments** | 9 activitats |

**Com s'han calculat els intervals.** Cada fase ocupa un nombre de setmanes
proporcional a les seues hores, arrodonint a setmanes completes: 55 h → 5
setmanes, 77 h → 7, 66 h → 6, 77 h → 7 i 39 h → 5. **Són indicatives perquè
cap font curricular distribueix les 332 h** (pendents **P-7** i **P-18**): no
són un calendari, sinó un ordre de treball. L'equip docent ha d'adaptar-les al
calendari real del centre.

### 5.4 Advertiments sobre aquesta taula

1. **§5.4.1 · El RA 6 travessa tot el curs.** No es redueix a les darreres setmanes: el
   criteri `6h` parla de l'ordre i la neteja com a factor de prevenció en **cada**
   operació, i els criteris `2h` i `4h` apliquen normes de seguretat **des del
   primer dia**. `[PROPOSTA]`
2. **§5.4.2 · `ACT-9` s'avalua dins de la fase 5 i es lliura a finals de curs.** Com que el
   RA 6 ja s'ha avaluat al llarg del curs, el lliurament final no necessita una fase
   6 separada. `[PROPOSTA]`
3. **§5.4.3 · No hi ha cap setmana compartida entre les fases 1 a 5** (1–5, 6–12, 13–18,
   19–25, 26–30), cosa que no era així abans d'aquesta revisió. El que sí que és
   transversal és la fase 6, i això està dit, no sobreentès.
4. **§5.4.4 · Els intervals són indicatius i s'han d'ajustar.** 332 h ÷ 10 h/setmana =
   33,2 setmanes-equivalent (§5.2): les fases 1 a 5 ocupen 30 setmanes i, si el
   curs fa 10 h/setmana de `3016` durant les 30 setmanes lectives, **32 h quedarien
   sense col·locar**. Aquesta diferència **no** la resol la graella; l'ha de fixar el
   centre, allargant els intervals o recuperant les hores en sessions de
   reinforce. `[PROPOSTA]`
5. **§5.4.5 · L'ordre i la coordinació amb la resta de mòduls del 2n curs no estan
   verificats** (`3030`, `3159`, `3162`, `3164`, `TU02CF`, `3160972`). Dependent de
   com es coordine el RA 6 amb els altres mòduls i de com s'ordenen les fases 1 i 2,
   cap font consultada ho diu: pendent **P-8**.
6. **§5.4.6 · Les hores per criteri** (§3) són un repartiment del bloc de 332 h ** fet pel
   projecte**. Cap font curricular el fixa. **Cal revisió docent** i el calendari
   real del centre (**P-18**, **P-7**).
7. **§5.4.7 · Les hores del criteri `4g` queden sense assignar.** Les 77 h de la fase 4 les
   cobrien els set criteris restants, que sí que tenen contingut bàsic. Quan, i com,
   s'assignen hores a `4g` depèn de resoldre **P-3** i **P-19**.
8. **§5.4.8 · Del material disponible al centre en depèn la viabilitat d'aquest repartiment.**
   Cap font acredita quins equips, eines o espais hi ha a l'aula, i de `ACT-3` a
   `ACT-6` i a `ACT-9` hi depèn: pendent **P-9**.

---

## 6. Advertiments de traçabilitat

### 6.1 Què és **text oficial** i per tant exigible

| Element | Font | Apartat | Recompte |
|---|---|---|---|
| Resultats d'apreneatge | **F-037** | Annex VII, 3.3, bloc `Código: 3016.` | **6** |
| Criteris d'avaluació | **F-037** | idem | **44** |
| Continguts bàsics (capçaleres i ítems) | **F-037** | idem | **6 blocs / 29 ítems** |
| Orientacions pedagògiques | **F-037** | idem | 4 paràgrafs + 8 vinyetes |
| Càrrega horària curricular | **F-032** | Anexo III-A, pàg. 34/58 | 10 h/set · 332 h/any |
| El camp `Duración: 115 horas.` | **F-037** | idem | text oficial **sense definir**; **no** és l'horari |

L'**art. 3.2 del Decret 117/2025** declara els RA i els criteris dels mòduls
professionals **«prescriptivos»**. Per això la formulació literal dels 44 criteris
no es toca, encara que done problemes (és el cas de `4g`).

### 6.2 Què és **resum** del projecte

| Element | Què se'n resumeix | On |
|---|---|---|
| `SB-3016-05` | Característiques que permeten determinar la tipologia de caixes | §3.1 · criteri `1d` |
| `SB-3016-06` — **reserva de `[TEXT EXTRET (parcial)]`, no un resum** | **Només la primera part** de l'ítem oficial `CB b4.i1`. El que hi ha escrit **sí que és literal**, caràcter per caràcter, i **no es reformula**, però **no reprodueix l'ítem sencer**; per això porta l'etiqueta **`[TEXT EXTRET (parcial)]`** (§0.1) en lloc de `[TEXT EXTRET]` a seques. L'ítem oficial és «Características y tipos de las fijaciones. **Técnicas de montaje.**» i la segona frase **no és el text de cap altre saber**; queda coberta només **en sentit** per `SB-3016-20` i `SB-3016-28`. **Reserva declarada** (correcció D-5). | §3.1, §3.4 · Annex A.1 |
| `SB-3016-36` | Actuar preventivament: identificar riscos abans de manipular | §3.6 · `6a`, `6c`, `6e` |
| `SB-3016-37` | Fer servir els EPI que corresponguen a cada operació | §3.6 · `6d`, `6e` |
| `SB-3016-38` | `[RESUM]`: assumeix l'abast de la funció professional del mòdul. **De la formulació del saber, només n'és literal el fragment entre comilles angulars** («instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos»); la resta és formulació del projecte (correcció D-6) | §2.1, Annex A.3 · transversal a tots els RA |
| `SB-3016-39` | Treballar de manera segura, ordenada i neta com a primer factor de prevenció | §3.3, §3.4, §3.6 · `3g`, `4f`, `6h` |
| Els textos de la columna «Criteri» de les taules de §3 | Resums fidels del text literal del criteri, que es conserva a la columna adjacent | §3.1–§3.6 |
| El caràcter del camp `Duración` | Cap interpretació no és sostenible: el RD no el defineix | §1.3, I-7, P-6 |

### 6.3 Què és **interpretació** del projecte

| Lectura | on |
|---|---|
| Les 115 h del camp `Duración` no són l'horari del curs i no s'han de convertir en sessions | §0.3, §1.3, P-6 |
| 332 h ÷ 10 h/setmana = 33,2 setmanes-equivalent; en 30 setmanes quedarien 32 h sense col·locar | §5.2, §5.4.4 |
| L'abast del mòdul és «instalaciones de redes locales en pequeños entornos» (paraula literal de les orientacions) | §2.1, `ACT-9` |
| La denominació de les competències es llegeix com a «competencias profesionales y para la empleabilidad» per la disposició addicional sisena de F-038 | §0.4 |
| Cap criteri de `3016`, ni de RA 5, avalua una operació de **configuració**: el contingut `CB b5.i6` és exigible per RA, però la seva valoració no pot ser la d'un criteri | §3.9.1, P-23 |

### 6.4 Què és **proposta** del projecte i no l'exigeix cap norma

| Element | Nombre | Etiqueta |
|---|---|---|
| Desglossament en **40** sabers (18 / 14 / 8) amb codis `SB-3016-nn` | 40 | `[RESUM]` si el text és resum; la codificació i el desglossament són del projecte (P-15) |
| 9 activitats didàctiques `ACT-1`…`ACT-9` | 9 | `[PROPOSTA]` |
| Instruments d'avaluació de cada criteri | **43 assignacions · 34 formulacions · 10 famílies** | `[PROPOSTA]` (P-17) |
| Hores estimades per criteri | 44 files (43 amb hores + `4g` a 0) | `[PROPOSTA]` (P-18) |
| Distribució temporal en 6 fases i setmanes indicatives 1–30 | 6 fases | `[PROPOSTA]` (P-7, P-8, P-18) |
| 4 relacions amb ODS | 4 | `[PROPOSTA]` (P-1, P-14) |
| 10 relacions amb temes transversals | 10 | `[PROPOSTA]` (P-2) |
| La reserva de TT-008 com a criteri de revisió de la memòria, no d'avaluació | 1 | `[PROPOSTA]` |

**Sobre el recompte d'instruments (correcció D-3).** Abans d'aquesta revisió
aquesta taula deia «8 tipus» i el recompte **no quadrava** amb el que hi ha. El que
hi ha realment és així, i es pot comptar fila a fila sobre les 44 files de §3:

| Família d'instrument | Formulacions distintes | Files |
|---|---|---|
| Rúbrica (inclou «Banc d'elements + rúbrica») | 16 | 17 |
| Prova escrita (inclou «Fitxa de materials i prova escrita») | 2 | 5 |
| Prova pràctica de taller (inclou «Prova pràctica amb rúbrica») | 2 | 6 |
| Inspecció o llista de verificació | 3 | 3 |
| Diari de taller | 3 | 4 |
| Lliurable | 2 | 2 |
| Fitxa o llistat | 2 | 2 |
| ITTS (instrucció de treball segur) | 2 | 2 |
| Memòria tècnica | 1 | 1 |
| Revisió de seguretat en taller | 1 | 1 |
| **Total** | **34** | **43** |

La 44a fila (`4g`) és `PENDENT` i no compta. Els noms compostes («+ rúbrica»,
«+ revisió de l'eina», «+ anàlisi de casos») **no són famílies noves**: es compten
en la família del seu element principal. Per tant, **no hi ha 8 tipus sinó 34
formulacions en 10 famílies**, i el detall anterior és el que fa el recompte
comprovable. **Tot és `[PROPOSTA]` (P-17) i tot ha de passar la revisió docent
(P-21).**

### 6.5 El que aquesta graella **no** fa

- **No assigna cap competència** a cap de les lletres `a)`–`i)` de les orientacions
  pedagògiques (P-12).
- **No crea cap contingut curricular** que no estiga als 29 continguts bàsics o a les
  8 vinyetes de les orientacions.
- **No estén cap criteri oficial** per omplir un buit. En particular, **no estén
  `5c`** perquè done cobertura a `CB b5.i6`, ni crea cap criteri nou per a la
  configuració de dispositius (§3.9.1, P-23).
- **No inventa cap itinerari curricular per a `OP v8`**, que queda `PENDENT` amb el
  motiu exacte (§3.9.2, P-24), ni presenta la pràctica de taller que la pot
  introduir com a contingut oficial.
- **No converteix `protección ambiental` en capçalera d'ODS.** És contingut de
  prevenció i protecció ambiental i això és tot.
- **No presenta cap relació d'ODS ni de TT com a exigència curricular.** La categoria
  `VERIFICADA` al mòdul és buida.
- **No omple el criteri `4g` amb contingut inventat.**
- **No ofereix les 115 h com a horari** ni com a alternativa a les 332 h.
- **No substitueix el calendari del centre** ni el currículum bàsic del projecte
  intermodular.
- **No es declara validada per la seva compte.** Hi ha un informe de validació
  independent a `sortides/informes-validacio/informe-validacio-3016.md` i cal
  llegir-lo; corregir els defectes que hi consten **no** substitueix la
  revalidació, que és del `verificador`.

---

## 7. Registre de pendents i nota de correcció

### 7.1 Tot allò que queda `PENDENT` en aquesta graella

| ID | Què queda pendent | On apareix a la graella | Estat |
|---|---|---|---|
| **P-1** | Vinculació acreditada d'un ODS al mòdul (`V-3016-ODS`) | §4.1, §4.4 | `PENDENT` |
| **P-2** | Vinculació acreditada d'un tema transversal al mòdul (`V-3016-TT`) | §4.1, §4.4 | `PENDENT` |
| **P-3** | Criteri `4g` sense contingut bàsic | §3.4 (fila `4g`), §3.8 | `PENDENT` |
| **P-4** | Elements dels criteris que els continguts bàsics no anomenen (19 criteris amb reserva) | Marcats «amb reserva» a les files de §3 | `PENDENT` |
| **P-5** | Criteri `3g` sense criteri d'avaluació propi | §3.3 (fila `3g`) | `PENDENT` |
| **P-6** | Caràcter del camp `Duración: 115 horas.` | §0.3, §1.3, §6.2 | `PENDENT` (incidència **I-7**) |
| **P-7** | Distribució de les 332 h en setmanes i sessions | §5.3, §5.4 | `PROPOSTA` |
| **P-8** | Calendari de les fases 1 i 2 i coordinació del RA 6 amb la resta de mòduls del 2n curs | §5.4.5 | `PENDENT` |
| **P-9** | Equips, eines i espais disponibles al centre | §5.4.8, Annex B | `PENDENT` |
| **P-10** | Format i eina del «mapa físico» | §3.5 (files `5f`, `5g`), Annex B (`ACT-6`) | `PENDENT` |
| **P-11** | Quins RA del projecte intermodular toquen `3016` | §4.3 (`TT-009`) | `PENDENT` |
| **P-12** | Lletres de les competències de les orientacions pedagògiques | §0.4 | `PENDENT` |
| **P-13** / **P-20** | Reverificació directa de F-037 i de F-032 | Annex C (nota de procedència), §6.1 | `PENDENT` |
| **P-14** | Actualització del registre de fonts per a F-001 | §4.1, §4.2 | `PENDENT` (de registre) |
| **P-15** | Codificació pròpia `SB-…`, `ACT-…`, `CB b#.i#`, `OP v#` | §0.2, Annex A, Annex B | `PENDENT` (declarada a la graella) |
| **P-16** | Divergència d'hores DOGV / fitxes CEICE | §0.3, §5.2 | `PENDENT` (incidències **I-2**, **I-3**) |
| **P-17** | Instruments d'avaluació de cada criteri | §3 (columna «Instrument»), §6.4 | `PENDENT` |
| **P-18** | Hores per criteri i ordre concret de blocs setmanals | §3 (columna «Hores»), §5.3, §5.4 | `PENDENT` |
| **P-19** | Hores del criteri `4g` | §3.4 (fila `4g`), §3.7, §5.4.7 | `PENDENT` |
| **P-21** | Revisió docent de tot allò que és `[PROPOSTA]` | §6.4 | `PENDENT` |
| **P-22** | Denominació literal de la família professional | §1.2 | `PENDENT` |
| **P-23** | **Contingut oficial exigible sense criteri que l'avalui: `CB b5.i6`** | §3.5 (nota), §3.7, §3.9.1, Annex A.2, Annex B (`ACT-6`, `ACT-9`), §6.5 | `PENDENT` |
| **P-24** | **Contingut oficial sense itinerari possible: `OP v8`** | §2.1, §3.9.2, Annex B (`ACT-3`, `ACT-9`), §6.5 | `PENDENT` |
| **P-25** | **`OP v7` redundant amb `CB b4.i2`** — resolt donant-li co-origin explícit de `SB-3016-26` | §2.1, §3.9.3, Annex A.2, Annex B (`ACT-5`) | **`RESOLT`** |

El registre complet, amb el motiu exacte de cadascun, és a
`sortides/informes-validacio/informe-fonts-3016.md` §4.

### 7.2 Què s'ha corregit en aquesta revisió i què no

La fase 4 (`verificador`) va emetre el **2026-10-01** l'informe independent
`sortides/informes-validacio/informe-validacio-3016.md`: **cap defecte
bloquejant**, 9 defectes no bloquejants i 4 reserves. Aquesta revisió ha corregit
els que eren d'aquesta fase i ha sincronitzat els que eren de la fase 2.

| Defecte | Què se n'ha fet | On |
|---|---|---|
| **D-1** (alta, origen fase 2) | **Sincronitzat**, no redissenyat: `CB b5.i6` rep itinerari via `SB-3016-40` (tipus **saber fer**, RA 5 i activitat `ACT-6`/`ACT-9`, **sense criteri**, `P-23`); `OP v8` queda `PENDENT` **sense itinerari inventat** (`P-24`); `OP v7` es declara **co-origin de `SB-3016-26`** amb reserva de literalitat (`P-25`) | §2.1, §3.5, §3.7, §3.9, Annex A.2, Annex B |
| **D-2** (mitjana) | La fila `6f` es queda amb **`ACT-8` només** (`ACT-7` avala `6a`–`6e`, no `6f`) | §3.6 (fila `6f`) |
| **D-3** (baixa) | «8 tipus» d'instruments, que no quadraven, substituïts per **43 assignacions · 34 formulacions · 10 famílies**, amb taula que fa el recompte comprovable fila a fila | §3.7, §6.4 |
| **D-4** (baixa) | Els **50** substituts `␣` (`U+2423`) dels quadres de §2 i §3 tornen al **caràcter oficial `U+2003`**. Els 44 criteris de la taula són ara **byte-idèntics** al text oficial | §2, §3.1–§3.6, §0.1 |
| **D-5** (baixa) | `SB-3016-06` ja no porta `[TEXT EXTRET]` a sobre d'un text truncat sense dir-ho: s'hi aplica l'etiqueta **`[TEXT EXTRET (parcial)]`** perquè es tracta d'una **subfrase literal parcial** de l'ítem oficial, i es declara a §0.1, §6.2 i Annex A.1. **No es reformula el text.** | Annex A.1, §6.2 |
| **D-6** (de la fase 2) | `SB-3016-38` passa a **`[RESUM]`** amb el literal delimitat i la reserva corresponent | Annex A.3, §6.2 |
| **D-7** (baixa) | «Sabers mobilitzats 39» → **38 a la taula + 2 que no sostenen cap criteri** (`SB-3016-38`, `SB-3016-40`) = **40 en total**, les taules per tipus passen a **18 / 14 / 8** i el recompte d'etiquetes s'ajusta a **34 `[TEXT EXTRET]` + 1 `[TEXT EXTRET (parcial)]` + 5 `[RESUM]` | §3.7, Annex A, capçalera |
| **D-8** (baixa) | Les setmanes indicatives passen a **intervals disjunts** (1–5, 6–12, 13–18, 19–25, 26–30), amb la fase 6 transversal declarada com a tal i amb la diferència de 32 h explicitada | §5.3, §5.4 |
| **D-9** (informativa) | Els codis **P-6**, **P-8**, **P-9**, **P-14** i **P-21** es citen allà on els tocar | §0.3, §1.3, §4.1, §4.2, §5.4, §6.4, Annex B, §7.1 |

**Què NO s'ha fet, i per què:**

- **No s'ha redissenyat cap itinerari** de la fase 2: els itineraris que hi arriben
  ja estan justificats criteri per criteri (§3.10–§3.12 de la fase 2) i aquí només
  es reflecteixen.
- **No s'ha creat, suprimit ni reescrit cap criteri oficial.** Els 44 de §3 són els
  44 de F-037, amb la mateixa numeració i el mateix text literal.
- **No s'ha tocat cap altre fitxer del projecte** en aquesta revisió: ni
  `fonts/registre-fonts.md`, ni els esborranys de les fases 1 i 2, ni l'informe de
  validació, que és del `verificador` i el torn de revalidar és seu.
- **Cap operació de git.**

### 7.3 Nota de fidelitat de caràcters

Al **Annex C** i als **quadres de §2 i §3** es reprodueix el text oficial amb els
caràcters especials del document original: espai fi `U+2003` entre la numeració i
el text (50 vegades als quadres i 50 al bloc literal), guion fi `U+2012` de les
vinyetes (40) i espai fi fi `U+2002` després de la vinyeta (37). **Al text
curricular ja no hi ha cap substitució per caràcters visibles**: els 50 espais
`U+2003` que abans s'havien
representat amb `␣` (`U+2423`) a la taula s'han restituït al caràcter oficial
(correcció **D-4**). El bloc literal de l'Annex C és **byte-idèntic** al de la
fase 1 i al de la fase 2.

**Les 2 aparicions de `U+2423` que queden al document són intencionades, i
aquestes línies les declaren com a tal** (reserva **D-4**, tancada per
declaració i no per supressió). **No són cap marcador d'espai**: les dues són el
**nom del caràcter**, dins d'un tram de codi, a la fila de **D-4** de §7.2 i a
la frase anterior d'aquesta secció, on es diu quin caràcter visible s'havia posat
en lloc de l'espai fi oficial i què se n'ha fet. **Sense elles, aquelles frases
no dirien quin caràcter era.** No toquen cap resultat d'aprenentatge, cap criteri,
cap contingut bàsic ni cap vinyeta: són **metatext del projecte** sobre la seua
pròpia correcció, no text oficial ni text exigible. **Cap altre caràcter visible
no oficial** no s'ha usat enlloc com a substitut: al recompte del fitxer hi ha
`U+2003` × 100 (50 als quadres de §2 i §3, 50 al bloc literal de l'Annex C),
`U+2012` × 40 i `U+2002` × 37, tots oficials i tots conservats.

---

## Annex A · Catàleg de sabers (40)

Codificació **del projecte** (P-15). Tots els sabers deriven dels **29 continguts
bàsics** i de les **8 vinyetes** de les orientacions pedagògiques de F-037.

| Tipus | Nombre | Sabers |
|---|---|---|
| `saber` — coneixement | **18** | `SB-3016-01` … `SB-3016-18` |
| `saber fer` — habilitat pràctica | **14** | `SB-3016-19` … `SB-3016-31` i `SB-3016-40` |
| `saber estar` — actituds i valors | **8** | `SB-3016-32` … `SB-3016-39` |
| **Total** | **40** | 34 `[TEXT EXTRET]` + 1 `[TEXT EXTRET (parcial)]` (`SB-3016-06`) + 5 `[RESUM]` |

### A.1 `saber` — coneixement (18)

| ID | Etiqueta | Text | Origen literal (F-037) |
|---|---|---|---|
| SB-3016-01 | `[TEXT EXTRET]` | «Instalaciones de infraestructuras de telecomunicación en edificios. Características.» | `CB b1.i2` |
| SB-3016-02 | `[TEXT EXTRET]` | «Medios de transmisión: cable coaxial, par trenzado y fibra óptica, entre otros.» | `CB b1.i1` |
| SB-3016-03 | `[TEXT EXTRET]` | «Sistemas y elementos de interconexión.» | `CB b1.i3` |
| SB-3016-04 | `[TEXT EXTRET]` | «Características y tipos de las canalizaciones: tubos rígidos y flexibles, canales, bandejas y soportes, entre otros.» | `CB b2.i2` |
| SB-3016-05 | `[RESUM]` | Característiques que permeten determinar la tipologia dels elements d'una instal·lació i, en particular, de les caixes: registres, armaris, «racks», caixes de superfície i de col·locar a obra. | `CB b1.i2` + `b1.i3` — **reserva**: la llista literal de tipus de caixa només consta al criteri `1d` |
| SB-3016-06 | `[TEXT EXTRET (parcial)]` | «Características y tipos de las fijaciones.» | `CB b4.i1` — l'ítem oficial sencer és «Características y tipos de las fijaciones. Técnicas de montaje.»; només la **primera frase** és text d'aquest saber, i per això l'etiqueta és **`[TEXT EXTRET (parcial)]`** i no `[TEXT EXTRET]` a seques. La segona, «Técnicas de montaje.», **no és el text de cap altre saber** i queda coberta **en sentit** per `SB-3016-20` i `SB-3016-28`. **Reserva:** cal llegir l'ítem oficial sencer per saber què queda fora de la cèl·la. **El fragment no es reformula** (reserva declarada a §0.1 i §6.2; correcció D-5) |
| SB-3016-07 | `[TEXT EXTRET]` | «Herramientas.» | `CB b4.i3` |
| SB-3016-08 | `[TEXT EXTRET]` | «Características. Ventajas e inconvenientes. Tipos. Elementos de red.» | `CB b5.i1` |
| SB-3016-09 | `[TEXT EXTRET]` | «Identificación de elementos y espacios físicos de una red local.» | `CB b5.i2` |
| SB-3016-10 | `[TEXT EXTRET]` | «Cuartos y armarios de comunicaciones.» | `CB b5.i3` |
| SB-3016-11 | `[TEXT EXTRET]` | «Conectores y tomas de red.» | `CB b5.i4` |
| SB-3016-12 | `[TEXT EXTRET]` | «Dispositivos de interconexión de redes.» | `CB b5.i5` |
| SB-3016-13 | `[TEXT EXTRET]` | «Normas de seguridad. Medios y sistemas de seguridad.» | `CB b6.i1` |
| SB-3016-14 | `[TEXT EXTRET]` | «Identificación de riesgos.» | `CB b6.i3` |
| SB-3016-15 | `[TEXT EXTRET]` | «Determinación de las medidas de prevención de riesgos laborales.» | `CB b6.i4` |
| SB-3016-16 | `[TEXT EXTRET]` | «Sistemas de protección individual.» | `CB b6.i6` |
| SB-3016-17 | `[TEXT EXTRET]` | «La identificación de sistemas, elementos, herramientas y medios auxiliares.» | `OP v1` |
| SB-3016-18 | `[TEXT EXTRET]` | «La identificación de los sistemas, medios auxiliares, sistemas y herramientas, para la realización del montaje y mantenimiento de las instalaciones.» | `OP v6` |

### A.2 `saber fer` — habilitat pràctica (14)

| ID | Etiqueta | Text | Origen literal (F-037) |
|---|---|---|---|
| SB-3016-19 | `[TEXT EXTRET]` | «Montaje de canalizaciones, soportes y armarios en las instalaciones de telecomunicación.» | `CB b2.i1` |
| SB-3016-20 | `[TEXT EXTRET]` | «Preparación y mecanizado de canalizaciones. Técnicas de montaje de canalizaciones y tubos.» | `CB b2.i3` |
| SB-3016-21 | `[TEXT EXTRET]` | «El montaje de las canalizaciones y soportes.» | `OP v2` |
| SB-3016-22 | `[TEXT EXTRET]` | «Recomendaciones en la instalación del cableado.» | `CB b3.i1` |
| SB-3016-23 | `[TEXT EXTRET]` | «Técnicas de tendido de los conductores.» | `CB b3.i2` |
| SB-3016-24 | `[TEXT EXTRET]` | «Identificación y etiquetado de conductores.» | `CB b3.i3` |
| SB-3016-25 | `[TEXT EXTRET]` | «El tendido de cables para redes locales cableadas.» | `OP v3` |
| SB-3016-26 | `[TEXT EXTRET]` | «Montaje de sistemas y elementos de las instalaciones de telecomunicación.» | `CB b4.i2` · **`OP v7` en és co-origin declarat** («La aplicación de técnicas de montaje de sistemas y elementos de las instalaciones.»): cobertura **equivalent però no idèntica** (`las instalaciones` / `las instalaciones de telecomunicación`), i per això no es crea cap saber nou per a `OP v7` ni es duplica contingut. Redundant, resolt, **P-25** · §3.9.3 |
| SB-3016-27 | `[TEXT EXTRET]` | «Instalación y fijación de sistemas en instalaciones de telecomunicación.» | `CB b4.i4` |
| SB-3016-28 | `[TEXT EXTRET]` | «Técnicas de fijación: en armarios, en superficie.» | `CB b4.i5` |
| SB-3016-29 | `[TEXT EXTRET]` | «Técnicas de conexionados de los conductores.» | `CB b4.i6` |
| SB-3016-30 | `[TEXT EXTRET]` | «El montaje de los elementos de la red local.» | `OP v4` |
| SB-3016-31 | `[TEXT EXTRET]` | «La integración de los elementos de la red.» | `OP v5` |
| SB-3016-40 | `[TEXT EXTRET]` | «Configuración básica de los dispositivos de interconexión de red cableada e inalámbrica.» | `CB b5.i6` (bloc 5, ítem 6 de 6) · **cap criteri de RA 5 el cobreix**: rep itinerari de **RA 5** i d'**activitat** (`ACT-6`, `ACT-9`), **mai de criteri**, i no s'estén ni se'n crea cap de nou per omplir el buit. Vegeu §3.9.1 i **P-23** |

### A.3 `saber estar` — actituds i valors (8)

| ID | Etiqueta | Text | Origen literal (F-037) |
|---|---|---|---|
| SB-3016-32 | `[TEXT EXTRET]` | «Cumplimiento de las normas de prevención de riesgos laborales y protección ambiental.» | `CB b6.i2` |
| SB-3016-33 | `[TEXT EXTRET]` | «Prevención de riesgos laborales en los procesos de montaje.» | `CB b6.i5` |
| SB-3016-34 | `[TEXT EXTRET]` | «Cumplimiento de la normativa de prevención de riesgos laborales.» | `CB b6.i7` |
| SB-3016-35 | `[TEXT EXTRET]` | «Cumplimiento de la normativa de protección ambiental.» | `CB b6.i8` |
| SB-3016-36 | `[RESUM]` | Actuar preventivament: identificar els riscos **abans** de manipular materials, eines i màquines i relacionar-los amb les mesures que cal aplicar. | `CB b6.i3` + `b6.i4` |
| SB-3016-37 | `[RESUM]` | Fer servir els equips de protecció individual que corresponguen a cada operació de muntatge i manteniment, i relacionar-los amb la manipulació concreta. | `CB b6.i4` + `b6.i6` — **reserva**: el llistat literal d'elements de seguretat de les màquines només consta al criteri `6d` |
| SB-3016-38 | `[RESUM]` | Assumir l'abast de la funció professional del mòdul, delimitat al literal següent: «instalar canalizaciones, cableado y sistemas auxiliares en instalaciones de redes locales en pequeños entornos». **Reserva:** la formulació del saber és del projecte; **només el fragment entre comilles angulars és literal**. | `OP`, 1r paràgraf (transversal a tots els RA) |
| SB-3016-39 | `[RESUM]` | Treballar de manera segura, ordenada i neta en cada operació de muntatge i manteniment, com a **primer factor de prevenció de riscos**. | `CB b3.i1` + `b6.i5` + `b6.i7` — **reserva**: l'ordre i la neteja com a primer factor només consten al criteri `6h` |

---

## Annex B · Catàleg d'activitats (9) — totes `[PROPOSTA]`

Cap activitat no ve exigida per cap font: totes deriven de sabers que, al seu torn,
deriven de text literal de F-037.

| ID | Activitat | Què fa l'alumne | Criteris que avalua | Sabers que mobilitza | ODS / TT (`PROPOSTA`) |
|---|---|---|---|---|---|
| **ACT-1** | Memòria tècnica de l'edifici i croquis d'ubicacions | Rep un croquis d'un edifici i hi situa els elements d'instal·lació, justificant cada decisió | `1a`, `1b`, `1d`, `2c`, `5e` | SB-01, SB-05, SB-09, SB-19 | ODS-04 · TT-007, TT-008 |
| **ACT-2** | Banc d'elements i conductors | Catàleg de mitjans de transmissió, classificació de conductors i fitxa de cada tipus de fixació amb l'element que subjecta | `1b`, `1c`, `1e`, `1f` | SB-02, SB-03, SB-04, SB-06, SB-12, SB-28 | TT-006 |
| **ACT-3** | Muntatge del «rack» i mecanització de canalitzacions | Taller pràctic amb fases: preparació i mecanització de canalitzacions, muntatge d'armari seguint el plànol, fixació mecànica i tancament amb revisió de seguretat. Prendre mesures de longituds i recorreguts és **pràctica `[PROPOSTA]` de material complementari**, no contingut curricular (§3.9.2, `P-24`) | `2a`–`2h` | SB-04, SB-07, SB-09, SB-13, SB-17, SB-18, SB-19, SB-20, SB-21, SB-33, SB-39 | TT-001, TT-003 |
| **ACT-4** | Tesa, etiquetatge i preses de la xarxa | Desplegament dels conductors amb les tècniques de tendido literals, tall i etiquetatge, muntatge dels armaris de comunicacions i connexió de preses | `3a`–`3g` | SB-02, SB-04, SB-10, SB-11, SB-12, SB-19, SB-22, SB-23, SB-24, SB-25, SB-29, SB-39 | ODS-08 · TT-006 |
| **ACT-5** | Muntatge i fixació d'antenes, amplificadors i accessoris | Assemblatge, col·locació, fixació (en armari i en superfície) i connexió d'un sistema de transmissió, amb revisió de seguretat. Correspon a l'orientació `OP v7`, **co-origin de `SB-3016-26`** (§3.9.3, P-25) | `4a`–`4f`, `4h` (**`4g` queda fora**, §3.8) | SB-03, SB-06, SB-07, SB-11, SB-13, SB-17, SB-18, SB-20, SB-24, SB-26, SB-27, SB-28, SB-29, SB-30, SB-33, SB-39 | ODS-08 · TT-004 |
| **ACT-6** | Configuració bàsica i representació del mapa física | Descripció de la xarxa local, identificació d'elements amb funció, interpretació i **representació del mapa físico** amb una eina informàtica triada per l'alumne. **Executa la configuració bàsica** de `SB-3016-40` (`CB b5.i6`): es pot ensenyar i valorar amb instrument `[PROPOSTA]`, però **cap criteri oficial de RA 5 l'avalui** (§3.9.1, `P-23`) | `5a`–`5g` | SB-02, SB-03, SB-08, SB-09, SB-12, SB-30, SB-31 · **SB-40 (sense criteri)** | TT-004, TT-007 |
| **ACT-7** | Instruccions de treball segurs | Elaboració i aplicació d'una instrucció de treball: riscos i perillositat de cada operació, causes d'accident, proteccions de màquina, EPI i mesures de prevenció | `6a`–`6e` | SB-13, SB-14, SB-15, SB-16, SB-32, SB-33, SB-34, SB-36, SB-37, SB-39 | TT-001 · ODS-12 (amb l'esclareixement de §4.2) |
| **ACT-8** | Ordre, neteja i retirada selectiva | Ordre i neteja de la instal·lació acabada, valoració de l'ordre i la neteja com a factor de prevenció, i classificació dels residus per a la retirada selectiva | `6f`, `6g`, `6h` | SB-32, SB-33, SB-34, SB-35, SB-39 | TT-002 · ODS-12 |
| **ACT-9** | Projecte integrador: instal·lació completa d'una xarxa local en un «pequeño entorno» | Projecta, munta, connecta, configura, documenta i posa en servei una instal·lació completa, amb rols rotatius i rúbrica compartida. A més del criteri, **avalua `SB-3016-40`** (`CB b5.i6`, §3.9.1) i pot introduir la mesura de longituds i recorreguts com a pràctica `[PROPOSTA]`, **material complementari que no resol `P-24`** (§3.9.2) | tots els criteris **excepte `4g`** · i **`SB-40` sense criteri** | tots els **40** sabers | ODS-04, ODS-08, ODS-10 · TT-005, TT-007, TT-009 |

**Comprovació:** cap criteri queda sense activitat. `4g` queda explícitament fora i
sense cobertura curricular. `SB-3016-40` queda **fora de la columna de criteris**
perquè **cap criteri oficial el cobreix**, i això s'ha fet constar a la taula en
lloc de distribuir-lo per un criteri que no li escau (§3.9.1, `P-23`).

**Del que depèn del centre (P-9):** cap font acredita quins equips, eines o espais
hi ha a l'aula, i la viabilitat d'`ACT-3` a `ACT-6` i `ACT-9` en depèn.

---

## Annex C · Bloc literal del mòdul `3016` (F-037, Annex VII, apartat 3.3)

**[TEXT EXTRET]** · text oficial · perquè qualsevol fila de la graella es pugui
traçar fins al document sense dependre d'un altre fitxer. Es conserven els espais
especials del document oficial: espai fi `U+2003` entre numeració i text, guion fi
`U+2012` de les vinyetes i espai fi fi `U+2002` després de la vinyeta.

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

**Procedència i reserva.** Font a citar: **F-037** (consolidat vigent, actualització
publicada el 28/05/2024). Origen de la transcripció: **F-027** («TEXTO ORIGINAL» de
2014), amb el registre acreditant que el bloc `3016` és **idèntic caràcter per
caràcter** en les dues versions (109 línies, `diff` sense diferències) i que **el
mòdul no ha canviat** amb el RD 498/2024 (F-038). La comparació prové del registre
de fonts; **no** d'una reverificació feta en aquesta fase (P-13, P-20).

---

*Fase 3 · `generador-graelles` · branca `issue/3-graella-3016` · 2026-10-01 ·
revisió posterior a la validació independent del 2026-10-01 ·
6 RA · 44 criteris (43 amb cobertura curricular, `4g` `PENDENT`) ·
**40 sabers** (18 / 14 / 8; 38 a la taula i 2 que no sostenen cap criteri) ·
9 activitats · 332 h (F-032) · 43 assignacions d'instruments (34 formulacions,
10 famílies) · 25 codis de pendent (P-1…P-25; `P-25` resolt) ·
4 relacions ODS i 10 relacions TT, totes `PROPOSTA` ·
0 relacions `VERIFICADA` al mòdul. Document **en revisió, no validat**: cal
llegir i revalidar `sortides/informes-validacio/informe-validacio-3016.md`.*