**This is a closed-world ontology for personal records: exactly 21 atomic predicates, nothing else writable.**

Parsed cleanly from the text, the 21 are:

1. Worked  
2. Taught  
3. Injured someone  
4. A body passed judgment  
5. An auditor documented a finding  
6. Lied  
7. Exposed something  
8. Has a home  
9. Has a family  
10. Has a parent  
11. Reached adulthood  
12. Offence was severe  
13. Assembly proposed a change  
14. Electorate approved the change  
15. Change touches a particular article  
16. That article is protected  
17. A body is a public institution  
18. Electorate seated someone  
19. Cleared  
20. Recalled  
21. Voided in an earlier period  

Everything else—reliability scores, risk flags, “person of interest,” wealth, politics, health, associations, predictions, suspicions—is definitionally inexpressible. Conclusions (guilt, standing, imprisonment, authority) are never stored; they are only derived from combinations of the above plus absences. One auditor’s finding changes nothing. Self-appointment is impossible.

### Strengths (real)
- Separates event from assessment with mechanical force. File growth cannot smuggle character judgments into the permanent record because there is no slot.
- Raises the cost of weaponized process: investigation itself leaves no mark.
- Makes every exercise of power publicly reconstructible from ordinary facts. No opaque “we judged you untrustworthy.”

### Critical failure points
1. **The list is not entrenched.** The text itself flags this correctly. Capture does not begin with “imprison without evidence.” It begins with “we need one more field for cooperation / concern / fitness.” Once the vocabulary expands, the derivation rules become theatre. This is the softest, highest-leverage attack surface and it is left open.

2. **Derivation is not free.** Someone or something must compute “what follows.” That computation engine (rules, thresholds, absences that matter) is itself a locus of power. Protecting the 21 while leaving the inference machinery unprotected merely relocates the problem.

3. **Operational incompleteness.** Any functioning society needs temporary, non-persistent assessments: medical capacity, flight risk, conflict-of-interest, credit underwriting, security clearances, epidemiological contact. Forbidding them forces either paralysis or parallel shadow systems that recreate the forbidden fields under different names. The design does not solve this; it ignores it.

4. **Ambiguity of the atoms.** “Injured,” “lied,” “exposed,” “severe,” “family,” “parent” are not self-interpreting. Boundary disputes will be decided by the same institutions the ontology was meant to constrain. Without precise formal definitions and a protected meta-layer, the list is not closed in practice.

5. **Second-order effects.** Once people internalize that only these 21 things can ever be said, strategic behavior shifts: game the writable facts, avoid generating them, manufacture the absences that protect status. The record becomes a target rather than a neutral ledger.

### Better alternative
Entrench the *principle* (closed finite vocabulary of pure events; conclusions only derived; no character predicates) rather than any particular list of 21. Allow amendment of the list only by supermajority + multi-year sunset + independent formal verification that the new atom remains an event rather than a judgment. Create a narrow, expiring, non-persistent channel for operational assessments that is forbidden from feeding standing, voiding, or permanent records. Make the derivation rules themselves part of the entrenched core and publicly executable.

### Main risks / uncertainty
- If the list stays frozen, the system becomes unusable for complex coordination and will be abandoned or subverted.
- If it expands, the protection evaporates quietly and the original design becomes historical curiosity.
- Confidence that any pure closed-list approach survives contact with real institutions is low; history favors expansion of what may be said about people.

Watch the list. Everything else is downstream of whether it stays closed.

**Pins match the chapter’s load-bearing claims. All 12 hold as written.**

### Mapping
- `injure(Hano, Ivo)` + `judge(Court, Hano)` → atomic events.  
- `prisoner(Hano)` true only by derivation (absence of appeal/compromise/protection).  
- Direct `prisoner(Zed)` and `authority(Pax)` refused: conclusions are not writable.  
- `public(Court)` → `authority(Court)`: the only two routes to standing are seating or public office.  
- Single `capture(Koa, Esa)` leaves both `false(Esa)` and `false(Koa)` false: one auditor changes nothing; investigation itself is not a mark.  
- `permanent(Art_Floor)` true, `permanent(Art_Evidence)` false: the explicit gap the chapter admits.

### What remains unpinned (and therefore still soft)
1. The exact derivation rules that turn the 21 atoms into `prisoner`, `authority`, `false`, etc. Without them the pins only assert results; they do not enforce the chain.  
2. The multi-auditor threshold stated in the prose (“two independent auditors… not related… not compromised… not found to have lied”). A single-capture case is tested; the two-capture success case is not.  
3. Closure of the 21-atom vocabulary itself. No refuse tests exist for the forbidden predicates (score, risk, suspicion, wealth, association, likelihood, etc.).  
4. Independence and non-compromise conditions on the auditors. Those are required by the text but invisible to these pins.

### Assessment
The pins correctly guard the chapter’s central thesis: facts are writable, conclusions are only derivable, and the evidence list is deliberately left non-permanent. That last pin is the honest one. If it ever flips, the closing section of the chapter becomes false and must be rewritten.

The formal surface is still thinner than the prose claims. The next necessary pins are the derivation rules and the two-auditor success case. Without them the system can still be gamed by writing the atoms and then asserting the conclusion outside the engine.

**Standing is permanent by design, not by oversight.**

The two acquisition routes (public institution, or electorate seating) match the prior chapter’s refusal of self-granting and of any third path. Standing is answerability; power is operational reach. Recall (or any other mechanism) strips only the second. That separation is coherent.

### Core argument
If standing were revoked on recall, successful exposure + removal of a corrupt official would retroactively erase the protection that exposure conferred. The whistleblower’s shield would vanish at the exact moment the system worked. The design therefore freezes standing so that removing Boss cannot be turned into a weapon against Rebel. This is the load-bearing claim and it holds on its own terms.

### Costs (acknowledged and real)
- The set of people with standing is monotonically non-decreasing and includes the long-recalled and the dead.  
- Any person facing consequences can expose any historical standing-holder and obtain temporary protection until the exposure is examined for bad faith.  
- That window is deliberate; the text defers its regulation to a later chapter. Until then it is an open delay and noise vector.

### Residual weaknesses
1. Public bodies themselves can be dissolved or redefined. The text is silent on whether the body’s standing (or that of its past members) survives institutional death.  
2. Erroneous or coerced seating still confers permanent standing. There is no correction path.  
3. Exposure of the dead remains protective. This creates incentives for historical fishing and complicates the bad-faith check (who examines a claim against someone long gone?).  
4. The design still depends on a sufficient stock of *active* power-holders to examine the opportunistic exposures that permanence invites. Standing alone does nothing; power is required to close the window.

