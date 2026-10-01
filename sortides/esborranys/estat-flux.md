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
obstacle_2: la pila de branques i PRs parteix de 36195a8 i no inclou 7cac142 ni 0490031 de main; cal resoldre abans del merge final
obstacle_3: PENDENT — els canvis de dades s'han portat a issue/3-graella-3016, però les modificacions locals de .opencode/ i els commits 7cac142 i 0490031 de main continuen sense commitejar en aquesta branca
ultima_accio: gestor-fonts unifica el registre de fonts (F-001…F-036, I-1…I-6) i actualitza dades/moduls-fp.md, dades/estat-catalogs.md, dades/referencies-cicles.md i fonts/normativa/gva/fp/README.md a la branca issue/3-graella-3016
proxim_pas: reprendre fase-1-fonts-i-extraccio amb la codificació unificada; cap dada curricular nova no està PENDENT per al mòdul 3016
intents: 0
actualitzat: 2026-10-01
