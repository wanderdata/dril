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