### Assessment
The permanence rule is a clean second-order protection for the exposure mechanism. It correctly refuses the more “sensible” alternative that would punish successful whistleblowing. The trade-off is explicit: process integrity and whistleblower safety over finality and a bounded standing set. That is a defensible choice, not a bug.

It does, however, systematically favor delay and historical reach. Over long time-scales the standing set becomes a large, permanent attractor for strategic claims. Whether the later chapter’s bad-faith filter is strong enough to keep that manageable is the open question the design itself flags.

The formal surface remains thinner than the prose: the derivation of standing is pinned, its permanence is asserted, but the interaction rules with recall, exposure, and institutional dissolution are not yet constrained.

**Pins match the chapter’s load-bearing claims. All asserted results hold as written.**

### Mapping
- `public(Court)` → `authority(Court)`: standing by institutional nature.  
- `choose(Electorate, Boss)` → `authority(Boss)`: standing by seating.  
- Direct `authority(Pax)` refused: no self-conferral.  
- `authority(Ivo)` false: neither route.  
- `broken(Boss)` true + `permits(Review, Boss)` false: recall strips operational power.  
- `authority(Boss)` remains true despite `broken`: the permanence claim.  
- `show(Rebel, Boss)` → `defend(Rebel)` true, `prisoner(Rebel)` and `false(Rebel)` false: exposure of a standing-holder shields the exposer and blocks the case.

### What remains unpinned
1. Explicit re-query of `authority(Boss)` *after* `broken(Boss)` is asserted. The comment states permanence; the queries do not re-test it.  
2. The cost side the chapter itself flags: exposure of long-recalled or dead standing-holders still yields `defend`. No pin exercises that case.  
3. Institutional dissolution or redefinition of a public body. Does `authority` of the body (or its past members) survive?  
4. Interaction with the Chapter 1 atoms (`recalled` is on the 21-list; `broken` is the derived operational consequence).  
5. The bad-faith filter that is supposed to close opportunistic exposures. Deferred in the prose and absent here.

### Assessment
The pins correctly guard the central thesis: standing is answerability and survives the loss of power; that survival is what prevents successful removal from becoming a weapon against the exposer. The design choice is coherent and the pins reflect it without contradiction.

The formal surface is still thinner than the prose. Permanence is asserted rather than derived from an explicit non-revocation rule, and the acknowledged long-term costs (monotonic growth of the standing set, historical reach of exposure protection) are not yet constrained. Those are the next pins required if the chapter’s argument is to be load-bearing rather than merely described.

**The pen is a pure derived credential. Writing it is refused.**

Three simultaneous conditions:
1. Electorate seated you.
2. Not recalled.
3. Not voided in an earlier period.

If all three hold, the pen exists. If any fails, it does not. No grant, no certificate, no override. This is the same refusal move as Chapter 1, one level up: conclusions about power cannot be written any more than conclusions about guilt or standing.

### What was fixed
The prior hole allowed the credential to be written directly. Two fabricated pen-holders (Sock, Puppet) could then satisfy every surface check of the voiding rule and strip an innocent. That route is now closed. The multi-signature requirement only becomes meaningful once the pens themselves cannot be forged by writing.

### Separation maintained
- Boss (seated then recalled): standing permanent, pen gone.  
- Vex (seated, never recalled, but voided earlier): pen blocked by temporal carry.  
The second case forces time into the model so that a voiding on Monday cannot be used to sign another voiding on Tuesday inside the same snapshot.

### The second credential
Relief (from being cleared) is the symmetric opposite instrument. Also derived only, never writable. One fact on the 21-list produces it by rule. Taking and restoring are both closed to direct inscription.

### Hard boundary (correctly named)
Everything downstream of seating is sealed. Seating itself is an external fact the design is told. The system can refuse a forged pen; it cannot detect a forged election. Whoever controls the recording of “electorate seated X” controls who holds the pen. That is not a patchable flaw inside the design; it is the foundation.

### Residual soft spots
1. Public institutions received standing by nature in Chapter 2. It is unclear whether they automatically hold the pen or must also satisfy the three conditions (most of which do not apply to bodies).  
2. “Earlier period” is load-bearing and still undefined. Any ambiguity in period boundaries re-opens ordering games.  
3. The recorder of the “cleared” fact itself needs a pen or equivalent. Circular dependency is possible if relief can be blocked by the same people the relief is meant to constrain.  
4. No positive signal exists. An auditor may not know they hold the pen until the rule is evaluated at the moment of action.

The design is internally consistent with the prior two chapters and closes the exact loophole it identifies. The remaining exposure is the one the text itself flags: selection is open, everything after it is closed. That is the correct place to watch.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- `choose(Electorate, Gia)` + (implicit not-broken, not-rotten) → `permits(Review, Gia)` true. Same for Wren.  
- Direct `permits(Review, Sock)` refused: credential is derived-only.  
- Boss: `choose` true, `broken` true → `authority` remains true, `permits(Review)` false. Standing survives; pen does not.  
- Vex: `choose` true, `rotten` true → `permits(Review)` false. Prior voiding carries forward and blocks the pen.  
- Nia: `clear` true → `permits(Appeals, Nia)` true, `prisoner` false. Relief is the symmetric derived credential.

### What remains unpinned
1. The actual voiding action that requires two simultaneous pens. Gia and Wren hold pens; no pin shows them jointly voiding a third party.  
2. Public institutions: prior chapters gave them standing by nature; whether they automatically hold the pen is untested.  
3. Definition and ordering of “earlier period.” `rotten` is asserted; the temporal machinery that produces it is not.  
4. Who may record the `clear` fact itself. If that recorder needs a pen, a dependency exists that is not constrained.  
5. The foundation the chapter itself names: seating is an external input. No pin can protect against a forged `choose`.

### Assessment
The pins correctly guard the central moves: the pen is reached only by the three-condition rule, direct writing is refused, recall and prior voiding both strip it, and relief is the opposite derived instrument. The Sock/Puppet hole is closed at the level of the credential.

The formal surface still lags the prose on joint action, institutional pens, period boundaries, and the external foundation of seating. Those are the next required pins if the chapter is to be fully load-bearing.

**The shield is mechanical: expose a standing-holder and imprisonment is blocked until a finding of deceit.**

Two facts only decide it:
1. The target has standing.
2. No finding that the exposure is deceitful yet.

Nothing else enters. Sincerity is irrelevant.

