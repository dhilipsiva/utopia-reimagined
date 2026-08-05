# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Repository Is

A book-writing project heading for **two new books**, with the original two manuscripts slated for deletion:

- **book-1** — the active work. Two parts to its scope, and the seam is deliberate:
  - **Parts I–V — the destination.** *What an ideal society must be and how it functions* — **never how to get there.** No roadmap, no transition, no MVS, no scaling story. Spine is *derived*: chapter order is computed from the dependency stratification of a formal constitution in nibli KR (`new-book-plans/constitution.nibli`), and content is **gated on that constitution** — if the KR does not derive it, it does not go in. **Jargon-free**: a general reader can finish Part V and stop, and the formalism is never mentioned here. Exactly three elements are exempt from the derivation gate and each is labelled as such in the text: a short non-derived **opening note**, **Part V** (argument and evidence), and the final method part. What they verify is the **data**.
  - **Final part — the method, explicitly optional.** Shows the machinery to whoever wants it: the constitution, the derived spine, the compile-time firewall, the evidence/conclusion split, and what the logic *refused*. Clearly labelled as a different kind of reading. This is the only place in book-1 where the formalism appears, and its existence is what answers the "you built a machine and hid it" objection.
- **book-2** — **how you would actually build it, organisationally and technically.** The transition material (MVS, the family→village→planet scaling story, legal collisions, costed transition) *and* the technology stack. Where book-1's claims are gated on derivation, book-2's will be gated on **evidence, costs, and data that regenerate by script** — the seam is epistemic, not editorial. It has a seed tracker now, `book-2/TODO.md` — **unordered until its chapters are decided**, seeded from the old hold list and the adoption reviews; collect there, do not work there while book-1 is active. book-1 references it exactly once, at the very end.
- **`book.md` and `manifesto.md`** — legacy. To be deleted once both new books exist, but **not before** the legacy-harvest section of `TODO.md` is complete: `book.md`'s 55 sourced references, the nine historical cases, the Bharati poem, and the five bright lines all need porting first.

So this is no longer only Markdown editing: there is a constitution to verify against the real engine, and a data pipeline to build. See `TODO.md`.

## Author-Ratified Book 1 Mandate — 2026-08-03

**The author has chosen the expanded mandate.** Book 1 is to become a complete
constitutional interface for a free society: universal standing; non-reciprocal
material floors; liberties and due process; democratic authority; public duties;
separation of public functions; records and accountability; locality; emergencies;
and common-resource/intergenerational limits. This is a scope decision, **not** a
claim that the present constitution or book already achieves that coverage.

[`new-book-plans/book-1-constitutional-coverage-map.md`](new-book-plans/book-1-constitutional-coverage-map.md)
is the controlling planning artifact. Before a new domain is drafted, its row must
specify its holder, duty-bearer, minimum or limit, admissible evidence, failure,
interim continuity/remedy, appeal, audit, independent check, and Book 2 handoff.
A named right, body, or value is not a complete constitutional interface until it
is formalised, pinned, counterfactually tested, and described accurately in
derived prose.

This supersedes as a **scope class** the previous Book-2-only governance-vocabulary
ruling, learning-only delivery ruling, Book-2-only duty-bearer-oversight ruling,
and roster-integrity-as-disclosure-only ruling. Book 1 may now add coherent
constitutional rule families for public authority, democratic limits, delivery
evidence, breach, continuity, remedy, review, and record integrity. It may not
smuggle in operations: transition, tax rates, budgets, staffing, procurement,
facilities, service workflows, clocks/calendars, record technology, cryptography,
and case administration remain Book 2.

**T3 is author-ratified (2026-08-03) and implemented in stages for case-bound
Court custody (2026-08-05).** T1 reconciles witnessed predecessor/successor
records and selected carry. A witnessed passport selects one constitutional
lineage, and only its collision-free terminal accepted successor can give
carried adverse/clear status or public power current legal effect in a fresh
evaluation. T2 builds independently witnessed, typed event and record paths;
transitive cycles propagate conflict within their path type. T3 makes the exact
current, source-bound review a positive premise of custody authority and rejoins
the case subject, Court holder, Court judgment, injury victim, lease, window,
renewal, source, and current-record witnesses. Competing witnessed source,
window, case-subject, or lease bindings fail closed; the judgment and victim evidence
are case-bound but have no general truth or uniqueness proof. Compact
identifier-status conclusions are never sufficient alone: every
consequential consumer rejoins the exact raw tuple and its matching witness
fields. The current constitution still admits no duration arithmetic, sentence
clock, filing deadline, or operational cadence, and it cannot make a successor
arrive or prove that an outside clock advances. The reviewed contracts,
two-snapshot harness, adversarial matrix, and residual Book 2 boundary live in
`new-book-plans/book-1-time-model-decision.md` and
`new-book-plans/temporal-assurance-case.json`. Another public power requires its
own temporal contract; Book 2 continues to operate clocks, calendars, witnesses,
publication, recovery, and time services.

**The constitutional taxonomy is author-ratified (2026-08-03).**
`new-book-plans/book-1-constitutional-taxonomy.md` is an author-chosen planning
grammar for Phase 2, not a derivation, a claim that the named classes are
exhaustive, or current formal coverage. Liberty limits bind public power directly
and public institutions are responsible for preventing, investigating, and
remedying private interference; no general private horizontal effect is implied,
and a future direct private duty must be named expressly.
Property is a conditional liberty bounded by floors and commons. Merit,
recognition, contribution, qualifying thresholds, and personal scores may not be
allocation keys for material security, standing, authority, political voice, or
property/commons access. Commons and future-condition claims have standing for
any present person and an independently checked public guardian; the guardian's
authority, evidence, independence, and removal remain Class 6/7/9 contract work.
Structural refusals remain cross-cutting walls, not ordinary subject-matter
rules: Article 1's firewall, `admits`, `derived_only`, and verifier guards keep
their own enforcement and test obligations. This ruling adds no predicate, duty,
or present remedy.

The existing guardrails survive the expansion: no floor may depend on work,
virtue, wealth, citizenship, documentation, score, compliance, or approval;
recognition remains non-ranked and non-operative; no provider's assertion alone
proves delivery; and Part V cannot create a right, power, or exception. The
democratic corridor is a **ratified constitutional design rule, not yet a formal
guarantee**: a majority chooses only among policies compatible with universal
standing, core floors, equal protection/non-discrimination, due process, core
liberties, and commons constraints.

**Book 1's public-edition boundary is author-ratified (2026-08-04): E2 + P1 +
D2.** The pre-expansion baseline remains public source and git history but receives
no promoted edition, canonical serialization, assembled release, or print
identity. The completed constitutional expansion becomes Book 1 — First Edition
and its first print-on-demand edition. Before completion, coherent expansion
milestones may appear only as immutable, tagged First-Edition previews with
permanent URLs, exact book and nibli sources, full verification records, and
visible supersession; they are design snapshots, not promises of final chapter
order. `main` is never an edition URL, and no public artifact may be silently
replaced. The controlling publication contract and release gates are in
`new-book-plans/book-1-edition-boundary-decision.md`. This ruling creates no tag,
release, site, preview, or print file by itself.

**`lose` and legacy `decide` are relation-wide conclusion-only — L1 + D1,
author-ratified and enacted 2026-08-04.** Both had been closed only by omission:
adding the exact `admits("lose")` or `admits("decide")` declaration made the
corresponding ground conclusion writable. Article 0 now reserves each relation
at every arity and through any future converted alias. Rule heads remain open:
the existing clawback and franchise rules still derive, and a hostile rule can
still derive either conclusion. `lose` remains an unread leaf with no amount,
proportionality, restoration, or remedy. `decide(_, Ballot)` is the current
franchise conclusion, **not** a cast ballot, delivery fact, tally, election, or
legal result; those interfaces need distinct names, and democratic redesign may
later retain or atomically replace the legacy relation. This is not a complete
closure sweep. The floor actualities, `obliged`, and `travel` remain
unadmitted and not conclusion-only pending their delivery, duty, and liberty
contracts under the generated assertion-surface audit. The controlling record is
`new-book-plans/book-1-closure-gaps-decision.md`.

**The assertion surface is generated and verifier-enforced, enacted 2026-08-04.**
`new-book-plans/7-assertion-surface.py` reconciles the engine's rule-produced
relations with active `admits` and `derived_only` declarations. Its reviewed JSON
ledger must classify every derived relation and provide an authority, provenance,
harm, challenge, and risk contract for every effective ground-writable premise.
A new head, ground-only admission, posture change, producer/consumer route change,
current ground-fact snapshot change, or missing contract field fails `verify.sh`;
edit the ledger and regenerate the Markdown audit together. The audit is an
inventory and reviewed threat model, not proof of real-world provenance. Its
scenarios are reviewed, not executable pins; the assurance case consumes the
inventory without upgrading it into runtime evidence.

