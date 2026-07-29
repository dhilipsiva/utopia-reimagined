# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A book-writing project heading for **two new books**, with the original two manuscripts slated for deletion:

- **book-1** — the active work. Two parts to its scope, and the seam is deliberate:
  - **Parts I–V — the destination.** *What an ideal society must be and how it functions* — **never how to get there.** No roadmap, no transition, no MVS, no scaling story. Spine is *derived*: chapter order is computed from the dependency stratification of a formal constitution in nibli KR (`new-book-plans/utopia-v2.nibli`), and content is **gated on that constitution** — if the KR does not derive it, it does not go in. **Jargon-free**: a general reader can finish Part V and stop, and the formalism is never mentioned here. Exactly three elements are exempt from the derivation gate and each is labelled as such in the text: a short non-derived **opening note**, **Part V** (argument and evidence), and the final method part. What they verify is the **data**.
  - **Final part — the method, explicitly optional.** Shows the machinery to whoever wants it: the constitution, the derived spine, the compile-time firewall, the evidence/conclusion split, and what the logic *refused*. Clearly labelled as a different kind of reading. This is the only place in book-1 where the formalism appears, and its existence is what answers the "you built a machine and hid it" objection.
- **book-2** — **how you would actually build it, organisationally and technically.** The transition material (MVS, the family→village→planet scaling story, legal collisions, costed transition) *and* the technology stack. Not planned yet; it gets its own tracker after book-1 ships. book-1 references it exactly once, at the very end.
- **`book.md` and `manifesto.md`** — legacy. To be deleted once both new books exist, but **not before** the legacy-harvest section of `TODO.md` is complete: `book.md`'s 55 sourced references, the nine historical cases, the Bharati poem, and the five bright lines all need porting first.

So this is no longer only Markdown editing: there is a constitution to verify against the real engine, and a data pipeline to build. See `TODO.md`.

The repo is deliberately **mixed-licence** — see `LICENSING.md` before adding files. In short: new prose is CC-BY-4.0, code is MIT OR Apache-2.0, the data registry is CC0, and everything committed before that decision (including `book.md` and `manifesto.md`) remains irrevocably CC0 under the root `LICENSE`.

## Files

- `book.md` — the entire book in a single Markdown file (~2970 lines).
- `manifesto.md` — a companion manifesto, structurally independent of the book.
- `tmp.txt` — the author's scratch notes/instructions for the section currently being drafted. Read it for context on what's in progress; don't treat it as book content.
- `TODO.md` — the **book-1** work tracker (plain bullets, ordered by dependency and leverage; work the first remaining bullet, delete it when it fully lands, update it if only partially done). Check it before starting any work. Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory, or a design decision — skip them in unattended work and take the highest-value non-gated bullet instead. It also holds the legacy-harvest manifest and a parked list for book-2; don't work book-2 items there.
- `new-book-plans/` — planning material for book-1, plus the constitution `utopia-v2.nibli`. `3-spine.md`'s stratification table and chapter order are **generated** — don't edit the block by hand and don't transcribe its counts elsewhere; it went stale twice that way. Check it with `python3 new-book-plans/5-spine-gen.py new-book-plans/utopia-v2.nibli new-book-plans/3-spine.md --check` (exit 0 = current), and regenerate by dropping `--check`. Verify constitution claims with the release `nibli-pin --kb`, never `nibli-host` — its wasm predates the `derived_only` and `entitled` corpus entries and silently drops the entire rights floor and all nine gate closures while still answering queries.
- `verify.sh` — **the one check.** `./verify.sh` (~15 min) runs the spine check, the evidence-vocabulary guard, the jargon sweep, the five absence claims with a positive control, the pin suite with a cross-file `:expect-pins` reconciliation, and the three counterfactual fixtures; `--quick` skips the pin suite and takes about two seconds. It exits non-zero on the first failure and names the claim that stopped being true. Run it before every commit and prefer it to any check by hand — each check here was negative-controlled, and the jargon sweep as previously specified did not catch the leak it was written for.
- `new-book-plans/counterfactual/` — three copies of the constitution, each missing exactly one line, each with pins asserting what the world looks like without it. They exist because derivation is monotone and probe facts load *on top*, so no probe can test a restriction; these are the only way an "if we removed X" claim is executed rather than argued. **Regenerate after every constitution edit** — see the README beside them.
- `LICENSING.md` — the mixed-licence map. Read before adding files.

## book.md Structure

