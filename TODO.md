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
  below. The five bright lines are already swept — the result stands under
  **Standing facts and methods**, and only BL1 ported, narrowed — leaving one open
  consequence, the Article 4 clawback decision in the Constitution section. It all
  ends with the deletion commit.

**THE WORKING ORDER, and it is three phases, not a priority list.** This file is
arranged in the order the work happens. Do not skip ahead: each phase removes
constraints the next one would otherwise have to work around.

1. **Phase 1 — author-gated decisions.** First, because several chapters cannot be
   revised until the decision above them is ruled — the ruling *is* what the chapter
   says — and because a lost decision costs more than any lost task; this section has
   been destroyed by tooling once and is watched accordingly.
2. **Phase 2 — engine handoffs (nibli).** Empty at the moment — nothing is pending
   upstream. It stays ahead of the chapter passes because some of what the book has to
   concede is an engine limitation rather than a design choice, and it is dishonest to
   write the concession while the limitation is fixable.
3. **Phase 3 — chapter passes, chapter 1 through 14, in order.** One chapter at a
   time: read it whole, fix what is false, revise what is thin, verify, commit,
   move to the next. The per-chapter bullets below are what is already known to be
   wrong — they are a floor for that pass, not its scope.

The sections after phase 3 are cross-cutting: constitution work that no single
chapter owns, harness work, the remaining book-1 writing (the opening note,
Part V, the method part), the data pipeline, the research brief, the legacy
harvest, and the book-2 hold list; **Standing facts and methods** closes the
file and holds knowledge, not tasks. Work them when a phase-3 pass reaches into
them, not on their own — except the remaining writing, which is a deliverable
in its own right.

Plain bullets, never numbered. Delete a bullet entirely when it fully lands;
update it if only partly done. One item at a time: do it, verify it, commit it.

Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory,
or a design decision — they are collected in phase 1 rather than scattered.

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

## Phase 1 — Author-gated decisions. Rule these before anything else.

Each of these is a design decision, not a task. Record the ruling in `CLAUDE.md` when it
lands, so it is not re-proposed. This section emptied once — every earlier decision was
ruled — and was deleted with its last bullet; it returns because the prefix's promise
("collected in phase 2 rather than scattered") has to point somewhere.

**Seven of this section's decisions were destroyed by tooling on 2026-08-01** — a
tracker-edit slice in `412e5a4` anchored on the next `---` after a separator that an
earlier cleanup had removed, and swallowed 145 lines, all but one of them open. The
loss went unnoticed because nothing checks this file, and a later commit then described
the emptied section as "every earlier decision was ruled", which was false. Restored
verbatim from `412e5a4^` on 2026-08-02; each may cite line numbers from before the
loss — re-derive before trusting them.


---

## Phase 2 — Engine handoffs (nibli). Nothing is pending upstream.

**dhilipsiva wrote nibli, and he is the channel between the sessions — for book-2's
tracker exactly as for this one.** The sessions cannot see each other, so **an item is not
ready until it carries a self-contained prompt in a fenced block**. Write the prompt as
one session speaking directly to the other, with dhilipsiva carrying it: address the
engine session in the second person, assume **zero** knowledge of this repo — no bullet
references, no chapter numbers, no "see above" — and close by instructing that session to
write its reply addressed directly back to this one, again through dhilipsiva: the sha,
what changed, whether any verdict moved, and what the prompt itself got wrong. That last
item has been non-empty more often than not, on both ends of the channel.

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

Pass complete 2026-08-02: whole-chapter read against the constitution, the two-routes
staleness fixed with the shape rather than the count, the severity walk corrected to
the pairings the rules check, the void summary restated in the rule's own conjuncts,
the investigation passage reconciled with the chapter's own list, all four measured
before writing and pinned after. No known defects remain.

### Chapter 2

Pass complete 2026-08-02: whole-chapter read, the two-routes staleness fixed as the
two kinds of route with the convocation named and Wren pinned as the seat-only
witness, the recalled-examiner sentence corrected to counts-for-nothing rather than
cannot-write. No known defects remain.

### Chapter 3

Pass complete 2026-08-02: whole-chapter read, the recorded-the-same-thing and
not-related glosses corrected to what the rule checks (the chapter 1 fixes, applied
where the chapter repeated them), the who-may-record disclosure the clear-bullet asked
for written into the relief section, Nia's conviction premises pinned so the relief
verdict cannot go vacuous. No known defects remain.

