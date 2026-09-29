# Fonts del projecte

Aquest directori conserva el catàleg de fonts que poden justificar afirmacions
curriculars o normatives. El fitxer `registre-fonts.md` és l’índex de treball i
les subcarpetes contenen fitxes detallades amb els enllaços oficials.

## Estructura

- `bibliografia/`: obres de consulta que no substituïxen la normativa.
- `normativa/estatal/`: legislació estatal.
- `normativa/gva/eso/`: Educació Secundària Obligatòria.
- `normativa/gva/batxillerat/`: Batxillerat.
- `normativa/gva/fp/`: Formació Professional.
- `normativa/gva/inclusio/`: inclusió educativa.
- `normativa/gva/inici-curs/2026-2027/`: instruccions d’inici de curs.

## Procediment

1. `gestor-fonts` consulta primer el registre i les fitxes del catàleg.
2. Obri l’enllaç oficial i comprova el document, l’apartat i la vigència.
3. Actualitza `registre-fonts.md` amb organisme, títol, URL, apartat, etapa,
   data de consulta i estat.
4. `extractor-normativa` només extreu dades de fonts registrades.
5. El verificador comprova que cada afirmació conserva la seua font i ubicació.

Una pàgina inicial d’un portal no substituïx el document normatiu concret. Una
font `PENDENT` no pot justificar una afirmació definitiva. Les fitxes copiades
del catàleg inicial són una base de treball: la vigència i l’aplicació concreta
s’han de revisar abans de cada proposta.

Estats permesos: `VERIFICADA`, `PENDENT`, `NO APLICABLE`.
