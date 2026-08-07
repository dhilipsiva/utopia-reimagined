<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# TODO — book-1

**This tracker covers book-1 only.** It is strictly future-facing: a bullet is
deleted the moment it fully lands. History belongs in git.

The repo is heading for two new books plus a clean deletion:

- **book-1** — the active work, in two parts with a deliberate seam:
  - **Parts I–V — the constitutional and social destination.** What the society
    must guarantee, permit, organise and constrain, including normal, failure and
    recovery interfaces — never transition or costed operation. Derived from the
    constitution and **gated on it**.
    **Jargon-free** — a general reader finishes Part V and stops, and the
    formalism is never mentioned in these parts.
  - **Final part — the method, explicitly optional.** The constitution, the
    derived spine, the compile-time firewall, the evidence/conclusion split, and
    what the logic refused. Labelled as a different kind of reading. The only
    place the formalism appears, and what answers "you built a machine and hid it".
- **book-2** — **how the destination would be operated and reached.** It owns
  staffing, costs, capacity, resources, technology, workflows, transition,
  deployment, empirical feasibility, and operation under ordinary and declared
  shock conditions. Its tracker is `book-2/TODO.md` — collect there, but do not
  execute Book 2 work until Book 1 — First Edition actually ships at Gate C.
  book-1 references it once, at the end.
- **`book.md` and `manifesto.md`** — legacy, to be **deleted** once both new books
  are written. Nothing in this tracker improves them. The one obligation they carry
  is that no valuable material is lost on the way out; what still needs porting is
  itemised under **Legacy harvest** below (the 55 sourced references are already in
  `registry/claims.json`, and the five bright lines are swept — the result stands
  under **Standing facts and methods**; the clawback consequence it forced was ruled
  2026-08-02, bright line 2 standing narrowed).

**THE WORKING ORDER.** All fourteen chapter passes are complete (2026-08-02) and
their records live in git, not here. What remains runs in two preliminary phases,
then a full-society expansion backlog and cross-cutting sections:

1. **Phase 1 — author-gated decisions.** The volume, edition, and stopping
   boundary, state form, and political membership are settled. Equality,
   economic, family/plurality, ecology, public-power, assurance, narrative, and
   reader-threshold decisions remain open. Neutral inventory and decision briefs
   may proceed in parallel; each still-gated domain's rules, prose, and public
   claim wait for its own ruling. The final reader threshold waits for the pilot.
   This section
   has been destroyed by tooling once and is watched accordingly.
2. **Phase 2 — engine handoffs (nibli).** A read-only finite-decision capability
   audit is open. Run it before formalising generic collective-decision rules because
   some of what the book has to concede may be an engine limitation rather than a
   design choice. It does not block unrelated inventory, evidence, or decision-brief
   work.
3. **Full-society expansion — implementation backlog.** The ratified constitutional
   mandate remains the legal spine, but the completion target also requires a
   versioned disposition map for declared social axes and envelope, a functional
   cross-domain model, and a balanced reader-experience contract, ordered from
   scope mapping through public review.

The remaining sections are cross-cutting: the book-1 work that remains around the
finished text (the pre-expansion text was complete as of 2026-08-03 — epigraph, opening note,
the derived chapters, Part V and the method part are all present in source; what is left is
the full-society destination expansion and the licence files), the reach
plan, data work, legacy harvest, and a pointer to book-2's own tracker. **Standing
facts and methods** closes the file and holds knowledge, not tasks.

Plain bullets, never numbered. Delete a bullet entirely when it fully lands;
update it if only partly done. Read-only inventory, evidence gathering and neutral
decision briefs may run in parallel; shared-tree edits, verification and commits land
serially, one owned item at a time.

Bullets prefixed **[AUTHOR-GATED]** need the author's own voice, personal memory,
or a design decision — they are collected in phase 1 rather than scattered.

**THE INCLUSION GATE — applies to Parts I–V only.** Those parts describe a
destination, not a route. Before any passage goes in, two tests: (a) does it
describe what the society must guarantee, permit, organise, or constrain — not
transition, costed operation, or how anyone gets there? and (b) does the
constitution derive it? A passage failing (a) belongs to **book-2**;
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
`new-book-plans/`; the full-society expansion backlog below turns the ratified
constitutional boundaries and full-society boundary into active work.

---

## Phase 1 — Author-gated decisions. Rule each before its dependent implementation.

Each of these is a design decision, not a task. Record the ruling in `CLAUDE.md` when it
lands, so it is not re-proposed. **This section was destroyed by tooling once** — a
tracker-edit slice in `412e5a4` anchored on the next `---` after a separator an earlier
cleanup had removed, and swallowed 145 lines, all but one of them open; the loss went
unnoticed because nothing checks this file, and a later commit then described the
emptied section as "every earlier decision was ruled", which was false. Treat these as
the most expensive lines in the file. Line numbers cited inside bullets may predate
later edits — re-derive before trusting.

The author has directed the project toward a well-balanced two-book model. Book
1's use of “comprehensive” remains bounded to its Gate B/C declared scope, and
the Gate E claim is bounded to a declared reference envelope. The two-book
container, C-then-E release sequence, and versioned stopping boundary are settled.
The state form and residence-first political membership are also settled. The
remaining decisions determine other constitutional choices, assurance,
narrative, and reader thresholds; they do not reopen whether the broader result
is wanted.
Scope inventory, gap discovery, evidence collection and neutral option briefs may
proceed before a ruling. Do not implement a contested rule family, rewrite
dependent prose, or make its completion claim until the author has ruled it.

- [ ] **[AUTHOR-GATED] Rule the substantive-equality and anti-subordination
  baseline.**
  - Decide whether the constitution reaches direct, indirect, systemic and
    intersectional discrimination; segregation, exclusion, harassment and
    retaliation; accessibility/reasonable accommodation; and lawful positive
    measures.
  - Rule permissible distinctions, evidence burdens, public and concentrated-
    private reach, privacy-safe group diagnostics, review, individual/systemic
    remedy and the end/review conditions for positive measures.
  - Formal equality alone may not hide durable dependency; corrective measures may
    not create identity scores or make documentation a condition of the floor.

- [ ] **[AUTHOR-GATED] Rule the economic-pluralism and protected-private-sphere
  settlement.**
  - Decide what ordinary majorities may choose among public, cooperative, commons,
    household, and private arrangements above the floor, and which labour,
    property, contract, association, family, conscience, culture, and privacy
    boundaries they may not cross.
  - Preserve the settled guards: property is conditional on floors and commons;
    recognition, merit, contribution, wealth, and personal scores buy no standing,
    floor, authority, political weight, or commons access.
  - Name when concentrated private power—employer, landlord, lender, insurer,
    platform, utility, or monopoly—acquires public-like duties because exit,
    dependency, or essential function makes formal consent inadequate.
  - Rule the constitutional allocation principle for genuine physical scarcity:
    what need, accessibility, urgency, rotation or lottery may decide; what continuity
    and appeal survive; and why wealth, merit, contribution, recognition and political
    favour never decide the floor.

  - Rule competence/licensing for safety-critical and fiduciary roles,
    portable social insurance, and lawful above-floor compensation/incentives for
    skill, difficult work, innovation, investment, maintenance and public service.
    Separate every such distinction from personhood, floor, political weight,
    immunity and personal-worth scoring.

- [ ] **[AUTHOR-GATED] Rule family, dependency, reproduction, and collective/
  plurality baselines.**
  - Rule children's independent rights, best-interests/voice standard, supported
    decision-making, guardianship limits, caregiver/dependant duties, family
    pluralism, reproductive autonomy, domestic intervention threshold, ageing and
    end-of-life authority.
  - Define the one general legal-adulthood status imported by the ratified
    political-membership contract, including non-discretionary acquisition,
    accessible evidence, challenge, correction, and continuity. Do not add a
    separate political maturity test, higher candidacy age, or retroactive loss.
  - Rule whether and how minority, indigenous, linguistic, religious and other
    collective claims receive self-government, representation, land/common claims
    or veto/procedural protections without subordinating individual standing.
  - Conditions and support may be guaranteed; no institution may prescribe the
    approved family, belief, relationship, identity or personal outcome.

- [ ] **[AUTHOR-GATED] Rule ecological, future-generation, commons, and
  non-human-animal baselines.**
  - Choose protected commons, enforceable ecological ceilings, non-regression and
    restoration duties; the authority and limits of an independently checked future-
    conditions guardian; and how these constrain majority, property and trade.
  - Rule the basis and minimum scope of non-human-animal protection, permitted use,
    enforcement and remedy without assuming that only constitutional personhood can
    ground protection.
  - Book 1 owns the invariant, evidence, standing/guardian and remedy contracts.
    Book 2 owns measurement, resource budgets, transition and feasibility.

- [ ] **[AUTHOR-GATED] Rule public-safety, defence, emergency, and external-power
  baselines.**
  - Decide the constitutional roles and separation of police/investigation,
    prosecution, intelligence, military/defence and civilian authority; permissible
    force; conscientious objection; emergency declaration/renewal/end; and the
    authority for borders, asylum/expulsion, treaties, trade, war/peace, humanitarian
    duties, plus external recognition, defence, cross-border status, and
    international effects before and after a lawful exit.
  - Do not reopen the internal secession rule: a regional vote opens negotiation,
    and exit needs federal agreement, rights/minority review, settlement, and final
    affected-population ratification; unilateral exit is invalid.
  - Name the non-derogable core, evidence and public-reason duties, cross-branch
    checks, temporal contracts, independent review and individual/systemic remedies.
    Operational capability and other states' cooperation remain Book 2/external.

- [ ] **[AUTHOR-GATED] Rule the assurance portfolio for a functional-society
  model.**
  - **Recommended:** use Nibli for legal entailment, admissibility, authority, and
    structural refusals; versioned quantitative models for resources and budgets;
    dynamic simulations for queues, shocks, and transition; the registry for
    empirical claims; and reader/lived-experience studies for comprehension and
    human effects. No one formalism may impersonate the others.
  - Rule which classes of Book 1 claim must be formally derived, which may be Part V
    specifications, which require Book 2 evidence, and what language is permitted
    when a model establishes safety but not liveness or feasibility.

- [ ] **[AUTHOR-GATED] Rule the narrative human register for ordinary social
  life.**
  - The current rule keeps record-people's inner lives flat and permits exactly one
    generic second-person domestic vignette. Decide whether balance must stay within
    flat constitution-backed cases, diagrams, historical evidence and reader tests,
    or whether the author will add a strictly limited class of clearly labelled,
    author-drafted ordinary-life vignettes.
  - Do not let an invented biography, composite citizen or attributed emotion become
    evidence. If the register broadens, define its location, label, sourcing/voice
    rule and maximum legal role before prose is written.

- [ ] **[AUTHOR-GATED] Rule the reader-balance evidence protocol and threshold
  timing; ratify the release threshold after the pilot.**
  - **Recommended:** approve now a pre-registered pilot-and-fresh-holdout method,
    while reserving the numerical/qualitative release threshold for an author ruling
    after the pilot. This lets constitutional work proceed without inventing a
    standard before evidence exists.
  - Require readers to identify ordinary constructive life, democratic choice,
    private freedom, successful provision, repair, and the prisoner as a stress test
    rather than the society's central inhabitant.
  - Do not use an arbitrary word, chapter, demographic or sentiment quota, and do
    not let an aggregate score hide a repeated core misconception.

