# AGENTS.md

## Propòsit

Preparar graelles curriculars traçables per a professorat. Escriu en valencià
clar, llevat que la persona demane un altre idioma.

La llengua de totes les respostes visibles, títols, informes i missatges d’estat
és el valencià clar. No contestes en anglés ni en castellà. Mantín literals els
textos normatius originals quan calga citar-los, però explica el resultat en
valencià.

## Fonts

- Usa `fonts/registre-fonts.md`.
- No presentes normativa, competències o criteris com a verificats sense font,
  apartat i data de consulta.
- Diferencia text extret, resum, interpretació i proposta.
- Marca `PENDENT` qualsevol dada no comprovada.

## Portes del flux

- El planificador acaba amb `ESPERANT APROVACIÓ DEL PLA`.
- El supervisor només continua amb `PLAN APPROVED`.
- El verificador no repara silenciosament els defectes.
- `github-manager` prepara el Pull Request, però el merge espera `PR APPROVED`.
- Només `READY FOR HUMAN REVIEW` permet la revisió docent final.
- El recorregut complet està definit en `.opencode/skills/issue-workflow/SKILL.md`.
- `planificador`, `verificador-context`, `gestor-fonts` i la resta de papers de
    `.opencode/agents/` són agents, no skills. No intentes carregar-los amb el
    mecanisme de skills; delega’ls com a agents quan el flux ho necessite.
- Les fonts no tenen un mòdul fix. Usa `fonts/registre-fonts.md` per a les
    referències oficials i les fonts d’entrada que consten en l’estat de la
    tasca actual. Els noms `extraccion-<id>.md`, `relacions-<id>-sabers.md`,
    `graella-<id>.md` i `graella-docent-<id>.md` són una convenció, no rutes
    obligatòries ni informació que es puga reutilitzar d’una execució anterior.
- `sortides/esborranys/estat-flux.md` és memòria de treball, no una font
    curricular. Abans de reutilitzar-la, compara etapa, assignatura o mòdul,
    curs, territori, finalitat i restriccions amb la petició actual. Si no
    coincideixen, inicia un context nou i no heretes fonts, recomptes, hores,
    codis ni decisions de l’execució anterior.
- Quan uses `glob`, `read` o una eina equivalent, consulta cada ruta en una
    crida separada. No ajuntes diversos fitxers amb comes dins d’un únic patró.

## Seguretat i eixides

No guardes dades personals, secrets, tokens, cookies ni fitxers `.env`.
Guarda graelles en `sortides/graelles/`, esborranys en `sortides/esborranys/`
i informes en `sortides/informes-validacio/`.

## Format de la graella docent

La font completa de traçabilitat i la taula docent són eixides diferents. No
substituïsques la font ni la convertisques en un informe llarg quan es demane la
taula visual.

La primera taula docent ha de presentar, per cada resultat d’aprenentatge, els seus
criteris d’avaluació agrupats i les columnes següents:

| Resultat d’aprenentatge | Criteris d’avaluació | Continguts | Bloc de continguts | Saber | Saber fer | Saber estar |
|---|---|---|---|---|---|

Agrupa les files del mateix resultat d’aprenentatge, mantín els criteris
separats i relaciona cada criteri amb els continguts que realment li
corresponen. Per a cada criteri, pensa si hi ha un saber, un saber fer i un
saber estar justificables; si no n’hi ha o no es pot comprovar, escriu
`PENDENT` i explica el motiu en la font completa. Conserva el text i l’estat
(`VERIFICADA`, `PROPOSTA` o `PENDENT`).
La vista docent ha de ser compacta i llegible, semblant a una taula de
traçabilitat curricular. Els ODS i els temes transversals es poden integrar en
els sabers, el saber fer i el saber estar com a propostes pedagògiques
etiquetades (`[PROPOSTA ODS-xx]` o `[PROPOSTA TT-xxx]`), sempre amb una
justificació. No els presentes com a exigències del Reial decret ni com a
`VERIFICADA` si la font no els assigna explícitament al mòdul. Les activitats
competencials i els instruments són una fase posterior i opcional; no han
d’ocupar ni substituir la primera taula. Les fonts, justificacions,
incidències i reserves detallades es conserven en la font completa i en
l’informe.
