# TODO — book.md and manifesto.md

Tracker for the **existing** book and manifesto. Plain bullets, never numbered —
work the FIRST remaining bullet; cross-reference items by name. Delete a bullet
entirely when it fully lands; update it if only partially done. Ordered by
leverage, not by chapter order. History belongs in git, not here.

Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory,
or a design decision — skip them in unattended work and take the highest-value
non-gated bullet instead.

Settled design decisions live in `CLAUDE.md`, not here — check them before writing
about points, identity, or voting. The **new** derived book has its own tracker at
`new-book-plans/TODO.md`; that work does not block anything below, and nothing
below blocks it.

---

- **[AUTHOR-GATED] Voice and people pass.** Convert the bullet scaffolds of Parts
  3-6 to paragraphs (keep bullets only for genuinely enumerable content); move the
  Part 5 confessional register ("I'm not the smartest person on Earth", ~1514) to
  the book's opening; pick one named fictional family and one village and carry
  them through food, healthcare, housing, governance, and crisis by expanding the
  existing day-in-the-life vignettes (~950-957, ~1374-1381, ~2397-2404) into a
  narrative spine; write ONE dramatized failure scene (a pod that collapses, a
  merit dispute mediation doesn't fix) and hang the Pitfalls material off it.
  Consider retitling around "Minimum Viable Society" — the book's best coinage.

- **[AUTHOR-GATED] Put the poem at the front and bind the two documents.** Move the
  Bharati poem from the back-of-book appendix to the opening with a page of
  personal framing (when you met it, why it structured your thinking); either open
  each book part with its corresponding lines (the poem as the book's spine) or
  fully separate and cross-reference. Add a short foreword to each document stating
  their relationship: manifesto = summons, book = specification. Manifesto side:
  compress Part 2 Ch 5-7 back toward image and demand (the org charts and funding
  streams bolted onto devotional lines produce bathos) and point to the book for
  mechanism; reconcile or consciously scope the manifesto's Ch 3-4
  transitional-justice demands (debt relief, reparations, expungement), which have
  no book counterpart. **Settle the attribution first** — book.md:2838 names *Yoga
  Siddhi* ("Varam Kettal"), and a Tamil-literature source should confirm it before
  the poem is promoted to the front matter.

- **Answer the duty-bearer question and fix the governance mechanics.** Universal
  "non-negotiable" rights atop a voluntary, coercion-free federation have no
  identified agent obligated to provide or compel transfers — either accept a thin
  constitutional layer with real taxing/inter-pod-equalization power (and carefully
  limit it), or rename the guarantees "mutual covenants" and be honest about
  non-members and defectors. Confront the magnet problem (mobility is itself a
  guaranteed right; generous pods attract need — standard fiscal-federalism
  territory). Replace at-will recall with defined thresholds + an administering
  body + staggered short terms; explain how a consensus-only global federation
  avoids the universal veto on exactly the planetary problems it exists for. Add a
  real justice chapter: standards of proof, due process, proportionality, an
  appeals path independent of the merit apparatus, a precise replacement for the
  misused "crimes against humanity", and who inspects "restricted housing". Answer
  Ambedkar: caste as a design problem, not a historical footnote — reserved
  committee representation, mandatory external audit of allocation patterns,
  portability of entitlements so exit from a hostile pod is not destitution.

- **[AUTHOR-GATED / needs data] Rewrite Transition Costs with a costed worked
  example.** A fiat price tag on the 200k-city baseline and funding per phase, plus
  a housing acquisition mechanism (community land trusts vs right-of-first-refusal).
  Needs real fiscal magnitudes and a design choice — don't fabricate numbers.

- **[AUTHOR-GATED] Consolidation cut — the destructive/subjective remainder.** NOT
  for autonomous execution. (a) Dedupe the safeguard litany (caps / diminishing
  returns / rotation / transparent ledgers / peer verification) across 5+ chapters
  — risky because the Pitfalls and Governance chapters re-answer distinct
  objections with it, so a blind "state once, reference after" would weaken their
  self-containment; decide per-occurrence. (b) Merge Part 4 (Implementing
  Fundamental Rights) into Part 2, and collapse Pitfalls + Governance into one
  chapter — reorganizes ~600 lines and ripples through the Part-5 cross-references
  and bridges. Both want author sign-off on scope.

- **[AUTHOR-GATED] Tech backbone — the two opinionated remainders.** (a) "Why a
  blockchain at all?", honestly weighing CRDTs / signed logs against nibli-store's
  HLC/tombstone/CRDT-export design — this partly argues against the book's central
  premise, so the author decides how hard to hedge. (b) Replace venture brand names
  (union.build, Sui, Fuel, linera) with capability requirements plus a dated
  appendix — removes specific tools the author chose to name. The nibli-side half of
  this convergence lives in nibli's own `TODO.md`.

- **Reconcile the rights floor across all three artifacts.** The 2026-07-27
  verification pass found `book.md` carries at least five mutually inconsistent
  floors internally, and the sentence that does the firewall work names seven items
  rather than the eleven asserted elsewhere; `manifesto.md` names five, promoting
  mobility and dropping security and expression. Pick the canonical list and make
  every enumeration in both documents match it. Coordinates with the same decision
  in `new-book-plans/TODO.md` — settle it once, apply it three places.