---

## Phase 2 — Engine handoffs (nibli)

**dhilipsiva wrote nibli, and he is the channel between the sessions — for book-2's
tracker exactly as for this one.** The sessions cannot see each other, so **an item is not
ready until it carries a self-contained prompt in a fenced block**. Write the prompt as
one session speaking directly to the other, with dhilipsiva carrying it: address the
engine session in the second person, assume **zero** knowledge of this repo — no bullet
references, no chapter numbers, no "see above" — and close by instructing that session to
write its reply addressed directly back to this one, again through dhilipsiva: the sha,
what changed, whether any verdict moved, and what the prompt itself got wrong. That last
item has been non-empty more often than not, on both ends of the channel.

Breadth by itself is not an engine defect. First assign each claim to the assurance
method ruled above. Open a repair prompt only when a minimal public fixture shows
that a claim assigned to Nibli cannot be expressed soundly, loses a definitive
verdict, or exceeds a measured bound. Do not ask one reasoning engine to become a
budget, population, logistics, psychology, transition, source-deployment, or
authentication system.

- [ ] **Measure the finite collective-decision boundary before formalising the
  democratic corridor.**
  - This is a read-only capability audit. It must not modify the engine repository,
    revise the ratified voting rules, choose new thresholds, or treat a renamed
    ground premise as authenticated.
  - **Done when:** the reply provides neutral executable probes and a surface-by-
    surface capability table; distinguishes fixed finite enumeration from
    roster-parametric aggregation; distinguishes duplicate submissions, conflicting
    choices and multiple derivations; executes the caller-supplied Assembly,
    Council, confidence, referendum, initiative, and recall cases below; states the
    external completeness,
    authentication and challenge contract; and reports any suspected engine bug as a
    separate minimal reproducer without fixing it.

~~~text
You are working in the Nibli engine repository. Assume no knowledge of any book
or constitution project. This is a read-only capability audit: do not edit,
commit, or push the engine repository.

Start from current engine main, report its exact source SHA and version, and
confirm that it is at or after the minimum compatible baseline
4cb02aade43b394374c40e661907ad66df3af3fe.

A separate formal-constitution project needs to know which finite
collective-decision checks current Nibli can establish and which require an
external, authenticated and contestable result service. Do not invent or revise
an electoral system. Use these caller-supplied legal cases without treating them
as built-in engine semantics:

- A constitutional amendment needs affirmative votes from two-thirds of the
  full People's Assembly roster.
- Its national referendum needs more affirmative than negative valid votes, no
  turnout quorum, and failure on a tie; blank and invalid submissions are not
  affirmative votes.
- A directly regional amendment needs a majority of the Regions Council's full
  aggregate regional voting weight. A competence or boundary change also needs
  more affirmative than negative valid votes in every directly affected region,
  with no turnout quorum and failure on a tie.
- For ordinary law, the Regions Council may return a bill once with reasons; the
  People's Assembly may repass it only under the same rule that first passed it.
- Constructive no confidence removes a government only when the same decision
  identifies and certifies its successor.
- If an ordinary-law initiative and Assembly counterproposal both pass that
  valid-vote test, the larger affirmative share wins; neither or a tied share
  preserves current law.
- Constructive recall requires both a removal majority and one successor under
  a predeclared majority-producing rule; failure or a successor tie preserves
  the ordinary term and succession route.
- Each decision admits at most one person-bound effective submission across all
  participating jurisdictions.

The exact decision roster and its completeness assurance are externally
supplied and distinct. Authentication, publication, challenge, correction,
clock advancement, and institutional action are external unless separately
represented by supplied premises. Do not design those systems in this audit.

Using neutral names, build the smallest fixtures needed to measure these
boundaries:

1. Exact snapshot find/count observations over an externally supplied finite
   roster and submitted-choice records.
2. Whether CountNode or compute expressions are query-only, and the exact
   refusal at assertion ingress and in rule antecedents.
3. Fixed hand-enumerated finite rules versus genuinely roster-parametric quorum
   or majority computation.
4. A complete-roster attestation supplied as an external premise, and the
   observational indistinguishability of an incomplete roster from a genuinely
   smaller roster when that assurance is absent.
5. Empty roster, tie, abstention, blank/invalid submission, incomplete roster,
   withheld completeness evidence, and every caller-supplied threshold/default
   case above.
6. Distinct submitted-record identities related to voter and choice. Separate:
   two identical submissions with different record identities; conflicting
   choices by one person across jurisdictions; and multiple derivations of one
   effective logical fact.
   State where set semantics collapse byte-identical facts and why conflict
   detection does not itself select an effective choice.
7. An externally supplied result certificate. State plainly that it remains an
   asserted trust-root premise to Nibli; authentication, publication,
   completeness, availability and challenge assurance are external unless
   represented by additional supplied premises, which are trust roots too.
8. Missing or undecidable witness leaves. Confirm whether find/count fail closed
   rather than silently undercounting, and distinguish FALSE, UNKNOWN and
   RESOURCE_EXCEEDED.

For every case, identify the usable surface: KR rule language, nibli-pin query,
core API, host harness or external service. A bounded three-person rule is only a
fixture result, not generic election semantics. Missing completeness evidence may
safely block authority but can create a withholding veto; state that liveness and
redundant attestation remain constitutional/operational design questions.

Do not add voting, arithmetic, certificate authentication, roster completeness,
closed-world semantics or non-monotonic behavior. If you find behavior that
contradicts a documented existing guarantee, report a separate minimal
reproducer and proposed acceptance test, but do not repair it in this audit.

Run the smallest relevant existing tests plus the neutral probes and give exact
commands and outputs. Then write your reply directly to the
rights-nobody-has-to-earn session through dhilipsiva. Include: exact source SHA
and version; probes; commands; the capability table; definitive/non-definitive
verdicts; external trust and liveness boundaries; any separate bug reproducer;
confirmation that no repository change occurred; and what this prompt got wrong.
~~~
Do not work around an engine limitation in prose — conceding a fixable limitation
as though it were a design choice is the specific dishonesty this phase exists to
prevent, and it is why this audit precedes generic collective-decision rules.

**When a reply lands here**, independently build or identify its source commit, select
that binary explicitly, and re-run `./verify.sh` before believing anything. This repo
has twice measured an engine change that was never rebuilt.

---

## Full-society expansion — implementation backlog

This is the canonical merged redesign backlog for the ratified constitutional
mandate and the author-directed full-society completion target. Except for the
staged T3 path already named below, it is future-facing: the mandate, coverage
map, taxonomy, democratic corridor, domain ledger, system map and reader contract
set requirements, but do not make an unimplemented predicate, duty, institution,
operation, delivery route, remedy, social outcome or narrative current.
The federal parliamentary state form and residence-first political membership
are author-ratified but unimplemented. Their controlling contract is
`new-book-plans/book-1-state-form-and-political-membership-decision.md`;
remaining office-term numbers and finite mechanics are delegated implementation
choices only inside its hard constraints, not a reopened author gate.

### Scope and guardrails

- The ratified scope and contract boundary live in
  [`new-book-plans/book-1-constitutional-coverage-map.md`](new-book-plans/book-1-constitutional-coverage-map.md),
  with the taxonomy, time, and edition decisions beside it. `CLAUDE.md` owns the
  settled rulings; this section owns the work still required to implement them.
- `reviews.md` is a tracked but undated collection of overlapping reviews. It is an
  idea source, not a specification: some findings describe older drafts and some
  recommendations conflict with settled decisions.
- Preserve the distinction between a **verified derived claim**, a **Part V
  specification or argument**, and a **Book 2 operational design**. Keep formal
  methods vocabulary out of derived chapters; the opening note, Part V, and
  `method.md` are the labelled exceptions.
- Do not pursue symmetry by making recognition rankable, the existing
  recognition predicate `reward` operative, or standing purchasable. This does not
  pre-decide author-ratified above-floor compensation or positive incentives. Do not mistake a provider's assertion for usable delivery,
  or call a chain self-healing while `owe`, `become`, or `obliged` remains unread.
- Standing and entitlement to a material floor may not depend on work, virtue,
  wealth, citizenship, documentation, score, compliance, contribution, a qualifying
  test, or official approval. Necessary, proportionate, contestable clinical or
  needs evidence may select a safe/accessibility-adjusted way to deliver what remains
  owed; it may not terminate or reduce the minimum. Book 1 defines constitutional
  interfaces; transition, operations, infrastructure and service logistics remain
  Book 2 until the author rules otherwise.

### Expansion foundation — Map the whole society before adding rule families

- [ ] **Build a full-society domain-and-layer ledger with a declared stopping rule.**
  - Create one reviewed, normalized canonical source with stable domain, role,
    body/institution, power, dependency, scenario, claim, external-assumption,
    threshold and assurance-route IDs. Give every record applicability, layer,
    status, severity, consequence, owner and closure fields.
    Generate the coverage map, contract-card views, role matrix, dependency map,
    assurance allocation, reader ledger and Book 2 crosswalk from that source; do
    not maintain competing matrices by hand.
  - Preserve the ratified constitutional taxonomy as the legal-effect axis; it is
    chosen, not exhaustive. Add an orthogonal social-domain axis answering which
    part of life is involved and where its decisions belong.
  - At minimum inventory: personhood/life course; body, health, care, family and
    intimacy; learning, knowledge, media, science, religion and culture; food,
    housing, land, utilities, infrastructure and public space; work, property,
    enterprise, exchange, money, credit, debt and public finance; democracy,
    government and administration; civil/criminal/administrative justice, safety
    and repair; records, surveillance and automated power; locality, membership,
    mobility, migration and external relations; emergencies, security and defence;
    ecology, non-human animals, commons and future conditions; and friendship, leisure, mutual aid,
    associations and the residual free social field.
  - For every domain record: constitutional invariants; decisions left to ordinary
    majorities; protected private/civic choice; public bodies and expressly bound
    private actors; Book 2 operations; external facts/liveness assumptions;
    applicable class cards and structural walls; evidence, time, challenge and
    remedy contracts; scenario applicability; and its reader-facing destination.
    Governed/provided domains require ordinary-success, failure/abuse and recovery
    paths. Protected free/private domains require non-interference, non-recording/
    non-compulsion and recourse boundaries—not a state-certified successful life.
  - A row is disposition-complete only when every applicable field is answered or
    explicitly marked “not constitutionally prescribed”,
    “democratic/ordinary-law choice”, “Book 2 operation”, or “external
    assumption”. Classification is routing, not assurance. An unresolved field
    must carry severity, consequence, owner, closure condition, and public-claim
    limitation; a critical gap applicable to the gate's permitted claim blocks
    that gate. An unclassified public power is a defect. A harmless private
    practice may map categorically to the protected free field only after checking
    rights harm, dependency/concentrated power, public duty, and commons/external
    effects.
  - Give every reviewer proposal one public disposition: add it to the
    canonical source; classify it with reasons under the available dispositions
    or as duplicate/immaterial; or retain it as an unresolved severity-rated
    limit. The named severity owner applies the published rubric and an
    independent checker reviews the result; a reviewer forces a reasoned
    disposition, not automatic acceptance or a personal veto.
  - **Done when:** every projection regenerates from the canonical source and an
    independent scope review can name no material omitted domain, role,
    dependency, or failure without the ledger adding it, classifying it out with
    reasons, or recording a visible severity-rated limit. The closure record
    binds the gate, claim, source version, envelope, candidate, review cut-off,
    assurance records, residuals, and claim limits. This is versioned
    exhaustiveness for those declared axes, not a timeless completeness theorem,
    and disclosure alone does not cure a critical gap.

