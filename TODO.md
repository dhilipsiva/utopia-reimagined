# TODO — book-1

**This tracker covers book-1 only.**

The repo is heading for two new books plus a clean deletion:

- **book-1** — the active work. Derived from the nibli constitution, plain English,
  for a **primarily international/global audience**, no technical jargon: anyone
  should be able to pick it up and follow it. The formalism stays invisible; what
  readers verify is the **data**.
- **book-2** — the technical companion: how book-1 is actually implemented with
  technology. Not planned yet. **It gets its own tracker, written from scratch once
  book-1 is finished.** Do not add book-2 items here — park them in the hold list
  at the bottom.
- **`book.md` and `manifesto.md`** — legacy, to be **deleted** once both new books
  are written. Nothing in this tracker improves them. The one obligation they carry
  is that no valuable material is lost on the way out; see the legacy-harvest
  section.

book-1 references book-2 **once**, at the very end (see the pointer item).

Plain bullets, never numbered. Work the FIRST remaining bullet; cross-reference
items by name. Delete a bullet entirely when it fully lands; update it if only
partly done. Ordered by dependency and leverage, not by chapter order. One item at
a time: do it, verify it, commit it. History belongs in git, not here.

Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory,
or a design decision — skip them in unattended work and take the highest-value
non-gated bullet instead.

Settled design decisions live in `CLAUDE.md`, not here. Planning material is in
`new-book-plans/`. Note `CLAUDE.md` still describes the repo as being *about*
`book.md` — it needs the same restructure this file just had.

**nibli handoff protocol.** dhilipsiva wrote nibli. When an item is blocked by an
engine bug or a missing KR construct, do not work around it in prose — the bullet
carries a ready-to-paste **HANDOFF PROMPT** for a Claude Code session in
`~/projects/dhilipsiva/nibli`. Hand it over, work the next unblocked bullet, and
resume when it lands.

**Already established — don't re-verify these** (verified on the real engine via
`nibli-host --script`, release wasm, `NIBLI_FUEL` pinned high):

- **A floor line is a compile-time prohibition, not a declaration.**
  `obligated(every person, event { P() })` compiles to a rule with `person` in the
  body, so `P` sits downstream of `prisoner`; any later rule taking `~P` into that
  cone is an unstratifiable negative cycle and is refused. Verified both ways plus
  a non-floor control. You cannot write a law punishing a person for lacking a
  floor right. Where it stops is equally established: `~P -> false` (standing),
  `~P -> lose(Points, ·)`, and positive compulsion `prisoner -> P` all still load.
- The floor is **eight** and is enacted in `new-book-plans/utopia-v2.nibli`, with
  the franchise and the isolation marker as rules. Graph after enactment: 37
  predicates, 16 derived, 28 rules, max stratum 3, **stratum 3 still exactly
  `{err, travel}`** — the single-deprivation theorem survives.
- All 17 v0.1 regression pins, all three exploit closures (E1 shield, E2 epoch
  carry, E3 farmhouse) and Article 9's self-entrenchment are unchanged through
  v0.2 and the enactment, each checked against a v0.1 baseline run.
- The seven original fidelity-table rows are true — but **none is reproducible
  from the committed artifacts**, which is what the harness bullets exist to fix.
- The 2026-07-27 source pass stands: nine parallel verifications against primary
  sources. Its corrections are the research-brief section below.

Note `3-spine.md`'s stratification table and chapter order are now **stale** — they
predate the enactment and do not contain `decide`, `meets` or `mature`. Recompute
before relying on them.

Everything else in `new-book-plans/` is unverified or corrected below.

---

## Blocking decisions — nothing should be drafted until these are settled

- **[AUTHOR-GATED] Answer the duty-bearer question — this is the one place the
  nearest established alternative beats the design outright.** Book-1's floor is
  social-democratic in its ends (universal provision, universalism over
  means-testing, decommodification of essentials — it is Universal Basic *Services*,
  not UBI, and should probably claim that name). But social democracy delivers
  through a coercive taxing state, and this design refuses one. A voluntary,
  coercion-free federation has **no identified agent obligated to provide anything
  or to compel transfers.** Social democracy answers this; the design currently does
  not. A reviewer who notices will file the whole book as social democracy with
  extra steps and an unpaid bill, which wastes the genuinely novel parts.

  **It is worse than an unanswered question — the vocabulary has no slot for the
  answer, and the predicate in use may invert the claim.** Verified against nibli's
  committed corpus: `obligated` comes from Lojban `bilga`, places
  `["duty", "do", "standard"]`, template **"{x1} is obligated to {x2}"** — x1 is the
  party *bearing* the duty. So `obligated(every person, event { eats() })` reads
  literally as *every person has a duty to eat*, not *every person is owed food*.
  That is an inversion of the book's central claim, and `bilga` has **no beneficiary
  place at all**, so the constitution cannot presently name who owes the floor to
  whom. Note this breaks no derivation — `obligated` appears in no rule head or body
  — and the Article 1 firewall works regardless, because it comes from the compiled
  `P -> person` edge rather than from the deontic reading. The damage is entirely to
  what the sentence *means*, which for the foundation of the book is worse than a
  broken rule. It would also be the fourth instance of prose lying about the machine,
  after the farmhouse bug, "due process" in a comment, and bright line 2.

  Resolve in this order:
  - **Fix the predicate before anything else is built on it.** Options: use nibli's
    deontic operator (`must`, compiling to `Obligatory(...)`) which is the
    semantically correct tool but still names no bearer; find a corpus predicate with
    a beneficiary place; or hand off for one. Do not "define `obligated` as a term of
    art in the file" — that is exactly the failure mode this project keeps hitting.
  - **Then take the political fork, which is a real choice and yours.** Either accept
    a thin constitutional layer with genuine taxing and inter-community equalisation
    power, and limit it carefully — which moves the design decisively toward social
    democracy and should be admitted as such — or rename the guarantees **mutual
    covenants**, and be honest in print about non-members, defectors, and what
    happens when a community simply declines. The second is more faithful to the
    voluntarism; the first is more likely to survive an economist.
  - Whichever way it goes, Part V's five-joints chapter must state plainly where the
    design sits relative to social democracy **and** where social democracy has the
    better answer. Conceding that is far stronger than letting a reviewer find it.

