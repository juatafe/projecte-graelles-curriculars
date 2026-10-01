# Estat de l’execució

status: EN_CURS
context: FP | Informàtica i Comunicacions | grau bàsic | Informàtica d'oficina (T.P.B.) | 2n curs | 3016 Instal·lació i manteniment de xarxes per a transmissió de dades | Comunitat Valenciana
fase: unificació del registre de fonts ( gestor-fonts)
pla: sortides/esborranys (pla del planificador, PLAN APPROVED 2026-10-01)
fonts_reutilitzades: [F-001, F-014, F-026, F-027, F-032, F-033, F-034, F-035, F-036]
milestone: 1 · Graella 3016 · Informàtica d'oficina (2n curs) · xarxes per a transmissió de dades
issues: [#1 pre-verificació, #2 gestor-fonts, #3 graella 3016]
branches: [milestone/graella-3016-informatica-oficina, issue/1-preverificacio-registre-fonts, issue/2-gestor-fonts-f027-ods, issue/3-graella-3016]
pull_requests: [#4 obert, #5 obert apilat sobre #4]
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
proxim_pas: supervisar la neteja final; si és correcta, marcar status COMPLET, i si no, deixar EN_CURS o BLOQUEJAT amb el que falta
intents: 2
actualitzat: 2026-10-01