- [ ] **Define the reference-society envelope and measurable meanings of
  “functional”.**
  - Version the population and demographic profile; territory, settlement pattern
    and geography; resource and ecological endowment; technology and infrastructure
    baseline; trade and external-cooperation assumptions; institutional starting
    state; time horizon; promised service levels; and ordinary plus compound shock
    set. Never let a result inherit these silently.
  - Define adequacy, continuity, equity, accessibility, resilience and sustainability
    criteria for each applicable domain. Distinguish a parameterized design from a
    result established only for one reference case.
  - Book 1 records which constitutional claim depends on which envelope field and
    what remains invariant when it changes. Book 2 owns calibration, empirical
    validation, capacity models and sensitivity/scenario analysis.
  - **Done when:** every functional or feasibility claim names an envelope version,
    metric, threshold owner, uncertainty range and failure interpretation, and no
    single favourable scenario is presented as society-wide feasibility.

- [ ] **Build the roles, life-course, scale, and power-position matrix.**
  - Cover birth/first contact, childhood, adulthood, ageing, disability, illness,
    dependency, caregiving, death and succession without making capacity or
    documentation a condition of standing.
  - Cover people as family/household members, friends, learners, patients,
    caregivers, workers/non-workers, union members, owners/tenants, consumers,
    creators, worshippers/non-believers, association members, voters/candidates,
    public servants, newcomers/migrants, claimants, accused people, prisoners and
    released people. One person may occupy many roles; none buys a higher floor.
  - Test individual, household/association, local, regional, national,
    cross-jurisdictional and intergenerational scale. Avoid demographic decoration
    and the impossible full Cartesian product; justify pairwise and
    high-consequence edge coverage.
  - **Done when:** each material domain has reviewed role/scale applicability,
    each public or concentrated-private power has both affected and checking
    positions, and omitted combinations carry an explicit risk-based reason.

- [ ] **Model the society's functional flows and cross-domain dependencies.**
  - Map flows of authority, information, care, labour, resources, money, claims,
    services and accountability from lawful source through ordinary operation,
    interruption, interim continuity, remedy, recovery and systemic correction.
  - Identify dependency cycles, bottlenecks, conflicts of interest, single points of
    failure and cascade paths. No right is called delivered because an institution
    promised it, and no body is called functional because its name exists.
  - Classify every dependency as constitutionally guaranteed, democratically
    selected, operationally supplied, or externally assumed. Assign an owner and a
    consequence for its absence.
  - **Done when:** the canonical source can generate an owner-labelled dependency
    graph, every critical input/output has a source, destination and failure
    consequence, and the closure audit rejects unowned or unsatisfiable edges plus
    unbounded, self-certifying, deadlocking or single-veto cycles/bottlenecks.
    Bounded, owned ordinary service, feedback, fiscal and ecological loops must be
    classified and tested, not rejected merely for being cyclic.

- [ ] **Build whole-society journeys, collisions, and stress cases.**
  - Execute ordinary-success, failure/abuse, continuity, remedy and recovery paths
    for every governed, provided or power-bearing domain—not only isolated clauses.
    For protected private/civic domains, test freedom without permission,
    non-recording/non-compulsion, the narrow evidenced-harm threshold and recourse
    against interference; never pin love, belief, friendship, art or fulfilment as
    a state-defined successful outcome.
  - Test at least: property versus floor; speech/association versus private harm;
    majority versus minority; parent/guardian power versus child standing;
    employer/landlord/platform power versus meaningful exit; emergency versus
    liberty; present allocation versus future commons; locality versus portability;
    privacy versus public accountability; and physical scarcity versus equal floor.
  - Include compound shocks such as pandemic, famine, infrastructure failure,
    displacement, institutional capture and conflicting jurisdictions. Book 1 must
    state invariant/failure behavior; Book 2 must test capacity and degradation.
  - First generate a reviewed scenario catalogue with stable IDs and applicability;
    execute constitutional cases only after the relevant author ruling and contract
    cards land. **Done when:** every critical domain/dependency and each high-
    consequence collision has an owned ordinary, failure and recovery route.

- [ ] **Create a generated constitutional-closure and model-allocation audit.**
  - Generate it from reviewed domain, role, dependency and assurance data; never
    infer constitutional importance from predicate names or raw counts.
  - Fail when a floor lacks delivery/continuity/remedy; a public power lacks source,
    limit, review or temporal status; a body decides, executes, audits and finally
    remedies itself; a private duty is merely implied; a record lacks
    writer/challenge/correction; a democratic choice crosses the floor; a Book 2
    operation is presented as Book 1 assurance; an external assumption is hidden;
    or a reader-facing claim has no formal/evidentiary owner.
  - Record which claims belong to Nibli, quantitative/resource models, dynamic
    simulations, the evidence registry, operational assurance, or reader/lived-
    experience testing. One green model may not substitute for another.
  - **Done when:** a deterministic check regenerates every projection from the
    reviewed canonical source, rejects stale/unowned records and all named closure
    failures, and publishes a claim-by-claim pass, block or bounded-unresolved
    result with the responsible verification route.

### Expansion phase 2 — Specify the comprehensive constitution

“Comprehensive” here is bounded to Book 1's declared source version and scope at
Gate B; it does not claim Book 2 operations or feasibility.

- [ ] **Implement the ratified T3 temporal path in stages — staged rule families and
  the full-source execution gates landed; four semantic and prose closures remain.**
  - Content commit `6f6c636` implements witnessed T1 transitions and carry,
    typed transitive T2 event/record paths, and canonical-current, source/window/
    case/lease-bound T3 Court custody. Forty fresh processes now execute 236
    temporal pins, including replay, divergence, omission, forgery, typed cycles,
    conflicting bindings, unwitnessed reverse dates, and withheld standing evidence.
  - Content commit `ed93d42` restored ordinary full-source opaque entitlements and
    deleted the extracted-floor workaround. Content commit `c7d9a19` then restored
    chapter 7's direct Zed entitlement and made every generated placement subject's
    floor projection execute cold against its exact matrix facts, without a `person`
    overlay. A standing-removal sabotage protects that composition boundary.
  - Before closure, repair or explicitly narrow four non-engine gaps:
    - withholding either predecessor-standing witness can still suppress `person`
      and the floor; resolve this through the universal-standing root item below or
      an explicit author ruling, then pin the chosen polarity;
    - temporal correction, supersession, lineage, non-revival, and challenge/duty
      carry are described more strongly than the current rules establish; formalise
      them or label each as a target, requirement, or Book 2 boundary;
    - suppressing a genuine challenge filing can leave a lease unsuspended; correct
      the fail-safe overclaim and add an executable challenge-intake-withholding case
      before deciding whether the durable record/advocate route lands here;
    - reconcile `3-spine.md`'s hand-written strata, floor, error-surface, and delivery
      interpretation with its current generated block and constitution.
  - **Done when:** the T3 implementation gate in
    [`new-book-plans/book-1-time-model-decision.md`](new-book-plans/book-1-time-model-decision.md)
    passes with the four closures above resolved and pinned, residual liveness
    explicitly handed to Book 2, and every affected claim revised or pinned.

- [ ] **Maintain completed constitutional coverage rows before drafting chapters.**
  - Use the coverage map's contract fields and the taxonomy's formalisation metadata
    for every new rule family. Every card also records any applicable structural-wall
    ID and enforcement mechanism. At minimum, record:

    | Object | Required fields |
    | --- | --- |
    | Right/floor | holder, duty-bearer, minimum, accessibility, recipient-side access/receipt evidence, authorised writer, challenge route, no personal-outcome inference, breach, interim continuity, remedy, appeal, audit, temporal status |
    | Liberty/power limit | protected person, prohibited act, direct public binding, public prevention/investigation/remedy duty for private interference, any explicit private binding, narrow exception test, evidence, independent reviewer, public reason, review or current-T0 non-temporal end condition, temporal status, remedy |
    | Public power | office, democratic source, trigger, evidence, scope, conflict rule, non-delegable limit, review, appeal, current-T0 non-temporal end condition, temporal status |
    | Record | writer, permitted basis, visibility/privacy, challenge, correction, retention, deletion control, external assurance, independent recipient, action duty, continuity/remedy path, temporal status |
    | Commons/future condition | protected common, present duty, ceiling or non-destruction rule, evidence, standing for any present person and an independently checked public guardian, guardian authority/independence/evidence/removal controls, remedy, public accountability, temporal status |

  - **Done when:** every domain in the full-society ledger has complete applicable
    rows before its rule family or prose lands; no name, value, office, or floor is
    accepted as coverage by itself.

- [ ] **Make universal standing a root condition, not a service denied by a missing entry.**
  - Design a safe “serve and reconcile” route for an unregistered person seeking help.
  - Cover birth/first contact, absent or disputed identity, migration between records,
    decision support, and death/status correction without making registry presence,
    capacity, citizenship, or documentation a condition of standing.
  - Keep identity resolution separate from access to emergency aid, floor protections,
    and due process.
  - Do not erase accountability through a right to disappear from the record.

- [ ] **Define the social floor, liberty shell, and ecological ceiling.**
  - Retain the existing floor as a compact core, then classify missing coverage:
    food, water/sanitation, housing and land access, adequate utilities, material
    security, health and care, learning and usable information, disability access,
    mobility, communication, public space and voluntary social life.
  - Put privacy, bodily autonomy, movement, due process, association, expression,
    conscience, family/intimate life, equal civic status, and procedural safeguards
    in a power-limiting layer where appropriate, not necessarily as more delivery
    predicates.
  - Add commons, non-regression and intergenerational constraints: present rights
    may not be delivered by exhausting air, water, climate, biodiversity, land,
    infrastructure or other conditions future people need to exercise them.

- [ ] **Establish substantive equality and anti-subordination across domains.**
  - Define direct, indirect, systemic and intersectional discrimination;
    accessibility and reasonable accommodation; segregation and exclusion;
    harassment, retaliation and status subordination; and lawful positive measures.
  - State permissible-distinction, evidence-burden, public-reason, independent-
    review and individual/systemic-remedy tests for public bodies and expressly
    bound private power. A formally identical rule is not sufficient when its
    predictable effect entrenches dependency or exclusion.
  - Use privacy-preserving group evidence to find institutional patterns without
    assigning individual worth, risk or entitlement scores. Positive measures must
    be reviewable and may not make identity documentation a condition of the floor.