- **[AUTHOR-GATED] Build Part V on the five-joints scorecard.** Four architectures
  were designed and judged by a reader, a trade editor and a hostile expert. The
  salvage audit is settled and measured (I re-verified the counts): the four harvest
  candidates total 6,653 words — social credit 1,757, "Learning from Those Who
  Tried" 2,264, "When the Pod Meets the State" 2,092, "The Calculation Problem" 540.
  **~30% survives near-verbatim and every near-verbatim survivor is evidence; not
  one argumentative frame survives.** "Learning from Those Who Tried" is the only
  genuine harvest — the nine historical cases are researched, sourced and
  mechanism-independent. "When the Pod Meets the State" is unsalvageable: it says
  "pod" 21 times in 2,092 words, and the new book has no pods. The social-credit
  chapter is the best writing in the manuscript and unliftable — seven named
  dependencies, including its showpiece self-correction passage, which points at
  three chapters that will not exist.

  **Recommended: the five-joints skeleton, at ~14,500 words.** A century of
  attempts broke at five recurring joints — valuation, rotation, coercion, capture,
  the state — so score this design against those five. It is the only principle
  legible in one sentence, the only proportionate length, and the only one that
  solves the confession problem structurally rather than rhetorically. It won the
  reader judge and the editor judge, and the editor's reason matters: it was the
  only design that *measured* rather than estimated, and its numbers check out.
  Graft on two things from the losing designs: the three-word verdict vocabulary
  (**Survives / Survives, narrowed / Fails as stated**, printed once and never
  expanded — the most enforceable seam device proposed, because it disciplines at
  the sentence level), and the rule that **every limit closes on a specification**
  concrete enough to be worked on, not on an admission.

  **One fix before building it:** do not publish a numeric self-grade. The hostile
  judge's dismissal sentence for this design was *"two and a half out of five"* — a
  failing grade, self-administered, printed as the structure of the part. Score
  against the joints without scoring the design out of five.

  Both open calls are now **decided**:
  - **Concealment — resolved by the book-2 split.** The hostile reviewer's attack
    was on the constraint, not the book: *"The repository is public. I found it in
    an afternoon."* An unmentioned but discoverable apparatus reads as concealment;
    a named one reads as discipline. But saying it plainly inside book-1 would put
    a formal-methods discussion in a book that must stay jargon-free. So it goes
    where it already belongs: **the single book-2 pointer at the end carries one
    honest sentence** — the design was machine-checked for consistency, the
    machinery is public, book-2 covers it. One sentence, skippable by the general
    reader, and it closes the open goal completely. It is also exactly Krugman's
    step (3) discharged.
  - **Proportion — capped.** Part V targets **~14,500 words**, and book-1 stays
    majority-derived. If Part V approaches half the book, the derivation reads as
    decoration; ~14,500 against ~36,000 derived keeps it near 29%.

- **[AUTHOR-GATED] Settle the title, and whether "Minimum Viable Society" travels.**
  MVS is the old book's best coinage. Decide whether the new book keeps it — and
  whether it reads for a global audience — before any sample chapters go out. The
  same question applies to retitling `book.md` around it.

## Settled — carry out as the artifacts land, blocks nothing

- **Apply the licence structure.** Decided and recorded in `LICENSING.md`: prose
  **CC-BY-4.0**, code **MIT OR Apache-2.0**, data registry **CC0**, constitution
  under nibli's terms. Already-committed files stay CC0 irrevocably; the root
  `LICENSE` stays put and keeps governing them. What remains is mechanical and
  belongs with the artifact it covers — drop `LICENSE-CC-BY` in the book's
  directory with a licence line in the front matter; add `LICENSE-MIT` +
  `LICENSE-APACHE` and `SPDX-License-Identifier` headers when the harness and
  fetchers are written; add `LICENSE-CC0` in the registry directory. Since
  exclusivity is now permanently off the table, the reach strategy is serialization
  and open circulation — plan the publishing route on that basis.

## The verification harness — build this before writing prose, so every later claim is checkable

- **Adopt nibli's own pinned-verdict format for the constitution's pins.** nibli
  already solved this: `determinism-corpus.nibli` annotates every query with
  `# => TRUE` and three separate CI legs assert against those annotations. The
  book's fidelity table should be the same artifact in the same format, not a
  Markdown table with green ticks. Convert `utopia-v2-run.nibli` to it. The
  verdicts to pin are known: `person(Hano)` TRUE, `expresses(Hano)` TRUE,
  `travel(Hano)` FALSE, `travel(Adam)` FALSE, `travel(Jala)` TRUE,
  `prisoner(Jala)` FALSE, `eats(Adam)` FALSE, `healthy(Bela)` FALSE, plus the
  enacted three — `decide(Hano, Ballot)` TRUE, `decide(Jala, Ballot)` TRUE,
  `err(Hano, Isolation)` TRUE.