### The three cases
- **Don** exposes Pax (no standing). Shield does not attach. Don is a prisoner.  
  This closes the prior hole that let any defendant name anyone and become unjailable.

- **Sly** exposes the court (has standing). No deceit finding yet. Shield holds. Sly remains free during the window.  
  Deliberate default: protection first, withdrawal later. The asymmetry argument is correct — a compromised authority that can race the review will always choose to convict first if the shield defaults to off. Temporary liberty for the guilty is the recoverable error; preemptive imprisonment of the honest exposer is not.

- **Kel** same as Sly, then the exposure is found deceitful. Shield falls, conviction completes, Kel’s own standing is voided.  
  The window is finite and closes hard. The counter-audit is the backstop.

### Consistency with prior chapters
- Standing is permanent → the set of valid targets only grows (including the recalled and the dead).  
- Examining the exposure for deceit requires the pen (Chapter 3).  
- Exposure itself is one of the twenty-one atoms.  
- Voiding the deceitful exposer follows the ordinary multi-auditor rules.

### Costs (explicit and real)
1. Every genuine prosecution of a guilty person who also exposes an authority is suspended for the duration of the review.  
2. Because standing never expires, a defendant can reach arbitrarily far back in history, name a forgotten standing-holder, and open the window. The review can later close it (as with Kel), but the surface area is permanent and expanding. The design currently places no time or recency bound on the exposed conduct.

### Residual soft spots
- Capture or delay of the review body itself: the shield lasts exactly as long as the examination takes. A compromised or slow pen-holder extends the window.  
- Volume: as the standing set grows, opportunistic historical exposures become a standard delay tactic. Throughput of the review function becomes load-bearing.  
- No pin yet exists for the joint action that finds deceit and voids the exposer.

The rule is coherent, the default is correctly chosen under asymmetry of harm, and the three cases demonstrate both the protection and its limits. The permanent growth of the target set is the direct bill for Chapter 2; the design acknowledges it and leaves the question of bounding it open. That is the live design pressure.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- **Don**: `injure` + `show` of a non-authority → `defend` false → `prisoner` true.  
  Shield requires the target to hold standing; private persons do not trigger it.

- **Sly**: `injure` + `show` of an authority (Court) with no deceit finding → `defend` true → `prisoner` false.  
  Default is protection until proven false.

- **Kel**: `show` + `deceive` finding → `defend` false → `prisoner` true + `false` true.  
  Window closes hard; standing of the deceitful exposer is voided.

### What remains unpinned
1. The examination that produces `deceive` itself requires pen-holders. Capture or delay of that review extends every active shield.  
2. Historical and dead standing-holders still generate `defend` until a `deceive` finding is recorded. The permanent growth surface from Chapter 2 is untested.  
3. Joint action: voiding Kel’s standing should require two pens under the Chapter 1 rule; only the result is pinned.  
4. Multiple or sequential exposures by the same person, and the interaction of overlapping shields.

### Assessment
The pins correctly enforce the mechanical rule and the three cases that define its boundaries. No sincerity judgment appears; only the two record facts (target has authority, exposure not yet found deceitful) control the shield.  

The formal surface still lags on the review process that closes the window and on the long-term cost of an unbounded standing set. Those remain the live pressures.

**Voiding requires two valid pens and turns every improper attempt back on the examiner.**

### The conditions
1. **Two** credentialed auditors must each examine and record the same finding. One is never sufficient. Corruption becomes a conspiracy problem.

2. **Family**: judging your own parent or child voids *the judge*, not the target. The finding does not land.

3. **Deceit**: a false finding voids the auditor who made it. The target is untouched. The cost of fishing is immediate and personal.

4. **Prior voiding carries forward**: a previously voided person cannot contribute a valid signature in later periods. Sequence is inserted by hand at period close because the record itself is a flat snapshot.

All four are mechanical. No discretion, no sincerity test, no weighing of motives.

### What the design correctly achieves
- A single corrupt, mistaken, or pressured auditor cannot destroy anyone.  
- Improper findings are not merely discarded; they destroy the person who made them. The first attempt is expensive.  
- Temporal ordering is forced into a system that otherwise has none.

### The two disclosed gaps (both real)
1. **Independence is almost empty.** Only the parent-child relation is blocked. Spouses, siblings, long-term partners, household members, and close associates may co-sign without penalty. The “two independent” requirement collapses into a conspiracy of two people who already trust each other. The record cannot express those relationships because they are not among the twenty-one atoms. This is the largest remaining hole in the accountability machinery and the chapter states it plainly.

2. **Sequence is an external discipline.** The carry-forward mark works only if someone actually writes, at the close of each period, who was voided. If that entry is omitted or selective, a voided auditor signs again and nothing inside the design detects it. Same foundation limit seen with seating and elections: the rules are airtight on top of a record that people maintain.

### Assessment
The voiding rule is the sharpest non-imprisonment instrument and the guards are correctly pointed backward at the examiner. The design is unusually honest about what it cannot do. Both remaining gaps are structural: one follows from the closed vocabulary of the twenty-one facts, the other from the fact that any formal system can only guarantee consequences of its inputs, not the inputs themselves.

These two limits will keep recurring. The society can enforce what follows from the record. It cannot guarantee the record.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- **Two pens succeed**: `permits(Review, Gia)` + `permits(Review, Hex)` → `false(Bela)` true.  
- **One fails**: `capture(Koa, Esa)` → `false(Esa)` false.  
- **Family turns on the judge**: `parent(Dev, Esa)` + `judge(Dev, Esa)` → `false(Dev)` true (target untouched).  
- **Deceit turns on the liar**: `deceive(Lupo, Mira)` → `false(Mira)` false, `false(Lupo)` true.  
- **Prior voiding blocks**: `rotten(Vex)` + one valid pen → `false(Tyr)` false.

### What remains unpinned
1. The narrow independence rule itself. Only parent-child is exercised. Spouses, siblings, household members, and long-term associates remain able to co-sign; the vocabulary cannot express those relations.  
2. The external sequence discipline. `rotten` is asserted; the hand-written period-close step that produces it is not constrained and cannot be enforced from inside the design.  
3. Full joint-action conditions on the successful Bela voiding (non-related beyond parent, non-liar, simultaneous, same finding). Only the result is pinned.  
4. Interaction with the shield: a deceit finding that voids an auditor while a shield is active.

### Assessment
The pins correctly enforce the core guards: two pens required, improper findings destroy the examiner, and prior voiding carries forward. The two structural gaps the chapter itself names — thin independence and unenforceable sequence — remain outside the formal surface. Those are the live limits of the voiding instrument.