**The record-integrity assurance case is generated and verifier-enforced,
enacted 2026-08-04.** `new-book-plans/8-record-integrity-assurance.py` validates
the authored `record-integrity-assurance-case.json`, binds it to the exact
assertion-surface contract digest, and requires every current writable premise
to belong to a record class whose claims cover every mandatory assurance
dimension. Those classes are reviewed grouping choices, not derived or
exhaustive constitutional categories. The case separately treats every use of
absence as an effective premise requiring a route-specific closed-world contract;
the positive writable-relation census does not make deletion-authored absence
safe. The generated case's top verdict is deliberately
**NOT ESTABLISHED** for the live record system: the repository verifies bounded
consequences of supplied records, not their authorship, truth, genesis
completeness, persistence, append-only history, recovery, or eventual
advancement. The case specifies Book 1's
authorship, authority, basis, privacy, challenge, independent-witness,
correction, reconciliation, failure-default, reader, action, continuity,
recovery, and remedy controls while leaving identity, storage, cryptography,
replication, clocks, availability, release/toolchain integrity, and operations
to Book 2. A complete visible basis is also insufficient if a consequential
decision uses a prohibited shadow input. The assurance source, ledger,
generators, verifier, engine, and review can be weakened together; their green
result does not authenticate or authorise their own trust root. It changes no
constitutional rule by itself. In particular, one flat snapshot cannot
distinguish a deleted entry from one withheld or never written.

**Bounded flat-snapshot red-team enacted 2026-08-04:**
`9-record-integrity-red-team.py` executes selected unauthenticated status
additions, exact ground-entry deletions, rollback pairs, generic-judgment reuse,
and same-snapshot combinations. It proves their consequences in supplied flat
records and confirms that a raw `rotten` report is inert. It deliberately does
not duplicate T1/T2/T3 transition, carry, order, or custody tests; it does not
attribute a runtime write or absence, authenticate a record, recover an entry,
or make a successor arrive. It checks itemised `owe` debts and their opaque
event-abstraction `entitled` projections together against the full constitution.
No second registration, adulthood, release, or carry gate was added.

**Full-source and composed opaque floor execution restored 2026-08-05:** release
Nibli `5cec80080eea0334c87508e60813f8f70f487441` first removed the temporary
extracted-floor isolation. It repaired two independent global costs: eager
materialisation of every eligible relation and backward witness generation over
the global typed domain and every Skolem family without first using relation
anchors and bound siblings. The exact full-T3 food entitlement fell from a
180.24 s timeout at 1,850,676 KiB RSS on `225bba4` to 0.13–0.15 s and about
12,000 KiB on clean `5cec800` builds.

Release Nibli `4cb02aade43b394374c40e661907ad66df3af3fe` closes the residual
composition where the queried subject's only standing proof traverses the
high-arity T3 custody chain. The remaining cause was general: rule firing built
independent candidate vectors for unbound Neo-Davidsonian events before shared
individual-role bindings could constrain them; partial dependent-Skolem
candidates rebuilt already grounded dependencies; opaque-query candidate order
did not favour the ground subject; and an exact eligible one-positive derived
antecedent could not request its complete relation cone lazily. The repair uses
deterministic left-deep event joins under accumulated bindings, grounded/index
selectivity, guarded early role binding, query-ground dependency ordering,
partial-Skolem specialisation, and fail-closed exact relation-scoped lookup. No
book predicate or definitive logical verdict was special-cased or moved.

On binary-bound 2026-08-05 measurements, `5cec800` timed out on both the composed
Zed chapter query (180.13 s, 25,792 KiB RSS) and the generated placement query
(180.11 s, 25,912 KiB). The supplied `4cb02aa` release returned Zed TRUE in a
0.87 s median at no more than 13,364 KiB and the placement entitlement TRUE in a
0.23 s median at no more than 12,868 KiB. These are dated fixtures, not a timeless
performance guarantee. An independent clean build (SHA-256 `d5d0f86a494aedd943434c2fa0abd0acbe0d7df36142d983df5774bf2dd38999`)
reproduced the two results at 0.87 s / 13,324 KiB and 0.22 s / 12,796 KiB. Its
bytes differ from the supplied binary (`33ea9c9805b899fa054b75371c60eedc9b975d4be356a45b57de0d6323071fa7`),
so this establishes source identity and behaviour, not byte-reproducible builds.
Chapter 7 now pins the Zed composition directly. Each placement row also runs a
fresh one-pin probe against its complete generated candidate: confined standing
must traverse the actual T3 facts, with no direct `person` overlay and no
extracted floor source.

`EventPath` and `RecordPath` are third-place constants in ternary `precede/3`, not
binary relation heads. The T3 chain amplified both engine failures but was not
their complete cause; opaque abstraction exposed witness expansion but was not
required for the separate eager-materialisation defect.

**Staged temporal assurance enacted 2026-08-05:**
`12-temporal-assurance.py` constructs cumulative T1, T2, and T3 sources and
executes every supplied-record case in a fresh engine process. T1 admits only
the collision-free terminal successor selected by the witnessed constitutional
lineage for adverse carry and public-power effect; T2 closes typed event and
record paths transitively and propagates type-scoped conflict; T3 rejoins exact,
independently witnessed source, window, case, lease, Court-judgment, and
injury-victim bindings. The protected-record alarm conservatively calls every
missing required carry `RecordDisappearance` because lawful record disposal is
not represented. Fresh processes are mandatory: derivation is monotonic inside
one process and does not retract an earlier conclusion when a later successor
is added. This is bounded safety evidence only. It does not authenticate
witnesses, prove a manifest complete, detect deletion before or inside the first
attested record, advance a clock, publish a successor, cause physical release,
or make Appeals act. A later operational claim can satisfy the record case only as scoped
`external_verified` evidence; it may not be relabelled as the repository-only
`current_verified` posture.

**Amendment semantics are now tested separately from amendment labels, enacted
2026-08-04.** Article 9 reads a proposer-supplied `adjust(amendment, label)` and
compares that label with the `permanent` register. It can derive a dead verdict
and suppress the otherwise-derived `become(amendment, Law)` label; it does not
inspect an exact candidate source change, verify the declared target, apply the
change, or bind the label to an effective version. Nothing reads `become`.
`approves` names the electorate, not the writer; no current rule authenticates
the tally, certificate, recount, challenge, or correction.
`10-amendment-semantics.py` executes exact bounded cases for a targetless label
beside a manually applied floor withdrawal, the same withdrawal beside falsely
harmless and honestly blocked labels, a concealed
one-token change that removes the food entitlement while the separate
anti-imprisonment firewall survives, false-target poisoning of an ordinary
reform, and a direct `admits("rich")` vocabulary widening. The harness manually
applies candidate mutations; it proves their consequences under supplied source
and facts, not proposal-to-diff causation, target truth, authorship, lawful
deployment, semantic completeness, or source-transition assurance. Direct
`admits` widening succeeds even with `Art_Evidence` placed on the candidate
register; it is source-visible and repository-reviewed but is neither an
Article 9 amendment nor constitutionally approved or entrenched. Do not repair
this by requiring an `adjust` fact or semantic-review certificate: withholding
that new premise would create a universal amendment veto while still proving no
target truth. No new constitutional rule or withholding gate was added, and
RI-12 remains `book1_target_unimplemented`.

**Placement exhaustiveness is generated and verifier-enforced, enacted
2026-08-05.** `11-placement-exhaustiveness.py` constructs the Cartesian product
of the current subject states and severity, family, and home axes from writable
premises rather than asserting `prisoner` or `severe`. Every confined row must derive `dwell`;
the exact destination is HighSec for severe cases, LowSec for non-severe family
cases, Homestay for non-severe people without family who have a home, and
deliberately absent for the no-home remainder. The audit separately mirrors
the axes for affirmative freedom and for personhood alone: the shelter debt and
entitlement remain while `fit`, `dwell`, and every destination remain absent. Its reviewed source
manifest inventories every current `fit`, `dwell`, and `building` producer and
destination, so a new route or MedSec-like constant cannot hide outside a
fixed query list. Executable source mutations create overlapping destinations,
delete the historical housing repair, remove a required destination, reverse a
route, and paint `dwell` onto every registered person; each must trip the base
contract. Every alarm-silence probe first supplies and pins a positive `put`
report, and the harmful copies still keep `err(_, Placement)` false. This is a
repository-before-merge guarantee over the current declared axes, **not** a
constitutional runtime exclusivity rule, authenticated placement act, appeal,
remedy, or free-person housing delivery. The live placement alarm still watches
only a reported ineligible Homestay placement. The deliberately housed-but-
destinationless row remains truthful, and the placement-input authority,
provenance, privacy, and challenge gaps remain owned by the future justice
interface rather than being closed by this audit.

The repo is deliberately **mixed-licence** — see `LICENSING.md` before adding files. In short: new prose is CC-BY-4.0, code is MIT OR Apache-2.0, the data registry is CC0, and everything committed before that decision (including `book.md` and `manifesto.md`) remains irrevocably CC0 under the root `LICENSE`.

## Files

