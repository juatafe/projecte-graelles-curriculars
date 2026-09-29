# Projecte de graelles curriculars verificables

Sistema multiagent per preparar graelles curriculars a partir de fonts oficials,
relacionant criteris, sabers, ODS i temes transversals.

## Què fa

1. Rep una petició sobre un mòdul o una assignatura.
2. Prepara un pla i espera l’aprovació.
3. Extrau informació de fonts registrades.
4. Relaciona criteris, sabers, ODS i temes transversals.
5. Genera una graella i un informe de fonts.
6. La verifica amb un agent independent.
7. La deixa preparada per a revisió humana.

## Estructura

- `AGENTS.md`: regles generals del projecte.
- `fonts/`: registre, portals oficials i procediment de verificació.
- `.opencode/agents/gestor-fonts.md`: localitza i registra fonts abans de l’extracció.
- `.opencode/skills/issue-workflow/SKILL.md`: defineix issues, branques, PR i merge.
- `dades/`: catàlegs i plantilles de treball.
- `sortides/`: esborranys, graelles i informes.
- `.opencode/agents/`: papers especialitzats.
- `.opencode/skills/`: procediments reutilitzables.

## Primera petició

Obri OpenCode en aquesta carpeta i demana al `supervisor` que prepare un pla
per al mòdul o assignatura que vulgues treballar. El supervisor ha d’esperar
`PLAN APPROVED` abans de crear o editar fitxers.

## Estat del projecte

La configuració inicial és una base didàctica. Les fonts, els criteris i les
relacions curriculars s’han d’omplir i revisar per a cada ensenyament.
