# TODO — book-1

**This tracker covers book-1 only.**

The repo is heading for two new books plus a clean deletion:

- **book-1** — the active work, in two parts with a deliberate seam:
  - **Parts I–V — the destination.** What the society IS and how it FUNCTIONS,
    never how to get there. Derived from the constitution and **gated on it**.
    **Jargon-free** — a general reader finishes Part V and stops, and the
    formalism is never mentioned in these parts.
  - **Final part — the method, explicitly optional.** The constitution, the
    derived spine, the compile-time firewall, the evidence/conclusion split, and
    what the logic refused. Labelled as a different kind of reading. The only
    place the formalism appears, and what answers "you built a machine and hid it".
- **book-2** — **how you would actually build it, organisationally and
  technically.** The transition material (MVS, family→village→planet scaling,
  legal collisions, costed transition) *and* the technology stack. Not planned;
  gets its own tracker after book-1 ships. book-1 references it once, at the end.
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

**THE INCLUSION GATE — applies to Parts I–V only.** Those parts describe a
destination, not a route. Before any passage goes in, two tests: (a) does it
describe what the society IS or how it FUNCTIONS — not how anyone gets there? and
(b) does the constitution derive it? A passage failing (a) belongs to **book-2**;
one failing (b) belongs in Part V's explicitly-not-derived section, or in the
opening note, or nowhere. Exactly three things in book-1 are exempt and each is
labelled as such: the opening note, Part V, and the final method part.
Anything about building up, scaling out, phasing in, or persuading anyone is out
of Parts I–V by construction.

The **final part is exempt and inverted**: it is *about* the constitution rather
than gated on it, and it is the one place jargon is allowed. Keep the seam sharp —
if a reader cannot tell they have crossed into a different kind of chapter, the
seam has failed.

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
  `entitled(every person, event { P() })` compiles to a rule with `person` in the
  body, so `P` sits downstream of `prisoner`; any later rule taking `~P` into that
  cone is an unstratifiable negative cycle and is refused. Verified both ways plus
  a non-floor control. You cannot write a law punishing a person for lacking a
  floor right. Where it stops is equally established: `~P -> false` (standing),
  `~P -> lose(Points, ·)`, and positive compulsion `prisoner -> P` all still load.
- The floor is **eight**, spelled `entitled(every person, event { P() })` with the
  rights-holder in x1, enacted in `new-book-plans/utopia-v2.nibli`, with the
  franchise and the isolation marker as rules. Graph: 37 predicates, 16 derived,
  28 rules, max stratum 3, **stratum 3 still exactly `{err, travel}`** — the
  single-deprivation theorem survives. All 51 pins pass; the firewall holds
  (`~believe`/`~meets`/`~eats`/`~secure -> prisoner` refused, `~home` control
  loads); five upstream regression tests pin the mechanism in nibli's CI.
- **All nine gate relations are closed to direct assertion** (Article 0):
  `fit`, `defend`, `false`, `reward`, `become`, `err`, `authority`, `permits`,
  `prisoner`. The three that once carried deliberate ground facts were split —
  institutions assert `public(Court).` and authority derives; relief asserts
  `clear(Nia).` and `permits(Appeals, ·)` derives; Adam is convicted through
  Article 6 rather than asserted. All three exploits are dead and pinned:
  `authority(Pax).`, `permits(Review, Sock).` and `fit(Ruk, Homestay).` are each
  refused at assert time, with complement pins proving the derivations still work.
- The widening hazard is **rule-head position**, not place index and not the
  predicate: `every`/`all` forms widen the protected set, ground facts and `some`
  are inert. It cannot be banned, because the widening *is* the firewall. The
  guarantee is the complement pins, not a compile-time rule.
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