- `book.md` — the entire book in a single Markdown file (~2970 lines).
- `manifesto.md` — a companion manifesto, structurally independent of the book.
- `tmp.txt` — the author's scratch notes/instructions for the section currently being drafted. Read it for context on what's in progress; don't treat it as book content.
- `TODO.md` — the **book-1** work tracker, arranged **in the order the work happens**, refreshed 2026-08-03 after all fourteen chapter passes completed (their records live in git, not the tracker). It starts with **Phase 1, author-gated decisions**, currently empty and reserved for questions that must be ruled before implementation, and **Phase 2, engine handoffs (nibli)**, currently empty and reserved for fixable engine boundaries. It then carries the merged **Constitutional expansion — implementation backlog**, which turns the ratified mandate, time target, taxonomy, coverage map, and democratic corridor into ordered work without claiming any unimplemented rule exists. Cross-cutting sections cover remaining book work, reach, data, legacy harvest, and book-2; **Standing facts and methods** closes the file with knowledge, not tasks. Delete a bullet when it fully lands; update it if only partly done. book-2's items live in `book-2/TODO.md`; don't work them while book-1 is active.
- `new-book-plans/` — planning material for book-1, plus the constitution `constitution.nibli`. `3-spine.md`'s stratification table and chapter order are **generated** — don't edit the block by hand and don't transcribe its counts elsewhere; it went stale twice that way. The generated assertion-surface, record-integrity assurance, flat-snapshot red-team, amendment-semantics, placement-exhaustiveness, and staged temporal-assurance reports are governed by reviewed sources; edit those sources and regenerate with the corresponding script, never hand-edit a report. The amendment audit applies exact bounded source mutations but does not enact them or establish source-transition assurance. The placement audit applies exact bounded source mutations but adds no runtime placement rule or delivery evidence. Refresh reviewed digests in source order: assertion ledger (7), assurance (8), red-team (9), amendment and placement (10/11), then temporal (12). Generate reports 9 and 12 before rendering report 8 because its reviewed references name both outputs; then generate/check reports 8, 10, and 11. Propagate every upstream digest before regenerating downstream artifacts. Check every generated artifact with its script's `--check` mode. Verify constitution claims with release `nibli-pin` at or after `4cb02aade43b394374c40e661907ad66df3af3fe` using `--kb`, never `nibli-host` — its wasm predates the `derived_only` and `entitled` corpus entries and silently drops the entire rights floor and every conclusion-only gate while still answering queries.
- `verify.sh` — **the one check.** The full command rebuilds `nibli-pin` unless `NIBLI_PIN` or `NIBLI_SRC` deliberately selects one, prints the engine commit when it builds from a source checkout and identifies an explicit binary path otherwise, validates every generated contract, and executes the chapter/floor pins, flat-record cases, staged temporal cases, amendment candidates, placement matrix, and source counterfactuals. `./verify.sh --quick` checks schemas, digests, generated freshness, and static guards but deliberately skips executable suites; it is not a commit gate. The suite exits non-zero on the first failure and names the claim that stopped being true. Run the full command after every constitution edit and before every commit; do not copy runtimes or suite counts here because both change with the governed sources.
- `new-book-plans/counterfactual/` — copies of the constitution, each differing in exactly one deliberate way, in three classes checked by diff shape: a line **deleted** (what the world loses), a line **changed** (`no-dead-conjuncts` — chapters 4 and 5's own pin files must pass against it, the standing proof Article 4's `~broken` and `~match(CarriedVoid)` signer checks decide nothing today), and a line **added** (`unguarded-pen` — the credential route somebody might someday write, whose pins show those kept conjuncts are all that stands between it and a matched carried-void signature counting). They exist because derivation is monotone and probe facts load *on top*, so no probe can test a restriction; these are the only way an "if we removed X" claim is executed rather than argued. **Regenerate after every constitution edit, comments included** — a fixture is a byte copy, so even a comment-only edit breaks the shape check. See the README beside them.
- `book-2/TODO.md` — book-2's seed tracker, deliberately unordered. Same channel protocol as book-1's Phase 2 when engine asks eventually arise.
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

**book-1 (the new book) — titled *The Rights Nobody Has to Earn*:**

- **The current formal floor is eight rights**, spelled `entitled(every person, event { P() })`, and its protection is a **compile-time prohibition**: a rule punishing someone for lacking a floor right is refused by the stratifier. The floor is protected *because* it is reachable — it sits inside the `prisoner` cone. This is the verified kernel, not the final social taxonomy under the 2026-08-03 mandate; any expansion still needs a completed map contract and formal proof. Do not restate the older claim that "nothing derives it, so nothing can retract it"; that had the mechanism backwards.
- **The current formal duty-bearer is a thin constitutional layer** — an agent with real taxing and inter-community equalisation power, carefully limited. Mutual covenants was rejected because the constitution has no membership concept and covenants would gate the floor on one; naming-the-gap was rejected as evasion of a solved question. The book concedes coercion plainly and states its social-democratic ends outright — the novelty is the constraint mechanism, not the absence of a provider. Under the 2026-08-03 mandate, this is not the final public-branch or remedy architecture.
- **The title is *The Rights Nobody Has to Earn*, subtitled *A design for a society worked out to the point where it catches its own failures*.** Not "utopia" — the word invites the naive-utopianism dismissal and belongs to the legacy book. **The title is chosen for legibility to a stranger, and that outranks elegance.** Two predecessors are dead and neither should be revived. *"Eight things every person is owed, and why no law can take them away"* carried two overclaims: "no law can take them away" is verified false — the refusal covers **imprisonment** and stops there, and a law voiding your credibility or docking your recognition for lacking a floor right loads fine (`08-what-you-are-owed.pins.nibli:52-57`) — and a count on a cover is the most permanent counted claim the project could make, in the one place it can never be revised chapter by chapter; the floor has already been six, then ten, then eight. *"Nothing Has to Happen First"* was accurate, survived every constraint, and failed the only test nobody had run: a stranger reads it and cannot tell what the book is about. **Test any future candidate on a reader who knows nothing, before testing it on the constraints.** Two things in the current wording are load-bearing and must not be tidied: **"nobody"**, because the universality is the thesis (`08:94`) — the same reason the dead subtitle needed "every person" rather than "you"; and **"catches its own failures"**, because "rights" is a settled noun that implies these things hold in practice and the book's second half is that they mostly do not. Drop that clause and the title overclaims. Do not restore *"and where the protection stops"* alongside "rights" — it says what "rights" already says.
- **Recognition is a bare fact and is never ranked** — not by writing a mark, not by counting entries. Decided 2026-07-30 against the proposal that verified learning mint grades for the student and outcome-conditioned perks for the teacher; all three halves are refused. **(a) Students earn nothing for being taught.** Being taught is not a contribution, the doors in `10-contribution.md:3-8` are the doors, and the constitution is **not** edited to add a student minting rule — that would commit the design to paying a child (Cira is `person` without `mature`, which is the whole of `09:43-51`). **(b) Counted degree on the reward side is refused, not merely unbuilt.** Degree needs no arithmetic here, only the same relation twice with the objects held apart — the idiom the severity rules use at `constitution.nibli:452-453` — and the cast already supplies the mirror, since Cira has two teachers. **(c) Article 3 stays unconditional**: a teacher's recognition does not depend on whether the student learned, the same shape as the auditor rule that pays for the examination and not the outcome (`10:85-87`). **State the disanalogy, never "there is no score here"** — that is verified false and its source sentence was deleted in `c0bede6`. Chapter 1 concedes a computed rating already — the paragraph opening *“Even that concedes something, and it should be said out loud rather than found later”*: severity rates an **act**, is reached through a process the accused was part of, and ends with the sentence; a grade rates a **person's capability**, with nothing adjudicated and no end. That concession is an exception the design paid for once, not a precedent. Enforced, not merely recorded — `verify.sh` section 4 checks that nothing reads `reward`, and section 4b that no rule joins `teaches` or `work` with itself; both were negative-controlled against a scratch copy. Neither is a proof: a new name for a learning record (`studies` is in the corpus, unused) routes around both, and is caught by the evidence-count gate instead, which is the only reason the pair is sufficient. **This does not block the delivery route**: teaching that delivers `learn` is a floor actuality, not recognition. Delivering learning is not grading the learner.
- **`person` is on chapter 1's evidence list**, decided 2026-07-30 and extended
  by T1 on 2026-08-05. The list had claimed to be everything the record can hold
  while omitting the entry every floor claim hangs from. “Roster membership is
  not a claim the world makes about you” was already refuted: `person` can be
  written directly, and both recorded freedom and imprisonment can derive it.
  T1 adds a supportive continuity route: an independently witnessed standing
  status in an accepted predecessor keeps deriving personhood even when its
  required successor carry is absent, and the omission becomes a named defect.
  Do not turn those routes into a hand-maintained count.
  **`derived_only("person")` remains permanently refused** because it would
  reject the ground roster itself. The remaining first-record boundary is
  external: the transition rule cannot discover someone never entered, detect
  deletion before or inside the first attested record, authenticate its
  witnesses, or make a successor arrive. Chapter 1's prose list and
  `3-spine.md`'s generated base-predicate list therefore **deliberately
  disagree**: the prose lists what may be written, while the generated figure
  lists predicates with no producing rule. The chapter's load-bearing sentence
  remains *“the **conclusions** that matter are not writable”*, narrowed from
  “things,” because personhood matters and is writable.
