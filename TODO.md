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

**THE WORKING ORDER, and it is three phases, not a priority list.** This file is
arranged in the order the work happens. Do not skip ahead: each phase removes
constraints the next one would otherwise have to work around.

1. **Phase 1 — engine (nibli).** Every prompt is written and ready to paste. Some
   of what the book has to concede is an engine limitation rather than a design
   choice, and it is dishonest to write the concession while the limitation is
   fixable. Phase 1 is also where the 47-minute verification lives, which taxes
   every later phase.
2. **Phase 2 — author-gated decisions.** Nothing here can be worked unattended.
   Several chapters cannot be revised until the decision above them is ruled,
   because the ruling is what the chapter says.
3. **Phase 3 — chapter passes, chapter 1 through 14, in order.** One chapter at a
   time: read it whole, fix what is false, revise what is thin, verify, commit,
   move to the next. The per-chapter bullets below are what is already known to be
   wrong — they are a floor for that pass, not its scope.

The sections after phase 3 are cross-cutting: constitution work that no single
chapter owns, harness work, the data pipeline, the research brief, the legacy
harvest, and the book-2 hold list. Work them when a phase-3 pass reaches into
them, not on their own.

Plain bullets, never numbered. Delete a bullet entirely when it fully lands;
update it if only partly done. One item at a time: do it, verify it, commit it.

Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory,
or a design decision — they are collected in phase 2 rather than scattered.

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

---

## Phase 1 — Engine work (nibli). Nothing is pending upstream.

**dhilipsiva wrote nibli, and is the channel between the two repos.** The two sessions
cannot see each other, so **an item is not ready until it carries a self-contained prompt
in a fenced block** — one that can be pasted into a Claude Code session in
`~/projects/dhilipsiva/nibli`, with that session's reply pasted back here. A prompt must
assume **zero** knowledge of this repo: no bullet references, no chapter numbers, no "see
above". If an item cannot be stated that way it says so instead of carrying half a prompt.
End every prompt by asking for the sha, what changed, whether a verdict moved, and what the
prompt itself got wrong; that last one has been non-empty more often than not.

**The section is empty on purpose.** Every ask written here has landed and been verified
here, and nothing is waiting on nibli. Do not
work around an engine limitation in prose — conceding a fixable limitation as though it
were a design choice is the specific dishonesty this phase exists to prevent, and it is why
the phase runs first.

**When a reply lands here**, re-run `./verify.sh` before believing anything — the script
rebuilds `nibli-pin` from the checkout and prints the commit, and this repo has twice
measured an engine change that was never rebuilt.

---

## Phase 3 — Chapter passes, chapter 1 through 14, in order.

One chapter at a time: read it whole, fix what is false, revise what is thin, verify,
commit, move on. **The bullets under each chapter are what is already known to be wrong —
a floor for that pass, not its scope.** Chapters with no bullets still get a pass.

### Chapter 1

### Chapter 2

No known defects. Read it against the constitution anyway.

### Chapter 3

No known defects. Read it against the constitution anyway.

### Chapter 4

- **Chapter 5 asserts two facts about Koa the constitution does not derive.**
  `book-1/05-voiding.md:25-26`: "Koa examined Esa and recorded a finding — a real
  finding, on the record, made by someone with the credential." Koa's entire presence is
  `person(Koa).` and `capture(Koa, Esa).` (`:788-789`). Verified:
  `? capture(Koa, Esa). => TRUE`, `? judge(Koa, Esa). => FALSE`,
  `? choose(Electorate, Koa). => FALSE`, `? permits(Review, Koa). => FALSE`,
  `? permits(Tribunal, Koa). => FALSE`. Two of the sentence's three clauses are
  underivable, which the inclusion gate forbids outright. Chapter 1 gets the same person
  right (`01:140`, "Koa documented something").
  The consequence is worse than the wording: `? false(Esa). => FALSE` is over-determined
  three ways, so the section's headline claim — "It takes two, from two places"
  (`05:11`) — is demonstrated by **no pin in the suite**. Two ways out, not equivalent.
  Either fix `05:25-28` to match chapter 1 — Koa documented, holds no pen, and *that* is
  the first reason nothing moved — which is cheap but changes what the section
  demonstrates. Or seat Koa on **both** bodies and add `judge(Koa, Esa).`, which since
  the cross-body change is the only fixture that isolates the count: verified, with
  `permits(Review, Koa)` and `permits(Tribunal, Koa)` both TRUE, `? false(Esa).` is
  still FALSE, and `~($a = $b)` is the only conjunct left doing it. A single
  Electorate-seated Koa does **not** isolate the count — it fails the Tribunal conjunct
  as well, which is the "from two places" half.
  Either way pin `? judge(Koa, Esa).` and `? permits(Review, Koa).`.

### Chapter 6

- **Chapter 6 tells the reader a voided person still eats; the engine says otherwise.**
  `book-1/06-clawback.md:29-33` says a voided person "still eats. Still has somewhere
  to live. Still learns, still speaks, still keeps company" — and the engine returns
  FALSE for every one of those about Bela, *the same person chapter 8 uses to say the
  opposite* (`08:31-34`). Verified FALSE: `eats(Bela)`, `dwell(Bela)`, `learn(Bela)`,
  `expresses(Bela)`, `meets(Bela)`; only `decide(Bela, Ballot)` is TRUE. Rewrite
  `06:29-33` to the *entitlement* reading and add the pins that would have caught it —
  `06-clawback.pins.nibli` pins the clawback verdicts and nothing about the floor it
  claims survives.