- [ ] **Complete bodily autonomy, health, care, family, and life-course interfaces.**
  - Specify consent, reproductive autonomy, mental and physical care, disability
    access and decision support; children’s interests and voice; ageing, dependency,
    caregiving, guardianship/representation, family pluralism and intimate privacy.
  - Protect against domestic and other private interference through explicit duties,
    evidence, challenge, continuity and remedy. Never infer compelled health, belief,
    relationship, family form or personal outcome from provision.
  - Give caregivers and dependants independent standing and routes to help; neither
    role may erase the other person's voice or floor.
  - Define the one general legal-adulthood status imported by political membership:
    non-discretionary acquisition, accessible evidence, challenge, correction, and
    continuity when evidence is missing or disputed. Add no separate political age,
    maturity test, higher candidacy age, or retroactive loss.

- [ ] **Write the Bodies specification.**
  - Constitute the ratified People's Assembly, Regions Council, Executive Council
    and public administration, non-executive Civic President, ordinary courts,
    Constitutional Court, electoral administration, audit/integrity,
    ombudsperson/rights advocate, and appointments-qualification function. Complete
    provision/treasury, regulators, justice/appeal, and regional/local cards without
    silently relabelling current fixtures as those institutions.
  - Separate in every card: universal human standing; political membership;
    franchise; candidacy; current office; current lawful power; and permanent
    historical public answerability. Reserve `standing` for universal personhood
    and rename chapter 2's official-status sense to public or historical
    answerability.
  - Give every office a democratic/legal source, jurisdiction, ordinary function,
    delegation boundary, conflict/recusal rule, appointment, removal, succession,
    temporal status, public-reason duty, and a typed challenge, review, audit or
    political-accountability route. Require appeal and remedy for individualized
    adverse determinations; do not recreate a universal right of appeal.
  - Fill the decision's delegated mechanics before formal enactment: Assembly
    term/vacancy/early-election source; Council delegation tenure/instruction/
    replacement; Executive composition/replacement/incapacity; presidential
    selection fallback/alternate/removal; and court/oversight seats, selectors, and
    vacancy fallback. Stay inside the ratified anti-capture and continuity limits.
  - Give elections, office terms, caretaker limits, succession, and record/office
    transfer their own source-bound temporal contracts. Custody T3 is not reusable,
    and a legal duty to call an election is not proof that a clock advances or the
    election occurs.
  - Census every producer and consumer before deciding whether to retain, replace,
    or retire `mature`, `decide`, `choose`, `broken`, `approves`,
    `authority`, or any current institutional constant and its floor-debt,
    credential, judgment, permission, or custody route.
  - Before a state-form rule family lands, audit chapters 2, 3, 9, 12, and 13,
    chapter 13's counted-claim guard, every additional census-found chapter, the
    temporal case,
    Part V's rotation/State verdicts, and `method.md`.
  - Apply separation of functions: no actor may assert case facts, decide their
    consequence, execute it, audit it, and remedy it alone. Show every body doing its
    ordinary job as well as being checked.
  - Define a rights advocate able to act without replacing the voice of a child,
    disabled person, prisoner, newcomer, dependant or unregistered claimant.

- [ ] **Specify obligations without making rights reciprocal bargains.**
  - Public institutions must respect, protect, fulfil, continue and remedy.
  - Contractors remain bound when delivering a public function. Direct private
    duties must be express, never inferred merely from the domain's subject matter.
  - Civic duties may exist, but failure to work, pay, identify oneself, comply, or be
    socially approved must not remove a basic floor.
  - Separate duties owed to a person, duties owed to a common, role duties, and
    voluntary commitments; define priority, conflict, excuse and remedy without
    turning rights into reciprocal bargains.

- [ ] **Specify delivery as a lifecycle.**
  - Model: entitlement → service offered → accessible service → authorised,
    recipient-side access/receipt evidence → disputed/failed → interim continuity
    → remedy → corrective control implemented → recurrence monitored over a declared
    horizon. No finite record can verify all future non-recurrence.
  - Apply the lifecycle across food, water, housing, utilities, health/care,
    learning/information, mobility, communication and other essential systems.
  - A missing receipt must invite outreach and challenge, never terminate entitlement.
  - **Book 2 handoff:** staffing, procurement, budgets, logistics, enforcement,
    routing, maintenance, capacity planning and graceful degradation.

- [ ] **Write the economic, labour, property, and fiscal constitution.**
  - Specify lawful taxation, appropriation, spending, borrowing and audit authority;
    floor financing; property/land as a conditional liberty; possession, use,
    transfer, inheritance and expropriation; work, workplace safety, unions,
    collective action; enterprise/co-operatives; contract and consumer protection;
    competition, monopoly and economic concentration; money, credit, debt and
    insolvency interfaces.
  - Let democratic choices determine rates, institutional mix and policy above the
    floor. Book 2 owns budgets, monetary/fiscal models, production, pricing,
    allocation, staffing and capacity.
  - Formalise the budget-deadlock default: only the constitutionally enumerated
    prior essential authority and protected floor continue, with public basis,
    independent audit, expedited review, and a source-bound end. It creates no new
    programme or permanent spending power; Book 2 must demonstrate operational
    capacity.
  - Preserve the no-earned-floor and no-score walls. Wealth, contribution,
    recognition and market success may not buy superior standing, public authority,
    political weight, or immunity from commons and liberty limits.

- [ ] **Define income security and social insurance without making survival
  contributory.**
  - Cover illness, disability, unemployment, caregiving, workplace injury, ageing,
    survivor support and pensions; portability across employers, family forms and
    jurisdictions; accessible claim/challenge routes; continuity; and insolvency.
  - The unconditional floor remains non-contributory. Democratically chosen
    contribution histories may affect transparent above-floor benefits only under
    equality, adequacy, privacy, appeal and anti-poverty guards; they never alter
    standing, emergency help or the floor.
  - Book 2 owns actuarial/fiscal assumptions, reserves, take-up, administration and
    shock testing. Book 1 owns the lawful interface and anti-exclusion limits.

- [ ] **Authorize qualifications, licensing, compensation, and positive incentives
  without ranking people.**
  - Permit evidence-based competence requirements for safety-critical or fiduciary
    roles such as clinician, pilot, judge, engineer or auditor. Separate role
    eligibility from personhood, floor and political standing; require accessible
    routes, proportionality, expiry/review, challenge and portability.
  - Permit fair above-floor compensation and democratically bounded incentives for
    difficult work, skill, innovation, investment, maintenance and public service.
    State the source, recipient, purpose, limit, conflict rule and audit; no reward
    may purchase authority, impunity, a higher floor or a personal-worth score.
  - Test credential cartels, inherited advantage, scarcity rents, favoritism and
    metric gaming. Recognition remains optional, binary and non-operative.

- [ ] **Constrain concentrated private and hybrid power.**
  - Complete contract cards for employers, landlords, lenders, insurers, utilities,
    corporations, platforms, monopolies and public contractors where essential
    function, dependency, lock-in, information asymmetry or lack of meaningful exit
    creates public-scale power.
  - Rule direct duties expressly; define evidence, transparency/privacy,
    non-discrimination, contestability, independent review, continuity and remedy.
    Do not constitutionalise harmless voluntary life merely because it is private.

- [ ] **Define the democratic ceiling and majority process.**
  - Ordinary majorities decide policy, tax mix, providers, public/co-operative/
    private institutional mix, and choices above the core; the protected free field
    remains neither a public programme nor a plebiscite.
  - Implement residence-first membership: ordinary residence plus the one general
    adulthood status gives equal franchise and candidacy at one claimant-chosen,
    nested political home. Registration is evidence, not source; citizenship adds
    no weight; custody, institutional placement, eviction, and forced displacement
    do not move the home; conviction or custody removes neither vote nor candidacy.
  - Transfer homes atomically, preserve the last uncontested home during dispute,
    give first-time residents a guarded provisional status, and admit at most one
    person-bound effective submission per decision across jurisdictions.
  - Require proportional People's Assembly outcomes and independent administration;
    keep the Regions Council's equal territorial weight confined to its limited
    federal role and one-time ordinary-law return. Implement constructive no
    confidence and single-holder constructive recall without an avoidable vacancy.
  - Current `approves(Electorate, amendment)` names the electorate but authenticates
    neither writer, roster, tally, certificate, recount, challenge, nor correction.
    Require an authenticated, contestable result with an exact attested roster,
    separate external completeness assurance, person-bound submissions, alternate
    writers/reviewers, and correction. Nibli cannot infer a complete population
    from a supplied finite roster.
  - Implement the ratified amendment route: two-thirds of the full Assembly and
    more affirmative than negative valid national referendum votes, no turnout
    quorum, and failure on a tie; add a full-weight Council majority for directly
    regional changes and the same valid-vote consent in each affected region for
    competence/boundary changes. An elector initiative can force an Assembly vote
    but cannot bypass two-thirds.
  - Bound direct ordinary-law initiatives by compatibility review and the
    deterministic initiative/counterproposal default. Silence cannot approve a
    proposal, while a missing reviewer must have a limited alternate route.
  - Every restrictive proposal needs public reasons, evidence,
    non-discrimination, least-restrictive means and a typed constitutional,
    judicial, administrative, audit or political challenge/review route. Require
    delivery/continuity duties where a floor is affected, and appeal/remedy for an
    individualized adverse determination. Capacity modelling remains Book 2;
    election, term, caretaker, recall, succession, and transfer time each need a
    source-bound T3 contract. Prove legal effect only from supplied time evidence;
    do not claim Book 1 advances clocks, publishes records, forms governments, or
    causes elections.

- [ ] **Protect democratic and administrative integrity.**
  - Cover electoral systems, parties and opposition, districting, campaign finance,
    political advertising, lobbying, gifts, procurement, public appointments,
    patronage/nepotism, conflicts of interest, revolving doors, corruption and
    coordinated information manipulation.
  - Define permitted writers and money/influence records; proportionate disclosure
    and privacy; independent election, procurement, ethics and anti-corruption
    oversight; recusal, challenge, correction, remedy and disqualification; and
    institutional independence from the governing coalition.
  - Implement open nominations, reasoned qualification review, divided selectors,
    staggered nonrenewable mandates, cause-only removal, and the legal
    incompatibility of majority appointment control by one current government,
    chamber, party coalition, profession, or appointing source. Make direct and de
    facto concentration detectable, challengeable, correctable, and unable to use
    vacancy or reviewer silence as a withholding veto.
  - Test capture through legal form, shell actors, third parties, media/platform
    concentration, selective enforcement, audit starvation and manufactured
    withholding. No integrity body may certify its own decisive facts and final cure.

- [ ] **Constitute official statistics and planning information without building a
  population score.**
  - Authorize censuses, representative sampling, administrative statistics and
    public planning data only with necessity, purpose limits, minimization,
    accessibility, privacy, correction, independent methodology and publication.
  - Separate aggregate planning evidence from individual eligibility and
    enforcement. Test non-response, undercount, classification harm, political
    manipulation, re-identification, stale data and suppression of adverse results.
  - Book 2 owns collection operations, secure linkage, calibration and uncertainty;
    Book 1 owns authority, non-use walls, contestability and public accountability.