- **The record is closed by name — Article 0a**, adopted 2026-07-31 (nibli `850cf96`). `admits("<rel>")` refuses a ground assertion of any unadmitted relation at assert time, and an `admits` line placed below the facts is refused as coming too late, so **widening the record is a visible, reviewable edit rather than a fact somebody types**. This is what makes chapter 1's first claim — *"Not may not. Cannot."* — true: before it, `rich(Adam).` loaded and answered TRUE, because the closure was at nibli's corpus of thousands rather than at this book's own list, and only an invented word ever failed. **It is extensional only.** Rules still derive `false`, `prisoner`, `err` and `obliged`; Article 0's `derived_only` is what closes those, and the two must never be described as one guard. The admitted roster deliberately includes `person`, while the generated base-predicate figure omits relations with a producing rule. *"What counts as evidence"* and *"what may be written"* answer different questions, and reconciling those lists would be an error rather than a tidy-up. One consequence worth stating where it bites: a ground assertion through the converse alias — `obligated_by(Warden, Ruk).` — is now refused as well, because `obliged` is not admitted (verified 2026-08-01; the refusal names `admits` and the repair). The converse mechanism survives in a **rule head**, where `err($x, Placement) -> obligated_by(Review, $x)` loads and derives the inverted `obliged(Ruk, Review)` — so the chapter-14 discriminator pair still earns its keep.
- **Earning may not alter sentence duration or severity — T3 supersession,
  2026-08-03.** The 2026-07-29 intention that a convicted person could earn a
  reduction in duration or severity is retired. T3 prohibits earned-time credit,
  severity-to-duration tables, character grading, and any personal score that
  decides a person's sentence. `reward` remains unread in the current kernel and
  can never become a condition of release, sentence reduction, or freedom.
  The older coercion diagnosis remains controlling: compelled work as the price
  of liberty is convict leasing, and nominally voluntary work is pressured when
  the alternative is longer confinement. The older stratifier tests that refuse
  `prisoner($x) & reward($x) -> free($x)` remain useful regression evidence, not
  a reason to invent a workaround.
- **Confinement houses you**, decided 2026-07-31 (v0.8). The combination *not severe / no family / no home* derived no placement at all — eligible for home confinement with no home to be confined in — and Adam and Kel stood in it. The rule is `prisoner($x) & fit($x, Homestay) & ~home($x) -> dwell($x)`, and it is **consistency, not new policy**: the design already held that the state houses whom it confines (`:460`, `:472`); this was the case those rules missed. **Do not restate it as "assume everybody has a home."** `home/1` is a fact the world reports, asserting it for everyone writes something that may be false, and closing the delivery gap by fiat is verified to *silence the isolation marker in the same edit* — the instrument that would have noticed goes quiet. **The framing that must survive**: this closes a *placement* gap and the *delivery* gap is exactly as wide, because the person was owed a home before the conviction and nothing delivered it. Chapters 11 and 13 say the criminal conviction is what housed Adam and Kel, for precisely as long as it punished them — neither is decoration; those lines stop this reading as a floor that works. Chapter 8's shelter sentence is now the rule — **"shelter derives for every confined person and for nobody else"** — which is this file's own canonical example of a good rule-statement and was false until this landed. Oversight of the duty-bearer (enablers, their checkers, a meta-study) was raised and **parked to book-2** under the former scope. **Superseded in scope 2026-08-03:** Book 1 now owns the constitutional mandate, independence, evidence, and remedy path for oversight; Book 2 retains inspection practice, staffing, and operating systems.
- **The audit feeds an obligation**, decided 2026-07-31 (v0.8), Article 8b. Chapter 14 used to argue the audit's powerlessness was **structural** — a pure observer, therefore nothing can follow. That was false and it was the comfortable kind of false: it turned a decision into a law of nature. `err($x, Placement) -> obliged(Review, $x)` and the `Isolation` twin both load and derive. **Spell it `obliged`.** The accidental route closed upstream on 2026-07-31 (nibli `e70f22f` renamed the converse alias `obligated` to `obligated_by`), so writing `obligated(...)` is now a compile error rather than a silently inverted fact — that was the realistic typo and it can no longer be made. **The mechanism is narrowed, not closed, and this repo narrowed it further by accident.** After the rename `obligated_by(Warden, Ruk)` still compiles to `obliged(Ruk, Warden)` — but re-measured 2026-08-01 against *this* constitution that ground assertion is now **refused**, because Article 0a closed the base vocabulary and `obliged` is not admitted. `admits` is extensional, so the converse survives in a **rule head**: `err($x, Placement) -> obligated_by(Review, $x)` loads and derives the inverted fact. Two things follow — the realistic forgery route is gone here, and the chapter-14 discriminator still earns its keep against a slip in a rule head. So the discriminating pin pair in the chapter-14 suite — `obliged(Review, Ruk)` TRUE **and** `obliged(Ruk, Review)` FALSE — is no longer the *only* defence, but it is still the only thing catching an argument-order slip within `obliged` itself. Keep both halves. **One constraint this puts on the method part**: nibli has a filed defect — its tracker bullet **"`obliged`-spelled every-duty renders the wrong obligated party"** — where the deontic collapse picks the event variable as duty-holder when back-translating the **base** spelling, which is ours; the converted `obligated_by` spelling binds correctly. Cited by title deliberately, not by line: this is the same file whose line numbers rotted twice inside one exchange. It cannot reach readers today because this repo runs `nibli-pin` only and never renders prose, but the method part exists to show readers the machinery, so if it ever prints a rendered sentence or a proof trace, check that party before it ships. **Two rules, not one**: the general form `err($x, $k) -> obliged(Review, $x)` loads and derives **nothing**, because a body-only variable does not bind over a derived relation on this engine — the same limitation the Article 4 note records. **This is not teeth.** Nothing reads `obliged`, so it is a second inert obligation beside Article 1b's `owe`, and `verify.sh` guards that: `err` left the absence loop and `obliged` took its place. The chapter must keep saying the chain merely ends one step later — the breach of the duty is *also* markable (`obliged & ~capture -> err($x, Duty)` is accepted and derives, pinned as the chapter's closing exhibit), so what runs out is not links but anybody who has to act.
- **The debt is itemised, and INVARIANT 1 was rewritten because it was broken**, both 2026-07-31 (v0.8). Article 1b now carries eight `owe(State, K, $x)` rules beside the surviving `Provision` token, which is kept because it is pinned in four other files. **Enumeration cost eight rules and no vocabulary** — the evidence list counts *predicates* and the generator never looks inside the parentheses, so a constant is free; the tracker had priced this as "eight new constants in the evidence vocabulary" and that was a category error. Verified: the firewall extends to each named debt (`~owe(State, Eats, $x) -> prisoner` is refused). **The constants are not joined to the predicates**: `Eats` and `eats` are unrelated and must never be "wired up" — the names match so the resemblance is visible, and chapter 8 turns on the gap. **INVARIANT 1 no longer says "no floor predicate in any rule body"** — that was false from v0.1, because Article 6's isolation marker reads `~meets`, and nothing checked it. It now reads: **a floor right may be read only into `err` — noticed, never acted on.** The stratifier does not enforce this; it refuses `~eats -> prisoner` as a negative cycle and accepts `~eats -> reward` or `~eats -> building` happily, so `verify.sh` guards it (negative-controlled). **Do not describe the delivery gap as something the design cannot detect** — verified, `owe(State, Eats, $x) & ~eats($x) -> err($x, Undelivered)` is accepted and derives, and the design already ships that shape for company and for none of the other seven. That asymmetry was discovered, then ruled: the markers are refused while the record holds no arrival facts — see the delivery-markers entry.
- **A control puts the base back; a premise does not**, settled 2026-08-01 with nibli
  `425567b`. `:accept` leaves its statement in the knowledge base, so every pin below one
  ran against a widened base — and that produced a real vacuous green here: with the
  complement controls loaded, `? prisoner(Adam).` passed against a constitution with
  **Article 6's conviction rule deleted outright** (re-measured 2026-08-01; silent under
  `:accept`, caught under `:accept-scoped`). **Write controls `:accept-scoped`.** The
  exceptions are allowlisted in `verify.sh` section 4d — do not re-derive the list here, it
  has grown twice; the script is the list — and the test for joining it is always the same:
  the accepted statement is a **premise the file goes on to query**, not a control. Chapter 1
  accepts a roster entry and asks what it derived; chapter 14 accepts the duty-breach rule and
  asks what it marks; chapter 5 accepts the void rule minus distinctness and asks what flips;
  chapter 9 accepts the disenfranchisement clause and asks what it failed to take. Scoping any
  of these makes its query meaningless — verified per file as each joined.
  The old workaround was "order the file so its controls come last", which is a rule
  nobody can see being broken; do not restore it, and do not delete the *history* those
  ordering comments recorded when deleting the *instruction*. **`derived_only` and
  `admits` cannot be scoped at all** — they survive the retraction by design, and asking
  is a harness error rather than a silent no-op.
  **This suite depends on `nibli-pin` giving each pin file a fresh engine, and that
  dependency is load-bearing rather than incidental.** `verify.sh` passes every file in one
  invocation; re-verified 2026-08-01 that a ground fact *and* an unscoped `:accept` in one
  file are both invisible to the next. It is the only reason chapter 8's widening — which
  was live, not latent: `lose(Points, Hano)` derived at the point the old ordering comment
  declared everything below sound — stopped at the file boundary instead of reaching the
  rest of the suite. If that isolation ever changes upstream, this suite's containment
  goes with it and every ordering assumption in every pin file has to be re-examined.