### Chapter 4

Pass complete 2026-08-02: whole-chapter read, the power/standing conflation fixed at
the condition's rationale and at the closing enumeration (the shield's test is
standing, held now or ever — the recalled Boss is the chapter's own witness), the
seating-class staleness fixed at the growing-list cost. No known defects remain.

### Chapter 5

Pass complete 2026-08-02: whole-chapter read, the opening's cannot-sign overclaim
reconciled with the chapter's own voided-and-credentialed disclosure (the signing dies
one period late, and the opening now says so), the recorded-the-same-finding and
not-related glosses corrected at the Vex block. The disclosure itself was already
fully pinned — seated Lupo co-signing Frisk, the carry closing it one round late. No
known defects remain.

### Chapter 6

Pass complete 2026-08-02: whole-chapter read, the withdrawal register corrected
throughout — the mint refuses and the loss is recorded, never taken — including the
at-its-best paragraph, which had claimed a taking the rule cannot perform on a student
it never voids; both halves of the corrected register pinned on Bela in the chapter's
own file. No known defects remain.

### Chapter 7

Pass complete 2026-08-02: whole-chapter read, the second-door corollary rewritten, the
counted claims stripped, the debt and second-door pins added. No known defects remain.

### Chapter 8

Pass complete 2026-08-02: whole-chapter read, the counted sites swept (ratchet 14 to
9), the marker cross-reference corrected to a later chapter, the nothing-compels
paragraph reconciled with the chapter's own named exception (the mark lands on the
body that audits, not the body that owes), and the floor enumerated in full on one
person in the pin file — both sides of the debt. No known defects remain.

### Chapter 9

Pass complete 2026-08-02: whole-chapter read, the automatic-ballot claim qualified to
its input, the never-written category named with the teacher exhibit pinned, the
counted sites swept. No known defects remain.

### Chapter 10

Pass complete 2026-08-02: whole-chapter read, the third door gated on voiding
(constitution v0.9, the enact branch of the fork — ruling in `CLAUDE.md`), the examiner
paragraph rewritten to name both guards, the severity echo corrected to the pairings the
rules check, the voided-examiner pins added with a surgical negative control. No known
defects remain.

### Chapter 11

