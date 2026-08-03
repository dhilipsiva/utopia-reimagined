<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Book 1 — 10/10 Redesign TODO

This is a forward-looking redesign backlog synthesized from the manuscript review,
`reviews.md`, the formal constitution, and the verified test suite. It is separate
from `TODO.md`, which remains the authoritative tracker for the current book-1
release work. Do not copy an item into `TODO.md` until its scope is ruled.

## Validated starting point

- The complete `./verify.sh` suite passes: the derived spine is current, the registry
  is valid, all claim-linked queries are reachable, and the full pin and
  counterfactual suites pass.
- `reviews.md` is an undated, untracked collection of overlapping reviews. It is an
  idea source, not a specification: some findings are current, others describe older
  drafts, and several recommendations contradict settled design decisions.
- The principal live weaknesses are the external trust base of the record, the
  determination-to-action gap, and the narrow coverage of a society beyond coercion.

## Guardrails

- Preserve the distinction between a **verified derived claim**, a **Part V
  specification or argument**, and a **Book 2 operational design**.
- Keep formal-methods vocabulary out of book-1's derived chapters. The opening note,
  Part V, and `method.md` are the existing labelled exceptions.
- Do not pursue symmetry by making recognition rankable, reward operative, or standing
  purchasable. Those changes would recreate a social score.
- Do not mistake a provider's assertion of `Fed` or `Housed` for delivery. A delivery
  model must distinguish a claim of service from a person's usable receipt of it.
- Do not call a chain self-healing while `owe`, `become`, or `obliged` remains unread.
  It can diagnose; it cannot compel action.

---

## Phase 0 — Author-gated scope rulings

- [x] **[AUTHOR-GATED] Decide Book 1's new mandate.**
  - **Ratified 2026-08-03:** expand Book 1 into a formally derived constitutional
    interface for the whole society. The mandate, scope boundary, and retained
    operational seam are recorded in `CLAUDE.md` and
    `new-book-plans/book-1-constitutional-coverage-map.md`.
  - A scope expansion still requires a new constitution, regenerated spine, pins,
    counterfactuals, and revised chapter order. It is not an additive prose pass.

- [ ] **[AUTHOR-GATED] Rule the time model.**
  - State one coherent model: snapshot facts have no intra-period ordering; epoch
    carry provides coarse succession; there is no clock or duration arithmetic.
  - Decide whether that is a permanent constitutional refusal or whether a new,
    independently auditable temporal layer is worth its capture and withholding risks.
  - **Done when:** Chapters 4, 5, and 13 use the same explanation, and adversarial
    tests cover recency, carry, release, adulthood, expiry, and omission.

- [ ] **[AUTHOR-GATED] Rule the constitutional taxonomy.**
  - Classify each proposed addition as a material floor, liberty/invariant,
    procedural guarantee, common good/ecological ceiling, democratic policy domain,
    or operational mechanism. Do not call every important good a floor.
  - Preserve the principle that no material floor depends on work, virtue, status,
    score, citizenship, documentation, or compliance.
  - Draft decision artifact:
    [`new-book-plans/book-1-constitutional-taxonomy.md`](new-book-plans/book-1-constitutional-taxonomy.md).
    It is pending author ratification and does not change the constitution.
  - **Done when:** a one-page taxonomy replaces ad hoc expansion proposals.

- [x] **[AUTHOR-GATED] Define the democratic corridor.**
  - **Ratified 2026-08-03:** a majority chooses only among policies compatible
    with universal standing, core floors, equal protection/non-discrimination,
    due process, core liberties, and commons constraints.
  - The rule distinguishes ordinary policy, constitutional change, emergency
    power, and administrative discretion. Its formal compatibility test,
    amendment process, reviewer, and time-gated emergency mechanics remain
    contract work; current amendment machinery is not misrepresented as that rule.

## Phase 1 — Repair and map the verified kernel

- [ ] **Harden the two low-risk closure gaps already recorded in `TODO.md`.**
  - Assess and, if still sound, add `derived_only("lose")` and
    `derived_only("decide")`; update Chapters 6 and 9, pin files, fixtures, and the
    generated spine as required.
  - Do not use the stale review labels `loss` and `ballot` as though they were the
    current predicates.
  - **Verify:** full `./verify.sh`, including counterfactual fixtures.

- [ ] **Create a generated high-consequence premise audit.**
  - For every admitted or otherwise writable premise, show: writer/authority,
    provenance requirement, cheapest harmful consequence, challenge route, and
    whether the risk is patchable, external, or deliberately refused.
  - Include at least the roster/person entry, `free`, `mature`, epoch carry,
    seating, public-body status, amendment inputs, and placement inputs.
  - Keep this as a generated technical or method artifact, not a brittle counted
    claim in derived prose.

