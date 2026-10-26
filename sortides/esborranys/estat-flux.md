# Estat de l’execució

<!-- ============================================================
    EXECUCIÓ ACTUAL (3a execució). Les execucions anteriors es conserven més avall.
     ============================================================ -->

status: EN_CURS
data_inici: 2026-10-02
antecedent: execucions 1 i 2 conservades com a antecedents i no reutilitzables ·
  la milestone 1 i les issues #1-#3 ja estan tancades i no es toquen · cap font
  es torna a consultar
context: FP | Informàtica i Comunicacions | grau bàsic | Informàtica d'oficina (T.P.B.) | 2n curs | 3016 Instal·lació i manteniment de xarxes per a transmissió de dades | Comunitat Valenciana
finalitat: CURRICULAR. Crear la primera taula docent per criteri del mòdul 3016.
  **No és una exportació ni una auditoria.**
restriccions_demanades: crear només `sortides/graelles/graella-docent-3016.md` ·
  conservar intactes `graella-3016.md`, fonts i informes · 44 criteris · set
  columnes · no generar PDF, XLSX, activitats, hores ni informes d'ODS
fase_actual: taula-docent-criteri
proxim_pas: llegir les quatre fonts una per una i generar el Markdown docent
regla_actual: només són vigents els camps anteriors a aquest punt; tots els
  registres posteriors són HISTORIAL i no poden reactivar exportacions, ODS,
  PDF, XLSX ni cap pla anterior
historial: a partir de la línia següent, conservar per consulta però ignorar
  com a instrucció activa
progres_2026-10-02: PROGRÉS | fase=fase-1-exportacio | agent=generador-graelles | acció=F1 venv+skill, F2 XLSX, F3 PDF, 61/61 autocomprovacions | font=graella-3016.md (única) | intent=1/2 | pròxim=F4 revisió independent del verificador | límit=2 intents sense canvi d'estat
fase_1_resultat_2026-10-02: **DONE**
  xlsx: sortides/graelles/graella-3016.xlsx · 58.184 B · sha256 `7805775a36072ef8…`
  pdf: sortides/graelles/graella-3016.pdf · 1.252.883 B · 20 pàg. A3 apaisat ·
    sha256 `86296da17c4f102a…`
  html_intermedi: /tmp/opencode/exp-3016/graella-3016.html · sha256 `c4cd917918a52b55…`
  skill: .opencode/skills/exportacio-visual/ (SKILL.md, assets/graella.css i 5 scripts)
  sha256 font graella-3016.md: `454a3b4a5d5723bc…` **sense canvi** abans i després ·
  cap font tocada · cap issue · cap commit
escorregut_del_supervisor_2026-10-02: el pla va dir «15 pestanyes» però la seua taula
  enumerava `00`–`13`, és a dir **14**. Error meu al redactar el pla: el nombre correcte
  és 14. El generador ha construït les 14 enumerades i **no n'ha inventat una
  quinzeena**, que és el que tocava. El llibre ho declara a la pestanya 00.