- **DECIDED (2026-07-28): a thin constitutional layer is the duty-bearer.** book-1
  names an agent obligated to provide the floor — one with real taxing and
  inter-community equalisation power, carefully limited. The other two options were
  rejected on grounds worth keeping, because each will be proposed again:
  - **Mutual covenants is inconsistent with the enacted floor.** Verified: the
    constitution has **no concept of membership, community, citizenship or
    residence**, and the floor quantifies over `every person`. Covenants would gate
    it on membership — inventing a `member` predicate and putting an eligibility
    computation *upstream of the floor*. That is exactly the structure the book's
    thesis refuses, moved one level up where it is harder to see.
  - **Naming the gap flinches, and reuses the wrong gap.** The delivery gap is
    honest because nobody has solved provisioning; it is a real frontier. The
    duty-bearer question is answered daily by every welfare state. Declining a
    solved question reads as evasion and spends the credibility Claim C earns.
  - **A duty-bearer does not weaken the design — it is what makes the firewall mean
    anything.** "You cannot write a law punishing a person for lacking a floor
    right" is a constraint on a powerful agent; a firewall with nothing behind it
    protects nobody. The book is not *society without a state*, it is **a state that
    structurally cannot do these particular things**.

  **It is expressible without cost — verified.** A bearer named *alongside* the
  intact floor preserves the firewall in every form tried:
  `owe(State, Provision, every person).`, `all $x: person($x) -> owe(State,
  Provision, $x).`, and a `public(State)` + rule variant. The earlier finding that
  duty-bearer forms destroy the firewall was about *replacing* the floor's shape;
  supplementing it is free. Pick a form, enact it, and pin it.

  **Three things this now obliges the book to do:**
  - **Concede coercion in plain words.** A reader who notices the word being avoided
    stops trusting the rest.
  - **State the social-democracy positioning outright** — the ends are
    social-democratic and the provider is a fiscal agent; the novelty is the
    constraint mechanism, not the absence of a provider. Said plainly, "social
    democracy with extra steps" loses its teeth, because the extra step is a
    compile-time prohibition nobody else has. This belongs in Part V's five joints,
    at the *state* joint.
  - **Bound the power explicitly, and answer the magnet problem** — mobility is a
    guaranteed right, so generous communities attract need. Standard fiscal
    federalism, currently unaddressed. This unblocks the governance-mechanics bullet
    in the KB section, which was waiting on this fork.

- **CONFIRMED (2026-07-28): build Part V on the five-joints scorecard.** Four architectures
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

  **Recommended: the five-joints skeleton, at ~14,500 words — but re-framed for
  the destination-only scope.** The joints themselves survive the narrowing, because
  valuation, rotation, coercion, capture and the state are places a *functioning*
  design breaks, not stages of a rollout. What must change is the framing: not
  "here is what happened to people who tried to build this", which is a transition
  story, but "here are five places a society of this shape fails, and here is
  whether this one holds". The historical cases become evidence about failure modes
  rather than a narrative of attempts. Score this design against those five. It is the only principle
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

  Design signed off by the author. Both open calls were already decided:
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

- **DECIDED: book-1 is titled *Nothing Has to Happen First*.** The subtitle is
  provisional — working version *"Eight things every person is owed, and why no law
  can take them away"* — and should be confirmed once Chapter 1 exists, since a
  subtitle chosen against a real voice survives and one chosen against a plan
  usually does not.

  The title is the thesis in five plain words, taken from the fidelity table's own
  sentence: *…are owed to every person, and nothing has to happen first.* It clears
  every constraint the book carries — it names a destination rather than a route, it
  uses no jargon, it carries the eligibility argument without stating it, and it
  avoids "utopia", which the reception literature identifies as the fastest way into
  the naive-utopianism dismissal and which the legacy book already used.

- **[AUTHOR-GATED] The repo name is now misleading.** `utopia-reimagined` names the
  legacy book, which is being deleted, and neither new book uses the word — book-1
  is *Nothing Has to Happen First* and book-2 is the build-it companion. Not urgent
  and it blocks nothing, but decide before anything is published under the URL: a
  rename costs remote references and clone paths, while leaving it costs a
  permanent mismatch between the repo and everything in it.

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

## The verification harness

**DONE, both halves.** Run the constitution suite with:

```
nibli-pin --kb new-book-plans/utopia-v2.nibli new-book-plans/rights-floor.pins.nibli
```

**62 pins, 0 findings, exit 0.** Use the **release** build of `nibli-pin` — debug is
far too slow for this suite. `--kb` loads the live constitution as a fixture.

The two pin files are different KINDS and both headers now say so. nibli's
`pins/*.nibli` are **mechanism** pins: they inline their fixtures because the
fixture is not the subject. `new-book-plans/rights-floor.pins.nibli` is a **content**
pin: it loads the constitution because the constitution *is* the subject, and
inlining it would certify a copy that then drifts.

Three guards, each of which caught something real on the way in: `:expect-pins` is
an anti-hollowing floor and caught a miscount on the first run; omitting `--kb`
yields 34 findings rather than a silent pass; and an inert `derived_only`
declaration — one placed below the facts it guards — is refused upstream at assert
time rather than merely detected, pinned at `pins/derived-only.nibli:94-106` with
both halves (a late declaration refused, a post-rules declaration accepted, since
derivations are never stored and only asserted facts can make one late).

- **The spine is now generated, and staleness is detectable.**
  `new-book-plans/5-spine-gen.py` owns the computed region of `3-spine.md` and reads
  the constitution directly — including the floor, which `4-strata.py` structurally
  cannot see. Regenerate with
  `python3 5-spine-gen.py utopia-v2.nibli 3-spine.md`; check with `--check`, which
  exits 1 when the document has drifted. Verified against the real failure mode:
  adding a ninth right to a scratch copy makes `--check` fail. **Wire `--check` in
  beside the pin suite** so a constitution change cannot land with a stale spine —
  that is exactly how this document went wrong twice.

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