- [ ] **Build amendment enactment and effective-version assurance outside the
  reasoning engine.**
  - Bind exact base/candidate byte identity and bounded semantic effects to the
    ratified lawful result: two-thirds of the full People's Assembly, national
    valid-vote majority with no turnout quorum and tie failure, plus a full-weight
    Regions Council majority and each affected region where the federal settlement
    requires them. Keep corridor compatibility separate from political consent.
  - Distinguish proposal, submissions, tally, review, certificate, publication,
    uniquely effective deployment, and later rollback/supersession. The current
    amendment audit manually applies candidates and proves only named bounded
    consequences.
  - Book 1 defines the constitutional source, proposal, result, challenge,
    independent review, successor/conflict/replay and remedy contract. A host harness
    and Book 2 must authenticate digests/signatures, store and publish versions,
    select/deploy the effective source, preserve rollback evidence and launch fresh
    reasoner sessions against that exact version.
  - Test stale base, replay, divergent candidates, conflicting approvals,
    withholding veto, unauthorised vocabulary change, semantic mismatch, rollback
    and query against the wrong source. Nibli may reason about supplied version facts
    but may not be credited with authenticating or deploying them.

- [ ] **Complete territory, membership, mobility, plurality, and external relations.**
  - Formalise the ratified federal settlement: enumerated common powers, regional
    residual authority, the protected local minimum, justiciable subsidiarity,
    equalisation, portability, and a competence-dispute route that cannot acquire
    power through delay.
  - Formalise residence-first political membership independently of human standing:
    factual ordinary residence, claimant choice among genuine homes, one nested
    political home, atomic transfer, last-uncontested-home continuity, guarded
    provisional status, and no move caused merely by custody, institutional
    placement, eviction, shelter use, or other compelled displacement. Citizenship
    adds no electoral weight.
  - Cover newcomers, migrants, refugees, stateless people, borders, asylum,
    expulsion, extradition, minority/indigenous self-government and language access.
  - Preserve a former resident's return right without creating a nonresident ballot.
    The later migration/external-power work owns accessible evidence and border
    operation, not the right's existence.
  - Treat the negotiated internal secession path as settled here. The still-gated
    external-power work owns recognition, defence, cross-border status,
    international obligations, and post-exit effects; it may not replace the
    affected-region vote, federal agreement, rights/minority review, settlement, or
    final affected-population ratification.
  - Define authority and non-derogable limits for treaties, diplomacy, external
    trade, war/peace and humanitarian duties. Prevent public procurement, investment,
    trade or corporate form from exporting labour exploitation, ecological damage
    or rights violations that would be unlawful at home. Other states' cooperation
    and supply-chain facts remain external assumptions, not derived facts.

- [ ] **Add the missing non-carceral justice interface.**
  - Cover notice, counsel/advocacy, hearing, challenge, reparation and enforcement
    across civil, administrative, family, labour, consumer and constitutional
    disputes as well as criminal justice.
  - Separate investigation/policing, prosecution, defence, adjudication, execution
    and review. Add victim/survivor protection, restitution, reparation, restorative
    options and least-coercive response without compelling forgiveness.
  - Add explicit carceral limits: bodily integrity, communication, conditions,
    proportionality, release review, post-release continuity and reintegration.
    Prison remains the hardest stress test, not the default social case.

- [ ] **Complete emergency, resilience, public-safety, and defence interfaces.**
  - Define disaster/public-health triggers, declaring and reviewing bodies,
    cross-branch control, non-derogable protections, public reasons, necessity,
    proportionality, source-bound duration/renewal/end, challenge and remedy.
  - Put policing, intelligence, force and defence under legality, civilian control,
    role separation, evidence, oversight and repair. Do not borrow the custody T3
    contract for a different power.
  - Book 1 states invariant and failure behavior; Book 2 owns incident command,
    stockpiles, force/logistics, infrastructure restoration and actual capacity.

- [ ] **Govern ecology, commons, non-human animals, and future conditions.**
  - Define present duties, evidence and enforceable ceilings for climate, air, water,
    soil, biodiversity, land, resource extraction, waste and shared infrastructure;
    restoration, non-regression and liability; and cross-border/common governance.
  - Give every present person standing and an independently checked public guardian
    authority to protect future conditions without pretending to receive facts from
    unborn people. Define the guardian's evidence, independence, removal, conflict,
    challenge and remedy contracts.
  - State minimum protections for non-human animals, including welfare, habitat,
    permitted use and enforcement, without pretending that personhood is the only
    possible basis for protection. Book 2 owns measurement, resource budgets,
    transition and ecological feasibility.

- [ ] **Protect knowledge, communication, culture, and the free social field.**
  - Cover learning and information access; expression, conscience, religion and
    non-belief; association; media/press plurality; academic, scientific and
    artistic freedom; language/accessibility; public information; sport, leisure,
    friendship, love, mutual aid, clubs and voluntary creation.
  - Secure the conditions and liberties for these activities without certifying
    official truth, taste, belief, creativity, relationship or personal fulfilment.
  - State residual freedom expressly: private/civic life remains free unless an
    evidenced rights or commons harm justifies a least-restrictive, reviewable rule.

- [ ] **Constrain records, surveillance, and automated power across every domain.**
  - Extend the record contract to identity/status, health, care, education,
    workplace, housing, finance, policing and public-decision records.
  - Cover surveillance, biometrics, profiling and automated/AI-assisted decisions:
    authorised inputs, purpose limits, privacy, explanation, contestability,
    correction, human/independent review, non-use walls, retention/deletion and
    remedy.
  - Technology, storage and algorithms remain Book 2 operations or external
    evidence. A computed output is never a constitutional oracle.

### Expansion phase 3 — Make the architecture elegant without making it false

- [ ] **Name the real symmetries and necessary asymmetries.**
  - Real recursive interfaces:
    - right → duty → accessible delivery → breach → continuity → remedy → review
      → corrective control → monitored recurrence over a declared horizon;
    - power → lawful source/trigger → evidence → limit → public reason → independent
      review → appeal → correction/end;
    - harm → notice/voice → due process → least-coercive response → repair/release;
    - democratic choice → authenticated mandate → bounded implementation → public
      feedback → challenge → correction or peaceful replacement.
  - Necessary asymmetries:
    - recognition is optional, binary, non-ranked, and non-operative;
    - punishment is coercive and requires a higher proof threshold;
    - public power is presumptively reason-giving and auditable subject to
      narrow lawful confidentiality, while private life is presumptively private;
    - accessibility may require unequal resources to secure equal standing;
    - children, dependants and people needing support retain rights without symmetric
      capacity or contribution duties.

- [ ] **State the determination/action boundary accurately.**
  - Book 1 must identify who owes what, what counts as ordinary lawful function,
    delivery, failure, continuity, remedy, public accountability, and protected
    freedom from direction.
  - Book 2 must specify how people, institutions, funding, resources, technology and
    real-world operations make those duties happen and how the system degrades under
    scarcity or shock.
  - Do not describe an infinite chain of duties as action, an interface as capacity,
    a simulation as deployment, or an external premise as a constitutional fact.

- [ ] **Use a vector of protected conditions, never a total social score.**
  - No abundance in one domain compensates for torture, homelessness, exclusion,
    disenfranchisement, ecological destruction or loss of standing.
  - Use aggregate, privacy-preserving disparity, capacity and outcome measures for
    public learning; never convert them into individual worth or risk labels.
  - Record trade-offs and Pareto/conflict boundaries openly; do not collapse
    heterogeneous floors, liberties, commons and democratic choices into one number.

- [ ] **Define cross-domain priority, conflict, and physical-scarcity rules.**
  - Distinguish genuine physical/capacity scarcity from monetary or administrative
    withholding. Rule transparent triggers, admissible evidence, interim continuity,
    equal standing, need/accessibility considerations, least-harm allocation,
    challenge, review, end and repair; never use wealth, merit, contribution,
    recognition or political favour.
  - Resolve conflicts through typed rules rather than hidden priority: property
    versus floor/commons, expression versus evidenced harm, privacy versus public
    accountability, local choice versus portability, current claims versus future
    conditions, and emergency action versus non-derogable protections.
  - Route the unresolved normative allocation choices back through the author gate
    and democratic corridor; do not let implementation code decide them silently.

- [ ] **Test compositional closure and graceful degradation.**
  - For formal interfaces, prove within the declared model that individually safe
    domains remain safe when joined; test quantitative, dynamic, empirical,
    operational and lived compositions through their assigned assurance routes.
    Search for duty cycles, contradictory writers, duplicated final authority, veto
    by withheld evidence, remedy loops, unbounded delegation and cross-domain routes
    that recreate a forbidden score or status gate.
  - For normal operation and each compound shock, state what continues, what narrows,
    who may decide, who is protected first, what cannot be suspended, how review
    arrives, and how ordinary authority is restored.
  - A bounded safety proof may not claim that people, clocks, supplies, institutions
    or other states actually act. Assign every liveness premise to Book 2 or an
    external assurance owner.

- [ ] **Red-team incentives, capture, and strategic behavior across the composed
  society.**
  - Test capture, collusion, rent-seeking, bribery, patronage, regulatory arbitrage,
    strategic withholding/misreporting, Goodhart effects, adverse selection, moral
    hazard, free-riding, black markets and burden-shifting into another domain or
    jurisdiction.
  - For every mechanism state who benefits from gaming it, the information and
    coordination required, who bears the hidden cost, how it is detected/challenged,
    and whether the response creates a new veto, surveillance system or score.
  - Nibli may test legal walls; quantitative models, games/simulations, empirical
    evidence and Book 2 operations test behavior and scale. Do not assume either
    universal selfishness or universal altruism.

### Expansion phase 4 — Build a reliably balanced non-specialist reader experience

- [ ] **Build a reviewed reader-experience coverage ledger before rewriting.**
  - For every derived chapter and substantive Part V passage record: social domain
    and rule family; normal function and protective/corrective function; setting;
    person posture (chooses, creates, cares, works, associates, requests, receives,
    challenges, governs, or is acted upon); trajectory (works, contested, fails,
    continuity/remedy, unresolved); roles/life stages/access conditions; and exact
    rule/fact/pin or exempt-source basis.
  - Generate the report as a projection of the canonical full-society source and
    fail verification on an unclassified passage or a completed constitutional row
    with no reader-facing mapping. Counts may appear in the generated audit, never
    as hand-maintained prose claims.
  - **Done when:** every completed governed/provided domain has traceable ordinary-
    operation, credible failure/abuse or boundary, and—where claimed—end-to-end
    continuity/remedy cases in its assigned assurance route. Use Nibli pins for
    formalized legal claims; use reviewed specifications, quantitative/dynamic
    models, operational evidence or lived-experience methods for their assigned
    claims. A protected private/civic domain needs traceable non-interference and
    non-recording/non-compulsion limits plus recourse; ordinary-life illustration
    remains non-evidentiary under the author-ruled narrative register. A non-justice
    domain represented only through prison or custody fails.