Pass complete 2026-08-02: whole-chapter read, the three unpinned routing inputs
pinned (Hano's absent family on the man the opening warns about, Lalo's family fact,
Nando's closed home-confinement door), the severity gloss corrected to the pairings
the rules check, the alarm tally made stable, and the same-rule-for-all claim
corrected to routes-are-rules-with-no-combination-uncovered. No known defects
remain beyond the declared alarm defect, which is the chapter's subject.

### Chapter 12

Pass complete 2026-08-02: whole-chapter read, the evidence-list paragraph added to the
register section — the honest form measured first: entrench the vocabulary's name on
paper and a widening edit still walks past unvoided, so the register cannot hold it,
not merely does not — with the connecting pin re-tested in this chapter's file. The
pin header now names one declared defect and one guarded absence; the Amend_Sneak
pair carries :defect directives, the become absence is a :require pair with its
positive control, and rights-floor's released-man placement pin is marked with the
shared err/2 reason string. The counted site swept (ratchet 9 to 8). No known
defects remain beyond the declared ones, which are the chapter's subject.

### Chapter 13

Pass complete 2026-08-02: whole-chapter read against the constitution — the duration
ratification, the release sting and the buildings-read-by-nothing walk all verified
against prior measurements — and the counted sites swept to their rule forms
(ratchet 8 to 5). The title stays: it is the theorem's name, and the ratchet
baseline holds it deliberately. No known defects remain.

### Chapter 14

Pass complete 2026-08-02: whole-chapter read against the settled Article 8b material —
the duty, its inheritance of the markers' miscalibration, the corrected
powerlessness-was-a-choice position all verified — and the counted sites swept: the
prisoner tally keeps its names and loses its count, and both chapter-count sites take
forms that survive a spine change. The sweep also took the last two leftovers in
chapters 9 and 10, so the ratchet lands at 1: chapter 13's title, held deliberately.

**Phase 3 is complete. All fourteen chapters have whole-chapter passes.**

---

## Constitution (KB) work

- **`lose/2` is a leaf — the remaining question is whether anything should read it.**
  The register rewrite the old form of this bullet prescribed landed with chapter 6's
  pass (2026-08-02): the chapter now says the mint refuses and the loss is recorded,
  and nothing anywhere says taken. What remains is a design option, adjacent to the
  open Article 4 clawback fork and best ruled with it: if a downstream consumer is
  ever wanted, `all $x: lose(Points, $x) -> err($x, Recognition).` loads at 0 errors
  and derives for Bela and Cira — measured 2026-08-01, re-measure before relying on
  it. Regenerate the "determination, then stop" family by the awk body-test rather
  than trusting any list here: `awk -F'->' '/^[^#]/ && /->/ && $1 ~ p' constitution.nibli`
  with each candidate name — a bare grep matches rule heads and can never fail.

- **Rename the Article 6 `dwell` head — one atom is doing two jobs, and it blocks the
  `err/2` repair.** Every rule producing `dwell` requires `prisoner` (`:591`, `:594`,
  `:606`, `:627`), and the Article 1 floor line at `:317` produces nothing — verified,
  `entitled(Bela, event { dwell() })` is TRUE while `dwell(Bela)` is FALSE. So
  `dwell(Lalo)` does not mean "Lalo is owed shelter"; it means "Lalo is housed at
  HighSec", and one atom carries both *entitled to a home* and *in a cell*. A hostile
  reviewer finds it in an afternoon. **`placed` is not the name** — verified 2026-08-01,
  `-> placed($x)` is refused outright ("not a corpus name") — so either find a name in
  nibli's committed alias corpus or fold the placement head into `building`, and add
  the asserted counterpart the `err/2` fix needs. **Regenerate the site list by census
  before touching anything** — every `dwell` pin in `08`, `11`, `13` and `rights-floor`
  moves with it, and so does `08:50`. **Since Article 0a the asserted counterpart costs
  two lines, not one**: the new name needs an `admits` declaration above its first use,
  and it takes the evidence count off 23, so `verify.sh`'s evidence-vocabulary check
  moves in the same commit.

- **Fix `err/2` — the placement alarm has never once fired correctly, and release gave
  it a third victim.** `:599` reads
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)`, which tests *having a home*,
  not *having been placed at home*. Re-verified 2026-08-01: exactly three people carry
  a `home` fact, and it fires on two of them — Ruk and Lalo, both routed correctly to
  `building(HighSec, ·)` — and on nobody misplaced. **Release made it worse rather than
  exposing it**: `free(Hano).` takes `fit` away while `home(Hano).` stays asserted, so
  the alarm fires on a released man in his own house — `prisoner(Hano)` FALSE,
  `fit(Hano, Homestay)` FALSE, `err(Hano, Placement)` TRUE.
  **Three false positives, zero true positives** — two on the shipped cast, the third
  pinned under the release scenario — and the newest one is not even in custody. That
  verdict is carried as a DEFECT PIN at `rights-floor.pins.nibli:279-284`, and four more
  pins carry the `:defect` reason string "keying err/2 on where somebody was PUT, not
  on having a home" — two in `11-where-people-are-put.pins.nibli:75-80` and two in
  `14-when-the-system-notices-it-broke.pins.nibli:100-106` — so the repair reads as a
  resolved defect rather than a regression.
  An alarm with that record is worse than none. The fix is **not** "key it on `dwell`" —
  `:591` already requires `fit`, so a marker over the derived placement atom could never
  fire. The marker can only fire on an ASSERTED placement, so give the world a way to
  report one: a new asserted relation for "X was put at Y" (name from the committed
  alias corpus, plus an `admits` line), checked against derived `fit`. That is Article
  0's own evidence/conclusion split applied to placement, and it is the same repair as
  the `dwell` rename — **do that one first**. Repairing it flips `err(Ruk, Placement)`,
  `err(Lalo, Placement)` and the released-Hano pin FALSE, so four files move in the same
  commit: `rights-floor.pins.nibli:80,283` (`:82` already pins FALSE and stays),
  `11-where-people-are-put.pins.nibli:75-80`,
  `14-when-the-system-notices-it-broke.pins.nibli:100-106`, and "The alarm that does not
  work" at `11:74-106`, written against the defect on purpose. That rewrite is the
  intended outcome.

- **Guard the personhood roster — one deletion defeats all eight rights, and the
  obvious repair only renames the target.** `person` has two producing rules —
  `prisoner -> person` (`:329`) and `free -> person` (`:339`) — so imprisonment is the
  only route in that needs **nobody's permission**; the `free` route needs one written
  fact, and that fact is itself on the evidence list. Re-verified 2026-08-01 by deleting
  `:782` `person(Bela).` and changing nothing else: `entitled(Bela, event { eats() })`,
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
  over the fact store, and stop looking for a rule. **The disclosure is done** — chapter
  1's pass moved it to `01:239-269` ("The other way in" through "watch it over time");
  what remains here is the obligation itself. Do not re-derive the disclosure; extend it
  if the obligation gets built.

- **Decide the Article 4 clawback question.** The two rules are `:498`
  (`false($f) -> lose(Points, $f)` — docks the wrongdoer, fairer, still a subtraction
  from a person's record) and `:499` (`teaches($t,$s) & false($t) -> lose(Points, $s)`
  — docks a **student** for a teacher's fraud: negative scoring, of a person, who did
  nothing). Re-verified: `lose(Points, Bela)` TRUE, `lose(Points, Cira)` TRUE. Legacy
  `book.md` bright line 2 — *"No negative scoring of persons"* — is contradicted by
  both, and note it is a **legacy** line recorded in `CLAUDE.md` under historical
  decisions, not one book-1 has adopted. Decide which side gives: either the bright
  line narrows to "no subtraction except by due process for one's own adjudicated
  fraud" and `:499` is deleted, or the clawback rules go and sanctions reach perks
  only. Do not leave both in print. Narrowing flips `lose(Points, Cira)` FALSE and
  rewrites the Cira section at `06:47-98`; that is the intended trade, the NOTE at
  `06-clawback.pins.nibli:8-18` records it, and the Cira pin is already declared
  `:defect` (`:73`) so the flip reads as a repair.
  **Both middle options are closed, and the wrongdoer's closed last.** On the wrongdoer's
  side — where Bela and Vex really do hold recognition — the narrower rule would need
  provenance on `reward` to say which recognition came from the fraud, and that is refused
  (`CLAUDE.md`, 2026-08-01). So this fork has two branches and no third, on both halves.
  **The student middle option was closed first, and the chapter now says so in print.**
  Since the grades ruling settled that students never mint, "claw back only the rewards
  that came from the fraudulent teaching" is the empty set for every student by
  construction — so narrowing `:499` is not narrowing, it is deleting it, and it should
  be decided as a deletion; `06:88-92` ("Whoever sits down to write the fix will find
  they have written a repeal") already argues exactly this.

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
  and the pair also fires Article 4's audit-reward rule — re-measured 2026-08-02 under the
  v0.9 `~false` guard: the forced Bela probe no longer mints, Bela being voided, but the
  rule pays a teacher in good standing for an audit nobody performed all the same
  (verified, a fresh clean person mints from the bare `judge`+`capture` pair).
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
  credibility-buying admission the book has. **Any layer built here must keep a delivery
  record — an evidence fact about something reaching a person — distinct from a derived
  actuality**: the constitution's "residual trust base, II" section records that all
  eight heads accept a fiat rule (`person -> P`) that fakes delivery, silences the
  isolation marker, and leaves `owe` reading as a discharged obligation; the only test
  that separates a delivery route from that fiat is what arrival evidence sits upstream
  of the head.

- **Resolve the polarity contradiction between Articles 6 and 7.** Article 7's shield is
  fail-**open** toward protection and defends the choice explicitly at `:634-640`.
  Article 6's `~permits(Appeals, $offender)` (`:536`) is fail-**closed** against
  protection and defends nothing. Since v0.3 relief is an asserted `clear($x)` feeding a
  derived `permits(Appeals, ·)`, so the *absence* of a granted relief is what convicts.
  Same file, opposite defaults on the absence of a finding, one justified and one silent.
  **The file now names the disagreement without settling it** — Article 6's severity
  polarity note at `:565-571` calls it "older than this revision and still unresolved" —
  so what is missing is the resolution, not the acknowledgement. Fix: either give the
  conviction rule its own explicit polarity note, or separate standing-to-seek-review
  from a granted relief that stays the sentence, or require an affirmative exhaustion
  fact for conviction. **Do not re-open the fail-open window in the chapter** —
  `04:57-81` defends the choice and the costs section at `04:146-175` names the cost
  outright.

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
  expungement fact as a `~<expunged>` body conjunct on the multi-sig rule (`:497`) and on
  `rotten -> false` (`:695`). Both are safe — the predicate is stratum 0 and `false` is
  stratum 1, so no cycle. **Do not** put `~false` in a `false`-headed rule; the file
  records that exact attempt failing as E2 at `:23-26`, and it still fails.
  **Two sites are not enough, and this was measured.** With the conjunct on both, an
  expunged Vex has `false(Vex)` FALSE and the clawback stops — but `permits(Review, Vex)`
  stays FALSE, because Article 8's credential rules (`:671`, `:690`) read `~rotten`
  directly. Decide whether expungement clears the mark only or also returns the pen; if
  the latter, it is four sites, not two.
  Costs one more evidence entry (23 → 24), an `admits` line above its first use, and the
  matching move of `verify.sh`'s evidence check; the prose sites that quote the list
  move again, so consider landing it in the same pass as the severity dimensions rather
  than alone. Worth framing in the book as forgiveness being a *right* rather than as a
  bug fix.

- **Put a precondition on `capture`.** `capture($a, $audited)` has no precondition
  anywhere: any credentialed pair — one Review, one Tribunal, since v0.7 — can void any
  person for no stated reason, and the book never admits it. The cross-body requirement
  raised the cost of assembling that pair and did nothing about the missing grounds. Needs one design decision — which predicate
  carries "grounds", since adding one enlarges the evidence vocabulary — after which
  the guard is a body conjunct. Pair with an epoch expiry on `capture` and `judge`.

- **Widen kinship beyond `parent/2` — the fix is available today, and it is not free.**
  Article 4's independence check names one relationship (`:497`), so spouses and siblings
  co-sign. **Not blocked on the engine**: `married` (speni), `brother` (bruna), `sister`
  (mensi) and `sibling` (tunba) are all in nibli's committed alias corpus — cite them by
  name, never by line. Re-verified 2026-08-01: appending `~married`/`~brother`/`~sister`
  in both directions loads at 0 errors and leaves `false(Bela)` and `false(Lupo)` TRUE,
  `false(Tyr)` FALSE. And the cross-body probe now has a verdict rather than a stale one:
  with `admits("married").` and `married(Gia, Hex).` added, `false(Bela)` flips **FALSE**
  — the shipped cross-body pair stops co-signing, which is the demonstration.
  **The cost is what needs deciding, and it is the only thing left open here.** Three
  evidence entries (23 → 26), three `admits` lines, and the matching move of
  `verify.sh`'s evidence check — and enlarging the vocabulary is the quietest way to
  capture a system, the file's own threat model. Chapter 5 is already honest either way:
  its costs section (`05:119-140`) says the words exist, the widening has not been judged
  worth it, and discloses that as a choice. So what remains is only whether to land the
  rule.

- **Check each governance item against what the rules can express, before any prose.**
  Parts I–V are gated on derivation, and the constitution has no predicate for a
  community, a transfer, a tax, or a term of office — so none of the following is
  derivable today and all of it is constitution work first. In dependency order:
  - Recall is one asserted `broken(·)` fact (`:867`), consumed by the two credential
    rules at `:671` and `:690` — at-will, no threshold, no administering body, no term.
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


- **Extract the claim-to-query table from the pin files — it cannot be generated from the
  constitution.** The substance already exists in a better form than the old bullet
  imagined: every chapter's pin file plus the constitution's own carry every load-bearing
  sentence, every one a query with an enforced expected verdict, all green, and a scan
  finds no `?` query lacking a `# =>` line (re-checked 2026-08-01, after the suite grew).
  What is left is the rendering, and it runs the other way round: the constitution cannot
  know which sentence of chapter 11 a query backs, so the table must be extracted from
  the pins rather than derived beside them. Blocked by a data gap — of the `?` queries
  under `book-1/`, half again as many have no comment line directly above as do, so an
  extractor run today leaves most of a chapter's sentence cells empty. (Re-measured
  2026-08-01 after the ch1–ch6 pin passes: 291 queries, 116 with a comment directly
  above; re-run the count rather than carrying it forward.) Fix: settle one
  machine-readable form for the sentence — the `# "…"` line immediately above the query
  is the existing convention — backfill the rest, then have the verification script emit
  the table as a by-product.