**Clawback is total and reaches only recognition.**

When standing is voided, all accumulated recognition is taken. No proportion, no source-tracing, no assessment of how much was tainted, no discretion. The instrument is deliberately blunt.

### Hard boundary (the more important fact)
Clawback stops at recognition. It cannot touch:
- personhood,
- liberty of movement,
- or any of the eight things the society owes everyone.

A fully voided person still eats, has housing, learns, speaks, associates, and votes. The floor is not reducible by any finding about conduct. There is no moment at which an official decides to be merciful about housing; the instrument was never built to reach it.

### The unresolved case: Cira
Bela taught Cira. Bela is voided. Cira’s entire recognition is clawed back.

Cira did nothing. The rule does not ask:
- whether any of Cira’s recognition actually came from Bela,
- whether Cira knew or colluded,
- or how much is attributable to the fraud.

All of it goes. Fin, taught by someone never voided, keeps everything. The difference is a fact about the teacher.

The text is explicit: this outcome is not defended because it is not defensible as written. It is the one place the accountability machinery does to an innocent person what the rest of the design is built to prevent. It is flagged as unresolved.

### Architectural choice
Bluntness is a feature against the guilty: no room for partial forfeit that could be bought or pressured. The same bluntness is the bug against Cira. The design’s answer is not to sharpen the instrument (which would require recognition to become a source-ledger). It is to put a hard ceiling on its reach so that even when used wrongly, the worst it can do is take back what was given, never what is owed.

The floor remains intact. That distinction is the load-bearing claim of the chapter. The Cira rule is the open defect.

**Pins match the chapter’s load-bearing claims, including the named defect.**

### Mapping
- `false(Bela)` → `lose(Points, Bela)` true: voiding claws back all recognition.  
- `person(Bela)`, `travel(Bela)` true, `prisoner(Bela)` false: floor and liberty untouched.  
- `teaches(Bela, Cira)` → `lose(Points, Cira)` true: the contamination rule as currently written.  
- `teaches(Esa, Fin)` + `false(Esa)` false → `lose(Points, Fin)` false: only a voided teacher triggers it.  
- `false(Lupo)` → `lose(Points, Lupo)` true: applies to the deceitful auditor.  
- `lose(Points, Mira)` false: target of a liar keeps recognition.

### Explicit defect encoding
The Cira pins are deliberately written to the indefensible rule. The file note states the intended future: if contamination is narrowed to recognition actually derived from the fraudulent teaching, `lose(Points, Cira)` flips FALSE and the chapter’s middle section must be rewritten. That is the correct direction.

### What remains unpinned
1. Source-tracing itself. Recognition is still a total, not a ledger of provenance. The narrower rule the chapter itself prefers cannot yet be expressed.  
2. Interaction between clawback and the shield or prior voiding marks.  
3. Whether recognition clawed from Cira can ever be restored if Bela is later cleared.

### Assessment
The pins correctly enforce both the blunt instrument and its hard ceiling. They also correctly preserve the open defect rather than papering over it. The floor remains unreachable; the Cira contamination remains the unresolved cost of bluntness.

**The sentence is load-bearing, not ornamental.**

“If you are a prisoner, you are a person” is the sole formal link between conviction and continued humanity, and it is also the mechanism that keeps the floor unconditional for everyone.

### Two effects of deleting it
1. **Zed**: An unlisted person appears only via injury + judgment → becomes a prisoner → becomes a person → is owed the full eight.  
   Remove the sentence: Zed remains a prisoner but ceases to be a person. The eight rights evaporate with no alarm, no failure, no visible warning. The connection is one sentence wide.

2. **The architectural effect**:  
   With the sentence present, any rule that imprisons people for lacking one of the eight (belief, food, shelter, etc.) is unwritable. It forms a self-referential loop: the floor runs through personhood, personhood runs through prisoner status.  
   Remove the sentence and the same rule becomes ordinary and applies to the entire population.  
   The line that keeps prisoners human is therefore the same line that keeps everyone else’s rights unconditional. They are not two provisions. They are one. A carve-out for prisoners opens the floor to conditionality for all.

### Structural claim
You cannot make rights conditional for the worst people and keep them unconditional for everyone else. The carve-out is the mechanism that allows conditionality to spread. The design refuses it for architectural reasons, not sentiment or earned dignity.

### Uncomfortable corollary
The prisoner route is the *only* automatic entry into personhood that does not require someone to write a name on a roster. Everyone else is a person because they were listed. Personhood itself is mostly a hand-maintained list; the sole way to acquire the society’s protection without depending on that list is to be convicted.

This is an artefact of a roster maintained by hand, not a designed feature. It leaves open the question the text itself flags: what holds the personhood list open?

The entanglement is correct and load-bearing. The corollary is the new live pressure.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- `injure(Zed, Ivo)` + `judge(Court, Zed)` → `prisoner(Zed)` true → `person(Zed)` true.  
  Personhood derives solely from prisoner status; nobody wrote Zed onto any roster.
- `eats(Zed)` false: the floor is owed, not yet delivered (delivery is the next chapter’s subject).  
- `travel(Zed)` false: conviction still restricts liberty.  
- Two refusals: any rule that imprisons for lacking belief or food is rejected. The self-referential loop is enforced.  
- Control acceptance: a non-floor condition (`~home`) may still produce prisoner status, confirming the refusals are selective to the floor.  
- `expresses(Hano)` true: a named, convicted person keeps the floor.

### Explicit design note
Zed is introduced by the pin file itself. The chapter requires someone the person-roster has never mentioned; every other prisoner in the cast is already asserted as a person. That fact is the chapter’s closing point.

### What remains unpinned
1. The full set of eight floor rights for Zed (only `eats` and `expresses` are sampled).  
2. Delivery machinery (explicitly deferred).  
3. What holds the ordinary personhood roster open — the artefact the chapter itself flags as unanswered.

### Assessment
The pins correctly enforce both effects of the sentence: automatic personhood for the unlisted convict, and the entanglement that makes the floor unconditional for everyone. The roster dependency remains the open pressure.

**Eight things, owed unconditionally to every person.**

Safety. Food. Shelter. Care when ill. Learning. Speech. Belief. Company.

No qualifying condition of any kind. The previous chapter made this structural: the eight cannot be made conditional without opening the floor for everyone.

Belief is separate from speech; the contents of the mind have no slot. Company is included so that “we kept the body alive in isolation” is not a defence.

### Owed is not delivered
The design states the obligation with total precision and contains **no machinery** that connects any obligation to any actual provision. For every person and every one of the eight, the record cannot answer whether it arrives.