- [ ] **Rebalance the pinned case portfolio without fictionalising it.**
  - Preserve the prisoner as the hardest stress test, not the default inhabitant.
    Cover ordinary provision and care; family/dependency; learning and knowledge;
    work/property/exchange/commons; association, conscience and creation;
    voting/deliberation/local government; mobility/newcomer portability; civil
    dispute/repair; emergency continuity; and institutional correction.
  - For every public body show one lawful ordinary function and one accountability
    path. For every materially operative role/status, pin equal standing/floor or
    the exact lawful distinction.
  - No role may appear only as an object of intervention when the constitution gives
    it agency. Do not add decorative demographic labels or pretend a full Cartesian
    product is meaningful; use reviewed pairwise/high-consequence coverage.

- [ ] **Add a Reader’s Map inside an existing exempt element.**
  - State the promise, five-layer society map, record/rule/reality distinction,
    this volume's destination/operation boundary, visible part structure, and why
    the prisoner is a stress test before Chapter 1. Preserve the settled single
    Book 2 pointer at the end; explain the earlier scope boundary without adding a
    second pointer.
  - Preserve computed chapter order; make the reader-facing arc visible rather than
    casually reordering the derivation spine. If the generated spine remains
    carceral after the constitution broadens, treat that as a model finding, not a
    cosmetic ordering problem.

- [ ] **Use constructive, private/civic, democratic, and coercive chapter patterns,
  not one failure-first formula.**
  - Constructive provision: person seeks a floor → body/duty responds → accessible
    receipt/effect → challenge if needed → continuity/remedy → boundary.
  - Protected private/civic agency: person chooses, creates, associates, cares or
    cooperates without permission → non-interference and enabling conditions →
    narrow evidenced-harm rule if applicable → recourse against interference.
  - Democratic/co-operative agency: people deliberate and organise → authenticated,
    bounded collective choice → implementation → feedback, challenge and peaceful
    correction/replacement.
  - Coercive/protective rule: power is proposed → lawful trigger/evidence → limit
    → independent review/appeal → correction/end → boundary.
  - Show the rule working before or beside its strongest credible failure. Do not
    force an attack section where the rule family supports no such claim.
  - Prefer chapter-local reminders to long backward cross-references. Preserve the
    record-people's deliberately flat inner lives; do not invent biographies,
    emotions or composite citizens as evidence.

- [ ] **Add accessible navigation and visual explanation.**
  - Provide an annotated table of contents, concise glossary, role/body and case
    indexes, domain-to-chapter map, and selected diagrams for the five layers,
    record/conclusion distinction, floor, democratic corridor, institutional roles,
    functional dependencies and delivery/remedy loops.
  - Every diagram needs a complete prose equivalent; no meaning may depend only on
    colour, layout, vision, hearing, fine motor control or specialist notation.
    Check semantic headings/navigation and screen-reader, EPUB, HTML and PDF paths.
  - Readability formulas are diagnostic flags, not truth or pass/fail targets. Each
    visual must earn its cognitive and accessibility cost.

- [ ] **Run pre-registered reader-comprehension and balance sessions.**
  - Pre-register questions, coding rubric, sample and pass rule; run a pilot, revise,
    then use a fresh holdout of non-specialists with varied reading confidence,
    language backgrounds and accessibility needs. Treat this as usability evidence,
    not population statistics.
  - Include unaided prompts: What do people do in ordinary life? What may they
    choose privately and democratically? What do public bodies do when nothing has
    failed? How does something owed arrive and get repaired? Why is the prisoner
    present? What remains operational or externally assumed, and what can no model
    guarantee?
  - Obtain informed consent; permit withdrawal; minimize and protect data; provide
    accessible participation and fair compensation; prevent retaliation; add trauma
    safeguards where coercive experience is discussed; and use independent ethics/
    safety review where appropriate. Reader evidence never purchases authority over
    the people studied.
  - A pass requires readers to identify constructive functions as well as restraints,
    trace one successful delivery/remedy path and one democratic choice, and
    recognise the prisoner as a stress test. Apply the pre-registered,
    severity-weighted misconception rule ratified by the author after the pilot; no
    aggregate score may hide a core failure. Revise, then use a fresh holdout.

### Expansion phase 5 — Evidence, psychology, and external review

- [ ] **Apply claim-type-specific scientific, statistical, formal, and normative
  discipline to every expansion.**
  - Empirical/descriptive claims need traceable data or primary sources, measurement
    definitions, representativeness limits and uncertainty. Causal claims also need
    an identification strategy, plausible alternatives and sensitivity analysis.
  - Predictive/feasibility claims need calibration, baselines, held-out or robustness
    tests, sensitivity to the reference envelope and explicit falsifiers. Formal
    claims need definitions, executable proof or derivation where applicable,
    countermodels/adversarial cases and a precise scope boundary.
  - Normative claims need stated values, alternatives, trade-offs, dissent and the
    lawful author/democratic decision owner; citation can inform but cannot prove a
    value choice. Psychological/lived-experience claims need ethical methods and may
    not be inferred from a formal or administrative record.
  - Pre-register acceptance criteria where feasible; publish code, data, provenance,
    sensitivity tests and null/negative results subject to privacy and licence. Use
    group-level outcomes for institutional repair, never individual worth.

- [ ] **Ground psychological claims without turning people into variables.**
  - Test for autonomy, voice, non-humiliation, relatedness, meaningful control,
    retaliation, status competition, coercive incentives, learned helplessness,
    trust, care burden and the effects of being watched or scored.
  - Use lived-experience review across ordinary and coercive institutions; do not
    infer psychology, wellbeing or compliance from a formal proof or service record.
  - Protect refusal and exit where compatible with others' rights; conditions may be
    secured, but belief, eating, learning, treatment, relationship and fulfilment
    may not be compelled or certified.

- [ ] **Run a multidisciplinary and lived-experience red-team before completion.**
  - Include constitutional law, public administration, disability/accessibility,
    public health, care/childhood/ageing, labour and enterprise economics, consumer
    and civil justice, policing/prison, media/science/culture/religious pluralism,
    local/migration/indigenous governance, defence/foreign affairs, infrastructure,
    ecology, data/AI governance, quantitative modelling and people directly affected
    by the relevant institutions.
  - Ask each reviewer to identify omitted domains, unowned dependencies, hidden
    liveness assumptions, private-power blind spots, impossible operations,
    totalising rules and narrative distortions. Every finding is fixed,
    classified out with reasons, or retained with severity, consequence, owner,
    closure condition, and public-claim limitation. The named severity owner
    applies the declared rubric and an independent checker reviews it. A critical
    unresolved finding applicable to a gate's permitted claim blocks that gate;
    “disclosed” is not “safe”.

### Explicitly rejected expansion proposals

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
  or implementation logistics as Book 1 prose unless the author replaces the current
  seam. The destination may specify complete functional interfaces without pretending
  to staff, fund, build or deploy them.
- Treating exhaustiveness as permission to regulate every harmless private practice.
  Unauthorised public power fails closed; unclassified harmless private life defaults
  to freedom.
- Asking Nibli, a spreadsheet, a simulation, an empirical registry, or a reader study
  to prove the domains assigned to the other assurance methods.
- Declaring narrative balance from word counts, sentiment, demographic decoration or
  a fixed prisoner/non-prisoner quota without reviewed context and reader evidence.

### Expansion completion standard — cumulative gates, not one finish line

These gates are cumulative but not interchangeable. The author-ratified
2026-08-07 boundary fixes the two-book seam, C-then-E publication sequence, and
versioned closure; `new-book-plans/full-society-boundary-decision.md` controls.
Gates D and E are project-level reference gates whose executable work lives only
in `book-2/TODO.md` after Book 1 — First Edition ships at Gate C. A later formal,
operational, or reader test cannot substitute for an earlier missing condition.

#### Gate A — Scope and assurance foundation

- the canonical source covers every material domain, role, power, dependency,
  scenario and claim, or visibly classifies it out with reasons;
- all projections regenerate from that source; unresolved items carry severity,
  consequence, owner and closure condition, and critical gaps block the affected
  claim;
- the versioned reference envelope, assurance allocation, stopping rule and
  decision briefs are reviewable; and
- independent scope reviewers can propose no omission that is neither added,
  classified out nor retained as an explicit severity-rated limit.

**Artifact and permitted claim:** the map and test program may be public, but no
book preview, release candidate, or edition may publish. The project has a
versioned, reviewable map and test program; it has not yet described or operated
a complete society.

#### Gate B — Expanded Book 1 constitutional/social destination

- every applicable right, liberty, public function/power, expressly bound private
  power, record and commons condition has a complete contract card, owner,
  adversarial case, counterfactual and accurate reader account;
- every floor has unconditional accessible delivery, recipient-side access/receipt
  evidence, continuity, remedy and corrective-control interfaces without pretending
  Book 1 supplies capacity;
- every public body performs an ordinary function and is independently checked; the
  democratic corridor and residual private/civic free field are explicit; and
- domain journeys, collisions and shocks establish the claimed constitutional
  invariants, lawful narrowing, challenge, restoration and model boundaries, with no
  critical constitutional, equality, safety or hidden-power gap.

**Artifact and permitted claim:** immutable Book 1 — First Edition previews may
publish under P1 after Gate B and their snapshot-specific gates pass. A preview
may say that it describes a comprehensive, versioned constitutional and social
destination for its declared scope. It may not claim reader suitability,
staffing, resources, feasibility, deployment, outside liveness, or an operational
society.

#### Gate C — Book 1 reader and public-edition readiness

- the full verifier, generated closure/reader audits, adversarial cases,
  accessibility checks and multidisciplinary/lived-experience red-team pass;
- each governed/provided domain has applicable ordinary-success, failure and
  recovery coverage; each protected private/civic domain has agency,
  non-interference, evidenced-harm and recourse coverage; and no non-carceral domain
  is explained only through prison, punishment or institutional failure;
- a fresh holdout passes the author-ratified, pre-registered comprehension and
  balance rule without an aggregate score hiding a core misconception; and
- readers can identify normal functions, freedoms, democratic choices, guarantees,
  remedies, Book 2 dependencies and external assumptions without reconstructing them
  from scattered chapters.

**Artifact and permitted claim:** publish Book 1 — First Edition, its assembled
digital artifacts, and its first Book 1 POD atomically under one provenance and
Gate C closure record. The cumulative Gate B destination passed the declared
accessibility and balance protocol for the tested sample; the evidence supports
suitability for the declared audience within stated sampling and method limits.
It is evidence about the book, not proof that the society is operational. If any
matching source, artifact, POD identity, provenance, or Gate C record fails, the
public object remains a preview and Book 2 does not activate.

#### Gate D — Book 2 operational model

- every Book 1 interface has a costed, staffed and accountable operator/model, a
  visible external assumption, or “Book 2 operation not applicable” where the
  protected condition is non-operation/non-interference; any recourse operation is
  mapped separately, and the reference envelope is calibrated and versioned;
