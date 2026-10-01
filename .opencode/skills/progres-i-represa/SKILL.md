---
name: progres-i-represa
description: Controla la memòria, la represa i la convergència del flux multiagent.
---

# Progrés, memòria i represa

## Memòria abans de començar

1. Llig `dades/estat-catalogs.md`, `fonts/registre-fonts.md` i les eixides
   existents abans de consultar cap font externa.
2. Si hi ha una execució o pla anterior amb la mateixa etapa, cicle, curs i
   mòdul, anuncia que existeix i reutilitza el context, les fonts i els fitxers.
3. Només pregunta si es vol reprendre, revisar o començar de nou quan hi haja
   més d’una execució compatible o una contradicció.
4. Una font `VERIFICADA` no es torna a buscar sense una raó registrada.

## Polsera de progrés

Abans i després de cada delegació, escriu una línia amb aquest format:

`PROGRÉS | fase=<fase> | agent=<agent> | acció=<acció> | font=<font o fitxer> | intent=<n>/<m> | pròxim=<acció següent> | límit=<condició d’aturada>`

Cada agent ha d’indicar també el resultat: `DONE`, `CONTEXT READY`,
`CONTEXT INCOMPLETE`, `SOURCE NOT FOUND`, `PASS` o `FAIL`.

## Convergència

- Una delegació té una finalitat, una font o fitxer objectiu i una condició de
  finalització explícita.
- No es repeteix la mateixa delegació amb el mateix context més de dues vegades.
- El gestor de fonts consulta com a màxim tres fonts oficials per bloqueig.
- Si no hi ha progrés després de dos intents, s’atura amb el bloqueig, les
  fonts consultades i el pròxim pas concret.
- No es continua amb una dada `PENDENT` ni es transforma en `VERIFICADA` per
  omissió.
