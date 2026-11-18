# Research log

Dated entries, newest first: prompt, what was done, key results, what failed.

## 2026-11-18. proveedores: archive, validator and coverage tables

Prompt. Materials for one DRIL use case (supplier development initiatives, ECLAC): the team's notes, Stage 1 instrument V260714, Stage 2 protocol V260721, the variable dictionary, the Stage 1 entity file and the compiled Stage 2 results and evidence. "How would you proceed?" The user confirmed these are all the materials, approved publishing them (reviewers' names removed), and does not know which model ran the agent.

Done. Created `projects/proveedores` (D-004): protocols and source files committed with hashes (D-007), a machine-readable Stage 2 instrument (D-005), derived tables with codes in place of labels (D-008). Built the first shared components: `dril/instrument.py`, `dril/validate.py` (generalising the protocol's section 15 checklist; synthetic tests plant one error of each kind), `dril/countries.py` (D-011). Built coverage, status and source tables (D-009, D-010), reference-value checks for every number quoted in the project README, `run_all.py`, `scripts/check_outputs.py` and CI that rebuilds outputs from source (D-012).

Results. The delivered data pass every check of the protocol's checklist. The Stage 1 file counts 1,102 entities, not 1,208; earlier figures counted rows (D-006, correction). Funnel: 1,102 entities, 235 with a candidate, 341 candidates, 265 initiatives in 31 countries; 76 candidates lost in review, with no record of why (OQ-08). 40.8 percent of cells are not found; budget is missing for 76.2 percent of initiatives and evaluation for 84.9 percent. Gaps are larger for subnational entities (44.8 vs 37.6 percent) and, against expectation, larger in South America than in the Caribbean. 73.9 percent of evidence rows come from government sites; multilateral sources carry 28.7 percent of evidence in the Caribbean against 4.9 percent in South America. Diagnostics flag 150 edition cells that may need `proxy_used` (OQ-06) and 512 quotes of three words or fewer (OQ-07).

Failed. A first version of the synthetic dependency test planted an inconsistent status and so expected one finding where the validator correctly found two; the test was fixed, not the validator.

## 2026-11-18. Repository set-up

Prompt. Create a general DRIL repository to hold replications and updates of past work, with several projects inside it that apply the method. Improve or extend the method where possible. Inputs: Afonso et al. (2026), NBER WP 35188, and the presentation "DRIL: Deep Research on a Loop. Agentes de IA para construir datos de políticas" (Wander and Carrillo, CEPAL, 30 September 2026). Project-specific references to follow.

Done. Read both documents in full. Prepared the repository skeleton (README, registers, literature register, project folder). Ran two web searches for follow-up work on the paper.

Results. The searches found no published critique, replication or extension of the paper as of this date, only announcements (NBER, RePEc, Marginal Revolution, news summaries). An adjacent paper, Shin (2026, arXiv 2603.17381), proposes an auditable agent loop for specification search in empirical economics with a post-search holdout; it concerns estimation rather than data construction. The presentation documents four ECLAC applications that are candidate projects: the GTED update (from the paper), technological extension programmes (33 countries, 502 initiatives), supplier development initiatives (1,208 public entities, 265 initiatives characterised, 6,242 evidence records) and evaluations of STI policy (337 evaluations).

Failed. Creating the GitHub repository from the workspace was refused (HTTP 403: the session can only reach repositories attached to it). The user has been asked to create an empty public repository wanderdata/DRIL.
