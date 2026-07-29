# TODO — book-1

**This tracker covers book-1 only.** It is strictly future-facing: a bullet is
deleted the moment it fully lands. History belongs in git.

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
  is that no valuable material is lost on the way out: the 55 sourced references,
  the nine historical cases and the Bharati poem, itemised under **Legacy harvest**
  below — plus the five bright lines, which are swept in the Constitution section
  because four of the five are settled against the enacted rules rather than ported, ending with the deletion commit.

Plain bullets, never numbered. Work the FIRST remaining bullet; cross-reference
items by name. Delete a bullet entirely when it fully lands; update it if only
partly done. Ordered by dependency and leverage, not by chapter order. One item at
a time: do it, verify it, commit it.

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
`new-book-plans/`.

**nibli handoff protocol.** dhilipsiva wrote nibli. When an item is blocked by an
engine bug or a missing KR construct, do not work around it in prose — the bullet
carries a ready-to-paste **HANDOFF PROMPT** for a Claude Code session in
`~/projects/dhilipsiva/nibli`. Hand it over, work the next unblocked bullet, and
resume when it lands.

---

## Already established — re-verify by command, not by hand

Every claim below is reproducible from committed artifacts by one command. Do not
transcribe numbers into this file; run it.

```
./verify.sh            # ~15 min: spine, evidence count, jargon, absences, 271 pins, counterfactuals
./verify.sh --quick    # ~2 s: everything except the pin suite
```

It exits non-zero on the first failure and says which claim stopped being true. **Prefer
it to running any single check by hand** — the checks it carries were each
negative-controlled, and one of them (the jargon sweep as this file used to specify it)
did not catch the leak it was written for.

Use the **release** `nibli-pin`. **Never `nibli-host`** — it loads
`target/wasm32-wasip2/debug/nibli.wasm` by default, built **2026-07-26**, and the newest
release component is **2026-07-23**, while `derived_only` (nibli `b053b77`) and the
`entitled` corpus entry (nibli `a65b398`) both landed **2026-07-28**. Either build
predates both. It silently drops the entire rights floor
and all nine gate closures, then reports a clean run over a constitution it is not
reading. The provenance line that used to sit here named exactly that tool, which
is how a hand-transcribed snapshot passed for a verification.

Two facts no command teaches:

- **A floor line is a compile-time prohibition, not a declaration — and since Article
  1b the prohibition covers the duty as well as the eight rights.**
  `entitled(every person, event { P() })` compiles to a rule with `person` in the
  body, so `P` sits downstream of `prisoner`; any later rule taking `~P` into that
  cone is an unstratifiable negative cycle and is refused. The floor is protected
  **because** it is reachable — at stratum 0 there would be no cycle to close and
  no protection at all. Where it stops is equally established and pinned in
  `book-1/08-what-you-are-owed.pins.nibli`: `~P -> false` (standing), `~P ->
  lose(Points, ·)` (recognition), and positive compulsion `prisoner -> P` all
  still load. The floor blocks punishment for ABSENCE, never manufacture, and it
  reaches `prisoner` only.
- **The widening hazard is rule-head position** — not place index, not the
  predicate. `every`/`all` forms widen the protected set; ground facts and `some`
  are inert. It cannot be banned, because the widening *is* the firewall. The
  guarantee is therefore the complement pins, not a compile-time rule.

The graph counts live in exactly one generated place, `new-book-plans/3-spine.md:17-32`.
`4-strata.py` disagrees with it and is blind to the floor by construction — see the
harness section. Fix while you are next in `utopia-v2.nibli`: `:182` cites the
upstream regression tests at `integration.rs:3228`; they are at `:3475-3571`.

---

## Blocking decisions — nothing should be drafted until these are settled

- **[AUTHOR-GATED] Name the four severity dimensions, then enact them.** DECIDED
  2026-07-29: punishment MAY end, and severity governs the outcome across intent,
  directness, victim plurality and harm kind. **Release landed; the dimensions did not**,
  because none of `intend`, `deliberate`, `direct` or `many` exists in the committed
  corpus and an unknown predicate name is a compile error. Nothing can be drafted until
  the four names are chosen — they define what chapter 1 enumerates.
  **Price it honestly before choosing.** Four dimensions take the evidence list 22 → 26.
  Outcome *tiers* are free — `building(MedSec, $x)` costs nothing because uppercase
  constants never enter the predicate set — but the constant must be digit-free, so
  `Tier1`/`Tier2` are unavailable. **Do not enact `greater`/`less`.** They would work: the
  engine's evaluator returns `None` for non-numeric arguments, so `greater(Killing,
  Insult).` is a plain stored fact that passes the digit ban. But routing each combination
  to a named tier by its own rule needs no ordering at all, which is how Article 6 already
  produces four placement outcomes from two booleans, and the comparison costs a 27th entry
  plus a much harder repair to chapter 10.
  **Two chapters must be narrowed in the same pass, and both are overclaims rather than
  errors.** `01:24` — *"There is no score. No rating, no rank, no tier, no percentile"* —
  should be narrowed to the argument the chapter actually makes one sentence later at
  `01:32`: the record holds no judgment about a person's **character**. It classifies acts;
  it holds no standing verdict on a person. And `10:21`/`10:27` — *"nothing anywhere in
  this society counts anything"*, *"There is no ordering"* — are unqualified whole-society
  claims inside a chapter about recognition; qualify both to recognition, where the ranking
  harm actually lives. `10:112`'s argument survives untouched.
  Combinatorics to watch: three dimensions already give 8 cells and chapter 11 covers 7 of
  them while claiming 4 exhaust it; seven dimensions give 128.

- **[AUTHOR-GATED] Confirm the subtitle — the condition it was waiting on has fired.**
  The title (*Nothing Has to Happen First*) is settled in `CLAUDE.md`. The subtitle
  is still the provisional *"Eight things every person is owed, and why no law can
  take them away"*, held back until Chapter 1 existed. All fourteen chapters now
  exist, so the call is due. One correction first: **"no law can take them away"
  overclaims the mechanism.** The firewall refuses only the *prisoner* route.
  Verified (4 pins, 0 findings): `all $x: person($x) & ~believe($x) -> false($x).`
  and `all $x: person($x) & ~eats($x) -> lose(Points, $x).` both load — a law can
  void your standing and dock your recognition for lacking a floor right; it simply
  cannot imprison you for it. A subtitle Part V has to walk back costs more than a
  duller one that holds.

- **[AUTHOR-GATED] Record three standing rejections so they are not re-proposed.**
  Following the precedent set when the duty-bearer fork was decided — grounds recorded
  in `CLAUDE.md` rather than left implicit — these are worth keeping because each
  will be proposed again by the next reader:
  - **Degree facts on contribution** (`taught_for(Esa, 40y)` and kin). Collides with
    the no-arithmetic result chapter 10 is built on and with the merit-points bright
    lines in `CLAUDE.md` — recognition is a fact, not a quantity, and the material a
    degree would be made of deliberately does not exist. This also answers the old
    exact-minor-unit-arithmetic question: the book wants no quantities, so that ask
    is moot.
  - **A narrative-dystopia second part.** Contradicts the book-1/book-2 split: book-2
    is *how you would actually build it*. A fictional counterfactual is neither the
    destination nor the build, and would put the one non-derived thing in the project
    outside all three labelled exemptions.
  - **"Two pens from different public bodies"** as a strengthening of the dual-pen
    void. **Unexpressible, verified**: `public/1` is one-place over institution
    constants (`:391-393`), no person-to-body relation exists, every Review pen flows
    from the single seating rule at `:407`, and `permits(Court, Gia).` is refused.
    Expressing it means enlarging the evidence vocabulary, which chapter 1 names as
    the softest place to push. The strengthening costs more than the weakness.

- **[AUTHOR-GATED] The repo name is now misleading.** `utopia-reimagined` names the
  legacy book, which is being deleted, and neither new book uses the word. Not urgent
  and it blocks nothing, but decide before anything is published under the URL: a
  rename costs remote references and clone paths, while leaving it costs a permanent
  mismatch between the repo and everything in it.

---

## Prose that is false against the constitution

**Work this section first.** Every bullet here is a sentence in a shipped chapter
that the engine contradicts. All were found by the 2026-07-28 review audit or while
verifying it; none was caught by the 248 green pins, which is itself the argument
for the harness section below.

- **[AUTHOR-GATED] "Standing" names two different predicates, and the manuscript uses
  one word for both.** `authority/1` is answerability and is never revoked; `false/1`
  is the credibility of the record and is destroyed routinely. They are independent,
  not opposite — verified on the unmodified constitution: `? false(Vex). => TRUE`
  alongside `? authority(Vex). => TRUE` and `? permits(Review, Vex). => FALSE`; and
  `? false(Bela). => TRUE` alongside `? authority(Bela). => FALSE`. So voiding takes
  the pen and the record and leaves standing wholly intact. **Chapter 2 is correct
  and needs no change** — every *other* chapter saying "voiding standing" means
  `false/1`. The reader meets the collision before chapter 2 defines the term
  (`01:75` precedes `02:34`), and chapter 4 does it to itself twenty-three lines
  apart: `:91` "Kel's own standing is voided" against `:114` "standing is never
  revoked".
  `authority/1` sense, leave alone: `02` throughout, `03:3`, `03:59`, `04:36`,
  `04:50`, `04:114`. `false/1` sense, needs the new word: `01:75`, `01:85-86`,
  `03:8`, `03:42`, `03:67`, `04:91`, `05:3`, `05:14`, `05:17`, `05:36`, `05:43`,
  `06:3`, `08:70`, `08:77`, `10:52`, `10:59`, `10:84`, `13:13`. A third sense hides
  at `12:22` — "the amendment has no standing" is `false/1` on a proposal.
  Decide the replacement word — `04:92-93` already reaches for "credibility" — then
  reserve "standing" for `authority/1` throughout. Add `? false(Vex). # => TRUE` and
  `? authority(Vex). # => TRUE` adjacent in `02-standing.pins.nibli` so the two senses
  can never re-merge silently. **Land this before the chapter-2, chapter-5 and
  chapter-8 rewrites below** — all three touch sentences containing the word.

- **Chapter 10: the third door is not gated on voiding, and the chapter says it is.**
  `book-1/10-contribution.md:50-68` claims "All three doors close for the same reason:
  a person whose standing has been voided earns nothing" and closes on "putting the
  same condition on all three doors". There is no such condition. Article 3 gates
  teaching and work on `~false` (`:324-325`); the examiner rule (`:333`) gates on
  `~deceive` and `~broken` only. **Verified:** `false(Vex)` TRUE *and* `reward(Vex)`
  TRUE — chapter 5's own voided auditor still earns recognition — and adding
  `judge(Bela, Ivo). capture(Bela, Ivo).` gives `false(Bela)` TRUE, `reward(Bela)`
  TRUE and `lose(Points, Bela)` TRUE together. Both worked reasons at `:58-60` are
  also wrong: `reward(Lupo)` is FALSE for `~deceive` and `reward(Dev)` because Dev
  never captured, neither for voiding. The 12-pin suite is green because
  `10-contribution.pins.nibli:45` pins `reward(Bela) => FALSE`, which holds only
  because Bela examines nobody in the shipped cast.
  Two ways out, and they are different societies: **rewrite the section** to say the
  doors are gated differently — a voided person can still earn by examining other
  people, which is worse than the version in print and worth saying — or **add
  `~false($auditor)` to `:333`** and keep the prose. The guard stratifies (verified,
  loads at 0 errors). Either way the suite needs a pin on a voided examiner, because
  its absence is what let this reach print. Also correct `10:52-53` and any tracker
  prose repeating the claim.

