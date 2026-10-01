# Sortides

- `esborranys/`: materials en revisió.
- `graelles/`: taules amb informe favorable.
- `informes-validacio/`: evidència de comprovacions i pendents.

Una graella només passa a `graelles/` amb un informe `READY FOR HUMAN REVIEW`.

## Estat de represa

Quan hi haja una execució en curs, conserva en `sortides/esborranys/estat-flux.md`
l’estat de la fase, el context, el pla, les fonts reutilitzades, els intents i
el pròxim pas. En una represa, el supervisor ha de llegir aquest estat abans de repetir preguntes o consultes.


## Finalització

L’estat només pot passar a `COMPLET` quan `main` conté el merge final, les
issues i la milestone estan tancades, els Pull Requests han quedat integrats i
les branques temporals s’han eliminat. Si queda qualsevol element obert, la
sessió es conserva com `EN_CURS` o `BLOQUEJAT` i el fitxer ha d’indicar el
pròxim pas.