- **Fix the Article 4 clawback rules — and Chapter 6 is now written against them.**
  Narrowing the contamination rule flips `lose(Points, Cira)` to FALSE and requires
  rewriting the middle third of `book-1/06-clawback.md`. That is a good trade, not a
  cost — but do it deliberately, and re-run the chapter's pins after. Note also that
  "no negative scoring of persons" is a **legacy `book.md`** bright line, not one
  book-1 has adopted; book-1 currently describes clawback as the design has it. This
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

- **Governance mechanics downstream of the duty-bearer fork — now UNBLOCKED.** The
  fork is taken (thin constitutional layer), so these can start. Confront the magnet problem: mobility is itself a guaranteed right, so
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

## Engine-adjacent work

**Nothing here blocks book-1.** The derived-only feature landed, and the
constitution work it exposed moved to the KB section. What is left is optional
upstream cleanup plus one convenience that would make the book-side suite
trustworthy.

- **Close the `obligated`/`obliged` de-swap upstream.** Not blocking book-1 — the
  floor no longer uses either. They are not converses: both from `bilga`, identical
  gloss and template, swap bolted on afterwards, so two interchangeable-looking
  spellings compile to argument-inverted facts. Repair is to drop the swap, give
  `obligated` `obliged`'s place order, and delete the two `nibli-render` overrides.
  It touches the GDPR corpus, and `gdpr.nibli:52` Art 6(1)(c) may be **vacuous** as
  a consequence — query it before deciding whether that line is meant to be live.

- **Give the book-side pin suite a real runner.** The upstream half is DONE:
  `just verify-pins` is in nibli's `ci`, with `pins/rights-floor.nibli` guarding
  the engine mechanism via a deliberately self-contained fixture, and the runner
  self-tests before it is trusted. Nothing further is owed there.
  The book side still needs work. `new-book-plans/rights-floor.pins.nibli` holds
  this constitution's 51 pins and must `:load` the live file — that is the whole
  point, and it is why it cannot simply move upstream where fixtures are inline by
  design. The two files are complements: nibli's guards the *mechanism*, this one
  guards this *content*. Today it runs on a scratch prototype (`kbcheck`) whose
  defects are known and listed in nibli's review: no `:accept`/`:refuse`, so the
  four complement controls and four firewall refusals are still a shell loop rather
  than pins; a stratification refusal is indistinguishable from a syntax typo;
  unpinned queries pass silently; `RESOURCE_EXCEEDED` is pinnable. Either port
  `nibli-pin` to accept `:load`, or rebuild the book-side runner with the same
  directive set. Until then the suite is real but the runner is not trustworthy.

- **[AUTHOR-GATED — a decision, not a blocker] Exact minor-unit arithmetic.** The plans claim any
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
  paragraph: point the reader who now wants to know *how you would actually build
  this* at book-2 — organisationally and technically. **Its old second job is gone.**
  It used to carry the one honest sentence about the apparatus, because the
  formalism appeared nowhere else; the final part now does that far better, by
  showing the machinery instead of alluding to it. Keep the pointer plain: no tool
  names, no jargon, nothing a general reader must decode.

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

- **DECIDED: the chapter order is strictly computed. `3-spine.md` is regenerated.**
  The floor sits at **stratum 2**, not 0 — each floor line compiles to
  `person($x) -> P($x)`, and `prisoner -> person` puts it inside the prisoner cone.
  That is not a defect: it *is* the firewall. The floor is protected **because** it
  is reachable, since being in that cone is what makes `~P -> prisoner` a negative
  cycle. At stratum 0 there would be no protection at all, and the old spine's
  "nothing derives it, so nothing can retract it" had the mechanism backwards.

  Consequences, all now reflected in `3-spine.md`: the first chapter is **"What
  Counts as Evidence"**, not the floor; the floor chapter is **8**, retitled **"What
  You Are Owed"**, and carries the firewall demonstration; the spine is 14 derived
  chapters, gaining "The Vote Conviction Does Not Take"; and the chapter-1 fidelity
  table was rebuilt from scratch, since no row of the old one survived.

  **One concession, deliberate:** a short **opening note** before Part I, explicitly
  non-derived and labelled the way Part V is labelled, so the book does not open
  cold on vocabulary. It claims no derivation and carries no verdicts. This is the
  second sanctioned exception to the inclusion gate, alongside Part V.