- **Provenance on `reward` is refused, and not because of the clawback fork**, decided
  2026-08-01. The proposal is to give `reward` a second place recording what the recognition
  was minted *for*, so a clawback could reach only what came from a fraud. **It keeps looking
  cheap, and that is why it needs a written refusal**: all three minting rules already bind the
  source and throw it away at the head — `$student`, `$task`, `$audited` — so the argument is
  sitting there unused and costs no new vocabulary. Refused on five grounds, and **each holds
  whichever way the Article 4 clawback fork is ruled**, so this does not reopen when that lands.
  **(a)** `verify.sh` section 4 holds that nothing reads `reward`, by decision — and an arity-2
  `reward` exists only to be read; verified, the narrower rule `reward($t,$s) & false($t) ->
  lose(Points,$t)` loads and the absence guard catches it. **(b)** Section 4b forbids joining
  `teaches`/`work` with itself, and a second place puts counted degree one rule away.
  **(c)** There is nothing at the other end to narrow *from*: `lose` is a **leaf** —
  no rule body reads it, derivation is monotone, so nothing is ever actually taken from anybody,
  and the apparent clawback in the shipped cast is entirely the `~false` guards on the
  minting rules — all three doors since v0.9 — **never minting**. Do **not** restate this as "`lose` has no slot for it" — that was the first
  draft of this bullet and it is false, cheaply refuted: nibli gives `lose` (gismu `cirko`) a
  third place, `conditions`, and `lose(Points, $s, $t)` loads. **(d)** The corpus entry will not carry it — `reward` is gismu `cnemu`,
  arity 4, places `["subject","rewards","atypical","reward"]`, `Generic` tier with places never
  hand-verified; the natural `reward($teacher,$student)` puts the student in the *party rewarded*
  slot, not the deed slot. That is the ground `deserve`/`jerna` was rejected on. **(e)** Measured
  2026-08-01: all three heads at arity 2 take `rights-floor.pins.nibli` from **15.07 s to
  337.50 s**. **Chapter 6 already rules this way and needs no change** — *"The design's answer to
  that tension is not to sharpen the instrument. It is to put a hard ceiling on it"* (`06:107`),
  and `06:81-85` says whoever writes the narrower rule "will find they have written a repeal".
  **Enforced by `verify.sh` section 4a, because nothing else can see it arrive.** Three TRUE pins
  (`reward(Esa/Quin/Gia)`) catch a *rewrite* of the heads, but **five** other `reward` pins go
  vacuous in that same edit — three more in chapter 10 plus `reward(Cira)` in `06-clawback` and
  `reward(Dev)` in `rights-floor` — because `reward/1` stops existing and a FALSE pin against a
  vanished relation still reads FALSE. Worse, the **additive** shape is invisible to everything:
  a fourth head at arity 2 added *beside* the three leaves `reward/1` deriving, so the absence
  guard and the whole pin suite stay green — verified. Section 4a also asserts `reward` is still
  mentioned at all, since "nothing reads `reward`" passes just as cleanly against a relation that
  has been renamed away.

- **Article 4's `~broken`/`~match(CarriedVoid)` signer checks stay, and are not dead code**, decided
  2026-08-01. No assignment can fail them today — every Review/Tribunal pen derives through
  Article 8's rules, which read both guards themselves, and `derived_only("permits")` closes the
  assertion route — but they were **live guards when v0.2 wrote them**, against sock-puppet
  credentials with a prior voiding. The raw `rotten` input is now inert by itself; the guard
  reads only an exactly witnessed void carried into the designated current record. The v0.3
  credential closure demoted the signer checks without anyone deciding to. They re-arm the
  moment any pen route omits the guards: measured, with one
  unguarded route added, `false(Tyr)` stays FALSE with them and flips TRUE without them — a
  carried-void signature counting. Both halves are **permanent fixtures**, not commit-body
  prose: `no-dead-conjuncts` (chapters 4 and 5's own pin files pass against the stripped copy —
  the subsumption) and `unguarded-pen` (the postulated future where the conjuncts are the
  deciding check). Same idiom as the rule's own `~($a = $b)`, kept for the day the assumption
  that hides it stops holding. **Do not delete them as dead code** — that proposal has now been
  made once, by the pass that produced this ruling — and note the reading consequence: chapter
  5's matched-history pins land on the *missing credential*, not on these conjuncts, and the prose
  ("that matched history blocks the credential") is correct about that.

- **The Esa passage tells the truth about Koa, and nobody seats him**, decided 2026-08-01.
  Chapter 5 claimed Koa *"examined Esa"* with *"the credential"*; the record holds a personhood
  entry and one `capture` fact — no judging, no seat, no pen — and both false clauses are now
  pinned FALSE in chapter 5's suite. The tracker's alternative repair, seating Koa on both
  bodies as the count-isolating fixture, is **refused**: chapter 2 pins `authority(Koa)` as its
  no-standing exhibit (*"two facts in the whole constitution, no seat, no office"*) and chapter
  1's *"documented something"* rests on the same two facts, so that route falsifies two chapters
  to repair one. The count isolation lives in a **pin-file fixture** instead: Ambi, a fresh
  person seated by both bodies who judges and records — every act the rule asks of either
  signer — and cannot void alone, with the closing exhibit (the void rule minus distinctness,
  accepted; `false(Solo)` flips TRUE) proving distinctness was the only bar. That fixture is
  also the liveness proof for the `~($a = $b)` conjunct Article 4's header keeps *"for the day
  one person holds both pens."* Chapter 5's pin file joined `verify.sh` section 4d's
  allowlist for that closing exhibit — chapter 14's shape (the section's positive control
  counts the allowlisted files; it moves whenever the list does). The section headline reads: the rule does not count signatures, it counts
  signers.

- **Care walks through two existing doors, and chapter 10 says so**, decided 2026-08-02,
  answering the one point in `reviews/ai_review.md` the book had no reply to. The teaching half
  of raising a child mints through door one — a parent who teaches is a teacher, the record
  never asks the relationship, and the pair that voids a *judge* (Article 5) disqualifies no
  teacher. The tending half mints through the work door — nothing narrows what counts as work
  to the salaried or the public, and the task constant is free vocabulary. **Do not add a
  fourth door, a care predicate, or any ranking** — the review's maximal ask ("highest-status,
  most heavily subsidized") stays refused under recognition-is-never-ranked. The exhibit is a
  **pin-file caregiver pair** (chapter 10's suite; fresh names, one route each so each door is
  isolated), deliberately not a cast member: the shipped record holds no care entry, and the
  chapter's claim is calibrated to that — *"the doors are open to it"*, never *"the society
  sees it"*, with the entry-has-to-be-written limit stated in the same breath. Found while
  ruling: **neither door carries a maturity test** — a child
  who works or teaches mints today (both verified), beside a design that refused student
  minting partly as paying a child. That question was ruled the same day — see the next
  entry ("The doors carry no age test, and that is defended, not confessed").

- **The doors carry no age test, and that is defended, not confessed**, decided 2026-08-02.
  A child who works or teaches mints recognition today — verified both ways, and chapter 10's
  care coda now says so in the open, on Cira: the child the design will not grade is recognised
  the moment she contributes. **The maturity guard was measured before being refused**: with
  `mature` conjuncts on the teaching and work doors, four of the five recognised people go dark
  (`reward(Esa/Quin/Nima/Sata)` all flip), because the record barely holds `mature` and none of
  the recognised have it — so the guard's real meaning is *your work counts only once somebody
  files your adulthood*, a written entry upstream of esteem, the same shape the old earned-time
  proposal used, and it shuts the care doors for a young carer in the same edit. **Do not add a
  maturity conjunct to any door as cleanup.** The disanalogy with the grades ruling is the
  argument, stated as a pair in the coda: being taught is not a contribution, at any age;
  contributing is, at any age. The exploitation reading is answered by the design's own shape —
  recognition cannot pay, and what makes a child's work worth exploiting is the wage. Exhibits
  in chapter 10's suite: the work door isolated on Cira (her not-mature status pinned first),
  the teaching door isolated by file order on Pico, whose `reward` FALSE while tended flips TRUE
  two verdicts later when he teaches. Prose stays in the conditional voice — the shipped record
  holds no child work entry, and chapter 6's *"Cira earned nothing"* stays true.

- **The third door closes on voiding — enacted, not disclosed**, decided 2026-08-02,
  resolving the chapter-10 fork (v0.9). Article 4's examiner rule now carries
  `~false($auditor)` beside `~deceive`/`~broken`, the guard the teaching and work doors
  already had, so chapter 10's "all three doors close for the same reason" is true as
  printed. The disclosure branch — keep the rule and print that a voided person can still
  earn by examining people — was refused as a contradiction rather than a mere cost: an
  examination is nothing but its author's word, voiding is the finding that the word is
  worthless, and Vex — carried-void, therefore penless — was being paid for examinations
  the same voiding made incapable of counting toward anything. Enactment is the
  confinement ruling's shape: consistency with the design's stated intent, not new policy.
  Measured before landing: `reward(Vex)` TRUE→FALSE, `reward(Gia/Esa/Quin)` unchanged,
  every pin suite green against the guarded copy, rights-floor runtime unchanged (~15 s).
  **What it does not do**: nothing un-mints — `lose` stays a leaf and derivation stays
  monotone; the guard never-mints, chapter 6's register. **Two things it exposed, recorded
  where they bite**: the chapter's worked reasons needed correcting anyway — Lupo's door
  shuts twice over (per-pair `~deceive` for the lie itself, then the void) and Dev never
  documented anybody, so his "nothing at all" is carried by the void alone — and the third
  door still pays a person in good standing for a bare `judge`+`capture` pair with no
  credential and no grounds (measured post-guard: a fresh clean person mints from the two
  writes), which is the `capture`-precondition bullet's territory, not this ruling's.
  Exhibits pinned in chapter 10's suite: the Vex pair, and the closing forced-Bela probe
  (a voided person examines; the mint refuses; the clawback registers) —
  negative-controlled, exactly those two `reward` pins flip against the pre-guard
  constitution.

