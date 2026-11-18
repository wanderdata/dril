# Open questions

Unresolved issues, numbered OQ-nn. Closed questions stay in the file with the date and the decision or result that closed them.

## OQ-01 (2026-11-18). How to validate agent-coded data against a benchmark

Afonso et al. (2026) did not run their verification stage and did not compare the GTED update with the published GTED. Each project should state in its protocol how accuracy will be measured: units with a known answer (an earlier hand-coded release, a survey, external reviewers), agreement by field and source type, and the share of cited quotes that appear in the cited source. Open until the first project protocol is written.

## OQ-02 (2026-11-18). Independence of the verification agent

A verifier using the same model as the coder may share its errors and defer to it (Mehdizadeh and Hilbert, 2025, cited in the CEPAL presentation). Options: programmatic check that each quote appears in the archived source; a different model, blind to the coded value; a human-coded random sample. Which combination is feasible and sufficient is open.

## OQ-03 (2026-11-18). Run-to-run stability

Neither the paper nor the ECLAC applications report whether independent runs of the same protocol on the same unit give the same values. Repeated runs on a subsample would measure this.

## OQ-04 (2026-11-18). Measurement error in downstream analysis

Agent-coded variables may have non-classical error (better-documented countries coded better), missingness related to outcomes, and errors correlated across units because one model and instrument are used for all. A hand-coded validation sample used to correct estimates (Ludwig, Mullainathan and Rambachan, 2026) is the candidate approach.

## OQ-05 (2026-11-18). Archiving cited sources

Web sources change. Whether to store a copy of each cited page with its SHA-256 hash, a Wayback Machine link, or both, and where (copyright limits what can be committed to a public repository).

## OQ-06 (2026-11-18). proveedores: edition cells supported only by shared quotes

150 substantive cells of initiatives coded as editions of a parent programme rest only on quotes also cited for other initiatives, and are marked answered, inferred or partial rather than `proxy_used` (188 such cells are marked `proxy_used`). If the quotes describe the parent, the protocol (section 13) requires `proxy_used`. To be settled by the verification sample.

## OQ-07 (2026-11-18). proveedores: very short quotes

512 evidence rows have quotes of three words or fewer. Whether these support the coded values, or whether the citation contract should set a minimum, is open.

## OQ-08 (2026-11-18). proveedores: candidates lost between stages

76 of 341 Stage 1 candidates did not reach Stage 2, and 45 entities with a candidate ended with none (all candidates in Guatemala and Honduras; 23 of 31 in Paraguay). The human review record is not available. Whether these were exclusions under the definition, merges of duplicates or omissions cannot be determined from the files.

## OQ-09 (2026-11-18). proveedores: counting unit

Territorial editions found through different subnational entities are separate initiatives (107 initiatives name a parent, among 78 distinct parents), although the Stage 1 instrument (section 8.1) asks that editions be recorded under the parent's name. Any count of "programmes" should state whether editions are grouped.

## OQ-10 (2026-11-18). proveedores: interpretive classification variables

77.4 percent of `tipo_programa`, 81.1 percent of `nivel_programa` and 78.5 percent of `mecanismo_vinculacion` cells are marked inferred. Their reliability is unknown and should be measured against a hand-coded sample.

## OQ-11 (2026-11-18). proveedores: no search logs

The protocol required a `Busquedas` sheet but its output specification omitted it, and no search log exists. "Not found after search" cannot be audited. Future runs need the log in the output specification.

## OQ-12 (2026-11-18). proveedores: model and host unknown

The model and host of the original run are not recorded. A verifier from a different model family cannot be guaranteed independent of the original coder. Future protocols should record model, version and host in each record (as `agent_version` records the protocol).