---

## book-1 — remaining writing

- **Write the opening note — the last unwritten non-derived element, and nothing else
  tracks it.** ~800 words before Part I, explicitly non-derived and labelled the way Part V
  is labelled, so the book does not open cold on vocabulary; it claims no derivation and
  carries no verdicts (`new-book-plans/3-spine.md:123-126`). One of exactly three sanctioned
  exceptions to the inclusion gate. No file exists. Write it against the final wording,
  which is settled: *The Rights Nobody Has to Earn — A design for a society worked out to
  the point where it catches its own failures.* **Written in the author's first person under the
  voice-boundary ruling** — the author drafts (`tmp.txt` is the channel), sessions edit
  mechanics only and never generate the voice. **Check the note against the counted-claims
  ratchet before committing it** — it will be the first prose in `book-1/` the ratchet has
  ever scored, every other file predating it. The subtitle itself is clean; a note that
  opens by naming the floor's size would not be.
  **The best evidence this note is load-bearing is now on file** (`reviews/ai_review.md`):
  a sympathetic, capable reader finished the manuscript and concluded it is a teardown —
  *"a beautiful nightmare to show us what not to do."* The note has to tell a reader what
  they are holding before chapter 6 teaches them wrong: the confessions are the method,
  not the verdict.

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
- **The method part discloses the stress surface.** It sits inside the voice boundary —
  first person permitted, same supply protocol as the opening note and Part V. The suite's confidence register must
  not outrun its provenance: every probe, fixture and refusal was written by the author and
  AI sessions against a cast of dozens — no independent reimplementation, no external
  red-team, and the engine that blesses the book shares the book's author. The counterfactual
  fixtures and the upstream differential oracles narrow this and do not close it. One
  honest paragraph, beside the machinery it qualifies; anything stronger (soliciting an
  independent verification) is post-ship work and goes to the reach strategy when it is
  ruled.