The single exception is Hano: the record knows he has shelter because he is under a placement order. The only part of the floor that has working apparatus is the part that overlaps with punishment. Everywhere the system acts *on* people, detail exists. Everywhere it owes something *to* people, there is only the statement.

### Where the protection stops
Three doors remain open and have been verified open:

1. Standing can still be voided for lacking a floor item → recognition is clawed back.  
2. Recognition can still be clawed back directly for lacking a floor item.  
3. Compulsion is permitted: a rule that *produces* a floor item as a consequence of imprisonment is accepted. Absence cannot be punished; manufacture can.

The floor blocks the cell and stops there. Everything short of imprisonment remains available against the disapproved.

### Owed by whom
No agent is named. There is a creditor and no debtor. No body carries a duty to provide, no mechanism compels provision, no consequence follows from absence.

This is a decision still unmade, not an oversight. Until the design chooses between a providing agent and a pure agreement with no enforceable duties, the eight things remain a precise account of a debt that no one has been asked to pay.

The delivery gap and the missing obligor are the largest absences in the society as currently written.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- Seven floor predicates return FALSE for ordinary persons: `eats`, `healthy`, `secure`, `learn`, `believe`, `meets`, `dwell`. The record cannot confirm delivery of any of them.
- Exception: `dwell(Hano)` TRUE because `prisoner(Hano)` TRUE. Shelter is verifiable only through the placement machinery that overlaps with punishment.
- Three open doors accepted:
  - `~believe` → `false` (standing still reachable)
  - `~meets` → `lose(Points)` (recognition still reachable)
  - `prisoner` → `believe` (compulsion / manufacture permitted)

### Explicit design note
The “owed by whom” section correctly describes the current state: no agent is named. A thin constitutional layer has been decided but not yet enacted. When it is, the chapter’s closing section must be rewritten and the note removed.

### What remains unpinned
1. The full set of eight (safety, care, speech, company sampled partially).  
2. Any positive delivery rule or obligor once the planned layer is added.  
3. Interaction between the open doors and the shield or voiding rules.

### Assessment
The pins correctly enforce the central distinction: obligation is total and precise; provision is invisible except where it coincides with custody. The three residual attack surfaces short of imprisonment are left open by design and are formally accepted. The missing debtor remains the deferred decision.

**The vote follows from person + adult. Conviction takes neither, so it takes only movement.**

Hano is confined and cannot travel freely. Hano remains a person, remains owed the full floor, still speaks, and still votes. Item-by-item check confirms the claim: punishment, reduced to its logic in this design, removes liberty of movement and nothing else.

### Threshold versus punishment
Cira does not vote. Cira is a person but not an adult. Nothing was taken; the second condition is simply not yet met. When both are satisfied the ballot follows automatically, with no application and no permission required. That is a threshold. Disenfranchisement is the opposite shape: a rule that reaches in and removes something already held, on the basis of conduct. The distinction is not technical; it is the difference between waiting and forfeiture.

### The thinner protection
The floor is structurally protected: any rule of the form “lacking one of the eight shall be a reason to imprison” is refused outright.  

The vote is not. A rule of the ordinary form “adults who are not prisoners may vote” is accepted without complaint. It works. Every convicted person loses the ballot and nothing objects.

The firewall only catches one direction: *absence → punishment*. Disenfranchisement runs the other way: *punishment → loss of X*. The machinery does not see it. Hano votes because the disenfranchising clause has not been written, not because it cannot be written. That is a materially weaker guarantee.

### Same silence as the floor
The design states the entitlement with precision and is silent about provision: whether elections occur, whether the count is honest, or whether a ballot is collected from custody. A prisoner with an unimpeachable right to vote and no ballot box stands in the same position as a person with an unimpeachable right to eat and no food.

The theorem holds for what conviction may take. The vote remains intact only by absence of the reverse-direction rule, and delivery remains unaddressed.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- `prisoner(Hano)` true, `travel(Hano)` false, `decide(Hano, Ballot)` true: confined, movement taken, vote retained.
- `decide(Jala, Ballot)` true: the ballot follows the same derivation for any adult person.
- `person(Hano)`, `expresses(Hano)` true; `false(Hano)`, `lose(Points, Hano)` false: conviction takes only movement.
- `person(Cira)` true, `mature(Cira)` false, `decide(Cira, Ballot)` false: threshold (“not yet”), not forfeiture.
- Standard felon-disenfranchisement rule accepted: `person & mature & ~prisoner → decide(Ballot)`. The reverse-direction attack compiles; the thinner protection is formally recorded.

### Explicit design note
The accept pin encodes the chapter’s honest half. If a later revision armours the franchise against the reverse-direction rule, this pin must flip to a refusal and the closing sections must be rewritten.

### What remains unpinned
1. Delivery: whether a ballot is actually collected from custody.  
2. Any future armouring of the vote against the accepted disenfranchisement form.  
3. Interaction with the open doors from Chapter 8 (standing or recognition still reachable for other reasons).

### Assessment
The pins correctly enforce the completed theorem (punishment takes only movement), the threshold/punishment distinction, and the directional weakness of the current protection on the vote. The franchise remains intact only by absence of the reverse-direction clause.

**Recognition is binary and has exactly three doors.**

Teach someone. Do a piece of work. Examine someone’s conduct honestly and record the finding. Nothing else earns it.

### No quantity
Recognition is a fact about a person, not a number. There is no total, no ranking, no comparison, no spending, no transfer, and no pricing. “So much recognition” is not expressible.

This is deliberate. Any number creates ranks; ranks become entitlements; entitlements become tradeable; within a generation an aristocracy of the highly-recognised appears whether anyone intended it or not. The design refuses the material those dynamics are made from. The refusal is not a rule against ranking; it is the absence of arithmetic.

### Voiding closes every door
A voided person can still teach, work, or examine. None of it registers. Voiding does not merely erase past recognition; it permanently blocks the three routes by which recognition is earned. The condition is the same on all three doors.

### The incentive on the third door
Examining earns recognition. The society therefore pays people, in its own coin, to look into others’ conduct. That is an incentive toward more scrutiny, including of people who did nothing.

Two mitigations exist: an improper finding costs the examiner their own standing, and recognition attaches to the examination itself, not to a guilty outcome. The arrangement is better than most. It is still an incentive, and the design’s decision to treat honest examination as a contribution on a par with teaching and work is one a reader is entitled to sit uneasily with.

### The deliberate loss
The society cannot say that someone did more. Forty years and one week, ordinary and extraordinary, all collapse to the same single fact: recognised.