- **The floor-delivery markers are refused while the record holds no arrival facts**, ruled
  2026-08-02, closing the largest restored Phase-1 decision. Measured before ruling: the
  Undelivered rule loads and derives — and fires on the voided, the confined-and-housed, and
  the never-accused alike, because `eats` is asserted for nobody and `~eats` is true of every
  person alive. A marker that fires on everyone discriminates nobody; chapter 11's own alarm
  standard applies. **The asymmetry is chosen now**: the two existing markers audit the
  design's own act — Isolation is prisoner-scoped, Placement audits placement — and chapter 8
  says so in print ("watches what it does, and does not yet watch what it owes"). The
  `undelivered-marker` fixture holds the measurement permanently and is where the marker
  design starts when book-2's delivery layer generates arrival facts — the ruling expires
  with its premise. **Two economics facts recorded so cost never decides this again**: the
  general `err($x,$k) -> obliged(·,$x)` form NOW DERIVES (the per-kind cost-doubling that
  shaped the original bullet is dead; Article 8b keeps its two constant-named rules
  deliberately — correct, pinned, not worth the churn), and Article 0a charges nothing for a
  derived head. Do not build a floor-delivery marker into this constitution without arrival
  facts, and do not re-price the decision on rule-count.

- **The design does not say how long — ruled 2026-08-02; superseded in scope by
  T3 on 2026-08-03 and implemented narrowly on 2026-08-05.** Ordinary duration
  vocabulary remains outside the record (measured: `year(Term, Two).` and
  `earlier(Custody, Release).` are both refused), but the constitution now admits
  the bounded inputs needed for witnessed record replacement, order, and a
  case-bound custody review. The implemented T3 rule says whether the supplied
  fresh evaluation carries current reviewed authority. A witnessed passport
  selects one constitutional lineage, and only its collision-free terminal
  successor can supply current adverse carry or public power. Typed event and
  record paths close transitively; a direct or longer cycle taints the connected
  path and cannot support a review window. The custody gate rejoins independently
  witnessed case-subject, Court-holder, Court-judgment, injury-victim, lease,
  window, renewal, and source fields; conflicts are explicitly rejected for the
  source, window, case-subject, and lease bindings. It does not count days, establish a
  maximum measured sentence, or prove the outside service advances. Chapter 13's
  closing pins preserve that distinction. **Release stays an act, not an expiry**:
  missing, stale, disputed, or incompletely witnessed authority prevents custody
  from deriving but never manufactures `free`. Compact status tags cannot lend
  their authority to another raw tuple sharing the same identifier: consequential
  consumers rejoin the exact fields and matching witnesses, and the temporal
  harness attacks that aliasing directly. Because the engine is monotonic within
  one process, later facts do not retract already-derived authority; every
  current-effect case runs in a fresh process. Book 2 retains clocks, calendars,
  scheduling, availability, publication, recovery, and operational time
  administration. The superseded earning-shortens ruling is not a deferred
  permission: nothing measures duration, nothing reads `reward`, and no temporal
  premise may price a person. One harness nuance
  recorded in the pin file: `admits` for a *fresh* name loads
  from a probe (too-late guards only relations with prior facts), so refusal pins guard the
  shipped text and a probe may always widen on top.

- **The shield's exposure surface is unbounded, refused as composed**, ruled 2026-08-02,
  closing chapter 4's own open question. Every candidate bound dies on a prior ruling, and the
  settled entry names them so nobody re-proposes one at a time: a **time** bound is not part
  of the implemented custody-only T3 family and would require its own power-specific contract,
  rather than an individual exception; an **epoch-recency fact** is an unadjudicated
  shield-stripping write — one fact retires a target from everyone's shield surface, the
  finding-with-no-finder class chapter 1 conceded, handed to whoever writes it; **lapsing or
  re-certifying standing** revokes it, and Rebel's shield surviving Boss's recall (chapter 2's
  thesis, pinned three files over) is the standing refutation. Beneath all three, **the shield
  remains non-temporal**: T2 can represent a separately witnessed sequence, but no shield rule
  reads it, and within an unordered snapshot exposed-then-recalled and recalled-then-exposed
  remain indistinguishable. The
  reach-back is pinned in chapter 4's suite (Zeno: convicted, one `show` naming the recalled
  Boss, conviction blocked — negative-controlled on the single write). **Do not bound the
  surface by any route**; the growing list stays priced in chapter 4's costs section, and
  whoever proposes the bound again must say which of the three protections they trade for it —
  that sentence is in print and is the chapter's answer to the delay-gaming objection, which
  Part V's capture joint defends rather than dissolves.

