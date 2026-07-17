# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A book-writing project, not a software project: *Utopia Reimagined: From Dream To Design*. There is no build system, test suite, or linter — all work is Markdown editing. (The `.gitignore` is a leftover Rust template; there is no Rust code.) Licensed CC0.

## Files

- `book.md` — the entire book in a single Markdown file (~2700 lines).
- `manifesto.md` — a companion manifesto, structurally independent of the book.
- `tmp.txt` — the author's scratch notes/instructions for the section currently being drafted. Read it for context on what's in progress; don't treat it as book content.
- `TODO.md` — the book/manifesto work tracker (plain bullets, ordered by leverage; delete a bullet when it lands). Check it before starting revision work. The companion repo `~/projects/dhilipsiva/nibli` carries the tech-backbone convergence bullets in its own TODO.md.

## book.md Structure

Six parts, each opened by a `{class: part}` attribute line (Leanpub/Markua syntax — preserve these markers exactly). Chapters are `#` headings, sections `##`, subsections `###`:

1. **The Need for Change** — the problem: physical abundance vs. financial scarcity
2. **Defining the Core** — fundamental human rights, employment redefined, merit points, and the technology chapters (The Technological Backbone, Proof of Personhood, Quantum-Secure & Privacy-Centric, Making It Simple)
3. **Implementing Fundamental Rights** — food/water/education, healthcare, shelter/mobility/communication, environmental stewardship
4. **The Roadmap to Minimum Viable Society (MVS)** — scaling from one family → village → cities/nations → planet
5. **Challenges, Collaboration, and the Path Forward** — pitfalls, governance, MVS in action
6. Closing appendix — Bharati's Tamil poem with translations

## manifesto.md Structure

Two parts ("The Great Sleep", "The Great Awakening") of eight chapters each. Every chapter is an expansion of one line of Bharati's poem (தேடிச் சோறுநிதந் தின்று…), quoted as an italic Tamil epigraph directly under the chapter heading. The full poem appears in book.md's closing appendix — the two documents are linked through it. Keep the epigraph lines and their order intact when editing.

## Vocabulary & Voice Conventions

The author has deliberately standardized terminology (see git history):

- **"employment"**, not "work" or "jobs" — the book redefines employment beyond salaried labor
- **"merit points"** (lowercase in prose, "Merit Points" in headings) — the recognition system replacing wages; never call it money or currency
- Recurring proper concepts: **MVS** (Minimum Viable Society), **YAD** (Yet Another Device — government-issued device for those without smartphones), **Proof of Personhood** (Orb-style biometric identity), **pods** (local pods → regional councils → global federation), **local-first / offline-first micro-blockchains**, **quantum-secure**

Style: first-person, personal, and accessible; economic framing routinely contrasts *Keynesian*, *Marxist*, and *neoclassical* lenses (italicized); heavy use of **bold** for key claims. The technology chapters are intentionally more technical, with "Making It Simple: A Layman's Guide" as the deliberately non-technical retelling — keep that chapter jargon-free.

## Workflow

Commits are small and scoped to one chapter or section (e.g., "Update proof of personhood", "merit points"). Follow that pattern rather than sweeping multi-part edits.