limitats_declarades_2026-10-02:
  - `U+2002` i `U+2003` **es perden al PDF**: Chrome converteix tots els separadors
    Unicode a `U+0020`, en el dibuix i en la capa de text. Comprovat amb un HTML
    mínim independent; no és problema de la CSS ni de la font. La resta (`U+2012` 40,
    `U+2013` 45, `U+2014` 105, `U+2423` 2, `«»` 174) sí que hi és, i **l'XLSX els
    conserva tots byte a byte**. Per a citació forense cal l'XLSX. Més sever que la
    limitació R1 que anuncià el pla, que només parlava de `pdftotext`.
  - El PDF **no és byte-reproduïble**: Chrome hi posa `CreationDate`/`ModDate` i ignora
    `SOURCE_DATE_EPOCH`. Els àncors reproductibles són el sha256 del Markdown, el de
    l'HTML intermedi i l'ordre de comandes.
  - §4.1 té **5** advertiments, no 4 (altra imprecisió del pla). Els 5 s'exporten.
  - 4 files sense marca curricular (§6.5 ítems 2, 8 i 9 i la taula de famílies
    d'instruments de §6.4) **no s'han emplenat**: tenen classe `advertiment`/`proposta`.
progres_2026-10-02: PROGRÉS | fase=fase-2-revalidacio | agent=verificador | acció=F4 revisió independent de l'exportació | font=graella-3016.md (única), xlsx, pdf | intent=1/2 | pròxim=F5 correccions d'exportació a generador-graelles | límit=2 intents sense canvi d'estat
fase_2_validacio_2026-10-02: **NOT READY** — 5 defectes confirmats, tots a l'exportació
  informe: sortides/informes-validacio/informe-validacio-exportacio-3016.md (191 línies)
  F1 §5.2 no s'exporta i l'omissió no es declara (pestanya `10`, salta de §5.1 a §5.3;
     5 blocs, 926 caràcters)
  F2 procedència falsa: `12!B4` concatena Annex C + «Procedència i reserva» + peu del
     document; el 78 % del valor no és del bloc oficial
  F3 els **2** `U+2423` no són al llibre (sí que hi són al PDF); §7.2/§7.3 no s'exporten
     però la llegenda hi remet
  F4 declaració falsa dins el llibre: `00!B34` diu que `U+2012` «NO es recupera» i
     es recupera 40/40
  F5 el bloc oficial de 109 línies queda en una columna de 14 caràcters (`12!B` amplada
     14; el codi genèric pren el valor de reserva)
  el que passa net: integritat dels 3 hascos · 14 pestanyes exactes · xifres
    recalculades des del llibre 58/58 (44 criteris, 332 h, 40 sabers 34/1/5, 25 codis
    P- en 24 files, 4 ODS + 10 TT PROPOSTA, 13 ODS PENDENT, 0 VERIFICADA) · hash
    Annex C `92a65b0f…` per tres vies independents · **control negatiu 3/3 detectat**
    (297/1 → 294/4, sense falsos positius) · PDF A3 apaisat confirmat, 0 paraules fora
    de pàgina, capçaleres repetides
correccions_del_verificador_al_generador_2026-10-02:
  - `U+2002`/`U+2003` **sí que es perden, però només a la capa de text**: en
    rasteritzar a 72 dpi renderitzen a 22 i 42 px davant 13 px d'un espai normal
    (1 em = 40 px). El PDF els **dibuixa** bé; es perden en copiar/enganxar i en
    `pdftotext`. El generador ho havia declarat massa ample.
  - `U+2012` **no es perd gens** (40/40). La llegenda ho afirma contrariament.
  - `comparar_export.py` passa 61/61 però el mateix script declara que «la cobertura de
    regions es calcula a la taula de traçabilitat» i **no la comprova**. F1 i F2 cauen
    exactament en aquesta acotació: l'exportador i el comparador comparteixen el mateix
    model de regions, i cap dels dos el detecta.
reserva_metodologica_2026-10-02: el verificador declara que el seu model **no accepta
  entrada visual**, de manera que la Capa B l'ha feta per geometria i extracció de text
  (caixes delimitadores, amplades de renderització, amplada de columna, conversió amb
  LibreOffice) i **no mirant les pàgines amb els ulls**. La revisió docent humana del
  PDF i de l'XLSX **continua pendent** i no se substitueix per aquesta geometria.
progres_2026-10-02: PROGRÉS | fase=fase-2-revalidacio | agent=generador-graelles (F5) + supervisor | acció=correcció F1-F5 i verificació directa del supervisor | font=graella-3016.md (intacta) | intent=2/2 | pròxim=F5b corregir F4, després F4 de nou | límit=2 intents sense canvi d'estat
verificacio_directa_del_supervisor_2026-10-02: **el informe del generador era inexacte
  en el hash i incomplet en el resultat.** El `sha256` que va reportar de l'XLSX
  (`7805775a…`) era **obsolet**: el hash real és `d462d23c84b8e70faf6fbd7d835e24e44
  bff6af7d72c9bf18eac0f438999fb27` (56.505 B, 58.184 → 56.505 B). El fitxer **sí** que
  s'havia reconstruït. Comprovat per mi mateix amb `openpyxl`:
  - pestanyes: **14**, ordre correcte, cap contingut inventat ✓
  - **F1 CORREGIT**: §5.2 hi és sencer a la pestanya `10` (hi apareix l'advertiment
    aritmètic i `P-18`)
  - **F2 CORREGIT**: el bloc oficial s'ha separat de la procedència; `12!B7` té 8.830
    caràcters i `sha256 92a65b0f8e6f4d505be189595d6351dac5cf5cc44c9853036f7d8679596e1a7f`
  - **F3 CORREGIT en el fons**: hi ha 4 `U+2423`, tots metatext legítim de §0.5
    (`00!B97`) i §7.2/§7.3 (`13!B9`, `13!B22`, `13!B23`), amb el caràcter visible ␣ on
    toca. No n'hi ha cap d'inventat. El criteri «exactament 2» valia per al Markdown,
    on el metatext apareix una sola vegada
  - **F5 CORREGIT**: amplada de la columna B de la pestanya 12 = 180 (abans 14)
  - comparador: **C8 cobertura de regions** i **C9 puresa de cel·les** afegits ✓
  - **F4 PENCORREGIT**: `00!B34` continua dient que `U+2012` «NO es recupera», cosa
    que el verificador ha refutat per rasterització (40/40). I encara hi posa
    `U+2003`/`U+2002` al mateix sac, quan el PDF els **dibuixa** bé (22 i 42 px davant
    13 px d'un espai normal) i només es perden a la **capa de text**. L'agent va
    reportar «declaracions de llegenda no alterades» com si fos una bonesa: era
    exactament el defecte
  - font `graella-3016.md`: `454a3b4a…` **intacta** ✓ · `git status` només mostra els
    fitxers nous i `estat-flux.md`; cap font tocada ✓
proxima_delegacio: generador-graelles — **F5b**, només F4: reescriure `00!B34` amb la
  declaració verificada i reportar el hash **real** del XLSX
proxim_pas: F5b, després F4 de nou amb el verificador. Límit de intents consumit: si
  F4 no queda corregida i verificada, es para amb bloqueig concret i es reporta.
verificador_context_2026-10-02: **CONTEXT READY** — etapa FP grau bàsic, família
  Informàtica y Comunicaciones, nivell grau bàsic, cicle Informática de oficina, 2n
  curs i mòdul 3016 confirmats contra `dades/moduls-fp.md` i F-032 (Anexo III-A,
  pàg. 34/58, 10 h/sem · 332 h/any). Cap PENDENT bloqueja l'exportació: I-6 és de
  registre, I-7 no afecta les hores perquè preval F-032, F-024 està substituïda.
  No s'ha consultat cap font nova.
planificador_2026-10-02: **DONE** — pla redactat i mostrat. Cap fitxer nou creat.
  Eixides: XLSX de 15 pestanyes (6 de RA + 9 de suport), PDF visual, skill
  reutilitzable `.opencode/skills/exportacio-visual/` amb exportador i comparador,
  i informe de validació independent. Decisions: XLSX amb `venv` + `openpyxl` 3.1.5
  (editable, sense protecció, caràcters especials conservats); PDF amb `pandoc` →
  HTML5 `--embed-resources` → `google-chrome --headless --print-to-pdf` (única via
  verificada; A3 apaisat amb `thead` repetit).
  Línies vermelles: cap fitxer nou fins a `PLAN APPROVED` · cap issue · fonts,
  informes i graella només en lectura · cap contingut curricular nou · cap valor per
  defecte en l'exportador (s'atura amb error si una fila no té marca reconeixible).
deure_fase_0: `PLAN APPROVED` literal. Després: F1 venv+skill → F2 XLSX → F3 PDF →
  F4 revisió independent del `verificador` → F5 correccions d'exportació si cal.
discrepancies_detectades_2026-10-02:
  - `pandoc` instal·lat és **3.1.3**, no 3.5.2 (el 3.5.2 era la versió del mòdul
    Python `markdown`, mal atribuïda en la meua ordre al planificador). Es deixa
    escrita la versió exacta a l'informe.
  - `python3 -m pip` del sistema està bloquejat per **PEP 668** → cal `venv` fora del
    repositori, mai versionat.
  - D-2: a §7.1 hi ha **23 codis `PENDENT`**, 1 `PROPOSTA` (`P-7`) i 1 `RESOLT`
    (`P-25`); els 22 que jo havia anunciat són files, no codis. L'exportació copia
    els estats **tal com estan escrits**; no es corregeix la graella.
  - D-3: l'informe de validació declara com a objecte una versió de 714 línies i el
    fitxer actual en té 1.005. La procedència es declara; **no** s'afirma cap
    revalidació nova.
  - R1 assumit: `pdftotext` no conserva les files de taula ni els codioms en blanc, de
    manera que la garantia caràcter a caràcter viu a l'XLSX i a l'HTML intermedi; el
    PDF es valida per contingut normalitzat. Es declara, no s'omet.
pregunta_governanca_2026-10-02: el planificador demana si pot actualizar
  `sortides/esborranys/estat-flux.md` per registrar fase, `PROGRÉS` i portes. La
  skill `progres-i-represa` ho exigeix. **Sense resposta, es queda en lectura.**
eixides_previstes:
  - sortides/graelles/graella-3016.xlsx (nou, pestanya per RA1-RA6 + pestanyes de
    suport; **contingut transcrit** de graella-3016.md, cap redactat nou)
  - sortides/graelles/graella-3016.pdf (nou, versió visual de la graella)
  - .opencode/skills/exportacio-visual/SKILL.md (skill reutilitzable, si cal)
font_operativa: sortides/graelles/graella-3016.md (única font de les dades) +
  sortides/informes-validacio/informe-validacio-3016.md (veredicte
  `READY FOR HUMAN REVIEW` del 2026-10-01) + sortides/esborranys/estat-flux.md
  (execució 1, com a antecedent)
fonts: cap consulta nova. F-032, F-035 i F-037 es reutilitzen de `VERIFICADA`.
  Cap relació ODS/TT puja d'estat: segueixen sent 4 + 10 `PROPOSTA` i 0 `VERIFICADA`
  al mòdul. I-7 continua `PENDENT`.
estat_pendents: els 25 codis P-1…P-25 de la graella es traslladen **sense canviar**
  d'estat: 22 `PENDENT` + els que la graella declara literals/reserva
capacitat_tecnica_verificada: python3 3.12.3 · `venv` + `openpyxl 3.1.5` instal·lat
  correctament en aquesta màquina (xlsx editable) · `pandoc 3.5.2` + `google-chrome`
  headless `--print-to-pdf` verificats (pdf visual). `pip3` del sistema està
  bloquejat per PEP 668 → cal `venv`. No hi ha `reportlab`, `weasyprint` ni `openpyxl`
  al sistema.
portes: cap oberta. No hi ha cap delegació d'execució fins a `PLAN APPROVED`.
progres_2026-10-02: PROGRÉS | fase=fase-0-planificacio | agent=supervisor | acció=memòria, lectura de la graella, informe i eines; comprovació de l'eina | font=estat-flux.md, estat-catalogs.md, registre-fonts.md, graella-3016.md | intent=1/2 | pròxim=verificador-context | límit=2 intents sense canvi d'estat
intents: 1
actualitzat: 2026-10-02

---

# Antecedent · execució 1 (COMPLET, 2026-10-01) — no reutilitzar

status: COMPLET
context: FP | Informàtica i Comunicacions | grau bàsic | Informàtica d'oficina (T.P.B.) | 2n curs | 3016 Instal·lació i manteniment de xarxes per a transmissió de dades | Comunitat Valenciana
fase: COMPLETADA — execució tancada amb repositori net el 2026-10-01
pla: sortides/esborranys (pla del planificador, PLAN APPROVED 2026-10-01) · autorització de merge: PR APPROVED de la persona usuària el 2026-10-01
fonts_reutilitzades: [F-001, F-014, F-026, F-027, F-032, F-033, F-034, F-035, F-036]
fonts_noves: [F-037 · RD 356/2014 versió consolidada vigent · /con · actualització 28/05/2024, F-038 · RD 498/2024 · BOE-A-2024-10683]
milestone: 1 · Graella 3016 · Informàtica d'oficina (2n curs) · xarxes per a transmissió de dades · TANCADA el 2026-10-01
issues: [#1 tancada, #2 tancada, #3 tancada]
branches: [eliminades — milestone/graella-3016-informatica-oficina, issue/1-preverificacio-registre-fonts, issue/2-gestor-fonts-f027-ods, issue/3-graella-3016, infra/memoria-i-neteja; només queda main]
pull_requests: [#4 MERGED, #5 MERGED, #6 MERGED, #7 MERGED, #8 MERGED (milestone cap a main)]
decisio_infraestructura: es reutilitza la milestone 1 i les issues #1-#3 existents; no es creen duplicats (autoritzat per la persona usuària)
fases_rastrejades: [fase-1-fonts-i-extraccio, fase-2-integracio-sabers, fase-3-graella-i-informe, fase-4-validacio]
decisio_codificacio_2026-10-01: es conserva el registre remot de origin/issue/3-graella-3016 com a base; F-032 queda reservada al Decret 117/2025 (PDF oficial DOGV, Anexo III-A, normativa) i la fitxa curricular del cicle a CEICE rep el codi nou F-036 (font de consulta); cap codi existent s'ha reutilitzat
incidencia_I-5: resolta per verificació directa al PDF oficial del DOGV — la remissió a l'annex III-A és l'art. 3.8 (pàg. 4/58), no l'art. 8.8 que deia el registre remot; SHA-256 idèntic a les còpies del 29 i del 30-09-2026
incidencia_I-6: PENDENT de decisió de la persona usuària — F-034 i F-036 tenen la mateixa URL (pàgina del segundo curso); es conserven separades i cap dada curricular depèn de la fusió, perquè preval F-032
obstacle_1: RESOLT — el conflicte de codis s'ha unificat (F-032 decret, F-036 fitxa CEICE) i s'ha registrat a fonts/registre-fonts.md
obstacle_2: RESOLT 2026-10-01 per github-manager — merge de main (7cac142, 0490031) cap a milestone/graella-3016-informatica-oficina (0923068) i propagació a issue/1 (febff9a), issue/2 (f2c849a) i issue/3 (d19031f); cap reescriptura d'historial; PR #4 i PR #5 segueixen MERGEABLE/CLEAN
obstacle_3: RESOLT 2026-10-01 per github-manager — el contingut de governança de .opencode/ s'ha commitejat en la branca d'infraestructura infra/memoria-i-neteja (ed0f644, PR cap a main obert i sense fusionar); no s'ha barrejat amb el material curricular de la milestone
ultima_accio: github-manager resol obstacle_2 (merge de main a la pila de branques) i obstacle_3 (governança de .opencode/ a infra/memoria-i-neteja amb PR obert a main); deixa l'arbre de treball net i no fusiona cap PR
comprovacio_repositori_2026-10-01: main=0490031 · milestone/graella-3016-informatica-oficina=36195a8 · issue/1=d515955 (PR #4 CLEAN) · issue/2=4dc666c (PR #5 CLEAN) · issue/3=b4731ff local, 1 commit per pujar, sense PR · arbre de treball amb 4 fitxers .opencode/ modificats i .opencode/skills/progres-i-represa/ sense versionar · issues #1, #2 i #3 i milestone 1 obertes
diagnostic_obstacle_2: CONFIRMAT — milestone i issue/1 i issue/2 parteixen de 36195a8 i no contenen 7cac142 ni 0490031 de main; es resol amb merge de main (no rebase, per no reescriure l'historial ja publicat)
diagnostic_obstacle_3: CONFIRMAT — el contingut nou no commitejat és de governança del projecte (cicle de vida i neteja de github-manager, passos 10-13 i «Condició de repositori net» d'issue-workflow, regla de reutilització de fonts VERIFICADES en gestor-fonts, memòria del supervisor). No és material curricular i no ha d'infectar el PR de la milestone: es preservarà en una branca d'infraestructura pròpia, sense merge a main fins a PR APPROVED
progres_2026-10-01: PROGRÉS | fase=represa | agent=supervisor | acció=verificar estat real del repositori i de GitHub | font=estat-flux.md, estat-catalogs.md, registre-fonts.md | intent=1/2 | pròxim=github-manager resol obstacle_2 i obstacle_3 | límit=2 intents sense canvi d'estat
proxima_delegacio: cap fins que la persona usuàra done PR APPROVED als PR #4, #5 i al PR d'infraestructura; després continua el supervisor amb fase-1-fonts-i-extraccio
proxim_pas: reprendre fase-1-fonts-i-extraccio amb la codificació unificada; el PR de issue/3-graella-3016 encara no s'obre perquè falten les fases 2, 3 i 4; cap dada curricular nova no està PENDENT per al mòdul 3016
intents: 1
actualitzat: 2026-10-01
progres_2026-10-01: RESULTAT | agent=github-manager | obstacle_2=RESOLT (milestone=0923068, issue/1=febff9a, issue/2=f2c849a, issue/3=d19031f) | obstacle_3=RESOLT (infra/memoria-i-neteja=ed0f644, PR obert cap a main, sense merge) | PR #4 i #5 MERGEABLE/CLEAN sobre la milestone | PR de issue/3 NO obert (fases 2-4 pendents) | arbre de treball net
verificacio_supervisor_2026-10-01: CONFIRMAT Independentment — b4731ff és ancestre de issue/3 · totes les branques amb behind=0 respecte de main · PR #4, #5 i #6 CLEAN i cap fusionat
fase_1_extraccio: DONE — sortides/esborranys/extraccion-3016.md (635 línies) · 6 RA, 44 criteris d'avaluació, 6 blocs de continguts bàsics amb 29 ítems, text literal de F-027
fase_1_incidencies: I-8 RESOLTA (el text consolidat vigent és F-037; el bloc 3016 és idèntic caràcter per caràcter; el mòdul 3016 NO ha canviat amb el RD 498/2024) · I-7 PENDENT (el RD 356/2014 no defineix el camp Duración; aritmètica inconsistent: 1.100 h dels 9 mòduls davant de les 2.000 h de l'apartat 1; no afecta la graella perquè preval F-032)
fonts_noves: F-037 (RD 356/2014 versió consolidada vigent, /con, actualització 28/05/2024) · F-038 (RD 498/2024, BOE-A-2024-10683) — cap codi reutilitzat, F-032 i F-036 no reassignats
correccion_traçabilitat: la graella s'ha de traçar a F-037 (consolidat vigent), NO a F-027 (TEXTO ORIGINAL de 2014); el text és el mateix però la font a citar és la vigent
advertiment_DA_sisena: les orientacions pedagògiques de 3016 diuen «competencias profesionales, personales y sociales» i s'han de llegir com a «competencias profesionales y para la empleabilidad» (F-038, disposició addicional sisena)
progres_2026-10-01: PROGRÉS | fase=fase-1-fonts-i-extraccio | agent=extractor-normativa+gestor-fonts | acció=extracció literal i tancament I-7/I-8 | font=F-027,F-032,F-035,F-037,F-038 | intent=1/2 | pròxim=fase-2-integracio-sabers | límit=3 fonts per bloqueig (assolit 3/3)
proxima_delegacio: integrador-sabers — relacionar criteris amb sabers (saber, saber fer, saber estar), ODS i temes transversals amb justificació
proxim_pas: fase-2 integració de sabers; la vinculació d'ODS al mòdul 3016 no té font (cap relació acreditada) i s'ha de tractar com a PROPOSTA pedagògica o deixar PENDENT
fase_2_integracio_sabers: DONE — sortides/esborranys/relacions-3016-sabers.md (818 línies) · 40 sabers finals (18 saber / 14 saber fer / 8 saber estar) · 44 criteris coberts (24 amb origen literal, 19 amb reserva, 1 sense cobertura: 4g) · 14 relacions ODS/TT totes PROPOSTA
fase_2_correccions_D1: CB b5.i6 rep itinerari via SB-3016-40 (saber fer, RA 5, sense criteri perquè cap 5a-5g cobreix «configurar» textualment) · OP v8 PENDENT (P-24, sense itinerari possible) · OP v7 co-origin redundant de SB-3016-26 ·nous P-23, P-24, P-25
fase_3_graella: DONE — sortides/graelles/graella-3016.md (~970 línies) · 6 RA + 44 criteris en text literal · 332 h repartides coherent amb F-032 · sortides/informes-validacio/informe-fonts-3016.md
fase_4_validacio: PRIMERA VALIDACIÓ — 0 bloquejants, 9 defectes no bloquejants (D-1 alta, D-2 mitjana, D-3 a D-9 baixes); feina retornada a integrador-sabers i generador-graelles
fase_4_revalidacio: READY FOR HUMAN REVIEW — D-1 PARCIAL (correcte: CB b5.i6 amb itinerari, OP v8 PENDENT, OP v7 redundant), D-4 PARCIAL i D-5 PARCIAL (reserves documentals), D-2 a D-3 i D-6 a D-9 CORRECTES · 0 defectesnous de regressió · 44/44 criteris i 6/6 RA literalment correctes, hores 332, 14/14 ODS/TT en PROPOSTA, 4g PENDENT
reserves_tancades: D-4 els 2 caràcters U+2423 són el nom del caràcter dins del metatext de correcció, no un residu: declarats intencionats a §0.5 · D-5 SB-3016-06 passa a [TEXT EXTRET (parcial)] amb reserva; recomptes ajustats a 34 [TEXT EXTRET] + 1 parcial + 5 [RESUM]
progres_2026-10-01: PROGRÉS | fase=fase-4-validacio | agent=verificador x2 + generador-graelles | acció=revalidacio independent i tancament de reserves | font=F-037,F-032,F-035,F-038 | intent=2/2 | pròxim=github-manager commit+PR de issue/3 | límit=2 intents sense canvi d'estat (assolit: canvi d'estat correctiu)
PORTES_OBERTES: cap — PR APPROVED rebut de la persona usuària el 2026-10-01 després de la revisió docent; autoritza el tancament complet
pr_7: https://github.com/juatafe/projecte-graelles-curriculars/pull/7 · issue/3-graella-3016 → milestone/graella-3016-informatica-oficina · OPEN i CLEAN · commits 442f466 (fonts F-037/F-038 i I-7/I-8), 0ba0aa9 (extracció fase 1), fe81220 (integració fase 2), 203b97d (graella i informe fase 3), 3af4e68 (validació fase 4 i estat del flux) · Refs #3, sense tancament automàtic
pull_requests: [#4 obert i CLEAN, #5 obert i CLEAN, #6 obert i CLEAN cap a main (infraestructura), #7 obert i CLEAN (graella 3016)]
autoritzacio_merge: PR APPROVED de la persona usuària (2026-10-01) — cobreix tota la cadena de merge fins a la neteja final
proxima_delegacio: github-manager — merge de #4, #5 i #7 a la milestone, PR de milestone cap a main, merge, tancament d'issues i milestone i eliminació de branques temporals; després verificació de repositori net
proxim_pas: cap — execució completada; per a una execució nova cal iniciar un context nou i conservar aquesta com a antecedent
neteja_final_2026-10-01: COMPROVADA pel supervisor de manera independent — 0 PR oberts, 0 issues obertes, 0 milestones obertes, només la branca main (local i origin/main) sincronitzada, arbre de treball net, els sis fitxers de la graella presents a origin/main amb contingut real
commits_a_main: 1e6c6fe (merge PR #6, governança) · 138ce92 (merge PR #8, milestone a main) · fa2ea82 (merge PR #7, graella) · 6a0f598 (merge PR #5) · c6a3003 (merge PR #4) · a6a5d30 (autorització PR APPROVED) · 442f466, 0ba0aa9, fe81220, 203b97d, 3af4e68 (fases 1 a 4)
resultat_curricular: 6 RA i 44 criteris en text literal de F-037 · 40 sabers (18 saber / 14 saber fer / 8 saber estar) · 332 h segons F-032 (10 h/setmana) · 14 relacions ODS/TT totes PROPOSTA, cap VERIFICADA al mòdul · veredicte READY FOR HUMAN REVIEW sense defectes bloquejants
pendents_assumits_que_no_s_inventen: P-1 i P-2 (cap vinculació acreditada d'ODS ni de tema transversal al mòdul) · P-3 criteri 4g sense contingut bàsic · P-23 CB b5.i6 exigible pel RA 5 sense criteri que l'avalua · P-24 OP v8 sense itinerari possible · I-7 el RD 356/2014 no defineix el camp Duración i no substitueix l'horari curricular
nota_incidencies: I-8 RESOLTA (el mòdul 3016 no ha canviat amb el RD 498/2024; F-037 és el text vigent) · I-6 continua PENDENT per decisió de la persona usuària sobre la fusió de F-034 i F-036; no afecta cap dada curricular perquè preval F-032
antecedent_per_a_execucions_noveles: no reutilitzar la milestone 1 ni les issues #1-#3; ja estan tancades
intents: 2
actualitzat: 2026-10-01