- **The harness needs a second mode: negative pins that must FAIL to load.** The
  Article 1 firewall cannot be tested by any query, because what must fail is the
  *assertion*. Its test is "append this rule and the file must refuse to compile" —
  a mode no existing runner has. Three cases are specified in `utopia-v2.nibli`'s
  v0.3 pin block: `~believe -> prisoner` MUST be refused, `~meets -> prisoner` MUST
  be refused, and the non-floor control `~home -> prisoner` MUST load. **Keep the
  control** — without it a green firewall test proves nothing about the floor, only
  about the rule shape. This is the only test the book's strongest claim has.

- **Fix the run script: it loads the wrong constitution and records no
  expectations.** `utopia-v2-run.nibli` line 1 is `:load utopia.nibli` — it pins
  **v0.1**, not the `utopia-v2.nibli` beside it — which now carries the enacted
  eight-right floor, so the gap is a whole constitutional revision wide. And it
  lists queries with no
  expected verdicts, so it cannot fail; it is a transcript, not a test. Six of the
  seven fidelity rows have no query in it at all.

- **Delete `run-kb.rs`, or make it the real runner — it cannot run the committed
  script.** It dispatches only `:load`, `:contradictions`, `?` and comments; the
  pin script is almost entirely `:proof-verbose` lines, which fall through to
  `assert_text` and produce **42 syntax errors and zero verdicts**. It is also
  wired into no `Cargo.toml`. `nibli-host --script` already does this job and does
  support `:proof-verbose` (but not `:contradictions` — pick one runner and make
  the script match it).

- **Make fuel exhaustion a hard failure, never a silent FALSE.** At default fuel,
  `travel(Hano)` and `travel(Jala)` return `RESOURCE_EXCEEDED (fuel)` — not TRUE,
  not FALSE. Any harness that treats "not TRUE" as FALSE would score the fidelity
  table green while proving nothing. nibli's own determinism gate explicitly
  **excludes** fuel-trapping queries as runtime-dependent. Pin `NIBLI_FUEL` in the
  harness, and fail loudly on `RESOURCE_EXCEEDED`.

- **Fix or replace `4-strata.py` — it is not cosmetic, it already caused a wrong
  answer.** Its parser takes only the *first* predicate on a fact line, so it never
  descends into `event { … }` and the floor rights are invisible to it: `secure`,
  `eats`, `healthy`, `learn` and now `believe` do not appear in its output at all.
  Two consequences, and the second is the serious one. (a) The "four rights appear
  exactly once" finding is true but the script did not compute it. (b) **The script
  reports floor lines as graph-inert, and they are not** — the engine sees an edge
  `P -> person` that the script cannot, which is the whole firewall. Relying on the
  script's "no change" output is what produced, and briefly committed, the wrong
  conclusion that a floor line does nothing. Extend the parser to descend into
  `event { }` blocks, or replace it with something that reads the engine's own
  compiled IR. Until then, treat its output as a lower bound and confirm any
  structural claim against the engine.

- **Write the claim-to-query table as a generated artifact, not a hand-maintained
  one.** One row per load-bearing sentence: sentence, query, expected verdict.
  Regenerated on every constitution change; any row whose verdict flips is a
  paragraph that has started lying. Private to the author — the reader never sees
  it. This is the Catala pattern, and the `err(Lalo)` bug below is the argument for
  it.

## Constitution (KB) work

