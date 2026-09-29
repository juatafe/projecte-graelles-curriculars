---
name: issue-workflow
description: Coordina el projecte mitjançant pla aprovat, milestone, issues, branques, validació, Pull Request i merge autoritzat.
metadata:
  audience: curricular-agents
  workflow: github
---

# Flux d’issues del projecte

Usa aquesta skill quan una petició curricular s’ha de convertir en una
milestone i issues o quan cal preparar, validar, revisar o fusionar una issue.

## Entrada i portes

1. Llig `AGENTS.md`, la petició, les skills pertinents i el context del projecte.
2. `planificador` prepara objectiu, abast, fora d’abast, fonts, fitxers, passos,
   criteris, riscos i agents responsables.
3. El supervisor mostra el pla i espera exactament `PLAN APPROVED`.
4. No es creen issues ni branques abans d’aquesta aprovació.

## Branques

- `main`: branca final.
- `milestone/<slug>`: branca d’integració de la milestone.
- `issue/<numero>-<slug>`: branca exclusiva de cada issue.

Cada issue es treballa en la seua branca i es presenta amb un Pull Request cap
a la branca de la milestone. Quan totes les issues estan integrades, es prepara
un Pull Request final de `milestone/<slug>` cap a `main`.

## Seqüència del projecte

1. `planificador` prepara el pla.
2. El supervisor espera `PLAN APPROVED`.
3. `github-manager` comprova l’estat de GitHub i crea la milestone, la branca
   d’integració, les issues i la branca de l’issue activa.
4. `gestor-fonts` registra les fonts oficials necessàries.
5. `extractor-normativa`, `integrador-sabers` i `generador-graelles` preparen
   els materials i les sortides de l’issue.
6. `verificador` comprova fonts, criteris, coherència i traçabilitat.
7. Si falla, el supervisor retorna la issue a l’agent responsable i repeteix la
   verificació.
8. Quan el resultat està preparat, `github-manager` fa el commit, el push i
   obri el Pull Request cap a la branca de la milestone.
9. El supervisor mostra l’estat i espera exactament `PR APPROVED`.
10. Després de `PR APPROVED`, `github-manager` comprova els checks, fa el merge,
    verifica el tancament de la issue i elimina la branca ja integrada.
11. En acabar totes les issues, es repeteix el procediment per al Pull Request
    de la milestone cap a `main`.

## Eixides i límits

- Graelles favorables: `sortides/graelles/`.
- Esborranys: `sortides/esborranys/`.
- Informes: `sortides/informes-validacio/`.
- No faces push directe a `main` ni forces l’historial.
- No tanques una issue sense el Pull Request autoritzat i integrat.
- No uses secrets ni dades reals de l’alumnat.
- Si falta una dada curricular imprescindible, pregunta-la; no inventes fonts ni
  normativa.