- **DRAFTED: Chapter 6, "Clawback"** — `book-1/06-clawback.md`, 994 words,
  `06-clawback.pins.nibli` (13 pins, green). Closes Part II. Written *around* the
  contamination defect rather than after fixing it: Cira is the chapter's centre and
  the chapter states plainly that the rule is not defensible as written. **If the
  rule is narrowed, `lose(Points, Cira)` flips FALSE and the middle section must be
  rewritten** — the pin file says so. Decide which way round you want it.
  Ends on the ceiling rather than a fourth consecutive limit: clawback reaches
  recognition and stops, so the worst the machinery can do leaves the floor,
  liberty and personhood untouched.

- **DRAFTED: Chapter 5, "Voiding"** — `book-1/05-voiding.md`, 1,040 words,
  `05-voiding.pins.nibli` (14 pins, green). Bela (it works), Esa (one is not
  enough), Dev (judging your child voids *you*), Lupo (lying voids *you*), Vex/Tyr
  (the epoch carry). Ends on the two disclosed gaps: only parents are excluded from
  the independence check, so spouses and siblings co-sign freely and the
  conspiracy-of-two is barely a conspiracy; and the sequence discipline is not
  enforceable from inside. Names the limit both chapters have now circled —
  **this society can guarantee what follows from its record, not its record.**

- **DRAFTED: Chapter 4, "The Shield"** — `book-1/04-the-shield.md`, 1,162 words,
  `04-the-shield.pins.nibli` (15 pins, green). Don, Sly and Kel. Don is the closed
  exploit — exposing his own victim bought a shield until the design required the
  exposed party to hold standing. Sly is the deliberate fail-open window, defended
  on asymmetry of harm rather than apologised for. Kel is what closes it. Ends by
  paying chapter 2's bill: the shield attaches to anyone with standing, standing is
  never revoked, so the surface of protective exposures only grows — and whether it
  should be bounded by time is a real question the design does not answer.

- **DRAFTED: Chapter 3, "Who Holds the Pen"** — `book-1/03-who-holds-the-pen.md`,
  1,090 words, `03-who-holds-the-pen.pins.nibli` (14 pins, green). Opens Part II.
  Carries the Sock/Puppet attack as its centre — the hole that let two people who
  were never chosen void an innocent — and closes on the honest boundary:
  everything downstream of selection is closed, selection itself is open, and no
  rule inside the design can reach up to check the election.

- **DRAFTED: Chapter 2, "Standing, and Why It Is Never Revoked"** —
  `book-1/02-standing.md`, 1,174 words, `02-standing.pins.nibli` (12 pins, green).
  Boss carries the chapter: seated, then recalled, keeps standing forever and loses
  every power immediately — and that permanence is what saves Rebel, because a
  recall that stripped standing would retroactively destroy the whistleblower's
  protection. Kept as a separate chapter rather than folded into ch 1: ch 1 is what
  may be *recorded*, ch 2 is who may *act*, and merging them blurs ch 1's single
  argument. Part I is therefore two chapters and the spine stays at 14.

- **DRAFTED: Chapter 1, "What Counts as Evidence"** — `book-1/01-what-counts-as-evidence.md`,
  1,391 words, with its fidelity file at `01-what-counts-as-evidence.pins.nibli`
  (12 pins, green). Verified jargon-free. Two things to settle on it:
  - **Length.** 1,391 words is short for a trade chapter. Deliberate — one argument,
    cleanly — but confirm before the pattern sets, since chapter length compounds.
  - **[AUTHOR-GATED] Voice.** Written in a plain, mostly impersonal register. The
    legacy book was first-person and warm, and the constitution's own commentary
    says "the manifesto voice is the author's to re-weave — I am not ghost-writing
    it." The personal register is yours to add and should go in before the pattern
    sets across chapters.

- **Add `LICENSE-CC-BY` to `book-1/`** with a licence line in the front matter, per
  `LICENSING.md`. Prose is CC-BY-4.0. Fetch the canonical text rather than
  reproducing it from memory.
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
  genuine chapter-level harvest in the manuscript. **Re-point them when porting:**
  book-1 does not tell the story of people who tried to build a better society —
  that is transition. Each case enters as evidence about a *failure mode of a
  functioning design* (how Owen's labour notes mispriced, how the kibbutz handled
  differentiation, where Mondragon's governance held), never as an attempt
  narrative.

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

**RESOLVED:** book-2 is now *how you would actually build it, organisationally and
technically*, so the transition material has a home here alongside the stack. They
belong together — measured across the six transition chapters, tech density is only
5.6–14.1 mentions per 1,000 words and mostly incidental, so the transition material
is the *why and when* and the stack is the *what with*. "When the Pod Meets the
State" already reads as a legal argument with technology as scenery.

- **The transition material** in `book.md` — Part 4 in full (One Person One
  Family; When a Village Joins; Cities, Provinces and Nations; One Planet One
  People), plus "When the Pod Meets the State" and "MVS in Action". ~8,600 words,
  largely organisational, legal and fiscal. This is book-2's spine, not an
  appendix to it.
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
