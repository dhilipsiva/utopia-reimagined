<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Book 1 Time-Model Decision

> **Status: author-ratified T3 target (2026-08-03); implementation gated.** This
> does not yet admit a temporal predicate or change the current constitution. It
> supersedes the 2026-08-02 refusal as a permanent scope rule, not as current law.

## 1. What exists now

Current Book 1 is **T0: flat snapshots plus an external carry convention**.
Facts inside one snapshot have no before/after relation, clock, duration, or
automatic expiry. **Engine-dependent—verify before relying:** in the release
`nibli-pin`, `past`, `now`, and `future` are distinct tensed wrappers, not a
clock. Stored facts match their own wrapper and bare rules preserve a queried
wrapper; the engine supplies no transition relation, duration, or ordering
between them. Before relying on that behaviour, re-run the release engine's
`test_tense_discrimination_past_vs_future`,
`test_tense_discrimination_present_vs_past`, `test_temporal_rule_lifting`, and
`test_temporal_rule_no_cross_tense`, and confirm this constitution still contains
no tensed wrappers. **Recorded check (2026-08-03):** at clean upstream `nibli`
commit `9b84be3`, those four tests passed. They establish wrapper discrimination
and rule lifting only, not cross-epoch time. `rotten` is an asserted next-epoch carry of a prior `false`
finding; the honest transition is an external obligation, not an in-snapshot
derivation. `free` and `mature` are writable status facts, not time-derived
states.

This distinction is load-bearing. A written term releases nobody; `free` is an
act, not an expiry. The current model cannot distinguish exposure-before-recall
from recall-before-exposure, cannot detect a deleted fact inside a snapshot,
and cannot prove that a later snapshot will ever be made.

The 2026-08-02 refusal remains controlling for the current T0 source, but T3
supersedes its permanent scope. Ratification does not license a contributor to
add a date-shaped fact or call it a time model.

## 2. The real constitutional choice

Keeping T0 permanently is technically honest, but it cannot make a
comprehensive social constitution. It cannot constitutionally prevent
indefinite unreviewed coercion, a frozen emergency, an office that never faces
renewal, or a remedy delayed forever. A manual epoch bridge improves record
integrity but does not supply promptness.

Conversely, a time layer is a new public power. Whoever can forge, withhold,
backdate, or freeze its record can extend confinement, suppress a ballot, or
make an emergency permanent. The issue is therefore not whether a timestamp
can be written; it is who controls the record of time and what failure does to
the affected person.

There is also a strict boundary between **safety** and **liveness**. Book 1 can
verify that a recorded condition limits a power. It cannot, by itself, prove
that an outside clock advances or that a reviewer eventually acts. Any such
claim needs an explicitly labelled, independently assured Book 2 handoff.

This is not an abstract trade-off under the ratified mandate. The Public
institutions and Emergency/resilience rows require review and an end condition.
T0 can specify an adjudicated end act, but cannot ensure that it occurs; it
therefore cannot complete those rows' protection against indefinitely
unreviewed public power.

## 3. Models available to the author

| Model | Book 1 can honestly claim | What it cannot supply |
| --- | --- | --- |
| **T0 — permanent refusal** | Snapshot conditions and explicit, adjudicated end acts. | Ordered events, promptness, expiry, or a bar on indefinite delay. |
| **T1 — audited epoch transitions** | Predecessor/successor reconciliation, carry, correction, and an auditable cross-snapshot continuity check: a required carried fact missing from the next attested snapshot is a defect. | Intra-epoch order; detection of a fact deleted within or before an attested snapshot; duration; or assurance that the next epoch arrives. |
| **T2 — ordered events** | Reviewable before/after evidence, such as notice before coercion. | Metric duration or a deadline that arrives. |
| **T3 — constitutional temporal limits** | A public power may have a review, renewal, sunset, or maximum-unreviewed-period limit through an independently assured time service. | A derived proof that the service itself advances; that remains operational assurance. |

T1 is necessary to make cross-epoch claims less trusting. T2 is necessary
where order itself matters. Only T3 can honestly prohibit indefinitely
unreviewed public power. Neither T1 nor T2 should be sold as a solution to that
problem.

## 4. Ratified ruling

**Author ruling (2026-08-03): adopt T3 as the constitutional target, with T1
required and T2 required wherever a rule depends on event order.** This supersedes
the old permanent-refusal rule as an expansion direction. T0 and its existing pins
remain the current law until the implementation gate passes.

The proposed constitutional principle is:

> Time constrains public power; it does not price a person. A temporal rule may
> require review, renewal, or an end to a public restriction. It may not map a
> person's character, contribution, recognition, wealth, identity, compliance,
> or score to a longer or shorter deprivation.

Book 1 would specify the temporal authority, its limits, challenge route, and
failure consequence. Book 2 would operate clocks, calendars, witnessing,
storage, scheduling, recovery, and availability. A Book 1 sentence must say
whether its temporal effect is formally modelled or externally assured; it may
not imply that an operational promise is a present derivation.

The rejected T0 alternative would retain only non-temporal end conditions. That
is coherent, but it leaves the Public institutions and Emergency/resilience rows
incomplete unless the author explicitly narrows their ratified scope. It is not
a safeguard against indefinitely unreviewed power.

## 5. Non-negotiable limits for a T3 design

