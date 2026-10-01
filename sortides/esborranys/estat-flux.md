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