- [ ] **Build a record-integrity assurance case.**
  - Specify the needed guarantees: authorship, authority, append-only correction
    history, independent witnessing, reconciliation, challenge, and recovery from
    omission or deletion.
  - State plainly that an in-snapshot rule cannot distinguish a deleted entry from an
    entry never written. Do not promise an internal fix that the model cannot supply.
  - **Book 2 handoff:** record-storage, identity, cryptographic, and operational
    integrity mechanisms.

- [ ] **Red-team release, adulthood, and carry without creating new withholding gates.**
  - Test forged `free`, forged/withheld `mature`, forged/withheld carry, roster
    omission, and cross-epoch correction.
  - Evaluate any proposed two-entry authorization shape against its opposite failure:
    an official withholding release, voting status, or basic standing.
  - **Done when:** each input has a declared risk posture and a test proving it.

- [ ] **Test amendment semantics, not only amendment labels.**
  - Add adversarial cases for targetless, falsely targeted, and semantically concealed
    amendments; keep the known limit that a self-declared target is not proof of an
    amendment's real effect.
  - Separate a visible `admits`-vocabulary change from an entrenched amendment; do not
    claim that the current mechanism protects both.

- [ ] **Make placement exhaustive rather than accidental.**
  - Generate the relevant placement combinations; test duplicate, missing, and
    opposite-direction placement outcomes.
  - Preserve the distinction between a placement repair and actual free-person
    housing delivery.

## Phase 2 — Specify the comprehensive constitution

- [x] **[AUTHOR-GATED] Ratify the constitutional coverage map and expanded mandate.**

  - **Ratified 2026-08-03:**
    [`new-book-plans/book-1-constitutional-coverage-map.md`](new-book-plans/book-1-constitutional-coverage-map.md)
    is the scope and planning control. It maps current coverage, ratified scope
    requirements, pending constitutional interfaces, Book 2 handoffs, roles,
    democratic limits, and scenario tests. It does **not** change the constitution
    or prove coverage.

- [ ] **Maintain completed constitutional coverage rows before drafting chapters.**

  | Object | Required fields |
  | --- | --- |
  | Right/floor | holder, duty-bearer, minimum, delivery evidence, breach, interim remedy, appeal, audit |
  | Liberty/power limit | protected person, prohibited act, exception test, evidence, reviewer, review or non-temporal end condition, temporal status, remedy |
  | Public power | office, trigger, evidence, scope, conflict rule, limit, review, appeal, end condition |
  | Record | writer, basis, visibility, challenge, correction, retention, external assurance |

  - **Done when:** no new right or institution is added without a completed row.

- [ ] **Make universal standing a root condition, not a service denied by a missing entry.**
  - Design a safe “serve and reconcile” route for an unregistered person seeking help.
  - Keep identity resolution separate from access to emergency aid, floor protections,
    and due process.
  - Do not erase accountability through a right to disappear from the record.

- [ ] **Define the social floor, liberty shell, and ecological ceiling.**
  - Retain the existing floor as a compact core, then classify missing coverage:
    water/sanitation, adequate utilities, material security, disability and care,
    bodily integrity, usable information, accessibility, and voluntary social life.
  - Put privacy, bodily autonomy, movement, due process, association, expression,
    equal civic status, and procedural safeguards in a power-limiting layer where
    appropriate, not necessarily as more delivery predicates.
  - Add a commons/intergenerational constraint: rights must not be delivered by
    exhausting the conditions future people need to exercise them.

- [ ] **Write the Bodies specification.**
  - Define People/civic associations; legislature and electoral-deliberative bodies;
    provision and treasury; justice, defence, and appeal; constitutional review;
    integrity/audit; local bodies; and an independent rights advocate/ombudsperson.
  - Apply separation of functions: no actor may assert case facts, decide their
    consequence, execute it, audit it, and remedy it alone.
  - Define a rights advocate able to act for a child, disabled person, prisoner,
    newcomer, or unregistered claimant.

- [ ] **Specify obligations without making rights reciprocal bargains.**
  - Public institutions must respect, protect, fulfil, and remedy.
  - Contractors remain bound when delivering a public function.
  - Civic duties may exist, but failure to work, pay, identify oneself, comply, or be
    socially approved must not remove a basic floor.

- [ ] **Specify delivery as a lifecycle.**
  - Model: entitlement → service offered → accessible service → received or
    independently verified → disputed/failed → interim continuity → remedy →
    systemic correction.
  - A missing receipt must invite outreach and challenge, never terminate entitlement.
  - **Book 2 handoff:** staffing, procurement, budgets, logistics, enforcement, and
    capacity planning.

- [ ] **Define the democratic ceiling and majority process.**
  - Ordinary majorities decide policy, tax mix, providers, and choices above the core.
  - Every restrictive proposal needs public reasons, evidence, non-discrimination,
    least-restrictive means, a constitutional delivery duty, appeal, and independent
    review. Capacity modelling remains Book 2; time-dependent review/expiry remains
    author-gated.
  - An emergency model may never erase personhood, core floors, evidence rights, or an
    appeal path. Its temporal authority and end condition remain time-gated.