Six parts, each opened by a `{class: part}` attribute line (Leanpub/Markua syntax — preserve these markers exactly). Chapters are `#` headings, sections `##`, subsections `###`:

1. **The Need for Change** — the problem: physical abundance vs. financial scarcity
2. **Defining the Core** — fundamental human rights, employment redefined, merit points, and the technology chapters (The Technological Backbone, Proof of Personhood, Quantum-Secure & Privacy-Centric, Making It Simple)
3. **Implementing Fundamental Rights** — food/water/education, healthcare, shelter/mobility/communication, environmental stewardship
4. **The Roadmap to Minimum Viable Society (MVS)** — scaling from one family → village → cities/nations → planet
5. **Challenges, Collaboration, and the Path Forward** — seven chapters: Pitfalls & Skepticisms, Why This Is Not a Social Credit System, Learning from Those Who Tried, When the Pod Meets the State, Governance & Conflict Resolution, MVS in Action, A Hopeful Reckoning
6. Closing appendix — Bharati's Tamil poem with translations, then `# References & Data Sources` (book.md:2886)

## manifesto.md Structure

Two parts ("The Great Sleep", "The Great Awakening") of eight chapters each. Every chapter is an expansion of one line of Bharati's poem (தேடிச் சோறுநிதந் தின்று…), quoted as an italic Tamil epigraph directly under the chapter heading. The full poem appears in book.md's closing appendix — the two documents are linked through it. Keep the epigraph lines and their order intact when editing.

Note the manifesto's heading convention differs deliberately from the book's: it uses `# Part 1: …` (no `{class: part}` markers) and `## **Chapter N — Title**` with bold markers. Don't "normalize" it to match book.md.

## Settled Design Decisions — Do Not Contradict

**book-1 (the new book) — titled *Nothing Has to Happen First*:**

- **The floor is eight rights**, spelled `entitled(every person, event { P() })`, and its protection is a **compile-time prohibition**: a rule punishing someone for lacking a floor right is refused by the stratifier. The floor is protected *because* it is reachable — it sits inside the `prisoner` cone. Do not restate the older claim that "nothing derives it, so nothing can retract it"; that had the mechanism backwards.
- **A thin constitutional layer is the duty-bearer** — an agent with real taxing and inter-community equalisation power, carefully limited. Mutual covenants was rejected because the constitution has no membership concept and covenants would gate the floor on one; naming-the-gap was rejected as evasion of a solved question. The book concedes coercion plainly and states its social-democratic ends outright — the novelty is the constraint mechanism, not the absence of a provider.
- **The title is *Nothing Has to Happen First*** (subtitle provisional). Not "utopia" — the word invites the naive-utopianism dismissal and belongs to the legacy book.
- **Chapter order is strictly computed**, never chosen. Exactly three elements are exempt from the derivation gate and each is labelled in the text: the opening note, Part V, and the final method part.
- **The length invariant is "book-1 stays majority-derived, measured across the whole book"** — the derived chapters must outweigh the opening note plus Part V plus the method part, combined. Targets: Parts I–IV **~38,000** (15,560 today), opening note ~800, Part V **~12,000**, method part **~5,000**; total ~55,800, derived 68%. Do **not** restate the old cap — *"~14,500 against ~36,000 derived keeps it near 29%"*. That ratio was computed before a single chapter existed, against a denominator its own commit hedged as "perhaps 36,000", implying ~2,570 words per chapter against an actual mean of 1,076; it also measured Part V against derived + Part V rather than against the book. Note the invariant is **not** what sets the 38,000: break-even is derived > 17,800, so the expansion is an editorial choice about the book's size and Part V's 12,000 has to be justified by content, not by ratio.

**Legacy `book.md` (below) — historical; do not port these into book-1 without re-checking them against the constitution:**

These were argued out and hardened in the text; several are stated as bright lines the book calls unamendable. A chapter edit made in isolation can easily re-introduce a passage the book now explicitly refutes, so check against this list before writing about points, identity, or voting.

