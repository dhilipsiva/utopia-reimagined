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

## Phase 1 — Engine work (nibli). Prompts are ready to paste.

**dhilipsiva wrote nibli, and is the channel between the two repos.** The two sessions
cannot see each other, so **every item here carries a self-contained prompt in a fenced
block** — copy the block, paste it into a Claude Code session in
`~/projects/dhilipsiva/nibli`, and paste that session's reply back here when it lands.
Each prompt ends by asking for the sha, what changed, whether a verdict moved, and what
the prompt itself got wrong; that last one has been non-empty more often than not.

Rules for this section. A prompt must assume **zero** knowledge of this repo — no bullet
references, no chapter numbers, no "see above". If an item cannot be stated that way it
is not ready to hand off, and it says so instead of carrying half a prompt. Do not work
around an engine limitation in prose: conceding a fixable limitation as though it were a
design choice is the specific dishonesty this phase exists to prevent.

**When a reply lands here**, re-run `./verify.sh` before believing anything — the script
rebuilds `nibli-pin` from the checkout and prints the commit, and this repo has twice
measured an engine change that was never rebuilt.

- **LANDED 2026-07-31 — `nibli-pin --strata`, and it found three live disagreements.**
  nibli `e1ce09d` dumps the engine's own stratification as TSV. `5-spine-gen.py` now
  **consumes it** instead of re-implementing the stratifier in regex. What the diff found,
  all verified here before changing anything:
  **`entitled`** read as base at stratum 0 — the FLOOR branch synthesised the `P -> domain`
  edge but never registered the outer predicate as a head. The engine puts it at **2,
  derived**. **`severe`** read as stratum 0 with a "monotone cone" — its rules carry
  `~($a = $b)`, a real negative edge to the `equals` builtin, so it is **stratum 1 and its
  cone is not negation-free**. **`derived_only`** was a phantom node: the fact branch
  registered the declaration keyword and never the name it quotes.
  **Two printed numbers were right only because two errors cancelled.** `derived_only`
  (phantom, +1) and `equals` (real, missed, −1) both hit the predicate total, so it read
  50 either way; evidence read 23 by two different subtractions. The derived count was
  genuinely wrong, 25 against the engine's 26.
  **Four prose claims went with it**, including this file's own "`severe` has a wholly
  negation-free cone", which was false in two places. **Chapter order did not move** —
  chapter 1 carries the severity derivation for a stated editorial reason, not a stratum
  one — so this was a numbers-and-prose correction, not a structural one.
  **One error was mine, introduced in the rewrite and caught by the diff**: counting only
  `->` lines undercounted rules by exactly the eight floor lines, which *are* rules — the
  engine agrees, since `entitled` is derived. Fixed, and the reason is commented at the
  count.
  Two filters remain this document's choice and are now named in the generated block so
  they are visible rather than silent: compiler artifacts (`event`, `__abs_<hash>`) are
  dropped, and `equals` counts as a predicate but is not evidence, since nobody writes it.

- **PARTLY LANDED 2026-07-31 — the typo route is closed, the mechanism is not.** nibli
  `e70f22f` renamed the converse alias `obligated` to `obligated_by`, so `obligated(...)`
  is now a compile error instead of a silently inverted fact. **Verified here**: the
  refusal fires, our 359 pins pass untouched (our three `obligated` occurrences were all
  in `#` comments), and `obligated_by(Warden, Ruk)` **still** compiles to
  `obliged(Ruk, Warden)`. So the accidental mistake is gone and the converse is not — you
  now have to type `_by`, which at least says which way the arguments run. The
  chapter-14 discriminator stays: it is the only thing catching an argument-order slip
  within `obliged` itself, which was never covered by the rename.
  **What remains open is theirs, not ours, and it points at our spelling.** nibli's own
  tracker files it as **"`obliged`-spelled every-duty renders the wrong obligated
  party"** — the deontic collapse picks the event variable as duty-holder for the base
  spelling, ours, while the converted `obligated_by` spelling binds correctly. Cited by
  title, not line: that file's line numbers rotted twice in one exchange. It cannot reach readers
  today because this repo runs `nibli-pin` only and never renders prose. **It becomes
  live the moment the method part prints a rendered sentence or a proof trace**, which is
  exactly what that part is for. Re-check before that ships; do not hand it off as a
  prompt, because it is already filed upstream and the fix is in their renderer.

- **LANDED 2026-07-31 — `admits`, and it made chapter 1's opening sentence true.** nibli
  `850cf96` ships `admits("<rel>")`, the dual of `derived_only`: an unadmitted ground
  assertion is refused at assert time, ordering enforced ("comes too late" if declared
  below the facts). Adopted here as **Article 0a**, 24 names.
  **The sentence it fixes is the book's first claim.** Chapter 1 says a thing off the list
  "cannot" be written — *"Not may not. Cannot."* **That was false.** Verified before
  adopting: `rich(Adam).` loaded and answered TRUE, because `rich` is a nibli corpus name.
  The closure was at nibli's vocabulary of thousands, not at this book's two dozen; only
  an invented word like `zorblat` ever failed. Now pinned in the chapter-1 suite by two
  refusals plus a control that conclusions still derive (16 → 19 pins; suite 359 → 362).
  **24, not 23, and the gap is the point.** `person` has producing rules *and* ground
  assertions, so it is absent from the spine's evidence figure and required here — *"what
  counts as evidence"* and *"what may be written"* are different sets, and `person` is the
  whole of the difference. Their prompt-reply said 24 and was right; my prompt's headline
  number was 21, two revisions stale, when `verify.sh` had already gated 23.
  **Chapter 1's disclosure changed with it**: widening the record is no longer something
  done by writing a fact, so the *quiet* version of that attack is closed. The chapter now
  says so and immediately says what it does not buy — visible is not hard, and nothing
  stops the edit going in.