- **Chapter 8 says one person has shelter. Four do — and a second floor right derives
  on the same terms, which breaks chapter 13's headline count.**
  `book-1/08-what-you-are-owed.md:50`: "One person in this society verifiably has
  shelter: Hano." Verified: `? dwell(Hano). => TRUE`, `? dwell(Ruk). => TRUE`,
  `? dwell(Lalo). => TRUE`, `? dwell(Nando). => TRUE`, `? dwell(Bela). => FALSE`.
  `dwell` derives for every *confined* person and nobody else (`:352`, `:355`, `:367`).
  And `expresses` does the same through `:307`: `expresses(Hano/Ruk/Don)` TRUE,
  `expresses(Bela/Cira)` FALSE. So `08:32` ("the same answer comes back for every one
  of the eight") is wrong on two of the eight, and `08:48-54` should read *two*
  exceptions covering seven people each. The chapter's pin file samples **seven of
  eight** floor rights and omits `expresses` entirely, which is why nothing caught it.
  **This reaches chapter 13, the more damaging half.** `13-the-one-thing-taken.md:21-22`
  says of Hano and Jala: "One item. Everything else on both lists is identical."
  Verified false: `expresses(Hano)` TRUE / `expresses(Jala)` FALSE; `dwell(Hano)` TRUE
  / `dwell(Jala)` FALSE; `fit(Hano, Homestay)` TRUE / `fit(Jala, Homestay)` FALSE;
  `err(Hano, Isolation)` TRUE / `err(Jala, Isolation)` FALSE. The lists differ by four
  items and three run the *wrong way* — conviction is the only thing in this design
  that gets you shelter, recorded speech and a placement. That is a sharper version of
  the chapter's own argument, currently mis-stated as a weaker one.
  Rewrite `08:31-34`, `08:48-54` and `13:21-22`. Add `? expresses(Bela). # => FALSE`
  and `? dwell(Ruk). # => TRUE` to chapter 8's pins, and `? expresses(Jala). # =>
  FALSE` and `? dwell(Jala). # => FALSE` to chapter 13's.

- **Chapter 11 claims its four cases exhaust the combinations. They cover seven of
  eight, and the eighth derives no placement at all.**
  `book-1/11-where-people-are-put.md:22-23`. The missing cell is *not severe, not
  domestic, no home*, and the constitution's own cast holds three people in it — Don
  (`:534-538`), Kel (`:547-552`) and Adam (`:452-454`), three of the seven convicted
  people in the file. Verified: `? prisoner(Don). => TRUE`, `? fit(Don, Homestay). =>
  TRUE`, `? dwell(Don). => FALSE`, `? building(LowSec, Don). => FALSE`,
  `? building(HighSec, Don). => FALSE`, `? err(Don, Placement). => FALSE`; same shape
  for Kel and Adam. They are eligible for home confinement and have no home, so `:352`
  never fires and neither facility rule reaches them. The chapter's own opening premise
  — "Somebody convicted has to be somewhere" (`:3`) — is not delivered for three of
  seven. The breach marker is blind by construction: `err/2` keys on *having* a home.
  `err(Don, Isolation)` is TRUE, but it is TRUE for every prisoner, so it is not a
  catch.
  **Correct the sentence first; it needs no ruling.** Say the four cases cover seven of
  eight, name the eighth, and say the design has never been asked where that person
  goes. Add a Don block to `11-where-people-are-put.pins.nibli` pinning all six
  verdicts. The design question itself is parked below under Constitution work.

- **`family/1` means "has a family", not "the offence was domestic" — chapter 11
  glosses it wrong twice.** `11:8-10` says placement follows from "whether the offence
  was severe, whether it was domestic, and whether they have a home", and `:21-22`
  calls Nando's offence domestic. Every rule reads `family($x)` — one place, a property
  of the *offender* (`:351`, `:354`, `:367`, `:368`, `:369`) — and
  `01-what-counts-as-evidence.md:12` defines it that way itself. Nando's whole record
  is `injure(Nando, Opal)`, `judge(Court, Nando)`, `family(Nando)`; nothing says Opal
  is family. Verified: `? family(Nando). => TRUE`, `? family(Opal). => FALSE`,
  `? building(LowSec, Nando). => TRUE`. There is no victim-relation slot in the
  twenty-one entries and adding one is a new entry, not a rewording — verified
  separately, asserting `family(Nando, Opal).` loads clean and changes nothing, because
  the two-place fact is a different relation no rule reads.
  Rewrite `11:8-10` and `11:21-22` to say the routing turns on whether the offender
  *has a family*. That is a weaker and stranger claim worth stating plainly rather than
  smoothing: an offender with no family on record is eligible for home confinement
  however domestic the offence, and an offender who has a family goes to a facility
  however unrelated the victim. Add `? family(Opal). # => FALSE`. **Same line span as
  the exhaustiveness bullet — do both in one pass or the second clobbers the first.**

- **Chapter 9 says the disenfranchisement clause "works". It takes nobody's ballot.**
  `book-1/09-the-vote-conviction-does-not-take.md:73-75`: "Nothing refuses it. **It
  works. Immediately, every convicted person in this society loses the ballot.**" The
  accepted clause is strictly *more* restrictive than the Article 2 franchise rule at
  `:321`, and derivation is monotone, so adding it subtracts nothing. Verified by
  accepting the chapter's own clause verbatim: `:accept all $x: person($x) & mature($x)
  & ~prisoner($x) -> decide($x, Ballot).` → `? decide(Hano, Ballot). => TRUE` with
  `? prisoner(Hano). => TRUE`. The chapter's real result — the clause *compiles*, where
  a floor-shaped one is refused — survives untouched; the sentence claiming it takes
  effect does not. `utopia-v2.nibli:12-17` teaches exactly this: "A permissive rule
  left in place keeps its exploit." The pin file cannot catch it because `:49-50` pins
  only that the rule loads and never re-queries the ballot.
  Rewrite `09:71-79`: the clause is writable, and it bites only if the existing
  franchise rule is repealed alongside it — a two-line repeal, not one, which is a
  marginally better result than the chapter claims and should be stated as such rather
  than as a save. Add `? decide(Hano, Ballot). # => TRUE` immediately after the
  `:accept`.

- **`mature/1` is a silent franchise gate, and chapter 9 says the ballot needs nobody's
  permission.** `mature` has no producing rule anywhere (asserted only at `:511-514`), is
  absent from `derived_only`, and is directly assertable — so a polity disenfranchises a
  demographic by **declining to write adulthood into their records**, passing no rule at all
  and tripping no marker. The constitution's own comment at `:510` concedes the second half
  ("no rule anywhere reads ~mature") while presenting it as a reassurance. Verified:
  `? mature(Cira). => FALSE` and `? decide(Cira, Ballot). => FALSE`; asserting
  `person(Zed). mature(Zed).` gives `? decide(Zed, Ballot). => TRUE`, while `person(Yun).`
  alone gives `? decide(Yun, Ballot). => FALSE` — two writes buy a ballot, one write short
  and there is neither a ballot nor an `err`. So `09:51-53` — "the ballot follows,
  automatically, with nobody's permission required and nothing to apply for" — is true of
  the rule and false of its input; and the Cira passage at `:49-53` rests on reading Cira as
  a child when the record cannot distinguish a child from an adult nobody wrote down.
  Qualify `09:51-53`: the ballot needs no permission *once the record says you are an
  adult*, and that is an asserted fact like any other. Add `mature` to the trust-base list
  below.

- **Chapter 1 must concede that at least four of the twenty-one are findings, not
  observations.** `01:24-33` presents the list as things the world reports and the
  exclusions as "considered and rejected on principle", but `severe`, `deceive` ("someone
  lied"), `family` and `parent` are adjudicative conclusions with no definition and no
  precondition anywhere in the constitution — `severe(X).` moves anyone into high security,
  one `deceive(Rebel, Boss).` jails the file's own whistleblower, and neither has an author
  or a standard. The chapter's argument survives the concession and is stronger for it: the
  claim is not that the twenty-one are raw sense-data, it is that a conclusion cannot be
  written **as a conclusion** — the adjudication still has to happen somewhere and the
  record still has to say who did it. Say that rather than letting a reader find the four.
  Pairs with the `capture` precondition bullet, which is the same problem one level down.

- **Chapter 5 asserts two facts about Koa the constitution does not derive.**
  `book-1/05-voiding.md:16-17`: "Koa **examined** Esa and recorded a finding — a real
  finding, on the record, made by **someone with the credential**." Koa's entire
  presence is `person(Koa).` and `capture(Koa, Esa).` (`:473-474`). Verified:
  `? capture(Koa, Esa). => TRUE`, `? judge(Koa, Esa). => FALSE`,
  `? choose(Electorate, Koa). => FALSE`, `? permits(Review, Koa). => FALSE`. Two of the
  sentence's three clauses are underivable, which the inclusion gate forbids outright.
  Chapter 1 gets the same person right (`01:82`, "Koa **documented** something").
  The consequence is worse than the wording: `? false(Esa). => FALSE` is
  over-determined three ways, so the section's headline claim — "It takes two" (`05:11`)
  — is demonstrated by **no pin in the suite**. Two ways out, not equivalent. Either
  fix `05:16-18` to match chapter 1 — Koa documented, holds no pen, and *that* is the
  first reason nothing moved — which is cheap but changes what the section
  demonstrates. Or add `choose(Electorate, Koa).` and `judge(Koa, Esa).` to the cast so
  Koa is a properly seated single auditor and "it takes two" is carried by the count
  alone, which is what the chapter says it is doing. Either way pin
  `? judge(Koa, Esa).` and `? permits(Review, Koa).`.

- **Chapter 6 tells the reader a voided person still eats; the engine says otherwise.**
  `book-1/06-clawback.md:29-33` says a voided person "still eats. Still has somewhere
  to live. Still learns, still speaks, still keeps company" — and the engine returns
  FALSE for every one of those about Bela, *the same person chapter 8 uses to say the
  opposite* (`08:31-34`). Verified FALSE: `eats(Bela)`, `dwell(Bela)`, `learn(Bela)`,
  `expresses(Bela)`, `meets(Bela)`; only `decide(Bela, Ballot)` is TRUE. Rewrite
  `06:29-33` to the *entitlement* reading and add the pins that would have caught it —
  `06-clawback.pins.nibli` pins the clawback verdicts and nothing about the floor it
  claims survives.

- **Chapter 12 enumerates the three entrenched articles and never says the evidence list is
  not among them.** `12-changing-the-rules.md` names `Art_Floor`, `Art_Person` and
  `Art_Entrench` as the register, all three pinned green — and stops. Chapter 1 closes on the
  evidence vocabulary being the one thing *not* entrenched, and chapter 12 is where a reader
  arrives holding the register that would have protected it. `permanent(Art_Evidence). # =>
  FALSE` is already pinned in chapter 1 and is not re-tested here, so the connection exists
  in the suite and nowhere in the prose. One sentence, connecting the register back to
  chapter 1's list. Cheap, and it is the difference between a reader noticing the gap and a
  reader being shown it — which is the register the whole book is written in. Read the
  vocabulary-entrenchment bullet below first: the honest sentence is that the list cannot be
  entrenched, not that it merely has not been.

- **[AUTHOR-GATED] Rule on whether `person` is the twenty-second entry.**
  `book-1/01-what-counts-as-evidence.md:5-8` ("It has twenty-one entries … they cannot.
  Not *may not*. Cannot. There is nowhere to put it") and `:18` describe a set that
  omits the one atom all eight floor rights hang off. `person/1` has **30** ground
  facts, is absent from the nine `derived_only` declarations, and is directly writable
  — verified: asserting `person(Ghost).` gives `? person(Ghost). => TRUE` and
  `? travel(Ghost). => TRUE`.
  **Why it is not in the twenty-one, precisely.** `5-spine-gen.py:116` computes evidence
  as predicates with **no producing rule**; `person` has one (`prisoner -> person`,
  `:248`), so the generator excludes it despite thirty assertions. The same definition
  excludes twelve other writable heads. Against `derived_only`'s nine names and the
  generated block, the directly-assertable surface is **34**, not 21. That is also the
  honest answer to the reviewer request that chapter 1 justify the number: twenty-one
  counts predicates-with-no-rule, which is not the same set as things-the-world-may-write,
  and it is not a minimality proof.
  Any answer that names a number has to name the right one. **Cost of "twenty-two":**
  nine occurrences across `01:5, :6, :32, :100, :106, :138`, `03:85, :100`, `05:93` —
  and it hands chapter 1 a natural on-ramp to the personhood-roster bullet below.
  **Cost of "deliberately outside the list":** one paragraph in `01:20-33` saying why
  roster membership is not something the world *says about* you, which is a real
  argument but has to be made rather than assumed. Either way `01:102-140` currently
  discloses only the *amendment* vector and should also disclose the *write* vector.
  Do not leave it silently uncounted; add a pin either way.

- **[AUTHOR-GATED] Rule on which of chapter 5's two gaps is the larger — the chapter
  says both, nine lines apart.** `05:81` opens the costs section with "Two gaps, both
  disclosed, and **the second is worse than the first**", and `:91` says of the
  **first** — only parents are excluded from the independence check — that it is "**the
  single largest gap in the accountability machinery**". Mutually exclusive, in the
  chapter that closes Part II. A text check, not an engine one, which is precisely why
  no pin catches it. Cheap once decided: either demote `:91`, or reverse `:81` and
  re-order the two sections. Note the ranking is not stable under this tracker's own
  queue — if kinship widens (below), the kinship gap closes and `:81` becomes true by
  attrition rather than judgement.

---

## Constitution (KB) work

- **Add `~false($auditor)` to Article 4's reward rule.** `:333` is the only one of the
  three minting rules with no `~false` guard; `:324` and `:325` both carry one. The
  fix is one conjunct, the negative edge stratifies (verified), and it makes chapter
  10's headline sentence true. See the chapter-10 prose bullet for the fork — enact or
  rewrite, not both.

- **`lose/2` is a leaf: clawback records a loss and retracts nothing.**
  Test it on the rule BODIES, not with a bare grep — `awk -F'->' '/^[^#]/ && /->/ && $1
  ~ /lose/' utopia-v2.nibli` returns nothing, and the only enacted occurrences are
  `:331` and `:332`, **both rule heads**. (A plain `grep 'lose('` returns three lines,
  the third being commentary at `:92`; and a grep that matches a rule's own head is a
  check that can never fail — see the chapter-8 pin NOTE for the same trap caught live.)
  No rule reads `lose`, so nothing downstream changes when it fires. **Care with the
  witness:** `reward(Bela)` is FALSE in the shipped cast, so Bela alone does not show
  it. Add `judge(Bela, Ivo). capture(Bela, Ivo).` and then `reward(Bela)` and
  `lose(Points, Bela)` are simultaneously TRUE — recognition earned by a person whose
  recognition has supposedly been clawed back. So `06-clawback.md:3` ("what they earned
  goes with it") and `:5-8` describe an effect the constitution does not have.
  The apparent clawback in the shipped cast is entirely the `~false` guards on
  `:324`/`:325` **never minting**, not `lose` **taking**. That makes `lose` the fifth
  member of the "determination, then stop" family, alongside `err`, `travel`, `become`
  and the Article 1b obligation `owe`.
  Derivation is monotone, so nothing can literally retract: the only expressible form
  of "taking away" is a guard on the minting rules, which is the fix above. If a
  downstream consumer is wanted instead, `all $x: lose(Points, $x) -> err($x,
  Recognition).` loads at 0 errors. Rewrite `06:3`, `:5-8` and `:103` to say
  recognition is **never minted** rather than **withdrawn** — the chapter's ceiling
  paragraph at `:98-101` already reaches for the right register, so the cost is three
  sentences, not the section.

- **Guard Article 9's head — one asserted fact voids a *person*.** `:437` is
  `all $m: all $t: adjust($m, $t) & permanent($t) -> false($m).` with **no restriction
  on `$m`**, and `adjust/2` is freely assertable. The single fact
  `adjust(Jala, Art_Floor).` gives, verified: `false(Jala)` TRUE, `lose(Points, Jala)`
  TRUE, `travel(Jala)` TRUE, `decide(Jala, Ballot)` TRUE. No imprisonment — but Jala's
  standing is destroyed and the clawback fires **without** two independent credentialed
  auditors, without `~parent`, without `~deceive`, without a clean epoch. Article 4's
  whole apparatus is defeated by one write, because Article 9 reuses `false/1` as its
  amendment-invalidity proxy (`:432-434`) and never restricts the reused head to
  amendments. **The fix is free and verified**: appending `& suggest(Assembly, $m)` to
  `:437` restricts the head to docketed proposals, uses no new vocabulary, and
  regresses nothing — `false(Jala)` FALSE, `false(Amend_Floor)` TRUE,
  `become(Amend_Floor, Law)` FALSE, `rights-floor` 75/75 and chapter 12 14/14 still
  green. Splitting amendment invalidity onto its own predicate is the cleaner
  alternative and costs a corpus name. **Do this before the shield fix below**, which
  couples the shield to `false/1`.

- **`clear/1` is a one-fact conviction nullifier.** `clear` appears twice: `:418`
  (`all $x: clear($x) -> permits(Appeals, $x).`) and `:494` (Nia's ground fact). No
  precondition, no author, no guard, no `derived_only`. Asserting `clear(Adam).`,
  verified: `permits(Appeals, Adam)` TRUE, `prisoner(Adam)` **FALSE**,
  `expresses(Adam)` FALSE, `travel(Adam)` TRUE. `prisoner(Adam). # => TRUE` is a pinned
  verdict at `rights-floor.pins.nibli:186`, and one write flips it. Note the asymmetry:
  the Sock/Puppet void takes six writes, springing a convict takes one. Fix: derive
  relief from an adjudication rather than a bare flag — `clear($x) & judge(Appeals, $x)
  -> permits(Appeals, $x)` is verified to stratify and needs no new vocabulary. Until
  it lands, `03:83-88` should say plainly that nothing constrains who records it.

- **Rename the Article 6 `dwell` head — one atom is doing two jobs, and it blocks the
  `err/2` repair.** Every rule producing `dwell` requires `prisoner` (`:352`, `:355`,
  `:367`), and the Article 1 floor line at `:236` produces nothing — verified,
  `entitled(Bela, event { dwell() })` is TRUE while `dwell(Bela)` is FALSE. So
  `dwell(Lalo)` does not mean "Lalo is owed shelter"; it means "Lalo is housed at
  HighSec", and one atom carries both *entitled to a home* and *in a cell*. Free to
  fix, and a hostile reviewer finds it in an afternoon. Rename the placement head to
  `placed`, or fold it into `building`, and add the asserted counterpart the `err/2`
  fix needs. Six pinned verdicts move with it —
  `08-what-you-are-owed.pins.nibli:33,38`, `11-where-people-are-put.pins.nibli:19`,
  `13-the-one-thing-taken.pins.nibli:39`, `rights-floor.pins.nibli:47,82` — and so does
  `08:50`.

- **Fix `err/2` — the placement alarm has never once fired correctly.** `:360` reads
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)`, which tests *having a home*,
  not *having been placed at home*. Verified: it fires on Ruk and Lalo, both routed
  correctly to `building(HighSec, ·)`, and on nobody misplaced — two false positives,
  zero true positives, on the entire cast. An alarm with that record is worse than
  none. The fix is **not** "key it on `dwell`" — `:352` already requires `fit`, so a
  marker over the derived placement atom could never fire. The marker can only fire on
  an ASSERTED placement, so give the world a way to report one: a new asserted relation
  for "X was put at Y" (name from the committed alias corpus), checked against derived
  `fit`. That is Article 0's own evidence/conclusion split applied to placement, and it
  is the same repair as the `dwell` rename — **do that one first**. Repairing it flips
  `err(Ruk, Placement)` and `err(Lalo, Placement)` FALSE, so three files move in the
  same commit: `rights-floor.pins.nibli:78,80`,
  `11-where-people-are-put.pins.nibli:52-58`, and "The alarm that does not work" at
  `11:50-81`, written against the defect on purpose. That rewrite is the intended
  outcome.

- **Mark confinement without conviction.** Nothing makes `building` derived-only:
  assert `building(HighSec, Rebel)` and no rule objects — no `injure`, no
  `judge(Court, ·)`, so `prisoner(Rebel)` is FALSE and `travel(Rebel)` stays TRUE. The
  constitution certifies as free a person it is holding. The prescribed rule was run
  verbatim and both fires and stays quiet in the right places:
  `all $x: all $f: building($f, $x) & ~prisoner($x) -> err($x, Confinement).` Use a
  third `err` flavour rather than reusing `Placement`, matching `err(_, Isolation)` —
  the audit surface stays one predicate while each breach stays separately queryable.
  Highest value-per-line in this section.

- **[AUTHOR-GATED] Confinement is a location and nothing else — decide whether the design
  says anything about conditions.** `building/2` is a bare placement fact: the three rules
  that produce it (`:354`, `:368`, `:369`) name a facility and stop, and there is no
  vocabulary anywhere for conditions, visits, who may enter, what may be done, or how long
  — `grep -niE "visit|condition|treat|enter|guard|inspect|duration|term"` over the enacted
  lines returns nothing. The only rule that looks at a confined person's treatment at all is
  the isolation marker (`:365`), which is the one that fires on every prisoner and therefore
  says nothing about any of them. Three reviewers reached this independently and rated it
  high or critical.
  **State the position precisely before deciding, because the obvious reading is wrong.**
  The floor *does* reach prisoners — Article 1 plus `prisoner -> person` (`:248`) is exactly
  the chapter-7 result — so a confined person is entitled to all eight rights, and nothing
  in the design permits a cell that starves someone. What is missing is one level down:
  entitlement binds the society, and nothing binds *the facility*. That is the same
  owed-versus-delivered seam the book already discloses, arriving somewhere a reader feels
  it much harder. Either add the vocabulary — which enlarges the evidence list and needs the
  `capture`-precondition decision first, since both are about who may do what to a person
  under authority — or say plainly in ch 13 that the design fixes where a convicted person
  is and says nothing about what happens there. Do not leave it unsaid; "punishment deprives
  exactly one thing" is a much weaker claim if the cell is unconstrained.

- **Write the fact-write trust base as a file-level section — Article 0 closed half of
  it.** `:51-59` now declares nine relations `derived_only` and direct assertion of
  each is refused. What Article 0 did **not** do is remove the write surface; it moved
  it one step back, and every headline attack is alive under a new spelling.
  *Assertion side*, all verified: `public(Pax).` re-derives `authority(Pax)` and reopens
  E1a verbatim (`defend(Don)` TRUE, `prisoner(Don)` FALSE); `clear(Adam).` empties a
  conviction; six ordinary writes reproduce the entire Sock/Puppet void **after** the
  Article 0 closure (`permits(Review, Sokk)` TRUE, `false(Vict)` TRUE,
  `lose(Points, Vict)` TRUE — and `person(Vict)` FALSE, so the victim is voided and
  docked without ever being given a personhood fact); `broken(Court).` is a universal
  amnesty; `rotten(X).` is a single-writer universal void; one `deceive(Rebel, Boss).`
  jails the file's own honest whistleblower; `severe(X).` moves anyone into high
  security.
  *Deletion side*, recorded nowhere, and it is the worse half. Both routes into
  standing are bare asserted facts, and the chapter suites turn out to be a deletion
  detector for free:
  ```
  # public(Court). deleted        04-the-shield.pins.nibli: 15 pins, 3 findings
  ✗ "authority(Court)." TRUE→FALSE  ✗ "defend(Sly)." TRUE→FALSE  ✗ "prisoner(Sly)." FALSE→TRUE
  # choose(Electorate, Boss). deleted   02-standing.pins.nibli: 12 pins, 4 findings
  ✗ "authority(Boss)." TRUE→FALSE   ✗ "defend(Rebel)." TRUE→FALSE  ✗ "prisoner(Rebel)." FALSE→TRUE
  ```
  Rebel — the file's own honest whistleblower, and the whole of chapter 2's argument —
  is jailed by deleting one line. Fix: regenerate the enumeration from
  `grep derived_only new-book-plans/utopia-v2.nibli` rather than editing a list in
  place — nine relations are closed, everything else is open — and record **three**
  undefended classes, not one. **Assertion**, at minimum `public`, `clear`, `choose`,
  `mature`, `person`, `show`, `injure`, `judge`, `capture`, `broken`, `rotten`,
  `deceive`, `severe`, `family`, `parent`, `teaches`, `work`, `home`, `suggest`,
  `approves`, `adjust`, `permanent`. **Deletion**, `person` first, then `permanent`,
  `severe`, `public`, `choose` — and note Article 1b added a fourth institution fact,
  `public(State).` at `:304`, the sole route to `authority(State)` via `:394`, so one
  deleted line makes the duty-bearer unexposable — the file discloses this class for `permanent()` alone,
  at `:442-446`. **Vocabulary**, per the bullet below. Prose consequence, and it is the
  reason this is not only a KB item: `03-who-holds-the-pen.md:100-103` tells the reader
  the Sock/Puppet hole is closed, and it is closed only against *forged credentials* —
  two `choose(Electorate, ·)` writes still seat the puppets and the credential derives.
  Rewrite it to name the cost in **writes** rather than in elections.

- **The evidence vocabulary cannot be entrenched — disclose it instead of patching it.**
  The threat is real and the book prints it at `01:133`, but the old prescribed fix was
  measured and does not close it. `permanent(Art_Evidence).` was applied verbatim and
  run: it kills an amendment that DECLARES that target and kills nothing else.
  `adjust` is self-declared by the proposer (`:437`), so an amendment naming no target
  enacts (`become(Amend_Sneak, Law)` TRUE) and one naming a harmless target enacts too
  (`become(Amend_Lie, Law)` TRUE) — and widening the vocabulary needs no amendment at
  all: `dangerous(Esa).` asserts straight into the store and no rule sees it happen.
  Entrenchment guards targets a proposer admits to; the vocabulary is not a target, it
  is the store. Fix: drop the `permanent(Art_Evidence)` idea, record the vocabulary as
  the third undefended class above, and take the real closure as a nibli handoff.

- **Guard the personhood roster — one deletion defeats all eight rights, and the
  obvious repair only renames the target.** `person` has **30** asserted facts and
  exactly one producing rule, `prisoner -> person` (`:248`), so the only non-assertion
  route into rights-bearing status is being imprisoned. Verified by deleting `:455`
  `person(Bela).` and changing nothing else: `entitled(Bela, event { eats() })`,
  `{ dwell() }` and `{ believe() }` all flip TRUE→FALSE, `travel(Bela)` and
  `decide(Bela, Ballot)` flip TRUE→FALSE, no `err` fires anywhere, and
  `become(Amend_Mint, Law)` stays TRUE — Article 9 entrenches rules, not facts, so it
  never notices. Article 1b follows the roster out of the door: `owe(State, Provision,
  Bela)` flips TRUE→FALSE in the same deletion, so the bearer stops owing the person at
  the instant they stop being one. The sharp part: `false(Bela)` and `lose(Points, Bela)` stay TRUE.
  **De-personing strips every right and leaves every sanction running.** Do **not**
  reach for `all $x: human($x) -> person($x).`: it renames the roster rather than
  closing it (delete `human(Bela)` and the run repeats), and the breach marker meant to
  accompany it can never fire, because with that rule in force `person` always derives.
  No in-snapshot rule can tell a deleted roster entry from one never written. This is
  the deletion class above, and `person` is its first entry: disclose it as a
  cross-epoch proof obligation over the fact store, and stop looking for a rule.

- **Close `entitled` *and* `owe` — the floor's own two relations, and the gates Article 0
  forgot.** Article 1b added the second: `owe` is not among the nine `derived_only`
  declarations and its head is a rule, so the relation is open to direct assertion exactly
  as `entitled` is, and forging `owe(State, Provision, Sokk).` forges the record of what is
  owed to a non-person. Verified: `entitled(Sokk, event { eats() }).` asserts cleanly onto the live
  constitution and answers TRUE while `? person(Sokk). => FALSE`. Nothing reads
  `entitled`, so this forges no downstream verdict — it forges the *record of what is
  owed*, which is the one thing the floor is. The obvious fear is unfounded and was
  checked: closing the relation does **not** refuse the floor lines at `:234-247`,
  because floor lines compile to rules and `derived_only` refuses only ground
  assertions. With `derived_only("entitled").` added: the floor still derives, the
  firewall still refuses the heresy law, the non-floor control still loads, and the
  forgery is refused. Article 0 goes from nine closed relations to ten.

- **[AUTHOR-GATED] Decide whether the shield closes against the person or the
  exposure.** `:383` scopes `~deceive($w, $o)` to the **pair**, and the rule is
  satisfied by *any* qualifying pair, so a deceit finding on one exposure is defeated
  by making a second. Verified with REX, a Kel clone who also exposed the Review body:
  `deceive(Rex, Court)` TRUE, `false(Rex)` TRUE, `defend(Rex)` TRUE, `prisoner(Rex)`
  FALSE. That falsifies `04:95-97` — "it resolves hard" — which is true of **one**
  exposure; Kel closes only because Kel made exactly one. The three per-subject `show`
  pins cannot catch a per-pair defect.
  **Bounded, which is what makes this a decision and not an emergency.** One further
  deceit finding per exposure restores conviction (verified: `defend(Ryo)` FALSE,
  `prisoner(Ryo)` TRUE), and the target set is finite in-snapshot at nine — four
  `public` bodies (Article 1b added `State`) plus five seats. Linear denial-of-service on the Review queue, not an
  unbounded bypass.
  **The person-scoped fix compiles and costs nothing in the suite**: appending
  `& ~false($w)` to `:383` gives `defend(Rex)` FALSE, `prisoner(Rex)` TRUE, with
  `defend(Sly)` and `defend(Rebel)` intact and both suites green. The prescribed
  `sham($w)` variant does **not** compile — `sham`, `deceitful` and `answerable` are
  all absent from the corpus, so that route is a lexicon ask.
  **Its cost is the decision.** `~false` closes the shield against anyone whose standing
  is voided for *any* reason, so one bad-faith finding costs a genuine whistleblower
  their future protection — precisely the asymmetry Article 7's polarity note exists to
  defend. And `false/1` has five producing rules, one of which is Article 9's
  unrestricted head — so **do not close against the person until that is guarded**.
  Separately and regardless of the fork: `show/2` has no derived-only status, no
  precondition, no author and no cost, and it is absent from the trust base.
  **Warning:** adding `person($w)` to this rule is rejected *atomically* — see the
  Article 7 landmine bullet.

- **[AUTHOR-GATED] Decide where a homeless, non-severe, non-domestic convict goes.**
  See the chapter-11 prose bullet for the evidence. **The obvious fix does not close
  it, and that is the decision.** Adding
  `all $x: prisoner($x) & ~severe($x) & ~family($x) & ~home($x) -> building(LowSec, $x).`
  is accepted and gives Don a facility, but not shelter — verified:
  `building(LowSec, Don)` TRUE, `dwell(Don)` **FALSE**, `err(Don, Placement)` still
  FALSE. `dwell` has exactly three producing rules and every one requires a home,
  severity or family, so a facility-placed homeless convict is housed by the placement
  machinery and owed nothing by the floor. Decide both halves: which facility, and
  whether `dwell` should follow from `building` at all. If it should, chapter 8's
  shelter arithmetic moves with it. Batch with the `err/2` repair — same section of the
  same chapter.

- **[AUTHOR-GATED] Decide whether `err` feeds an obligation — chapter 14 presents the
  audit's powerlessness as structural, and it is a choice.** `14:92-100` argues the
  marker cannot be read *because* of where it sits, closing on "The audit is powerless
  because it is uncorruptible, and uncorruptible because it is powerless." That is an
  argument from stratification, and the stratifier does not make it. Verified:
  `:accept all $x: err($x, Placement) -> obliged(Review, $x).` is accepted **and
  derives** — `? obliged(Review, Ruk). => TRUE`. What the stratifier would refuse is a
  rule taking `~err` back into the cone `err` depends on — far narrower than "nothing
  can follow from it".
  **Two costs, both measured.** (1) It breaks a stated invariant: appending the rule
  and running `5-spine-gen.py --check` gives `3-spine.md is STALE` (exit 1);
  regenerating shows 46→47 predicates, 23→24 derived, 39→40 rules, and stratum 3 going
  from `{err, travel}` to `{err, obliged, travel}`. A new derived relation at the top
  stratum is book content under the inclusion gate. (2) The spelling is a trap:
  `obligated` and `obliged` are argument-inverted twins of the same gismu, and **both
  spellings accept the rule and answer TRUE on the surface form** — so whichever you
  write *looks* right, and one of them says the prisoner owes the duty to the Review.
  Answering yes promotes the `obligated`/`obliged` de-swap from optional upstream
  cleanup to a blocker.
  Three ways out: enact the obligation and rewrite `14:92-100`; keep the design and
  rewrite those lines to say the powerlessness is **chosen**, showing the accepted rule
  as proof it could be otherwise; or leave the prose and be wrong. Either of the first
  two wants the `:accept` added as a pin, and it would be a third exhibit for the
  method part's "here is what the logic refused, and here is what it permitted".

- **Article 3 mints for the *teacher*, so Cira has no recognition to lose.** `:324`
  heads on `$teacher` and nothing anywhere mints for a student. Cira's only base facts
  are `person(Cira)` and being the *object* of two `teaches` facts. Verified:
  `reward(Cira)` FALSE, `reward(Fin)` FALSE, `lose(Points, Cira)` TRUE, `person(Fin)`
  FALSE. So `06:49-53`, `:68` ("Esa was never voided, so Fin keeps everything" — Fin
  has nothing, and is not even on the personhood roster) and `:103` all describe a
  transfer the constitution never derives. What actually happens is stranger and, for
  the chapter's own argument about collective punishment, **stronger: Cira is docked
  for recognition Cira never had.** It also empties the prescribed remedy below —
  "rewards actually derived from the fraudulent teaching" is the empty set for every
  student in the design, so that narrowing collapses into deleting the rule. The fork:
  either give students a minting path (a new article, and with it the claim that being
  taught is itself a contribution) or rewrite `06:49-53`, `:68` and `:103`.

- **Decide the Article 4 clawback question.** The two rules are `:331`
  (`false($f) -> lose(Points, $f)` — docks the wrongdoer, fairer, still a subtraction
  from a person's record) and `:332` (`teaches($t,$s) & false($t) -> lose(Points, $s)`
  — docks a **student** for a teacher's fraud: negative scoring, of a person, who did
  nothing). Verified: `lose(Points, Bela)` TRUE, `lose(Points, Cira)` TRUE. Legacy
  `book.md` bright line 2 — *"No negative scoring of persons"* — is contradicted by
  both, and note it is a **legacy** line recorded in `CLAUDE.md` under historical
  decisions, not one book-1 has adopted. Decide which side gives: either the bright
  line narrows to "no subtraction except by due process for one's own adjudicated
  fraud" and `:332` is deleted, or the clawback rules go and sanctions reach perks
  only. Do not leave both in print. Narrowing flips `lose(Points, Cira)` FALSE and
  rewrites `06:40-82`; that is the intended trade and `06-clawback.pins.nibli:5-9`
  already records it. Read the Article 3 bullet above first — it changes what
  "narrowing" can mean.

- **The delivery gap can be closed by fiat and nothing objects — record the *rule*-write
  trust base.** All eight floor predicates are rule-writable heads. Verified:
  `all $x: person($x) -> P($x).` loads at **0 errors** for every one of the eight, and
  every floor query flips TRUE. The sharp part: the same fiat **silences the isolation
  audit marker** (`err(Hano, Isolation)` FALSE), so the one instrument that would have
  noticed goes quiet in the same edit. **Article 0 cannot close it** — verified against
  a copy with `derived_only("eats").` inserted: the direct assertion is refused *and*
  the fiat rule still loads, with `? eats(Adam). TRUE`. `derived_only` closes assertion,
  not rule heads, and a KB-owned vocabulary declaration is unshipped. So there is no
  compile-time guard available and the fix is disclosure: state in the constitution's
  commentary, and in the provisioning bullet below, that any provisioning layer must
  distinguish a delivery **record** — an evidence fact about something reaching a
  person — from a derived legal fiction. Otherwise the most credibility-buying
  admission the book has is one line and a green suite away from being erased.
  **Article 1b raised the stakes rather than lowering them.** Re-verified with the
  duty-bearer in force: the eight fiat rules still load, every actuality still flips
  TRUE, `err(Hano, Isolation)` still goes FALSE — and `owe(State, Provision, Bela)` is
  TRUE throughout, because nothing reads `owe`. So one edit now yields a constitution
  reporting a named debtor *and* every actuality satisfied: it reads as a discharged
  obligation rather than an undisclosed gap.

- **[AUTHOR-GATED] Article 1b's obligation is contentless — decide whether the bearer owes
  *the eight* or owes an opaque token.** `Provision` occurs exactly once in the enacted
  lines, at `:303`, and nothing anywhere connects it to `secure`, `eats`, `dwell`,
  `healthy`, `learn`, `expresses`, `believe` or `meets`. So the constitution says a body
  owes *something* to every person and never says what. Caught while re-verifying the
  chapter: the first draft of `08-what-you-are-owed.md:93` said "The eight things are owed
  by a public body", which the design does not derive; the sentence has been narrowed and
  the gap is now disclosed in the chapter's own "does not buy" list, but disclosure is not
  a fix. Two ways, and they are different designs. **Enumerate** — eight rules of the shape
  `all $x: person($x) -> owe(State, Eats, $x).` — which makes the obligation say what it is
  about, costs eight new constants in the evidence vocabulary (the file's own named threat),
  and needs the firewall re-checked on each. Or **keep the single token** and say plainly in
  Part V that the design names a debtor without specifying the debt, which is defensible
  only if it is stated rather than discovered. Do not leave the chapter carrying the
  disclosure while the tracker carries no decision.

- **Grow the provisioning layer, or write Parts I–V to stop where they stop.** Of eight
  floor rights, six have no rule of their own (`eats`, `healthy`, `secure`, `learn`,
  `believe`, `meets`, all FALSE for everyone) and the two that derive — `dwell`,
  `expresses` — derive only for prisoners. **Article 1b named the bearer and moved none
  of it**: verified, `owe(State, Provision, Hano)` and `authority(State)` are both TRUE
  while every one of those six stays FALSE for every person in the cast. The obligation
  layer is now complete *and attributed*; the delivery layer still does not exist. Either build one or state that Parts I–V stop at
  entitlement. Keep it visible in the prose either way; it is the single most
  credibility-buying admission the book has.

- **Document Article 7's stratification landmine — the note is missing and the recorded
  mechanism is wrong.** Article 7 (`:371-397`) carries no stratification note. Adding
  `person($w)` to the shield rule at `:383` is the most natural tightening anyone would
  reach for, and **both** ways of making that edit fail — differently, which is the part
  worth writing down. Verified:
  - **Edited in place**: the rule is dropped and nothing replaces it. `nibli-pin`
    returns `HARNESS ERROR (exit 2) — pins not trustworthy`, so every chapter suite
    touching `defend` or `prisoner` stops meaning anything until it is reverted.
  - **Added alongside the original**: the tightened copy is dropped and the *permissive
    rule stays in force* — `defend(Sly)` TRUE, `prisoner(Sly)` FALSE, `defend(Rebel)`
    TRUE all still pass, with one finding logged. Exactly the "a permissive rule left in
    place keeps its exploit" failure the v0.2 header warns about at `:12-17`, now
    reachable through the stratifier rather than through oversight.
  Neither is silent — the engine names the cycle precisely. Write the note against what
  it actually does and drop the "silently vanishes" framing.

- **Resolve the polarity contradiction between Articles 6 and 7.** Article 7's shield is
  fail-**open** toward protection and defends the choice explicitly at `:376-382`.
  Article 6's `~permits(Appeals, $offender)` (`:348`) is fail-**closed** against
  protection and gives no reason at all. Since v0.3 relief is an asserted `clear($x)`
  feeding a derived `permits(Appeals, ·)`, so the *absence* of a granted relief is what
  convicts. Same file, opposite defaults on the absence of a finding, one justified and
  one silent. Fix: either give Article 6 the same explicit polarity note, or separate
  standing-to-seek-review from a granted relief that stays the sentence, or require an
  affirmative exhaustion fact for conviction. **Do not re-open the fail-open window in
  the chapter** — `04:54-81` defends the choice and `:120-124` names the cost outright.

- **[AUTHOR-GATED] Decide whether the shield's exposure surface is bounded by time.**
  `authority` comes from `choose(Electorate, ·)` and `public(·)`, neither of which ever
  expires, so the set of people whose exposure buys a defendant the fail-open window
  only grows: everyone the electorate has ever seated stays on it permanently, and a
  defendant a century from now can reach back and open the window. The constitution has
  no in-snapshot time, so a recency bound is expressible only as another asserted fact,
  which lands it back in the fact-write trust base. **Settle the person-versus-exposure shield fork first** — the bullet above, where one
  deceit finding is defeated by making a second exposure —
  it may reduce the pressure to nearly nothing. Then either bound the exposed conduct
  by epoch, or decide the growth is accepted and defend it in Part V.

- **Give `rotten` — and `capture` and `judge` — an expungement path. URGENT: release
  landed and this did not, so the asymmetry is now live in print.** A single void is
  perpetual and compounds, with no route back, while a conviction can now be finished.
  That makes losing your standing the harshest sanction in the design — harsher than
  imprisonment — which inverts `02-standing.md:41-42` (*"This is the only thing in the
  entire society that is protected that way. Everything else can be lost"*) and sits
  badly beside `10-contribution.md:50` (*"Nothing to earn it back with"*). The author
  decided on 2026-07-29 that both halves are designed together; only the first half
  shipped.
  **The shape is known and cheap**, because it is the shape release used: an asserted
  expungement fact as a `~<expunged>` body conjunct on the multi-sig rule (`:330`) and on
  `rotten -> false` (`:412`). Both are safe — the predicate is stratum 0 and `false` is
  stratum 1, so no cycle. **Do not** put `~false` in a `false`-headed rule; the file
  records that exact attempt failing as E2 at `:24-26`. Costs one more evidence entry
  (22 → 23) and the nine prose sites move again, so consider landing it in the same pass
  as the severity dimensions rather than alone.
  Worth framing in the book as forgiveness being a *right* rather than as a bug fix.

- **Put a precondition on `capture`.** `capture($a, $audited)` has no precondition
  anywhere: any two Review-credentialed people can void any person for no stated
  reason, and the book never admits it. Needs one design decision — which predicate
  carries "grounds", since adding one enlarges the evidence vocabulary — after which
  the guard is a body conjunct. Pair with an epoch expiry on `capture` and `judge`.

- **Widen kinship beyond `parent/2` — the fix is available today, and it is not free.**
  Article 4's independence check names one relationship (`:330`), so spouses and
  siblings co-sign. Verified: two Electorate-seated siblings void a stranger —
  `false(Targ)` TRUE. **Not blocked on the engine**, as the old wording implied:
  `married` (speni), `brother` (bruna) and `sister` (mensi) are already in the committed
  corpus. Verified fix — appending `~married`/`~brother`/`~sister` in both directions to
  `:330` loads at 0 errors, flips `false(Targ)` FALSE, and leaves `false(Bela)` and
  `false(Lupo)` TRUE. **The cost is what needs deciding.** It takes the evidence
  vocabulary from 21 entries to 24, and enlarging it is the quietest way to capture a
  system — the file's own threat model. It also falsifies two shipped passages: `01:3-18`
  counts the list at twenty-one and calls it exhaustive, and `05:89-93` explains the gap
  as the record having "no way to say that two people are married", which the corpus
  refutes. Land the rule and both chapters together, or ship the gap and rewrite
  `05:92-93` to say the design has not *admitted* the vocabulary rather than that it
  *cannot*.

- **Check each governance item against what the rules can express, before any prose.**
  Parts I–V are gated on derivation, and the constitution has no predicate for a
  community, a transfer, a tax, or a term of office — so none of the following is
  derivable today and all of it is constitution work first. In dependency order:
  - Recall is one asserted `broken(·)` fact (`:529`, consumed at `:407`) — at-will, no
    threshold, no administering body, no term. Replacing it also rewrites `02:55-59`
    and `03:53-60`, which describe it as is.
  - The magnet problem: mobility is derived at `:308` and there is no community concept
    at all, so "generous communities attract need" cannot currently be *stated*, let
    alone answered. Standard fiscal-federalism territory; it needs vocabulary first.
  - Justice material: standards of proof, proportionality, an appeals path independent
    of the recognition apparatus, and who inspects placement under Article 6.
  - Portability of entitlements, so exit from a hostile community is not destitution —
    blocked on the same missing community concept.
  Every one of these enlarges the evidence vocabulary. Price that in rather than adding
  predicates one at a time.

- **Sweep the five legacy bright lines against the enacted rules — only one ports.**
  `book.md:2277-2290` states them. Checked: **BL2** ("no negative scoring of persons")
  is refuted — `lose(Points, Cira)` derives TRUE — and the decision it forces lives at
  the clawback bullet above. **BL3** ("merit never weights votes") survives vacuously:
  there is no arithmetic anywhere in the enacted lines, so weighting cannot be written.
  **BL4** (portability and exit between pods) and **BL5** (minimal data on-chain) are
  pod-and-tech-stack material and belong to book-2. **BL1** is the one to port and it
  must be narrowed: the floor is unconditional *above* `person($x)`, but `person` is 30
  asserted facts with one producing rule, so personhood **is** an enrolment — say that
  plainly, or BL1 lies in book-1 the way BL2 lies in `book.md`.

---

## The verification harness

- **Extend `verify.sh` as the book grows — the runner shipped, the discipline is keeping it
  honest.** `./verify.sh` at the repo root; `--quick` skips the pin suite and runs in about
  two seconds. It checks, first-failure-wins: the spine is regenerated; the evidence
  vocabulary reads 21; no formalism has leaked into a derived chapter; the five absence
  claims still hold; there is no arithmetic in the constitution; the pin suite is green and
  the number it ran equals the sum of `:expect-pins` across the fifteen files; and the three
  counterfactual fixtures still prove what the book says they prove.
  **Every check was negative-controlled before it was trusted, and one failed the control.**
  The tracker's original jargon pattern (`stratum|strata`) does **not** match *stratifier* —
  the likeliest leak of all, since it is the word this tracker uses constantly — and a
  chapter containing it passed. `strat` alone is too greedy: it matches "demonstrate", which
  is in chapter 14. The shipped pattern uses three explicit stems and was checked both ways.
  The absence checks carry a positive control (`/false/` must return 5 rule bodies) for the
  same reason: a grep that also matches a predicate's own rule head can never fail, which is
  a trap this repo fell into twice in one day.
  Left to do: fold the ~15-minute pin run into something a person will actually run before
  every commit — the shared-engine ask below is the real fix, and expansion is what makes it
  urgent, since ~600 pins projects to 25–40 minutes.

- **Wire the vocabulary guard in, and stop calling it a closure — 87 pins stay green
  when the evidence vocabulary is widened.** Chapter 1 stakes its opening on closure
  (`01:6-8`: "they cannot. Not *may not*. Cannot. There is nowhere to put it."). Verified
  against a copy of the constitution with two evidence facts appended — `rich(Esa).` and
  `dangerous(Esa).`, both committed corpus names, so mounting this needs no lexicon work
  at all: chapter 1's suite and the constitution's suite both pass, `PASS — 87 pins`. The
  single committed artifact that notices is the spine generator —
  `5-spine-gen.py utopia-widened.nibli 3-spine.md --check` → `STALE` (exit 1). So the
  guard exists and is not run. Two limits to record while wiring it: `--check` reads the
  constitution **file**, so it catches a drafting drift and cannot see a fact asserted at
  query time; and it detects rather than refuses. A real closure is a nibli ask. Chapter
  cost: `01:6-8` and `01:24-29` overclaim and must be weakened to what is true, and
  `01:102-136` discloses only the *amendment* route into the vocabulary, never the write
  route.

- **Pin the three Article 0 closures that nothing guards: `defend`, `reward`, `become`.**
  Article 0 closes nine relations and the file says those closures are "what makes
  Articles 4, 6, 7 and 8 mean what they say". Repo-wide only six have a `:refuse` pin.
  The three unpinned ones are the shield, the mint and the enactment gate — the heads of
  Articles 7, 3 and 9. Verified that all three refusals hold today and the pins go in
  as-is. Add to `rights-floor.pins.nibli` beside the other six and bump `:expect-pins` from 75 to
  78. Ten minutes' work, and without them the file's own named failure mode at `:44-47`
  — a `derived_only` line moved below the facts it guards "is inert and looks identical"
  — takes three of the nine gates with it in silence.

- **The floor's own relation is queryable, discriminating, and appears in no pin file.**
  `grep -rn entitled book-1/*.pins.nibli new-book-plans/rights-floor.pins.nibli` returns
  nothing. The queryable shape discriminates in three directions at once, verified:
  `? entitled(Adam, event { eats() }). TRUE` (the floor reaches a person),
  `? eats(Adam). FALSE` (and does not fabricate it),
  `? entitled(Adam, event { home() }). FALSE` (home is not on the floor),
  `? entitled(Hano, event { meets() }). TRUE` (including the convicted). This is not a
  nicety: `08:31` turns the entire chapter on exactly this contrast — "Ask whether Bela
  eats. Not whether Bela is entitled to eat — whether Bela eats" — and the pin file pins
  only the second half. **Delete every floor line from the constitution and those seven
  pins stay green**, because the actuality was always FALSE. Add
  `? entitled(Bela, event { eats() }). # => TRUE` beside `? eats(Bela).` in chapter 8,
  one `entitled` pin for Zed in chapter 7, and the `home` and non-person controls in
  `rights-floor.pins.nibli` — without the controls the pin passes for the wrong reason.
  Pairs with closing `entitled`; until that lands an `entitled` pin proves reach, not
  derivation.

- **Regenerate the counterfactual fixtures after every constitution edit.** They landed at
  `new-book-plans/counterfactual/` — three copies of the constitution, each with exactly one
  line deleted, each with a pin file asserting what the world looks like once it is gone, all
  three run by `verify.sh`. `no-person-line` is the fixture behind chapter 7's headline
  result: with `prisoner -> person` the heresy law is refused, without it the same law loads
  and the whole population becomes imprisonable for belief. `no-public-court` and
  `no-choose-boss` are the deletion axis of the trust base — one line each, and Sly loses the
  shield, and **Rebel, the file's own honest whistleblower, is jailed**.
  This is the only way a "remove this line and X breaks" claim gets executed rather than
  argued, because derivation is monotone and probe facts load *on top*, so no probe can test
  a restriction. **The standing obligation is the regeneration**: a fixture built from an
  older constitution proves something about a file that no longer exists, which is exactly
  the failure they were built to answer. The three committed here were rebuilt from the
  post-Article-1b file for that reason; the `README.md` beside them carries the one-line
  `grep -v` for each.

- **`:accept` pollutes every query below it — the ordering is load-bearing and was not
  documented.** An `:accept` directive loads its rule into the knowledge base and leaves it
  there, so a pin file's complement controls widen the base for everything that follows.
  In `rights-floor.pins.nibli` the four controls each add a second route to `prisoner` that
  Article 6 does not gate, and this produced a **real vacuous green**: `? prisoner(Adam).`
  sat below them and would have passed with Article 6 deleted outright. Verified — after the
  `~false` control loads, `prisoner(Quin)` is TRUE though Quin has no conviction at all, and
  a released person is dragged back in (`free(Hano).` then `prisoner(Hano)` TRUE,
  `travel(Hano)` FALSE).
  **Fixed** by moving that file's controls to the end, with the reason written above them.
  `07-a-prisoner-is-a-person.pins.nibli` and `08-what-you-are-owed.pins.nibli` both have
  queries after an `:accept` and were checked: neither is currently vacuous (ch 7's Hano has
  a home so the `~home` control never fires for him; ch 8's queries read no predicate the
  three accepts touch), and both now carry an ordering warning.
  Remaining work: make this a rule rather than a habit. Either a convention that `:accept`
  blocks come last in every file, checkable by a one-line grep in `verify.sh`, or a nibli ask
  for a scoped accept that does not persist. The second is better and is a one-prompt
  handoff — a directive that tests loadability and then discards the rule is what every one
  of these pins actually wants.

- **Write down what FALSE means in a pin file — it means three different things and two
  of them are worthless.** All verified, and the distinction is why five false prose
  claims survived 180 green pins:
  - A **corpus name with no occurrence in the KB** answers FALSE and passes cleanly:
    `? rich(Bela). => FALSE`. This is precisely why a widened evidence vocabulary is
    invisible to the whole suite.
  - A **non-corpus name** is not a FALSE at all, it is an abort: `nibli-pin: HARNESS
    ERROR (exit 2) — pins not trustworthy`.
  - A **well-formed query on an argument the relation never carries** is a vacuous green
    that passes forever: `? fit(Ruk, HighSec). => FALSE`, `? lose(Standing, Bela). =>
    FALSE`.
  Only the first is a real verdict, and only when something in the KB could have made it
  TRUE. Put this in the shared header block of the pin files — three sentences — because
  the pin suggestions that arrive from reviewers are disproportionately of kinds two and
  three, and a reader cannot tell them apart by looking.

- **Chapters 4 and 5 argue about voids and pin none of the premises a void turns on.**
  Four gaps, all cheap, all verified in one run:
  - `? deceive(Sly, Court). # => FALSE` — the conjunct the shield chapter turns on.
    `04-the-shield.pins.nibli:26-41` pins Sly's `show`, the authority and the outcome,
    and never the *absence* of a deceit finding, which is the only thing separating Sly
    from Kel sixteen lines later.
  - `? judge(Gia, Bela).` / `? capture(Gia, Bela).` / `? judge(Hex, Bela).` /
    `? capture(Hex, Bela).`, all TRUE. Chapter 5's Bela block pins the two credentials
    and the result and skips the four facts that actually satisfy `:330`.
  - The `~parent($a,$b) & ~parent($b,$a)` independence conjunct is exercised by **no pin
    anywhere**. `05-voiding.pins.nibli:25-33` looks like it covers this and does not — it
    exercises Article 5 (`:341`), a different rule with a different head. Verified with a
    seated parent/child pair against one target and an unrelated seated pair against
    another: `? false(Targ). => FALSE`, `? false(Targo). => TRUE`. The control is the
    point.
  - No fixture shows a voided pen-holder **in the same snapshot**. Seat Lupo and
    `? false(Lupo). => TRUE` and `? permits(Review, Lupo). => TRUE` hold together, and
    Lupo then co-signs a fresh void. That is the epoch-granularity limit the constitution
    discloses in prose at `:419-424` and that no pin has ever demonstrated.

- **Chapter 6's two clawback routes are each pinned at one end, and the epoch-carry route
  is scattered across three files that never mention each other.** `rotten(Vex)` is pinned
  at `03-who-holds-the-pen.pins.nibli:41` and `05-voiding.pins.nibli:46`,
  `permits(Review, Vex)` at `03:44` and `rights-floor.pins.nibli:60`, `false(Vex)` at
  `rights-floor.pins.nibli:64` — so three of the five verdicts *are* pinned, but no file
  carries more than two and no reader of any one file sees the sequence.
  `06-clawback.pins.nibli`, the chapter whose subject this is, never touches the carry.
  Verified end to end:
  `rotten(Vex)` TRUE, `permits(Review, Vex)` FALSE, `false(Vex)` TRUE, `authority(Vex)`
  TRUE, `lose(Points, Vex)` TRUE. Vex is the one person in the cast who is voided,
  stripped of the pen, still possessed of standing, and clawed back — four verdicts that
  between them settle three of the book's recurring confusions — and no single suite puts
  more than two of them in front of a reader.
  Second gap: `? false(Cira). # => FALSE` is unpinned, and `06:103` rests on it. **Add
  both before the Article 4 clawback narrowing** (the "Decide the Article 4 clawback
  question" bullet), not after, or the chapter loses the only fixture that would show
  what changed.

- **The eight floor rights are sampled, never enumerated — and the omitted one is exactly
  where the claim fails.** `08:32` says "the same answer comes back for every one of the
  eight", and the pin file tests seven, omitting `expresses`. Chapter 7 is worse: the
  comment at `07-a-prisoner-is-a-person.pins.nibli:29-32` says "the floor derives for Zed
  like anyone" and pins one right of the eight. Eight pins per subject is not expensive
  and it is the only shape that makes "every one of the eight" a checked sentence rather
  than a summary. Put the pin block in **before** the chapter-8 rewrite, so the rewrite
  has something to write against.

- **Chapter 11 pins three of its four cases' inputs.** `11-where-people-are-put.pins.nibli:14-58`
  pins `severe`, `family` and the outcome for Hano, Ruk and Lalo, and leaves three facts
  the routing turns on untested: `? fit(Nando, Homestay). => FALSE`, `? family(Hano). =>
  FALSE`, `? family(Lalo). => TRUE`. Three lines, and they matter because `family/1` is
  the input the chapter misdescribes — a pin naming `family(Hano)` FALSE against a man
  who has no family fact is the cheapest place for that error to become visible.
  **Do not** add a pin "testing `fit/2` for a placement other than Homestay": `fit` has
  one producing rule and only ever carries `Homestay`, so `? fit(Ruk, HighSec). => FALSE`
  is a vacuous green of kind three above.

- **Chapter 12's pin NOTE claims a pin that does not exist.**
  `12-changing-the-rules.pins.nibli:7-9` says the file "pins two live defects: the
  self-declared target (`Amend_Sneak`) and the fact that `become()` feeds nothing." The
  first is pinned, at `:53-62`. The second is not and cannot be: "nothing reads `become`"
  is an absence, and all four `become` pins assert what does or does not become law,
  which is the opposite claim. Correct the NOTE to say one defect is pinned and the other
  is a grep, and put the grep in the runner. Worth doing early because it is the
  concrete, already-realised cost of the NOTE problem below: a header comment drifted
  from its own file, nothing detected it, and the drift propagated into this tracker.

- **Chapter 14's pin file carries six defect pins and no rewrite trigger.**
  `06-clawback.pins.nibli:6-9` and `11-where-people-are-put.pins.nibli:7-10` both say
  plainly which pins encode a defect and what flips when it is repaired.
  `14-when-the-system-notices-it-broke.pins.nibli:7-9` warns only that "nothing reads
  these markers" needs a grep — and then half the file is defect pins, at `:14-31`,
  encoding an alarm that fires on every prisoner and no free person. If the isolation
  marker is repaired, or a single `meets` fact is ever recorded anywhere, those six flip
  and the chapter's middle section is wrong. The two placement pins at `:41-48` duplicate
  chapter 11's defect and carry no trigger either. Add the same note both other files
  already have, naming the pins by line.

- **Bring the pin-file NOTEs into line with the checks that now run them.** The five
  absence claims — no arithmetic anywhere, nothing reads `become`, `travel` appears once
  as a rule head, nothing reads `err`, nothing reads the Article 1b obligation — are no
  longer instructions to a human: `verify.sh` runs all five with a positive control, so
  they fail loudly. What is left is the prose. Three of the five NOTEs still tell a reader
  to run a grep, and two of those greps are the broken kind that also matches the
  predicate's own rule head and therefore can never fail
  (`10-contribution.pins.nibli:6-9`, `12-changing-the-rules.pins.nibli:7-9`,
  `13-the-one-thing-taken.pins.nibli:7-12`; chapters 8 and 14 were already corrected to
  test rule bodies with a control). Point all five at `./verify.sh` instead of restating a
  command, and **while in `12-changing-the-rules.pins.nibli`, fix the claim beside it**:
  its NOTE says the file "pins two live defects" when the second is an absence no pin can
  hold — a header that drifted from its own file, undetected, which is the whole argument
  for this bullet.

- **Extract the claim-to-query table from the pin files — it cannot be generated from the
  constitution.** The substance already exists in a better form than the old bullet
  imagined: fifteen pin files carry 271 pins, every one a query with an enforced expected
  verdict, all green, and a scan finds no `?` query lacking a `# =>` line. What is left is
  the rendering, and it runs the other way round: the constitution cannot know which
  sentence of chapter 11 a query backs, so the table must be extracted from the pins
  rather than derived beside them. Blocked by a data gap — only 83 of the 173 `?` queries
  under `book-1/` have a comment line directly above, so an extractor run today leaves 90
  sentence cells empty. Fix: settle one machine-readable form for the sentence (a `# "…"`
  line immediately above the query is already the majority convention), backfill the 89,
  then have the verification script emit the table as a by-product.

- **Freeze `4-strata.py` as an exhibit rather than fixing it — the live risk has moved.**
  The defect is real and still present: the fact branch takes only the first predicate on
  a line (`:52`, `:54`), so `entitled(every person, event { secure() }).` registers as a
  fact of `entitled` and nothing else. Repairing it now buys nothing and costs something.
  Nothing consumes it, because `5-spine-gen.py` parses the floor lines explicitly and owns
  the generated region of `3-spine.md` — and `3-spine.md:35-37` now keeps the discrepancy
  deliberately, as "the tooling-blindness story for the method part", so fixing the script
  deletes a planned exhibit. Give it a header saying it is retained wrong, on purpose.
  Then take the risk the old bullet did not name: **`5-spine-gen.py` is a second
  hand-rolled regex parser and it is the load-bearing one.** It reports 46/23/39/4 where
  `4-strata.py` reports 41/17/31, and *nothing checks either against the engine* — the pin
  suite verifies the firewall behaviourally, never the strata numbers the method part will
  print.

- **`5-spine-gen.py` only recognises a universal when it wears the floor's shape — and that
  already cost the book its headline number once.** The `FLOOR` regex at `:25` matches
  `PRED(every <domain>, event { P() })` and nothing else, so any *other* universally
  quantified line is parsed as a ground fact: its head never enters `head_preds`, it falls
  into `base`, and it is emitted as an evidence predicate. Found while enacting Article 1b.
  Written as `owe(State, Provision, every person).` — a form the engine treats identically,
  and which is exactly parallel to the eight floor lines — the generated list read
  **"Evidence predicates (22)"** and included `owe`, silently contradicting
  `01-what-counts-as-evidence.md`'s twenty-one. The engine was never fooled: the firewall
  refusal `'prisoner' -> 'owe' (negative)` only fires if `owe` is inside the person cone,
  i.e. derived. Worked around by writing Article 1b as an explicit
  `all $x: person($x) -> owe(…)` rule, which the rule branch reads correctly — evidence back
  to 21, `owe` at stratum 2, chapter order unmoved — and the constitution now carries a
  comment saying why the shorter form is not to be restored. **But the blind spot is still
  there for the next universal anyone writes**, and the failure mode is silent and lands on
  the one number chapter 1 is built on. Fix by extending the regex to any `every <domain>`
  in any place, or properly by taking the strata from the engine per the handoff above. Until
  then: after any constitution change, check `grep "Evidence predicates" 3-spine.md` reads 21.

- **Fix the upstream test citation in the constitution.** `utopia-v2.nibli:182` cites the
  five regression tests that pin the floor firewall at `integration.rs:3228`; they are at
  `:3475-3571`. That citation is the only pointer from the constitution to the tests whose
  deletion would silently end the firewall argument, so it is worth being right.

- **Two stale numbers and one dead artifact, both in the way of anyone running the suite
  for the first time.** `new-book-plans/utopia-v2-run.nibli` is committed, 54 lines, opens
  with `:load utopia.nibli` — a file that exists nowhere in the repo — and carries 42
  `:proof-verbose` directives, which `nibli-pin` does not take. It is the first thing a
  reader looking for the runner will open, and it cannot run. Delete it, or replace its
  contents with the real invocation. And `01-what-counts-as-evidence.pins.nibli:4-6` plus
  fourteen copies name a single-file invocation as the run command; point them at the
  runner once it exists.

---

## Engine handoffs (nibli)

Per the handoff protocol above, these go to `~/projects/dhilipsiva/nibli` as prompts,
never worked around in prose.

- **HANDOFF PROMPT — KB-owned predicate-set closure.** `derived_only` closes a *relation*
  against direct assertion; nothing closes the *set of relations* a KB will accept. Any of
  the committed corpus's ~1,351 names asserts cleanly onto the constitution and answers
  TRUE, and the whole 271-pin suite stays green. `NIBLI_KR.md:548` §14.1 describes
  KB-owned `pred` declarations and marks them a v2 target, "not implemented" — so this is
  an ask, not a bug.

  ```text
  In ~/projects/dhilipsiva/nibli: a KB needs to be able to declare its own fact
  vocabulary closed, the way `derived_only` declares a relation closed to assertion.
  Today `derived_only("false")` refuses `false(X).`, but nothing refuses `rich(X).` in
  a KB that has no business having a `rich` predicate — any corpus name asserts,
  fail-open. NIBLI_KR.md §14.1 sketches KB-owned `pred` declarations; §15's roadmap
  lists the injectable schema source at the arity/label lookup seam. Ship a fail-closed
  form of that: a declaration block naming the predicates this KB admits, with every
  other corpus name refused at assert time with the same message shape `derived_only`
  uses. Ordering should be load-bearing and stated, as `derived_only`'s is.

  Consumer: ~/projects/dhilipsiva/utopia-reimagined/new-book-plans/utopia-v2.nibli,
  whose Article 0 already closes nine relations, and whose book states as its opening
  claim that the record has exactly twenty-one entries and that a twenty-second
  "cannot" be written. It currently can.
  ```

- **HANDOFF PROMPT — defect pins vs guarantee pins.** Roughly a fifth of the book's 271
  pins encode admitted defects rather than guarantees, and the harness cannot tell them
  apart. A defect pin flipping reports as a regression when it is the repair landing, and
  the only thing preventing that confusion today is a prose comment in each file, one of
  which has already drifted.

  ```text
  In ~/projects/dhilipsiva/nibli: nibli-pin has no way to mark that a pin encodes a
  defect the artifact currently HAS, as opposed to a guarantee it MAKES. Both are
  `? q.` + `# => VERDICT`, so a flip is reported identically, and the two cases mean
  opposite things. Add a per-pin annotation — e.g. `:defect "<what flips it>"`
  immediately preceding a pin — and have the runner (a) report the defect-pin count in
  the summary line, and (b) when a defect pin's verdict changes, exit with a distinct
  status and message ("a pinned defect no longer reproduces") rather than the
  regression message. Keep it inert for files that do not use it. Secondary ask in the
  same area: let a pin file declare a shell precondition, so the grep-only NOTEs in the
  book's pin files become checks in the same run. The consuming artifact is
  ~/projects/dhilipsiva/utopia-reimagined/book-1/*.pins.nibli.
  ```

- **HANDOFF PROMPT — expose the compiled stratification as data.** The book needs the
  stratification from the engine, so the spine stops depending on a regex
  re-implementation of the stratifier. `nibli-pin --kb` is the only book-facing entry
  point and exposes nothing but pass/fail; `nibli-host` is unusable here. Add a way to
  dump, for a loaded KB, every predicate with its stratum, whether it is base or derived,
  and the negative edges — stable enough to diff. Then `5-spine-gen.py` renders that
  instead of parsing text, and the method part's numbers come from the engine that
  enforces them. Ask for a shared-engine mode in the same pass — `--kb` re-stratifies once
  per pin file, which is what makes the full suite a thirteen-minute run.

- **Not ready, deliberately.** Provenance on `reward` is downstream of the clawback fork —
  do not hand it off until that is settled, because the shape of the ask depends on which
  side gives. One measured correction to record while it waits: the audit reported an
  arity-2 `reward` probe as non-terminating past 15 minutes; that **does not reproduce**.
  Rewriting all three `reward` heads to arity 2 and running a single pin took **38.9s**
  against a **2.1s** baseline — a ~19x cost, not a hang. Budget it, do not fear it.
  Supermajority thresholds and sunsets need arithmetic and temporal vocabulary the KR does
  not have, and both are downstream of "there is no release" — hand those off together,
  after that is decided, or the ask will be malformed. The `obligated`/`obliged` de-swap
  is optional today and becomes a blocker if `err` gains a consumer.

---

## Data — "latest data, by script" is a build system nobody has written yet

- **Build the data pipeline before writing the empirical chapters.** The requirement is
  that the book depends on the latest data as much as possible, achieved through
  scripting — but `final-research.md` is a hand-assembled static snapshot, with the
  predictable result: figures two tax years stale, a superseded working paper, market data
  from 2015. Design: one machine-readable claim registry (claim id, value, units, source,
  retrieval date, fetch script); fetchers against sources that have APIs (World Bank, WHO
  GHO, UNEP, IEA, OWID, FAOSTAT); a rendering step that injects current values into the
  prose; and a **staleness gate** that fails the build when a figure's source has a newer
  edition than the one pinned. Where a number can only come from a paper, the registry
  pins the version and the retrieval date so the drift is visible. **Resolve the EIU
  licence question below first** — the democracy data is the registry's first customer.

- **Use the democracy/happiness dataset — but for the opposite claim to the obvious one.**
  `demo-happy.txt` + `democracy_vs_happiness_144.csv` (144 countries, EIU 2025 merged with
  WHR 2025). Every headline number reproduces exactly: raw r = 0.5975, ρ = 0.6231,
  R² = 0.357; partial r | log GDP = 0.195; r(GDP, happiness | democracy) = 0.623; and the
  regime table to the digit.
  - **Do NOT use the floor claim — and write down the regression exactly as it was run.**
    Its headline finding ("democracy behaves like a floor on subjective wellbeing, not a
    lift toward the top", p = 0.0004) is the one claim the source never controls for
    income, and it does not survive. Re-derived: take the residual of `whr2025_life_eval ~
    eiu_2025 + Log GDP per capita`, regress its absolute value on both, and democracy is
    b = −0.0196, t = −0.91, **p = 0.37** while income is b = −0.336, t = −2.53, p = 0.012.
    The residual definition is load-bearing: taking it from the democracy-only fit instead
    gives democracy p = 0.077, a real but much weaker refutation. State the specification
    or the refutation cannot be checked. **Drop the "within income tertiles the dispersion
    goes the wrong way" line** — it is not what the data show: corr(democracy, |residual|)
    is −0.140, −0.126 and +0.008, so dispersion falls with democracy in the bottom two
    tertiles and reverses only in the top one. The claim still dies; it dies on the income
    control alone. This is precisely the claim book-1 would most want to be true — a floor
    effect, in a book about floors — which is exactly why it must not be used.
  - **Use the income result instead — as a redundancy statement, not a causal one.**
    Partial r(income, happiness | democracy) = 0.623 against partial r(democracy, happiness
    | income) = 0.195. That ordering is on-thesis for a book whose floor is eight
    material-and-personal guarantees and which deliberately demoted the vote *off* the
    floor to a rule. Two limits must travel with the sentence or an economist takes it
    apart exactly as they take apart the floor claim: partialling out income plausibly
    removes democracy's own downstream effect, so this is redundancy between predictors,
    not causal irrelevance — the source says so itself; and GDP per capita is a mean, not a
    floor, so average national income cannot be evidence that a guaranteed minimum is what
    compresses wellbeing. Write the claim at the width the data support and not one word
    wider.
  - **Use the step sizes — the first one is +0.13, not +0.16.** Authoritarian → Hybrid buys
    **+0.13** (4.945 → 5.072), Hybrid → Flawed **+0.73**, Flawed → Full **+1.01**. The
    regime table already gives 4.94 → 5.07 and the source says "~0.13", so +0.16 was never
    anybody's number. The argument is unchanged and is a real one against gradualist "add a
    little democracy" reform. Say plainly that these are unconditional means — 23 of the 26
    full democracies sit in the top income tertile, so Flawed → Full is substantially the
    rich-country step, the same confound that kills the floor claim.
  - **Make it Part V's worked example of the method.** Take "democracy makes people
    happier", test it, and report: survives raw, narrows sharply under income control, and
    the floor version fails outright. The book demonstrating that discipline on a claim it
    would have loved is worth more than the claim.
  - **Licensing blocker: the EIU index is non-redistributable, and the escape hatch costs
    more than it looks.** Our World in Data cannot export the series, and `LICENSING.md`
    commits the claim registry to CC0 — so a CC-BY book with a public registry cannot ship
    those numbers. Cite-and-link keeps every figure intact but breaks the registry's promise
    that a reader can re-run it. Or switch to **V-Dem**, which is openly licensed — but then
    every number here has to be re-derived: the r = 0.52 is quoted from the transcript, no
    V-Dem data is in the repo, and V-Dem's Regimes of the World gives four categories that
    are not EIU's four, so the regime table and the step sizes do not carry over. Budget the
    re-derivation if the answer is V-Dem.
  - Housekeeping: record `demo-happy.txt` in the registry as "prior analysis, independently
    re-derived", with the CSV's provenance pinned: WHR 2025 (2022–2024 average) merged with
    EIU 2025, 144 countries matched from EIU's 166 and WHR's 147.

- **Publish the registry with the book, not just in the repo.** The formalism stays
  invisible, so what the reader verifies is the data — which only works if the registry is
  reachable from the page they are reading. Front matter names it and gives the URL, every
  figure in the prose resolves to a registry id, and the registry ships CC0 with its own
  `LICENSE-CC0`. This is the thing that earns the trust and the honest substitute for
  showing the constitution.

- **Re-cite everything against the published versions.** Muralidharan, Niehaus & Sukhtankar
  is no longer a working paper — it is *Review of Economics and Statistics* 107(2): 372–392
  (2025). Expect several others to have moved similarly. Fold the check into the registry
  build so it happens once.

---

## Correcting the research brief — each is a discrete, committable fix

- **Rewrite the social-choice paragraph — the most damaging error in the brief, and it
  appears in two places.** `final-research.md:103` says score voting "escapes
  Gibbard–Satterthwaite's ordinal frame", glossed *"it is always optimal for a voter to
  give the best candidate the highest possible score"* — unsourceable, and it inverts the
  result: **Gibbard's 1973 game-form theorem applies directly to score voting, and score
  voting is manipulable**. That sentence describes strategic exaggeration, not
  strategyproofness. Same line: Arrow is stated without the **transitive-social-ordering**
  condition; Gibbard–Satterthwaite without **determinism/single-valuedness** (randomised
  schemes escape, per Gibbard 1977); Black (1948) is credited with the strategyproofness
  escape on single-peaked domains when it gives the *Arrow* escape — **Moulin (1980)**
  gives the other, with the McKelvey–Schofield caveat that it dies in more than one
  dimension; and "a rule requiring two-thirds is neither manipulable nor dictatorial" has
  no source — the substance is the **two-outcome** restriction, not the supermajority
  threshold. The defensible claim in this vicinity is the sincere-favourite criterion.
  **Fix `:147` in the same commit** — recommendation 5 repeats the same three escapes in
  compressed form. One thing survives untouched: the theorems say nothing against a rights
  floor removed from majoritarian aggregation, and this constitution removes it.

- **Fix the Muralidharan quotation — it is a splice.** `final-research.md:56` presents a
  sentence as "verbatim from the abstract" that appears in **no** version of it: it welds
  the February 2020 abstract (which says **10%**) onto a **10.6%** figure from the body of
  the September 2021 revision. Do not correct it to the 2021 revision either — quote from
  the published *REStat* version and drop the NBER citation in the same edit. Numbers to
  re-derive: "~2 million lost access" should be **1.5–2 million**; "~1.6 million (13% of
  beneficiaries)" should be **1.7 million** (1.2 million under the paper's conservative
  assumption), and the 13 is a percentage-*point* increase in treated blocks only. The
  "almost 90% genuine" figure at `:58` — the brief's self-declared strongest datapoint — is
  **88%**, is labelled *"purely descriptive"* and non-causal by its own authors, and covers
  **1.44 lakh** deletions in 10 study districts, not the 11 lakh statewide cancellations the
  Drèze survey reports at `:57`. Those two must never be narrated as the same number.

- **Restate Krugman honestly — he prescribes the opposite of concealment, and the repo is
  no longer the answer.** `final-research.md:18` says "Two Cheers for Formalism" "explicitly
  prescribes the workflow the author is following", quoting only steps (4) and (5). The
  omitted step (3) is *"Publish the intuition, the math, and the evidence — all three."*
  Steps (4)–(5) are an *additional* obligation, not a substitute. The paragraph's conclusion
  — that the system being public on GitHub means "this is solved… the ideal configuration"
  — must go with it: **the final method part is what discharges step (3)**, publishing the
  intuition, the machinery and the evidence inside one book. Rewrite `:18` around the method
  part and delete the "ideal configuration" line; a reader sent to a repository is exactly
  the inspectability-without-inspection that Woodford's argument, quoted two sentences
  earlier, says forfeits the model's authority.

- **Fix the Housing First bullet — two outright errors.** Pull the CPSTF effectiveness-review
  summary and the Jacob et al. (2022) economic review and re-derive the two sentences at
  `final-research.md:85`.

- **Reframe Santoshi Kumari around what is documented.** The uncontested "died of prolonged
  hunger" phrasing is still in the brief at `:16` and is still the prescribed lead at `:143`.
  Write the documented-chain version instead (cancellation 22 July 2017, the sequence that
  followed) rather than the contested cause of death.

- **Replace the Mandela Rules "authoritative gloss" — it is blog-sourced.** Still
  load-bearing at `:68` and reused at `:141`. Substitute Principle 5 of GA res. 45/111
  (1990) at both sites and demote "normalisation" to one of UNODC's five principles rather
  than the authoritative reading.

- **Fix the collateral-consequences and whistleblower numbers.** All four are still wrong,
  at `:70`, `:141` and `:97`. Re-read the USCCR report and the GBES 2021/2023 waves, and fix
  both collateral-consequence sites together.

- **Fix four misattributed quotations** at `:14`, `:30`, `:32` and `:115`. Any one is a
  reviewer's free kill. Re-check each against its primary source and re-attribute in one
  commit.

- **Smaller citation fixes — with the line numbers, and one item that is not an error.**
  Roberts, *The Price of Everything*, PUP at `:16` — first edition **2008** (pbk. 2009).
  Bregman is wrong in two places, `:12` and `:30`: it is **Little, Brown (US) ~288pp /
  Bloomsbury (UK) 336pp**, and the English edition came first from The Correspondent (April
  2016). `:14` dates the HBS case method to the "mid-20th century" — it was formalised in
  the **early 1920s** (Donham; "case system" adopted 1922) — and the decision-forcing-case
  quote on the same line traces only to Wikipedia and governs *instructors*, not authors;
  cut it rather than re-source it. `:115` has Cottrell & Cockshott arguing the equations can
  be solved "fast enough"; their claim is the narrower one that **labour-time** calculation
  is tractable. **Not a correction:** the brief states no workweek length. Bregman's proposal
  is a **15-hour** week — that number belongs in the claim registry, not in an edit to a
  sentence that never made the mistake.

- **Cut or rebuild the Indian-market paragraph — and remove the Rupa characterisation** at
  `:36`, which is a standing defamation risk in a committed file and can be deleted
  unattended today. The market figures only matter if any of `:36` survives.

---

## book-1 — remaining writing

- **Write the opening note — the last unwritten non-derived element, and nothing else
  tracks it.** ~800 words before Part I, explicitly non-derived and labelled the way Part V
  is labelled, so the book does not open cold on vocabulary; it claims no derivation and
  carries no verdicts (`new-book-plans/3-spine.md:85-88`). One of exactly three sanctioned
  exceptions to the inclusion gate. No file exists. It is also where the licence line and
  the title/subtitle will have to live, so it unblocks the licence bullet below.

- **The honesty paragraph goes in the opening note, and half of it is already in print.**
  book-1 has no introduction, so the destination this item used to name is gone. One half
  has landed: *the system proves what is owed, not that anything arrives* is stated hard in
  `08:27-46` and leaned on again at `13:62` and `14:24-28`. The other half is in no chapter
  — that a formalisation makes commitments **precise**, never **justified**; nothing in
  logic says the floor should contain expression and not water. Put that half in the opening
  note and have it point forward rather than restate chapter 8, or the book opens by
  spending its strongest admission before the reader knows what was admitted.

- **Build Part V on the five-joints scorecard, re-framed for destination-only scope.**
  Nothing of it exists. Score this design at the five joints — **valuation, rotation,
  coercion, capture, the state** — as places a *functioning* design breaks, never as stages
  of a rollout, because "here is what happened to people who tried to build this" is a
  transition story and belongs to book-2. Three constraints, all grafted deliberately. Use
  the three-word verdict vocabulary — **Survives / Survives, narrowed / Fails as stated** —
  printed once and never expanded, because it is the only proposed seam device that
  disciplines at the sentence level. Every limit closes on a **specification** concrete
  enough to be worked on, not on an admission. And publish **no numeric self-grade**: the
  hostile judge's dismissal sentence was *"two and a half out of five"*, and printing that
  as the structure of the part administers his verdict for him. On salvage: the only genuine
  harvest is "Learning from Those Who Tried" (`book.md:2303-2380`, 2,264 words), and its
  nine cases enter as **evidence about failure modes**, never as a narrative of attempts.
  "When the Pod Meets the State" is unsalvageable — 21 uses of "pod" in 2,092 words and this
  book has no pods. The social-credit chapter is the best writing in the manuscript and
  unliftable, with seven named dependencies pointing at three chapters that will not exist.
  **Budget: ~12,000 words** — settled, see `CLAUDE.md`'s length invariant. Shape: a
  ~1,700-word frame, five joints of ~1,600–2,500, a ~400-word close. **The frame earns
  the three verdict words on somebody else's claim before spending one on the design** —
  the democracy-and-happiness data runs Survives → Survives, narrowed → Fails as stated,
  on a claim this book would have loved to be true, which is exactly why it is the
  exhibit. Then every joint runs the same five moves: what broke here historically →
  what this design does → **the strongest real objection, named, not straw-manned, and
  left unanswered for a beat** → the answer, and what of the objection survives it →
  the verdict and its specification. Each objector picks up a concession the derived
  spine already made and argues it is fatal, which is what stops the voices reading as
  invented. Two rules, stated once and enforced: **no aggregate verdict anywhere** — a
  five-row summary table *is* the numeric self-grade in another notation, and one
  Survives plus three narrowed plus one Fails renders as "two and a half out of five" to
  any reader who wants it to, so no recap, no verdict word in a heading or the contents;
  and **every specification is a property of the finished society, never a task** —
  "allocation patterns by group are published in a form an outsider can check", never
  "set up an audit body", or the inclusion gate leaks out of the part that is exempt
  from only half of it.
  Two collisions to fix while drafting. One of the five joints is named **coercion**
  (what may be done to a person) and the coercion *concession* is assigned to the
  **state** joint (a body funded compulsorily) — same one-word-two-things problem as
  `standing`/`false`; disambiguate once in the frame with a forward reference. And the
  single book-2 pointer is specified "at the very end", but the method part is now the
  final part, so it belongs at the end of **that**, not here.

- **[AUTHOR-GATED] Concede coercion and state the social-democratic positioning, at Part
  V's *state* joint.** The duty-bearer is enacted (Article 1b) and chapter 8 names it, but
  both of these are still unsaid anywhere in book-1 — `grep -rn "coercion\|social democ"
  book-1/` returns nothing. Neither can go in Parts I–IV, and the reason is the inclusion
  gate rather than taste: the constitution has no vocabulary for a tax, a transfer or a
  community, so the *fiscal* character of the bearer is not derivable and chapter 8 can only
  say a public body owes the eight to every person. Part V is exempt, and this is its state
  joint. **Concede coercion in plain words** — a body obliged to provide at scale is funded
  compulsorily, and a reader who notices the word being avoided stops trusting the rest.
  **State the positioning outright** — the ends are social-democratic and the provider is a
  fiscal agent; the novelty is the constraint mechanism, not the absence of a provider. Said
  plainly, "social democracy with extra steps" loses its teeth, because the extra step is a
  compile-time prohibition nobody else has. Chapter 8 sets this up and does not spend it:
  it says nothing compels the body, which is the true state of the design and is exactly the
  question Part V has to answer.

- **Write what the logic refused — in the method part, paired with chapter 7.** Re-verified:
  appending `all $x: prisoner($x) -> permits(Appeals, $x).` returns *"[Stratification Error]
  Unstratifiable negation: strongly-connected component containing 'prisoner' -> 'permits'
  (negative)"*. A **universal right of appeal cannot be expressed** in this constitution.
  That is not a defeat; the machine refuses a thing the author wanted and can say exactly
  why. Ship the error message. **Not in Part V** — Part V is argument and evidence and stays
  jargon-free; an engine error message is formalism, which appears in exactly one place.
  **And the firewall it pairs with is chapter 7, not chapter 1** — `07:44` is where the
  heresy law is refused; chapter 1 is the evidence vocabulary and contains no refusal at
  all. The symmetry is the argument: the same stratifier that refuses the author a universal
  right of appeal refuses an attacker a heresy law. One mechanism, no special pleading,
  neither outcome chosen by whoever was writing that day.

- **[AUTHOR-GATED] Decide whether Part V prices the temporary-assessment exclusion.**
  Chapter 1 excludes assessments of a person's present state (`01:24-29`) and says at
  `:31-33` that the exclusions were "considered and rejected on principle". It never prices
  what the exclusion costs. The strongest objection in the review corpus: medical capacity,
  flight risk and conflict-of-interest are *temporary, operational* assessments a
  functioning society cannot run without, so forbidding them does not abolish them — it
  pushes them into a parallel record the constitution cannot see, which is the exact failure
  mode chapter 1 exists to prevent, relocated one level out. A hostile reader reaches this
  in a paragraph. Inclusion-gate ruling: this is how the society **functions**, so it is
  legitimate Part V material and out of Parts I–IV by construction. **The remedy is not
  adoptable as stated** — a capacity or risk field is a standing judgment about a person,
  breaking bright line 2 and landing an eligibility computation upstream of the floor. The
  survivable answers are narrower and both need a ruling: a two-place fact about an
  *episode* rather than a one-place property of a person (which costs a twenty-second
  entry), or an explicit concession that this design routes such assessments outside the
  record, with the reason why that is the lesser harm stated rather than implied. Decide
  which joint owns it — capture is the closest fit — and which of the three verdicts it gets.

- **[AUTHOR-GATED] Decide how much emotional texture Part V absorbs.** Five of six reviewers
  independently asked for the same three things: emotional register, an external antagonist,
  and characterisation of the named cast. Mostly foreclosed by construction — the chapter
  order is computed, the cast comes from the constitution's own adversarial fixtures rather
  than from invention, and Parts I–V are jargon-free — but *five of six* is a signal about
  **how the derived spine reads**, not a taste complaint. Two channels are open without
  breaching the gate: Part V is explicitly non-derived, and the day-in-the-life technique is
  already queued for harvest. Decide the ceiling **now**, before Part V is drafted, because
  retrofitting register across fourteen finished chapters is a different job. The concrete
  question is narrow: does the named cast get any interiority at all in Part V, or does the
  book hold the line that the people in it are exactly the facts recorded about them — which
  is itself the thesis.

- **[AUTHOR-GATED] Answer Ambedkar in Part V, not in the derived spine.** Caste as a design
  problem rather than a historical footnote: reserved committee representation, mandatory
  external audit of allocation patterns. Part V is exempt from the derivation gate, which is
  exactly why this belongs there and not in a computed chapter.

- **Write the single book-2 pointer, at the very end.** book-1 references book-2 exactly
  **once**, in the closing note — not in the introduction, because a reader on page one has
  no idea whether they want the machinery, and a forward reference reads as an apology for
  the book they are holding. At the end it reads as an invitation. **Its old second job is
  gone** — it used to carry the one honest sentence about the apparatus; the method part now
  does that far better, by showing the machinery instead of alluding to it. Keep the pointer
  plain: no tool names, no jargon, nothing a general reader must decode.

- **Reframe the brief's India-first assumptions for a global audience.** India material stays
  as **evidence** — Aadhaar/PDS is among the strongest evidence the book has — but it is one
  case among several, not the frame, and every reference needs enough context for a reader
  who has never heard of a ration card. Unblocked by drafting Part V; that is the only place
  the India evidence lands.

- **[AUTHOR-GATED] Voice.** All fourteen chapters are written in a plain, mostly impersonal
  register. The legacy book was first-person and warm, and the constitution's own commentary
  says "the manifesto voice is the author's to re-weave — I am not ghost-writing it." Only
  the author can supply it, and every chapter drafted before that pass needs re-touching, so
  it gets more expensive each week.

- **Expand Parts I–IV from 15,188 to ~38,000 words.** DECIDED 2026-07-29; the invariant and
  the budget are in `CLAUDE.md`. This is the largest single item in the tracker — **+22,812
  words**, mean chapter 1,085 → ~2,714 — and it is one bullet only because the work is one
  decision; it becomes fourteen commits. **Know what it is not:** the invariant does not
  force it. Break-even is derived > 17,800, so Parts I–IV could stay near 18,000 and
  majority-derived would still hold. The 38,000 is an editorial choice about the book's
  size, and it means Part V's 12,000 must be justified by content rather than by ratio.

  **Where the words legitimately come from**, ranked by how much each can carry. The gate
  is satisfied a priori for the first four — the material is already derived and merely
  unwritten.
  - **Unfold compressed derivations, ~10,000.** The chapters state chains rather than
    walking them: `03:13-14` disposes of the whole credential rule in one sentence, and the
    cast has a person for each of its three conditions. `05:8` says "the answer is a list of
    conditions" and works four of the eleven conjuncts in `:330`. 150–400 words per unfold,
    one pin per named conjunct.
  - **Write the complement, ~4,500** — who a rule does *not* reach. `reward(Boss)` is FALSE,
    so a recalled auditor earns nothing and chapter 10 never says so; `decide(Ivo, Ballot)`
    is FALSE because nobody wrote down that the book's most-used victim is an adult.
    **Screen every one**: a FALSE is content only when something in the knowledge base could
    have made it TRUE. `fit(Ruk, HighSec)` is FALSE forever and a paragraph built on it is a
    vacuous green wearing prose.
  - **A second case from the existing cast, ~4,500.** The cast is badly under-used — **Adam
    appears in zero chapters** and is chapter 11's missing eighth cell; `Mira` earns
    recognition as the target of a deceitful examination and chapter 10 never uses her; and
    `Amend_Floor` derives `false` **and** `lose(Points, ·)`, so the clawback rule docks
    recognition from a legislative proposal, which no chapter mentions.
  - **New disjoint cast islands, ~3,500** — only where the existing cast cannot cover the
    cell. Not as a way to make chapters longer.
  - **Absences made queryable, ~2,500**, on chapter 13's "And it never ends" model. Each one
    ships its shell check *in `verify.sh`*, never as a comment — that is what let chapter
    12's NOTE drift.
  Available ≈26,200 against 22,928 required. The margin is thin enough that the complement
  screen and the absence cap have to be enforced or the shortfall becomes padding.

  **The domestic register stays out of Parts I–IV**, and the reason is sharper than "the
  gate is strict": six of the eight floor rights derive for **nobody**, so there is no meal,
  no clinic, no classroom and no neighbour in this constitution. A domestic scene here would
  have to invent the delivery layer chapter 8 exists to say does not exist. **One exception
  is legitimate and worth taking**: the only domestic facts the design derives are `dwell`
  and `expresses` for prisoners, so book-1 can write exactly one day-in-the-life and it is a
  day in custody. ~1,000–1,500 words across chapters 8, 11 and 13, dramatising chapter 8's
  own asymmetry rather than asserting it.

  **Per-chapter targets, deliberately uneven** — weighted by how much derived material the
  chapter's subject predicate actually holds, and by whether its argument is one blade that
  dilutes when padded:

  | ch | now | target | why |
  |---|---|---|---|
  | 8 What You Are Owed | 1,365 | **4,200** | largest: 240 latent `entitled` verdicts, 30 `owe`, three open doors, the duty-bearer, the delivery gap, the custody day |
  | 1 What Counts as Evidence | 1,392 | 3,600 | 21 predicates carrying 83 ground facts, and the list is one 90-word paragraph |
  | 5 Voiding | 1,040 | 3,200 | highest conjunct density in the file — eleven in `:330`, four in the prose |
  | 4 The Shield | 1,162 | 3,000 | three cases; the per-pair defeat is a fourth; polarity and the growing surface each carry a section |
  | 11 Where People Are Put | 940 | 3,000 | the missing eighth cell (Adam, Don, Kel), the `family` re-gloss, the `err/2` rewrite |
  | 3 Who Holds the Pen | 1,092 | 2,600 | three conditions each with a live case; the second credential; the selection boundary |
  | 6 Clawback | 994 | 2,600 | `lose` has 8 atoms including two amendments; the Vex carry no single file shows |
  | 10 Contribution | 1,019 | 2,600 | Mira, Wren and Boss all unused; the no-arithmetic argument; the third-door fix |
  | 12 Changing the Rules | 953 | 2,600 | three amendments with full fact sets; `false`/`lose` firing on proposals |
  | 13 The One Thing Taken | 988 | 2,400 | `travel` has 23 atoms; the Hano/Jala list rebuilt into a stronger claim |
  | 2 Standing | 1,236 | 2,200 | `authority` has 9 atoms, 2 routes, no negation in its cone — a thin predicate, do not inflate it |
  | 9 The Vote | 919 | 2,000 | thin in the KB: `decide` 4 atoms, `mature` 4. Below average honestly rather than by padding |
  | 7 A Prisoner Is a Person | 977 | 2,000 | **held low on purpose** — the sharpest argument in the book; padding blunts it |
  | 14 When the System Notices It Broke | 1,111 | 2,000 | **smallest on purpose** — it is the closing beat and length is the enemy of a hard finish |

  **Draft in dependency order, not chapter order:** 7 → 2 → 3 → 4 → 5 → 12 → 6 → 10 → 1 → 9
  → 8 → 11 → 13 → 14. Chapter 1 goes late because three undecided items define the list it
  enumerates; 11 and 14 go last because the `err/2` repair rewrites them; 8 goes late
  because every other chapter's admissions point at it. One chapter per commit, `verify.sh`
  before each.

- **The rule that decides whether expansion is cheap — verified, do not re-derive it.**
  *Ground facts over predicates that already occur in the constitution are structurally
  free. Anything that introduces a predicate name, or a rule head, is not.* A ground fact
  reaches only `all_preds` in `5-spine-gen.py:77-80`, so if the predicate is already there
  the generated block is **byte-identical** — predicate count, derived count, rule count,
  strata, the floor list, the evidence list and therefore chapter order all unmoved. A body
  conjunct is free too (`rules` counts arrows, not literals). A **new predicate name** costs
  the evidence list 21 → 22 and falsifies chapter 1's headline number in nine places
  (`01:5, :6, :32, :100, :106`, `03:85, :100`, `05:93`); a **new rule** moves the rule count
  and may add a stratum, which would add a chapter, which the computed order forbids.
  **Structural freedom is not verdict freedom, and this is what will actually bite.**
  Article 4's multi-sig quantifies over two auditor variables, so a new person naming
  *existing* constants can complete a rule no existing pair could satisfy: four facts
  (`person(Ann). choose(Electorate, Ann). judge(Ann, Tyr). capture(Ann, Tyr).`) flip
  `false(Tyr)` FALSE→TRUE and destroy chapter 5's headline case. **Every argument position
  in every new fact must be a new constant**, except the four institution constants — and
  even those need care, since `judge(Review, ·)` is the deceit adjudication and
  `broken(Court).` is a universal amnesty. The rule is a heuristic; `verify.sh` is the proof.

- **Re-run the jargon sweep after every chapter.** `grep -rniE
  "nibli|predicate|stratum|strata|compil|assert|rule head|quantif" book-1/*.md` returns
  nothing today, across all fourteen. "It compiles" leaked into ch 9 once and was caught by
  eye, not by a sweep run on schedule — which is the argument for wiring it into the runner
  rather than remembering it.

- **Add `LICENSE-CC-BY` to `book-1/` — and take the SPDX-header branch.** `LICENSING.md:58-59`
  offers "an SPDX header **or** a licence line in the front matter"; `book-1/` holds `01`–`14`
  and nothing else, and the opening note that would carry front matter is still unwritten.
  `find . -name "LICENSE*"` still returns only the root CC0 `LICENSE`, so the new prose is
  covered by nothing — or worse, reads as covered by the irrevocable CC0 dedication it was
  deliberately moved out of. Fetch the canonical CC-BY-4.0 text from
  <https://creativecommons.org/licenses/by/4.0/legalcode> rather than reproducing it from
  memory, drop it at `book-1/LICENSE-CC-BY`, and carry `SPDX-License-Identifier: CC-BY-4.0`
  either as an HTML comment at the top of each chapter or once in a `book-1/README.md` — a
  visible licence header in reader-facing prose is not acceptable. The rest stays correctly
  deferred: `LICENSE-MIT` + `LICENSE-APACHE` with SPDX headers when the harness and fetchers
  are written; `LICENSE-CC0` when a registry directory exists.

- **[AUTHOR-GATED] Plan the reach strategy on the basis that exclusivity is gone.**
  CC-BY-4.0 is perpetual and irrevocable, so no trade publisher can ever be sold exclusivity
  — `LICENSING.md` records this as a cost accepted deliberately. That makes serialization and
  open circulation the route by default rather than by choice, and it is a publishing
  decision nobody but the author can make. Worth knowing when it is made: the **title** is
  the only integrity lever that survives an irrevocable content licence, since no licence
  here grants trademark.

---

## Legacy harvest — before `book.md` and `manifesto.md` are deleted

- **Harvest the References & Data Sources section — the single most valuable thing in the
  legacy books.** `book.md` closes with **55 sourced entries**, grouped by chapter, each with
  a primary source and URL, built by a 30-claim fact-check against primary sources. That is
  the seed corpus for book-1's claim registry and it would take weeks to rebuild. Port it
  into the registry format *before* deletion, applying the research-brief corrections above,
  and drop entries whose claims book-1 does not make. **Blocked on the registry format
  existing** — that is the long pole for the whole harvest.

- **Harvest the nine historical cases.** New Harmony and the labour exchange, China's
  work-point villages, the kibbutzim, Nyerere's Ujamaa, Chile's Cybersyn, Auroville,
  Mondragon, WIR, Kerala's People's Plan — 2,264 words, researched, sourced, and
  mechanism-independent. **Re-point them when porting:** book-1 does not tell the story of
  people who tried to build a better society — that is transition. Each case enters as
  evidence about a *failure mode of a functioning design*, never as an attempt narrative.
  Nowhere to put them until Part V exists.

- **Harvest the Bharati poem and settle its attribution.** The full poem with Tamil original
  and translations lives in `book.md`'s closing appendix, attributed there to *Yoga Siddhi*
  ("Varam Kettal"), stanzas 4–5. `1.md` attributes the manifesto's frame to *நின்னைச்
  சரணடைந்தேன்* — a string that appears **nowhere** in any artifact, and the manifesto's own
  Part 2 Ch 1 epigraph is நின்னைச் **சிலவரங்கள் கேட்பேன்**, which `1.md` appears to have
  garbled into a title. Confirming the correct name against a Tamil-literature source is
  plain research and unblocked. **[AUTHOR-GATED]** is the second half: whether book-1 opens
  with an epigraph at all — at most **one**, original, plain translation, one sentence on who
  Bharati was, never as structure. The manifesto's sixteen-chapter mapping onto the sixteen
  lines is a real piece of craft; record it before the file goes.

- **Harvest the day-in-the-life technique, not the prose — and fix the citations.** The three
  vignettes are at `book.md:981-984` (merit points), `1395-1398` (shelter, mobility,
  communication) and `2560-2563` (governance); the ranges previously cited here land on
  tech-UX bullets and legal-collision prose instead. All three are second-person and generic
  and two are MVS-framed, so nothing ports verbatim. book-1 is also no longer without a
  narrative register — seventeen named characters, Hano in 37 places, every chapter built on
  a case. What is actually missing is the **domestic** register: a household carried through
  food, care, housing and crisis, rather than a defendant carried through a procedure. Decide
  whether Part V gets one, since Parts I–IV are derivation-gated and cannot hold it.

- **Finish the floor corrections in book-1 — two of four landed.** Landed: the eight-right
  floor is stated exactly once, at `08:5-6`; and the franchise is carried as a derived rule
  — person plus adult — at `09:14-18`, not as a floor right. Still open: **`dwell` is nowhere
  glossed in prose as protective shelter** — `grep -rniE "weatherproof|ventilat|plumb|sanitation"
  book-1/` returns nothing, so ch 8's "somewhere to live" carries the whole weight and the
  water-and-sanitation case is not absorbed; write the gloss into ch 8 now, it costs a
  sentence. And **privacy is not argued down anywhere** — book-1 has one incidental use of
  the word (`04:42`), and the argument that encoding it as a defeasible right lands it at
  stratum 3 and destroys the single-deprivation theorem is Part V material. That half waits
  on Part V; the `dwell` half does not.

- **Then delete both files, in one commit, with the harvest manifest in the body.** Not
  before. The commit message is the record of what was taken and what was consciously
  dropped.

---

## Hold for book-2 — do not work these here

Parked, so they are not lost when the legacy files go. These become the seed of book-2's
tracker, written from scratch after book-1 ships.

- **The transition material** in `book.md` — Part 4 in full (One Person One Family; When a
  Village Joins; Cities, Provinces and Nations; One Planet One People), plus "When the Pod
  Meets the State" and "MVS in Action". ~8,600 words, largely organisational, legal and
  fiscal. This is book-2's spine, not an appendix to it.
- **The technical backbone material** in `book.md` — local-first/offline-first
  micro-blockchains, Proof of Personhood, quantum-secure and privacy-centric design, YAD, the
  layman's guide. It has **no support in the constitution** — no ledger, no biometric, no
  device, no cryptography — which is precisely why it is book-2's subject and not book-1's.
- **"Why a blockchain at all?"** — honestly weighing CRDTs and signed logs against
  nibli-store's HLC/tombstone/CRDT-export design. It partly argues against the legacy book's
  central premise, which makes it a strong opening question for book-2 rather than a threat
  to book-1.
- **Replace venture brand names** (union.build, Sui, Fuel, linera) with capability
  requirements plus a dated appendix. The list in the legacy text is incomplete; re-grep when
  the book-2 tracker is written rather than trusting it.
- **The costed transition** — a fiat price tag on a 200k-city baseline, funding per phase, and
  a housing acquisition mechanism (community land trusts vs right-of-first-refusal). Needs
  real fiscal magnitudes; don't fabricate numbers.
- The nibli-side convergence bullets live in nibli's own `TODO.md`.
