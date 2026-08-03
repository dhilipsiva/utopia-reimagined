# Repository Guidelines

## Authority, Scope & Structure

`CLAUDE.md` is the authoritative record of settled design and editorial decisions; follow it if this guide conflicts. Before active work, read `CLAUDE.md`, `TODO.md`, and `tmp.txt` (draft context, never book content). This is a verified book-design repository, not an application. `book-1/` contains active numbered chapters such as `01-what-counts-as-evidence.md` and their matching `.pins.nibli` files. Apart from its labelled opening note, Part V, and method, book-1 prose must derive from `new-book-plans/constitution.nibli`; keep it jargon-free and exclude roadmaps, MVS, scaling, and technology implementation. Those belong to book 2; do not develop book 2 while book 1 is active. Do not remove legacy `book.md` or `manifesto.md` before the TODO's legacy harvest is complete.

`new-book-plans/` owns the constitution, generated `3-spine.md`, and counterfactual fixtures. `registry/` contains claims, snapshots, checks, and Python fetchers. Keep `book-1/epigraph.md` and `method.md` unnumbered.

## Validation & Development Commands

Run from the repository root:

```bash
./verify.sh --quick   # iteration only; skips pins and counterfactuals
./verify.sh           # authoritative suite; required before every commit
python3 new-book-plans/5-spine-gen.py new-book-plans/constitution.nibli new-book-plans/3-spine.md --check
python3 registry/check.py
```

Use release `nibli-pin --kb`, never `nibli-host`. Omit `--check` only to regenerate the spine. After every constitution edit, including comments, regenerate counterfactual fixtures and run the full verifier. Never hand-edit generated spine blocks.

## Editing, Testing & Naming

Match existing Markdown hierarchy and `NN-kebab-case.md` / `.pins.nibli` pairs. Write pin controls as `:accept-scoped`; use plain `:accept` only when an accepted statement is a later query's premise. In book-1, state the rule that produces a count rather than a counted design claim. Add a primary source and URL for every empirical statistic or named study in the same commit. Python uses four-space indentation and new code needs `SPDX-License-Identifier: MIT OR Apache-2.0`.

## Commits, Pull Requests & Licensing

Make one chapter or section change per content commit. Use descriptive `<area>: <outcome>` subjects, explain *why* in a ~72-column body, then make a separate `Tracker: <what landed> (<content SHA>)` TODO commit. Pull requests should summarize the claim or mechanism, report validation, identify regenerated artifacts, and link the tracker item; include screenshots only for rendered visual changes.

Read `LICENSING.md` before adding files. New prose is CC-BY-4.0, code is MIT OR Apache-2.0, registry claims are CC0, and data snapshots can carry upstream terms. Legacy pre-decision material remains CC0 under the root `LICENSE`.
