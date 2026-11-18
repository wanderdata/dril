# Decision log

Every framing, scope, data, definitional or implementation choice, numbered D-nnn. Entries are never deleted; superseded entries are marked as such, with a pointer to the entry that replaces them.

## D-001 (2026-11-18). One repository, shared core plus projects

The repository holds shared components in `dril/` and one folder per application in `projects/<name>/`. Reason: the four building blocks of DRIL (instrument, unit space, evidence policy, data-quality mechanisms) and the verification stage are common to all applications; writing them once keeps records comparable across projects and lets each project be audited with the same tools. The shared components will be written after the first projects specify their requirements, not before.

## D-002 (2026-11-18). Public repository

The repository is public, at the user's instruction.

## D-003 (2026-11-18). Copyrighted source documents are not committed

Papers and reports read for the project (for example NBER WP 35188) are listed in `references/literature_register.csv` with their URL, but the files themselves are not committed. ECLAC internal presentations and working documents are not committed unless the user says they can be published.