- **Write what the logic refused — in the method part, paired with chapter 7.** Re-verified
  2026-08-01: appending `all $x: prisoner($x) -> permits(Appeals, $x).` returns
  *"[Stratification Error] Unstratifiable negation: strongly-connected component containing
  'prisoner' -> 'permits' (negative)"*. A **universal right of appeal cannot be expressed**
  in this constitution. That is not a defeat; the machine refuses a thing the author wanted
  and can say exactly why. Ship the error message. **Not in Part V** — Part V is argument
  and evidence and stays jargon-free; an engine error message is formalism, which appears
  in exactly one place. **And the firewall it pairs with is chapter 7, not chapter 1** —
  `07:44` is where the heresy law is refused by the stratifier. Chapter 1 now carries a
  refusal of its own — Article 0a turning away the write of an unadmitted word — but that
  is assert-time closure, a different mechanism, and pairing with it would blur the
  symmetry. The symmetry is the argument: the same stratifier that refuses the author a
  universal right of appeal refuses an attacker a heresy law. One mechanism, no special
  pleading, neither outcome chosen by whoever was writing that day.

  **The texture ceiling, ruled 2026-08-02: four real channels, and no imagined people.**
  No record-person gets an inner life anywhere in this book, Part V included — inventing
  Cira's fear would fabricate exactly the kind of entry the record refuses to hold, and the
  restraint is the thesis performed; one Part V passage states it as chosen. Five of six
  reviewers asking for characterisation enters as citable evidence — a reader who felt the
  flatness has felt the design — never as a defect being repaired. The four channels: the
  author's first person (the Voice ruling landed 2026-08-02: admitted, author-drafted,
  sessions edit mechanics only); the
  second-person **domestic vignette** — a household carried through food, care, housing and
  crisis, generic "you", never a cast name (the register the derived chapters cannot hold);
  the **hostile reviewer corpus as the antagonist**, quoted by name from `reviews/` and
  answered at the joints; and the **nine historical cases as the feeling** — documented
  grief, never counterfeited.
  **The capture joint owns the temporary-assessment exclusion, ruled 2026-08-02, verdict
  "Survives, narrowed."** The claim shrinks from "no assessments" to "no assessments where
  they can reach liberty": this design does not abolish capacity, risk or crisis
  assessments — it refuses them entry to the one record that reaches standing, liberty and
  the floor, and the firewall is the actual claim (a hospital chart can inform care and can
  never void you). The exile price is stated in full — assessments pushed outside live in
  records this design does not police, and power migrates toward whatever record matters —
  and the lesser-harm argument carries the defense: inside this record an assessment sits
  upstream of liberty forever; outside it, its harm is bounded by what the record refuses
  to hear. The section closes on the specification, per this bullet's own constraint: the
  operational layer book-2 must build — expiring, episode-scoped, one-way firewalled.
  **The objection docket is now external and convergent** (`reviews/adoption_reviews.md`,
  2026-08-02): four independent reviewers land on release/duration, delivery/obligor,
  audit teeth, degree/equity, and legitimacy/transition — plus two new Part V objections
  from the engine-book review, the unenumerated-rights cage and proportionality-vs-
  structure. Part V answers these by name or it has not done its job. **One burden is
  Part V's alone and derivation cannot carry it**: *why this vocabulary* — the record's
  names are a stipulation, the book proves only what follows from them, and Part V either
  argues the choice or concedes it is one. Disclosure is done (chapter 1); justification
  is not.

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