- all applicable operational domains in the canonical generated set—including
  material/care, economy, equality/life course, democracy/integrity/statistics,
  justice/safety/defence/external relations, ecology, knowledge/free life, records/
  technology, transition, gameability and reader experience—meet their
  pre-registered adequacy, accessibility/equity, continuity, resilience,
  sustainability and fiscal/resource-feasibility thresholds in ordinary and
  declared shock cases;
- the Book 2 reader/lived-operation view covers ordinary agency,
  maintenance, failure/degradation and recovery and passes its declared
  comprehension/balance protocol for the tested sample;
- models publish code/data, uncertainty, sensitivity, negative results, capacity
  and failure boundaries; simulations and pilots state external-validity limits; and
- any unresolved critical floor, equality, safety, capacity, feasibility,
  hidden-power or cross-domain dependency gap blocks the affected operational claim.
  A non-critical residual needs severity, consequence, owner, closure condition and
  an explicit public-claim limitation.

**Artifact and permitted claim:** only immutable Book 2 — First Edition previews
or release candidates may publish. Book 2 may say that it supplies a reproducible
operational design within the named envelope. It may not publish Book 2 — First
Edition or claim deployment, generalisation beyond the envelope, or an integrated
functional society.

#### Gate E — Integrated two-book full-society claim

- every guarantee and democratic choice crosswalks to its operational path and
  back; each private-freedom boundary crosswalks either to enabling/recourse
  operations or to an explicit non-operation/non-interference disposition;
  constitutional rules survive operational scarcity and operations respect floors,
  liberties, equality, democracy, privacy and commons;
- cross-domain journeys and compound shocks pass their declared safety, continuity,
  recovery and feasibility gates with no hidden critical assumption;
- an integrated reader test can identify ordinary life, agency, maintenance,
  constraints, failure and recovery across both books without reducing Book 2 to a
  crisis/cost manual; and
- independent constitutional, operational, scientific, lived-experience and
  accessibility reviewers can reproduce applicable analyses, audit provenance and
  methods for non-reproducible evidence, and identify residual limits.

**Artifact and permitted claim:** atomically publish Book 2 — First Edition and
an immutable integrated release manifest pairing the exact compatible Book 1 and
Book 2 editions, artifact hashes, canonical-source version, reference-envelope
version, assurance and review records, external assumptions, and residual limits.
If the pairing, integrated checks, or manifest fails, Book 2 remains a preview or
release candidate. Only Gate E permits the bounded claim that the exact paired
editions model a fully functional society for the declared reference envelope.
The claim remains versioned, falsifiable and open to the stopping rule; it never
means successful deployment, timeless completeness, prescription of every
harmless private life, or control of every external condition.

---

## book-1 — remaining work

- **Parts I–IV second expansion wave — DONE 2026-08-03, with its stop.** Ruled
  content-governs (the ~38,000 target retired; CLAUDE.md's length entry carries the
  ruling) and swept all fourteen chapters. Outcome, measured the same day: chapters
  1–14 went **29,440 → 35,071** words across 24 commits, against 10,722 non-derived —
  majority-derived holds at roughly three quarters. The retired target was approached
  from below by material rather than aimed at, which is the only way this wave would
  have accepted reaching it.
  - **The stop-map, checked 2026-08-03.** Thirteen chapters took new material. **13 is
    dry and was declined on the merits, not skipped**: its two candidate sharpenings —
    that the time words are refused at the door rather than merely unused, and that
    release has the shape it has because derivation only ever adds — were read against
    the chapter and judged already covered by its existing passage, so writing them
    would have been padding against the wave's own rule. Start a third wave elsewhere.
  - **Four fidelity corrections landed first**, because wrong prose outranks untold
    prose: chapter 1 listed "a date" among what the record holds; chapter 5's bolded
    headline read "judge your family" over a rule reading parenthood alone; chapter 8
    claimed a mark was "the only form the design allows"; chapter 14 claimed the audit
    "cannot be gamed from below" when it can be starved. A fifth was found by
    measurement mid-wave and folded into chapter 6.
  - **The wave corrected the constitution, not only the book.** Chapter 8's planned
    passage rested on a margin note claiming that threading the universal into a floor
    line fakes delivery for everyone "while every entitlement pin stays green".
    Measured before writing: it fabricates no actuality and instead deletes the
    entitlement — the opposite failure, and the guard is the entitlement pins, not the
    actuality ones. Note corrected, all six fixtures regenerated. Nothing checked that
    comment, which is why it rotted.
  - **The adversarial pass earned its place and then some.** Two checkers over the
    whole wave diff returned twenty-two findings, and seven were factual errors in new
    prose — most importantly that a voiding does not take the pen (the credential
    rules read the carried mark, never the current voiding, which is the design's own
    disclosed exploit), that a recall does not strip a seat, and that the record does
    hold a word for intent. Three correction commits landed before this close. **Do
    not skip this pass on a future wave**: per-commit gates cannot see cross-chapter
    drift, and every one of the seven had passed its own chapter's full suite.
  - **Two commit bodies carry word counts off by a little** (chapter 3 says 2,652 for
    2,651; the method addendum says 4,255 for 4,270) because the count was composed
    before the final edit. The figures above are the authoritative re-measurement;
    pushed bodies were not rewritten.
  - **Process notes worth keeping.** Two gates failed for a reason that was not the
    prose — editing another chapter's files while a full run was in flight breaks the
    cross-file pin reconciliation, so gate strictly serially. And the two-second
    `--quick` prose pre-check before each five-minute full run caught three violations
    in this wave at a fortieth of the cost; the counted-claims gate stopped "one thing"
    twice more, which is now four times across two waves.

- **Add `LICENSE-MIT` + `LICENSE-APACHE` — now unblocked.** The condition ("when the
  harness and fetchers are written") is met: `registry/check.py`,
  `registry/fetch/worldbank.py` and `new-book-plans/6-claim-table.py` exist, the first
  two already carrying `SPDX-License-Identifier: MIT OR Apache-2.0` headers. Fetch both
  canonical texts (per `LICENSING.md`), mirror nibli's layout, and add the SPDX header
  to `6-claim-table.py` and `verify.sh` in the same commit.

---

## Reach — delivery and edition boundary ruled 2026-08-04

The ratified policy is E2 + P1 + D2, refined on 2026-08-07 by the two-book,
C-then-E, versioned-closure boundary. The current-T0 baseline remains public
source and git history but receives no canonical serialization, assembled
edition, edition tag, or print identity. “Completed expansion” means cumulative
Gate C completion; Gate C publishes Book 1 — First Edition, its assembled digital
artifacts, and its first Book 1 POD without making an operational or integrated
full-society claim.

Building in public survives through P1: coherent expansion milestones may be
published as immutable, tagged previews only after Gate B and their
snapshot-specific gates. They are design snapshots with provisional order, not
editions or final serialization. Constitution and spine freeze may create a
private release candidate, but every public pre-Gate-C object remains a preview.
The controlling publication mechanics are in
[`new-book-plans/book-1-edition-boundary-decision.md`](new-book-plans/book-1-edition-boundary-decision.md);
the gate, claim, and stopping contract is
[`new-book-plans/full-society-boundary-decision.md`](new-book-plans/full-society-boundary-decision.md).

- **Align the current time account before any public expansion snapshot.**
  - Chapter 13's ordinary-language/admitted-fact distinction has landed. Remove
    or narrow the remaining permanent-refusal wording in Chapters 4 and 13 that
    contradicts T3 as a ratified future target.
  - Cross-read Chapters 4, 5, and 13 against one current model: flat snapshots
    have no internal order; epoch carry is an external/manual cross-snapshot
    convention; no current duration or automatic expiry exists.
  - Keep this prose-only correction separate from the ratified T3 implementation
    gate.
    Re-run the relevant prose, claim, and pin checks before publishing a
    snapshot that contains the affected chapters.

- **Implement the ratified E2 + P1 + D2 edition contract.**
  - Do not create a promoted artifact from the current-T0 baseline. Before the
    first expansion preview, audit the root README and opening note for
    unregistered-standing overclaims, and have the author replace the final-page
    publication-order promise with the single permitted, scope-only Book 2
    pointer.
  - Create a machine-readable ordered-input manifest and reproducible assembled
    reader artifacts. A repository archive is not a book artifact: it also
    contains legacy manuscripts, reviews, plans, and verification files.
  - Record an immutable namespaced tag; full book-repository and nibli commit
    SHAs, each verified from a clean tree; the full verification transcript/date;
    registry snapshot; known limits; licences; and artifact hashes. Never cite
    `main`, move a tag, or replace an asset in place.
  - Publish coherent milestones, when useful, only after Gate B and their
    snapshot-specific gates, as immutable tags such as
    `book-1-v1.0.0-preview.1`; preserve superseded previews and mark their order
    provisional. After the expansion freezes, use a private candidate for
    holdout and release checks. Publish `book-1-v1.0.0`, the assembled digital
    capstone, and matching POD atomically only after cumulative Gate C and an
    explicit review-close event pass.
  - Give every version a permanent URL; only `latest` navigation may move. New
    content creates a new version, and withdrawal means visibly disrecommended,
    not silently erased.

- **The site.** A dedicated domain — **registering it is the author's own task**
  — plain, built from the Markdown that already exists; immutable preview
  snapshots during expansion, then final chapters in computed order; the repo
  and the one-command suite linked from the front page. Platforms syndicate
  *from* it: CC-BY means they will copy regardless, so the canonical home must
  name itself.
- **The launch essay. [AUTHOR-GATED]** A standalone distillation for someone who will
  never read the book, carrying the thesis and the honest second half in miniature. *The
  Furnished Prison* is the standing headline candidate. First-person territory: the voice
  protocol applies — the author drafts, sessions edit mechanics only.
- **The method paper.** JURIX/ICAIL/formal-methods-for-law genre: the derivation gate,
  the pin suite, the counterfactual classes, the defect markers — the methodology made
  citable. Coordinate with the method part rather than duplicating it; the paper cites
  the book, the book does not depend on the paper.
- **Make run-it-yourself true as a launch claim.** `verify.sh` and its `--only`
  mode are the core artifact, but the script currently defaults to an adjacent,
  mutable nibli checkout. Supply and test a pinned two-checkout or bootstrap path
  from clean inputs, and publish the exact engine commit; only then say “clone,
  one command, the pins pass.”
- **Print-on-demand for the Gate C-complete expansion only (D2).** A priced,
  well-made
  physical edition of a free text. Quality is the lever and revenue a side
  effect: the typography is canonical because it is first and good, never
  because it is exclusive. Generate it only from the final tagged First
  Edition; put the edition, source commit, licence, print-file identity, and
  errata URL inside every copy, and mint a new version for any changed interior.

---

## Data

The registry (`registry/claims.json`, CC0), its staleness gate and the first fetcher
exist and run inside `verify.sh`; see `registry/README.md`. What remains:

- **The rendering and Part V traceability step — build it beside the first prose that
  cites a registry id.**
  Nothing in book-1's derived chapters may carry a number (the counted-claims gate), so
  value-injection waited for the empirical writing it serves — and Part V now exists:
  its frame and capture joint carry registry-backed numbers as hand-written prose,
  checked against the registry by the landing verification. Build the step beside
  those figures, or rule that Part V's handful stays hand-checked. Do not build past
  its consumers. More fetchers (WHO GHO, OWID, FAOSTAT…) land the
  same way — as entries need them.
  - This task owns point-of-claim traceability: every empirical statement needs its
    registry ID and source; causal language must match the evidence, uncertainty, and
    instrument sensitivity the record supports.

- **Re-cite the ported registry entries against published versions.** The port
  (`dd25b49`) honestly stamped `retrieved: 2026-07` — book.md's own last verification —
  on the legacy entries without re-verifying them, and most of the registry still
  carries that stamp. The sweep the old plan deferred to "as each reference is ported"
  is now due, since the porting is done: work through the pinned entries, check each
  against its source's current published version (the Muralidharan REStat move is the
  model — a working paper that became a journal article), update the entry and its
  `retrieved` date. The Kenya UBI entry carries its own warning: it must not reach
  Part V as a working paper.

