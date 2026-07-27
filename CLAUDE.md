# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A book-writing project, not a software project: *Utopia Reimagined: From Dream To Design*. There is no build system, test suite, or linter — all work is Markdown editing. (The `.gitignore` is a leftover Rust template; there is no Rust code.) Licensed CC0.

## Files

- `book.md` — the entire book in a single Markdown file (~2970 lines).
- `manifesto.md` — a companion manifesto, structurally independent of the book.
- `tmp.txt` — the author's scratch notes/instructions for the section currently being drafted. Read it for context on what's in progress; don't treat it as book content.
- `TODO.md` — the book/manifesto work tracker (plain bullets, ordered by leverage; work the first remaining bullet, delete it when it fully lands, update it if only partially done). Check it before starting revision work. Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory, or a design decision — skip them in unattended work and take the highest-value non-gated bullet instead.

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
- Recurring proper concepts: **MVS** (Minimum Viable Society), **YAD** (Yet Another Device — government-issued device for those without smartphones), **Proof of Personhood** (Orb-style biometric identity), **pods** (local pods → regional councils → global federation), **local-first / offline-first micro-blockchains**, **quantum-secure**

Style: first-person, personal, and accessible; economic framing routinely contrasts *Keynesian*, *Marxist*, and *neoclassical* lenses (italicized); heavy use of **bold** for key claims. Both documents use curly quotes and em dashes throughout — match them. The technology chapters are intentionally more technical, with "Making It Simple: A Layman's Guide" as the deliberately non-technical retelling — keep that chapter jargon-free.

## Companion Repo

`~/projects/dhilipsiva/nibli` is a companion reasoning engine, cited by name in the tech backbone (book.md:923). Its `GUARANTEES.md` sets the register the tech chapters are converging on — state the guarantee, then name the sharp edge where it stops, rather than claiming unqualified safety. The nibli side of that convergence work lives in nibli's own `TODO.md`.

## Commits

- One chapter or section per commit; the subject names the area (`Merit points: …`, `Tech backbone (3/n): …`). Avoid sweeping multi-part edits.
- The body explains **why** — the contradiction, gap, or review finding the change resolves — wrapped at ~72 characters. Not a list of what changed.
- A content commit is followed by a separate tracker commit updating `TODO.md`: `Tracker: <what landed> (<sha of the content commit>)`.