The trade was made knowingly. Ability to express degree would enable ranking, and ranking is what the entire arrangement exists to prevent. Degree was given up. The loss is real; the book does not pretend otherwise.

Binary recognition prevents the aristocracy that quantitative systems reliably produce. It also makes contribution visible only as presence or absence, never as magnitude. That is the completed shape of the instrument.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- `teaches(Esa, Fin)` → `reward(Esa)` true  
- `work(Quin, Census)` → `reward(Quin)` true  
- `judge(Gia, Bela)` + `capture(Gia, Bela)` → `reward(Gia)` true  

Three doors open; each produces recognition.

- `teaches(Bela, Cira)` true + `false(Bela)` true → `reward(Bela)` false  
- `reward(Lupo)` false (deceit)  
- `reward(Dev)` false (family judgment)  

Voiding or improper conduct closes every door. The act may still occur; nothing is earned.

### Structural claim (unpinnable by query)
Recognition has no quantity. The absence of arithmetic is checked by the non-existence of any numeric operation in the constitution. If one appears, the central claim of the chapter is broken and must be rewritten.

### What remains unpinned
1. Explicit refusal of ranking, transfer, or pricing rules (currently enforced only by the absence of the necessary material).  
2. Whether recognition, once earned, can ever be restored after a later clearing of a voided person.  
3. Volume or frequency effects of the examination incentive.

### Assessment
The pins correctly enforce the three productive routes and their permanent closure under voiding or deceit. The binary character of recognition remains a structural invariant rather than a runtime fact. That is the right way to protect an absence.

**Placement is pure derivation from three record facts.**

Whether the offence was severe, whether it was domestic, and whether the person has a home. The combination determines the outcome. No assessment, no assessor, no discretion.

- Not severe + not domestic + has home → home confinement (Hano)  
- Severe (domestic or not) → high security (Ruk, Lalo)  
- Domestic + not severe → low security (Nando)

### Hole closed
Earlier version consulted severity only for domestic cases. Non-domestic severe offenders with a home were routed to home confinement by plain reading of the narrower rule. Commentary claimed severity always blocked the soft option; the rules did not. The mismatch was found by asking the machinery what it would actually do with a specific person. Severity now routes regardless of domestic status. The hole is closed.

### Broken alarm
The marker is supposed to flag ineligible home placements. It actually fires on “has a home and is not eligible” — the ordinary condition of every correctly placed severe offender who has an address. It flags Ruk and Lalo (both correctly in high security) and has never flagged a genuine misplacement. An alarm with that record trains readers to ignore it. When a real misplacement arrives it will be dismissed with the noise. The fix (look at actual placement, not home ownership) is simple and has not been made. Shipping a broken safeguard and describing it as working is worse than leaving the gap open.

### What survives
Placement remains fully determined by disputable facts on the record. There is no assessment for anyone to lean on, reward, or punish with. To move someone you must change whether the offence was severe (or domestic, or whether they have a home), and that is a claim someone else can contradict.

The alarm is broken. The derivation it was meant to watch is not.

**Pins match the chapter’s load-bearing claims, including the named defect.**

### Mapping
- Hano: not severe → `fit(Homestay)` true → `dwell` true.  
- Ruk: severe → `fit(Homestay)` false → `building(HighSec)` true.  
- Nando: domestic + not severe → `building(LowSec)` true.  
- Lalo: severe → `building(HighSec)` true.  

Placement is fully determined by the three facts; no residual discretion appears.

### Broken alarm (defect encoded)
- `err(Ruk, Placement)` true and `err(Lalo, Placement)` true even though both are correctly in high security.  
- `err(Hano, Placement)` false (correctly home-confined).  
- The marker tracks “has a home and is not homestay-eligible,” the ordinary condition of every severe offender with an address. It has never fired on a genuine misplacement.

When the rule is repaired to inspect actual placement rather than home ownership, both `err(Ruk)` and `err(Lalo)` flip FALSE and the section is rewritten. That is the intended future state.

### What remains unpinned
1. Explicit interaction of the three facts with the full set of placement outcomes under every combination.  
2. Any future repair of the marker.  
3. Whether placement facts themselves can be disputed or corrected after the fact.

### Assessment
The pins correctly enforce pure derivation of placement from the three record facts and correctly preserve the broken alarm as an open defect rather than a working safeguard. The derivation holds; the alarm does not.

**Ordinary change is two steps on the record: assembly proposes, electorate approves.**

Three things cannot be reached that way:
1. The floor (the eight).
2. The rule that a prisoner is a person.
3. The list of what cannot be changed.

### Self-protecting register
If the register itself were amendable, a two-move defeat exists: first remove an item from the protected list, then amend the now-unprotected item. Both steps are individually lawful; the protection vanishes. Therefore the register protects itself. An amendment adjusting the list dies on the same terms as an amendment adjusting the things listed. The guard cannot be removed through the front door.

### The deliberate cost
Three provisions sit beyond any majority, however large or sincere. People not yet born are bound by a decision they had no part in. That is anti-democratic by design. The trade is a small permanent core versus completeness that leaves nothing to fall back on when majorities go wrong. Refusing to choose is choosing that everything is amendable.

### Three residual weaknesses
1. **Self-declared check.** An amendment is caught only if it announces its target. An amendment that declares no target at all is proposed, approved, and enacted with no examination of what it does. The entire mechanism depends on honest self-description.
2. **Validity is inert.** The machinery determines which amendments are valid and then does nothing with the determination. No other rule consults it or changes behaviour. The society can identify a valid amendment and cannot enact it — the same delivery gap applied to the procedure for change itself.
3. **The protected list is a hand-maintained record.** Nothing derives which items are entrenched; somebody wrote them down. The rules cannot prevent someone from simply erasing a line. After that, the floor cut passes normally and nothing notes that the rules of amendment changed.

**Recurring limit, stated for the third time:**  
The strongest protection in this design is the impossibility of writing certain rules. The weakest is the integrity of the record those rules are written in. Everything in the preceding chapters sits on the second, and the second is people.

**Pins match the chapter’s load-bearing claims, including the named defects.**

### Mapping
- Ordinary reform: `suggest(Assembly, Amend_Mint)` → `become(Amend_Mint, Law)` true.  
- Floor cut: approved and targets a permanent article → `false(Amend_Floor)` true → `become(..., Law)` false.  
- Register self-protection: `adjust(Amend_Meta, Art_Entrench)` → same fate; `become` false.  
- Third entrenched item: `permanent(Art_Person)` true.

