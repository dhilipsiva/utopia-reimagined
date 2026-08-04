# Repository Guidelines

## Authority, Scope & Structure

`CLAUDE.md` is authoritative; follow it if this guide conflicts. Before work, read `CLAUDE.md`, `TODO.md`, and `tmp.txt` (draft context, never book content). `book-1/` contains numbered chapter/`.pins.nibli` pairs. Except for its labelled opening note, Part V, and method, prose must derive from `new-book-plans/constitution.nibli`; keep it jargon-free and move roadmaps, MVS, scaling, and technology implementation to book 2. Do not develop book 2 while book 1 is active or remove legacy `book.md`/`manifesto.md` before the TODO harvest.

`new-book-plans/` owns the constitution, generated spine/audits, reviewed JSON contracts, bounded record-snapshot red-team, and counterfactuals. `registry/` holds claims, snapshots, checks, and fetchers. Keep `book-1/epigraph.md` and `method.md` unnumbered.

## Validation & Development Commands

Run from the repository root:

```bash
./verify.sh --quick   # iteration; skips pins, executable snapshots, counterfactuals
./verify.sh           # authoritative suite; required before every commit
python3 new-book-plans/5-spine-gen.py new-book-plans/constitution.nibli new-book-plans/3-spine.md --check
python3 new-book-plans/7-assertion-surface.py --check
python3 new-book-plans/8-record-integrity-assurance.py --check
python3 new-book-plans/9-record-integrity-red-team.py --check
python3 new-book-plans/9-record-integrity-red-team.py --check --execute
python3 registry/check.py
```

Use release `nibli-pin --kb`, never `nibli-host`. Omit `--check` only to regenerate. Edit JSON contracts, never generated reports or spine blocks. After a rule/fact change, use `7-assertion-surface.py --fingerprints`, review contracts, then copy candidate digests. Dependency order is 7 → 8 → 9: an assertion-contract change requires assurance review and new 8/9 digests; an assurance-source change requires a new 9 digest. Evidence roles may not relabel a gap as assurance. After every constitution edit, including comments, regenerate counterfactuals and run the full verifier.

## Editing, Testing & Naming

Match Markdown hierarchy and `NN-kebab-case.md`/`.pins.nibli` pairs. Write controls as `:accept-scoped`; use `:accept` only when the accepted statement is a later premise. State the rule producing a count, not a counted design claim. Add a primary source and URL with every statistic or named study. Python uses four spaces; new code needs `SPDX-License-Identifier: MIT OR Apache-2.0`.

## Commits, Pull Requests & Licensing

Make one chapter or section change per content commit. Use `<area>: <outcome>` subjects and explain why in a ~72-column body. Close TODOs separately with `Tracker: <what landed> (<content SHA>)`. Pull requests summarize the claim, validation, regenerated artifacts, and tracker item; screenshots are only for rendered visual changes.

Read `LICENSING.md` before adding files. New prose is CC-BY-4.0, code is MIT OR Apache-2.0, registry claims are CC0, and data snapshots can carry upstream terms. Legacy pre-decision material remains CC0 under the root `LICENSE`.