- **Fix `err/2`: it fires on correctly-placed prisoners.** `err(Lalo, Placement)`
  is **TRUE** — but Lalo is severe+family and Article 6 routes him correctly to
  `building(HighSec, Lalo)` (also TRUE). The rule
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)` reads *"has a home"* as
  *"was placed at home"*. Any severe offender who happens to have a home trips a
  false breach. It behaves correctly for Ruk (TRUE, intended) and Hano (FALSE,
  intended) and false-positives on Lalo. The pin script queries
  `err(Lalo, Placement)` — with no expected value, so nothing caught it. Fix:
  separate the *fact* of having a home from the *decision* to place someone there.

- **Write the fact-write trust base as a file-level section — it is the
  constitution's actual security model.** An adversarial re-audit confirmed **15
  further exploits** on the engine beyond the three disclosed, sharing one root
  cause: *nibli cannot make a predicate derived-only, so every gate v0.2 calls
  "derived" is still assertable.* Confirmed attacks: `authority(Pax).` reopens E1a
  verbatim (`defend(Don)` TRUE, `prisoner(Don)` FALSE); `fit(Ruk, Homestay).`
  silences E3's breach marker; two asserted `permits(Review, ·)` facts defeat
  Article 8's headline claim outright and void an innocent (`false(Ara)` TRUE,
  `lose(Points, Ara)` TRUE) using sock puppets the Electorate never seated. Others
  worth naming: `rotten/1` is a single-writer universal void; `broken(Court).` is a
  one-fact universal amnesty; one asserted `deceive` jails the file's own honest
  whistleblower Rebel; Article 9's `adjust` is self-declared by the proposer, so a
  target-less amendment enacts unconditionally. The file discloses this hole for
  `permanent()` only (lines 150–154). Promote it: list **every** predicate whose
  direct assertion breaks a stated guarantee — `permits(Review,·)`,
  `permits(Appeals,·)`, `authority`, `fit`, `defend`, `rotten`, `deceive`, `severe`,
  `family`, `broken`, `parent`, `teaches`, `work`, `adjust`, `permanent`.

- **Guard the personhood roster — it defeats all eight rights at once.** `person`
  has 29 asserted facts and exactly one producing rule (`prisoner -> person`), so
  the sole non-assertion route into rights-bearing status is *being imprisoned*.
  Deleting `person(Bela)` costs Bela the entire floor plus `travel` and the
  ballot, derives no `err`, and never touches Article 9 — which entrenches **rules,
  not facts**. This is now the largest hole in the design: the floor's protection
  is a compile-time firewall over `person`, so the firewall is only as good as the
  roster, and the roster is a pile of assertions. Every right is unconditional
  *above* the atom `person(X)`, and `person(X)` is one deletion away. Fix: `all $x: human($x) -> person($x).` plus a roster
  breach marker so de-personing derives an `err` rather than silently succeeding.
  Add `person` to the fact-write trust base list above.

- **Rename the Article 6 `dwell` head — one atom is doing two jobs.** Every rule
  head producing `dwell` requires `prisoner` (lines 78, 81, 88; there is no other),
  so `dwell(Lalo)` does not mean "Lalo is owed shelter" — it means "Lalo is housed
  at HighSec". The same atom carries both *entitled to a home* and *in a cell*.
  Free to fix, and a hostile reviewer finds it in an afternoon. Rename the
  placement head to `placed`, or fold it into `building`. Pairs with the `err/2`
  fix above — both are Article 6 conflating a fact with a decision.

- **Mark confinement without conviction.** Nothing makes `building` derived-only:
  assert `building(HighSec, Rebel)` and no rule objects — no `injure`, no
  `judge(Court, ·)`, so `prisoner(Rebel)` is FALSE and `travel(Rebel)` stays TRUE.
  The constitution certifies as free a person it is holding. Cheapest high-value
  fix in the set, and it defends the crown jewel directly:
  `all $x: all $f: building($f, $x) & ~prisoner($x) -> err($x, Confinement).`
  Use a third `err` flavour rather than reusing `Placement`, matching the
  `err(_, Isolation)` marker already enacted — the audit surface stays one
  predicate while each breach stays separately queryable.

- **Entrench the evidence vocabulary.** The file states its own threat model in one
  sentence — *"enlarging the evidence vocabulary is the quietest way to capture a
  system"* — and then `permanent()` entrenches `Art_Floor`, `Art_Person` and
  `Art_Entrench`. The named attack is the one thing not entrenched. Add
  `permanent(Art_Evidence).`

- **Put a precondition on `capture`.** Every lens that examined the evidence layer
  converged here independently. `capture($a, $audited)` has no precondition
  anywhere: any two Review-credentialed people who `judge` and `capture` a target
  can void them, with nothing limiting who may be captured or on what grounds. Add
  a standing/grounds guard, plus an epoch expiry on `capture` and `judge`.

- **Restore v0.1's stratification note to Article 7 — its deletion is a live
  landmine.** v0.1 carried: *"(No `person(_)` condition: person depends on prisoner
  via Art 1, and prisoner uses `~defend` — that would form an unstratifiable
  negative cycle.)"* v0.2 dropped it. Adding `person($w)` to the shield rule is the
  most natural tightening anyone would reach for, and it is **rejected atomically**
  — the replacement silently vanishes and the *original permissive rule stays in
  force*. That is precisely the "a permissive rule left in place keeps its exploit"
  failure the v0.2 header warns about, now reachable through the stratifier rather
  than through oversight. Related but distinct from the Article 1 firewall
  commentary already enacted: that documents the stratifier *protecting* the floor,
  this documents it *silently rejecting* a well-meant tightening.

- **Resolve the polarity contradiction between Articles 6 and 7.** Article 7's
  shield is deliberately fail-**open** toward protection and defended at length as
  "a political choice surfaced in logic" — `defend(Sly)` TRUE / `prisoner(Sly)`
  FALSE works exactly as designed. Article 6's `~permits(Appeals, $offender)` is
  fail-**closed** against protection: appeal is relief that must be granted, not
  standing anyone holds. Same book, opposite defaults, no stated reason. This is an
  internal inconsistency rather than an imported criticism. Separate
  standing-to-seek-review from a pending review that stays the sentence, or require
  an affirmative exhaustion fact for conviction. Also bound the fail-open window,
  or state the bound honestly in the chapter.

- **Give `rotten` — and `capture` and `judge` — an expiry or expungement path.** A
  single void is currently perpetual and compounds, with no route back. Derivation
  here is monotone, so nothing that ever derives stops deriving: the constitution
  **cannot forgive**. For a design whose thesis is that sanctions are defeasible,
  that is a contradiction in the machine, and it is worth framing in the book as
  forgiveness being a *right* rather than merely as a bug fix.

- **Fix the Article 4 clawback rules — they refute a published bright line.** This
  is the third instance of prose lying about the machine, after the farmhouse bug
  and "due process" appearing only in a comment, and it is the worst of the three
  because the contradicted sentence is in the manuscript's most-praised chapter.
  `book.md` bright line 2 reads *"No negative scoring of persons. Merit is earn-only
  recognition."* It is also recorded in `CLAUDE.md` as a settled decision. The
  enacted constitution contradicts it twice:
  - `utopia-v2.nibli:117` — `teaches($t,$s) & false($t) -> lose(Points, $s)` docks
    a **student** for a teacher's fraud. Negative scoring, of a person, who did
    nothing. Collective punishment, and a peremptory-norm violation.
  - `utopia-v2.nibli:116` — `false($f) -> lose(Points, $f)` docks the wrongdoer.
    Fairer, still a subtraction from a person's record, still refutes the line.
  Decide which side gives: either the bright line narrows to "no subtraction except
  by due process for one's own adjudicated fraud" and 117 is deleted, or the
  clawback rules go and sanctions reach perks only. Do not leave both in print.
  Whichever way, narrow 117 to rewards actually *derived* from the fraudulent
  teaching, which needs provenance on `reward`. Then re-check every other bright
  line against the enacted rules — nobody has done that sweep, and this one was
  found by accident.

- **Grow the provisioning layer, or write Part I to stop where it stops.**
  `eats(Adam)`, `healthy(Bela)`, `secure(Bela)`, `learn(Cira)` and now
  `believe(Bela)` are all FALSE — the gap is uniform across every floor right with
  no rule of its own, and enacting two more rights widened it rather than closing
  it. Not denial; no rule
  connects an obligation to any fact about anything reaching a person. The
  obligation layer is complete and the delivery layer does not exist. Chapters 1–2
  are writable now; a "does it actually arrive" chapter is not. Keep this visible in
  the prose either way — it is the single most credibility-buying admission the book
  has.

- **Governance mechanics downstream of the duty-bearer fork.** Do not start these
  until the fork above is taken — several change shape depending on which way it
  goes. Confront the magnet problem: mobility is itself a guaranteed right, so
  generous communities attract need, which is standard fiscal-federalism territory
  and currently unaddressed. Replace at-will recall with defined thresholds, an
  administering body, and staggered short terms. Explain how a consensus-only global
  federation avoids a universal veto on exactly the planetary problems it exists to
  solve. Add real justice material: standards of proof, proportionality, an appeals
  path independent of the recognition apparatus, a precise replacement for the
  misused "crimes against humanity", and who inspects restricted housing. Answer
  Ambedkar — caste as a design problem, not a historical footnote: reserved
  committee representation, mandatory external audit of allocation patterns, and
  portability of entitlements so that exit from a hostile community is not
  destitution. Check each against what the rules can actually express before writing
  prose about it; several are constitution work, not chapters.

- **Widen kinship beyond `parent/2`.** The multi-sig independence check excludes
  only parents; spouses and siblings co-sign freely. Disclosed in v0.1, still open.

## nibli handoffs — blocked on engine work

- **HANDOFF: derived-only (intensional) predicates.** Root cause of 13 of the 15
  new exploits, and it defeats the constitution's central security claim. Prompt to
  paste into a nibli session:
  > In nibli KR, a predicate that appears as a rule head can still be asserted
  > directly as a fact — a rule *adds* a derivation path, it never *removes*
  > assertability. I need the opposite for a constitutional model: a way to declare
  > a predicate **derived-only**, so that any attempt to assert it as a ground fact
  > is a compile/assert-time error, and its only route to TRUE is derivation.
  > Concretely, in `utopia.nibli` I derive `permits(Review, X)` from
  > `choose(Electorate, X) & ~rotten(X) & ~broken(X)`, and the whole point is that
  > nobody can hand themselves a credential — but `permits(Review, Sock).` still
  > works and voids an innocent party through the multi-sig rule. Same for
  > `authority/1` and `fit/2`. Please add an EDB/IDB separation: a declaration
  > (syntax your call) marking a predicate intensional, enforced fail-closed at
  > assert time, with a clear error. Needs to survive retraction/rebuild and behave
  > the same on all three runtimes. Please also say whether this interacts with
  > stratification or the fact-store replay.

- **HANDOFF (verify need first): exact minor-unit arithmetic.** The plans claim any
  quantitative treatment of contribution is blocked because "engine float comparison
  is tolerant". That is only half right — nibli has **both** tolerant (`sum`) and
  exact (`num_equal`/`dunli`) comparison, plus a guarded `quotient` with an exact
  divide-by-zero rule, all over f64. Before asking for anything, settle whether the
  book needs merit arithmetic at all: the old book already decided merit points are
  earn-only recognition with the arithmetic *deliberately absent*. If that holds,
  this item is **moot — delete it**. If the new book wants summed or compared
  quantities, the ask is integer/decimal minor units so exact totals are
  representable without float error.

## Data — "latest data, by script" is a build system nobody has written yet

- **Build the data pipeline before writing the empirical chapters.** The stated
  requirement is that the book depends on the latest data *as much as possible,
  achieved through scripting* — but `final-research.md` is a hand-assembled static
  snapshot, with the predictable result: figures two tax years stale, a superseded
  working paper, market data from 2015. Design: one machine-readable claim registry
  (claim id, value, units, source, retrieval date, fetch script); fetchers against
  sources that have APIs (World Bank, WHO GHO, UNEP, IEA, OWID, FAOSTAT); a
  rendering step that injects current values into the prose; and a **staleness
  gate** that fails the build when a figure's source has a newer edition than the
  one pinned. Where a number can only come from a paper, the registry pins the
  version and the retrieval date so the drift is visible.

- **Use the democracy/happiness dataset — but for the opposite claim to the obvious
  one.** `demo-happy.txt` + `democracy_vs_happiness_144.csv` (144 countries, EIU 2025
  merged with WHR 2025 life evaluations). I re-derived every headline number and they
  reproduce exactly: raw r = 0.5975, ρ = 0.6231, R² = 0.357; partial r | log GDP =
  0.195; r(GDP, happiness | democracy) = 0.623; and the regime table to the digit
  (Authoritarian 45/4.94/1.11, Hybrid 29/5.07/0.95, Flawed 44/5.80/0.94, Full
  26/6.82/0.51). The source document is careful work and its caveats are sound.
  - **Do NOT use the floor claim.** Its headline finding — "democracy behaves like a
    floor on subjective wellbeing, not a lift toward the top", from regressing
    |residual| on democracy score, p = 0.0004 — is the one claim it never controls
    for income, and **it does not survive**: adding log GDP gives democracy b =
    −0.0196, t = −0.91, **p = 0.37**, while log GDP itself is b = −0.336, t = −2.53,
    p = 0.011. Within income tertiles the dispersion goes the *wrong* way for the
    democracy story. The compression is income, misattributed. This is precisely the
    claim book-1 would most want to be true — a floor effect, in a book about floors
    — which is exactly why it must not be used. An economist kills it in one
    regression.
  - **Use the income result instead: it supports the book's real thesis better.**
    What compresses the dispersion of human wellbeing across countries is material
    provision, not the franchise. A book whose floor is eight material-and-personal
    guarantees, and which deliberately demoted the vote *off* the floor to a rule,
    just got empirical support for exactly that ordering. That is on-thesis, honest,
    and stronger than the claim that failed.
  - **Use the step sizes.** Authoritarian → Hybrid buys **+0.16** — nothing. Hybrid →
    Flawed +0.73. Flawed → Full +1.01. Partial democratisation does approximately
    nothing; the gain is concentrated at the top of the scale. That is a real
    argument against gradualist "add a little democracy" reform.
  - **Make it Part V's worked example of the method.** Take "democracy makes people
    happier", test it, and report: survives raw, narrows sharply under income
    control, and the floor version fails outright. The book demonstrating that
    discipline on a claim it would have loved is worth more than the claim.
  - **Licensing blocker for the registry: the EIU index is non-redistributable** —
    Our World in Data cannot export it. A CC-BY book with a public claim registry
    cannot ship those numbers. Either cite-and-link without redistributing, or switch
    to **V-Dem**, which is openly licensed and gives the same picture (r = 0.52).
    Resolve before the registry is built.
  - Housekeeping: `demo-happy.txt` is a chat transcript, not a source — record it as
    "prior analysis, independently re-derived" with the CSV's provenance pinned (WHR
    2025 = 2022–2024 average; EIU 2025). Delete
    `democracy_vs_happiness_144.csv:Zone.Identifier`, a Windows
    alternate-data-stream artifact, and add the pattern to `.gitignore`.

- **Give the reader a verification path, since they cannot see the logic.** The
  formalism stays invisible — so what the reader verifies is data. Ship the claim
  registry as the public artifact: every number in the book, its primary source,
  the date it was fetched, and the script that fetches it. This is the thing that
  earns the trust, and the honest substitute for showing the constitution.

- **Re-cite everything against the published versions.** Muralidharan, Niehaus &
  Sukhtankar is no longer a working paper — it is *Review of Economics and
  Statistics* 107(2): 372–392 (2025). Expect several others to have moved similarly.

## Correcting the research brief — each is a discrete, committable fix

- **Rewrite the social-choice paragraph — the most damaging error in the brief.**
  The claim that score voting "escapes Gibbard–Satterthwaite's ordinal frame", with
  the gloss *"it is always optimal for a voter to give the best candidate the
  highest possible score"*, is unsourceable and inverts the result: **Gibbard's 1973
  game-form theorem applies directly to score voting, and score voting is
  manipulable**. The quoted sentence describes strategic exaggeration, not
  strategyproofness. Also: Arrow's theorem needs the **transitive-social-ordering**
  condition the brief drops (relaxing it is a real escape route);
  Gibbard–Satterthwaite needs **determinism/single-valuedness** (randomised schemes
  escape, per Gibbard 1977); Black (1948) gives the *Arrow* escape on single-peaked
  domains but **Moulin (1980)** gives the strategyproofness escape, with the
  McKelvey–Schofield caveat that it dies in multiple dimensions; and the "two-thirds
  is neither manipulable nor dictatorial" quote has no source — the substance is the
  **two-outcome** restriction, not the supermajority threshold. The defensible claim
  in this vicinity is the sincere-favourite criterion. Getting this wrong is what
  gets the book dismissed by exactly the readers it wants.

- **Fix the Housing First bullet — two outright errors.** The AJPM Community Guide
  economic review is **Jacob et al. (2022)**, not "Chapman et al. (2021)". And
  "decreased homelessness by 88% versus 47% for Treatment First" misdescribes what
  the CPSTF review reports. Re-derive both from source before the sentence is used.

- **Fix the Muralidharan quotation — it is a splice presented as verbatim.** The
  sentence given as "verbatim from the abstract" appears in **no** version of the
  abstract: it welds the February 2020 abstract (which says **10%**) onto a
  **10.6%** figure from the body of the September 2021 revision. Related number
  fixes: "~2 million lost access" should be **1.5–2 million**; "~1.6 million (13% of
  beneficiaries)" should be **1.7 million** (1.2 million under the paper's
  conservative assumption), and the 13 is a percentage-*point* increase in treated
  blocks only. The "almost 90% genuine" figure — the brief's self-declared strongest
  datapoint — is **88%**, is labelled *"purely descriptive"* and non-causal by its
  own authors, and covers **1.44 lakh** deletions in 10 study districts, not the 11
  lakh statewide cancellations.

- **Reframe Santoshi Kumari around what is documented.** The *cancellation* is
  documented (card struck off 22 July 2017; the block development officer confirmed
  the Aadhaar-seeding failure; rations refused for months before). The *cause of
  death* is **officially disputed** — a district team reported malaria, the family
  was reportedly harassed for "defaming the village", and no court has adjudicated
  it. Lead with the documented chain, note the dispute in the same breath. Stating
  "died of prolonged hunger" as uncontested is one search away from being caught,
  and this case is the emotional anchor of the strongest chapter.

- **Replace the Mandela Rules "authoritative gloss" — it is a blog post.** Rule 3 is
  quoted **word-for-word correctly** (verified against A/RES/70/175), and the
  soft-law characterisation is right and quotable from operative paragraph 8 of the
  adopting resolution. But the line offered as "one authoritative gloss" — *"the
  deprivation of liberty is the only permissible restriction imposed by a lawful
  sentence…"* — traces verbatim to a **December 2025 personal legal blog**. Replace
  with **Principle 5 of the UN Basic Principles for the Treatment of Prisoners** (GA
  res. 45/111, 1990), which says the same thing with standing. Also: "normalisation"
  is genuinely UNODC's gloss but is one of five principles, not "the" governing one,
  and the word appears nowhere in the Rules.

- **Fix the collateral-consequences and whistleblower numbers.** USCCR says
  employment-related consequences are *"most (roughly 70%)"*, not "60–70%"; the
  44,000 count is a 2019 snapshot that has drifted (the inventory now says "more
  than 40,000"; an independent 2022 count found 48,229). The ECI figures are
  misstated: 79% and 61% are among employees **who reported misconduct**, not all
  employees, and the 61% (10-country median, 2021) and 46% (42-country, 2020 and
  2023 waves) are **not comparable** — they must not be narrated as a decline.

- **Fix four misattributed quotations.** The Langdell *"study the things to be
  defined, rather than ready-made definitions"* line is **Young B. Smith (1913)**,
  not Langdell — legal historians will catch it instantly. Both anti-utopian quotes
  are **Scruton (2010)**, not "Popper/Scruton"; the second is a secondary-source
  paraphrase, and Popper's argument is structurally different and should be stated
  separately. The *"never an informational or even a computational problem"* line is
  **Nguyen's** QJAE sentence, not Boettke/Candela/Truitt's. The "elaborates too
  little on how to accomplish" complaint belongs to **neither** the Lowy Institute
  (whose review is favourable throughout) nor Global Policy Journal as quoted.

- **Restate Krugman honestly — he prescribes the opposite of concealment.** The
  brief says "Two Cheers for Formalism" prescribes the author's workflow. Krugman's
  step (3), which the brief omits, is *"Publish the intuition, the math, and the
  evidence — all three."* Steps (4)–(5) are an *additional* obligation, not a
  substitute. The stronger and honest framing: **the public nibli repo is what
  discharges Krugman's step (3)** — the apparatus is inspectable by anyone who wants
  it and invisible to everyone who does not.

- **Smaller citation fixes.** Roberts, *The Price of Everything*, PUP — first
  edition **2008** (pbk. 2009). Bregman: **Little, Brown (US) ~288pp / Bloomsbury
  (UK) 336pp**, English edition first from The Correspondent (April 2016), and the
  proposal is a **15-hour** week. HBS formalised the case method in the **early
  1920s** (Donham; "case system" adopted 1922), not mid-century — and the
  decision-forcing-case quote traces only to Wikipedia and governs *instructors*,
  not authors. Cottrell & Cockshott argue **labour-time** calculation is tractable,
  which is narrower than "solve the equations fast enough".

- **Cut or rebuild the Indian-market paragraph — and remove one defamation risk.**
  Lower priority now the audience is global, but if any of it survives: the figures
  come from the **Nielsen India Book Market Report 2015**, superseded by the 2022
  Nielsen BookData/FIP edition (**24,000+ publishers**, trade at **4%** of the print
  market). "Trade books in Indian languages account for roughly half of all sales"
  is **wrong** — the 2015 figure was 45% of *trade* sales only. And calling **Rupa**
  an "ideologically-aligned right-wing press" is unsupported and defamatory-adjacent:
  it is a 1936 general trade house and co-owner of Aleph. Delete that
  characterisation regardless of what else survives.

## book-1 — framing and first chapters

- **Write the single book-2 pointer, at the very end.** book-1 references book-2
  exactly **once**, in the closing note — not in the introduction, because a reader
  on page one has no idea whether they want the machinery, and a forward reference
  reads as an apology for the book they are holding. At the end it reads as an
  invitation to the reader who now wants more. It does two jobs in a short
  paragraph: point the technically curious at book-2, and carry the **one honest
  sentence about the apparatus** — that the design was machine-checked for
  consistency, that the machinery is public, and that book-2 covers it. That single
  sentence is what closes the concealment objection, and it is the only place in
  book-1 where the formalism is acknowledged at all. Keep it plain: no tool names,
  no jargon, nothing a general reader must decode.

- **Reframe the brief's India-first assumptions for a global audience.** The
  research brief recommends foregrounding Bharathi and an India-first publishing
  route; the audience decision overrides that. India material stays as **evidence**
  — Aadhaar/PDS is among the strongest evidence the book has — but it is one case
  among several, not the frame, and every reference needs enough context for a
  reader who has never heard of a ration card.

- **Write the introduction's honesty paragraph early, not last.** Two things belong
  there and both are load-bearing: that a formalisation makes commitments *precise*,
  never *justified* — nothing in logic says the floor should contain expression and
  not water — and that the system proves what is **owed**, not that anything
  **arrives**. Say both plainly or the book is dishonest; saying them is also the
  most disarming move available.

- **Write the chapter where the logic refuses.** Verified on the engine: appending
  `all $x: prisoner($x) -> permits(Appeals, $x).` returns *"[Stratification Error]
  Unstratifiable negation: strongly-connected component containing 'prisoner' ->
  'permits' (negative)"*. A **universal right of appeal cannot be expressed** in
  this constitution — `prisoner` derives behind `~permits(Appeals, ·)`, so the rule
  is a negative cycle. That is not a defeat; it is the strongest chapter in Part V.
  The book's whole register is *state the guarantee, then name the sharp edge where
  it stops*, and here the machine refuses a thing the author wanted and can say
  exactly why. Ship the error message.

  Pair it with the firewall from Chapter 1, because together they are the argument:
  the same stratifier that refuses the author a universal right of appeal is what
  refuses an attacker a heresy law. One mechanism, no special pleading, and neither
  outcome chosen by whoever was writing that day. That symmetry is worth more than
  either half alone.

- **Draft Chapter 1 ("The Floor Nobody Computes") as the proof of method.** Short:
  the eight obligations, and the argument that computing eligibility is where denial
  lives. **Lead with the firewall, not with assert-only-ness.** The old framing —
  "no rule can reach `obligated`, so nothing can retract it" — is true but weak, and
  it is not what actually protects anyone. The real claim is stronger and
  demonstrable on a page: *write a law that jails people for not holding the right
  belief, and this constitution will not compile.* Show the rule, show the
  stratification error, show the same rule loading fine against a right that is not
  on the floor. A reader who has never seen a line of logic can follow that, and it
  is the only place in the book where the machine visibly does something no prose
  could. Then state where it stops — standing and points are still reachable, and
  positive compulsion is untouched. Ship it with its pinned-verdict file **and** its
  negative pins, and use it to prove the harness works end to end before Chapter 2.

## Legacy harvest — everything valuable out of book.md and manifesto.md before they go

Both legacy files are slated for deletion once book-1 and book-2 are written.
Nothing here improves them. The job is to make sure nothing valuable dies with
them — and the deletion must not happen until every bullet in this section is
either landed or consciously dropped.

- **Harvest the References & Data Sources section — it is the single most valuable
  thing in the legacy books.** `book.md` closes with **55 sourced entries**, grouped
  by chapter, each with a primary source and URL, built by a 30-claim fact-check
  against primary sources. That is the seed corpus for book-1's claim registry and
  it would take weeks to rebuild. Port it into the registry format (claim id, value,
  units, source, retrieval date, fetch script) *before* deletion, applying the
  corrections in the research-brief section above, and drop entries whose claims
  book-1 does not make.

- **Harvest the nine historical cases.** New Harmony and the labour exchange, China's
  work-point villages, the kibbutzim, Nyerere's Ujamaa, Chile's Cybersyn, Auroville,
  Mondragon, WIR, Kerala's People's Plan — 2,264 words in "Learning from Those Who
  Tried", researched, sourced, and mechanism-independent. Verified as the only
  genuine chapter-level harvest in the manuscript. They become the spine of Part V's
  five-joints chapter.

- **Harvest the Bharati poem and settle its attribution.** The full poem with Tamil
  original and translations lives in `book.md`'s closing appendix, attributed there
  to *Yoga Siddhi* ("Varam Kettal"), stanzas 4–5. `1.md` attributes the manifesto's
  frame to *நின்னைச் சரணடைந்தேன்* — a string that appears **nowhere** in any
  artifact, and the manifesto's own Part 2 Ch 1 epigraph is நின்னைச் **சிலவரங்கள்
  கேட்பேன்**, which `1.md` appears to have garbled into a title. Confirm the correct
  name with a Tamil-literature source, then decide book-1's use: at most **one**
  framing epigraph — original, plain translation, one sentence on who Bharati was —
  never as structure. The manifesto's sixteen-chapter mapping onto the sixteen lines
  is a real piece of craft; record it before the file goes.

- **Harvest the five bright lines — and check each against the enacted rules.**
  `book.md`'s social-credit chapter states five enforceable bright lines. They are
  the most credible thing in the legacy corpus and book-1 needs them. But bright
  line 2 is already **refuted** by the constitution (see the Article 4 clawback item
  above), and that was found by accident. Sweep all five against the enacted rules
  before porting any of them.

- **Harvest the day-in-the-life vignettes.** `book.md` ~950-957, ~1374-1381,
  ~2397-2404. The legacy books' most human passages, and book-1 currently has no
  narrative register at all. Whether or not the prose survives, the *technique*
  should — a named family carried through food, care, housing and crisis.

- **Carry the floor corrections into book-1 rather than into the legacy files.**
  Three fixes were queued against the manuscripts and should now be written
  correctly *once*, in book-1: state the eight-right floor exactly and once;
  **privacy is not a fundamental right** (encoded as a defeasible right it lands at
  stratum 3 and destroys the single-deprivation theorem — it is Part V argument);
  and define `dwell` in prose as **protective** shelter — weatherproof, ventilated,
  powered, plumbed — which absorbs the water-and-sanitation case at zero cost. The
  franchise is a rule that survives conviction, not a floor right.

- **Then delete both files, in one commit, with the harvest manifest in the body.**
  Not before. The commit message is the record of what was taken and what was
  consciously dropped.

## Hold for book-2 — do not work these here

Parked, so they are not lost when the legacy files go. These become the seed of
book-2's tracker, written from scratch after book-1 ships.

- **The technical backbone material** in `book.md` — local-first/offline-first
  micro-blockchains, Proof of Personhood, quantum-secure and privacy-centric design,
  YAD, the layman's guide. Roughly a third of the legacy book's word count. It has
  **no support in the constitution** — `utopia.nibli` contains no ledger, no
  biometric, no device, no cryptography — which is precisely why it is book-2's
  subject and not book-1's.
- **"Why a blockchain at all?"** — honestly weighing CRDTs and signed logs against
  nibli-store's HLC/tombstone/CRDT-export design. It partly argues against the
  legacy book's central premise, which makes it a strong opening question for
  book-2 rather than a threat to book-1.
- **Replace venture brand names** (union.build, Sui, Fuel, linera) with capability
  requirements plus a dated appendix.
- **The costed transition** — a fiat price tag on a 200k-city baseline, funding per
  phase, and a housing acquisition mechanism (community land trusts vs
  right-of-first-refusal). Needs real fiscal magnitudes; don't fabricate numbers.
- The nibli-side convergence bullets live in nibli's own `TODO.md`.