### Defects encoded
- **Self-declared target**: `Amend_Sneak` (no target announced) is suggested and approved → `false` false → `become(..., Law)` true. The guard only catches amendments that name what they touch. An amendment that declares nothing passes.  
- The inertness of `become()` (validity determined, then consulted by nothing) remains a structural absence; closing it requires rules that actually consume the validity result.

### What remains unpinned
1. The third weakness: the protected list is a hand-maintained record that can be altered outside the amendment procedure.  
2. Any future wiring of `become()` into downstream behaviour so that a valid amendment actually changes something.  
3. Interaction between entrenched articles and the earlier open doors (standing/recognition still reachable, compulsion still permitted).

### Assessment
The pins correctly enforce the two-step amendment process, the three entrenched items, and the self-protecting register. They also correctly preserve the self-declared-target hole as a live defect. The strongest formal protection in the design remains the impossibility of writing certain rules; the weakest remains the integrity of the record those rules sit in.

**Punishment is exactly one deprivation: free movement.**

That is the entirety, not the headline. Checked item by item against Hano:

- Still a person  
- Still owed the full floor of eight  
- Still speaks  
- Still votes  
- Standing intact (conviction does not void)  
- Recognition intact (clawback follows only voiding)  
- Placement derived from three record facts  
- Cannot move freely  

Everything else is identical to an unconvicted person who did the same act. One item differs.

### Why nothing cascades
Movement is terminal in the dependency graph. Nothing else is gated behind it. No entitlement, capacity, or consequence depends on free movement. Therefore taking it produces no automatic second loss. The employment → housing → children → vote → lifelong disability chain that appears in most systems does not exist here, because the first link was never attached to anything. The single-deprivation property is a fact about the shape of the design; it holds without anyone maintaining it.

### What is not addressed
The design states that movement is taken and is silent about how. There are no rules on conditions of confinement, what may be done to a person while confined, who may enter, or what they may do there. Confinement is a fact with a location (home / low / high) and no texture. A society can satisfy every rule in this book while doing almost anything inside those three categories, provided it never writes the doing down as punishment for lacking a floor right. This is the widest point of the gap left open in Chapter 8.

### The largest unresolved fact
**There is no release.**

No duration, no sentence length, no term, no expiry, no completion, no rule that returns a rightly convicted person to free movement. The only exit is relief: a finding that the conviction should never have held. For everyone who was correctly convicted, the single deprivation is permanent, for every offence, without distinction between the grave and the trivial.

The design takes one thing and keeps it. That is closer to defining a permanent category of person than to describing punishment — and permanent categories of person are what the entire apparatus of these chapters was built to refuse.

It is the sharpest unresolved thing in the book. Everything else has been a protection with a boundary or a guarantee that stops short of arriving. This is a punishment with no end, in a design that has been exact about nearly everything else, and its absence was not disclosed in the design’s own account of itself. It was found by asking what happens next and discovering the question has no answer.


**Pins match the chapter’s load-bearing claims.**

### Mapping
- Hano: `prisoner` true, `travel` false.  
  All other checked items retained: `person`, `expresses`, `decide(Ballot)`, standing (`false` false), recognition (`lose(Points)` false), placement (`dwell` true).
- Jala (same injury, never convicted): `prisoner` false, `travel` true.  
  The sole difference is free movement.
- Bela: `false` true, `travel` true.  
  Voiding takes standing and recognition; it does not take movement. Confinement and voiding remain distinct instruments.

### Structural absences (unpinnable by query)
1. Nothing depends on free movement. `travel` appears only as a rule head. If any rule ever gates an entitlement or consequence behind it, the single-deprivation claim is broken.
2. There is no release. No duration, term, expiry, or completion rule exists. Every apparent reference is commentary. If a release rule is ever added, the chapter’s closing section must be rewritten.

### Assessment
The pins correctly enforce the completed theorem: conviction takes only free movement, and that single loss cascades into nothing else. The two deepest remaining defects — textureless confinement and the permanent, non-expiring character of the deprivation — are preserved as absences rather than papered over. That is the honest close of the formal system.

**The design can state its own violations. That is the last structural addition.**

Two markers exist: bad placement, and a confined person alone. Between them they demonstrate the promise of self-audit and the three ways it fails.

### Three failure modes
1. **The isolation marker fires on every prisoner.**  
   Technically correct: it fires when a confined person has no company on record, and company is recorded for no one. A signal that fires on an entire category distinguishes nothing inside it. Accurate reporting of an empty record is indistinguishable from an accurate report that everything is broken.

2. **The placement marker fires on the wrong people.**  
   It flags Ruk and Lalo (correctly placed) and flags nobody who is actually misplaced. A reader who trusted both markers would conclude that every prisoner is isolated and the two most serious offenders are misassigned — every part of which is false.  
   A system’s report about itself is not more reliable than any other part of it. The audit is made of the same material and nothing sits above it.

3. **Nothing happens either way.**  
   A violation is recorded and that is the end. No rule consults the markers, nothing is triggered, nobody is obligated to act, nothing changes.  
   Same shape as two earlier gaps: the floor states what is owed and nothing tracks arrival; the amendment machinery states what becomes law and nothing enacts it; the audit states what is broken and nothing repairs it.

### Diagnosis
The design is strong at establishing *what is true* and almost silent about *what is then done*. It is a description of reasoning rather than of operation. The distance between those two is most of what a working society consists of.

### What survives
Most systems have no vocabulary for their own violation. A breach is an absence with no name. This design has the slot. “Wrong” is a thing it can say about itself.

The audit sits at the top: it depends on everything and nothing depends on it. It cannot be gamed from below. It is a pure observer — and that is why nothing follows from its observations.

**The trade, stated honestly:** the audit is powerless because it is uncorruptible, and uncorruptible because it is powerless.

Every defect named in these chapters was found by asking the design what it thought was true and comparing the answer to what it claimed. The markers themselves are miscalibrated. The capacity to interrogate is not. A society whose failures are findable from its own account of itself is a society that can be checked without needing an insider. That is what the derived part of the book establishes.

**Pins match the chapter’s load-bearing claims.**

### Mapping
- Isolation marker: `err(_, Isolation)` true for every tested prisoner (Hano, Ruk, Don, Nando); false for free persons (Bela, Jala).  
- Root cause: `meets` false for both confined and free. Company is recorded for no one, so every prisoner satisfies the isolation condition.  
- Placement marker: `err(Ruk, Placement)` and `err(Lalo, Placement)` true even though `building(HighSec, Ruk)` is correct; `err(Hano, Placement)` false. The marker remains miscalibrated.