- **HANDOFF PROMPT — defect pins vs guarantee pins.** Roughly a fifth of the book's 359
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
  the book repo's `book-1/*.pins.nibli`.
  

  ────────────────────────────────────────────────────────────────────
  When this lands, reply with: the commit sha, what changed in one line,
  whether any existing verdict moved, and anything you found that this
  prompt got wrong. Paste that reply back into the book session — it is
  the only channel between the two repos.
  ```

- **HANDOFF PROMPT — nibli: an `:accept` that does not persist.** Every complement control in
  every pin file wants to test that a rule *loads* and then throw it away. `:accept` instead
  leaves the rule in the knowledge base, so each control silently widens the base for every
  query below it — which produced a real vacuous green in this repo (see the harness section).
  The fix is upstream and small.

  ```text
  In ~/projects/dhilipsiva/nibli: nibli-pin's `:accept` loads its rule into the KB and
  leaves it there. Content pin files use `:accept` as a CONTROL — "this rule must still
  load" — and never want the rule afterwards, but every query below it then runs against
  a widened base. In constitution.nibli's suite the four complement controls each add a
  second route to `prisoner`, so `? prisoner(Adam).` below them passed even though the
  rule that should derive it could have been deleted; and a `~false` control makes a
  person with no conviction at all come back TRUE for `prisoner`.

  Ask: a scoped form — `:accept-scoped` (or a flag on `:accept`) that compiles and
  stratifies the rule, reports loadability as the pin verdict, and then DISCARDS it so
  the KB is unchanged for subsequent pins. `:refuse` already has this property for free,
  since a refused rule never enters the store; the asymmetry between the two is the bug.
  Consumer: the book repo, `new-book-plans/rights-floor.pins.nibli`
  and book-1/*.pins.nibli, which currently work around it by ordering.
  

  ────────────────────────────────────────────────────────────────────
  When this lands, reply with: the commit sha, what changed in one line,
  whether any existing verdict moved, and anything you found that this
  prompt got wrong. Paste that reply back into the book session — it is
  the only channel between the two repos.
  ```

---

- **BLOCKED, do not hand off — provenance on `reward`.** The shape of the ask depends on
  which side the Article 4 clawback fork gives (phase 2), because provenance is only
  needed if clawback is narrowed rather than deleted. Hand it off after that ruling, not
  before. One measured correction while it waits: an earlier audit reported an arity-2
  `reward` probe as non-terminating past 15 minutes; that **does not reproduce**.
  Rewriting all three `reward` heads to arity 2 and running a single pin took **38.9 s**
  against a **2.1 s** baseline — a ~19× cost, not a hang. Budget it, do not fear it.

## Phase 2 — Author-gated decisions. Rule these before the chapter passes.

Each of these is a design decision, not a task. Several chapters below cannot be
revised until the decision above them is ruled, because the ruling is what the chapter
says. Record the decision in `CLAUDE.md` when it lands, so it is not re-proposed.

- **[AUTHOR-GATED] Decide whether the other seven floor rights get delivery markers.**
  Opened 2026-07-31 by the Article 1b itemisation, and it is the largest thing the
  delivery gap has ever had. **The design already detects a floor right that did not
  arrive** — Article 6's `prisoner($p) & ~meets($p) -> err($p, Isolation)` is exactly an
  undelivered-right marker, for company. Seven have nothing. Verified that the general
  shape works: `owe(State, Eats, $x) & ~eats($x) -> err($x, Undelivered)` is **accepted
  and derives**, `err(Bela, Undelivered)` TRUE. It is legal under the narrowed INVARIANT 1
  (head is `err`, so it notices without acting) and it is simply unbuilt.
  **The asymmetry was discovered, not chosen**, which is why this needs a ruling rather
  than a defence: nothing anywhere records why company is checked and food is not.
  Cost if built: seven rules, no vocabulary, and a real rewrite of `08`'s closing item and
  of chapter 14, which gains seven markers to be honest about — including that they would
  fire on nearly everybody, since almost nothing is delivered. That last point is the
  argument against, and it is not nothing: seven more alarms that fire on the whole
  population report the same emptiness the isolation marker already reports.

- **[AUTHOR-GATED] Now that duration is expressible, decide whether the design says how
  long.** Opened 2026-07-31 by nibli `fc277a9`, which established that **no new primitive
  was ever needed** — the corpus already carries `earlier`/`later`, `happen`, `continue`,
  `cease`/`end`, `concurrent`, and `time(x, from, to)` as an interval, none with a numeric
  place. Verified against *this* constitution: all nine compile and answer, including
  `year(Term, Two)` — a term length with **no digit**, so `verify.sh`'s ban does not stop
  it. "Not yet" was never a tense question either: `~cease(Term, Custody)` says it.
  **What is genuinely absent is arithmetic on time** — nothing computes a length, compares
  two, or advances a clock. So a term could be stated and nothing would count it down.
  **Chapter 13 has been corrected either way** (`93da52f`+): it used to say the refusal to
  grade duration "is not principle — it is that the vocabulary for duration was never
  built", which is now false. It says the refusal is a choice, and holds the chapter's own
  reason — grading *how long* means saying what makes one sentence longer than another,
  and every answer prices someone's character.
  **The decision is whether that stays a refusal.** Building it costs the evidence
  vocabulary several entries, which is chapter 1's named threat, and buys a design that
  can state a term it cannot enforce — the enforcement needs arithmetic that does not
  exist. Ruling "no" is now a position to defend rather than a limit to disclose, which is
  the stronger place to be and the harder one.

- **[AUTHOR-GATED] Refine release: earning may only shorten, never lengthen.** DECIDED
  2026-07-29 — punishment is loss of liberty, and a person **may optionally choose** to earn
  reward to reduce its duration or severity. An earlier form of this had them *forced* to
  earn, which was dropped: compulsory labour as the price of liberty is convict leasing, and
  it would have broken the single-deprivation theorem outright by taking liberty *and*
  labour. Two properties to build in deliberately rather than discover. **Earning shortens
  and never lengthens** — otherwise someone disabled, ill or elderly serves longer for being
  incapable, which puts a capacity test upstream of liberty. And **"voluntary" is
  structurally pressured** when the alternative is longer confinement; that is the standard
  critique of earned-time credit, it is survivable, and it should be conceded at Part V's
  coercion joint rather than discovered by a reviewer.

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

- **[AUTHOR-GATED] Voice.** All fourteen chapters are written in a plain, mostly impersonal
  register. The legacy book was first-person and warm, and the constitution's own commentary
  says "the manifesto voice is the author's to re-weave — I am not ghost-writing it." Only
  the author can supply it, and every chapter drafted before that pass needs re-touching, so
  it gets more expensive each week.

- **[AUTHOR-GATED] Plan the reach strategy on the basis that exclusivity is gone.**
  CC-BY-4.0 is perpetual and irrevocable, so no trade publisher can ever be sold exclusivity
  — `LICENSING.md` records this as a cost accepted deliberately. That makes serialization and
  open circulation the route by default rather than by choice, and it is a publishing
  decision nobody but the author can make. Worth knowing when it is made: the **title** is
  the only integrity lever that survives an irrevocable content licence, since no licence
  here grants trademark.

---

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

---

## Phase 3 — Chapter passes, chapter 1 through 14, in order.

One chapter at a time: read it whole, fix what is false, revise what is thin, verify,
commit, move on. **The bullets under each chapter are what is already known to be wrong —
a floor for that pass, not its scope.** Chapters with no bullets still get a pass.

### Chapter 1

- **Chapter 1 must concede that at least five of the twenty-two are findings, not
  observations.** `01:25-34` presents the list as things the world reports and the
  exclusions as "considered and rejected on principle", but `severe`, `deceive`
  ("someone lied"), `family` and `parent` are adjudicative conclusions with no
  definition and no precondition anywhere in the constitution — `severe(X).` moves
  anyone into high security, and one `deceive(Rebel, Boss).` jails the file's own
  whistleblower (verified: `prisoner(Rebel)` FALSE → TRUE on that single write).
  **Article 6's release added a fifth, and it is the sharpest.** `free` — `01:16-17`,
  "Someone's sentence is finished" — has no producing rule, no precondition, no author
  and no standard, and one write both empties a conviction and stops the only two
  floor goods the design was actually delivering. Verified: assert `free(Ruk).` and
  `prisoner(Ruk)` TRUE→FALSE, `dwell(Ruk)` TRUE→FALSE, `expresses(Ruk)` TRUE→FALSE,
  `travel(Ruk)` TRUE. That is `clear/1`'s one-fact nullifier shape a second time, and
  chapter 13's closing at `:108-112` argues its consequence without naming the write
  that causes it.
  The chapter's argument survives the concession and is stronger for it: the claim is
  not that the twenty-two are raw sense-data, it is that a conclusion cannot be written
  **as a conclusion** — the adjudication still has to happen somewhere and the record
  still has to say who did it. Say that rather than letting a reader find the five.
  Pairs with the `capture` precondition bullet, which is the same problem one level
  down.

- **The stale run-command in fifteen pin files.** `01-what-counts-as-evidence.pins.nibli`
  and fourteen siblings each name a single-file `nibli-pin --kb …` invocation as the run
  command. It works, but it is not how the suite is run and it cannot see the cross-file
  `:expect-pins` reconciliation, so a reader following it gets a green that means less than
  they think. Point all fifteen at `./verify.sh`.
  *(The dead runner this bullet used to also name — `utopia-v2-run.nibli`, which opened
  with `:load utopia.nibli` and carried 42 directives `nibli-pin` does not take — was
  deleted in the v0.7 rename pass.)*

### Chapter 2

No known defects. Read it against the constitution anyway.

### Chapter 3

No known defects. Read it against the constitution anyway.

### Chapter 4

- **Chapters 4 and 5 argue about voids and pin none of the premises a void turns on.**
  Four gaps, all cheap, all verified in one run:
  - `? deceive(Sly, Court). # => FALSE` — the conjunct the shield chapter turns on.
    `04-the-shield.pins.nibli:26-41` pins Sly's `show`, the authority and the outcome,
    and never the *absence* of a deceit finding, which is the only thing separating Sly
    from Kel sixteen lines later.
  - `? judge(Gia, Bela).` / `? capture(Gia, Bela).` / `? judge(Hex, Bela).` /
    `? capture(Hex, Bela).`, all TRUE. Chapter 5's Bela block pins the two credentials
    and the result and skips the four facts that actually satisfy `:346`.
  - The `~parent($a,$b) & ~parent($b,$a)` independence conjunct is exercised by **no pin
    anywhere**. `05-voiding.pins.nibli:25-33` looks like it covers this and does not — it
    exercises Article 5 (`:357`), a different rule with a different head. Verified with a
    seated parent/child pair against one target and an unrelated seated pair against
    another: `? false(Targ). => FALSE`, `? false(Targo). => TRUE`. The control is the
    point.
  - No fixture shows a voided pen-holder **in the same snapshot**. Seat Lupo and
    `? false(Lupo). => TRUE` and `? permits(Review, Lupo). => TRUE` hold together, and
    Lupo then co-signs a fresh void. That is the epoch-granularity limit the constitution
    discloses in prose at `:506-511` and that no pin has ever demonstrated.

### Chapter 5

- **Chapter 5 asserts two facts about Koa the constitution does not derive.**
  `book-1/05-voiding.md:25-26`: "Koa **examined** Esa and recorded a finding — a real
  finding, on the record, made by **someone with the credential**." Koa's entire
  presence is `person(Koa).` and `capture(Koa, Esa).` (`:560-561`). Verified:
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
  stripped of the pen, still possessed of standing (the other sense), and clawed back —
  four verdicts that between them settle three of the book's recurring confusions.
  **Partly closed 2026-07-30**: `02-standing.pins.nibli` now carries `false(Vex)`,
  `authority(Vex)` and `permits(Review, Vex)` as one adjacent block, so three of the five
  are in front of one reader in one file. Still missing from that block: `rotten(Vex)`,
  which is the *reason* for the other three, and `lose(Points, Vex)`, which is the cost.
  Second gap: `? false(Cira). # => FALSE` is unpinned, and `06:103` rests on it. **Add
  both before the Article 4 clawback narrowing** (the "Decide the Article 4 clawback
  question" bullet), not after, or the chapter loses the only fixture that would show
  what changed.

### Chapter 7

No known defects. Read it against the constitution anyway.

### Chapter 8

- **Chapter 8 says one person has shelter. Four do — and a second floor right derives
  for all seven prisoners, which breaks chapter 13's headline count.**
  `book-1/08-what-you-are-owed.md:50`: "One person in this society verifiably has
  shelter: Hano." Verified: `? dwell(Hano). => TRUE`, `? dwell(Ruk). => TRUE`,
  `? dwell(Lalo). => TRUE`, `? dwell(Nando). => TRUE`, `? dwell(Bela). => FALSE`.
  The two exceptions are of **different widths** and the difference is the point.
  `dwell` needs a home plus homestay eligibility, or severity, or family (`:439`,
  `:442`, `:454`), so it reaches **four of the seven convicted people** — `dwell(Don)`,
  `dwell(Kel)` and `dwell(Adam)` are all FALSE with `prisoner` TRUE, which is the
  exhaustiveness bullet below seen from the other side. `expresses` is the wide one:
  `:323` gates on `prisoner` alone, so it reaches **all seven** —
  `expresses(Hano/Ruk/Don)` TRUE, `expresses(Bela/Cira)` FALSE. So `08:32` ("the same
  answer comes back for every one of the eight, for every person in it") is wrong on
  two of the eight, and `08:48-54` should read *two* exceptions, one covering seven
  people and one covering four.
  **Half of this landed in chapter 13 and the damaging half did not.** The rewritten
  closing at `13:105-106` now states the finding — "Two of the eight things owed to
  every person actually arrive in this design. Recorded speech arrives, and shelter
  arrives. **Both of them arrive only for prisoners.**" — while `13:21-22` still says
  of Hano and Jala: "One item. Everything else on both lists is identical." Verified
  false: `expresses(Hano)` TRUE / `expresses(Jala)` FALSE; `dwell(Hano)` TRUE /
  `dwell(Jala)` FALSE; `fit(Hano, Homestay)` TRUE / `fit(Jala, Homestay)` FALSE;
  `err(Hano, Isolation)` TRUE / `err(Jala, Isolation)` FALSE. The lists differ by four
  items and three run the *wrong way* — conviction is the only thing in this design
  that gets you shelter, recorded speech and a placement. The chapter now makes that
  argument correctly in its closing and mis-states it on its first page.
  Rewrite `08:31-34`, `08:48-54` and `13:21-22`. Add `? expresses(Bela). # => FALSE`
  and `? dwell(Ruk). # => TRUE` to chapter 8's pins, and `? expresses(Jala). # =>
  FALSE` and `? dwell(Jala). # => FALSE` to chapter 13's — **above** its `free(Hano).`
  block at `:72`, which changes Hano for every query after it.

### Chapter 9

- **Chapter 9 says the disenfranchisement clause "works". It takes nobody's ballot.**
  `book-1/09-the-vote-conviction-does-not-take.md:73-75`: "Nothing refuses it. **It
  works. Immediately, every convicted person in this society loses the ballot.**" The
  accepted clause is strictly *more* restrictive than the Article 2 franchise rule at
  `:337`, and derivation is monotone, so adding it subtracts nothing. Verified by
  accepting the chapter's own clause verbatim: `:accept all $x: person($x) & mature($x)
  & ~prisoner($x) -> decide($x, Ballot).` → `? decide(Hano, Ballot). => TRUE` with
  `? prisoner(Hano). => TRUE`. The chapter's real result — the clause *compiles*, where
  a floor-shaped one is refused — survives untouched; the sentence claiming it takes
  effect does not. `constitution.nibli:12-17` teaches exactly this: "A permissive rule
  left in place keeps its exploit." The pin file cannot catch it because `:49-50` pins
  only that the rule loads and never re-queries the ballot.
  Rewrite `09:71-79`: the clause is writable, and it bites only if the existing
  franchise rule is repealed alongside it — a two-line repeal, not one, which is a
  marginally better result than the chapter claims and should be stated as such rather
  than as a save. Add `? decide(Hano, Ballot). # => TRUE` immediately after the
  `:accept`.

- **`mature/1` is a silent franchise gate, and chapter 9 says the ballot needs nobody's
  permission.** `mature` has no producing rule anywhere (asserted only at `:606-609`), is
  absent from `derived_only`, and is directly assertable — so a polity disenfranchises a
  demographic by **declining to write adulthood into their records**, passing no rule at all
  and tripping no marker. The constitution's own comment at `:605` concedes the second half
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

### Chapter 10

- **Chapter 10: the third door is not gated on voiding, and the chapter says it is.**
  `book-1/10-contribution.md:50-68` claims "All three doors close for the same reason:
  a person whose credibility has been voided earns nothing" and closes on "putting the
  same condition on all three doors". There is no such condition. Article 3 gates
  teaching and work on `~false` (`:340-341`); the examiner rule (`:349`) gates on
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
  `~false($auditor)` to `:349`** and keep the prose. The guard stratifies (verified,
  loads at 0 errors). Either way the suite needs a pin on a voided examiner, because
  its absence is what let this reach print. Also correct `10:52-53` and any tracker
  prose repeating the claim.

### Chapter 11

- **Chapter 11 pins three of its four cases' inputs.** `11-where-people-are-put.pins.nibli:14-58`
  pins `severe`, `family` and the outcome for Hano, Ruk and Lalo, and leaves three facts
  the routing turns on untested: `? fit(Nando, Homestay). => FALSE`, `? family(Hano). =>
  FALSE`, `? family(Lalo). => TRUE`. Three lines, and they matter because `family/1` is
  the input the chapter misdescribes — a pin naming `family(Hano)` FALSE against a man
  who has no family fact is the cheapest place for that error to become visible.
  **Do not** add a pin "testing `fit/2` for a placement other than Homestay": `fit` has
  one producing rule and only ever carries `Homestay`, so `? fit(Ruk, HighSec). => FALSE`
  is a vacuous green of kind three above.

### Chapter 12

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

---

- **Chapter 12's pin NOTE claims a pin that does not exist.**
  `12-changing-the-rules.pins.nibli:7-9` says the file "pins two live defects: the
  self-declared target (`Amend_Sneak`) and the fact that `become()` feeds nothing." The
  first is pinned, at `:53-62`. The second is not and cannot be: "nothing reads `become`"
  is an absence, and all four `become` pins assert what does or does not become law,
  which is the opposite claim. Correct the NOTE to say one defect is pinned and the other
  is a grep, and put the grep in the runner. Worth doing early because it is the
  concrete, already-realised cost of the NOTE problem below: a header comment drifted
  from its own file, nothing detected it, and the drift propagated into this tracker.

### Chapter 13

No known defects. Read it against the constitution anyway.

### Chapter 14

No known defects. Read it against the constitution anyway.

---

## Constitution (KB) work

- **Add `~false($auditor)` to Article 4's reward rule.** `:349` is the only one of the
  three minting rules with no `~false` guard; `:340` and `:341` both carry one. The
  fix is one conjunct, the negative edge stratifies (verified), and it makes chapter
  10's headline sentence true. See the chapter-10 prose bullet for the fork — enact or
  rewrite, not both.

- **`lose/2` is a leaf: clawback records a loss and retracts nothing.**
  Test it on the rule BODIES, not with a bare grep — `awk -F'->' '/^[^#]/ && /->/ && $1
  ~ /lose/' constitution.nibli` returns nothing, and the only enacted occurrences are
  `:347` and `:348`, **both rule heads**. (A plain `grep 'lose('` returns three lines,
  the third being commentary at `:98`; and a grep that matches a rule's own head is a
  check that can never fail — see the chapter-8 pin NOTE for the same trap caught live.)
  No rule reads `lose`, so nothing downstream changes when it fires. **Care with the
  witness:** `reward(Bela)` is FALSE in the shipped cast, so Bela alone does not show
  it. Add `judge(Bela, Ivo). capture(Bela, Ivo).` and then `reward(Bela)` and
  `lose(Points, Bela)` are simultaneously TRUE — recognition earned by a person whose
  recognition has supposedly been clawed back. So `06-clawback.md:3` ("what they earned
  goes with it") and `:5-8` describe an effect the constitution does not have.
  The apparent clawback in the shipped cast is entirely the `~false` guards on
  `:340`/`:341` **never minting**, not `lose` **taking**. That makes `lose` the fifth
  member of the "determination, then stop" family, alongside `err`, `travel`, `become`
  and the Article 1b obligation `owe`.
  Derivation is monotone, so nothing can literally retract: the only expressible form
  of "taking away" is a guard on the minting rules, which is the fix above. If a
  downstream consumer is wanted instead, `all $x: lose(Points, $x) -> err($x,
  Recognition).` loads at 0 errors. Rewrite `06:3`, `:5-8` and `:103` to say
  recognition is **never minted** rather than **withdrawn** — the chapter's ceiling
  paragraph at `:98-101` already reaches for the right register, so the cost is three
  sentences, not the section.

- **Guard Article 9's head — one asserted fact voids a *person*.** `:524` is
  `all $m: all $t: adjust($m, $t) & permanent($t) -> false($m).` with **no restriction
  on `$m`**, and `adjust/2` is freely assertable. The single fact
  `adjust(Jala, Art_Floor).` gives, verified: `false(Jala)` TRUE, `lose(Points, Jala)`
  TRUE, `travel(Jala)` TRUE, `decide(Jala, Ballot)` TRUE. No imprisonment — but Jala's
  credibility is destroyed and the clawback fires **without** two independent credentialed
  auditors, without `~parent`, without `~deceive`, without a clean epoch. Article 4's
  whole apparatus is defeated by one write, because Article 9 reuses `false/1` as its
  amendment-invalidity proxy (`:519-521`) and never restricts the reused head to
  amendments. **The fix is free and verified**: appending `& suggest(Assembly, $m)` to
  `:524` restricts the head to docketed proposals, uses no new vocabulary, and
  regresses nothing — `false(Jala)` FALSE, `false(Amend_Floor)` TRUE,
  `become(Amend_Floor, Law)` FALSE, `rights-floor` 75/75 and chapter 12 14/14 still
  green. Splitting amendment invalidity onto its own predicate is the cleaner
  alternative and costs a corpus name.
  **No longer blocking anything, and the ordering note is withdrawn.** This used to read
  "do this before the shield fix below". The shield was ruled exposure-scoped on
  2026-07-30 and is not coupled to `false/1`, so nothing waits on this — but the attack
  is unchanged and still live against recognition, which is the reason to do it.
  **Its line references have rotted ~43 lines**: the rule is `:567`, not `:524`, and the
  reuse comment is `:562-563`, not `:519-521`. Re-derive before quoting.

- **`clear/1` is a one-fact conviction nullifier.** `clear` appears twice: `:505`
  (`all $x: clear($x) -> permits(Appeals, $x).`) and `:586` (Nia's ground fact). No
  precondition, no author, no guard, no `derived_only`. Asserting `clear(Adam).`,
  verified: `permits(Appeals, Adam)` TRUE, `prisoner(Adam)` **FALSE**,
  `expresses(Adam)` FALSE, `travel(Adam)` TRUE. `prisoner(Adam). # => TRUE` is a pinned
  verdict at `rights-floor.pins.nibli:186`, and one write flips it. Note the asymmetry:
  the Sock/Puppet void takes six writes, springing a convict takes one. Fix: derive
  relief from an adjudication rather than a bare flag — `clear($x) & judge(Appeals, $x)
  -> permits(Appeals, $x)` is verified to stratify and needs no new vocabulary. Until
  it lands, `03:83-88` should say plainly that nothing constrains who records it.

- **Rename the Article 6 `dwell` head — one atom is doing two jobs, and it blocks the
  `err/2` repair.** Every rule producing `dwell` requires `prisoner` (`:439`, `:442`,
  `:454`), and the Article 1 floor line at `:242` produces nothing — verified,
  `entitled(Bela, event { dwell() })` is TRUE while `dwell(Bela)` is FALSE. So
  `dwell(Lalo)` does not mean "Lalo is owed shelter"; it means "Lalo is housed at
  HighSec", and one atom carries both *entitled to a home* and *in a cell*. Free to
  fix, and a hostile reviewer finds it in an afternoon. Rename the placement head to
  `placed`, or fold it into `building`, and add the asserted counterpart the `err/2`
  fix needs. Six pinned verdicts move with it —
  `08-what-you-are-owed.pins.nibli:33,38`, `11-where-people-are-put.pins.nibli:19`,
  `13-the-one-thing-taken.pins.nibli:39`, `rights-floor.pins.nibli:47,82` — and so does
  `08:50`.

- **Fix `err/2` — the placement alarm has never once fired correctly, and release gave it a third victim.** `:447` reads
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)`, which tests *having a home*,
  not *having been placed at home*. Verified: it fires on Ruk and Lalo, both routed
  correctly to `building(HighSec, ·)`, and on nobody misplaced. **Release made it worse
  rather than exposing it**: `free(Hano).` takes `fit` away while `home(Hano).` stays
  asserted, so the alarm now fires on a released man in his own house — verified,
  `prisoner(Hano)` FALSE, `fit(Hano, Homestay)` FALSE, `err(Hano, Placement)` TRUE.
  **Three false positives, zero true positives** on the entire cast, and the newest one
  is not even in custody. That verdict is already carried as a DEFECT PIN at
  `rights-floor.pins.nibli:248-253`, so the repair has a green test waiting for it.
  An alarm with that record is worse than none. The fix is **not** "key it on `dwell`" —
  `:439` already requires `fit`, so a marker over the derived placement atom could never
  fire. The marker can only fire on an ASSERTED placement, so give the world a way to
  report one: a new asserted relation for "X was put at Y" (name from the committed alias
  corpus), checked against derived `fit`. That is Article 0's own evidence/conclusion
  split applied to placement, and it is the same repair as the `dwell` rename — **do that
  one first**. Repairing it flips `err(Ruk, Placement)`, `err(Lalo, Placement)` and the
  released-Hano pin FALSE, so three files move in the same commit:
  `rights-floor.pins.nibli:78,252` (`:80` already pins FALSE and stays), 
  `11-where-people-are-put.pins.nibli:49-53`, and "The alarm that does not work" at
  `11:50-81`, written against the defect on purpose. That rewrite is the intended outcome.

- **Mark confinement without conviction.** Nothing makes `building` derived-only:
  assert `building(HighSec, Rebel)` and no rule objects — no `injure`, no
  `judge(Court, ·)`, so `prisoner(Rebel)` is FALSE and `travel(Rebel)` stays TRUE. The
  constitution certifies as free a person it is holding. The prescribed rule was run
  verbatim and both fires and stays quiet in the right places:
  `all $x: all $f: building($f, $x) & ~prisoner($x) -> err($x, Confinement).`
  **Re-run that before trusting it.** `$f` is body-only over a derived relation, which is
  the exact shape that silently derived nothing when Article 8b was built —
  `err($x, $k) -> obliged(Review, $x)` loaded clean and gave FALSE for everybody. If the
  same thing is happening here the recorded verification is measuring an inert rule. The
  fix if so is a constant in slot 1, as Article 8b uses. Use a
  third `err` flavour rather than reusing `Placement`, matching `err(_, Isolation)` —
  the audit surface stays one predicate while each breach stays separately queryable.
  Highest value-per-line in this section.

- **Write the fact-write trust base as a file-level section — Article 0 closed half of
  it.** `:51-60` now declares ten relations `derived_only` — `severe` joined them in
  v0.5 — and direct assertion of each is refused. What Article 0 did **not** do is remove the write surface; it moved
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
  `grep derived_only new-book-plans/constitution.nibli` rather than editing a list in
  place — nine relations are closed, everything else is open — and record **three**
  undefended classes, not one. **Assertion**, at minimum `public`, `clear`, `choose`,
  `mature`, `person`, `show`, `injure`, `judge`, `capture`, `broken`, `rotten`,
  `deceive`, `severe`, `family`, `parent`, `teaches`, `work`, `home`, `suggest`,
  `approves`, `adjust`, `permanent`. **Deletion**, `person` first, then `permanent`,
  `severe`, `public`, `choose` — and note Article 1b added a fourth institution fact,
  `public(State).` at `:320`, the sole route to `authority(State)` via `:481`, so one
  deleted line makes the duty-bearer unexposable — the file discloses this class for `permanent()` alone,
  at `:529-533`. **Vocabulary**, per the bullet below. Prose consequence, and it is the
  reason this is not only a KB item: `03-who-holds-the-pen.md:100-103` tells the reader
  the Sock/Puppet hole is closed, and it is closed only against *forged credentials* —
  two `choose(Electorate, ·)` writes still seat the puppets and the credential derives.
  Rewrite it to name the cost in **writes** rather than in elections.

- **The evidence vocabulary cannot be entrenched — disclose it instead of patching it.**
  The threat is real and the book prints it at `01:133`, but the old prescribed fix was
  measured and does not close it. `permanent(Art_Evidence).` was applied verbatim and
  run: it kills an amendment that DECLARES that target and kills nothing else.
  `adjust` is self-declared by the proposer (`:524`), so an amendment naming no target
  enacts (`become(Amend_Sneak, Law)` TRUE) and one naming a harmless target enacts too
  (`become(Amend_Lie, Law)` TRUE) — and widening the vocabulary needs no amendment at
  all: `dangerous(Esa).` asserts straight into the store and no rule sees it happen.
  Entrenchment guards targets a proposer admits to; the vocabulary is not a target, it
  is the store. Fix: drop the `permanent(Art_Evidence)` idea, record the vocabulary as
  the third undefended class above, and take the real closure as a nibli handoff.

- **Guard the personhood roster — one deletion defeats all eight rights, and the
  obvious repair only renames the target.** `person` has **30** asserted facts and
  **two** producing rules — `prisoner -> person` (`:254`) and `free -> person` (`:264`,
  added with release) — so imprisonment is the only route in that needs **nobody's
  permission**, not the only non-assertion route; the `free` route needs one written
  fact, and that fact is itself on the evidence list. The counterfactual's own pin file
  (`counterfactual/no-person-line.pins.nibli`) has stated this correctly since release
  and this bullet did not get the update. Verified by deleting `:542`
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
  **The prose half of this landed 2026-07-30** with the decision to put `person` on the
  evidence list: `01`'s new closing section states all three vectors — forging an entry,
  withholding one, deleting one — says the sanctions survive de-personing while every
  right goes, and says outright that no rule can close it because an absence is not
  visible from inside the record. What remains here is the obligation itself, not its
  disclosure. Do not re-derive the disclosure; extend it if the obligation gets built.

- **Close `entitled` *and* `owe` — the floor's own two relations, and the gates Article 0
  forgot.** Article 1b added the second: `owe` is not among the ten `derived_only`
  declarations and its head is a rule, so the relation is open to direct assertion exactly
  as `entitled` is, and forging `owe(State, Provision, Sokk).` forges the record of what is
  owed to a non-person. Verified: `entitled(Sokk, event { eats() }).` asserts cleanly onto the live
  constitution and answers TRUE while `? person(Sokk). => FALSE`. Nothing reads
  `entitled`, so this forges no downstream verdict — it forges the *record of what is
  owed*, which is the one thing the floor is. The obvious fear is unfounded and was
  checked: closing the relation does **not** refuse the floor lines at `:240-253`,
  because floor lines compile to rules and `derived_only` refuses only ground
  assertions. With `derived_only("entitled").` added: the floor still derives, the
  firewall still refuses the heresy law, the non-floor control still loads, and the
  forgery is refused. Article 0 goes from ten closed relations to eleven — `severe`
  closed the tenth in v0.5, and three bullets went on saying nine until 2026-07-30.
  **`person` is not a candidate and never will be**: closing it would refuse all 30
  ground facts and collapse the cast, which is why chapter 1 now discloses the roster
  as a gap no rule can close rather than promising a guard.

- **Decide the Article 4 clawback question.** The two rules are `:347`
  (`false($f) -> lose(Points, $f)` — docks the wrongdoer, fairer, still a subtraction
  from a person's record) and `:348` (`teaches($t,$s) & false($t) -> lose(Points, $s)`
  — docks a **student** for a teacher's fraud: negative scoring, of a person, who did
  nothing). Verified: `lose(Points, Bela)` TRUE, `lose(Points, Cira)` TRUE. Legacy
  `book.md` bright line 2 — *"No negative scoring of persons"* — is contradicted by
  both, and note it is a **legacy** line recorded in `CLAUDE.md` under historical
  decisions, not one book-1 has adopted. Decide which side gives: either the bright
  line narrows to "no subtraction except by due process for one's own adjudicated
  fraud" and `:348` is deleted, or the clawback rules go and sanctions reach perks
  only. Do not leave both in print. Narrowing flips `lose(Points, Cira)` FALSE and
  rewrites `06:40-91`; that is the intended trade and `06-clawback.pins.nibli:6-16`
  already records it. **The middle option is now closed.** Since the grades ruling
  settled that students never mint, "claw back only the rewards that came from the
  fraudulent teaching" is the empty set for every student by construction — so
  narrowing `:348` is not narrowing, it is deleting it, and it should be decided as a
  deletion.

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

- **Build the first delivery route: verified teaching delivers learning. VERIFIED TO WORK,
  and it is the highest-value item in this section.** Nothing in this design touches the
  floor. Rule heads producing each floor right: `learn` 0, `eats` 0, `healthy` 0, `secure`
  0, `believe` 0, `meets` 0 — and the two that are non-zero, `dwell` (3) and `expresses`
  (1), derive only from `prisoner`. **Teaching does not produce learning**: `teaches($t,$s)`
  produces `reward($t)` and nothing else. So the society's only working provision runs
  through its prisons.
  A floor predicate may be a **rule head** — `dwell` and `expresses` already are, and
  INVARIANT 1 forbids only rule *bodies*. Verified on the live engine 2026-07-29: the rule
  `all $t: all $s: teaches($t, $s) & capture($t, $s) -> learn($s).` is **accepted**, the
  firewall still refuses `person & ~believe -> prisoner`, and the non-floor `~home` control
  still loads. So the delivery layer is expressible and does not cost the firewall.
  **Keep the entitlement and the actuality apart when writing it.** `entitled(every person,
  event { learn() })` stays unconditional; `learn(X)` becomes trackable. Written carelessly
  this reads as "you have the right to learn only if you passed", which is the
  eligibility-computation-upstream-of-rights structure the design refuses everywhere else.
  **And do not name it "verification".** Examining a person and recording a finding is
  already `judge` + `capture`, and two credentialed people from different bodies doing that
  to one person complete Article 4's multi-sig and **void them** — verifying a student
  twice, once by each body, would destroy their credibility. The probe above uses `capture` deliberately to expose that; a real delivery rule
  needs its own predicate.
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
  mechanism is wrong.** Article 7 (`:458-484`) carries no stratification note. Adding
  `person($w)` to the shield rule at `:470` is the most natural tightening anyone would
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
  fail-**open** toward protection and defends the choice explicitly at `:407-413`.
  Article 6's `~permits(Appeals, $offender)` (`:385`) is fail-**closed** against
  protection and gives no reason at all. Since v0.3 relief is an asserted `clear($x)`
  feeding a derived `permits(Appeals, ·)`, so the *absence* of a granted relief is what
  convicts. Same file, opposite defaults on the absence of a finding, one justified and
  one silent. Fix: either give Article 6 the same explicit polarity note, or separate
  standing-to-seek-review from a granted relief that stays the sentence, or require an
  affirmative exhaustion fact for conviction. **Do not re-open the fail-open window in
  the chapter** — `04:54-81` defends the choice and `:120-124` names the cost outright.

- **Give `rotten` — and `capture` and `judge` — an expungement path. URGENT: release
  landed and this did not, so the asymmetry is now live in print.** A single void is
  perpetual and compounds, with no route back, while a conviction can now be finished.
  That makes losing your credibility the harshest sanction in the design — harsher than
  imprisonment. Note the comparison it invites is with *standing*, the other sense, at
  `02-standing.md:41-42` (*"This is the only thing in the
  entire society that is protected that way. Everything else can be lost"*) and sits
  badly beside `10-contribution.md:50` (*"Nothing to earn it back with"*). The author
  decided on 2026-07-29 that both halves are designed together; only the first half
  shipped.
  **The shape is known and cheap**, because it is the shape release used: an asserted
  expungement fact as a `~<expunged>` body conjunct on the multi-sig rule (`:346`) and on
  `rotten -> false` (`:499`). Both are safe — the predicate is stratum 0 and `false` is
  stratum 1, so no cycle. **Do not** put `~false` in a `false`-headed rule; the file
  records that exact attempt failing as E2 at `:24-26`. Costs one more evidence entry
  (22 → 23) and the nine prose sites move again, so consider landing it in the same pass
  as the severity dimensions rather than alone.
  Worth framing in the book as forgiveness being a *right* rather than as a bug fix.

- **Put a precondition on `capture`.** `capture($a, $audited)` has no precondition
  anywhere: any credentialed pair — one Review, one Tribunal, since v0.7 — can void any
  person for no stated reason, and the book never admits it. The cross-body requirement
  raised the cost of assembling that pair and did nothing about the missing grounds. Needs one design decision — which predicate
  carries "grounds", since adding one enlarges the evidence vocabulary — after which
  the guard is a body conjunct. Pair with an epoch expiry on `capture` and `judge`.

- **Widen kinship beyond `parent/2` — the fix is available today, and it is not free.**
  Article 4's independence check names one relationship (`:363`, not `:346` — that is
  now the v0.7 comment header), so spouses and siblings co-sign. **Not blocked on the
  engine**, as the old wording implied: `married` (speni), `brother` (bruna), `sister`
  (mensi) and `sibling` (tunba) are already in the committed corpus
  (`nibli-lexicon/src/corpus/predicates.rs:331,1444,2167,2185`). Appending
  `~married`/`~brother`/`~sister` in both directions was verified to load at 0 errors and
  to leave `false(Bela)` and `false(Lupo)` TRUE.
  **The recorded probe is stale and the gap is narrower than it says.** *"Two
  Electorate-seated siblings void a stranger — `false(Targ)` TRUE"* predates v0.7:
  `permits(Review, ·)` derives from `choose(Electorate, ·)` (`:518`) and
  `permits(Tribunal, ·)` from `choose(Convocation, ·)` (`:537`), so two people seated by
  the same body cannot co-sign at all now. The pair must span bodies — one seated by
  each — which is still reachable for a married couple or siblings and is what `05`
  now describes. Re-run the probe with a cross-body pair before quoting a verdict.
  **The cost is what needs deciding, and it is the only thing left open here.** It takes
  the evidence vocabulary from **23** to **26**, and enlarging it is the quietest way to
  capture a system — the file's own threat model.
  **The prose half landed 2026-07-30.** `05`'s costs section no longer says the record
  *cannot* express marriage; it says the words exist, the widening has not been judged
  worth it, and discloses that as a choice. So the fork is gone: what remains is whether
  to land the rule, and the chapter is already honest either way. The old note that
  `01:3-18` "counts the list at twenty-one and calls it exhaustive" is doubly dead —
  chapter 1 names no number at all, and `person` has since joined the list.

- **Check each governance item against what the rules can express, before any prose.**
  Parts I–V are gated on derivation, and the constitution has no predicate for a
  community, a transfer, a tax, or a term of office — so none of the following is
  derivable today and all of it is constitution work first. In dependency order:
  - Recall is one asserted `broken(·)` fact (`:624`, consumed at `:494`) — at-will, no
    threshold, no administering body, no term. Replacing it also rewrites `02:55-59`
    and `03:53-60`, which describe it as is.
  - The magnet problem: mobility is derived at `:324` and there is no community concept
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
  vocabulary reads **23**; no formalism has leaked into a derived chapter; counted claims in
  the prose have not increased (a ratchet — lower `BASELINE` in the same commit that removes
  a site); **the engine is rebuilt from source and the commit it was built from is printed**;
  seven absence claims still hold; no floor right is read into anything but `err`
  (INVARIANT 1); recognition is never counted; there is no arithmetic in the constitution;
  the pin suite is green and the number it ran equals the sum of `:expect-pins` across the
  fifteen files; and the three counterfactual fixtures still prove what the book says.
  **The engine build is not housekeeping.** A stale `nibli-pin` is invisible here — the pins
  check the constitution, not the engine, so an out-of-date binary returns the same green
  359/0 and the same runtime. That happened on 2026-07-31 and would have read as "the
  upstream NAF work achieved nothing". `cargo build --release` before the pin step costs
  ~0.2 s incremental; `NIBLI_PIN` skips it, because overriding the path is how you
  deliberately test a different build.
  **Every check was negative-controlled before it was trusted, and one failed the control.**
  The tracker's original jargon pattern (`stratum|strata`) does **not** match *stratifier* —
  the likeliest leak of all, since it is the word this tracker uses constantly — and a
  chapter containing it passed. `strat` alone is too greedy: it matches "demonstrate", which
  is in chapter 14. The shipped pattern uses three explicit stems and was checked both ways.
  The absence checks carry a positive control (`/false/` must return 5 rule bodies) for the
  same reason: a grep that also matches a predicate's own rule head can never fail, which is
  a trap this repo fell into twice in one day.
  Left to do: fold the ~29-minute pin run into something a person will actually run before
  every commit. The phase-1 successor prompt is the real fix — materialising the positive
  side and persisting the saturation across a file — and expansion is what makes it urgent,
  since ~600 pins projects back past 45 minutes even at the post-materialisation rate.

- **Wire the vocabulary guard in, and stop calling it a closure — 97 pins stay green
  when the evidence vocabulary is widened.**   … (and at :966)   at all: chapter 1's suite
  and the constitution's suite both pass, `PASS — 97 pins`.

- **Pin the three Article 0 closures that nothing guards: `defend`, `reward`, `become`.**
  Article 0 closes nine relations and the file says those closures are "what makes
  Articles 4, 6, 7 and 8 mean what they say". Repo-wide only six have a `:refuse` pin.
  The three unpinned ones are the shield, the mint and the enactment gate — the heads of
  Articles 7, 3 and 9. Verified that all three refusals hold today and the pins go in
  as-is. Add to `rights-floor.pins.nibli` beside the other six and bump `:expect-pins` from 91 to
  94. Ten minutes' work, and without them the file's own named failure mode at `:44-47`
  — a `derived_only` line moved below the facts it guards "is inert and looks identical"
  — takes three of the nine gates with it in silence.

- **The floor's own relation is now queryable in two places and controlled in none.**
  `grep -rn entitled book-1/*.pins.nibli new-book-plans/rights-floor.pins.nibli` returns two,
  both added with Article 6 release: `rights-floor.pins.nibli:227`
  (`entitled(Hano, event { eats() })`) and `13-the-one-thing-taken.pins.nibli:90`
  (`entitled(Hano, event { dwell() })`). Neither is paired with a control, so both still
  prove reach rather than derivation. The queryable shape discriminates in three directions
  at once, verified: …[rest of bullet unchanged]… Add
  `? entitled(Bela, event { eats() }). # => TRUE` beside `? eats(Bela).` in chapter 8,
  one `entitled` pin for Zed in chapter 7, and the `home` and non-person controls in
  `rights-floor.pins.nibli` — without the controls the pins above pass for the wrong reason.

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

- **The eight floor rights are sampled, never enumerated — and the omitted one is exactly
  where the claim fails.** `08:32` says "the same answer comes back for every one of the
  eight", and the pin file tests seven, omitting `expresses`. Chapter 7 is worse: the
  comment at `07-a-prisoner-is-a-person.pins.nibli:29-32` says "the floor derives for Zed
  like anyone" and pins one right of the eight. Eight pins per subject is not expensive
  and it is the only shape that makes "every one of the eight" a checked sentence rather
  than a summary. Put the pin block in **before** the chapter-8 rewrite, so the rewrite
  has something to write against.

- **Bring the pin-file NOTEs into line with the checks that now run them.** The five
  absence claims — nothing reads `owe`, `become`, `travel`, `err` or `lose` — are no
  longer instructions to a human: `verify.sh` runs all five with a positive control, so
  they fail loudly, and the no-arithmetic check runs beside them as a sixth. What is left
  is the prose. One NOTE still tells a reader to run an unspecified grep
  (`10-contribution.pins.nibli:6-9`); chapters 8, 13 and 14 were already corrected to test
  rule bodies with a control. Point it at `./verify.sh` instead of restating a command,
  and **while in `12-changing-the-rules.pins.nibli`, fix the claim beside it**: its NOTE
  says the file "pins two live defects" when the second is an absence no pin can hold — a
  header that drifted from its own file, undetected, which is the whole argument for this
  bullet.

- **Extract the claim-to-query table from the pin files — it cannot be generated from the
  constitution.** The substance already exists in a better form than the old bullet
  imagined: fifteen pin files carry every load-bearing sentence, every one a query with an enforced expected
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

- **Fix the upstream test citation in the constitution.** `constitution.nibli:182` cites the
  five regression tests that pin the floor firewall at `integration.rs:3228`; they are at
  `:3475-3571`. That citation is the only pointer from the constitution to the tests whose
  deletion would silently end the firewall argument, so it is worth being right.

---

## book-1 — remaining writing

- **Write the opening note — the last unwritten non-derived element, and nothing else
  tracks it.** ~800 words before Part I, explicitly non-derived and labelled the way Part V
  is labelled, so the book does not open cold on vocabulary; it claims no derivation and
  carries no verdicts (`new-book-plans/3-spine.md:91-94`). One of exactly three sanctioned
  exceptions to the inclusion gate. No file exists. It is also where the licence line and
  the title/subtitle will have to live, so it unblocks the licence bullet below. Write it
  against the final wording, which is settled: *The Rights Nobody Has to Earn — A design
  for a society worked out to the point where it catches its own failures.* **Check the note against the counted-
  claims ratchet before committing it** — it will be the fifteenth file in `book-1/*.md`
  and therefore the first new prose the ratchet has ever scored. The subtitle itself is
  clean; a note that opens by naming the floor's size would not be.

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

- **"The Furnished Prison" — a rejected title that is a good part title.** Scored highest
  of the twenty title candidates on pick-up and lowest on legibility, so it lost the cover
  and is wasted sitting in git. It is the phrase at
  `13-the-one-thing-taken.md:169-171` — *"A society whose only working provision runs
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

- **Expand Parts I–IV from 15,436 to ~38,000 words.** DECIDED 2026-07-29; the invariant and
  the budget are in `CLAUDE.md`. This is the largest single item in the tracker — **+22,564
  words**, mean chapter 1,103 → ~2,714 — and it is one bullet only because the work is one
  decision; it becomes fourteen commits. **Know what it is not:** the invariant does not
  force it. Break-even is derived > 17,800, so Parts I–IV could stay near 18,000 and
  majority-derived would still hold. The 38,000 is an editorial choice about the book's
  size, and it means Part V's 12,000 must be justified by content rather than by ratio.

…and at :1674:

  Available ≈26,200 against 22,564 required. The margin is thin enough that the complement
  screen and the absence cap have to be enforced or the shortfall becomes padding.


  **Every chapter revision also strips its counted claims.** A per-chapter check, not a task of
  its own. Do not write "twenty-two entries", "four people have shelter", "eight rights" or "one
  thing taken" — **state the rule that produces the count** instead. Every counting claim in this
  book that was checked turned out *wrong*, not merely stale: "every convicted person" named four
  of seven, "one person verifiably has shelter" was four, "everything else on both lists is
  identical" differed in four places, "the four cases exhaust the combinations" covered seven of
  eight. And the numbers keep moving — the evidence list changed in a single commit, the floor
  may stop being eight, and more than one thing may become takeable. `verify.sh` carries a
  **ratchet**: 28 sites after v0.5, down from 38; it fails if the count rises, and it also fails
  if the count falls without `BASELINE` being lowered in the same commit, so the tightening
  cannot be forgotten. When it reaches zero, make it a hard gate. **Chapter 1's cluster is
  cleared** — it held the largest group, all the same evidence-count claim, and the chapter
  printed the entire list two sentences later, so the numeral was redundant with the evidence
  beside it; closedness is now carried by "when someone wants to say something that is not on the
  list, they cannot". Chapters 3 and 5 went with it. The remaining sites are concentrated in
  **chapter 8** (the shelter arithmetic, which is wrong on its own terms — see the prose section)
  and **chapter 7**. And
  **chapters 9 and 14 count chapters** ("twelve chapters later", "fourteen chapters"), which the
  computed spine can invalidate silently with no pin able to catch it. Rhetorical durations
  ("thirty years") are exempt and allowlisted in the guard.

- **The rule that decides whether expansion is cheap — verified, do not re-derive it.**
  *Ground facts over predicates that already occur in the constitution are structurally
  free. Anything that introduces a predicate name, or a rule head, is not.* A ground fact
  reaches only `all_preds` in `5-spine-gen.py:77-80`, so if the predicate is already there
  the generated block is **byte-identical** — predicate count, derived count, rule count,
  strata, the floor list, the evidence list and therefore chapter order all unmoved. A body
  conjunct is free too (`rules` counts arrows, not literals). A **new predicate name** costs
  the evidence list 23 → 24. That used to falsify chapter 1's headline number in nine
  prose places; all nine were converted to rule-statements, and no chapter names a count
  any more, so the cost is now the spine check and `verify.sh`'s gate on 23 rather than
  prose — cheaper, and it fails by name instead of quietly. A **new rule** moves the rule count
  and may add a stratum, which would add a chapter, which the computed order forbids.
  **Structural freedom is not verdict freedom, and this is what will actually bite.**
  Article 4's multi-sig quantifies over two auditor variables, so a new person naming
  *existing* constants can complete a rule no existing pair could satisfy: four facts
  (`person(Ann). choose(Electorate, Ann). judge(Ann, Tyr). capture(Ann, Tyr).`) flip
  `false(Tyr)` FALSE→TRUE and destroy chapter 5's headline case. **Every argument position
  in every new fact must be a new constant**, except the four institution constants — and
  even those need care, since `judge(Review, ·)` is the deceit adjudication and
  `broken(Court).` is a universal amnesty. The rule is a heuristic; `verify.sh` is the proof.

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

- **Oversight of the duty-bearer — enablers, their checkers, and the meta-study.** Raised
  by the author 2026-07-31 while ruling the homeless-convict gap: if shelter is owed and
  somebody has none, the people who deliver it should have to study why, and somebody
  else should have to check on *them*. Right instinct, wrong book. In book-1 terms it
  duplicates two mechanisms that already exist and are deliberately inert — `owe`, which
  nothing reads (`08:122-126`, "Nothing compels the body"), and `err`, whose read
  question is its own gated bullet above. And the constitution has no vocabulary for a
  study, an inspection, oversight, a community or a transfer; verified, the grep returns
  nothing. So this is institutional design with a lexicon ask under it, which is book-2's
  subject exactly. **Its book-1 half is already queued**: the `err`-feeds-an-obligation
  decision. Do not build the structure here; rule that one and stop.

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
./verify.sh            # ~10 min: engine build, spine, evidence count, jargon, absences, the suite, counterfactuals
./verify.sh --quick    # ~2 s: everything except the pin suite
```

Prefer it to any check by hand. It exits non-zero on the first failure and names the
claim that stopped being true; every check in it was negative-controlled, and one — the
jargon sweep as this file used to specify it — did not catch the leak it was written for.
Use the **release** `nibli-pin`, never `nibli-host`; the script now builds the engine
itself and prints the commit, so a stale binary can no longer pass green.

**Two facts about the floor that no command teaches.**

- **A floor line is a compile-time prohibition, not a declaration**, and since Article 1b
  it covers the duty as well as the eight rights. `entitled(every person, event { P() })`
  compiles to a rule with `person` in the body, so `P` sits downstream of `prisoner`; any
  later rule taking `~P` into that cone is an unstratifiable negative cycle and is
  refused. The floor is protected **because** it is reachable — at stratum 0 there would
  be no cycle to close and no protection at all. Where it stops is pinned in
  `08-what-you-are-owed.pins.nibli`: `~P -> false`, `~P -> lose(Points, ·)` and positive
  compulsion `prisoner -> P` all still load. It blocks punishment for ABSENCE, never
  manufacture, and it reaches `prisoner` only. Five upstream regression tests pin the
  asymmetry at `nibli-engine/tests/integration.rs:3475-3571`.
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