1. **Independent source:** no body may alone create a case fact, control the
   temporal record that governs it, execute the consequence, and review itself.
   The source must be monotonic, publicly checkable, replicated or independently
   witnessed, and challengeable.
2. **Fail-safe polarity:** missing, disputed, or corrected temporal evidence may
   not cut off standing, a floor, liberty, appeal, or remedy. It must not silently
   extend a restrictive power or punish the person whose record was withheld.
3. **Power-scoped defaults:** a missed renewal ends or suspends the authority
   unless an independent, reviewable lawful basis remains. It never turns a
   claimant's missed deadline into loss of a core claim.
4. **No personal time score:** no earned-time credit, severity-to-duration table,
   character grading, or recency label may decide a person's standing, floor,
   ballot, or sentence. `reward` remains unread.
5. **Visible correction:** backdating, replay, correction, and recovery require
   a reason, a contest route, and a non-retroactivity rule: correction cannot
   silently extend an already expired restriction.
6. **Protected special cases:** emergency and office time limits cannot erase
   personhood, core floors, equality, evidence rights, appeal, or the shield.
   An adulthood rule, if retained, needs an accessible correction route and may
   never gate anything beyond the expressly ratified civic function.

## 6. Current-baseline prose coherence — not gated by the time ruling

These are corrections to the current T0 description, not temporal
formalisation. They remain necessary despite T3's selection as the future
target and must land before any public expansion snapshot containing the
affected chapters or the First-Edition release candidate.

1. [x] **Chapter 13's ambiguous “words exist” claim is repaired:** ordinary
   language is now distinguished from admitted constitutional facts and from a
   clock.
2. [ ] **Complete the cross-chapter coherence pass.** Chapters 4, 5, and 13 must
   use one current account: flat snapshots have no internal order; epoch carry
   is an external/manual cross-snapshot convention; the current constitution
   has no duration arithmetic or automatic expiry; and T3 is a ratified future
   target. In particular, retire the remaining permanent-refusal wording in
   Chapters 4 and 13 without implying that T3 already exists.
3. [ ] **Verify the corrected prose and existing pins/counted-claim gates**
   without introducing a temporal predicate, deadline, cadence, or new current
   Book 1 guarantee.

## 7. Formal implementation and verification gate

Do not alter `constitution.nibli` until all of these are present:

1. [x] **Author decision — complete:** T3 is ratified as the target and
   supersedes the 2026-08-02 duration refusal in `CLAUDE.md` as a permanent scope
   rule.
2. **Temporal-input contracts:** for every input, name writer, evidence,
   forge route, withholding route, correction, appeal, cross-epoch handoff,
   residual external assurance, and exact Book 1/Book 2 boundary.
3. **A two-snapshot differential harness:** current one-file pins cannot prove
   an N-to-N+1 transition. The harness must fail on omitted carry, forged carry,
   unexplained cross-snapshot disappearance, replay, or a frozen transition
   rather than merely producing a harmless-looking green result. It cannot claim
   to detect a fact deleted within or before an attested snapshot.
4. **Staged formal work:** implement and test T1 first, then T2 wherever an
   effect depends on before/after, then T3. Do not bypass this with `year`,
   `earlier`, a numeral, a tense wrapper, or a raw `temporary` assertion.
5. **Narrowness-impact note:** before each family lands, classify the impact on
   Chapters 1, 4, 5, 7, 8, 9, 13, 14, and Part V. In particular, name the fate
   of Chapter 4's unbounded reach-back, Chapter 13's title and no-duration
   claim, Chapter 8's three-open-doors claim, and Chapter 14's unread-duty
   endpoint. Apply the coverage map's impact gate.
## 8. Required adversarial matrix

| Area | Attack and required control |
| --- | --- |
| Baseline | Prove tense wrappers, `year`, `earlier`, and an opaque stated term create neither chronology nor release under T0. |
| Carry | Test honest carry, omitted carry, forged `rotten`, cross-snapshot disappearance/replay, forgiveness, and same-epoch reciprocal voids. Both omission and forgery must become a named, appealable defect; do not claim detection of intra-snapshot deletion. |
| Release | Test forged `free`, withheld release after any adopted end condition, and valid release. Preserve personhood, travel, floor debt, and the disclosed delivery gap. |
| Maturity | Test forged and withheld `mature`; prove it cannot gate personhood, floors, liberty, due process, or remedy. |
| Order and recency | Test exposure before/after office end, forged/withheld stale facts, and backdated records. Do not claim an ordering result without separately represented event and record time. |
| Emergency and office | Test forged declaration/end, frozen end, re-declaration loop, succession, and self-review. Ending power must not erase answerability or the shield. |
| Audit | Any deadline or ignored-duty rule that reads `obliged` must deliberately retire Chapter 14's current endpoint and update its pins and prose. |

## 9. Ratification record

- [ ] **Retain T0 permanently.** Not chosen. This would retain the no-time ruling
  and leave Public institutions and Emergency/resilience incomplete unless their
  mandate were narrowed.
- [x] **Adopt T3 as the constitutional target (ratified 2026-08-03).** Keep the
  current formal kernel at T0 until T1, T2 wherever order matters, the
  temporal-input contracts, the differential harness, and the adversarial matrix
  all pass.

No third option is honest: an unassured manual timestamp, a new word for an
epoch, or a Book 2 promise with no named failure consequence is not a time
model.
