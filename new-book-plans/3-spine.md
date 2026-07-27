# The Derived Spine

Chapter order computed from the constitution's dependency graph, not chosen.
Method: parse every rule, build the predicate dependency graph, assign strata by
the standard fixpoint (positive edge ⇒ `stratum(head) ≥ stratum(body)`; negative
edge ⇒ `stratum(head) > stratum(body)`), then order chapters by stratum and, within
a stratum, by dependency. 34 predicates, 26 rules, 4 strata. Every verdict quoted
below was produced by the engine, not by hand.

---

## 1. The computed stratification

| Stratum | Predicates | What this layer is |
|---|---|---|
| **0** | `obligated`, `authority`, and 18 evidence predicates (`work`, `teaches`, `injure`, `show`, `judge`, `capture`, `deceive`, `family`, `home`, `severe`, `parent`, `broken`, `rotten`, `choose`, `suggest`, `approves`, `adjust`, `permanent`) | What is owed, and what the world reports |
| **1** | `false`, `permits`, `defend`, `lose` | Accountability: voiding, credentials, the shield, clawback |
| **2** | `person`, `prisoner`, `reward`, `expresses`, `dwell`, `fit`, `building`, `become` | Status and consequence |
| **3** | `err`, `travel` | The self-audit, and the single deprivation |

`obligated` is **assert-only**: it appears in no rule head and no rule body.
Nothing derives it and nothing can retract it. That is not a promise about the
floor; it is the floor's position in the graph.

`authority` is the only derived predicate whose entire dependency cone is
negation-free. Seating is never revoked — deliberately, so that recall cannot
retroactively strip a whistleblower's protection.

---

## 2. Three findings that reshape the book

**(a) The machinery exists only where the system might be tempted to take
something away.** Four of the six floor rights — `secure`, `eats`, `healthy`,
`learn` — appear *exactly once each*, inside their obligation, and in no rule
anywhere. They have no derivation because the ordinary case has nothing to
compute. Rules appear only around the accused, the convicted, the corrupt, and
the accuser. This is the book's thesis and it was computed, not asserted: **a
right that requires a computation to establish is not a right, it is a benefit.**

**(b) Conviction deprives exactly one thing.** `travel` sits alone at the top of
the graph behind `~prisoner`. Every other floor right survives conviction — and
where it might have been lost by inheritance, there is an *explicit re-grant*
rule (`prisoner($p) -> expresses($p)`, `prisoner($x) -> person($x)`). Verified:
`person(Hano)` TRUE, `expresses(Hano)` TRUE, `travel(Hano)` FALSE,
`travel(Adam)` FALSE. The entire punishment system, reduced to its logic,
takes away movement and nothing else.

**(c) The constitution obligates delivery it cannot yet derive.** `eats(Adam)`
FALSE. `healthy(Bela)` FALSE. Not because anyone is denied — because no rule
connects the obligation to any fact about food or care reaching a person. The
obligation layer is complete; the delivery layer does not exist. This is the
honest boundary of what the current constitution supports, and the book must
either stop where it stops or the KB must grow a provisioning layer first.

---

## 3. The spine

**Part I — What is owed (stratum 0)**

1. **The Floor Nobody Computes.** Six obligations, asserted, depending on
   nothing. Why unconditionality is a structural property rather than a promise:
   no rule can reach `obligated`, so no fact about a person can retract it.
   Contrast with every benefits system, where eligibility is a computation and
   therefore a place to stand and deny.
2. **What Counts as Evidence.** The eighteen things the world is allowed to
   report. Why the vocabulary is small and fixed, and why enlarging it is the
   quietest way to capture a system. `authority` and why it is never revoked.

**Part II — Accountability (stratum 1)**

3. **Who Holds the Pen.** `permits` — credentials derive from selection, never
   from assertion. The Article 8 fix and why it was needed: in the first draft,
   anyone who could write a fact could seat an auditor.
4. **Voiding.** `false` — multi-sig, independence, counter-audit. **Vex**: the
   auditor caught taking bribes who kept signing. The epoch fix, and the
   admission that it is a discipline over the record store rather than something
   the rules can enforce alone.