- **Write the single book-2 pointer, at the very end — which is now the end of the method
  part.** book-1 references book-2 exactly **once**, and the method part is the book's
  final element, so the pointer closes it; the Part V bullet's collision note says the
  same, and this bullet used to say "in the closing note", which is not an element the
  spine has. Not in the introduction, because a reader on page one has no idea whether
  they want the machinery, and a forward reference reads as an apology for the book they
  are holding. At the end it reads as an invitation. **Its old second job is gone** — it
  used to carry the one honest sentence about the apparatus; the method part now does that
  far better, by showing the machinery instead of alluding to it. Keep the pointer plain:
  no tool names, no jargon, nothing a general reader must decode — it addresses whoever
  reached the last page, not only the readers who came for the formalism.

- **Reframe the brief's India-first assumptions for a global audience.** India material stays
  as **evidence** — Aadhaar/PDS is among the strongest evidence the book has — but it is one
  case among several, not the frame, and every reference needs enough context for a reader
  who has never heard of a ration card. Unblocked by drafting Part V; that is the only place
  the India evidence lands.

- **Expand Parts I–IV toward ~38,000 words.** DECIDED 2026-07-29; the invariant and the
  budget are in `CLAUDE.md`. **Re-measure with `wc -w book-1/*.md` before planning against
  any figure here** — the tree measured 22,412 on 2026-08-01, every previously written
  figure has been stale when checked, and `CLAUDE.md`'s own refresh was 627 words behind
  the tree on the day it was dated. This is the largest single item in the tracker —
  roughly +15,600 words, mean chapter ~1,600 → ~2,700 — and it is one bullet only because
  the work is one decision; it becomes fourteen commits. **Know what it is not:** the
  invariant does not force it. Break-even is derived > 17,800 and Parts I–IV already clear
  it, so majority-derived holds today with no expansion at all. The 38,000 is an editorial
  choice about the book's size, and it means Part V's 12,000 must be justified by content
  rather than by ratio.

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