- **Chapter 6's clawback pins are missing the reason and the cost, and the chapter's own
  file never touches the epoch carry.** `02-standing.pins.nibli:91-102` now carries
  `false(Vex)`, `authority(Vex)` and `permits(Review, Vex)` as one adjacent block, so
  three of the five verdicts are in front of one reader in one file. Still missing from
  that block: `rotten(Vex)`, which is the *reason* for the other three, and
  `lose(Points, Vex)`, which is the cost — the latter is pinned in no file at all.
  Re-verified 2026-08-01: `rotten(Vex)` TRUE, `permits(Review, Vex)` FALSE,
  `false(Vex)` TRUE, `authority(Vex)` TRUE, `lose(Points, Vex)` TRUE. Vex is the one
  person in the cast who is voided, stripped of the pen, still possessed of standing
  (the other sense), and clawed back — four verdicts that between them settle three of
  the book's recurring confusions — and `06-clawback.pins.nibli`, the chapter whose
  subject this is, contains no Vex.
  Second gap: `? false(Cira). # => FALSE` is unpinned (verified FALSE) and `06:112-113`
  rests on it. **Add both before the Article 4 clawback narrowing** (the "Decide the
  Article 4 clawback question" bullet), not after, or the chapter loses the only fixture
  that would show what changed.

- **Chapter 7 says the prisoner rule is the only route into personhood that needs no
  roster entry. There are two, and the second is worse.** `07:99-104`: "The rule that a
  prisoner is a person is the *only* route into personhood that does not require
  somebody to write your name down … the sole way to acquire the protection of this
  society without depending on someone's willingness to list you is to be found guilty
  of a crime." `free` is the other route. Verified on a name the record has never held:
  assert `free(Nemo).` alone and `? person(Nemo). => TRUE`, the whole floor is owed, and
  `? travel(Nemo). => TRUE` — personhood without a roster entry, without a conviction,
  and without losing anything, from one write by anybody. The release predicate chapter
  13 treats as the end of a sentence mints a person who never had one.
  Rewrite `07:99-104` to name both routes and say which of them nobody adjudicates, and
  pin `? person(·).` off a bare `free` fact — chapter 7's suite queries neither. This is
  chapter 1's `free` finding seen from the other side: the same write empties a
  conviction there and creates a person here.

- **Chapter 8 concedes one exception to the delivery gap and there are two.**
  `08:50` now states the shelter rule correctly, but `08:31-34` still says the answer
  "no" "comes back for every one of the eight, for every person in it", and `08:48`
  still says "There is one exception". Recorded speech is the second, and since the v0.8
  confinement rule the two have exactly the same width: both derive for every confined
  person and for nobody else. Verified 2026-08-01 across the cast — `dwell` and
  `expresses` are TRUE for every prisoner and FALSE for Bela and Cira, and
  `expresses(Jala)` and `dwell(Jala)` are FALSE for the unconvicted woman chapter 13
  pairs with Hano.
  The pin file is why this survived: `08-what-you-are-owed.pins.nibli` pins the "no" for
  seven of the eight and never names `expresses` anywhere, so the one entry that answers
  TRUE is the one nothing looks at. Rewrite `08:31-34` and `08:48-58`, and add
  `? expresses(Hano). # => TRUE` and `? expresses(Bela). # => FALSE` beside the `dwell`
  block at `:40-59`.

### Chapter 9

- **Chapter 9 says the disenfranchisement clause "works". It takes nobody's ballot.**
  `book-1/09-the-vote-conviction-does-not-take.md:73-75`: "Nothing refuses it. **It
  works. Immediately, every convicted person in this society loses the ballot.**" The
  accepted clause is strictly *more* restrictive than the Article 2 franchise rule at
  `:456`, and derivation is monotone, so adding it subtracts nothing. Verified by
  accepting the chapter's own clause verbatim: `all $x: person($x) & mature($x) &
  ~prisoner($x) -> decide($x, Ballot).` → `? decide(Hano, Ballot). => TRUE` with
  `? prisoner(Hano). => TRUE`. The chapter's real result — the clause *compiles*, where
  a floor-shaped one is refused — survives untouched; the sentence claiming it takes
  effect does not. `constitution.nibli:15` teaches exactly this: "A permissive rule left
  in place keeps its exploit." The pin file cannot catch it because `:49-50` pins only
  that the rule loads and never re-queries the ballot.
  Rewrite `09:71-79`: the clause is writable, and it bites only if the existing
  franchise rule is repealed alongside it — a two-line repeal, not one, which is a
  marginally better result than the chapter claims and should be stated as such rather
  than as a save. **The pin needs care now the accept is scoped.** Verified:
  `:accept-scoped` retracts the clause before the next query runs, so a query placed
  under it is about the base and not about the clause. Keep the scoped accept as the
  loadability pin, then add a second, **unscoped** `:accept` of the same clause as the
  file's last block with `? decide(Hano, Ballot). # => TRUE` beneath it — verified green
  at 14 pins — and say in the comment why it must be unscoped and last.

- **`mature/1` is a silent franchise gate, and chapter 9 says the ballot needs nobody's
  permission.** `mature` has no producing rule anywhere (asserted only at `:834-837`), is
  absent from `derived_only`, and is directly assertable — so a polity disenfranchises a
  demographic by **declining to write adulthood into their records**, passing no rule at all
  and tripping no marker. The constitution's own comment at `:831-833` concedes the second
  half ("no rule anywhere reads ~mature") while presenting it as a reassurance. Verified:
  `? mature(Cira). => FALSE` and `? decide(Cira, Ballot). => FALSE`; asserting
  `person(Zed). mature(Zed).` gives `? decide(Zed, Ballot). => TRUE`, while `person(Yun).`
  alone gives `? decide(Yun, Ballot). => FALSE` — two writes buy a ballot, one write short
  and there is neither a ballot nor an `err`. So `09:50-53` — "the ballot follows,
  automatically, with nobody's permission required and nothing to apply for" — is true of
  the rule and false of its input; and the Cira passage at `09:43-53` rests on reading Cira
  as a child when the record cannot distinguish a child from an adult nobody wrote down.
  Qualify `09:50-53`: the ballot needs no permission *once the record says you are an
  adult*, and that is an asserted fact like any other. Add `mature` to the trust-base list
  below.

### Chapter 10

- **Chapter 10: the third door is not gated on voiding, and the chapter says it is.**
  `book-1/10-contribution.md:50-68` claims "All three doors close for the same reason:
  a person whose credibility has been voided earns nothing" and closes on "putting the
  same condition on all three doors". There is no such condition. Article 3 gates
  teaching and work on `~false` (`:459-460`); the examiner rule (`:485`) gates on
  `~deceive` and `~broken` only. **Verified:** `false(Vex)` TRUE *and* `reward(Vex)`
  TRUE — chapter 5's own voided auditor still earns recognition — and adding
  `judge(Bela, Ivo). capture(Bela, Ivo).` gives `false(Bela)` TRUE, `reward(Bela)`
  TRUE and `lose(Points, Bela)` TRUE together. Both worked reasons at `10:58-60` are
  also wrong: `reward(Lupo)` is FALSE for `~deceive` and `reward(Dev)` because Dev
  never captured, neither for voiding. The 12-pin suite is green because
  `10-contribution.pins.nibli:50` pins `reward(Bela) => FALSE`, which holds only
  because Bela examines nobody in the shipped cast.
  Two ways out, and they are different societies: **rewrite the section** to say the
  doors are gated differently — a voided person can still earn by examining other
  people, which is worse than the version in print and worth saying — or **add
  `~false($auditor)` to `:485`** and keep the prose. The guard stratifies (re-verified
  2026-08-01 on a scratch copy: `reward(Vex)` goes FALSE, `reward(Gia)` stays TRUE).
  Either way the suite needs a pin on a voided examiner, because its absence is what let
  this reach print. Also correct `10:52-53` and any tracker prose repeating the claim.

### Chapter 11

- **Three inputs chapter 11's routing turns on are pinned nowhere.**
  `11-where-people-are-put.pins.nibli` pins `severe`, `family`, `home` and the outcome
  across the cast and still leaves these untested — verified 2026-08-01:
  `? fit(Nando, Homestay). => FALSE`, `? family(Hano). => FALSE`,
  `? family(Lalo). => TRUE`. Three lines, and they matter because `family/1` is the
  input the chapter warns about at `11:14-21` — a pin naming `family(Hano)` FALSE
  against a man the chapter says has no family on record (`11:25`) is the cheapest place
  for that error to become visible.
  **Do not** add a pin "testing `fit/2` for a placement other than Homestay": `fit` has
  one producing rule and only ever carries `Homestay`, so `? fit(Ruk, HighSec). => FALSE`
  is a vacuous green of kind three **below**. When the three pins land, that warning is
  standing knowledge and moves to the standing section — it does not go with the bullet.

### Chapter 12

- **Chapter 12 enumerates the three entrenched articles and never says the evidence list is
  not among them.** `12-changing-the-rules.md:10-11` names the floor, the personhood rule
  and the register, all three pinned green — and stops. Chapter 1 argues at `01:202-217`
  that the evidence vocabulary is the one thing *not* on that register, and chapter 12 is
  where a reader arrives holding the register that would have protected it.
  `permanent(Art_Evidence). # => FALSE` is pinned in chapter 1's file and is not re-tested
  here, so the connection exists in the suite and nowhere in the prose. One sentence,
  connecting the register back to chapter 1's list. Cheap, and it is the difference between
  a reader noticing the gap and a reader being shown it — which is the register the whole
  book is written in. Read the vocabulary-entrenchment bullet below first: the honest
  sentence is that the list cannot be entrenched, not that it merely has not been.

---

- **Chapter 12's pin NOTE claims a pin that does not exist, and its defect is unmarked.**
  `12-changing-the-rules.pins.nibli:7-9` says the file "pins two live defects: the
  self-declared target (`Amend_Sneak`) and the fact that `become()` feeds nothing." The
  first is pinned, at `:53-62`; the second is not. It is now *pinnable* — a `:require`
  with a body-testing `awk` and a positive control, the shape chapter 8 already uses at
  `08-what-you-are-owed.pins.nibli:15-16`. Verified: the `become` body test returns
  nothing and the `/prisoner/` control returns twelve rules, so the pair runs green and
  can fail. Add it, and the NOTE becomes true as written instead of needing a correction.
  Second gap in the same file: the `Amend_Sneak` block pins a live defect and carries no
  `:defect` marker, so it reads as an ordinary green — the only pinned defect in the
  suite that does. Mark it, naming the repair that would close it.

### Chapter 13

No known defects. Read it against the constitution anyway.

### Chapter 14

No known defects. Read it against the constitution anyway.

---

## Constitution (KB) work

- **Add `~false($auditor)` to Article 4's reward rule.** `:485` is the only one of the
  three minting rules with no `~false` guard; `:459` and `:460` both carry one. **The
  witness is already in the shipped cast** and nobody has to be added: `false(Vex)` and
  `reward(Vex)` are both TRUE — chapter 5's carried-void auditor is still earning
  recognition for auditing. The fix is one conjunct; verified 2026-08-01 that the file
  loads at 0 errors, `reward(Vex)` flips FALSE, and `rights-floor` 91/91 and chapter 10
  12/12 stay green. See the chapter-10 prose bullet for the fork — enact or rewrite, not
  both.

- **`lose/2` is a leaf: clawback records a loss and retracts nothing.**
  Test it on the rule BODIES, not with a bare grep — `awk -F'->' '/^[^#]/ && /->/ && $1
  ~ /lose/' constitution.nibli` returns nothing, and the only enacted occurrences are
  `:483` and `:484`, **both rule heads**. (A plain `grep 'lose('` returns three lines,
  the third being commentary at `:137`; and a grep that matches a rule's own head is a
  check that can never fail — see the chapter-8 pin NOTE for the same trap caught live.)
  No rule reads `lose`, so nothing downstream changes when it fires. **Care with the
  witness:** `reward(Bela)` is FALSE in the shipped cast, so Bela alone does not show
  it. Add `judge(Bela, Ivo). capture(Bela, Ivo).` and then `reward(Bela)` and
  `lose(Points, Bela)` are simultaneously TRUE — recognition earned by a person whose
  recognition has supposedly been clawed back. So `06-clawback.md:3` ("what they earned
  goes with it") and `:5-8` describe an effect the constitution does not have.
  The apparent clawback in the shipped cast is entirely the `~false` guards on
  `:459`/`:460` **never minting**, not `lose` **taking**. `lose` belongs to the
  "determination, then stop" family — run the same awk test with each name to regenerate
  it rather than trusting a list here; today it is `lose`, `travel`, `become`, `decide`,
  `building`, Article 1b's `owe` and Article 8b's `obliged`. **`err` has left that
  family**: Article 8b reads it, which is where `obliged` came from.
  Derivation is monotone, so nothing can literally retract: the only expressible form
  of "taking away" is a guard on the minting rules, which is the fix above. If a
  downstream consumer is wanted instead, `all $x: lose(Points, $x) -> err($x,
  Recognition).` loads at 0 errors and derives for Bela and Cira. Rewrite `06:3`, `:5-8`
  and `:103` to say recognition is **never minted** rather than **withdrawn** — the
  chapter's ceiling paragraph at `:107-110` already reaches for the right register, so
  the cost is three sentences, not the section.

- **Guard Article 9's head — one asserted fact voids a *person*.** `:749` is
  `all $m: all $t: adjust($m, $t) & permanent($t) -> false($m).` with **no restriction
  on `$m`**, and `adjust` is an admitted name, so `adjust/2` is freely assertable. The
  single fact `adjust(Jala, Art_Floor).` gives, verified 2026-08-01: `false(Jala)` TRUE,
  `lose(Points, Jala)` TRUE, `travel(Jala)` TRUE, `decide(Jala, Ballot)` TRUE. No
  imprisonment — but Jala's credibility is destroyed and the clawback fires **without**
  two independent credentialed auditors, without `~parent`, without `~deceive`, without
  a clean epoch. Article 4's whole apparatus is defeated by one write, because Article 9
  reuses `false/1` as its amendment-invalidity proxy (`:747-748`) and never restricts the
  reused head to amendments. **The fix is free and re-verified**: appending
  `& suggest(Assembly, $m)` restricts the head to docketed proposals, uses no new
  vocabulary, and regresses nothing — `false(Jala)` FALSE, `false(Amend_Floor)` TRUE,
  `become(Amend_Floor, Law)` FALSE, `become(Amend_Mint, Law)` TRUE, `rights-floor` 91/91
  and chapter 12 14/14 still green. Splitting amendment invalidity onto its own predicate
  is the cleaner alternative and costs a corpus name — and, since Article 0a, an `admits`
  line as well.
  **Nothing blocks this and nothing waits on it.** The shield was ruled exposure-scoped
  on 2026-07-30 and is not coupled to `false/1`; the attack is unchanged and still live
  against recognition, which is the whole reason to do it. **Re-derive the line numbers
  before quoting them** — this bullet's have now rotted twice.

- **`clear/1` is a one-fact conviction nullifier.** `clear` appears twice: `:686`
  (`all $x: clear($x) -> permits(Appeals, $x).`) and `:814` (Nia's ground fact). No
  precondition, no author, no guard, no `derived_only` — and it is an admitted name, so
  Article 0a does not touch it. Asserting `clear(Adam).`, verified 2026-08-01:
  `permits(Appeals, Adam)` TRUE, `prisoner(Adam)` **FALSE**, `expresses(Adam)` FALSE,
  `travel(Adam)` TRUE. `prisoner(Adam). # => TRUE` is a pinned verdict at
  `rights-floor.pins.nibli:173`, and one write flips it. Note the asymmetry: the
  Sock/Puppet void takes six writes, springing a convict takes one. Fix: derive relief
  from an adjudication rather than a bare flag — `clear($x) & judge(Appeals, $x)
  -> permits(Appeals, $x)` is verified to stratify and needs no new vocabulary. **It is
  not free**: run alone it breaks Nia, `prisoner(Nia)` FALSE→TRUE and
  `permits(Appeals, Nia)` TRUE→FALSE, so `judge(Appeals, Nia).` joins the cast in the
  same commit and the suite returns to 91/91. Until it lands, `03:107-122` should say
  plainly that nothing constrains who records it — the section already says the relief
  follows by rule from a recorded fact, and stops one sentence short of who may record
  it.

- **Rename the Article 6 `dwell` head — one atom is doing two jobs, and it blocks the
  `err/2` repair.** Every rule producing `dwell` requires `prisoner` (`:576`, `:579`,
  `:591`, `:612`), and the Article 1 floor line at `:317` produces nothing — verified,
  `entitled(Bela, event { dwell() })` is TRUE while `dwell(Bela)` is FALSE. So
  `dwell(Lalo)` does not mean "Lalo is owed shelter"; it means "Lalo is housed at
  HighSec", and one atom carries both *entitled to a home* and *in a cell*. Free to
  fix, and a hostile reviewer finds it in an afternoon. Rename the placement head to
  `placed`, or fold it into `building`, and add the asserted counterpart the `err/2`
  fix needs. **Regenerate the site list by census before touching anything** — every
  `dwell` pin in `08`, `11`, `13` and `rights-floor` moves with it, and so does `08:50`.
  **Since Article 0a the asserted counterpart costs two lines, not one**: the new name
  needs an `admits` declaration above its first use, and it takes the evidence count off
  23, so `verify.sh:51` moves in the same commit.

- **Fix `err/2` — the placement alarm has never once fired correctly, and release gave it a third victim.** `:584` reads
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)`, which tests *having a home*,
  not *having been placed at home*. Verified 2026-08-01: exactly three people carry a
  `home` fact, and it fires on two of them — Ruk and Lalo, both routed correctly to
  `building(HighSec, ·)` — and on nobody misplaced. **Release made it worse rather than
  exposing it**: `free(Hano).` takes `fit` away while `home(Hano).` stays asserted, so
  the alarm now fires on a released man in his own house — `prisoner(Hano)` FALSE,
  `fit(Hano, Homestay)` FALSE, `err(Hano, Placement)` TRUE.
  **Three false positives, zero true positives** on the entire cast, and the newest one
  is not even in custody. That verdict is carried as a DEFECT PIN at
  `rights-floor.pins.nibli:277-282`, and four more pins now carry the `:defect` reason
  string "keying err/2 on where somebody was PUT, not on having a home" — two in
  `11-where-people-are-put.pins.nibli:73-81` and two in
  `14-when-the-system-notices-it-broke.pins.nibli:94,98` — so the repair reads as a
  resolved defect rather than a regression.
  An alarm with that record is worse than none. The fix is **not** "key it on `dwell`" —
  `:576` already requires `fit`, so a marker over the derived placement atom could never
  fire. The marker can only fire on an ASSERTED placement, so give the world a way to
  report one: a new asserted relation for "X was put at Y" (name from the committed alias
  corpus, plus an `admits` line), checked against derived `fit`. That is Article 0's own
  evidence/conclusion split applied to placement, and it is the same repair as the
  `dwell` rename — **do that one first**. Repairing it flips `err(Ruk, Placement)`,
  `err(Lalo, Placement)` and the released-Hano pin FALSE, so four files move in the same
  commit: `rights-floor.pins.nibli:78,281` (`:80` already pins FALSE and stays),
  `11-where-people-are-put.pins.nibli:73-81`,
  `14-when-the-system-notices-it-broke.pins.nibli:94,98`, and "The alarm that does not
  work" at `11:74-106`, written against the defect on purpose. That rewrite is the
  intended outcome.

- **Close `building` in Article 0 — it is shut by omission, and omission is the weak
  form.** The attack this bullet used to carry is **dead**: verified 2026-08-01,
  `building(HighSec, Ghosty).` is refused with "`building` is not admitted vocabulary",
  because Article 0a declares the record closed and `building` is not one of the
  twenty-four names. What is left is that it is closed by *not being listed* rather than
  by being declared, so anybody who later adds `admits("building")` for an unrelated
  reason reopens it in silence. `derived_only("building").` is one line, loads clean,
  leaves all three placements deriving and `rights-floor` 91/91 green.
  **Do not build the breach marker.** Every rule producing `building` requires `prisoner`
  (`:578`, `:592`, `:593`), so with assertion closed `building($f, $x) & ~prisoner($x)`
  is unsatisfiable — run verbatim it loads and derives nothing for anyone. **And the
  engine caveat attached to it is retired**: with `admits("building")` temporarily added,
  the body-only `$f` over a derived relation binds and the marker fires on the asserted
  placement while staying quiet on Ruk and Nando. That was the Article 8b limitation, and
  nibli has fixed it.

- **Write the fact-write trust base as a file-level section — two undefended classes,
  not three.** Articles 0 and 0a between them closed as much of the write surface as a
  compile-time check can: ten relations are `derived_only` and refuse direct assertion,
  twenty-four names are `admits`-ed, and anything else is refused as "not admitted
  vocabulary". The vocabulary class is therefore **closed** — that bullet is gone. What
  is left is what those two cannot reach.
  *Assertion*, and the enumeration is **generated, never hand-kept** —
  `grep -o 'admits("[a-z_]*")' new-book-plans/constitution.nibli` is the list; the
  hand-list this bullet used to carry had four errors, including `severe`, which Article
  0 closed in v0.5. Every headline attack is alive under an admitted name, all
  re-verified 2026-08-01: `public(Pax).` re-derives `authority(Pax)` and reopens E1a
  verbatim (`defend(Don)` TRUE, `prisoner(Don)` FALSE); `clear(Adam).` empties a
  conviction; six ordinary writes reproduce the entire Sock/Puppet void
  (`permits(Review, Sokk)` TRUE, `permits(Tribunal, Pupp)` TRUE, `false(Vict)` TRUE,
  `lose(Points, Vict)` TRUE — and `person(Vict)` FALSE, so the victim is voided and
  docked without ever being given a personhood fact); `broken(Court).` is a universal
  amnesty that frees every convicted person in the cast; `rotten(X).` is a single-writer
  universal void; one `deceive(Rebel, Boss).` jails the file's own honest whistleblower.
  *Deletion*, recorded nowhere, and it is the worse half — `admits` governs what may be
  written and says nothing about what may be removed. Both routes into standing are bare
  asserted facts, and the chapter suites turn out to be a deletion detector for free
  (re-measured 2026-08-01):
  ```
  # public(Court). deleted              04-the-shield.pins.nibli: 3 findings
  ✗ "authority(Court)." TRUE→FALSE  ✗ "defend(Sly)." TRUE→FALSE  ✗ "prisoner(Sly)." FALSE→TRUE
  # choose(Electorate, Boss). deleted   02-standing.pins.nibli: 4 findings
  ✗ "authority(Boss)." TRUE→FALSE   ✗ "defend(Rebel)." TRUE→FALSE  ✗ "prisoner(Rebel)." FALSE→TRUE
  ```
  Rebel — the file's own honest whistleblower, and the whole of chapter 2's argument —
  is jailed by deleting one line. Order the class `person` first, then `permanent`,
  `public`, `choose`, then the severity inputs: `severe` itself has no ground facts to
  delete, but deleting `cruel(Lalo, Mina).` moves Lalo out of high security, verified.
  Note also that Article 1b's `public(State).` (`:395`) is the sole route to
  `authority(State)` via `:643`, so one deleted line makes the duty-bearer unexposable.
  The file discloses this class for `permanent()` alone, at `:754-758`.


- **Guard the personhood roster — one deletion defeats all eight rights, and the
  obvious repair only renames the target.** `person` has two producing rules —
  `prisoner -> person` (`:329`) and `free -> person` (`:339`) — so imprisonment is the
  only route in that needs **nobody's permission**; the `free` route needs one written
  fact, and that fact is itself on the evidence list. Verified 2026-08-01 by deleting
  `:767` `person(Bela).` and changing nothing else: `entitled(Bela, event { eats() })`,
  `{ dwell() }` and `{ believe() }` all flip TRUE→FALSE, `travel(Bela)` and
  `decide(Bela, Ballot)` flip TRUE→FALSE, no `err` fires anywhere, and
  `become(Amend_Mint, Law)` stays TRUE — Article 9 entrenches rules, not facts, so it
  never notices. Article 1b follows the roster out of the door: `owe(State, Provision,
  Bela)` flips TRUE→FALSE in the same deletion, so the bearer stops owing the person at
  the instant they stop being one. The sharp part: `false(Bela)` and `lose(Points, Bela)`
  stay TRUE. **De-personing strips every right and leaves every sanction running.**
  Do **not** reach for `all $x: human($x) -> person($x).`: re-run 2026-08-01, it renames
  the roster rather than closing it — `person(Bela)` stays FALSE and `person(Adam)` is
  TRUE only off the prisoner route — and the breach marker meant to accompany it can
  never fire, because with that rule in force `person` always derives. No in-snapshot
  rule can tell a deleted roster entry from one never written. This is the deletion class
  above, and `person` is its first entry: disclose it as a cross-epoch proof obligation
  over the fact store, and stop looking for a rule. **The disclosure is done** (`01:219-254`);
  what remains here is the obligation itself. Do not re-derive the disclosure; extend it
  if the obligation gets built.

- **Declare `entitled` and `owe` `derived_only` — Article 0a already refuses the
  forgery, but by omission.** Verified 2026-08-01: `entitled(Sokk, event { eats() }).`
  and `owe(State, Provision, Sokk).` are both refused with "not admitted vocabulary",
  because neither name is in the `admits` block and neither needs to be — floor lines and
  Article 1b's rules compile to rules, not ground facts. That closes forging *the record
  of what is owed*, which is the one thing the floor is. What it does not do is say so:
  the relations are shut by not being listed, so an unrelated `admits` edit reopens both
  in silence. The declaration is free and was checked — with `derived_only("entitled").`
  and `derived_only("owe").` added, the floor still derives, `owe(State, Provision, ·)`
  and the eight itemised debts still derive, the actualities stay FALSE, and
  `rights-floor` 91/91 and chapter 8 30/30 stay green. Article 0 goes from ten closed
  relations to twelve.

- **Decide the Article 4 clawback question.** The two rules are `:483`
  (`false($f) -> lose(Points, $f)` — docks the wrongdoer, fairer, still a subtraction
  from a person's record) and `:484` (`teaches($t,$s) & false($t) -> lose(Points, $s)`
  — docks a **student** for a teacher's fraud: negative scoring, of a person, who did
  nothing). Verified: `lose(Points, Bela)` TRUE, `lose(Points, Cira)` TRUE. Legacy
  `book.md` bright line 2 — *"No negative scoring of persons"* — is contradicted by
  both, and note it is a **legacy** line recorded in `CLAUDE.md` under historical
  decisions, not one book-1 has adopted. Decide which side gives: either the bright
  line narrows to "no subtraction except by due process for one's own adjudicated
  fraud" and `:484` is deleted, or the clawback rules go and sanctions reach perks
  only. Do not leave both in print. Narrowing flips `lose(Points, Cira)` FALSE and
  rewrites `06:40-92`; that is the intended trade, `06-clawback.pins.nibli:6-16` records
  it, and the pin itself is already declared `:defect` so the flip reads as a repair.
  **Both middle options are closed, and the wrongdoer's closed last.** On the wrongdoer's
  side — where Bela and Vex really do hold recognition — the narrower rule would need
  provenance on `reward` to say which recognition came from the fraud, and that is refused
  (`CLAUDE.md`, 2026-08-01). So this fork has two branches and no third, on both halves.
  **The student middle option was closed first.** Since the grades ruling settled that students
  never mint, "claw back only the rewards that came from the fraudulent teaching" is the
  empty set for every student by construction — so narrowing `:484` is not narrowing, it
  is deleting it, and it should be decided as a deletion.

- **The delivery gap can be closed by fiat and nothing objects — record the *rule*-write
  trust base.** All eight floor predicates are rule-writable heads. Verified 2026-08-01:
  `all $x: person($x) -> P($x).` loads at **0 errors** for every one of the eight, and
  every floor query flips TRUE. The sharp part: the same fiat **silences the isolation
  audit marker** (`err(Hano, Isolation)` FALSE), so the one instrument that would have
  noticed goes quiet in the same edit. **Neither closure reaches it.** `derived_only`
  refuses the direct assertion and lets the fiat rule through — verified against a copy
  with `derived_only("eats").` inserted, `? eats(Adam). TRUE`. Article 0a behaves
  identically: none of the eight names is admitted, and all eight fiat rules load anyway,
  because `admits` closes ground assertion and says nothing about rule heads. So there is
  no compile-time guard available from either direction and the fix is disclosure: state
  in the constitution's commentary, and in the provisioning bullet below, that any
  provisioning layer must distinguish a delivery **record** — an evidence fact about
  something reaching a person — from a derived legal fiction. Otherwise the most
  credibility-buying admission the book has is one line and a green suite away from being
  erased.
  **Article 1b raised the stakes rather than lowering them.** Re-verified with the
  duty-bearer in force: the eight fiat rules still load, every actuality still flips
  TRUE, `err(Hano, Isolation)` still goes FALSE — and `owe(State, Provision, Bela)` and
  `owe(State, Eats, Bela)` are TRUE throughout, because nothing reads `owe`. So one edit
  now yields a constitution reporting a named debtor *and* every actuality satisfied: it
  reads as a discharged obligation rather than an undisclosed gap.

- **Build the first delivery route: verified teaching delivers learning. VERIFIED TO WORK,
  and it is the highest-value item in this section.** Nothing in this design touches the
  floor. Rule heads producing each floor right: `learn` 0, `eats` 0, `healthy` 0, `secure`
  0, `believe` 0, `meets` 0 — and the two that are non-zero, `dwell` (4) and `expresses`
  (1), derive only from `prisoner`. **Teaching does not produce learning**: `teaches($t,$s)`
  produces `reward($t)` and nothing else. So the society's only working provision runs
  through its prisons.
  A floor predicate may be a **rule head** — `dwell` and `expresses` already are, and
  INVARIANT 1 forbids only rule *bodies*. Re-verified on the live engine 2026-08-01: the
  rule `all $t: all $s: teaches($t, $s) & capture($t, $s) -> learn($s).` is **accepted**,
  the firewall still refuses `person & ~believe -> prisoner`, and the non-floor `~home`
  control still loads. Note it derives nothing as it stands — no teacher captures a
  student in the shipped cast — so force it before believing it: adding
  `judge(Bela, Cira). capture(Bela, Cira).` gives `learn(Cira)` TRUE.
  **Keep the entitlement and the actuality apart when writing it.** `entitled(every person,
  event { learn() })` stays unconditional; `learn(X)` becomes trackable. Written carelessly
  this reads as "you have the right to learn only if you passed", which is the
  eligibility-computation-upstream-of-rights structure the design refuses everywhere else.
  **And do not name it "verification".** Examining a person and recording a finding is
  already `judge` + `capture`, and borrowing them costs twice: two credentialed people from
  different bodies doing it to one person complete Article 4's multi-sig and **void them**,
  and the pair also fires Article 4's audit-reward rule at `:485` — the forced probe above
  mints `reward(Bela)` as a side effect, paying the teacher for an audit nobody performed.
  The probe uses `capture` deliberately to expose both; a real delivery rule needs its own
  predicate, which since Article 0a costs an `admits` line as well as an evidence entry.
  **The recognition half of the original proposal is refused and does not come back with
  this.** The 2026-07-30 grades ruling (`CLAUDE.md`) refuses marks for the student,
  counted degree on the reward side, and conditioning the teacher's `reward` on whether
  the student learned. None of that touches this bullet: `learn` is a floor actuality,
  not recognition, and delivering learning is not grading the learner. Build the
  delivery rule; do not let it grow a scoring head. `verify.sh` section 4b will refuse
  a rule that counts `teaches` entries, so the failure mode is caught rather than
  argued.
  This is also what unblocks the floor-proximity perks gradient, which cannot be computed
  while nothing reaches the floor at all.

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
  mechanism has changed.** Article 7 (`:614-646`) carries no stratification note. Adding
  `person($w)` to the shield rule at `:626` is the most natural tightening anyone would
  reach for, and it cannot be made either way. Re-verified 2026-08-01:
  - **Edited in place**: the rule is dropped and nothing replaces it. `nibli-pin`
    returns `HARNESS ERROR (exit 2) — pins not trustworthy`, so every chapter suite
    touching `defend` or `prisoner` stops meaning anything until it is reverted.
  - **Added alongside the original**: also a harness error now, naming the tightened
    copy's own line. This used to run green with one finding logged, and the change is
    in the harness, not the engine — `nibli-pin` no longer runs pins over a fixture whose
    line failed to load.
  **The hazard underneath is unchanged, and that is the part to write down.** Introduce
  the tightened copy through a pin file instead, so the fixture loads clean, and it is
  refused while the *permissive rule stays in force* — measured, `defend(Sly)` TRUE,
  `prisoner(Sly)` FALSE, `defend(Rebel)` TRUE, 4 pins, 0 findings. Exactly the "a
  permissive rule left in place keeps its exploit" failure the v0.2 header warns about at
  `:12-17`, now reachable through the stratifier rather than through oversight. Write the
  note against what it actually does: the engine names the cycle precisely and the runner
  stops, but only because the runner is watching — drop the "silently vanishes" framing
  and say that the silence was the harness's, and is fixed.

- **Resolve the polarity contradiction between Articles 6 and 7.** Article 7's shield is
  fail-**open** toward protection and defends the choice explicitly at `:619-625`.
  Article 6's `~permits(Appeals, $offender)` (`:521`) is fail-**closed** against
  protection and defends nothing. Since v0.3 relief is an asserted `clear($x)` feeding a
  derived `permits(Appeals, ·)`, so the *absence* of a granted relief is what convicts.
  Same file, opposite defaults on the absence of a finding, one justified and one silent.
  **The file now names the disagreement without settling it** — Article 6's severity
  polarity note at `:550-556` calls it "older than this revision and still unresolved" —
  so what is missing is the resolution, not the acknowledgement. Fix: either give the
  conviction rule its own explicit polarity note, or separate standing-to-seek-review
  from a granted relief that stays the sentence, or require an affirmative exhaustion
  fact for conviction. **Do not re-open the fail-open window in the chapter** —
  `04:57-81` defends the choice and `04:144-171` names the cost outright.

- **Give `rotten` — and `capture` and `judge` — an expungement path. URGENT: release
  landed and this did not, so the asymmetry is now live in print.** A single void is
  perpetual and compounds, with no route back, while a conviction can now be finished.
  That makes losing your credibility the harshest sanction in the design — harsher than
  imprisonment. Note the comparison it invites is with *standing*, the other sense, at
  `02-standing.md:42-43` (*"This is the only thing in the entire society that is
  protected that way. Everything else can be lost"*) and sits badly beside
  `10-contribution.md:50` (*"Nothing to earn it back with"*). The author decided on
  2026-07-29 that both halves are designed together; only the first half shipped.
  **The shape is known and cheap**, because it is the shape release used: an asserted
  expungement fact as a `~<expunged>` body conjunct on the multi-sig rule (`:482`) and on
  `rotten -> false` (`:680`). Both are safe — the predicate is stratum 0 and `false` is
  stratum 1, so no cycle. **Do not** put `~false` in a `false`-headed rule; the file
  records that exact attempt failing as E2 at `:23-26`, and it still fails.
  **Two sites are not enough, and this was measured.** With the conjunct on both, an
  expunged Vex has `false(Vex)` FALSE and the clawback stops — but `permits(Review, Vex)`
  stays FALSE, because Article 8's credential rules (`:656`, `:675`) read `~rotten`
  directly. Decide whether expungement clears the mark only or also returns the pen; if
  the latter, it is four sites, not two.
  Costs one more evidence entry (23 → 24), an `admits` line above its first use, and the
  matching move of `verify.sh`'s evidence check; the nine prose sites move again, so
  consider landing it in the same pass as the severity dimensions rather than alone.
  Worth framing in the book as forgiveness being a *right* rather than as a bug fix.

- **Put a precondition on `capture`.** `capture($a, $audited)` has no precondition
  anywhere: any credentialed pair — one Review, one Tribunal, since v0.7 — can void any
  person for no stated reason, and the book never admits it. The cross-body requirement
  raised the cost of assembling that pair and did nothing about the missing grounds. Needs one design decision — which predicate
  carries "grounds", since adding one enlarges the evidence vocabulary — after which
  the guard is a body conjunct. Pair with an epoch expiry on `capture` and `judge`.

- **Widen kinship beyond `parent/2` — the fix is available today, and it is not free.**
  Article 4's independence check names one relationship (`:493`), so spouses and siblings
  co-sign. **Not blocked on the engine**: `married` (speni), `brother` (bruna), `sister`
  (mensi) and `sibling` (tunba) are all in nibli's committed alias corpus — cite them by
  name, never by line. Verified 2026-08-01: appending `~married`/`~brother`/`~sister` in
  both directions loads at 0 errors and leaves `false(Bela)` and `false(Lupo)` TRUE,
  `false(Tyr)` FALSE. And the cross-body probe now has a verdict rather than a stale one:
  with `admits("married").` and `married(Gia, Hex).` added, `false(Bela)` flips **FALSE**
  — the shipped cross-body pair stops co-signing, which is the demonstration.
  **The cost is what needs deciding, and it is the only thing left open here.** Three
  evidence entries (23 → 26), three `admits` lines, and the matching move of
  `verify.sh`'s evidence check — and enlarging the vocabulary is the quietest way to
  capture a system, the file's own threat model. Chapter 5 is already honest either way:
  its costs section says the words exist, the widening has not been judged worth it, and
  discloses that as a choice. So what remains is only whether to land the rule.

- **Check each governance item against what the rules can express, before any prose.**
  Parts I–V are gated on derivation, and the constitution has no predicate for a
  community, a transfer, a tax, or a term of office — so none of the following is
  derivable today and all of it is constitution work first. In dependency order:
  - Recall is one asserted `broken(·)` fact (`:852`), consumed by the two credential
    rules at `:656` and `:675` — at-will, no threshold, no administering body, no term.
    Replacing it also rewrites `02:55-62` and `03:82-96`, which describe it as is.
  - The magnet problem: mobility is derived at `:443` and there is no community concept
    at all, so "generous communities attract need" cannot currently be *stated*, let
    alone answered. Standard fiscal-federalism territory; it needs vocabulary first.
  - Justice material: standards of proof, proportionality, an appeals path independent
    of the recognition apparatus, and who inspects placement under Article 6.
  - Portability of entitlements, so exit from a hostile community is not destitution —
    blocked on the same missing community concept.
  Every one of these enlarges the evidence vocabulary **and the Article 0a `admits`
  block**, and moves `verify.sh`'s evidence count. Price that in rather than adding
  predicates one at a time.


---

## The verification harness


- **Pin the three Article 0 closures that nothing guards: `defend`, `reward`, `become`.**
  Article 0 closes ten relations and the file says those closures are "what makes
  Articles 4, 6, 7 and 8 mean what they say". Repo-wide only seven have a `:refuse` pin.
  The three unpinned ones are the shield, the mint and the enactment gate — the heads of
  Articles 7, 3 and 9. Verified that all three refusals hold today and the pins go in
  as-is. Add to `rights-floor.pins.nibli` beside the other seven and bump `:expect-pins`
  from 91 to 94. Ten minutes' work, and without them the file's own named failure mode
  at `:83-86` — a `derived_only` line moved below the facts it guards "is inert and looks
  identical" — takes three of the ten gates with it in silence. Note the contrast Article
  0a supplies: `admits` refuses a late declaration outright, as "comes too late", so
  Article 0 is now the one whose ordering hazard the engine still cannot see.

- **The floor's own relation is queryable in two places and controlled in none.**
  `grep -rn entitled book-1/*.pins.nibli new-book-plans/rights-floor.pins.nibli` returns two,
  both added with Article 6 release: `rights-floor.pins.nibli:256`
  (`entitled(Hano, event { eats() })`) and `13-the-one-thing-taken.pins.nibli:90`
  (`entitled(Hano, event { dwell() })`). Neither is paired with a control, so both still
  prove reach rather than derivation. (A third sits in
  `counterfactual/no-person-line.pins.nibli:14`, where the fixture itself is the control.)
  The queryable shape discriminates in three directions at once, re-executed 2026-08-01:
  `? entitled(Adam, event { eats() }).` TRUE — the floor reaches a person;
  `? eats(Adam).` FALSE — and does not fabricate it;
  `? entitled(Adam, event { home() }).` FALSE — home is not on the floor;
  `? entitled(Court, event { eats() }).` FALSE — and it does not reach a non-person;
  `? entitled(Hano, event { meets() }).` TRUE — including the convicted.
  This is not a nicety: `08:31` turns the whole chapter on exactly this contrast — "Ask
  whether Bela eats. Not whether Bela is *entitled* to eat — whether Bela eats" — and the
  pin file pins only the second half. Add
  `? entitled(Bela, event { eats() }). # => TRUE` beside `? eats(Bela).` in chapter 8,
  one `entitled` pin for Zed in chapter 7, and the `home` and non-person controls in
  `rights-floor.pins.nibli` — without the controls the pins above pass for the wrong reason.


- **Write down what FALSE means in a pin file — it means three different things and two
  of them are worthless.** All three re-executed 2026-08-01, and the distinction is why
  five false prose claims survived 180 green pins:
  - A **corpus name the KB never mentions** answers FALSE and passes cleanly:
    `? rich(Bela). => FALSE`. It is a real verdict about a name nothing could have made
    true, which is not the same as a real verdict about the design.
  - A **non-corpus name** is not a FALSE at all, it is an abort: `nibli-pin: HARNESS
    ERROR (exit 2) — pins not trustworthy`.
  - A **well-formed query on an argument the relation never carries** is a vacuous green
    that passes forever: `? fit(Ruk, HighSec). => FALSE`, `? lose(Standing, Bela). =>
    FALSE`.
  Only the first is a verdict at all, and only when something in the KB could have made
  it TRUE. Put this in the shared header block of the pin files — three sentences —
  because the pin suggestions that arrive from reviewers are disproportionately of kinds
  two and three, and a reader cannot tell them apart by looking. Be exact about what
  Article 0a changed: `admits` closes the *assertion* side, so a widened evidence
  vocabulary is no longer invisible — appending `rich(Esa).` to the constitution now
  aborts the run instead of passing green — but a *query* on a name the file never
  mentions still answers a clean FALSE, so kind one is untouched.

- **The eight floor rights are sampled, never enumerated — and the omitted one is exactly
  where the claim fails.** `08:32` says "the same answer comes back for every one of the
  eight", and the pin file tests seven, omitting `expresses`. Chapter 7 is worse: the
  comment at `07-a-prisoner-is-a-person.pins.nibli:29-32` says "the floor derives for Zed
  like anyone" and pins one right of the eight. Eight pins per subject is not expensive
  and it is the only shape that makes "every one of the eight" a checked sentence rather
  than a summary. Put the pin block in **before** the chapter-8 rewrite, so the rewrite
  has something to write against.

- **Chapter 12's pin file is the last one whose header argues instead of checking.**
  `12-changing-the-rules.pins.nibli:7-8` says the "three ways this is thinner" section
  "pins two live defects", and neither half is true as written. The second — that
  `become()` feeds nothing — is an absence no pin can hold, and `verify.sh` already holds
  it in the absence loop. The first is real and is marked with a bare `# DEFECT:` comment
  at `:53` rather than the `:defect` directive chapters 6, 11 and 14 adopted, so the file
  reports `14 pins, 0 findings` and declares nothing, while the marker that would say what
  the *repair* is stays invisible to the harness. Verified: marking both `Amend_Sneak`
  pins runs green at `14 pins (2 defects), 0 findings`. Fix the header to name one
  declared defect and one guarded absence in the same pass. This is a header that drifted
  from its own file undetected, which is the whole argument for reading every NOTE against
  the check that now runs it.

- **Extract the claim-to-query table from the pin files — it cannot be generated from the
  constitution.** The substance already exists in a better form than the old bullet
  imagined: fifteen pin files carry every load-bearing sentence, every one a query with an
  enforced expected verdict, all green, and a scan finds no `?` query lacking a `# =>`
  line. What is left is the rendering, and it runs the other way round: the constitution
  cannot know which sentence of chapter 11 a query backs, so the table must be extracted
  from the pins rather than derived beside them. Blocked by a data gap — of the `?`
  queries under `book-1/`, half again as many have no comment line directly above as do,
  so an extractor run today leaves most of a chapter's sentence cells empty. (Measured
  2026-08-01 at 128 of 253; re-run the count rather than carrying those forward.) Fix:
  settle one machine-readable form for the sentence — a `# "…"` line immediately above the
  query is already the majority convention — backfill the rest, then have the verification
  script emit the table as a by-product.

- **Freeze `4-strata.py` as an exhibit rather than fixing it.** The defect is real and
  still present: the fact branch takes only the first predicate on a line (`:52`, `:54`),
  so `entitled(every person, event { secure() }).` registers as a fact of `entitled` and
  nothing else — and the declaration keywords `derived_only` and `admits` register as
  predicates in their own right. Repairing it now buys nothing and costs something.
  Nothing consumes it: `5-spine-gen.py` takes strata, base/derived and edge polarity from
  `nibli-pin --strata` and owns the generated region of `3-spine.md` — and
  `3-spine.md:36-39` keeps the discrepancy deliberately, as "the tooling-blindness story
  for the method part", so fixing the script deletes a planned exhibit. Give it a header
  saying it is retained wrong, on purpose, and naming what it is blind to: run against the
  same constitution on 2026-08-01 it reported 46 predicates, 19 derived and 48 rules where
  the engine reported 50, 26 and 56.

- **`5-spine-gen.py`'s rule count is still text-derived, and only recognises a universal
  when it wears the floor's shape.** `text_facts` counts a line as a rule if it carries an
  arrow, or if it matches the `FLOOR` regex at `:47` — `PRED(every <domain>, event { P() })`
  and nothing else. Any *other* universally quantified line is counted as neither.
  Executed 2026-08-01 against a scratch copy with Article 1b written back as
  `owe(State, Provision, every person).`: the generated block came back identical except
  that rules read **55** instead of 56. **The worse version of this is closed** — the head
  failing to enter `head_preds`, `owe` emitted as an evidence predicate, and the generated
  list silently reading twenty-two against chapter 1 — because base/derived and strata
  have come from the engine since `93da52f`. What is left is a figure the method part will
  print being quietly one low. Fix by taking the rule count from the engine's dump as
  well, or by widening the regex to any `every <domain>` in any place.
  **Land the constitution's comment in the same pass**, because it now states the closed
  version as if it were live: `constitution.nibli:363-367` cites `5-spine-gen.py:25` and
  says the evidence list "silently becomes TWENTY-TWO". Verified false. The instruction it
  ends with — do not restore the short form — stays right for a different reason now: it
  is the form nothing counts. Regenerate the three counterfactual fixtures with it; they
  carry the same paragraph.


---

## book-1 — remaining writing

- **Write the opening note — the last unwritten non-derived element, and nothing else
  tracks it.** ~800 words before Part I, explicitly non-derived and labelled the way Part V
  is labelled, so the book does not open cold on vocabulary; it claims no derivation and
  carries no verdicts (`new-book-plans/3-spine.md:123-126`). One of exactly three sanctioned
  exceptions to the inclusion gate. No file exists. Write it against the final wording,
  which is settled: *The Rights Nobody Has to Earn — A design for a society worked out to
  the point where it catches its own failures.* **Check the note against the counted-claims
  ratchet before committing it** — it will be the first prose in `book-1/` the ratchet has
  ever scored, every other file predating it. The subtitle itself is clean; a note that
  opens by naming the floor's size would not be.

- **The honesty paragraph goes in the opening note, and half of it is already in print.**
  book-1 has no introduction, so the destination this item used to name is gone. One half
  has landed: *the system proves what is owed, not that anything arrives* is stated hard in
  `08:27-46`, leaned on again where chapter 13 says only speech and shelter arrive and only
  for prisoners (`13:163-164`, `13:181-184`), and again where chapter 14 names what the
  design delivers (`14:32-33`, `14:83-87`). The other half is in no chapter — that a
  formalisation makes commitments **precise**, never **justified**; nothing in logic says
  the floor should contain expression and not water. Put that half in the opening note and
  have it point forward rather than restate chapter 8, or the book opens by spending its
  strongest admission before the reader knows what was admitted.

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


**The capture joint answers Ambedkar by name.** Caste as a design problem rather than a
  historical footnote — reserved committee representation, and external audit of allocation
  patterns, the second of which is already this part's worked example of a specification
  stated as a property ("allocation patterns by group are published in a form an outsider
  can check"). Part V is exempt from the derivation gate, which is exactly why this belongs
  here and not in a computed chapter.

**The state joint carries two sentences nothing else in book-1 can.** *Concede coercion
  in plain words* — a body obliged to provide at scale is funded compulsorily, and a reader
  who notices the word being avoided stops trusting the rest; `grep -rn "coercion\|social
  democ" book-1/` still returns nothing. *State the positioning outright* — the ends are
  social-democratic and the provider is a fiscal agent; the novelty is the constraint
  mechanism, not the absence of a provider. Said plainly, "social democracy with extra
  steps" loses its teeth, because the extra step is a compile-time prohibition nobody else
  has. Neither can go in Parts I–IV, and the reason is the inclusion gate rather than
  taste: the constitution has no vocabulary for a tax, a transfer or a community, so the
  *fiscal* character of the bearer is not derivable and chapter 8 can only say a public
  body owes the eight to every person. Chapter 8 sets this up and does not spend it —
  `08:98` names the body, `08:138` says nothing compels it — which is the true state of the
  design and exactly the question this joint has to answer. The earned-time concession from
  the release ruling lands at the *coercion* joint next door: "voluntary" is structurally
  pressured when the alternative is longer confinement.
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


- **Before the method part prints a rendered sentence or a proof trace, check who the duty
  names.** nibli carries a filed defect — its tracker bullet **"`obliged`-spelled every-duty
  renders the wrong obligated party"**, re-verified upstream as still reproducing on
  2026-08-01 — where the deontic collapse picks the event variable as duty-holder when
  back-translating the **base** spelling, which is ours; the converted `obligated_by`
  spelling binds correctly. Cited by title and never by line: that file's line numbers
  rotted twice inside one exchange. It cannot reach a reader today, because this repo runs
  `nibli-pin` and never renders prose — which is exactly why the gate is the moment the
  method part ships rendered English or a trace. Do not hand it off as a prompt: it is
  already filed upstream and the fix is in their renderer.
- **"The Furnished Prison" — a rejected title that is a good part title.** Scored highest
  of the twenty title candidates on pick-up and lowest on legibility, so it lost the cover
  and is wasted sitting in git. It is the phrase at
  `13-the-one-thing-taken.md:184-186` — *"A society whose only working provision runs
  through its prisons has not built a floor; it has built a prison that happens to be
  furnished."* Candidate for a Part title, the back cover, or a launch-essay headline,
  none of which are decided yet. Kept here because the title work is done and this is the
  one asset from it that outlived the decision.

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

- **Expand Parts I–IV from 21,038 to ~38,000 words.** DECIDED 2026-07-29; the invariant and
  the budget are in `CLAUDE.md`. **Re-measure with `wc -w book-1/*.md` before planning
  against this figure** — it has been wrong every time anybody checked it, and it moves with
  every chapter pass. This is the largest single item in the tracker — roughly +17,000
  words, mean chapter ~1,500 → ~2,700 — and it is one bullet only because the work is one
  decision; it becomes fourteen commits. **Know what it is not:** the invariant does not
  force it. Break-even is derived > 17,800 and Parts I–IV already clear it, so
  majority-derived holds today with no expansion at all. The 38,000 is an editorial choice
  about the book's size, and it means Part V's 12,000 must be justified by content rather
  than by ratio.


  **Every chapter revision also strips its counted claims.** A per-chapter check, not a task
  of its own; the rule lives in `CLAUDE.md` and the guard in `verify.sh` section 3b. What
  this bullet is for is where the work still is. The ratchet stands at `BASELINE=25`: it
  fails if the count rises, and it also fails if the count falls without `BASELINE` being
  lowered in the same commit, so the tightening cannot be forgotten. When it reaches zero,
  make it a hard gate. **Read the current sites off the guard, never off a list in this
  file** — run the `COUNTED` grep in `verify.sh` and it prints them. Today they cluster in
  the chapters that talk about the floor — 7, 8, 9 and 13 — and nearly every one is the same
  "eight" claim, which goes away by stating the rule that produces it. Two are a different
  problem and are worth doing first: **chapters 9 and 14 count chapters** ("twelve chapters
  later", "fourteen chapters"), which the computed spine can invalidate silently with no pin
  able to catch it. Rhetorical durations ("thirty years") are exempt and allowlisted.


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

  - **Do NOT use the floor claim — and write down the regression exactly as it was run.**
    Its headline finding ("democracy behaves like a floor on subjective wellbeing, not a
    lift toward the top", p = 0.0004) is the one claim the source never controls for
    income, and it does not survive. Re-derived from the CSV 2026-08-01: take the residual
    of `whr2025_life_eval ~ eiu_2025 + Log GDP per capita`, regress its absolute value on
    both, and democracy is b = −0.0196, t = −0.91, **p = 0.37** while income is b = −0.336,
    t = −2.53, p = 0.012. The residual definition is load-bearing: taking it from the
    democracy-only fit instead gives democracy p = 0.077, a real but much weaker refutation.
    State the specification or the refutation cannot be checked. **Drop the "within income
    tertiles the dispersion goes the wrong way" line** — under the specification above it is
    not what the data show: corr(democracy, |residual|) by income tertile is −0.165, −0.197
    and −0.071, all three negative, so dispersion falls with democracy in every tertile and
    reverses in none. **The three figures this bullet used to print — −0.140, −0.126,
    +0.008 — reproduce under none of the three natural residual definitions** (full-model,
    democracy-only, income-only), which is the failure the sentence above warns about,
    committed one line later: a tertile number without its specification cannot be checked.
    The claim still dies; it dies on the income control alone. This is precisely the claim
    book-1 would most want to be true — a floor effect, in a book about floors — which is
    exactly why it must not be used.

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

## Legacy harvest — before `book.md` and `manifesto.md` are deleted


- **Settle the Bharati attribution, then decide whether book-1 opens with an epigraph.**
  The full poem with Tamil original and translations lives in `book.md`'s closing appendix,
  attributed there to *Yoga Siddhi* ("Varam Kettal"), stanzas 4–5, and sourced to Project
  Madurai (`book.md:2838`, `book.md:2967`). **The mapping is already recorded, and it is
  recorded wrong.** `new-book-plans/1.md:12` carries the manifesto's sixteen-chapter mapping
  onto the sixteen lines — eight of lament and eight of petition, which is why Part 1 is
  diagnosis and Part 2 is demand — and that file is planning material rather than one of
  the two going, so the craft is not at risk. What is at risk is the name: `1.md` attributes
  the frame to *நின்னைச் சரணடைந்தேன்*, a string that appears nowhere in any artifact except
  that one sentence, while the manifesto's own Part 2 Ch 1 epigraph is நின்னைச்
  **சிலவரங்கள் கேட்பேன்** (`manifesto.md:202`), which `1.md` appears to have garbled into a
  title. Confirming the correct name against a Tamil-literature source is plain research and
  unblocked, and fixing `1.md:12` is the deliverable. **[AUTHOR-GATED]** is the second half:
  whether book-1 opens with an epigraph at all — at most **one**, original, plain
  translation, one sentence on who Bharati was, never as structure.
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

- **Harvest the day-in-the-life technique, not the prose — and fix the citations.** The three
  vignettes are at `book.md:981-984` (merit points), `1395-1398` (shelter, mobility,
  communication) and `2560-2563` (governance) — all three verified in place; the ranges
  previously cited here landed on tech-UX bullets and legal-collision prose instead. All
  three are second-person and generic and two are MVS-framed, so nothing ports verbatim.
  book-1 is also no longer without a narrative register — every chapter is built on a named
  case, and Hano runs through most of the book. What is actually missing is the **domestic**
  register: a household carried through food, care, housing and crisis, rather than a
  defendant carried through a procedure. Decide whether Part V gets one, since Parts I–IV
  are derivation-gated and cannot hold it.

- **Finish the floor corrections in book-1 — two remain.** **`dwell` is nowhere glossed in
  prose as protective shelter** — `grep -rniE "weatherproof|ventilat|plumb|sanitation"
  book-1/` still returns nothing, so ch 8's "somewhere to live" carries the whole weight and
  the water-and-sanitation case is not absorbed; write the gloss into ch 8 now, it costs a
  sentence. And **privacy is not argued down anywhere** — book-1 has one incidental use of
  the word (`04:42`, "a private person"), and the argument that encoding it as a defeasible
  right lands it at stratum 3 and destroys the single-deprivation theorem is Part V material.
  That half waits on Part V; the `dwell` half does not.

- **Then delete both files, in one commit, with the harvest manifest in the body.** Not
  before. The commit message is the record of what was taken and what was consciously
  dropped.

---

## Hold for book-2 — do not work these here


Parked, so they are not lost when the legacy files go. These become the seed of book-2's
tracker, written from scratch after book-1 ships.

- **Oversight of the duty-bearer — enablers, their checkers, and the meta-study.** Raised
  by the author 2026-07-31 while ruling the homeless-convict gap: if shelter is owed and
  somebody has none, the people who deliver it should have to study why, and somebody
  else should have to check on *them*. Right instinct, wrong book. In book-1 terms it
  duplicates two mechanisms that already exist and are deliberately inert — `owe`, which
  nothing reads (`08:138`, "Nothing compels the body"), and `err`, whose only consequence
  is Article 8b's `obliged`, which nothing reads either. And the constitution has no
  vocabulary for a study, an inspection, oversight, a community or a transfer; verified
  again 2026-08-01, the grep returns one word inside a comment and no relation. So this is
  institutional design with a lexicon ask under it, which is book-2's subject exactly.
  **Its book-1 half is done** — the `err`-feeds-an-obligation decision was ruled and
  enacted as Article 8b. Do not build the structure here.

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

---

## Standing facts and methods — not tasks, and not history

Landed work is not recorded here; that is what git is for. What survives is the small
set of things a command cannot teach you and a rename cannot re-derive.

```
./verify.sh            # ~30 s: spine, evidence count, jargon, counted-claims ratchet,
                       #        absences, INVARIANT 1, the counting guard, control scope,
                       #        engine build, the pin suite, counterfactuals
./verify.sh --quick    # ~2 s: everything except the pin suite AND the counterfactuals
```

Prefer it to any check by hand. It exits non-zero on the first failure and names the
claim that stopped being true. Use the **release** `nibli-pin`, never `nibli-host`. The
script builds the engine itself and prints the commit, because a stale binary is
invisible here — the pins check the constitution, not the engine, so an out-of-date
build returns the same green and the same runtime.

**Every check was negative-controlled before it was trusted, and one failed the
control.** The jargon pattern this file used to specify (`stratum|strata`) does not
match *stratifier* — the likeliest leak of all, since it is the word this tracker uses
constantly — and a chapter containing it passed; `strat` alone is too greedy, it matches
"demonstrate". The shipped pattern uses three explicit stems. For the same reason every
structural check carries a positive control: a grep that also matches a predicate's own
rule head can never fail, which is a trap this repo fell into twice in one day.

**Extending it as the book grows is the standing job**, and a new check earns its place
by failing against a sabotaged copy before it is trusted, never after.

**Two facts about the floor that no command teaches.**

- **A floor line is a compile-time prohibition, not a declaration**, and since Article 1b
  it covers the duty as well as the eight rights. `entitled(every person, event { P() })`
  compiles to a rule with `person` in the body, so `P` sits downstream of `prisoner`; any
  later rule taking `~P` into that cone is an unstratifiable negative cycle and is
  refused. The floor is protected **because** it is reachable — at stratum 0 there would
  be no cycle to close and no protection at all. Where it stops is pinned in
  `08-what-you-are-owed.pins.nibli`: `~P -> false`, `~P -> lose(Points, ·)` and positive
  compulsion `prisoner -> P` all still load — each under `:accept-scoped`, so the control
  proves loadability without leaving the forbidden shape resident. It blocks punishment for
  ABSENCE, never manufacture, and it reaches `prisoner` only. Upstream the asymmetry is
  pinned by the `rights_floor_*` tests in `nibli-engine/tests/integration.rs` together with
  their negative control `punishment_rule_alone_is_stratifiable` — **cite them by test
  name, never by line.** That citation has already rotted once and a line range is exactly
  what a rebase in another repo breaks silently.
- **The widening hazard is rule-head position** — not place index, not the predicate.
  `every`/`all` forms widen the protected set; ground facts and `some` are inert. It
  cannot be banned, because the widening *is* the firewall, so the guarantee is the
  complement pins rather than a compile-time rule.

The graph counts live in exactly one generated place, `3-spine.md`'s stratification
block. `4-strata.py` disagrees with it and is blind to the floor by construction.

**Four disciplines, each learned by being burned.**

- **Re-derive a site list by census before executing any rename.** A list written in this
  file is a snapshot and every commit since is an invalidation. The v0.6 rename list
  missed one site outright, omitted two from its leave-alone list so a mechanical pass
  would have renamed them, and predated four occurrences a later pass introduced. Line
  numbers in it had rotted by 38.
- **Citation remaps must cover every file a commit touched**, not just the one being
  edited — a careful remap still rotted three citations because it was scoped to one
  file while another was edited in the same pass. Content-match against
  `git show HEAD~1:<path>`:
  ```
  python3 - <<'PY'
  import re, subprocess
  F='new-book-plans/3-spine.md'
  old=subprocess.run(['git','show',f'HEAD~1:{F}'],capture_output=True,text=True).stdout.split('\n')
  new=open(F).read().split('\n'); todo=open('TODO.md').read()
  for m in re.finditer(re.escape(F.split('/')[-1])+r':(\d{1,4})', todo):
      a=int(m.group(1))
      if a>len(old) or not old[a-1].strip(): continue
      hits=[i+1 for i,l in enumerate(new) if l==old[a-1]]
      if a not in hits: print(m.group(0), '->', hits or 'GONE', '|', old[a-1][:50])
  PY
  ```
  Bare `:NNN` citations inheriting a filename from earlier in the sentence are **not**
  caught by this and still need reading by eye.
- **A rule that gets stricter can make an existing pin vacuous without flipping it**, and
  nothing in the harness can see that happen. When v0.7 required two bodies, a pin that
  had tested the epoch-carry guard began failing on body-difference *first* — still
  green, testing nothing. Check what a pin proves after tightening the rule it sits under.
- **Check whether a quantifier has anything to range over before blaming the quantifier.**
  "Different bodies" was parked as an engine limitation when the real problem was that
  `permits/2` had exactly one audit-pen issuer, so the quantifier had nothing to range
  over.

- **The rule that decides whether expansion is cheap — re-verified 2026-08-01 against the
engine-driven generator.** *Ground facts over predicates that already occur in the
constitution are structurally free. Anything that introduces a predicate name, or a rule
head, is not.* Since `5-spine-gen.py` takes its strata from `nibli-pin --strata` rather than
from a regex, "free" means the engine reports the same graph: appending `person(Nova).
work(Nova, Census). clear(Nova).` to a copy of the constitution leaves `5-spine-gen.py
--check` reporting the spine current — predicate count, derived count, rule count, strata,
the floor list, the evidence list and therefore chapter order all unmoved. A body conjunct
is free too; the rule count counts arrows, not literals.

**A new predicate name costs more than a number now, and in one case costs nothing at all.**
Article 0a closed the record, so an unadmitted name does not load — `studies(Cira, Hano).`
is refused with *"`studies` is not admitted vocabulary"* until `admits("studies")` is written
above it, which is the visible, reviewable edit the closure exists to force. Admit it and
write it **only as a ground fact** and the evidence figure does not move at all: measured,
`nibli-pin --strata` never reports a predicate that appears in no rule, so the generated
block comes back byte-identical and `verify.sh`'s gate on 23 sees nothing. The 23 → 24 cost
lands when the name enters a **rule** — measured, predicates 50 → 51 and rules 56 → 57 with
it. A **new rule** may also add a stratum, which would add a chapter, which the computed
order forbids.

**Structural freedom is not verdict freedom, and this is what will actually bite.**
Article 4's multi-sig quantifies over two auditor variables, so a new person naming
*existing* constants can complete a rule no existing pair could satisfy: four facts
(`person(Ann). choose(Electorate, Ann). judge(Ann, Tyr). capture(Ann, Tyr).`) flip
`false(Tyr)` FALSE→TRUE and destroy chapter 5's headline case — re-executed 2026-08-01,
still true. **Every argument position in every new fact must be a new constant**, except the
four institution constants — and even those need care, since `judge(Review, ·)` is the
deceit adjudication and `broken(Court).` is a universal amnesty. The rule is a heuristic;
`verify.sh` is the proof.

- **The five legacy bright lines were swept against the enacted rules; only BL1 ported.**
  **BL2** ("no negative scoring of persons") is refuted by the constitution, not merely
  unimplemented — `lose(Points, Cira)` derives TRUE, docking a student for a teacher's
  fraud — and the decision it forces is the Article 4 clawback question. **BL3** ("merit
  never weights votes") survives vacuously: there is no arithmetic anywhere in the
  enacted lines and `verify.sh`'s digit ban keeps it that way, so weighting cannot be
  written. **BL4** and **BL5** are pod-and-tech-stack material and belong to book-2.
  **BL1** ported in narrowed form and is in chapter 1's closing section: the floor is
  unconditional *above* `person($x)`, and `person` is a roster of written facts with two
  producing rules, so personhood **is** an enrolment. Do not restate the unnarrowed BL1
  in book-1; it would be false the way BL2 is false in `book.md`.

- **Entrenchment cannot protect the evidence vocabulary, and the reason is structural.**
  `permanent(Art_Evidence).` was applied verbatim and run: it kills an amendment that
  DECLARES that target and kills nothing else. `adjust` is self-declared by the proposer,
  so an amendment naming no target enacts and one naming a harmless target enacts too.
  **Entrenchment guards targets a proposer admits to; the vocabulary is not a target, it
  is the store.** Article 0a closed the quiet route — an unadmitted name is refused at
  assert time — but that makes widening *visible*, not *hard*, and nothing entrenches the
  `admits` block itself. So the honest sentence, in chapter 1 and chapter 12 alike, is
  that the list **cannot** be entrenched, not that it merely has not been.

- **`--allow-shell` stays opt-in, and do not ask upstream to make it unconditional.**
  nibli's pin language is closed by design — nothing under their `pins/` may reach outside
  the repo, and their own gate never passes the flag. We control our own invocation, so the
  gate costs us one flag in `verify.sh` and protects a guarantee that is theirs to keep.

- **An extra argument on a derived relation costs about 22x, and the cost lands in one file.**
  Measured 2026-08-01 on the release engine: rewriting all three `reward` heads from arity 1 to
  arity 2 takes `rights-floor.pins.nibli` from **15.07 s to 337.50 s**. A single probe is
  unaffected — it answers in about a tenth of a second either way — so the cost is not in the
  query, it is in re-saturating per pin, which is nibli's own open item *"Materialisation:
  incremental re-saturation (C3)"*. Two older figures for this are dead and should not be
  quoted: a claimed non-termination past fifteen minutes never reproduced, and a 38.9 s-against-
  2.1 s pair predates the `event { }` projection. This is the answer to "how expensive is one
  more argument here", which is the question anybody proposing one will ask first. It is not an
  argument against a second place on `reward`; that is refused on other grounds, and they are
  in `CLAUDE.md`.
