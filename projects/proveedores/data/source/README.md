# Source files

Files as received from the user on 2026-11-18. They are the compiled outputs of the ECLAC application of DRIL to supplier development initiatives (Stage 1 protocol V260714, Stage 2 protocol V260721). The cell contents are unmodified. In two files the author fields of the document metadata (`dc:creator`, `cp:lastModifiedBy` in `docProps/core.xml`) were blanked before committing, because they held a personal name and an internal account name (D-007). `scripts/01_build.py` checks the committed hashes before building the derived tables.

| File | Content | SHA-256 as received | SHA-256 committed |
|---|---|---|---|
| `entidades_con_resultados_V260714.xlsx` | Stage 1 result by entity: 1,208 rows, 6 columns (entity identifiers and `existe_programa_proveeduria`). Rows repeat for entities with more than one candidate; see D-006. | `ca63ba772f133e17e6c2c2a9771fc8e5734969706065ac9d810523ab9ce8e2cf` | `e2c7fa8996143f34ea443aa68e45970fdc45d05729deee521565808bf98353a9` |
| `resultados_etapa2_compilados_V260721.xlsx` | Stage 2 characterisation: 265 initiatives, 43 variables, each with a status column. Categorical variables are stored as labels, not codes. | `21bce8eeef7a2447617650d40ee32a04d014903c2981c55b1a2bc8cbf42e3c67` | same |
| `evidencias_etapa2_compiladas_V260721.xlsx` | Stage 2 evidence: 6,242 rows, one per initiative, variable and source. | `03c7bdd839586348a521ad7c89a87657ac022789881fc70ff300140f0f55b4a1` | same |
| `diccionario_variables_dril_etapa2_V260721.xlsx` | Variable dictionary generated from the Stage 2 instrument: codes, labels and coding rules. | `249343afc39eea4b3b22b8374bb4055faa6dfd7fb5583589eab27924709142c5` | `3323dff20682ae06f5d070018cb62e69ae3be5e95a01d62fb72eeb8767916d94` |

Not available (the user has confirmed these are all the materials for this application): the Stage 1 candidate-level output (`nombre_candidato`, `razon_inclusion`, evidence, `notas_busqueda`), the record of the human review between stages, search logs, the pilot-run spreadsheet, the construction of the entity list, and the model and host used to run the agent.