## Reach — ruled 2026-08-02; the gate is the chapter pass

Serialize in spine order as whole-chapter passes complete, from a dedicated domain, with
the assembled book — opening note, Part V, method part — as the capstone release rather
than the first contact. Building in public performs the thesis: the repo history is the
proof of the method, serialization recruits the red-team the method part admits it lacks,
and defect pins turn known flaws into declared features. **A chapter serializes only when
its whole-chapter pass is complete** — today only chapter 7 qualifies — so reach is
sequenced behind Phase 3's discipline by construction.

- **The site.** A dedicated domain — registering it is the author's own task — plain,
  built from the Markdown that already exists; chapters in spine order; the repo and the
  one-command suite run linked from the front page. Platforms syndicate *from* it: CC-BY
  means they will copy regardless, so the canonical home must name itself.
- **The launch essay.** A standalone distillation for someone who will never read the
  book, carrying the thesis and the honest second half in miniature. *The Furnished
  Prison* is the standing headline candidate. First-person territory: the voice protocol
  applies — the author drafts, sessions edit mechanics only.
- **The method paper.** JURIX/ICAIL/formal-methods-for-law genre: the derivation gate,
  the pin suite, the counterfactual classes, the defect markers — the methodology made
  citable. Coordinate with the method part rather than duplicating it; the paper cites
  the book, the book does not depend on the paper.
- **Run-it-yourself as a launch claim.** The suite promoted to a first-class launch
  artifact — clone, one command, the pins pass — stated where a stranger lands. Nothing
  new to build: `verify.sh` and its `--only` mode already are the artifact.
- **Print-on-demand.** A priced, well-made physical edition of a free text. Quality is
  the lever and revenue a side effect: the typography is canonical because it is first
  and good, never because it is exclusive.

