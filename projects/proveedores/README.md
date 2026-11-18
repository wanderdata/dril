# Supplier development initiatives in Latin America and the Caribbean

This project archives, checks and documents an application of DRIL by ECLAC: a map of public initiatives that build supplier relationships between anchor firms (large buyers) and small and medium-sized suppliers in 33 countries of Latin America and the Caribbean (CEPAL, 2026c). The agent was run in July 2026. This folder holds the frozen protocols, the data as delivered, a machine-readable version of the instrument, and descriptive tables of coverage, gaps and sources. It does not yet contain a verification of the evidence or a second run; those are the next steps (see the last section).

## Design of the original application

The application had two stages. In Stage 1 (protocol V260714, `protocol/260714_Instrumento_DRIL_-_Etapa_1.md`) the units were public entities: national ministries and agencies, sectoral bodies, first-level subnational governments and the main second-level governments by contribution to GDP. For each entity the agent searched for eligible initiatives under an operational definition with six inclusion and six exclusion criteria, a minimum set of search families, a rule against stopping after the first finding, and a saturation rule. The design favoured sensitivity: doubtful cases were included and left to human review. After review, each retained initiative became a unit of Stage 2 (protocol V260721, `protocol/260721_Protocolo_DRIL_Etapa_2_caracterizacion.md`), in which the agent coded 43 variables in seven blocks (identification, beneficiaries and objectives, coverage and timing, budget and regulation, services, subsidies and co-financing, evaluation). Each variable has a companion status column with seven values, and every substantive answer must be backed by an evidence row with URL, access date, locator and a verbatim quote. Before freezing the protocol, the team tested versions on Argentina, the Dominican Republic and Trinidad and Tobago, watching for signs of truncated search: similar run times across very different countries, similar numbers of programmes per country, and almost no entity with more than one programme. Brazil and Mexico were split into two runs each. The team's notes on this process are in `protocol/apuntes_experiencia_aplicacion_DRIL.md`.

## Coverage

Table 1 gives the funnel from entities searched to initiatives characterised. The Stage 1 file has 1,208 rows but 1,102 distinct entities; rows repeat once per candidate initiative for the 235 entities that had at least one candidate (D-006). Earlier presentations of this work reported 1,208 entities (327 national, 881 subnational) and 341 entities with at least one initiative; those figures count rows, and the corrected figures are below.

Table 1. Entities searched, candidates and initiatives characterised

| | National entities | Subnational entities | Total |
|---|---:|---:|---:|
| Entities searched | 251 | 851 | 1,102 |
| Stage 1 candidate initiatives | 187 | 154 | 341 |
| Initiatives characterised in Stage 2 | 148 | 117 | 265 |
| Initiatives per 100 entities searched | 59.0 | 13.7 | 24.0 |

Source: `output/funnel_total.csv`, `output/funnel_by_level.csv`.

Of the 341 candidates, 76 did not reach Stage 2, and 45 entities with at least one candidate ended with none characterised. The record of the human review that made these decisions is not available, so the reasons cannot be reconstructed. The losses are concentrated: in Paraguay 8 of 31 candidates were characterised, and in Argentina 12 candidates were dropped; Guatemala (6 candidates) and Honduras (5) have none in Stage 2, which is why Stage 2 covers 31 countries rather than 33. Counts by country are in `output/funnel_by_country.csv`.

The unit of Stage 2 is the initiative as delivered by Stage 1, and territorial editions of one programme are separate units when they were found through different subnational governments. 107 initiatives name a parent programme, among 78 distinct parents; the largest family is the Colombian Proyecto Apoyo a Alianzas Productivas, which nine initiatives name as their parent and which is itself a separate initiative. Counts of initiatives are therefore not counts of distinct programmes.

## Gaps

Of the 11,395 coded cells (265 initiatives by 43 variables), 30.4 percent are answered directly from a source, 17.8 percent inferred from evidence, and 40.8 percent recorded as not found after search. Gaps are concentrated in budget, regulation, subsidies and evaluation: no budget was found for 76.2 percent of initiatives, no evidence on whether a subsidy is given for 67.5 percent, no operating rules for 52.8 percent and no evaluation for 84.9 percent. The current status of the initiative (`vigencia`) was not found for 22.3 percent. The full table is `output/status_by_variable.csv`.