5. **The Shield.** `defend` — exposure protects, but only against an authority,
   and only until deceit is found. **Don**, who claimed protection for exposing
   his own victim and, in the first draft, got it. **Sly**, who is protected
   during a window the author chose to leave open. **Kel**, whose shield falls.
6. **Clawback.** `lose` — what taking back looks like when the floor is not
   touchable.

**Part III — Status and consequence (stratum 2)**

7. **A Prisoner Is a Person.** One rule, and everything it forces. Why this is
   the load-bearing line of the constitution and why removing it silently
   removes six rights at once.
8. **Contribution.** `reward` — recognition conditioned on not having been
   voided. **Bela**, **Esa**, **Dev**, **Mira**, **Lupo**. Why recognition is
   earn-only and why the arithmetic is deliberately absent.
9. **Where People Are Put.** `fit`, `dwell`, `building` — eligibility derived
   rather than asserted. **Ruk** in the farmhouse: the escape the first draft's
   own commentary mocked and its rules permitted.
10. **Changing the Rules.** `become` — amendment, and the register that
    entrenches itself. **Amend_Meta**, which voids itself by touching the
    entrenchment list. Why the bootstrap is underivable rather than forbidden.

**Part IV — The top of the graph (stratum 3)**

11. **The One Thing Taken.** `travel`. What it means that the whole apparatus
    of punishment reduces to a single deprivation.
12. **When the System Notices It Broke.** `err` — the breach marker, above
    everything, whose only job is to make a wrong placement queryable. A system
    that cannot state its own violations cannot be audited.

**Part V — Outside the graph** *(nothing here is derived; label it as such)*

13. Harvest from `book.md`: the social-credit chapter, the five joints, the pod
    and the state, the calculation problem. These are argument and evidence,
    not derivation, and should be visibly a different kind of chapter.
14. **What This Cannot Do.** The delivery gap (finding c). The fact channel as
    residual trust base. Manipulability of any selection rule. The difference
    between precise and justified.

---

## 4. Chapter 1 fidelity table (proof of method)

One row per load-bearing sentence. Private to the author; never shown to the
reader. Regenerate on every constitution change; any row whose verdict flips is a
paragraph that has started lying.

| # | Sentence in chapter | Query | Expected | Verified |
|---|---|---|---|---|
| 1.1 | "Six things are owed to every person, and nothing has to happen first." | `obligated` assertions, lines 37–42 | asserted, stratum 0, assert-only | ✅ |
| 1.2 | "No rule anywhere can reach the floor to withdraw it." | `obligated` occurs in no rule head or body | structural | ✅ |
| 1.3 | "A convicted person is still a person." | `person(Hano)` | TRUE | ✅ |
| 1.4 | "Conviction does not take away your voice." | `expresses(Hano)` | TRUE | ✅ |
| 1.5 | "It does take away your freedom to move." | `travel(Hano)`, `travel(Adam)` | FALSE, FALSE | ✅ |
| 1.6 | "A free person may move." | `travel(Jala)`, `prisoner(Jala)` | TRUE, FALSE | ✅ |
| 1.7 | "Being owed food is not the same as being fed, and this constitution can prove the first and not the second." | `eats(Adam)`, `healthy(Bela)` | FALSE, FALSE | ✅ |

Row 1.7 is the one to keep visible in the writing. Stating the gap is what makes
the rest of the book credible; hiding it is what would make it propaganda.

---

## 5. Writing blocked on constitution work

- **Provisioning layer.** Until rules connect obligation to delivery, Part I
  chapters can describe what is owed and not what arrives. Chapters 1–2 are
  writable now; a "does it reach people" chapter is not.
- **Exact arithmetic.** Any quantitative treatment of contribution needs integer
  minor-units before it can be derived; tolerant float comparison cannot back
  claims about money.
- **`lose` coverage.** Clawback appears in the graph at stratum 1 but chapter 6
  needs pins that exercise it; none exist yet.