- **Add Bregman's 15-hour workweek figure to the registry** when Part V or book-2 first
  cites his proposal — the one claim the research-brief corrections found no error in but
  no registry entry for either.

- **The V-Dem re-derivation is DONE (2026-08-03) — Part V's worked example has its
  numbers and a better third act.** `registry/fetch/vdem_happiness.py` derives
  everything from OWID's CC BY series (V-Dem polyarchy + RoW, WHR ladder, WB GDP);
  three registry entries + snapshot landed; working record at
  `new-book-plans/vdem-rederivation.md`. Robust across instruments: the income-control
  narrowing (partial r ≈ 0.20, was 0.195) and the step pattern (+0.02/+0.59/+1.09 —
  bottom step buys nothing). Changed: the floor claim is **instrument-fragile**, not
  cleanly refuted — it survives the income control narrowed on polyarchy (p = 0.032)
  and dies-or-marginal on the alternative index over the identical sample — so the
  worked example's third act becomes "a verdict that tracks the instrument is not
  citable", which is a stronger methods lesson than the refutation it replaces. Part V's
  frame now runs this arc (landed 2026-08-03); the EIU-era sub-bullets below remain
  the historical working reference. FLAG for the author: `democracy_vs_happiness_144.csv`
  in the repo root (CC0 under the root LICENSE, committed pre-ruling) carries EIU
  index values — same grounds as the registry ruling, worth a look.
  - **Do NOT use the floor claim.** Its headline finding — "democracy behaves like a
    floor on subjective wellbeing", from regressing |residual| on democracy score,
    p = 0.0004, which is exactly how convincing it looks — is the one claim it never
    controls for income, and
    **it does not survive**: adding log GDP gives democracy b = −0.0196, t = −0.91,
    **p = 0.37**, while log GDP itself is b = −0.336, t = −2.53, p = 0.011. Within
    income tertiles the dispersion goes the *wrong* way for the democracy story. The
    compression is income, misattributed. This is precisely the claim book-1 would most
    want to be true — a floor effect, in a book about floors — which is exactly why it
    must not be used. An economist kills it in one regression.
  - **Use the income result instead: it supports the book's real thesis better.** What
    compresses the dispersion of human wellbeing across countries is material provision,
    not the franchise. A book whose floor is material-and-personal guarantees, and which
    deliberately demoted the vote *off* the floor to a rule, just got empirical support
    for exactly that ordering.
  - **Use the step sizes.** Authoritarian → Hybrid buys **+0.16** — nothing. Hybrid →
    Flawed +0.73. Flawed → Full +1.01. Partial democratisation does approximately
    nothing; the gain is concentrated at the top of the scale.
  - Still to do from the ruling: record `demo-happy.txt` in the registry as "prior
    analysis, independently re-derived", with the CSV's provenance pinned: WHR 2025 (2022–2024
    average) merged with EIU 2025, 144 countries matched from EIU's 166 and WHR's 147.

- **Publish the registry with the book, not just in the repo.** The formalism stays
  invisible, so what the reader verifies is the data — which only works if the registry is
  reachable from the page they are reading. Front matter names it and gives the URL, every
  figure in the prose resolves to a registry id, and the registry ships CC0. This is the
  thing that earns the trust and the honest substitute for showing the constitution.

---

## Legacy harvest — before `book.md` and `manifesto.md` are deleted

- **Delete both files, in one commit, with the harvest manifest in the body.** The
  harvest gate is fully discharged as of 2026-08-03: the 55 references
  (`registry/claims.json`); the five bright lines (swept; result under Standing
  facts); the poem (stanza 4 and the author's translation are `book-1/epigraph.md`,
  the full two-stanza text consciously kept in git history and recorded so in the
  manifest); the nine historical cases (Part V, re-pointed as failure-mode evidence);
  the domestic vignette register (Part V's kitchen); and the privacy argument (Part
  V's capture joint). What remains is the deletion commit itself, and its timing is
  the author's: CLAUDE.md ties deletion to both new books existing, so the files
  stand until that is true or the author rules sooner. The commit message is the
  record of what was taken and what was consciously dropped.

---

## book-2

book-2 has its own tracker: `book-2/TODO.md` — unordered until its chapters are
decided, seeded from the hold list, adoption reviews, and the 2026-08-05
full-society operational completion contract. The discipline is unchanged:
**do not work book-2 items until Book 1 — First Edition actually ships at Gate
C**; collect there, rule here.
Every Book 1 domain card must nevertheless name its Book 2 operator/evidence owner
or an explicit external assumption so the seam cannot hide an unfunded,
unstaffed, unmeasured or physically impossible promise.

---

## Standing facts and methods — not tasks, and not history

Landed work is not recorded here; that is what git is for. What survives is the small
set of things a command cannot teach you and a rename cannot re-derive.

```
./verify.sh                 # 34.89 s measured 2026-08-05 with an independently
                            #   built clean 4cb02aa release supplied through NIBLI_PIN:
                            #   engine, spine, assertion surface, assurance case,
                            #   bounded red-team, amendment-semantics and placement
                            #   contracts,
                            #   evidence count, jargon,
                            #   counted-claims hard
                            #   gate, claim-comment check,
                            #   registry check, absences, INVARIANT 1, the arity and
                            #   counting guards, control scope, the pin
                            #   suite (555 pins) with cross-file :expect-pins
                            #   reconciliation, 15 record snapshots / 108 pins,
                            #   40 temporal processes / 236 pins, nine amendment
                            #   candidates / 44 pins, 24 placement rows / 336 pins,
                            #   24 cold composed floor probes / 24 pins, five
                            #   placement mutations / 73 pins, five placement
                            #   mutation-baseline sabotages, one composed-standing-
                            #   removal sabotage, the other executable
                            #   controls, one record failing-pin control, and source
                            #   counterfactuals in three diff classes — line deleted,
                            #   line changed, line added
./verify.sh --quick         # 2.22 s with the same pinned binary (2026-08-05): skips
                            #   chapter/floor pins, executable record snapshots,
                            #   amendment and placement executions, and counterfactuals
                            #   — never sufficient after a constitution edit
./verify.sh --only <file>   # one pin file, selected release engine, --allow-shell, and
                            #   the fixture's own KB chosen for counterfactual files;
                            #   partial by design — full run before committing
./verify.sh --table         # emit the claim-to-query table extracted from the pins
```

Prefer it to any check by hand. It exits non-zero on the first failure and names the
claim that stopped being true — including exit 3, the failure that is good news: a
pinned `:defect` stopped reproducing, and the script names it a REPAIR, not a
regression, because the response is to drop the marker and rewrite the prose that
called it a flaw, never to debug the harness. Use the **release** `nibli-pin` at or
after `4cb02aade43b394374c40e661907ad66df3af3fe`, never `nibli-host`. The script builds the adjacent engine unless
`NIBLI_PIN` or `NIBLI_SRC` deliberately selects one; an explicit binary path is used
as-is, so record its source commit separately. A stale binary can preserve logical
verdicts while violating bounded completion: pre-`5cec800` builds failed ordinary
full-source opaque queries, and `5cec800` restored those but could still time out when
standing itself had to traverse the T3 custody chain. `4cb02aa` closes that composed
boundary, so a green pin result alone does not establish engine freshness. **Gate on
the verifier's exit status, never on its output**: piping to `tail` swallows the exit, and `echo $?`
followed by `&&` gates on the echo — both shapes shipped a red commit on 2026-08-02.
The only safe chain is `./verify.sh > /dev/null 2>&1 && git commit …`.

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

- **A `fit/2` pin for any placement other than Homestay is a vacuous green.** `fit`
  has one producing rule and only ever carries `Homestay`, so `? fit(Ruk, HighSec).
  => FALSE` passes forever regardless of the design — kind three of the three FALSEs.

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
block comes back byte-identical and `verify.sh`'s evidence gate sees nothing. The cost
lands when the name enters a **rule** — measured live when `put` joined (evidence 23 → 24,
the gate moving in the same commit). A **new rule** may also add a stratum, which would
add a chapter, which the computed order forbids.

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
  **BL2** ("no negative scoring of persons") stood refuted by the constitution until the
  clawback ruling (2026-08-02): the student rule that docked Cira for a teacher's fraud
  is deleted, `lose(Points, Cira)` no longer derives, and BL2 stands **narrowed** —
  "no subtraction except by due process for one's own adjudicated fraud" — which the
  surviving wrongdoer rule satisfies.
  **BL3** ("merit never weights votes") survives vacuously: there is no arithmetic
  anywhere in the enacted lines and `verify.sh`'s digit ban keeps it that way, so
  weighting cannot be written. **BL4** and **BL5** are pod-and-tech-stack material and
  belong to book-2. **BL1** ported in narrowed form and is in chapter 1's closing
  section: the floor is unconditional *above* `person($x)`, and `person` is a roster of
  written facts with two producing rules, so personhood **is** an enrolment. Do not
  restate the unnarrowed BL1 in book-1; it would be false the way BL2 is false in
  `book.md`.

- **Article 9 does not semantically entrench the evidence vocabulary.**
  The source audit applies `permanent(Art_Evidence).` and still executes a direct
  vocabulary widening: `rich(Adam)` becomes writable. Article 9's general rule marks
  dead a docketed proposal that DECLARES a registered target and does nothing to the
  source itself. `adjust` is self-declared, so a targetless proposal and one naming a
  harmless target both receive the otherwise-derived law label.
  In the reverse direction, `false(Amend_Floor)` remains true and `become` remains false
  while an independently constructed source deletion removes the food entitlement and
  makes the adverse rule loadable.
  The executable source audit goes further: a concealed grammar change can remove the
  food entitlement while the separate anti-imprisonment firewall survives, and direct
  `admits("rich")` widening bypasses Article 9 entirely. Article 0a therefore makes
  widening *source-visible*, not approved, authenticated, or semantically entrenched.
  Nothing reads `become`, and the audit manually applies its candidates; it proves no
  proposal-to-source transition. A future entrenchment design must bind an exact change,
  independent effect review, compatibility verdict, and effective version.

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
