# AGENTS.md

## Propòsit

Preparar graelles curriculars traçables per a professorat. Escriu en valencià
clar, llevat que la persona demane un altre idioma.

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
- Només `READY FOR HUMAN REVIEW` permet la revisió docent final.

## Seguretat i eixides

No guardes dades personals, secrets, tokens, cookies ni fitxers `.env`.
Guarda graelles en `sortides/graelles/`, esborranys en `sortides/esborranys/`
i informes en `sortides/informes-validacio/`.