- [ ] **Add the missing non-carceral justice interface.**
  - Cover notice, counsel/advocacy, hearing, challenge, reparation, civil disputes,
    child representation, and post-release continuity.
  - Add explicit carceral limits: bodily integrity, communication, conditions,
    proportionality, release review, and reintegration support.

## Phase 3 — Make the architecture elegant without making it false

- [ ] **Name the real symmetries and necessary asymmetries.**
  - Real recursive interfaces:
    - right → duty → delivery → breach → remedy → review;
    - power → evidence → limit → appeal → correction;
    - harm → due process → least coercive response → repair/release.
  - Necessary asymmetries:
    - recognition is optional, binary, non-ranked, and non-operative;
    - punishment is coercive and requires a higher proof threshold;
    - public power is transparent while private life remains private;
    - accessibility may require unequal resources to secure equal standing.

- [ ] **State the determination/action boundary accurately.**
  - Book 1 must identify who owes what, what counts as delivery, failure, remedy, and
    public accountability.
  - Book 2 must specify how people, institutions, funding, and real-world operations
    make those duties happen.
  - Do not describe an infinite chain of duties as a solution to the need for people
    and institutions to act.

- [ ] **Use a vector of protected conditions, never a total social score.**
  - No abundance in one domain compensates for torture, homelessness, exclusion, or
    disenfranchisement in another.
  - Use aggregate, privacy-preserving disparity and outcome measures for public
    learning; never convert them into individual risk labels.

## Phase 4 — Rewrite for an intelligent non-specialist reader

- [ ] **Add a Reader’s Map inside an existing exempt element.**
  - State the promise, record/rule/reality distinction, the scope boundary, and the
    visible part structure before Chapter 1.
  - Preserve computed chapter order; make the reader-facing arc visible rather than
    casually reordering the derivation spine.

- [ ] **Standardize the chapter experience.**
  - Use: concrete existing case → plain finding → how the rule works → attack/failure
    → boundary → brief “what this established.”
  - Prefer chapter-local reminders to long backward cross-references.
  - Preserve the record-people's deliberately flat inner lives; do not add invented
    biographies or emotions as if they were evidence.

- [ ] **Add navigation aids.**
  - Annotated table of contents, concise glossary, character/case index, and selected
    diagrams for the record/conclusion distinction, the floor, institutional roles,
    and the delivery/remedy loop.
  - Do not add a diagram mechanically to every chapter; each must earn its cognitive
    cost.

- [ ] **Run reader-comprehension sessions.**
  - Test the Reader’s Map and representative chapters with non-specialist readers.
  - Success means readers can explain: what is written versus derived; who owes the
    floor; why an entitlement is not delivery; what a majority may decide; and where
    the design stops.

## Phase 5 — Evidence, psychology, and external review

- [ ] **Make Part V traceable at the point of claim.**
  - Link each empirical claim to its registry ID and source; rephrase causal language
    that rests only on association; retain uncertainty and instrument sensitivity.

- [ ] **Apply scientific and statistical discipline to every expansion.**
  - Each new claim needs a source, an abuse case, a counterexample test, a residual
    assumption, and an explicit uncertainty boundary.
  - Treat group-level outcome data as feedback for institutional repair, not as a
    measure of individual worth.

- [ ] **Ground psychological claims without turning people into variables.**
  - Test for autonomy, voice, non-humiliation, relatedness, meaningful control,
    retaliation, status competition, and coercive incentives.
  - Use lived-experience review; do not infer psychology from a formal proof.

- [ ] **Run a multidisciplinary red-team before calling the redesign complete.**
  - Include constitutional law, public administration, disability/accessibility,
    public health, economics, data governance, and people affected by coercive
    institutions.

## Explicitly rejected review proposals

- Restoring fixed counts in reader-facing book prose; counts are intentionally gated
  and have historically rotted.
- Treating `reward` as punishment's inverse, granting standing for contribution, or
  allowing recognition to buy material security, authority, or voting power.
- Calling the current record a self-healing closed circle, a mathematical group, a
  Bayesian model, or proof that random sampling cannot be captured.
- Adding provider-authored delivery facts as evidence that the floor was met.
- Adding formal-language explanations, histories, or implementation detail throughout
  derived chapters instead of using the existing Part V/method boundary.
- Treating a transition roadmap, full operational economy, record-storage technology,
  or implementation logistics as Book 1 prose. The 2026-08-03 mandate adds
  constitutional interfaces—not their operating machinery—to Book 1 scope.

## Completion standard

The redesign is ready only when:

- every constitutional domain has a completed coverage-matrix row;
- the Book 1/Part V/Book 2 seam is visible and honest;
- the full verification suite and new adversarial tests pass;
- no material floor is gated by a mutable status or a provider’s self-certification;
- ordinary readers can follow the core argument without formal-methods training; and
- reviewers can identify both the system's guarantees and its external trust
  assumptions without reconstructing them from scattered chapters.