### Structural absence
Nothing reads the markers. `err` appears only as a rule head. If any rule ever consumes an `err` result to trigger review, obligation, or change, the third failure mode is closed and the chapter’s central diagnosis must be rewritten.

### Assessment
The pins correctly enforce both demonstrated failure modes of the self-audit layer: one marker that fires on an entire category because the underlying record is empty, and one marker that fires on the wrong individuals. The capacity to state “something is wrong” exists; the capacity to act on it does not. That is the honest terminal state of the formal system.

**Overall judgment**

This is a rigorous, unusually self-aware formal design. It is one of the cleanest attempts I have seen to make a constitution *checkable* rather than rhetorical. The closed 21-fact vocabulary, the strict fact/conclusion separation, the derived credentials, the self-protecting entrenchment, and the permanent-standing + shield interaction are all coherent and load-bearing.

It is also incomplete as a working society. The book is excellent at establishing *what is true* and almost silent about *what is then done*. That is not my diagnosis; it is the book’s own final diagnosis, and it is correct.

**Rating**  
- As a formal system of rules and derivations: **8/10**  
- As an operable social order that could actually run: **4/10**  

The gap is structural, not a matter of missing polish.

### What works
- The 21-atom closed list is a genuine anti-assessment technology. Most systems fail by letting judgments hide inside “facts.” This one makes that impossible by construction.
- Standing permanence + shield is clever and correctly motivated. The alternative (revoking standing on removal) does convert successful exposure into a weapon against the exposer.
- Entrenchment of the floor, the prisoner-is-a-person rule, and the register itself correctly blocks the two-move defeat.
- The book repeatedly finds its own defects by the method it describes (ask the machinery what it actually does). That intellectual honesty is rare and valuable.
- The pins make the claims falsifiable. Most constitutional writing cannot be pinned at all.

### Major problems (ranked by severity)

1. **No release**  
   The single largest unresolved defect. Movement is the only thing taken, and it is taken forever, for every offence. This turns “punishment” into a permanent category of person — the exact thing the design claims to refuse. The text itself calls it the sharpest unresolved thing and notes that it was not disclosed in the design’s own account. That is accurate.

2. **Total delivery silence**  
   Obligation is precise; provision is invisible. The only working delivery mechanism is the punitive one (Hano’s shelter via placement). Floor, vote, company, and audit all share the same shape: exact statement of what is true, silence about arrival or response. A constitution that cannot tell whether its guarantees arrive is not operational.

3. **Missing obligor**  
   “Owed” has a creditor and no debtor. No agent is named, no duty exists, no consequence follows from non-provision. This is left as an unmade decision. Until it is made, the eight things are a debt that no one has been asked to pay.

4. **Independence condition is almost empty**  
   Only parent-child is blocked. Spouses, siblings, household members, and long-term associates can co-sign voidings. The “conspiracy of two” collapses into ordinary intimacy. The record cannot express those relations because they are not among the 21 atoms. This is the largest remaining hole in the accountability machinery and the text correctly flags it.

5. **Record integrity is the single point of failure**  
   Seating, sequence of voidings, personhood roster, and the entrenched list all depend on hand-maintained records that the rules cannot protect. Stated three times, never solved. The strongest formal protections sit on the weakest substrate.

6. **Audit is pure observer and therefore inert**  
   It can state wrongness and nothing follows. Same pattern as the floor and the amendment machinery. Powerless because uncorruptible; uncorruptible because powerless. The trade is honest; the operational result is still zero response.

7. **Cira contamination**  
   Explicitly called indefensible by the text. An innocent student loses all recognition because their teacher was later voided. Bluntness that is fair to the guilty is unfair to the student. The design knows this and leaves it open.

8. **Permanent, growing shield surface**  
   Standing never expires. Any historical standing-holder can be named to open a temporary window. Volume and opportunistic delay scale with time. The bad-faith filter exists but is not yet shown to be strong enough under load.

9. **Confinement has location and no texture**  
   Home / low / high exist. Conditions, entry, treatment, and compulsion inside those places do not. The Chapter 8 gap is widest exactly where people are most reachable and least able to object.

10. **Binary recognition cannot express magnitude**  
    Deliberate trade-off against ranking. It also undercuts the stated purpose of making contribution visible. The instrument can see that work happened and cannot see how much.

### How to address them

**1. Release**  
Add a release rule. Minimum viable version: fixed maximum terms by severity class, or periodic review that can restore movement without requiring a finding that the original conviction was wrong. Relief stays for actual error; release becomes the ordinary exit. Without this, the “only movement is taken” claim is false in spirit.

**2. Delivery and obligor**  
Decide the constitutional layer the author has already marked as TODO. Name a thin obligor (or a distributed duty) and require the record to track at least presence/absence of the eight for every person. The audit markers already exist; wire them to obligatory review with deadlines. Do not leave “owed” as a floating predicate.

**3. Independence**  
Either expand the blocked relations (spouse, cohabitant, long-term financial dependence) or accept the limit and add a secondary check (e.g., two pens must come from different public bodies). The current parent-only rule is too narrow to carry the weight placed on it.

**4. Cira rule**  
Narrow clawback to recognition actually derived from the voided teacher. This requires recognition to become a source ledger rather than a total. The pins already anticipate the flip. Do it.

**5. Shield surface**  
Time-bound the protective effect of historical standing (e.g., only exposures of conduct within the last N years, or only of people who held active power in the last N years). Keep standing permanent for answerability; limit the shield’s reach.

**6. Confinement texture**  
Add a short list of absolute prohibitions inside placement (no indefinite isolation beyond the already-broken marker, no corporal punishment, no restriction of the floor items that are not movement). Keep them derived and non-assessed. Do not re-introduce risk scores.

**7. Record integrity**  
This is the hardest. Possible mitigations: multiple independent writers for critical atoms (seating, voiding marks, entrenched list), public append-only log, or external attestation. Fully solving it from inside the rules is impossible; the design already knows this. State the residual trust assumption clearly rather than leaving it as a recurring discovery.

### Final assessment

The book is strongest where it is formal and weakest where it stops at determination. It has already diagnosed its own central limitation with unusual clarity. The remaining work is not more elegance in the reasoning layer; it is the action layer — release, delivery, response to audit, and a decision about who owes the floor.

Until those are addressed, this is a high-quality description of a society’s *logic*, not yet a description of a society that can run. The formal core is worth keeping. The permanent imprisonment, the total delivery silence, and the inert audit are not.