- **Merit points are earn-only recognition** — never spent, gifted, priced, or converted. Recognition is also non-rivalrous: no fixed sectoral pools, because one nurse's acknowledgment must not come at another's expense. Inflation is controlled at the contribution level (per-task standards, caps, diminishing returns). See "What Merit Points Are—and Are Not". Scarce non-essentials above the floor are allocated by transparent non-market rules (need, rotation, waitlist, lottery), with merit only as a qualifying threshold.
- **No negative scoring of persons.** Nobody's record is ever docked as punishment; sanctions reach *perks* through due process. Pollution and fraud are handled by regulating the enterprise — a different instrument from scoring a human being (book.md:339).
- **The rights floor is never gated on identity.** *Serve first, reconcile the record afterward*; `"no record found"` must read as *pending*, never *denied*. Stated as doctrine at book.md:746 and as the first bright line at book.md:2281. Every canteen, clinic, and shelter keeps a working non-biometric path.
- **One person, one vote is an unamendable floor.** Merit never weights votes; contribution can earn advisory voice (speaking slots, sponsorship), never a heavier ballot. book.md:2285 records the book correcting its own earlier drafts on this — don't reintroduce weighted voting anywhere.
- **Transparency is aimed at power, privacy at persons.** The three-tier data classification in the Quantum-Secure chapter (Public: budgets, flows, weights, tallies / Pod-visible: who-verified-whom, waitlists, standing tier / Private-ZK: biometrics, vote choice, medical records) resolves the transparency-vs-ZK tension. "Anyone can see who's amassing points" means tier and flagged anomalies, never an itemized feed.

## Editorial Decisions Already Executed

Deliberately removed — don't helpfully restore them: part-intro preview lists, and the mechanical "Coming Up Next" / "Next Steps" / "Ready to Begin" teasers (the three substantive Part-5 prose bridges were kept on purpose). Book headings carry **no** bold markers — `grep -c "^#\+ \*\*" book.md` should stay 0. Only one `## Key Takeaways` block survives, in Merit Points; that is intentional.

## Sourcing

Every statistic and named study in the book is listed under `# References & Data Sources`, grouped by chapter, with a primary source and URL. Adding an empirical claim means adding its reference there in the same commit. Don't fabricate figures — the costed-transition TODO item is author-gated precisely because it needs real fiscal magnitudes.

## Vocabulary & Voice Conventions

The author has deliberately standardized terminology (see git history):

- **"employment"**, not "work" or "jobs" — the book redefines employment beyond salaried labor
- **"merit points"** (lowercase in prose, "Merit Points" in headings) — the recognition system replacing wages; never call it money or currency
- Recurring proper concepts (legacy `book.md` only — **MVS, pods and the tech stack are all out of scope for book-1**): **MVS** (Minimum Viable Society), **YAD** (Yet Another Device — government-issued device for those without smartphones), **Proof of Personhood** (Orb-style biometric identity), **pods** (local pods → regional councils → global federation), **local-first / offline-first micro-blockchains**, **quantum-secure**

**No counted claims in the prose.** Do not write "twenty-two entries", "four people have
shelter", "eight rights" or "one thing taken". Every counting claim in this book that has been
checked was *wrong*, not merely stale, and the design keeps moving — the evidence list changed
in a single commit, the floor may stop being eight, and more than one thing may become
takeable. The rule is not "delete numbers", which only makes the prose vaguer: **state the rule
that produces the count**. "Shelter derives for every confined person and for nobody else"
beats "four people have shelter" — it is stable under cast changes, more informative, and it is
what the book is about. `verify.sh` carries a ratchet on this; lower its `BASELINE` in the same
commit that removes a site. Rhetorical durations ("thirty years") are fine — they are not claims
about this design. This is checked per chapter as each is revised, not as one task.

Style: first-person, personal, and accessible; economic framing routinely contrasts *Keynesian*, *Marxist*, and *neoclassical* lenses (italicized); heavy use of **bold** for key claims. Both documents use curly quotes and em dashes throughout — match them. The technology chapters are intentionally more technical, with "Making It Simple: A Layman's Guide" as the deliberately non-technical retelling — keep that chapter jargon-free.

## Companion Repo

`~/projects/dhilipsiva/nibli` is a companion reasoning engine, cited by name in the tech backbone (book.md:923). Its `GUARANTEES.md` sets the register the tech chapters are converging on — state the guarantee, then name the sharp edge where it stops, rather than claiming unqualified safety. The nibli side of that convergence work lives in nibli's own `TODO.md`.

## Commits

- One chapter or section per commit; the subject names the area (`Merit points: …`, `Tech backbone (3/n): …`). Avoid sweeping multi-part edits.
- The body explains **why** — the contradiction, gap, or review finding the change resolves — wrapped at ~72 characters. Not a list of what changed.
- A content commit is followed by a separate tracker commit updating `TODO.md`: `Tracker: <what landed> (<sha of the content commit>)`.