---

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

  - **Licensing blocker: the EIU index is non-redistributable, and the escape hatch costs
    more than it looks.** Our World in Data cannot export the series, and `LICENSING.md`
    commits the claim registry to CC0 — so a CC-BY book with a public registry cannot
    ship those numbers. Cite-and-link keeps every figure intact but breaks the registry’s
    promise that a reader can re-run it. Or switch to **V-Dem**, which is openly
    licensed — but then every number has to be re-derived: the r = 0.52 is quoted from a
    transcript, no V-Dem data is in the repo, and V-Dem’s Regimes of the World categories
    are not EIU’s four, so the regime table and the step sizes do not carry over. Budget
    the re-derivation if the answer is V-Dem. When the registry exists, record
    `demo-happy.txt` in it as “prior analysis, independently re-derived”, with the CSV’s
    provenance pinned: WHR 2025 (2022–2024 average) merged with EIU 2025, 144 countries
    matched from EIU’s 166 and WHR’s 147.

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
  defendant carried through a procedure. **Ruled 2026-08-02: Part V gets one** — generic
  second person, never a cast name, per the texture ceiling. What remains here is the
  harvest itself: the technique, not the prose.

- **Finish the floor corrections in book-1 — two remain.** **`dwell` is nowhere glossed in
  prose as protective shelter** — `grep -rniE "weatherproof|ventilat|plumb|sanitation"
  book-1/` still returns nothing, so ch 8’s “somewhere to live” carries the whole weight and
  the water-and-sanitation case is not absorbed; write the gloss into ch 8 now, it costs a
  sentence. And **privacy is not argued down anywhere** — book-1 has one incidental use of
  the word (`04:44`, “a private person”), and the argument that encoding it as a defeasible
  right lands it at stratum 3 and destroys the single-deprivation theorem is Part V material.
  That half waits on Part V; the `dwell` half does not.

- **Then delete both files, in one commit, with the harvest manifest in the body.** Not
  before. The commit message is the record of what was taken and what was consciously
  dropped.

---

## book-2

book-2 now has its own tracker: `book-2/TODO.md` — unordered until its chapters are
decided, seeded from the hold list that used to live here plus the adoption reviews
(`reviews/adoption_reviews.md`). The discipline is unchanged: **do not work book-2 items
while book-1 is active**; collect there, rule here.

---

## Standing facts and methods

- **A `fit/2` pin for any placement other than Homestay is a vacuous green.** `fit`
  has one producing rule and only ever carries `Homestay`, so `? fit(Ruk, HighSec).
  => FALSE` passes forever regardless of the design — kind three of the three FALSEs.
  Moved here from chapter 11's bullet when its three input pins landed (2026-08-02). — not tasks, and not history

Landed work is not recorded here; that is what git is for. What survives is the small
set of things a command cannot teach you and a rename cannot re-derive.

```
./verify.sh                 # ~30 s: spine, evidence count, jargon, counted-claims
                            #   ratchet, absences, INVARIANT 1, the arity and counting
                            #   guards, control scope, engine build, the pin suite with
                            #   its cross-file :expect-pins reconciliation, and the
                            #   counterfactual fixtures in their three diff classes —
                            #   line deleted, line changed, line added
./verify.sh --quick         # ~2 s: everything except the pin suite AND the
                            #   counterfactuals — never sufficient after a constitution
                            #   edit
./verify.sh --only <file>   # one pin file, engine rebuilt, --allow-shell passed, and
                            #   the fixture’s own KB chosen for counterfactual files;
                            #   partial by design — full run before committing
```

Prefer it to any check by hand. It exits non-zero on the first failure and names the
claim that stopped being true — including exit 3, the failure that is good news: a
pinned `:defect` stopped reproducing, and the script names it a REPAIR, not a
regression, because the response is to drop the marker and rewrite the prose that
called it a flaw, never to debug the harness. Use the **release** `nibli-pin`, never
`nibli-host`. The script builds the engine itself and prints the commit, because a
stale binary is invisible here — the pins check the constitution, not the engine, so an
out-of-date build returns the same green and the same runtime.

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

- **"The Furnished Prison" — a rejected title that is a good part title.** Scored highest
  of the twenty title candidates on pick-up and lowest on legibility, so it lost the cover
  and is wasted sitting in git. It is the sentence that closes chapter 13's delivery-gap
  passage (`13-the-one-thing-taken.md`) — *"A society whose only working provision runs
  through its prisons has not built a floor; it has built a prison that happens to be
  furnished."* Primary candidate since the reach ruling
  (2026-08-02): the launch-essay headline; the Part-title and back-cover uses stay
  listed behind it. The title work is done; this is the one asset from it
  that outlived the decision.