The share of cells not found is higher for initiatives of subnational entities (44.8 percent) than of national entities (37.6 percent), and higher in South America (43.4 percent) than in Central America (38.3) or the Caribbean (36.8). The subregional ordering runs against the expectation, stated in the team's notes, that Caribbean programmes are less documented online. The comparison is across initiatives that were found, so it says nothing about programmes that were never identified, and it mixes differences in documentation with differences in the kinds of initiatives found in each subregion.

The classification variables rest mostly on the agent's reading rather than on literal statements: 77.4 percent of `tipo_programa`, 81.1 percent of `nivel_programa` and 78.5 percent of `mecanismo_vinculacion` cells are marked inferred. These are the variables whose coding a verification should check first.

## Sources

Evidence rows cite 475 distinct URLs on 261 domains. We classified domains by type, using the government pattern of the domain name and, for the 110 domains that do not match it, a manual table based on knowledge of the institutions that has not been checked against the sites (`data/manual/source_domains.csv`; 12 domains, carrying 3.4 percent of evidence rows, are left as uncertain). By that classification, 73.9 percent of evidence rows come from government or public-agency sites and 14.0 percent from multilateral or cooperation agencies; the press accounts for 1.7 percent. Reliance on multilateral sources differs by subregion: 28.7 percent of evidence rows in the Caribbean, 18.2 percent in Central America and 4.9 percent in South America (`output/source_types.csv`).

## Checks

The end-of-run checklist of protocol V260721 (section 15) was implemented as a general validator (`dril/validate.py`) that reads the instrument in `instrument/stage2_V260721.yaml`. On the delivered data it finds no errors: identifiers are unique, no cell is empty, special codes agree with their status, all values lie in their domains, the eight dependency rules hold, and every substantive cell has at least one evidence row meeting the citation contract (`output/validation_summary.csv`). These checks establish internal consistency. They do not establish that a quote appears in its source or that it supports the coded value.

Two diagnostics beyond the checklist point to where verification should look (`output/diagnostics.csv`; D-010). First, 731 substantive cells rest only on quotes that are also cited for other initiatives. For initiatives coded as editions of a parent programme, 338 such cells exist; 188 are marked `proxy_used`, as the protocol requires for information taken from the parent, and 150 are marked answered, inferred or partial. If those quotes describe the parent rather than the edition, the status understates reliance on parent-level information. Second, 512 evidence rows have quotes of three words or fewer (for example "matching grants"), which meet the citation contract formally but can rarely support a coded value on their own. A quarter of evidence rows have no source date.

## Limitations

The protocol required a search log (`Busquedas`), but its output specification listed only the characterisation and evidence sheets, and no search log was produced. A cell marked "not found after search" therefore cannot be distinguished from one where the search was not carried out. The Stage 1 candidate-level output, the human review record, the pilot-run records and the construction of the entity list are not available. The model and host used to run the agent are not recorded, which matters for choosing an independent verifier. As the team's notes say, the map covers what is published online: launches are better documented than closures, and the number of initiatives found in a country reflects how visible its programmes are online as well as how many exist. The database is not a census.

## Files

| Path | Content |
|---|---|
| `protocol/` | Stage 1 instrument V260714, Stage 2 protocol V260721, and the team's notes (reviewers' names removed) |
| `instrument/stage2_V260721.yaml` | Machine-readable Stage 2 instrument, generated by `scripts/00_instrument.py` from the variable dictionary |
| `data/source/` | Files as delivered, with hashes (see its README) |
| `data/derived/` | `entities.csv` (one row per entity), `entities_stage1_rows.csv`, `records.csv` (Stage 2, categorical labels converted to codes), `evidence.csv` |
| `data/manual/source_domains.csv` | Source-type classification of domains |
| `scripts/` | `01_build.py`, `02_validate.py`, `03_coverage.py`; run all with `python run_all.py` from the repository root |
| `output/` | Validation results and the tables cited above |

## Next steps

Verification of a stratified random sample of initiatives: whether each quote appears in the cited source (programmatically, from archived copies of the pages), and whether it supports the coded value (a reviewer blind to the value, using a different model from the original run, with a hand-coded subsample to measure the reviewer's own error). A second, independent Stage 1 run on a sample of entities, including those reviewed externally in Chile and Colombia, to estimate how many initiatives a single run misses. Each will have a pre-analysis plan committed before results are computed.

## Reference

CEPAL (2026c). Aplicación de DRIL al mapeo de iniciativas de desarrollo estratégico de proveedores en América Latina y el Caribe: protocolo, instrumentos y bases de resultados (versión V260721). Santiago: Comisión Económica para América Latina y el Caribe. Documento de trabajo.