- **The temporary-assessment exclusion is priced as an exile, not defended as an absence**,
  ruled 2026-08-02 — Part V, capture joint, verdict "Survives, narrowed." The design does not
  abolish capacity, risk or crisis assessments; it refuses them entry to the one record that
  reaches standing, liberty and the floor. **The firewall is the claim** — a hospital chart
  can inform care and can never void you — and **the exile is the price, stated in full**:
  assessments pushed outside live in records this design does not police, and power migrates
  toward whatever record matters. The lesser-harm defense: inside this record an assessment
  sits upstream of liberty forever; outside it, its harm is bounded by what the record
  refuses to hear. **The episode-fact route is refused for book-1, composed — do not
  re-propose an assessment entry, episode-scoped or otherwise**: it is a new admitted name
  (chapter 1's list and the twenty-four move), a finding-with-no-finder (the class chapter 1
  conceded), and it faces the inert-or-dangerous dilemma — read by nothing it is a third
  pretending instrument (refused at the markers and at duration), read by anything it is an
  assessment feeding consequences. The standing exhibit is already pinned (`dangerous(Adam).`
  refused, chapter 1's suite). Part V owns the argument; book-2 owns the one-way firewalled
  operational layer, filed there.

- **No record-person gets an inner life, and the flatness is evidence, not a defect**, ruled
  2026-08-02. Five of six reviewers asked for emotional register, an external antagonist, and
  characterisation of the named cast; the ruling holds the line the book's own thesis draws —
  the people in it are exactly the facts recorded about them, and inventing Bela's fear or
  Cira's confusion would fabricate the kind of entry the record refuses to hold. **Do not warm
  the cast in any pass, any part, ever**, and do not read the flatness as awaiting repair:
  Part V states the restraint once as chosen and cites the five-of-six as evidence that a
  reader who felt it has felt the design. Part V's approved register channels, each with its
  guard: the **author's first person** (supplied at the Voice ruling, not ghost-written); one
  **second-person domestic vignette** — a household through food, care, housing and crisis,
  generic "you", never a cast name; the **hostile reviewer corpus as the antagonist**, quoted
  from `reviews/` and answered at the joints; and the **nine historical cases as the
  documented feeling**. Nothing else — no invented antagonist, no composite citizens, no
  dramatised cast scenes.

- **The voice boundary is the derivation boundary**, ruled 2026-08-02. The plain, direct,
  reader-facing register of the fourteen derived chapters is ratified as their voice — it is a
  voice, and the texture ruling cites its restraint as the thesis performed. The author's
  first person enters at exactly the three elements the derivation gate already exempts: the
  opening note, Part V, and the method part. **The seam is audible and deliberate** — a reader
  can hear the crossing from what the machine derived to where the author argues — so **do not
  warm the derived chapters and do not flatten the exempt three**; either direction erases a
  boundary that is doing epistemic work. **Supply protocol**: the first person is
  author-drafted — sessions edit mechanics only (guards, citations, wrapping, the ratchet) and
  never generate or extend the voice; ghost-writing stays refused, per the constitution's own
  register note, which stands as written. `tmp.txt` is the channel for drafts in progress.
  **All three exempt elements were session-drafted by the author's explicit instruction,
  each a recorded exception (2026-08-03).** The opening note: "You draft it yourself",
  reviewed in `tmp.txt`, adopted with no changes ("I have no changes to suggest"). Part V:
  "Same for Part V — draft it yourself, commit and push" — adversarially verified against
  the reviews corpus, the registry and the chapters before landing (three checkers; two
  misattributions and two overclaims caught and fixed pre-commit). The method part: ruled
  session-drafted in the planning session for its landing (AskUserQuestion, the same
  explicit-override basis), adversarially verified the same way. This line is the record of
  all three. The ghost-writing refusal stands for any future first-person writing — the
  launch essay and the epigraph translation remain the author's — unless the author rules
  again. The
  full re-weave the tracker once priced (every chapter re-touched, dearer each week) is dead
  by this ruling, not deferred.

- **The method part's scope is sealed — `book-1/method.md`, landed 2026-08-03.** Five
  decisions, each load-bearing: **(a) the filename is unnumbered and must never be
  renumbered** — verify.sh's jargon and counted-claims gates glob `book-1/[0-9]*.md`, and
  the file quotes the stratifier error verbatim, so a numbered name fails the build
  instantly; the epigraph is the precedent and `book-1/README.md` records the convention.
  **(b) No pin file** — non-derived elements are unpinned (Part V's precedent), and a new
  `*.pins.nibli` would enter the suite and break the `:expect-pins` reconciliation. **(c) No
  machine-rendered English and no proof traces, ever** — rules as written, error messages as
  printed, pin verdicts only; this is stated in the part's own reading contract and is what
  keeps nibli's still-open renderer defect (its tracker bullet **"`obliged`-spelled
  every-duty renders the wrong obligated party"**, cited by title, never by line) dormant.
  Adding a rendered example "for friendliness" arms it. **(d) Excerpts + pointer, never the
  full KR inline** — the part owns the resolution in print (the repository is the appendix);
  reproducing the constitution or the spine's generated table creates the documented
  staleness failure mode. **(e) The compute backend is not discussed** — if any future edit
  adds it, cite nibli README's "Trust boundary" callout by heading. The part's quoted error
  messages were reproduced against the built engine on landing day; the stress-surface
  paragraph's upstream inventory names artifact classes, never counts, because upstream
  counts rot. book-1 references book-2 exactly once, in this file's closing lines — do not
  add a second reference anywhere.

- **The reach strategy: public construction from a home of its own**, ruled
  2026-08-02 and qualified by E2 + P1 + D2 on 2026-08-04. The dedicated domain,
  platform syndication, public red team, and assembled-book capstone survive.
  The original instruction to serialize the pass-complete pre-expansion manuscript
  does not: E2 leaves that manuscript as public source and git history without a
  promoted edition. P1 replaces that immediate route with immutable, tagged
  expansion snapshots after their full gates; they are previews, not final
  spine-order serialization. Once the expanded constitution and spine freeze,
  the First-Edition release candidate serializes in computed order **as each
  whole-chapter pass completes against that exact candidate**; the assembled
  digital book is the capstone, and D2 makes that completed expansion the first
  print-on-demand edition. Building in public still performs the thesis: repo
  history is the method's proof, previews recruit the outside red team, and
  defect pins make known flaws declared features. Four companions remain: the
  launch essay (*The Furnished Prison* the standing headline candidate; inside
  the voice boundary — author-drafted), the method paper (formal-methods-for-law
  genre; cites the book, never the reverse dependency), run-it-yourself as a
  front-page claim once the exact nibli dependency is reproducible (`verify.sh`
  is the core artifact, not yet a one-repo reproduction), and the D2 physical
  edition whose lever is quality, not exclusivity. **The dilution guard from the
  adoption reviews rides along: reach adapts the packaging, never the design** —
  an audience that needs a different design is book-2's reader, not book-1's.

- **The student clawback is deleted, and `lose` stays a leaf**, ruled 2026-08-02 — the
  Article 4 clawback fork, decided as Branch A. The rule `teaches($t,$s) & false($t) ->
  lose(Points, $s)` recorded a loss against a student for a teacher's fraud — negative
  scoring of a person who did nothing — and is deleted outright; the wrongdoer rule
  `false($f) -> lose(Points, $f)` **stays**. Deletion, not narrowing, because the middle
  options were closed before the fork was ruled: students never mint (the grades ruling),
  so "claw back only recognition derived from the fraudulent teaching" had an empty
  target — narrowing was always repeal — and the wrongdoer-side narrowing needs
  provenance on `reward`, which is refused. **Legacy bright line 2 narrows with the
  ruling**: book-1's form is *"no subtraction except by due process for one's own
  adjudicated fraud"*, which the surviving rule satisfies; do not restate the unnarrowed
  "no negative scoring of persons" as book-1 doctrine. **The `lose`-reader half is ruled
  closed with it**: the leaf stays — the loss is recorded and read by nothing, chapter
  14's determination-then-stop register — and the measured-to-load consumer
  `all $x: lose(Points, $x) -> err($x, Recognition).` is **refused**, not merely
  unbuilt; do not re-propose it as a small rule. The Cira pin flipped its declared
  `:defect` to a plain FALSE, chapter 6's middle section tells the deletion as history
  (the repaired-defect register of the alarm and third-door repairs), and the exhibits
  that survive are `reward(Cira)` FALSE and `person(Fin)` FALSE — the student who earned
  nothing and the student who was never on the roster.

- **The Articles 6/7 polarity asymmetry is defended, not repaired**, ruled 2026-08-02 —
  the polarity contradiction, resolved as a chosen asymmetry. The shield stays
  fail-open (absence of a deceit finding protects; chapter 4's priced choice) and the
  conviction rule stays fail-closed (absence of granted relief convicts), because **the
  two absences differ in kind**: the shield's absent finding is an *accusation not yet
  adjudicated* — nobody is treated as a liar on no one's finding — while relief's
  absent finding is a *remedy not yet performed*, and a remedy present by default is
  not a remedy: read `~permits(Appeals, ·)` fail-open and no conviction ever derives,
  handing whoever declines to adjudicate a veto over every conviction. Both defaults
  give the benefit of absence to what the guarded machinery already concluded, against
  the same enemy — the captured or idle adjudicator. The defense is in print three
  ways: Article 6's head note, the severity note's re-dating (the "unexplained…still
  unresolved" sentence is gone the honest way), and chapter 3's default paragraph in
  "The other pen", pinned by the either-alone pair — the bare clear flag (Adam) and
  the bare appeals judgment (Voss) each leave the conviction standing while Nia's
  both-together block lifts it. The cost is stated, not hidden: a person whose case
  nobody takes up stays held, the mirror of chapter 4's window, weighed the same way.
  **The alternatives are refused as composed — do not re-propose either**:
  review-standing derived from `prisoner` and read under negation by the conviction
  rule is the measured stratifier cycle (Article 7's own landmine), and "pending"
  framing collides with chapter 5's "Not provisionally, not pending anything"
  because the relief pair itself remains case-unbound and unordered; an
  affirmative exhaustion fact is a new admitted name in the
  finding-with-no-finder class whose *withheld* entry blocks every conviction — one
  word upstream of liberty, pointed the other way.

- **The vocabulary batch — five rulings, one sitting**, 2026-08-02, landed as four
  constitution commits (`b51781f` kinship, `6c68306` forgive, `fc51b75` cite, `4231547`
  hears; evidence vocabulary 24 → 29, admits 25 → 30). Each ruling names its refused
  wider form so nothing trickles back. **(1) Kinship**: `married` (speni) and `sibling`
  (tunba) joined Article 4's independence check in both directions, beside `~parent` —
  dead guards, since the cast records no marriage or siblinghood; the gendered pair
  (`brother`/`sister`) was skipped so the record carries no axis it does not need, and
  **Article 5's judge-your-child rule was deliberately not extended**. Chapter 5 keeps
  the residue: closeness the record has no words for still co-signs. **(2) Expungement,
  mark only**: `forgive(Appeals, $x)` beside `judge(Appeals, $x)` derives `clean($x)`
  (a new `derived_only` — hold it apart from the asserted `clear`), and the effective
  witnessed carry became `match(CarriedVoid) & ~clean -> false`. The raw
  `rotten` report remains an input but is inert alone. Two writes, never one —
  the clear-guard shape.
  Word restored, clawback stops, earning doors reopen, and the measured retroactive consequence
  is told in print: a forgiven examiner's recorded past examinations start paying.
  **The pen-return form (four sites) was refused**: credential rules and the multi-sig's
  signer checks still read the mark itself, which stays on the record — forgiven, not
  erased; the way back for the person and the way back to power are different roads.
  **(3) Grounds, the paid door only**: `cite($auditor, $ground, $audited)` (sitna) is a
  condition on the examiner-reward rule — the bare pair that minted for a fresh clean
  person now earns nothing (the Yano exhibit, ch10) — with the limit stated where the
  guard is: any word fills the slot, so the record buys an author for the why, not its
  truth. **The void's own grounds stay deliberately unasked** — Article 4's multi-sig is
  untouched and chapter 5's who-never-why stays the open question, now narrowed to
  where it matters most. **(4) Delivery**: `teaches($t,$s) & hears($s,$t) -> learn($s)`
  — the first route to a floor actuality that does not run through a prison. `hears`
  (tirna) is a two-sided arrival record rating nobody; the entitlement stays
  unconditional; the route ships **dormant** (no cast arrival — the placement-marker
  posture, pinned live in ch8), and **cast exercise was declined**: Cira's hearing is a
  probe, not a shipped fact, so chapter 8's no-litany and chapter 13's sting stand.
  The grades ruling is untouched in both directions — being taught still mints nothing,
  and the rule joins `teaches` with `hears`, never with itself. **(5) Governance
  vocabulary — superseded in scope 2026-08-03**: the former ruling deferred community,
  transfer, tax, and term-of-office vocabulary to Book 2 because the present constitution
  cannot state portability, justice, or a complete public architecture. The ratified
  mandate now permits the constitutional vocabulary and interfaces those domains require.
  Add them as completed, mapped constitutional rule families—not one predicate at a
  time—and retain operational finance, administration, and infrastructure in Book 2.

- **The learning route was book-1's whole delivery story**, ruled 2026-08-02, and is
  **superseded in scope 2026-08-03**. `teaches` + `hears` -> `learn` remains the
  valid demonstration: two-sided arrival evidence upstream of a floor actuality,
  without ranking the learner. The expanded mandate now permits generic constitutional
  delivery, receipt, breach, interim-continuity, remedy, and review interfaces for every
  floor. A provider's self-authored assertion cannot alone count as receipt or delivery,
  and no floor may become conditional. Meal logistics, care workflow, facilities,
  staffing, procurement, capacity, and all other operating machinery remain Book 2.
  **Its shape was ruled on 2026-08-03:** the legacy route is not a generic delivery
  template—`hears` is audio-literal and uncontrolled, while `learn` is a personal
  outcome rather than neutral receipt. Future delivery families must use
  accessibility-neutral, recipient-side access/receipt evidence with a named
  authorised writer and challenge route; they may secure conditions but may not
  certify learning, health, belief, or another compelled personal state. This is
  a Phase-2 interface requirement, not a new current formal route.

- **book-1 opens with one epigraph, and the poem's full text lives in git**, ruled
  2026-08-02. `book-1/epigraph.md` (unnumbered, so the chapter gates do not sweep it)
  carries stanza 4 of Bharati's *Yoga Siddhi* with the author's own translation ported
  verbatim from `book.md`'s appendix — the stanza whose subject, the daily search for a
  meal, is the condition the floor abolishes, closing on "Did you think I, too, would
  yield?". At most one, never structure, one sentence on who Bharati was — the settled
  constraints, all honored. **The translation is the author's voice**: whether to
  replace the rhymed rendering with a plainer one is theirs alone; sessions never
  redraft it. The full two-stanza text and both translations stay in git history when
  `book.md` is deleted, recorded in the deletion manifest as consciously kept there;
  the registry entry `bharati-yoga-siddhi` is the standing pointer.

- **The democracy/happiness analysis stands on V-Dem, re-derived**, ruled 2026-08-02 —
  the data-licensing fork, closed. EIU's index is non-redistributable and the registry
  is CC0, so EIU-derived values never enter it; cite-and-link was refused because Part
  V's worked example is the method performed and must be re-runnable by a stranger.
  The re-derivation is real work, priced in the Data section: V-Dem's Regimes of the
  World categories are not EIU's four, so the regime table and step sizes are
  re-derived and may shift — which the example's own discipline (test the claim you
  would love, report what survives) absorbs by design. The EIU registry entry stays
  source-reference-only, available for book-2 to cite-and-link.

- **Two severity refusals, both on lexical/structural grounds rather than taste.** **Directness is refused**: the committed corpus has exactly five relations with a `victim` place — `attack`, `bad`, `cruel`, `dangerous`, `injure` — and none means "directly"; `cause` (rinka) compiles but puts the person in the *effect* slot and is true of every injury in the cast, so as a boolean it routes nothing. Do not re-propose without a corpus name that carries the meaning. **Graded tiers are refused**: `building(MedSec, $x)` compiles and the constant is free, but `building/2` has no exclusivity constraint. Its relation-wide closure blocks direct ground assertions; it does not stop rules from deriving two placements for an offender matching two combinations, and `err(_, Placement)` is blind to that conflict at runtime. The full verifier's generated placement audit rejects a conflicting source outcome when run; it does not give the deployed society a reader or remedy. A graded outcome needs a mutual-exclusion marker built in the same edit.
- **Never route a constitutional judgment through the compute backend**, and the reason is not performance. An external predicate is a **trusted oracle, not something nibli proves**: a `true` reply is auto-asserted as a ground fact mid-query and never re-derived or checked (nibli `README.md:18`, and the *Trust boundary* callout in its compute-backend section — **cite that one by its heading, not a line number**; the citation has rotted twice, `:333` then `:323`, and is `:325` today). So a grade, tier or severity computed there enters the record as *a conclusion someone wrote*, which is exactly what chapter 1 says this design makes impossible. Embedding the backend changes who operates the oracle, not whether the result is derived. **Built-in arithmetic is different on trust and identical on lifecycle** — `product`/`sum`/`quotient` are computed locally with no third party, but the arithmetic fast path calls the same `assert_typed_fact`, so they leave the same untracked ground fact; "carries none of the oracle problem" is true of trust only. Two engine behaviours worth stating precisely because the earlier wording overstated both: an unreachable backend yields `UNKNOWN(BackendUnavailable)` and never `FALSE`, but a tuple already computed in that session still answers TRUE from the auto-asserted fact — an outage-*cache*, not a stall. And a universal over a number-bearing predicate is still vacuously true. It is **sometimes** no longer silent, and the earlier wording here overstated that twice. Since nibli `95cba22` a `[Domain]` note fires — but only where the restricting relation is **asserted**; put one rule in between and it goes quiet again (their corrected repro: `sum(every dog, 2, 2)` notes, the one-hop twin `sum(every animal, 2, 2)` does not). And **neither the note nor the proof step is reachable from `nibli-pin`**, which is the only binary this repo runs — verified 2026-08-01, no flag exposes it, and `nibli-host` still fails outright on a stale wasm. So treat the diagnostic as absent here, not as a safety net. What actually contains this is `verify.sh`'s digit ban: there is nothing numeric to quantify over. Compute is legitimate for the claim registry and the method part; never for the society's own conclusions.
- **Chapter order is strictly computed**, never chosen. Exactly three elements are exempt from the derivation gate and each is labelled in the text: the opening note, Part V, and the final method part.
- **The length invariant is "book-1 stays majority-derived, measured across the whole book"** — the derived chapters must outweigh the opening note plus Part V plus the method part, combined. **The ~38,000 target for Parts I–IV is retired — ruled 2026-08-03: content governs.** The book's length is an outcome, not a goal: expansion happens only where verified-untold material exists (TRUE in the engine, absent from prose), and every non-derived part landed under its old budget by exactly that rule (Part V ~5,500 against ~12,000; the method part ~4,100 against ~5,000). Figures are hand-maintained and go stale — re-run `wc -w book-1/*.md` before trusting any; measured 2026-08-03: derived 29,440 against 10,545 non-derived, the invariant holding with a wide margin. Do **not** restate the old cap — *"~14,500 against ~36,000 derived keeps it near 29%"* — and do not restate the retired 38,000 as a target; both belong to git history now.

**Legacy `book.md` (below) — historical; do not port these into book-1 without re-checking them against the constitution:**

These were argued out and hardened in the text; several are stated as bright lines the book calls unamendable. A chapter edit made in isolation can easily re-introduce a passage the book now explicitly refutes, so check against this list before writing about points, identity, or voting.

- **Merit points are earn-only recognition** — never spent, gifted, priced, or converted. Recognition is also non-rivalrous: no fixed sectoral pools, because one nurse's acknowledgment must not come at another's expense. Inflation is controlled at the contribution level (per-task standards, caps, diminishing returns). See "What Merit Points Are—and Are Not". Scarce non-essentials above the floor are allocated by transparent non-market rules (need, rotation, waitlist, lottery), with merit only as a qualifying threshold.
- **No negative scoring of persons.** Nobody's record is ever docked as punishment; sanctions reach *perks* through due process. Pollution and fraud are handled by regulating the enterprise — a different instrument from scoring a human being (book.md:339). **book-1 adopted this narrowed** (ruling 2026-08-02, in the settled decisions above): *no subtraction except by due process for one's own adjudicated fraud* — the wrongdoer clawback stands, the student clawback is deleted.
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
what the book is about. `verify.sh` carries a **hard gate at zero** on this (since 2026-08-02;
the ratchet ran 14 → 0 across the chapter passes). Two allowlisted exceptions only: rhetorical
durations ("thirty years"), which are not claims about this design, and chapter 13's title —
"The One Thing Taken" *is* the single-deprivation claim, kept where the whole chapter defends
it, and the allowlist pins it to that file's line 1, so the phrase anywhere else counts.

Style — **legacy `book.md`/`manifesto.md` only; book-1's register is governed by the voice-boundary ruling in the settled decisions, and this warm first-person style must not be imported into derived chapters**: first-person, personal, and accessible; economic framing routinely contrasts *Keynesian*, *Marxist*, and *neoclassical* lenses (italicized); heavy use of **bold** for key claims. Both documents use curly quotes and em dashes throughout — match them. The technology chapters are intentionally more technical, with "Making It Simple: A Layman's Guide" as the deliberately non-technical retelling — keep that chapter jargon-free.

## Companion Repo

`~/projects/dhilipsiva/nibli` is a companion reasoning engine, cited by name in the tech backbone (book.md:923). Its `GUARANTEES.md` sets the register the tech chapters are converging on — state the guarantee, then name the sharp edge where it stops, rather than claiming unqualified safety. The nibli side of that convergence work lives in nibli's own `TODO.md`.

**nibli's `utopia.nibli` keeps the dead word deliberately** — do not "finish" the v0.7 rename by touching it. It is `include_str!`-compiled into three binaries and its UI label is pinned byte-stable by `nibli/CLAUDE.md:161`, so renaming it is real cost in another repo for no gain here. The dependency is one-way: nibli contains zero references to this repo, verified across its whole tree.

## Repo identity

This repo was renamed from `dhilipsiva/utopia-reimagined` on 2026-07-30 (v0.7). **Never let anything reoccupy that name** — GitHub's redirect covers web, API and git over both protocols and carries issues, stars and forks, but it dies the instant something takes the old slug, including an accidental `gh repo create`. That is irreversible and there is no warning. Note also that a rename does not redirect `raw.githubusercontent.com` links, and does not fix anything that already resolved the old name into a stored identifier.

## Commits

- One chapter or section per commit; the subject names the area (`Merit points: …`, `Tech backbone (3/n): …`). Avoid sweeping multi-part edits.
- The body explains **why** — the contradiction, gap, or review finding the change resolves — wrapped at ~72 characters. Not a list of what changed.
- A content commit is followed by a separate tracker commit updating `TODO.md`: `Tracker: <what landed> (<sha of the content commit>)`.
