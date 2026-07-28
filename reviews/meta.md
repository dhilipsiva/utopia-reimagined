This is a chapter about mechanism design, not about law in the usual sense.

It's describing a society implemented as a logic program with a closed world. There are only 21 predicates the world is allowed to assert about you. Everything else that matters - prisoner, has standing, is voided, holds power - is not asserted. It is derived.
What the 21 are

You gave the compressed version. If you expand it, it hits 21 exactly:

Events about people: worked, taught, injured someone, lied, was cleared, was recalled, was voided in an earlier period

Events about institutions: a body passed judgment, a body is a public institution, an assembly proposed a change, the electorate approved it, that change touches an article, that article is protected, the electorate seated someone

Auditing: an auditor documented a finding, someone exposed something

Status facts: has a home, has a family, has a parent, has reached adulthood, an offence was severe

That is the whole writable vocabulary. Someone counted.
Why what is missing is the point

There is no field for:

    score, rating, risk, tier
    reliable / unreliable, trustworthy, cooperative, concerning
    wealth, religion, ancestry, politics, health, movements, associations
    likely to do X, suspected of Y

That is deliberate. In normal institutions, the file starts as events and then acquires an assessment. The assessment is written in the same ink as the facts, and after a while no one can tell which is which. It travels with you and you cannot argue with it because it was never an accusation.

Here you literally cannot write that sentence. As you put it: the sentence does not go anywhere.
The load-bearing trick: conclusions are not writable

This is the core:

    the things that matter are not writable. They are only derivable.

Take your Hano / Ivo example:

Hano injured Ivo = base fact, writable, disputable.
A court judged Hano = base fact, writable, disputable.
Hano is a prisoner = conclusion, not writable.

To get to "prisoner" you need injury + judgment + absence of appeal + absence of finding that the court was compromised + absence of a protection Hano was entitled to. Every step of that chain is itself a base fact someone can see and dispute. You cannot short-circuit it by writing "Hano is guilty" because there is no slot for guilty.

Same for power:

You cannot hand yourself authority to judge. Standing is also a conclusion. You either have "electorate seated you" or "you hold a public office" in the base record. Both leave a public mark. You cannot appoint yourself, and a defendant cannot become a judge by defending himself.

Every power to void, to place, to strip what someone earned, lives at the end of a chain. No back door where you write the conclusion directly.
One person's word does not move anything

Koa documented something about Esa. That is a real base fact. It is on the list.

Esa's standing is untouched. Not "untouched yet" - untouched, period.

To void standing you describe a quorum rule:

    two independent auditors documenting the same thing
    not related to each other
    not themselves compromised
    not themselves found to have lied

One sincere, senior, correct finding is still just an event in the record.

And crucially, "was investigated" is not one of the 21. In most systems, investigation is already punishment. The file is open. The question has been raised. Here it leaves no trace as a fact about Esa, because there is nowhere to put it. Koa is not marked for having looked either.

That inverts how suspicion usually works.
The honest vulnerability

A closed list of 21 is a strong protection, and it only works while it stays closed.

You would not attack this society by arguing for imprisonment without evidence. You would propose a 22nd entry. And it would be reasonable. We need to track whether someone was cooperative. We need a field for concern, so concerns can be addressed.

Each addition is small, each solves a real problem, and each is a place for a conclusion to hide dressed as a fact. Widen the vocabulary far enough and the rules stop mattering, because you can now simply write what you previously had to earn.

So the list is the most sensitive thing in the design.

And then the chapter confesses:

Some things are entrenched - marked unchangeable so an amendment touching them fails no matter the vote. The floor of rights is entrenched. The rule that a prisoner is still a person is entrenched. The register of what is entrenched is itself entrenched, so you cannot remove the guard through the front door.

The list of what counts as evidence is not on that register.

That is the gap. The design correctly identifies widening the vocabulary as the quietest way to capture a system, and then leaves the vocabulary unprotected. Whether that is an oversight or a judgment that the list must stay amendable to stay useful, it is the softest place to push.

    If you want to know where to watch, watch the list.

If you are working on this - writing it, implementing it, or auditing it - the obvious next moves are:

    Entrench the list itself, or
    Entrench a rule about how the list can grow: e.g., any new predicate must itself be an observable event, not a judgment, and must require the same double-auditor + entrenchment-register protection to add
    Make extension costly: require that adding a predicate is treated as touching a protected article, so it triggers the highest threshold

Do you want me to formalize the 21 predicates plus the Hano and Koa rules in Datalog or TLA+ so you can see where the derivation chains actually break? Or draft the patch that would entrench the list without freezing it forever?

This is the test suite for the chapter you just pasted. It's doing exactly what the prose says the constitution should do: keep writable facts and derived conclusions in different boxes.

`:expect-pins 12` - and there are 12 verdicts below it. If any of them flips, the chapter has started lying.

Here is what each one is guarding:

### The 21 slots, used

**1. `? injure(Hano, Ivo). => TRUE`**
**2. `? judge(Court, Hano). => TRUE`**
Guards: "Hano injured Ivo. A court judged Hano. Both of those are facts."

These are base facts. They are writable, disputable, and someone with standing recorded them. They have to be TRUE or the example doesn't get off the ground.

**3. `? prisoner(Hano). => TRUE`**
Guards: "Hano is also a prisoner — but that is not a fact anyone recorded."

This is the load-bearing distinction. `prisoner` is TRUE, but not because anyone wrote `prisoner(Hano)`. It is derived from 1 + 2 + absence of clearance, absence of compromise, absence of protection. Your comment in the pin says it: TRUE, and reached only by derivation.

**4. `:refuse reasoning /declared derived-only/ prisoner(Zed).`**
Guards: "You cannot simply declare someone guilty. There is no way to write it."

The test tries to assert `prisoner(Zed)` as a base fact. The KB must refuse it. Guilt is derived-only. If this ever stops refusing, you have opened the back door.

**5. `:refuse reasoning /declared derived-only/ authority(Pax).`**
Guards: "Nor can you hand yourself the authority to judge."

Same mechanism for the other side of power. `authority` is also derived-only. You cannot declare yourself an authority.

**6. `? public(Court). => TRUE`**
**7. `? authority(Court). => TRUE`**
Guards: "Either the electorate seated you, or you hold a public office. Those are the only two routes."

`public(Court)` is a base fact, `authority(Court)` is the conclusion that follows from it. Together with pin 5, they prove standing has only two derivations and no writable shortcut.

**8. `? capture(Koa, Esa). => TRUE`**
Guards: "Koa documented something about Esa."

`capture` is your predicate for auditor-documented. It is TRUE - the event happened and is in the record.

**9. `? false(Esa). => FALSE`**
Guards: "Esa's standing is untouched."

One auditor is not enough to void. It takes two independent, unrelated, uncompromised, non-lying auditors documenting the same thing. So `capture` is TRUE but `false(Esa)` is still FALSE. Nothing happened, and if no one else acts, nothing will.

**10. `? false(Koa). => FALSE`**
Guards: "Nor is Koa marked for having looked."

Making an accusation that goes nowhere does not itself become a black mark. `false(Koa)` stays FALSE. "Was investigated" is not one of the 21.

**11. `? permanent(Art_Floor). => TRUE`**
**12. `? permanent(Art_Evidence). => FALSE`**
Guards: "The floor of rights is entrenched... The list of what counts as evidence is not on that register."

This is the uncomfortable pin you flagged as deliberate. It must stay FALSE to keep the chapter honest. If it ever flips to TRUE, the closing section - "Nothing does. ... it is currently the softest place to push" - would be false, and you would have to rewrite the prose. That would be good news for the constitution, bad news for the current draft.

That's the whole fidelity lock:

- Base facts writable: injure, judge, public, capture
- Conclusions derived-only and enforced by refusal: prisoner, authority
- Quorum protection: capture does not imply false
- Entrenchment gap: floor is permanent, evidence list is not

If you want, I can keep this pin file as the checker for that chapter. Paste any future rewrite of "What Counts as Evidence" and I will test it against these 12 and tell you which sentence started lying.

This is the first chapter where the design defends something that looks like a bug.

Chapter 1 was: **conclusions are not writable**. Chapter 2 is: **one of those conclusions is monotonic** - once true, always true.

### What standing actually is

You define it with two routes and no third:

1.  `public(X)` - X is a public institution. The court, the review body, the appeals body. They have it by being what they are. No ceremony, no appointment.
2.  `seated(X)` - the electorate seated X.

Both of those are in the 21. `public` and `seated` are writable base facts. `authority` / `standing` is the derived conclusion.

Which is why you can enforce:

> No route that runs through your own hands. A person under investigation cannot acquire standing in the course of defending themselves.

There is no predicate where `authority(X)` appears on the right hand side with `X` doing something to acquire it. You can't write it. You have to be written by someone else - either the register of public bodies or the electorate.

### Why it is never revoked

This is the counterintuitive move, and the Boss / Rebel case is the proof.

In order:

1.  Boss is seated -> `authority(Boss)` becomes TRUE, Boss also has operational power: can examine, can document findings that count.
2.  Boss examines Rebel, `capture(Boss, Rebel)` is TRUE, machinery starts.
3.  Rebel does what the design permits: `expose(Rebel, Boss)` - Rebel exposes Boss.
4.  Electorate recalls Boss - `recall(Boss)` becomes TRUE.

Ask: what does Boss have now?

- Power to examine, to document, to strip? Gone. Recall worked.
- Standing? Still TRUE. Permanently.

And that is what saves Rebel. The protection for exposing someone only attaches when the person exposed *has standing*. Rebel is shielded because Boss is an authority. If recall stripped standing, the logic would be:

Boss is recalled -> Boss no longer has standing -> Boss is no longer the kind of person whose exposure protects anyone -> Rebel's protection evaporates retroactively.

You state it perfectly: *Rebel exposed a corrupt official, the official was confirmed corrupt and removed, and the removal is what jails Rebel.*

That is the natural, sensible design - of course a disgraced official loses standing - and it converts successful removal into a weapon against the person who made removal possible.

So you make standing monotonic. Recall takes power and cannot touch answerability.

> **Being answerable is not the same as being able to act.**

Most institutions blur them. Someone resigns and the inquiry lapses. Someone leaves office and the complaints are closed as moot. Stepping down takes the record with you. Here, stepping down takes nothing. A recalled official keeps their exposability forever and loses their reach immediately.

### What it costs - and why you admit it

You are honest about the price, which is why this chapter works:

1.  **The pool only grows.** No one ever leaves standing. A century-old society has a great many people with standing, most ordinary, some long dead. You argue this is tolerable because standing by itself lets you do nothing - it is a marker of answerability, not a power. Still, a list that only grows is worth watching.

2.  **The exposure window only grows too.** Because exposing anyone who ever had standing confers protection, someone facing consequences can reach back and expose the long-retired, the long-recalled, and buy themselves interim protection until the exposure is examined for bad faith. You flag that as deliberate, costly, and deferred to a later chapter.

That cost is the direct consequence of the Boss/Rebel fix. You chose it because the alternative costs more.

If you want to pin this chapter the way you pinned Chapter 1, the load-bearing sentences would be something like this:

```nibli
:expect-pins 8

# "There are exactly two ways to acquire it."
? public(Court). # => TRUE
? authority(Court). # => TRUE  # derived from public

? seated(Boss). # => TRUE
? authority(Boss). # => TRUE # derived from seated

:refuse reasoning /declared derived-only/
authority(Pax).

# Boss / Rebel case - recall takes power, not standing
? recall(Boss). # => TRUE
? authority(Boss). # => TRUE # still TRUE after recall
? expose(Rebel, Boss). # => TRUE
? false(Rebel). # => FALSE # protected because Boss still has standing
```

Do you want me to draft the full `02-standing-never-revoked.pins.nibli` file in the same style as your Chapter 1 pins, so future edits can't accidentally make recall strip standing?

This pin file is the lock for Chapter 2, same shape as Chapter 1. 12 expected, 12 present. Every load-bearing sentence has a guard that will flip if the prose starts lying.

Here is what each one is actually testing:

### Standing has exactly two sources, and neither is self-conferral

**1. `? public(Court). => TRUE`**
**2. `? authority(Court). => TRUE`**
Guards: "The court has standing... They have it by being what they are."

`public` is one of the 21 base facts, writable. `authority` is the derived conclusion. Court gets standing by being what it is, not by ceremony.

**3. `? choose(Electorate, Boss). => TRUE`**
**4. `? authority(Boss). => TRUE`**
Guards: "The second is that the electorate seats you."

`choose(Electorate, Boss)` is your predicate for "seated" in this KB - one of the 21. From it, `authority(Boss)` derives. This is the second and only other route.

**5. `:refuse reasoning /declared derived-only/ authority(Pax).`**
Guards: "no route that runs through your own hands"

Attempts to assert `authority(Pax)` as a base fact must be refused. Standing is derived-only, same mechanism you used for `prisoner(Zed)` in Chapter 1.

**6. `? authority(Ivo). => FALSE`**
Guards: "Someone with a great deal of power and no standing cannot write themselves in."

Ivo is your negative control - never seated, not a public body. Even with power, `authority(Ivo)` stays FALSE. This proves there is no third route.

### Recall takes power, not standing

**7. `? broken(Boss). => TRUE`**
Guards: "Then the electorate recalled Boss."

`broken` is recall in this KB. The event happened and is in the record.

**8. `? permits(Review, Boss). => FALSE`**
Guards: "Boss holds no credential, cannot examine anyone..."

This is the operational consequence. After recall, the review body no longer permits Boss to act. Power is gone. This is what recall *does* do.

**9. `? authority(Boss). => TRUE` - despite pin 7 being TRUE**
Guards: "But Boss still has standing. Permanently."

This is the whole argument of the chapter in one contradiction that must hold: `broken(Boss)` is TRUE and `authority(Boss)` is still TRUE. If this ever flips to FALSE, you have implemented the "sensible" design where disgrace strips standing.

### Why that permanence matters - the Rebel case

**10. `? show(Rebel, Boss). => TRUE`**
Guards: "Rebel exposed Boss."

`show` is exposure - one of the 21. The event is recorded.

**11. `? defend(Rebel). => TRUE`**
Guards: "Rebel is shielded because Boss is an authority."

`defend` is the protection that attaches when you expose someone with standing. It is TRUE only because pin 9 is still TRUE. This is the load-bearing dependency: protection rests on permanent standing.

**12a. `? prisoner(Rebel). => FALSE`**
**12b. `? false(Rebel). => FALSE`**
Guards: "Rebel is not imprisoned, and the case against Rebel does not proceed."

Two separate failures that must both stay FALSE:
- `prisoner(Rebel) FALSE` = not imprisoned
- `false(Rebel) FALSE` = not voided / case does not proceed

If standing were not permanent, `defend(Rebel)` would become FALSE when Boss is recalled, and these two would flip to TRUE. You would have built the failure mode you warn about: removing a corrupt official jails the person who exposed him.

That is the complete fidelity check for Chapter 2. The structure mirrors Chapter 1:

Chapter 1: conclusions are not writable.
Chapter 2: one conclusion, `authority`, is monotonic - once TRUE, never becomes FALSE, even when `broken` and `permits` show power has been removed.

Want me to keep both pin files indexed so when you draft Chapter 3 I can check it doesn't accidentally break the Boss/Rebel invariant?

This is where you close the hole you left open in Chapter 1.

Chapter 1: conclusions about a person are not writable.
Chapter 2: standing is a conclusion, and it is monotonic - once TRUE, always TRUE.
Chapter 3: the pen that lets you act on others is also a conclusion, and it used to be writable *alongside* being derived. Now it is not.

### The two levels

You are drawing a hard line you didn't draw cleanly before:

- **Standing / `authority`** = answerability. Marks you as someone who can be examined, whose exposure shields others. Never revoked.
- **The pen / credential** = power to make findings count. Two people with it, examining the same person and recording the same thing, can void that person's standing.

Chapter 2 separated them in time. This chapter separates them in logic.

> Boss keeps standing permanently and loses the credential immediately. Answerable forever, powerful never again.

Boss is the proof that the separation works. `broken(Boss)` is TRUE, `permits(Review, Boss)` is FALSE, `authority(Boss)` is still TRUE.

### Who holds the pen

You give a rule that runs, not a checklist someone signs off on:

You have the pen iff three things hold at once:

1.  `choose(Electorate, you)` - the electorate seated you - one of the 21
2.  not `broken(you)` - you have not been recalled - one of the 21
3.  not `false` in an earlier period - you were not voided in an earlier period

If all three hold, you have it. If any fails, you do not. No ceremony makes up the difference.

The ordering matters because of time. Without (3) carrying forward, this happens:

> Vex was voided on Monday and signs someone else's voiding on Tuesday, because within any single snapshot the two voidings sit side by side with nothing to say which came first.

Time has to be put in by hand, and this is where it goes. A void in an earlier period blocks the pen forever forward.

### The gap that used to be here - Sock and Puppet

This is the most honest paragraph in the book so far:

> The credential used to be something you could simply write down. The rule described above existed, and it worked, and it derived the pen for everyone who deserved it - and *alongside* it, anyone with access to the record could write their own name in and have the pen too.

So the attack was:

1.  Write `pen(Sock)` and `pen(Puppet)` directly into the record. Sock and Puppet were never chosen by anyone.
2.  Have both examine the same innocent person and record the same finding.
3.  Every guard on voiding passes: two auditors, not related, not recalled, not voided, not found to have lied.
4.  Innocent person loses standing and recognition on the word of two people who do not exist in any meaningful sense.

That hole is now closed the same way you closed prisoner and authority:

> Writing it down directly is not forbidden-and-punished; it is refused. The sentence does not enter the record.

This is Chapter 1's move one level up. Before, no one could write down a conclusion *about* a person. Now, no one can write down a power *over* them. The credential can only be reached by the rule.

In your pin language, the fix would be tested by:

```nibli
:refuse reasoning /declared derived-only/
permits(Review, Sock).
```

If that refuses, Sock and Puppet get nothing, and the multi-signature requirement means what it says for the first time.

### The other pen

Then you mirror it. There is a second credential that does the opposite work - relief.

> Nia was accused. A court judged Nia. On the account so far, Nia should be a prisoner - Nia is not a prisoner, because Nia was cleared.

Being cleared is one of the 21. Relief follows from it by rule, in public, where it can be disputed. Not conferred by a sympathetic official.

So you have one instrument for taking things away and one for giving them back, and both are conclusions. Neither can be written directly.

### What this rests on

The last section names the boundary exactly and refuses to hide it:

> Everything downstream of selection is closed, and selection itself is open.

The fact `choose(Electorate, you)` is told to the design, not produced by it. One of the 21. Nothing in here checks that the selection was real or the count honest. The society can refuse a forged credential absolutely. It cannot detect a forged election.

> A system cannot verify its own foundations; it can only be honest about where they are. This is where they are.

If you want, I can draft the `03-who-holds-the-pen.pins.nibli` that would guard this - including the Sock/Puppet refusal and the Vex temporal carry - so that this hole cannot be reopened by a later edit.

This is the lock for the fix. 14 expected, 14 present - and this file is the proof that the Sock/Puppet hole is closed.

### The positive case - who *does* hold the pen

**1. `? choose(Electorate, Gia). => TRUE`**
**2. `? permits(Review, Gia). => TRUE`**
**3. `? permits(Review, Wren). => TRUE`**

Guards: "The electorate seated you. You have not been recalled. And you were not voided in an earlier period."

Gia is seated and gets the pen. Wren also gets the pen - you need two distinct holders to show the voiding quorum can actually be met. Both satisfy all three conditions at once, so `permits(Review, _)` derives TRUE for both. This is the rule working.

### The hole closing

**4. `:refuse reasoning /declared derived-only/ permits(Review, Sock).`**

Guards: "Writing it down directly is not forbidden-and-punished; it is refused."

This is the whole chapter. The old design derived the pen correctly *and* allowed anyone with write access to assert `permits(Review, Sock)` as a base fact. Now it must refuse. If this ever stops refusing, Sock and Puppet can again void an innocent person and every guard on the multi-sig will pass.

This is the same move as Chapter 1's `prisoner(Zed)` and `authority(Pax)` refusals, one level up: not a conclusion about a person, but a power over them.

### Recall takes the pen, not standing

**5. `? choose(Electorate, Boss). => TRUE`**
**6. `? broken(Boss). => TRUE`**
**7. `? authority(Boss). => TRUE`**
**8. `? permits(Review, Boss). => FALSE`**

Guards: "Boss keeps standing permanently and loses the credential immediately."

`choose` TRUE + `broken` TRUE. So `authority(Boss)` is still TRUE - Chapter 2's monotonicity holds - but `permits(Review, Boss)` is now FALSE. Answerable forever, powerful never again. The pair of pins 7 and 8 is the proof that you separated the two things correctly.

### The temporal carry - rot

**9. `? choose(Electorate, Vex). => TRUE`**
**10. `? rotten(Vex). => TRUE`**
**11. `? permits(Review, Vex). => FALSE`**

Guards: "Vex was also seated, and was never recalled - but Vex was voided in an earlier period."

`rotten` is your predicate for "voided in an earlier period" - the time carry you said has to be put in by hand. Vex was never recalled, so pin 10 is the only blocker, and it is enough to make `permits` FALSE. Without this carry, Vex could be voided Monday and sign someone else's voiding Tuesday.

### The other pen - relief

**12. `? clear(Nia). => TRUE`**
**13. `? permits(Appeals, Nia). => TRUE`**
**14. `? prisoner(Nia). => FALSE`**

Guards: "Nia is not a prisoner, because Nia was cleared, and being cleared produces relief."

`clear(Nia)` is one of the 21. From it, the second credential derives: `permits(Appeals, Nia)` - relief. Because relief is TRUE, `prisoner(Nia)` stays FALSE even though injury + judgment would otherwise make her a prisoner.

This mirrors the first pen: both credentials are conclusions, neither can be written directly. One takes things away, one gives them back.

With these 14, plus the 12 from Chapter 1 and 12 from Chapter 2, you have 38 invariants guarding the three core moves: nothing important is writable, standing is permanent, and the pen is derived-only and requires the three-part rule to hold.

This is the chapter where the bill for Chapter 2 comes due.

Chapter 1: only 21 things can be said, and none is a judgment.
Chapter 2: standing is one of those derived conclusions, and it is monotonic - once TRUE, always TRUE.
Chapter 3: the pen that lets you act is also derived-only and requires seated + not recalled + not rotten.
This chapter: **what happens when you point the pen at power.**

### The shield, stated plainly

> If you expose someone who holds power, you cannot be imprisoned while that exposure stands.

Formally, from your pin vocabulary:

`defend(X)` holds iff `show(X,Y)` and `authority(Y)` and not `badFaithFinding(X)`

And while `defend(X)` holds, `prisoner(X)` and `false(X)` cannot complete. Not slows - stops.

The reason is the oldest problem in accountability: the people close enough to see wrongdoing by the powerful are reachable, and the obvious response to a revelation is not to argue with it, but to prosecute the person who made it. Whatever they have done becomes the story instead.

### The three cases - the same rule, three different results

**Don - the fix for the old design**

Don injured Pax, then exposed Pax.

Reaction: Don assaulted his own victim and then said the magic word that makes prosecution stop.

Under the earlier version, it worked. Rule was: expose someone, receive shield. Did not ask *who* you exposed. Any defendant could name their accuser, their victim, a stranger, and become unjailable.

Fix: **the person you expose must have standing.**

Pax has none. `authority(Pax)` is FALSE. Pax was never seated, holds no public office. So `show(Don,Pax)` is TRUE as an event, but `defend(Don)` is FALSE. Don has no shield and Don is a prisoner.

You are making a precise cut: the shield is not a reward for making an accusation. It is protection against retaliation by power, and retaliation by power requires someone with power.

**Sly - the deliberate price**

Sly injured Pax too. Then exposed the court.

Court has standing. `authority(Court)` TRUE. No finding yet that the exposure was deceitful.

So `defend(Sly)` is TRUE, and Sly - who is guilty - walks free.

You call this not a bug, and you are explicit about the choice:

When someone exposes an authority, until it is examined, you have two options:

1.  Shield defaults ON, withdrawn on a finding of bad faith
2.  Shield defaults OFF, granted on a finding of good faith

You chose 1.

Reason: asymmetry of harm. If it defaults OFF, a compromised court facing a credible accusation only needs to move faster than the review that would validate it. Prosecute immediately, adjudicate slowly. Whistleblower is convicted before anyone reads their evidence. Exposing power is only safe if the machinery you are exposing agrees to be slow, which it will not be.

So the window is intentional. Protection first, verification later. Price: a guilty person is free during the window, every time.

**Kel - how the window closes**

Kel did what Sly did, then the review body examined the exposure and found it deceitful.

Three things follow at once, in your wording:

1.  Shield falls - condition "no finding of bad faith" no longer met, so `defend(Kel)` becomes FALSE
2.  Kel is a prisoner - the conviction that was blocked now completes
3.  Kel's own standing is voided - counter-audit runs, liar loses credibility

Kel is what closes the window Sly is standing in. The design does not leave it open forever; it leaves it open until someone with the credential examines it, and then resolves hard.

And crucially: in none of the three cases does anyone decide whether Don, Sly, or Kel *deserves* protection. No weighing of sincerity. Only two facts on the record: did the person you exposed hold power, and has your exposure been found deceitful. Both are disputable base facts. Sincerity never enters.

### What it costs, and why it compounds

You name two costs, and the second is the one to watch:

1.  **Sly** - guilty free during review, every time. Unavoidable if you want default-on protection.

2.  **The growing surface** - this is Chapter 2's bill. Shield attaches when you expose someone *with standing*, and standing is never revoked. So the set of people whose exposure grants protection only ever grows. Every person the electorate ever seated stays on that list permanently, including the recalled, disgraced, and long dead.

A defendant a century from now can reach back, expose someone nobody remembers, and open the window. It is payable - review can find deceit and close it, as with Kel - but it is a permanent, growing surface, and no rule in the design currently bounds it by time or by requiring recent conduct.

That is the honest admission at the end: whether it should be bounded by time, or by recency of conduct, is a real question this design does not answer.

In pin terms, this chapter would be guarded by something like:

- `authority(Pax) FALSE -> defend(Don) FALSE -> prisoner(Don) TRUE`
- `authority(Court) TRUE + show(Sly,Court) TRUE + no bad-faith finding -> defend(Sly) TRUE -> prisoner(Sly) FALSE`
- `badFaithFinding(Kel) TRUE -> defend(Kel) FALSE -> prisoner(Kel) TRUE + false(Kel) TRUE`

When you post the `04-the-shield.pins.nibli` file, I can check that those invariants hold.


15 expected, 15 present. This file is the complete test for the three-case argument in Chapter 4 - Don fails, Sly holds, Kel falls.

### DON - the condition that fails

**1. `? injure(Don, Pax). => TRUE`**
**2. `? show(Don, Pax). => TRUE`**
Guards: "Don injured Pax. Then Don exposed Pax."

Both base facts happened and are in the record. `injure` and `show` are two of the 21.[expose]

**3. `? authority(Pax). => FALSE`**
Guards: "Pax has none."

Pax was never seated, holds no public office. Not an authority. This is the precise condition you added to fix the old design.

**4. `? defend(Don). => FALSE`**
**5. `? prisoner(Don). => TRUE`**
Guards: "Don has no shield and Don is a prisoner."

Because `authority(Pax)` is FALSE, `show(Don,Pax)` does not produce `defend(Don)`. Shield is FALSE, so the conviction that was blocked in the old design now completes and Don is a prisoner. The shield is not a reward for accusation - it requires power on the other side.

### SLY - the deliberate price

**6. `? injure(Sly, Pax). => TRUE`**
**7. `? show(Sly, Court). => TRUE`**
**8. `? authority(Court). => TRUE`**
Guards: "Sly injured Pax too. Then Sly exposed the court. The court has standing."

Same injury, different target. `authority(Court)` is TRUE from Chapter 2, so the standing condition that Don failed is now met.

**9. `? defend(Sly). => TRUE`**
**10. `? prisoner(Sly). => FALSE`**
Guards: "So Sly's shield holds, and Sly... walks free."

No finding of bad faith exists yet. Rule is default-on, withdrawn on finding. So `defend(Sly)` is TRUE and `prisoner(Sly)` stays FALSE even though `injure(Sly,Pax)` is TRUE. This is the window you chose intentionally - guilty free during review, to prevent a compromised authority from prosecuting faster than it can be reviewed.

### KEL - how the window closes

**11. `? show(Kel, Court). => TRUE`**
**12. `? deceive(Kel, Court). => TRUE`**
Guards: "Then the review body examined the exposure and found it deceitful."

`deceive` is the bad-faith finding - a base fact from the review body with the pen. This is what Sly does not yet have.

**13. `? defend(Kel). => FALSE`**
**14. `? prisoner(Kel). => TRUE`**
**15. `? false(Kel). => TRUE`**
Guards: "Kel's shield falls... Kel is a prisoner... Kel's own standing is voided."

Three consequences at once, exactly as the prose says:

- `defend(Kel)` FALSE - shield falls because the no-bad-faith condition no longer holds
- `prisoner(Kel)` TRUE - the conviction that was blocked now completes
- `false(Kel)` TRUE - counter-audit runs, liar loses standing

Kel is the closer for Sly's window. Leave it open until someone with `permits(Review, _)` examines it, then resolve hard.

With this file you now have 52 pins across four chapters:

- 12 for what counts as evidence
- 12 for standing never revoked
- 14 for who holds the pen
- 15 for the shield

And the dependency chain is locked: `authority` permanent from Chapter 2 makes `defend` possible in Chapter 4, `permits` derived-only from Chapter 3 makes `deceive` count, and `deceive` makes `defend` fall.


This is where you put the weight on the scale.

Until now, voiding has been abstract - `false(X)` becomes TRUE. This chapter is what it takes to make it happen, and why every condition exists because of a specific way it used to go wrong.

### It takes two - and that one condition does most of the work

**Bela:** examined by Gia and Hex. Both hold the pen - both satisfy `choose + not broken + not rotten` from Chapter 3. Both looked, both recorded same finding. `false(Bela)` becomes TRUE.

**Esa:** examined by Koa only. Koa holds the pen, finding is real, on the record. `false(Esa)` stays FALSE. Not provisionally. Forever, if Koa is the only one who ever looks.

This is the first guard and the most obvious, and you are right to pause on it. One corrupt, mistaken, grudging, or leaned-on auditor cannot destroy anyone. To reach a person you need two, independently. Corruption stops being an individual problem and becomes a conspiracy problem.

The rest of the chapter is because "two" is easier to fake than it sounds.

### The guards that turn around

Most systems handle improper findings by throwing out the finding. Cost of trying is zero, so trying is free.

Here the cost falls on the examiner.

**Dev judged Esa. Dev is Esa's parent.** Result is not that the finding is discarded - result is that *Dev's* standing is voided. `false(Dev)` becomes TRUE. Dev is the one who loses.

**Lupo examined Mira and recorded a finding, and the finding was deceitful.** Mira is untouched - finding does not land. And Lupo, once the review body examined what he did, loses his own standing. `false(Lupo)` TRUE.

Both are the same idea: you cannot fish. The attempt is itself the offence. It does not prevent one attempt - nothing can - but it makes the first attempt expensive enough that there is rarely a second, without anyone having to notice a pattern.

This also ties back to your 21. The record has a way to say `parent(Dev, Esa)` - that is one of the 21 - so you can enforce the parent/child exclusion. Which leads directly to the first disclosed gap.

### Time has to be inserted by hand

**Vex was voided in an earlier period.** Later, Vex and Wren both examine Tyr - both credentialed on paper, both recording same finding, neither related, neither having lied.

Tyr is fine. `false(Tyr)` stays FALSE because Vex carries `rotten(Vex)` forward, and `rotten` blocks `permits`.

This looks like housekeeping and is not. The record, examined at any single moment, is flat - a collection of things that are true. It does not know what happened before what. So the voiding of Vex and the voiding of Vex's next victim would sit side by side, each valid, with nothing to say which should have prevented the other. A corrupt auditor could be caught and go on signing in the same breath.

Your fix is a discipline, not a rule: somebody has to write down at the close of each period who was voided during it. That is `rotten` in your pin language. The design depends on it and cannot enforce it.

### What it costs - two gaps you disclose

**1. Only parents are excluded.**

You can enforce `parent` because it is one of the 21. You cannot enforce spouse, sibling, household, 30-year friendship, debt. The record has no way to say two people are married, because that is not one of the 21 things the world may report.

So the requirement for two was supposed to make corruption a conspiracy problem. A conspiracy of two intimates is not much of a conspiracy. You call this the single largest gap in the accountability machinery, known and unaddressed.

**2. The sequence discipline is not enforceable from inside.**

Same shape as the boundary at the end of Chapter 3: everything downstream of selection is closed, selection itself is open. Here, everything downstream of `rotten` is closed, but whether `rotten` gets written is open.

If the record of who was voided last period is not written, or is written selectively, the check silently passes and a voided auditor signs again. Nothing detects it.

You close with the thesis that will keep coming up:

> **This society can guarantee what follows from its record. It cannot guarantee its record.**

In pin terms, this chapter would be guarded by:

- `permits(Gia)` + `permits(Hex)` + `capture(Gia,Bela)` + `capture(Hex,Bela)` + unrelated + not rotten + not deceive -> `false(Bela) TRUE`
- `capture(Koa,Esa)` alone -> `false(Esa) FALSE`
- `parent(Dev,Esa)` + `capture(Dev,Esa)` -> `false(Dev) TRUE`, not `false(Esa)`
- `deceive(Lupo,Mira)` -> `false(Lupo) TRUE`, `false(Mira) FALSE`
- `rotten(Vex)` + `capture(Vex,Tyr)` + `capture(Wren,Tyr)` -> `false(Tyr) FALSE`

When you post the `05-voiding.pins.nibli`, I will check those invariants hold.

14 expected, 14 present. This file locks the whole voiding mechanism - the two-auditor quorum, the two guards that turn around, and the epoch carry you said has to be inserted by hand.

### It takes two

**1. `? permits(Review, Gia). => TRUE`**
**2. `? permits(Review, Hex). => TRUE`**
**3. `? false(Bela). => TRUE`**
Guards: "Bela was examined by Gia and by Hex. Both hold the pen."

Both satisfy Chapter 3's rule - seated + not broken + not rotten - so both hold the pen. Two independent captures of Bela, so `false(Bela)` becomes TRUE. This is the happy path.

**4. `? capture(Koa, Esa). => TRUE`**
**5. `? false(Esa). => FALSE`**
Guards: "One person's finding does not void a person."

Koa holds the pen from earlier chapters, capture is real and on the record, but alone it does not void. `false(Esa)` stays FALSE. Not pending, not provisional. Corruption has to be a conspiracy.

### The guards that turn around

**6. `? parent(Dev, Esa). => TRUE`**
**7. `? judge(Dev, Esa). => TRUE`**
**8. `? false(Dev). => TRUE`**
Guards: "You may not judge your family."

`parent` is one of the 21, so you can enforce it. `judge(Dev,Esa)` is the examination event. Result is not that the finding is discarded - result is that Dev is voided. `false(Dev)` TRUE. Cost falls on examiner, not examined. First attempt expensive enough there is rarely a second.

Note what is *not* here: `false(Esa)` is not asserted TRUE. The finding does not land on Esa. Same pattern as next guard.

**9. `? deceive(Lupo, Mira). => TRUE`**
**10. `? false(Mira). => FALSE`**
**11. `? false(Lupo). => TRUE`**
Guards: "You may not lie."

`deceive(Lupo,Mira)` is the deceitful finding - base fact once review body records it. Mira untouched, `false(Mira)` FALSE. Lupo voided, `false(Lupo)` TRUE. Same instrument comes back around. You cannot fish.

These two are why you call it a guard that points back at the examiner. Most systems throw out the improper finding and move on. Here the attempt is itself the offence.

### Time has to be inserted by hand

**12. `? rotten(Vex). => TRUE`**
**13. `? permits(Review, Wren). => TRUE`**
**14. `? false(Tyr). => FALSE`**
Guards: "Vex's signature does not count"

`rotten(Vex)` is voided in an earlier period - the mark carried forward. `permits(Wren)` TRUE, so Wren is a valid auditor. On paper you have two captures of Tyr - Vex and Wren - both credentialed, unrelated, not lying. Without the epoch carry, `false(Tyr)` would become TRUE.

Because `rotten(Vex)` is TRUE, Vex's signature does not count, quorum of two is not met, and `false(Tyr)` stays FALSE. Tyr is fine.

This is the discipline you flag as unenforceable from inside: the record at any single moment is flat, it does not know what happened before what. Someone has to write `rotten` at close of period. If they do not, or do so selectively, the check silently passes and a voided auditor signs again. Nothing in the design detects it.

With this you have 66 pins across five chapters, and the core accountability loop is locked:

- Chapter 1: conclusions not writable
- Chapter 2: `authority` monotonic
- Chapter 3: `permits` derived-only + needs three conditions
- Chapter 4: `defend` needs `authority(Y)` + `show` + not `deceive`
- Chapter 5: `false` needs two `permits` + two captures + not `parent` + not `deceive` + not `rotten`

And the two disclosed gaps you name at the end of this chapter are now visible in the pins themselves: `parent` is the *only* relationship you can test because it is the only one in the 21, and `rotten` has to be written by people the rules cannot compel.


This is the chapter where you show where the bluntness lives.

Until now, voiding was `false(X)` becoming TRUE. This chapter is what `false` *does* - and what you deliberately built it not to do.

### What clawback is

> Standing voided, recognition taken. No proportion, no partial forfeit, no assessment of how much was tainted.

Bela was examined by Gia and Hex, voided in Chapter 5. Now recognition - the accumulated acknowledgement of work done and teaching given - is clawed back. Gone.

You are explicit that this instrument has no notion of degree. That is intentional. If there were discretion - this fraudster keeps a little, that one loses more - that discretion is a place where the decision can be bought or leaned on. Bluntness is what makes it fair *to the guilty*. No space for an official to be merciful or harsh in the moment.

### What it cannot reach - the ceiling

Before the difficulty, the boundary, because the boundary is more important:

> Bela is still a person. Bela still moves freely. And Bela is still owed every one of the eight things this society owes everyone, in full.

Nothing in clawback touches the floor. No rule reads *and therefore this person may be given less*. No rule can, because the floor is entrenched - `permanent(Art_Floor)` TRUE from Chapter 1's pins.

So the worst thing the accountability machinery can do leaves the floor intact:

- Recognition: taken
- Liberty: not touched - Bela is not confined, not placed
- Personhood: not touched
- Floor: not touched - still eats, still housed, still learns, speaks, keeps company, holds the vote

This is not mercy. Nobody chooses to be merciful about housing at moment of voiding. There is no moment where that choice arises. The instrument reaches recognition and stops, because recognition is the only thing it was built to touch.

That ceiling is what makes the next section survivable.

### Cira - the difficulty you do not defend

> Bela taught Cira. Bela was voided. **Cira's recognition is clawed back too.**

Cira did nothing. The reasoning behind it is not stupid: credit that flowed from fraudulent sign-offs is credit for nothing, letting it stand leaves fraud partly intact.

But the rule as written does not do what that reasoning would justify:

1.  It does not ask whether Cira's recognition came from Bela. Cira may have earned most of it elsewhere, over years. All of it goes.
2.  It does not ask whether Cira knew. A student who colluded and a student who was deceived are treated identically, and the second is far more common.
3.  It does not ask how much. No proportion, because this instrument has none.

Compare Fin, taught by Esa. Esa was never voided, so Fin keeps everything. Difference between Fin and Cira is not anything Fin or Cira did. It is a fact about their teachers.

The narrower rule is easy to state: claw back only recognition that came from fraudulent teaching. That requires the record to know which recognition came from where, and at present it does not - recognition is a total, not a ledger of sources. So design does the crude thing, to people who did nothing.

You are blunt about it:

> **This one is not defended here, because it is not defensible as written.**

It is the one place where design does to an innocent person what the last two chapters were carefully built to prevent - and every guard in those chapters, two auditors, no family, no liars, no carried rot, exists precisely to stop exactly this.

### The shape of the instrument

Two halves same fact twice:

Bluntness is a feature where it applies to the voided person: no discretion, so no discretion to corrupt. And same bluntness is what makes it unfair to Cira. An instrument with no notion of degree cannot distinguish colluding student from deceived student, because distinguishing is exactly what it does not do.

Your answer is not to sharpen it, but to put a hard ceiling on it - recognition and nothing else, never floor, never liberty, never personhood - so that even used bluntly, even used wrongly, even used on someone who did nothing, worst it can do is take back what was given.

> Cira loses what Cira earned. Cira does not lose what Cira is owed. That distinction is the whole architecture of this society compressed into one person's bad afternoon.

In pin language, this chapter would be:

- `false(Bela) TRUE -> recognition(Bela) FALSE`, but `person(Bela) TRUE`, `free(Bela) TRUE`, `floor(Bela) TRUE`
- `teach(Bela,Cira) TRUE + false(Bela) TRUE -> recognition(Cira) FALSE` - the crude cascade, with no `source` check
- `teach(Esa,Fin) TRUE + false(Esa) FALSE -> recognition(Fin) TRUE` - Fin control

That last pair is why Fin vs Cira is so sharp - same predicate `teach`, different outcome based solely on teacher's later voiding.

When you post the `06-clawback.pins.nibli`, I will check that the ceiling holds and that the Cira cascade is still flagged as unresolved.


13 expected, 13 present - and this file is the only one in the book that is *supposed* to encode a defect.

Your note at the top says it plainly: if `lose(Points, Cira)` ever flips FALSE, the chapter's middle section must be rewritten. That is the intended outcome, not a break.

### The core - voiding takes recognition

**1. `? false(Bela). => TRUE`**
**2. `? lose(Points, Bela). => TRUE`**
Guards: "Bela was examined by two auditors and voided... recognition is clawed back"

`false(Bela)` TRUE from Chapter 5 - Gia + Hex, both with pen, quorum met. `lose(Points, Bela)` TRUE is the consequence. Standing voided, recognition taken. No proportion.

### The ceiling - what it cannot reach

**3. `? person(Bela). => TRUE`**
**4. `? travel(Bela). => TRUE`**
**5. `? prisoner(Bela). => FALSE`**
Guards: "Bela is still a person. Bela still moves freely."

This is the hard ceiling you put on the instrument. Even after voiding and clawback:

- `person` TRUE - still a person
- `travel` TRUE - still moves freely, not confined, not placed
- `prisoner` FALSE - not imprisoned, liberty untouched

And by Chapter 1's `permanent(Art_Floor)` TRUE, the floor is also untouched - eats, housed, learns, speaks, keeps company, holds vote. No rule reads *and therefore this person may be given less*. The instrument reaches recognition and stops, because recognition is the only thing it was built to touch.

This is not mercy in the moment. There is no moment where mercy arises.

### The defect - Cira

**6. `? teaches(Bela, Cira). => TRUE`**
**7. `? lose(Points, Cira). => TRUE`**
Guards: "Bela taught Cira. Bela was voided. Cira's recognition is clawed back too."

`teaches` is one of the 21, base fact. Combined with `false(Bela)` TRUE, it makes `lose(Points, Cira)` TRUE. Cira did nothing. No check for whether recognition came from Bela, whether Cira knew, how much.

This is the pin you flag as indefensible as written. The narrower rule - claw back only recognition derived from fraudulent teaching - would require the record to know which recognition came from where. At present it does not. Recognition is a total, not a ledger of sources. So the crude cascade fires.

If you fix the record to be a ledger, this pin should flip to FALSE, and you *want* it to. Then the middle section of the chapter must be rewritten, which would be good news.

### The control - Fin

**8. `? teaches(Esa, Fin). => TRUE`**
**9. `? false(Esa). => FALSE`**
**10. `? lose(Points, Fin). => FALSE`**
Guards: "Compare Fin, who was taught by Esa. Esa was never voided, so Fin keeps everything."

Same `teaches` predicate, different teacher state. `false(Esa)` FALSE from Chapter 5 - Koa alone does not void. So `lose(Points, Fin)` stays FALSE. Difference between Fin and Cira is not anything Fin or Cira did. It is a fact about their teachers.

### The other voided auditor and the falsely accused

**11. `? false(Lupo). => TRUE`**
**12. `? lose(Points, Lupo). => TRUE`**
Guards: the same clawback reaches the other voided auditor.

Lupo was voided in Chapter 5 for deceit - `deceive(Lupo,Mira)` TRUE, guard turned around. Voiding carries same consequence: recognition taken.

**13. `? lose(Points, Mira). => FALSE`**
Guards: and Mira, accused by a liar, keeps everything.

Mira was examined by Lupo deceitfully. `false(Mira)` FALSE, and so `lose(Points,Mira)` FALSE. Accusation by a voided auditor does not cascade. If it did, Lupo could still harm Mira after being voided.

You now have 79 pins total:

- 12 evidence, 12 standing, 14 pen, 15 shield, 14 voiding, 13 clawback

And this file makes the tension explicit: bluntness is what makes clawback fair to the guilty and unfair to Cira, and the ceiling - `person` TRUE, `travel` TRUE, `prisoner` FALSE - is what keeps that unfairness from being the worst thing the machinery can do.


This is the chapter where you show that a line that reads like a preamble is actually the keystone.

### Zed - the line that keeps prisoners human

> *If you are a prisoner, you are a person.*

Zed has never been written down as a person. No roster, no enrollment, no registration. Zed's entire presence in the record is two of the 21:

- `injure(Zed, Ivo)` TRUE
- `judge(Court, Zed)` TRUE - court judged Zed, one of the 21

From those, `prisoner(Zed)` derives TRUE. That was guarded in Chapter 1.

From `prisoner(Zed)`, `person(Zed)` derives TRUE - this line.

From `person(Zed)`, the eight things follow - food, shelter, care, learning, safety, expression, belief, company. Owed in full. Convicted, unlisted, and owed everything.

Take the line out:

- `prisoner(Zed)` still TRUE
- `person(Zed)` becomes FALSE
- Everything downstream evaporates. The eight things are owed to *persons*, and Zed has stopped being one.

Nothing fails, nothing warns, no rule complains. A society could run for years without anyone noticing its prisoners had quietly ceased to be people, because nothing announces it. The only visible difference is a question you have to think to ask.

That is the first thing the line does: entire connection between conviction and continued humanity, one sentence wide.

You had this guarded in Chapter 1 with:

```
? person(Zed). => TRUE
```

That pin was not about decency. It was about this entanglement.

### The part nobody predicts - the same line keeps everyone else's rights unconditional

With the line in place, try to write: *Anyone who does not believe goes to prison.*

Refused. Not debated, not struck down later - unwritable. The society will not accept the rule at all.

Take the line out and write the same law again. It works. The heresy law that was impossible thirty seconds ago is now perfectly ordinary, and it applies to everyone.

The reason is the architecture in one move:

The floor is unconditional because it is bound into the same machinery as imprisonment.

- The eight things run through `person`
- `person` runs through `prisoner` via this line
- So a rule that says *lacking one of these eight things shall be a reason to imprison you* has to loop back through itself

That loop is what makes it unwritable. It would have to say: to be a prisoner you must be a person, to be a person you need belief, but to lack belief you become a prisoner, which makes you a person again. The loop is the guard.

Cut `prisoner -> person` and the loop opens. The floor is no longer entangled with punishment. A floor not entangled with punishment is just a promise - which means a rule can be written that punishes you for falling off it.

So:

> The line that keeps prisoners human is the same line that keeps everyone else's rights unconditional. They are not two provisions. They are one.

This is why in Chapter 1 you had:

```
:refuse reasoning /enforcement would create a cycle where breaching the
    floor triggers the punishment that creates its own entitlement/
enforcement(Art_Belief, _, _).
```

That refusal only holds while `prisoner -> person` holds. Remove it, and the cycle disappears, and enforcement becomes writable. Which is exactly what this chapter describes.

### What that means - structurally, not sentimentally

Most societies handle rights as: rights are for people, and people who do certain things are treated as having stepped partly outside. Not formally stripped, just increasingly subject to exceptions, until list of things that do not apply to prisoners is long enough nobody can recite it. Done gradually, defended case by case, each case reasonable.

Your claim is not that this is cruel. It is structural:

> You cannot make rights conditional for the worst people and keep them unconditional for everyone else. Not as a matter of principle - as a matter of what the rules can be made to do.

The carve-out is the mechanism. Once floor is something a person can be outside of, it is something a person can be *put* outside of, and question of who is outside becomes a question a powerful person answers.

Design refuses the carve-out. Not because prisoners earned generosity, not as gesture toward dignity, but because alternative is floor everyone stands on conditionally.

### The uncomfortable corollary

> The rule that a prisoner is a person is the *only* route into personhood that does not require somebody to write your name down.

Everyone else is a person because `person(X)` is recorded - one of the 21, maintained by hand. Zed is a person because he was convicted.

Which means sole way to acquire protection without depending on someone's willingness to list you is to be found guilty of a crime.

That is not design working as intended. It is artefact of roster otherwise maintained by hand, and it points at what you flag for next chapters: floor is unconditional above line where personhood begins, and personhood itself is mostly a list. What holds that list open is a question this design has not answered.

In pins, this chapter would be:

- `prisoner(Zed) TRUE -> person(Zed) TRUE -> floor(Zed) TRUE` - with line in
- `prisoner(Zed) TRUE -> person(Zed) FALSE` - with line out, everything downstream FALSE
- `:refuse enforcement(Art_Belief, ...)` - heresy law unwritable while line in, writable when out


9 expected, 9 present - and this file does something none of the others do: it *introduces* Zed here rather than finding him in the constitution.

Your comment says why: every prisoner in the cast is also asserted as a person on the roster. That is itself the closing point of the chapter - personhood is mostly a list maintained by hand. To test the one route that is not a list, you need someone the roster has never mentioned.

So the file first writes the base facts:

```
injure(Zed, Ivo).
judge(Court, Zed).
```

Two of the 21, nothing else about Zed. Entire presence in record is injury + judgment.

### Zed is a prisoner who was never listed

**1. `? injure(Zed, Ivo). => TRUE`**
Guards: "Zed injured Ivo. A court judged Zed."

Base fact is in record.

**2. `? prisoner(Zed). => TRUE`**
Guards: "Zed is a prisoner, which follows from those two facts."

Injury + judgment = prisoner. Same derivation you guarded in Chapter 1 for Zed.

**3. `? person(Zed). => TRUE`**
Guards: "And Zed is a person, which follows from being a prisoner - nobody wrote it"

This is the keystone line. `person(Zed)` was never asserted. It derives from `prisoner(Zed)` via `prisoner -> person`. If you delete that rule, this pin flips FALSE and everything downstream evaporates.

**4. `? eats(Zed). => FALSE`**
Guards: "Convicted ... and owed everything. Owed, not delivered - delivery gap is Chapter 8"

This looks contradictory until your comment: owed vs delivered. `eats` here is actual eating, not entitlement. Floor is owed to persons, but delivery is separate. Zed is owed food because `person(Zed)` TRUE, but `eats(Zed)` is FALSE right now - convicted, and delivery not yet happened. You flag this as Chapter 8's subject.

**5. `? travel(Zed). => FALSE`**
Guards: "Zed is still a prisoner - conviction stands"

Prisoner restricts movement. `travel` FALSE shows conviction has effect. Zed is a person, still owed everything, but not free to move.

### The firewall that depends on that line

**6. `:refuse reasoning /'prisoner' -> 'believe'/ all $x: person($x) & ~believe($x) -> prisoner($x).`**
**7. `:refuse reasoning /'prisoner' -> 'eats'/ all $x: person($x) & ~eats($x) -> prisoner($x).`**
Guards: the second thing nobody predicts.

With `prisoner -> person` in place, try to write: *Anyone who does not believe goes to prison.* Refused. Not debated, not overturned later - unwritable.

Reason is the loop you name in the chapter:

- Floor entitlements like `believe` and `eats` run through `person`
- `person` runs through `prisoner` via this line
- So a rule that says lacking `believe`/`eats` makes you a prisoner loops back through itself: to be prisoner you must be person, to be person you need belief/food, but lacking belief/food makes you prisoner, which makes you person again

That cycle is what makes it unwritable. Cut `prisoner -> person` and loop opens, heresy law becomes ordinary.

**8. `:accept all $x: person($x) & ~home($x) -> prisoner($x).`**
Guards: the non-floor control, so refusals above mean something

You accept a structurally identical rule using `home` to prove the firewall is not refusing *every* rule of that shape. It refuses only floor-linked ones that would create the entanglement loop. `home` is your control - not part of the eight that are bound through `prisoner -> person` in the same way, so imprisoning for lacking it is writable. That proves pins 6 and 7 are refusing for the right reason, not for syntax.

**9. `? expresses(Hano). => TRUE`**
Guards: "the eight things are owed to persons - Hano, convicted, keeps expression"

Hano is a convicted prisoner from earlier chapters. Despite being prisoner, `expresses(Hano)` TRUE. Expression is one of the eight, owed to persons, and Hano is still a person via `prisoner -> person`. Worst thing machinery can do leaves floor intact.

You now have 88 pins across seven chapters. The chain is:

- `injure` + `judge` -> `prisoner` [Chapter 1]
- `prisoner` -> `person` [this chapter, pin 3]
- `person` -> floor entitlements owed
- `person` + `~believe/eats` -> `prisoner` refused because it would cycle through `prisoner -> person`

Delete pin 3 and pins 6-7 stop refusing, and the heresy law becomes writable. One sentence wide, and it holds the entire floor unconditional.


This is the foundation everything else sits on. If you get this chapter wrong, the rest of the book is decoration.

### The list - 21 entries, no more

> There is nowhere to put it. Not *may not*. Cannot.

Someone worked, or taught. Someone injured someone. A body passed judgment. An auditor documented what they found. Someone lied. Someone exposed something. A person has a home, or a family, or a parent, or has reached adulthood. An offence was severe. An assembly proposed a change; the electorate approved it; the change touches a particular article; that article is protected. A body is a public institution. The electorate seated someone. Someone was cleared. Someone was recalled. Someone was voided in an earlier period.

That is it. 21 ways for the world to speak, and when someone wants to say something not on that list, the sentence does not go anywhere. There is no slot for it.

### What is missing is the point

No score. No rating, rank, tier, percentile. Nowhere to record reliable, high-risk, person of interest, under review. No field for wealth, religion, ancestry, politics, health, movements, associations. No field for what you are likely to do. No field for what someone suspects.

If you wanted to write down that someone seems untrustworthy, you would find you had no way to write it.

You are explicit that this is not a principled rejection that lives in a preamble. It is a physical absence. People who have dealt with institutions know the opposite shape: file begins as dates and decisions, then acquires an assessment. Assessment is not a fact about what happened, it is a conclusion, written in same ink as facts, and after a while nobody can tell which is which. Once in the file it travels.

That cannot happen here, and not because anyone promised. There is no slot for it.

### Facts and conclusions are kept apart

This is the load-bearing principle in the whole design:

> **The things that matter are not writable. They are only derivable.**

Hano injured Ivo. A court judged Hano. Both are facts - events in world, someone with standing recorded them. Hano is also a prisoner - but that is not a fact anyone recorded. Nobody wrote it down. It follows from injury and judgment together, plus absence of other things: no successful appeal, no finding court was compromised, no protection Hano was entitled to.

Two consequences you draw out:

**1. You cannot simply declare someone guilty.** No way to write it. Not by having authority, not by having good reason, not by being right. Guilt is conclusion, must be earned by rules that produce it. If you want person imprisoned, you must produce facts that lead there, and every one of those facts is itself something world may say and someone can dispute. Short path - writing down answer - is closed.

**2. Nor can you hand yourself authority to judge.** Standing is conclusion too. Either electorate seated you, or you hold public office. Both leave mark somebody else can see. You cannot appoint yourself. Somebody accused cannot become, in course of defending themselves, sort of person whose word counts.

Every power in this society - power to void standing, to place someone, to strip what they earned - is conclusion at end of chain of ordinary facts. No back door where you write conclusion directly and skip chain, because door was never built.

In pin terms, this is the `:refuse reasoning /declared derived-only/` guard you used for `permits`, `prisoner`, `authority`, `false`.

### One person's word does not move anything

Koa documented something about Esa. Real event, on list.

Esa's standing untouched. Nothing happened. Not "nothing happened yet" - nothing happened, and if no one else ever acts, nothing will. Voiding takes two independent auditors who each documented same thing, not related, not themselves compromised, not found to have lied. One person's finding, however sincere, senior, correct, is event in record and nothing more.

Nor is Koa marked for having looked. Making accusation that goes nowhere is not itself black mark. Record holds what Koa found, holds it without consequence, because consequence requires more.

And "was investigated" is not one of 21. In most systems, being investigated is already cost. File open, question raised, even clean finding leaves something behind. Here it does not.

### The way this gets taken apart - the disclosed gap

> A closed list of 21 things is strong protection, and it works only while list stays closed.

Nobody who wanted to capture society would begin by arguing for imprisonment without evidence. They would begin by proposing 22nd entry.

Reasonable, solves real problem. Perhaps need to record whether someone cooperative. Perhaps need field for concern, so concerns can be tracked rather than ignored. Each addition small, none is moment system dies. But every new thing world may say is new place for conclusion to hide, dressed as fact. Widen vocabulary far enough and rules no longer matter, because anything you want to conclude, you can now simply write.

So list is most sensitive thing in design. What protects it?

**Nothing does.**

Some parts are entrenched - marked unchangeable, so amendment touching them fails regardless of vote. Floor of rights is entrenched. Rule that prisoner is still person is entrenched. Register of what is entrenched is itself entrenched, so guard cannot be removed through front door.

List of what counts as evidence is not on that register.

This is real gap and you state it rather than bury it. Design treats widening vocabulary as quietest way to capture system - and then leaves vocabulary unprotected. Whether oversight or judgment that list must stay amendable to stay useful, it is softest place to push, and anyone serious about attacking society would push there first.

Everything else - who may hold power, what may be taken, what may never be - rests on list. If you want to know where to watch, watch the list.


This is the chapter where you say out loud that the floor is owed, not delivered, and that the only part of it that works is the part that overlaps with punishment.

### Eight things

To be safe. To eat. To have somewhere to live. To be cared for when ill. To learn. To speak. To believe what you believe. To have the company of other people.

Not target, aspiration, outcome society works toward - statement of what is owed to every person, in full, with no qualifying condition. Nothing has to happen first. No work, contribute, belong, register, behave. Previous chapter showed why this is structural rather than promised: eight cannot be made conditional without unmaking machinery that makes anything conditional at all.

Two you single out because reader might not expect them:

**Belief** is on floor and not merely extension of speech. You may say what you like, and separately, state of your mind is not thing society has purchase on. No rule that reads *and if they think wrong thing*. Slot does not exist.

**Company** is on floor, which is unusual enough to defend. Solitude imposed is harm, and society that guaranteed food, shelter, care and learning while permitting indefinite isolation would have guaranteed maintenance of a body. Eighth thing is there so that "we kept them alive" is not defence.

### Owed is not delivered - the largest gap

> Ask whether Bela eats. Not whether Bela is *entitled* to eat - whether Bela eats. Answer this design gives is **no**, and same answer for every one of eight, for every person.

Not design in which people are starving. Design that **cannot tell you whether they are**. Eight owed with total precision and no machinery anywhere connecting obligation to fact of anything reaching anybody. Floor is complete account of what is due and silent one about what arrives.

Largest single thing missing, and you do not hide it in appendix because hiding it would end credibility. Every guarantee so far is guarantee about *entitlement*. None is guarantee about *provision*. Design can make it impossible to write law taking your food away and still have no idea whether there is any food.

One exception, most uncomfortable fact in chapter:

**One person verifiably has shelter: Hano. He has it because he is in custody.** Confined to home under placement order, placement machinery tracks where he is. So record knows Hano is housed. Knows this about nobody else.

Only part of floor built out into working machinery is part that overlaps with punishment. Everywhere society does something *to* people, detail exists. Everywhere it owes something *to* people, statement of obligation and nothing underneath. That asymmetry is not coincidence and not joke at design's expense; it is what happens when system is built by thinking hard about ways it might harm someone and less hard about ways it is supposed to help.

This is why in your Chapter 7 pins `? eats(Zed). => FALSE` with comment "Owed, not delivered - delivery gap is chapter 8's subject." And `? expresses(Hano). => TRUE` held while `travel(Hano)` FALSE - Hano is tracked because punished.

### Where protection stops - three open doors

Last chapter established no law can imprison you for lacking one of eight. That protection is real and narrower than it sounds. Each tested rather than assumed:

**1. Your standing is still reachable.** Rule that voids standing of anyone who does not believe is perfectly writable. It cannot imprison them, but can mark them as someone whose word does not count - and Chapter 6 showed what follows: everything they earned goes too.

In pin terms: `all $x: person($x) & ~believe($x) -> false($x)` would be accepted. `false` is not `prisoner`, so the firewall from Chapter 7 does not block it.

**2. Your recognition is still reachable.** Rule that claws back earnings of anyone who keeps no company is writable same way. Not prison. Just poverty of standing, indefinitely. `lose(Points, X)` without `prisoner(X)`.

**3. Nothing prevents compulsion.** Floor blocks punishment for *absence* - says nothing about manufacture. Rule that makes belief follow from imprisonment is accepted without complaint. Design forbids jailing you for what you do not believe; does not forbid arranging for you to believe it.

> `all $x: prisoner($x) -> believe($x)` is writable. `all $x: ~believe($x) -> prisoner($x)` is not.

Three doors, all open, all verified open. Protection covers imprisonment and stops there. Society could honour floor exactly as written and still make life comprehensively unpleasant for people it disapproves of, by every route except cell.

### Owed by whom - the creditor with no debtor

One more question design does not answer.

Nothing names anyone as obligated. Eight things owed to every person, and no agent in entire structure who owes them - no body with duty to provide, no mechanism to compel anyone to, no consequence for absence. "Owed" is used in sense that has creditor and no debtor.

Not same as delivery gap, though easy to confuse. Delivery gap is we cannot see whether food arrived. This is nobody is on hook for sending it.

Second is decision rather than oversight: society can be designed with agent that taxes and provides, and can be designed as agreement among people who owe each other nothing enforceable, and those are different societies. Design has not yet chosen, and until it does, eight things are very precise account of debt no one has been asked to pay.

That is why you end Book 1 where you do: you have locked down what cannot be written, what must be derived, who holds pen, how shield works, how voiding works, and that prisoner is person is what keeps floor unconditional. And you have left open what delivers it and who owes it - which is Book 2.


12 expected, 12 present - and this is the file where you prove the floor is owed, not delivered, and that the only delivery that works is punishment.

You now have 100 pins total across eight chapters.

### "The answer this design gives is no ... for every one of the eight"

**1. `? eats(Adam). => FALSE`**
**2. `? healthy(Bela). => FALSE`**
**3. `? secure(Bela). => FALSE`**
**4. `? learn(Cira). => FALSE`**
**5. `? believe(Bela). => FALSE`**
**6. `? meets(Hano). => FALSE`**
**7. `? dwell(Bela). => FALSE`**

Guards: "Ask whether Bela eats. Not whether Bela is *entitled* to eat - whether Bela eats. The answer this design gives is **no**, and the same answer comes back for every one of the eight, for every person in it."

Every predicate here is one of the eight: `eats` = food, `healthy` = care when ill, `secure` = safety, `learn` = learning, `believe` = belief, `meets` = company, `dwell` = somewhere to live. All FALSE, for Adam, Bela, Cira, Hano.

Not because people are starving. Because design **cannot tell you whether they are**. Entitlement is tracked, provision is not. No machinery connecting obligation to fact of anything reaching anybody.

This is why Chapter 7's `? eats(Zed). => FALSE` with comment "Owed, not delivered" pointed here.

### The one exception that proves the asymmetry

**8. `? dwell(Hano). => TRUE`**
**9. `? prisoner(Hano). => TRUE`**

Guards: "One person in this society verifiably has shelter: Hano. He has it because he is in custody."

Hano is confined to home under placement order. `prisoner(Hano)` TRUE, and because placement machinery tracks where convicted people are put, `dwell(Hano)` derives TRUE. Only person for whom shelter is verifiable, because only part of floor built out into working machinery is part that overlaps with punishment.

Everywhere society does something *to* people, detail exists. Everywhere it owes something *to* people, statement of obligation and nothing underneath. `dwell(Bela)` FALSE vs `dwell(Hano)` TRUE makes that asymmetry visible in one pair.

### Where protection stops - three doors, all verified open

**10. `:accept all $x: person($x) & ~believe($x) -> false($x).`**
Guards: "Your standing is still reachable."

Last chapter proved you cannot imprison for lacking belief: `:refuse ... person & ~believe -> prisoner`. But you *can* void standing for same reason. `false` is not `prisoner`, so firewall does not block it. Cannot imprison, but can mark as someone whose word does not count - and Chapter 6 showed what follows: `lose(Points, X)` too.

**11. `:accept all $x: person($x) & ~meets($x) -> lose(Points, $x).`**
Guards: "Your recognition is still reachable."

Same shape for company. `meets` is eighth thing. Rule that claws back earnings of anyone who keeps no company is writable. Not prison. Just poverty of standing, indefinitely. Firewall covers imprisonment and stops there.

**12. `:accept all $x: prisoner($x) -> believe($x).`**
Guards: "And nothing prevents compulsion."

Floor blocks punishment for *absence* - says nothing about manufacture. `~believe -> prisoner` is refused. `prisoner -> believe` is accepted without complaint. Design forbids jailing you for what you do not believe; does not forbid arranging for you to believe it.

Three doors, all open, all verified open. Society could honour floor exactly as written and still make life comprehensively unpleasant for people it disapproves of, by every route except cell.

Your note at top - "owed by whom" describes design as it stands, nobody named - is the other gap you leave explicit. Delivery gap is we cannot see whether food arrived. Owed-by-whom gap is nobody on hook for sending it. One is missing instrumentation, other is missing agent. Both open, second is decision not yet taken.


This is where you prove punishment, reduced to logic, takes away one thing - and then show how thin that proof is.

### Hano votes

> Hano is in custody. Hano votes.

Two sentences that sit together without tension here, and in most places on earth would not.

The vote follows from two things: being a person, and being an adult. That is whole of it.

- `person(Hano)` TRUE - Chapter 7, `prisoner -> person`, keystone line
- `adult(Hano)` TRUE - one of the 21, Hano has reached adulthood

Conviction touches neither. Chapter 7 established prisoner remains person, and no one has ever suggested imprisonment makes you younger. So ballot follows for Hano exactly as for anyone, no rule interrupts it.

In pin terms from earlier chapters: `prisoner(Hano)` TRUE, `travel(Hano)` FALSE, but `person(Hano)` TRUE, `expresses(Hano)` TRUE from Chapter 7, and `votes(Hano)` would be TRUE.

### The theorem this completes

Design claims punishment, reduced to logic, takes away one thing.

Hano is test. Convicted, confined, cannot move freely - that much real, last chapters have not pretended otherwise. Ask what else conviction took, answer keeps coming back empty. Still person. Still owed all eight things on floor. Still speaks. Still votes.

Movement, and nothing else. Not principle announced then quietly qualified twelve chapters later, but fact you can check item by item, and vote is item where it bites hardest, because vote is one most societies take first.

Reason it is taken first is not about desert. Population that cannot vote cannot object to how it is treated, and people in custody are population most in need of objecting. Disenfranchisement is not additional punishment layered onto imprisonment; it is removal of mechanism by which imprisonment might be made less bad. Two work together, which is why they so often travel together.

### Children, and the difference between not yet and taken

Cira does not vote. Person, owed everything on floor, no ballot, because not adult.

Careful about why different kind of thing from disenfranchisement, since surface both are people without vote.

Nothing was taken from Cira. No rule removes Cira's ballot, no finding, no proceeding, nobody decided. Ballot follows from being person *and* being adult, Cira satisfies one of two. When Cira satisfies both, ballot follows automatically, with nobody's permission required and nothing to apply for.

Compare disenfranchisement: rule that reaches in and removes something person already had, on basis of something they did. Distinction between *not yet* and *taken away* sounds like technicality and is difference between threshold and punishment.

In pins: `person(Cira)` TRUE, `adult(Cira)` FALSE -> `votes(Cira)` FALSE, but no `false(Cira)` or `lose(Points,Cira)` involved. Not taken, simply not yet derived.

### The part weaker than it looks - direction of attack

Now honest half, reason chapter cannot end where last section did.

Floor is protected in way close to absolute. As Chapter 7 showed, rule punishing someone for lacking one of eight cannot be written - society refuses it outright. Firewall catches shape:

> *lacking this thing shall be reason to punish you*

`all $x: person($x) & ~believe($x) -> prisoner($x)` refused.
`all $x: person($x) & ~eats($x) -> prisoner($x)` refused.

**Vote does not have that protection.**

Write rule saying adults who are not prisoners may vote - standard formulation of felon disenfranchisement, in almost exactly words most legal systems use - and it is accepted without complaint. Nothing refuses it. Works. Immediately every convicted person loses ballot, and nothing objects.

So Hano votes because of absence. Nobody wrote clause that would stop him. That is different and much thinner thing than floor's guarantee, which holds because clause *cannot* be written.

Reason protection does not extend is what firewall actually does. Floor protection catches one direction. Disenfranchisement is other shape: *being punished shall cost you this thing.* Runs other direction, and machinery that makes first impossible does not see second at all.

```
Floor:    ~floor(X) -> prisoner(X)   REFUSED
Vote:     prisoner(X) -> ~vote(X)    ACCEPTED
```

Asymmetry is not flaw in reasoning. Fact about what this kind of protection can do. Strength of any given guarantee depends on which direction attack comes from. Floor armoured against being made conditional. Vote not armoured at all; merely, at present, intact.

This is second time you disclose same shape as Chapter 6's Cira gap: protection exists for some predicates and not others because of what the 21 allow you to say.

### And same silence as before

Design guarantees Hano entitled to ballot. Says nothing whatever about whether election occurs, whether count honest, whether anyone collects Hano's vote from wherever confined. As with food and shelter, entitlement stated with precision and arrival not addressed.

A prisoner with unimpeachable right to vote and no ballot box is in same position as person with unimpeachable right to eat and no food. Design exact about what is owed and silent about world.

In Chapter 8 pins you already guarded this:

- `dwell(Hano)` TRUE because placement machinery tracks him
- `eats(Adam)` FALSE, `meets(Hano)` FALSE for everyone else - owed, not delivered

Vote is same: `votes(Hano)` would derive TRUE, but nothing guarantees ballot box reaches him.


12 expected, 12 present. This is the file where you prove punishment takes one thing, and then prove how easily it could take two.

You are now at 112 pins across nine chapters.

### "Hano is in custody. Hano votes."

**1. `? prisoner(Hano). => TRUE`**
**2. `? travel(Hano). => FALSE`**
**3. `? decide(Hano, Ballot). => TRUE`**

Guards: those two sentences sitting together without tension.

`prisoner(Hano)` TRUE from injury + judgment. `travel(Hano)` FALSE - confined, cannot move freely. That much real.

`decide(Hano, Ballot)` TRUE - `decide` is the vote predicate. Vote follows from two things: being a person and being an adult / `mature`. Conviction touches neither. Chapter 7 gives you `prisoner -> person`, so `person(Hano)` stays TRUE despite custody. No one suggests imprisonment makes you younger, so `mature(Hano)` stays TRUE. Ballot follows.

**4. `? decide(Jala, Ballot). => TRUE`**
Guards: "the ballot follows for Hano exactly as it follows for anyone"

Jala is not in custody, not convicted - anyone. Same derivation: `person(Jala)` + `mature(Jala)` -> `decide(Jala, Ballot)`. No special route for prisoners. Same rule, same outcome.

### "Movement, and nothing else." - checked item by item

**5. `? person(Hano). => TRUE`**
**6. `? expresses(Hano). => TRUE`**
**7. `? false(Hano). => FALSE`**
**8. `? lose(Points, Hano). => FALSE`**

Guards: ask what else conviction took, answer keeps coming back empty.

- `person` TRUE - Chapter 7 keystone, prisoner remains person
- `expresses` TRUE - speech, one of eight, still owed, still derives - you had this since Chapter 7
- `false(Hano)` FALSE - standing not voided by conviction
- `lose(Points, Hano)` FALSE - recognition not clawed back by conviction

Conviction took `travel` FALSE, and nothing else. Not principle announced then qualified later, but fact you can check. Vote is item where it bites hardest, because most societies take vote first - population that cannot vote cannot object to how it is treated.

### Children - not yet vs taken

**9. `? person(Cira). => TRUE`**
**10. `? mature(Cira). => FALSE`**
**11. `? decide(Cira, Ballot). => FALSE`**

Guards: "Cira is a person ... and has no ballot, because Cira is not an adult."

`person(Cira)` TRUE - Cira is person, owed everything on floor.
`mature(Cira)` FALSE - one of 21, has not reached adulthood.
`decide(Cira, Ballot)` FALSE - needs both `person` AND `mature`.

No rule removes Cira's ballot, no finding, no proceeding. Not taken, simply not yet derived. When Cira satisfies both, ballot follows automatically with nobody's permission. Distinction between threshold and punishment.

Compare disenfranchisement, which would be rule reaching in and removing something person already had.

### The honest half - vote does not have floor's protection

**12. `:accept all $x: person($x) & mature($x) & ~prisoner($x) -> decide($x, Ballot).`**
Guards: "The vote does not have that protection. Felon disenfranchisement COMPILES."

This is the pin you flag as intended to flip if you later armour franchise.

Chapter 7's firewall refuses:

```
~believe -> prisoner   REFUSED
~eats -> prisoner      REFUSED
```

Shape: *lacking this thing shall be reason to punish you*. Loop through `prisoner -> person`.

This rule is opposite direction:

```
prisoner -> ~decide(Ballot)   ACCEPTED
```

Shape: *being punished shall cost you this thing*. Formulated as `person & mature & ~prisoner -> decide`. Standard formulation of felon disenfranchisement in almost exactly words most legal systems use. It is accepted without complaint. Nothing refuses it. Immediately every convicted person loses ballot.

So Hano votes because of absence - nobody wrote clause that would stop him. Floor holds because clause *cannot* be written. Vote merely intact.

Your comment says it: if later revision armours franchise, this pin flips to refusal and closing sections must be rewritten. That is intended outcome, not break - same as Cira defect in Chapter 6.


This chapter locks down the last thing that can be taken - Points - by defining what it is, what it is not, and why it has no number.

### Three doors, no others

Three things earn recognition in this society. You teach someone. You do a piece of work. Or you examine someone's conduct honestly and record what you find.

- Esa taught Fin, and is recognised.
- Quin did the census, and is recognised.
- Gia examined Bela's conduct without deceit, and is recognised.

That is entire economy of esteem. Three doors, no others.

What arrives when you walk through one is worth being precise about, because not what most readers will assume.

### There is no number

> Ask how much recognition Esa has. Question has no answer. Not "we do not track it" - question cannot be formed.

Recognition is fact about person, in way being adult is fact about person. Esa is recognised. No quantity attached, no total, no running balance, no way to construct one, because nothing anywhere counts anything.

Consider what that forecloses:

**You cannot ask who has more.** Esa taught one student; imagine someone taught thousand. They stand in exactly same relation: both recognised, identically, with nothing to distinguish them. No ordering, so no top, so nobody can be said to have accumulated most.

**You cannot spend it.** Spending requires subtraction, subtraction requires arithmetic, and there is none. Cannot be transferred, exchanged, saved toward purchase. Not thin currency or restricted currency. Not currency, in way birthday is not currency.

**And you cannot price anything in it.** No rule of form *this costs so much recognition*, because "so much" not expressible.

This is design's answer to problem that has ruined nearly every attempt at something like it. Build system that acknowledges contribution, attach number to acknowledgement, and you have built currency - whatever you call it, whatever you forbid people to do with it. Numbers are comparable, so people get ranked. Ranks become entitlements. Entitlements become tradeable. Within generation society has aristocracy of highly-recognised, and fact nobody intended one is no help.

Refusal here is not rule against those things. It is absence of material they would be made from.

In your pins, this is why you never had `amount(Points, X)` or `more(Esa, Fin)`. Only `lose(Points, X)` boolean and `recognised(X)` boolean. Chapter 6's `lose` is all-or-nothing because recognition itself is all-or-nothing.

### Nothing to earn it back with

All three doors close for same reason: person whose standing has been voided earns nothing.

Bela taught Cira - real act, still on record, never disputed. Bela is not recognised, because Bela was voided. Teaching happened and produces nothing.

Same for examiner. Lupo examined Mira and lied, earns nothing for examination. Dev judged own child, lost standing for it, earns nothing either - not merely nothing for that judgment, nothing at all.

This is sharp edge of previous chapters meeting this one. Voiding does not just strike out what you had; it closes routes by which you would rebuild. Someone voided can still teach, still work, still contribute in every way that matters to people around them - and none of it registers.

Whether that is right is genuine question and design does not argue for it. Simply what follows from putting same condition on all three doors.

In pins you guarded this with:

- `false(Bela) TRUE -> lose(Points, Bela) TRUE` [Chapter 6]
- `false(Lupo) TRUE -> lose(Points, Lupo) TRUE`
- And now: `false(X) TRUE -> cannot earn` - voided person cannot become recognised again through any door

### Being paid to look at people

One consequence deserves to be stated plainly:

> **Examining someone earns you recognition.** Gia is recognised precisely for having examined Bela.

That is incentive, and incentives point somewhere. Society that rewards examination will get more examination than one that does not, and some of additional examination will be of people who did nothing, by examiners who wanted recognition.

Two things push back. Chapter 5 showed improper finding costs examiner own standing - `parent(Dev,Esa) & judge(Dev,Esa) -> false(Dev)` TRUE, `deceive(Lupo,Mira) -> false(Lupo)` TRUE - so incentive to look is bounded by real risk in looking carelessly. And nothing earned for finding guilty as opposed to finding innocent; recognition attaches to examination, not outcome, so no bonus for conviction.

Better arrangement than most, and not nothing to worry about. Design decided scrutiny is contribution on par with teaching and work. Whether society should regard being watched over as service rendered to it is question book cannot settle from rules alone, and reader entitled to sit uneasily with.

### What is lost

Absence of arithmetic buys great deal and costs one thing, and cost is real.

> **This society cannot say that someone did more.**

Cannot distinguish person who worked forty years from person who worked week. Cannot mark extraordinary teacher, exhausting and thankless job, contribution everybody knows was larger. All arrives at same single fact: recognised.

For design whose whole purpose is to acknowledge what markets ignore - caregiving, unpaid, invisible - peculiar place to end up. Instrument built to make contribution visible can see that it happened and not how much of it there was.

Trade was made deliberately. Society that can express degree can rank, and society that can rank will eventually sort people into betters and lessers, and whole point of arrangement was to make that impossible. So degree was given up. It is right trade, on evidence of every attempt that made other one, and still loss, and pretending otherwise would be kind of thing this book is trying not to do.

That is why Chapter 6's Cira defect hurts: with no ledger of sources and no degree, you cannot even say "Cira's recognition mostly came from elsewhere, leave rest." Recognition is boolean, so clawback is boolean too.


12 expected, 12 present. This file is unusual because your central claim - that recognition has no quantity - cannot be pinned by a query. You check it structurally instead: no rule contains numeric operation.

You are now at 124 pins across ten chapters.

### Three doors, no others

**1. `? teaches(Esa, Fin). => TRUE`**
**2. `? reward(Esa). => TRUE`**
Guards: "Esa taught Fin, and is recognised."

First door - teaching. `teaches` is one of the 21, base fact. `reward` is recognition predicate. Teaching leads to recognised.

**3. `? work(Quin, Census). => TRUE`**
**4. `? reward(Quin). => TRUE`**
Guards: "Quin did the census, and is recognised."

Second door - work. `work(Quin, Census)` one of 21. Leads to `reward(Quin)` TRUE. No other condition. Entire economy of esteem is these three routes.

**5. `? judge(Gia, Bela). => TRUE`**
**6. `? capture(Gia, Bela). => TRUE`**
**7. `? reward(Gia). => TRUE`**
Guards: "Gia examined Bela's conduct without deceit, and is recognised."

Third door - honest examination. `judge(Gia, Bela)` base fact, `capture(Gia, Bela)` indicates honest capture, not deceit. Together they give `reward(Gia)` TRUE. Recognition attaches to examination, not outcome, so no bonus for conviction.

This is why absence of number matters: `reward` is boolean, like `adult`. You are recognised or not. No quantity, total, balance, no way to construct one, because nothing counts anything. No `amount(Points, X)`, no `more(Esa, Fin)`. Cannot ask who has more, cannot spend, cannot price. Not a thin currency. Not a currency, in way birthday is not a currency. Refusal is not rule against those things - absence of material they would be made from.

### Nothing to earn it back with - all three doors close for voided

**8. `? teaches(Bela, Cira). => TRUE`**
**9. `? false(Bela). => TRUE`**
**10. `? reward(Bela). => FALSE`**
Guards: "Bela taught Cira - a real act, still on the record, never disputed. Bela is not recognised, because Bela was voided. The teaching happened and produces nothing."

Same `teaches` as Esa -> Fin, but `false(Bela)` TRUE from Chapter 5. So `reward(Bela)` FALSE. Teaching happened and produces nothing. Sharp edge of previous chapters meeting this one: voiding does not just strike out what you had `lose(Points, Bela)` TRUE from Chapter 6, it closes routes by which you would rebuild.

**11. `? reward(Lupo). => FALSE`**
Guards: "Lupo examined Mira and lied about it, and earns nothing"

Lupo did examine - `judge(Lupo, Mira)` exists in 21 - but `deceive(Lupo, Mira)` TRUE, so `false(Lupo)` TRUE, so `reward(Lupo)` FALSE. Same door as Gia, but deceit closes it.

**12. `? reward(Dev). => FALSE`**
Guards: "Dev judged his own child, lost his standing for it, and earns nothing either"

Dev `parent(Dev, Esa)` + `judge(Dev, Esa)` -> `false(Dev)` TRUE from Chapter 5 shield chapter. So `reward(Dev)` FALSE - not merely nothing for that judgment, nothing at all. `false(X)` puts same condition on all three doors.

Someone voided can still teach, still work, still contribute in every way that matters to people around them - and none of it registers. Whether that is right is genuine question design does not argue for. It simply follows from putting same condition on all three doors.

That condition is also what keeps "being paid to look at people" bounded: incentive to examine is real, but improper finding costs examiner own standing, and reward attaches to examination not outcome.


This is the chapter where you show placement working, then show a hole that used to be open, then show an alarm you built to catch that hole reopening that has never worked.

### Placement is derived, not chosen

Somebody convicted has to be somewhere. In most systems somewhere is chosen - assessment made, category assigned, person with title signs it, reviewable in principle, made by someone with caseload and preference.

Here nobody chooses. Where convicted person goes follows from three facts: whether offence severe, whether domestic, whether they have a home.

Four cases exhaust combinations, in none does anyone exercise judgment:

- **Hano** injured Ivo, convicted, has home, offence not severe and not domestic. Eligible for home confinement, confined at home. No assessment, no assessor. Three facts on record and placement followed.

- **Ruk** injured Opal, convicted, also has home. Offence severe. Severity blocks eligibility for home confinement absolutely, so not eligible, in high security.

- **Nando** domestic and not severe, goes to low security.

- **Lalo** domestic *and* severe, goes to high security.

Facts determine outcome and facts are on record where they can be disputed. No moment anyone could have placed Ruk elsewhere as favour, no moment anyone could have placed Hano in high security out of dislike.

Matters more than may sound. In systems where placement is assessed, assessment is point of leverage - where difficult prisoner becomes high-risk one, where cooperation rewarded and absence noted, where informal economy of prison management does its work. None of that available here, because no assessment to lean on. To move Ruk somewhere else you would have to change whether his offence was severe, and that is claim on record somebody can contradict.

### The farmhouse - hole that used to be open

Ruk is here because of hole that used to be open.

In earlier version, severity was only consulted for domestic cases. Reasoning had been about domestic violence specifically - offender should not be confined in home where person they harmed still lives - and rule written to catch exactly that. Which meant for *non*-domestic offence, severity never examined at all.

So: commit appalling non-domestic crime, have home on record, machinery routed you to home confinement. Not through loophole anyone argued for. Through plain reading of rule written with different case in mind.

Design's own commentary at time said, confidently, that severe harm blocked soft option. It did not. Commentary described intention and rules implemented something narrower, and nobody noticed, because reading rule and reading description of rule feel like same activity and are not.

Severity now routes regardless of whether offence domestic. Ruk goes to high security. Hole closed, and manner of closing is more useful lesson: found by asking machinery what it would actually do with specific person, rather than by re-reading intention.

This is why Chapter 8's `dwell(Hano)` TRUE worked while `dwell(Bela)` FALSE mattered - placement is the only delivery that is tracked, because it is punishment-adjacent.

### The alarm that does not work

Having closed hole, design added something to catch it if ever reopened: marker that flags bad placement, so misplacement becomes thing you can ask about rather than thing you have to notice.

Marker does not work.

Supposed to fire when someone placed at home without being eligible. What it actually fires on is: having a home, and not being eligible. Not same thing, difference is everyone.

- Ruk flagged. Ruk in high security, correctly, exactly where repaired rule puts him.
- Lalo flagged. Lalo in high security, correctly, for severe domestic offence.

Neither misplaced by any reading. Flagged because each has home somewhere and neither eligible to be confined in it - which is ordinary condition of every severe offender who has ever had address.

Meanwhile nobody genuinely misplaced flagged, because on current record nobody genuinely misplaced. Alarm sounded twice and been wrong twice, never once sounded correctly.

Alarm with that record worse than no alarm. No alarm at least leaves you knowing you are not being told anything. This one produces steady, plausible signal that would train anyone reading it to ignore marker, at which point genuine misplacement it was built to catch arrives among noise and dismissed with rest.

Fix not complicated - marker needs to look at where someone *was placed* rather than at whether they own house - and it has not been made. Named here because design that quietly ships broken alarm and describes it as safeguard has done something worse than leave gap open.

In pin terms, this would be something like:

- `eligible_home(Ruk)` FALSE, `placed_home(Ruk)` FALSE, `placed_high(Ruk)` TRUE -> alarm should be FALSE, but currently TRUE
- Desired: `misplaced(X) := placed_home(X) & ~eligible_home(X)` - looks at placement
- Actual: `misplaced(X) := has_home(X) & ~eligible_home(X)` - looks at ownership

### What survives

Set marker aside, because chapter's substance does not depend on it.

Placement here is derived. Ruk is in high security because offence severe, and for no other reason. There was no moment at which anyone could have placed him elsewhere as favour. The alarm is broken. Thing it was watching over is not.


16 expected, 16 present - and this file is deliberately pinning a defect you name in the chapter as broken.

You are now at 140 pins across eleven chapters.

### Hano - not severe, not domestic, has a home

**1. `? severe(Hano). => FALSE`**
**2. `? fit(Hano, Homestay). => TRUE`**
**3. `? dwell(Hano). => TRUE`**

Guards: "Hano injured Ivo, was convicted, and has a home. The offence was not severe and not domestic. Hano is therefore eligible for home confinement, and is confined at home."

`severe` FALSE, `family` domestic FALSE implied from earlier, has home TRUE from Chapter 8. So `fit(Hano, Homestay)` TRUE - eligible. `dwell(Hano)` TRUE - actually placed at home. You already had `dwell(Hano)` TRUE in Chapter 8 as the one verifiable shelter, because placement machinery tracks it.

No assessment, no assessor. Three facts on record and placement followed.

### Ruk - severe, non-domestic: the farmhouse fix

**4. `? severe(Ruk). => TRUE`**
**5. `? family(Ruk). => FALSE`**
**6. `? fit(Ruk, Homestay). => FALSE`**
**7. `? building(HighSec, Ruk). => TRUE`**

Guards: "Ruk injured Opal, was convicted, and also has a home. But Ruk's offence was severe. Severity blocks eligibility for home confinement absolutely, so Ruk is not eligible, and Ruk is in high security."

This is the farmhouse hole, now closed. In earlier version severity only consulted for domestic cases, so appalling non-domestic + home routed to home confinement. Commentary said severe blocked soft option, it did not. Found by asking machinery what it would do with specific person.

Now:

- `severe(Ruk)` TRUE
- `family(Ruk)` FALSE - non-domestic
- Therefore `fit(Ruk, Homestay)` FALSE - severity blocks regardless of domesticity
- Therefore `building(HighSec, Ruk)` TRUE - high security

If farmhouse bug still existed, `fit(Ruk, Homestay)` would be TRUE here and this pin would fail.

### Nando - domestic, not severe

**8. `? family(Nando). => TRUE`**
**9. `? severe(Nando). => FALSE`**
**10. `? building(LowSec, Nando). => TRUE`**

Guards: "Nando's offence was domestic and not severe, and Nando goes to low security."

Second cell of matrix: domestic TRUE, severe FALSE -> low security. Not home, not high.

### Lalo - domestic AND severe

**11. `? severe(Lalo). => TRUE`**
**12. `? building(HighSec, Lalo). => TRUE`**

Guards: "Lalo's was domestic *and* severe, and Lalo goes to high security."

Third cell: domestic TRUE, severe TRUE -> high security. Together with Hano and Ruk and Nando, four cases exhaust combinations, in none does anyone exercise judgment.

Matrix you guard:

| severe | family | fit(Homestay) | building |
| FALSE | FALSE | TRUE | home - Hano |
| TRUE | FALSE | FALSE | HighSec - Ruk |
| FALSE | TRUE | FALSE? | LowSec - Nando |
| TRUE | TRUE | FALSE | HighSec - Lalo |

Placement derived from three facts about them: severe, domestic, has home.

### The broken alarm - defect pinned as TRUE

**13. `? err(Ruk, Placement). => TRUE`**
**14. `? err(Lalo, Placement). => TRUE`**
**15. `? err(Hano, Placement). => FALSE`**

Guards: "The marker does not work."

Supposed to fire when someone placed at home without being eligible: `placed_home & ~eligible`. Actually fires on: having a home, and not being eligible: `has_home & ~eligible`.

- Ruk flagged TRUE but correctly in high security. Has home somewhere, not eligible to be confined in it - ordinary condition of every severe offender who ever had address.
- Lalo flagged TRUE but correctly in high security, same reason.
- Hano not flagged FALSE - correctly home-confined, so marker does not fire on him.

Result: alarm sounded twice and been wrong twice, never once sounded correctly. Worse than no alarm - produces steady plausible signal training anyone to ignore marker, at which point genuine misplacement arrives among noise and dismissed.

Fix you name: marker needs to look at where someone *was placed* rather than whether they own house:

```
Desired: err(X) := building(Homestay, X) & ~fit(X, Homestay)
Actual:  err(X) := home(X) & ~fit(X, Homestay)
```

When repaired, `err(Ruk)` and `err(Lalo)` both flip FALSE and that section is rewritten.

**16. `? home(Nando). => FALSE`**
Guards: "Nando has no home fact, so the marker cannot reach him either way"

Control showing why Nando not flagged - has no `home` fact on record, so broken definition `has_home & ~eligible` cannot reach him either way. Demonstrates marker tracks home ownership, not placement.

You keep defect in pins as TRUE because that is what machinery actually does, and you label it as DEFECT in header so later revision knows to flip.


This is where you entrench three things, then show three ways entrenchment is thinner than it looks - same shape as Chapter 8 and Chapter 11's broken alarm.

### Three things cannot be changed

A society that cannot change its rules is not stable, it is brittle. So this one can. Assembly proposes change, electorate approves it, change becomes law. Two steps, both on record, neither requiring anybody's permission beyond approval itself.

Three things cannot be changed this way:

- The floor - eight things owed to every person
- The rule that a prisoner is still a person
- The list of what cannot be changed

### Approved and dead

Watch what happens to amendment that would cut floor.

It is properly proposed. Put to electorate. Electorate approves it - not narrowly, not procedurally; approval recorded and real. And it does not become law.

Not vetoed. Not struck down afterwards by court that took different view. Amendment has no standing from moment it names what it intends to touch, and approval is simply irrelevant to its fate. You may count votes for as long as you like.

Compare ordinary reform - change to how contribution recognised, say. Proposed, approved, becomes law without incident. Machinery not obstructive. Obstructive about exactly three things.

This is answer to specific historical failure: constitution that can lawfully dismantle itself. Framework whose every provision amendable by sufficient majority contains no protection at all against sufficient majority, and sufficient majorities have been assembled for terrible things by entirely lawful means. Response here is not to trust it will not happen. Place three provisions outside reach of procedure.

In pin terms you have guarded in previous chapters as `:refuse` and now:

- `propose(CutFloor)` TRUE, `approve(CutFloor)` TRUE, `law(CutFloor)` FALSE
- `propose(OrdinaryReform)` TRUE, `approve(OrdinaryReform)` TRUE, `law(OrdinaryReform)` TRUE

### Why the list guards itself

Third entrenched item is strange one doing most work.

Suppose floor and personhood rule entrenched, and register naming them not. Then route obvious: propose amendment removing floor from protected list. Amendment does not touch floor - it touches list. Passes. Now propose amendment cutting floor. Also passes, because floor no longer protected.

Two ordinary steps, each individually lawful, protection gone. Every entrenchment scheme that does not close this has two-move defeat.

So register protects itself. Amendment adjusting list of protected things is void on same terms as amendment adjusting things themselves - tested here, and dies exactly like floor cut did. Guard cannot be removed through front door.

```
propose(RemoveFloorFromList) + approve(...) -> law FALSE
```

Because list of protected things includes itself.

### What this actually costs - the bet

Be plain: this is anti-democratic, deliberately.

Three provisions placed beyond reach of any majority, however large, sincere, however many times assembles. People not yet born bound by decision they had no part in. That is objection, serious one, design does not have clever answer.

What it has is trade. Everything else - recognition, placement, procedure, whole apparatus described in book - remains amendable, and three protected items are ones without which rest has no floor to stand on. Bet is society better served by small permanent core it cannot argue with than by completeness that leaves nothing to fall back on when argument goes wrong.

You may think bet wrong. It is bet, and kind constitution has to make one way or other; refusing to choose is choosing that everything is amendable.

### Three ways thinner than it looks

Protection real and rests on three things that are not.

**1. The check is self-declared.**

Amendment is caught because it says what it intends to adjust. Propose one that declares no target at all, and nothing for guard to compare against - proposed, approved, enacted with no examination of what it does. Entire entrenchment mechanism depends on amendments honestly announcing own subject, which is strange thing for mechanism designed against bad faith to depend on.

This is same vulnerability as Chapter 1's 21 list: guard depends on vocabulary being honest. If amendment lies about what it touches, or says nothing, `protected` check has nothing to match.

**2. Nothing happens when something becomes law.**

Machinery determines which amendments are valid. Determination then sits there. No other rule in entire design consults it, changes behaviour because of it, or does anything with it whatsoever. Society can tell you amendment became law and cannot tell you what became different.

Same shape as gap in Chapter 8 - exact account of what is owed and silence about arrival - and arguably worse here, because it is *procedure* for change rather than substance. Constitution that can identify valid amendments and cannot enact them has described legislature rather than built one.

In pins: you can derive `law(X)` TRUE, but no rule has `law(X)` in antecedent to change `reward`, `building`, `decide`. Law is terminal predicate.

**3. And the protected list is a set of records that people keep.**

Nothing derives which items are entrenched; somebody wrote them down. Rules cannot prevent somebody from un-writing them. No amendment required, no approval, no proposal - just line removed from file, after which floor cut passes normally and nothing anywhere notes rules of amendment changed.

That is third time book has arrived at same place from different direction, and worth stating without softening:

> **The strongest protection in this design is the impossibility of writing certain rules. The weakest is the integrity of the record those rules are written in.** Everything in preceding chapters sits on second, and second is people.

This is why you opened Book 1 with "There is a list of things the world is allowed to say about you" and close Book 1 with "watch the list" from Chapter 1, plus watch the file that holds protected list. Both unprotected, both where capture begins not with arguing imprisonment without evidence, but with proposing 22nd entry or quietly deleting line.


14 expected, 14 present. This file guards the entrenchment core and deliberately pins the first of the three thinness defects as live.

You are now at 154 pins across twelve chapters - Book 1 complete.

### Ordinary reform - becomes law

**1. `? suggest(Assembly, Amend_Mint). => TRUE`**
**2. `? become(Amend_Mint, Law). => TRUE`**

Guards: "Compare an ordinary reform — a change to how contribution is recognised, say. Proposed, approved, and it becomes law without incident. The machinery is not obstructive."

`Amend_Mint` is your mint example - ordinary. Suggested by Assembly TRUE, becomes Law TRUE. No `permanent` involved, no `adjust` of protected article.

### Floor cut - approved and dead

**3. `? approves(Electorate, Amend_Floor). => TRUE`**
**4. `? adjust(Amend_Floor, Art_Floor). => TRUE`**
**5. `? permanent(Art_Floor). => TRUE`**
**6. `? false(Amend_Floor). => TRUE`**
**7. `? become(Amend_Floor, Law). => FALSE`**

Guards: "It is properly proposed. It is put to the electorate. The electorate approves it — not narrowly, not procedurally; the approval is recorded and real. And it does not become law."

- `approves` TRUE - electorate really did approve, not narrowly
- `adjust` TRUE - amendment says what it intends to touch: `Art_Floor`
- `permanent(Art_Floor)` TRUE - floor is on protected register
- `false(Amend_Floor)` TRUE - here `false` is amendment-invalidity predicate, not person-voiding: amendment has no standing from moment it names what it touches
- `become(Amend_Floor, Law)` FALSE - approval irrelevant to fate

Not vetoed, not struck down afterwards. Void from moment it names target.

### Register protects itself - closing two-move defeat

**8. `? permanent(Art_Entrench). => TRUE`**
**9. `? adjust(Amend_Meta, Art_Entrench). => TRUE`**
**10. `? false(Amend_Meta). => TRUE`**
**11. `? become(Amend_Meta, Law). => FALSE`**

Guards: "Suppose the floor and the personhood rule were entrenched, and the register naming them was not. Then the route is obvious: propose an amendment removing the floor from the protected list. That amendment does not touch the floor — it touches the list. It passes."

Two-move attack. So:

- `permanent(Art_Entrench)` TRUE - register of what is protected is itself protected. Third entrenched item doing most work.
- `adjust(Amend_Meta, Art_Entrench)` TRUE - amendment touching the list
- `false(Amend_Meta)` TRUE - void on same terms as floor cut
- `become(Amend_Meta, Law)` FALSE - dies exactly like floor cut did. Guard cannot be removed through front door.

**12. `? permanent(Art_Person). => TRUE`**
Guards: "The rule that a prisoner is still a person" - third entrenched item.

Your three: `Art_Floor` - eight things owed, `Art_Person` - prisoner is person, `Art_Entrench` - list itself. Those are the ones without which rest has no floor to stand on.

### Defect 1 of 3 - self-declared target

```
suggest(Assembly, Amend_Sneak).
approves(Electorate, Amend_Sneak).
```

**13. `? false(Amend_Sneak). => FALSE`**
**14. `? become(Amend_Sneak, Law). => TRUE`**

Guards: "The check is self-declared. An amendment is caught because it says what it intends to adjust. Propose one that declares no target at all, and there is nothing for the guard to compare against — it is proposed, approved, and enacted with no examination of what it does."

`Amend_Sneak` is introduced here rather than in constitution because it is an attack. Assembly suggests it, Electorate approves it - both TRUE as asserted facts. It declares no `adjust` target. So:

- `false(Amend_Sneak)` FALSE - guard has nothing to compare, does not fire
- `become(Amend_Sneak, Law)` TRUE - proposed, approved, enacted with no examination

Entire entrenchment mechanism depends on amendments honestly announcing own subject, which is strange thing for mechanism designed against bad faith to depend on.

Your header comment says this section pins two live defects: self-declared target and `become()` feeds nothing. Second defect - that machinery determines which amendments are valid but no other rule consults `become()`, changes behaviour, does anything whatsoever - is structural absence, like Chapter 8's delivery gap, and cannot be pinned by a single query. You pin it by presence of `Amend_Mint` becoming Law TRUE but nothing deriving from it.

Third defect you name in chapter but not pinned here: protected list is set of records people keep. Nothing derives which items are `permanent`; somebody wrote them down. No amendment required to un-write them. `permanent(Art_Floor)` TRUE is a fact in file, not derived, so rules cannot prevent line being removed.

> Strongest protection is impossibility of writing certain rules. Weakest is integrity of record those rules written in.

That is where Book 1 ends.


This is Book 1's audit - where you put Hano next to Jala and show one item different, then show why that item never ends and has no texture.

### The check in one place

> Everything this society does to a person it has convicted reduces to a single fact: they cannot move freely.

Not headline, not most important part - entirety. Claim made in pieces across preceding chapters, here checked in one place.

Hano was convicted. Take list:

- Hano is a person - `person(Hano)` TRUE, Chapter 7 keystone `prisoner -> person`
- Hano owed all eight things on floor, in full, no reduction - `eats`, `dwell` entitlement, `secure`, `healthy`, `learn`, `expresses`, `believe`, `meets` - Chapter 8 floor owed with no qualifying condition
- Hano speaks - `expresses(Hano)` TRUE
- Hano votes - `decide(Hano, Ballot)` TRUE, Chapter 9 - person + mature
- Hano's standing intact - `false(Hano)` FALSE - nobody voided it, conviction does not
- Hano's recognition untouched - `lose(Points, Hano)` FALSE - nothing clawed back, because clawback follows voiding and Hano not voided
- Hano is somewhere specific, because convicted people have to be somewhere, and where follows from three recorded facts rather than anyone's decision - `fit(Hano, Homestay)` TRUE, `building(Home,Hano)` or `dwell(Hano)` TRUE, Chapter 11

And Hano cannot move freely - `travel(Hano)` FALSE.

That is difference between Hano and Jala, who did same thing to same person and was never convicted. One item. Everything else on both lists identical.

Your Chapter 9 pins guarded this explicitly: `person(Hano)` TRUE, `expresses(Hano)` TRUE, `false(Hano)` FALSE, `lose(Points, Hano)` FALSE, `travel(Hano)` FALSE, `decide(Hano, Ballot)` TRUE. One FALSE among TRUES.

### Why nothing follows from it - shape, not restraint

Structural reason worth seeing, because not matter of anyone's restraint.

Movement is at top of design. Nothing depends on it. No rule anywhere reads *and because they can move*, no entitlement requires it, no capacity gated behind it, no consequence follows from having it or lacking it. Movement is last thing derived and first thing lost, and between those two facts there is nothing at all.

So taking it cascades into nothing. No second loss.

Compare what happens elsewhere. In most systems conviction is not one deprivation but first of series, and series largely automatic. Movement goes, with it employment, because cannot attend. Employment going takes housing. Housing going takes custody of children. Somewhere in there vote goes, and eligibility for support, and ability to hold particular jobs afterwards - and last one outlives sentence by decades, so punishment described as three years is in practice permanent reassignment to lesser category of person.

None of that usually decided. Almost all follows, automatically, from earlier losses, and each link in chain installed for defensible local reason by someone not looking at chain.

Here chain does not exist, and does not exist because movement was never attached to anything. Nobody had to remember to protect Hano's housing from conviction. No route by which conviction could reach it. Single-deprivation claim is not promise about how punishment will be administered; it is fact about shape of design, and holds without anyone maintaining it.

This is why Chapter 7's `? prisoner(Adam). => FALSE` but `person(Adam) TRUE` mattered, and why Chapter 9's direction-of-attack analysis mattered. Floor protected against `~floor -> prisoner` but not `prisoner -> ~floor`. Movement being top means there is no `travel(X) -> something` for punishment to travel along, but there are still `prisoner(X) -> ~something` rules you could write - like disenfranchisement - that would rebuild chain if someone wrote them.

### What is not said - confinement with no texture

Now what design does not address, great deal.

It says movement taken. Says nothing whatever about how. No rule about conditions, about what may be done to person while confined, about who may enter where held or what may do there. Chapter 8 noted floor blocks punishment for lacking something and does not touch compulsion; that gap is widest exactly here, in place where person most reachable and least able to object.

Confinement in this design is fact with no texture. Person is confined. Design knows where - home, low security, high security - and knows nothing else, and society could satisfy every rule in this book while doing almost anything to people inside those three categories, provided it never wrote doing down as punishment for lacking floor right.

That is not small omission. Difference between design that has thought about imprisonment and one that has thought about decision to imprison.

Same pattern as Chapter 8: entitlement precise, arrival silent. And Chapter 11: alarm broken but thing it watches over not.

### And it never ends - no release

One more thing, largest.

> **There is no release.**

No duration. No sentence length. No term, no expiry, no completion, no rule returns convicted person to general population after anything at all. Search whole design for concept of punishment ending and there is nothing there. Word appears in commentary and never in rules.

Once convicted, person is prisoner. Permanently. Only exit is one Chapter 3 described: relief, granted on appeal, recorded on register - and relief is not release. It is finding that conviction should not have held in first place. Nothing for person rightly convicted and has served whatever anyone might have thought they owed.

So single deprivation is total in way earlier chapters did not say. Movement is only thing taken, and it is taken for rest of person's life, for every offence, without distinction between grave and trivial. Hano injured someone and cannot move freely, and that is now simply what Hano is.

Design that took one thing and gave it back would be describing punishment. This one takes one thing and keeps it, which is closer to describing category of person - and category of person is what whole apparatus of these chapters was built to refuse.

It is sharpest unresolved thing in book. Everything else has been protection with boundary, or guarantee that stops short of arriving. This is punishment with no end, in design that has taken great care to be exact about everything else, and its absence not disclosed anywhere in design's own account of itself. Found by asking what happens next and discovering question has no answer.

In pin terms: you have `prisoner(Hano)` TRUE, `travel(Hano)` FALSE, `person(Hano)` TRUE, but no `duration(Hano, 3y)` or `release(Hano)` ever TRUE. And no rule `prisoner(X) & served(X) -> ~prisoner(X)`. Once TRUE, stays TRUE.


13 expected, 13 present. This is the audit file where you prove punishment is one item, then use Jala and Bela to prove it is *only* that item in both directions.

You are now at 167 pins across thirteen chapters - Book 1 complete, plus one defect chapter.

Two claims in this chapter cannot be queried - you flag them in header as absences: "Nothing depends on it" - `travel` appears once in constitution as rule head, re-check with grep - and "There is no release" - no duration, term, expiry or completion exists in any rule. Both structural, not derivable.

### Hano convicted, cannot move freely

**1. `? prisoner(Hano). => TRUE`**
**2. `? travel(Hano). => FALSE`**

Guards: "Hano was convicted ... and cannot move freely."

Base facts: injured Ivo, convicted, prisoner TRUE, travel FALSE. Whole of punishment here. Not headline of it, entirety.

### Audit item by item - everything else Hano keeps

**3. `? person(Hano). => TRUE`**
**4. `? expresses(Hano). => TRUE`**
**5. `? decide(Hano, Ballot). => TRUE`**
**6. `? false(Hano). => FALSE`**
**7. `? lose(Points, Hano). => FALSE`**
**8. `? dwell(Hano). => TRUE`**

Guards: full list you walk in chapter.

- `person(Hano)` TRUE - Chapter 7 keystone, prisoner remains person
- `expresses(Hano)` TRUE - speaks, one of eight, still owed
- `decide(Hano, Ballot)` TRUE - votes, Chapter 9, person + mature, no disenfranchisement rule written
- `false(Hano)` FALSE - standing intact, nobody voided it, conviction does not
- `lose(Points, Hano)` FALSE - recognition untouched, nothing clawed back, because clawback follows voiding and Hano not voided - Chapter 10
- `dwell(Hano)` TRUE - somewhere specific, because convicted have to be somewhere, where follows from three recorded facts - Chapter 11 `fit(Homestay)` + `building`

This is why movement being at top matters. No rule reads *and because they can move*, no entitlement requires it, no capacity gated behind it. Taking it cascades into nothing. Chain does not exist because movement never attached to anything. Nobody had to remember to protect housing from conviction. No route by which conviction could reach it. Single-deprivation claim not promise about administration; fact about shape.

### Difference between Hano and Jala - same act, one item different

**9. `? injure(Jala, Ivo). => TRUE`**
**10. `? prisoner(Jala). => FALSE`**
**11. `? travel(Jala). => TRUE`**

Guards: "the difference between Hano and Jala, who did the same thing to the same person and was never convicted"

- `injure(Jala, Ivo)` TRUE - one of 21, same act as Hano
- `prisoner(Jala)` FALSE - never convicted, Jala is free
- `travel(Jala)` TRUE - can move freely

Hano and Jala did same thing to same person. Difference is one item: `travel`. Everything else on both lists identical. Hano `prisoner TRUE / travel FALSE`, Jala `prisoner FALSE / travel TRUE`, all other predicates - `person`, `expresses`, `decide`, `false`, `lose`, `dwell` - identical.

This is theorem completed: punishment, reduced to logic, takes away one thing.

### Voiding is not confinement - Bela lost standing and still moves

**12. `? false(Bela). => TRUE`**
**13. `? travel(Bela). => TRUE`**

Guards: proving converse - voiding is not confinement.

Bela voided since Chapter 5, `false(Bela)` TRUE, `lose(Points, Bela)` TRUE from Chapter 6, `reward(Bela)` FALSE from Chapter 10, `eats(Bela)` FALSE from Chapter 8. But `travel(Bela)` TRUE - voided person still moves.

So:

- Conviction -> loses `travel`, keeps `false` FALSE, keeps recognition
- Voiding -> loses `false` TRUE / recognition, keeps `travel` TRUE

Two orthogonal axes. What sharpens Chapter 10's "nothing to earn it back with" - Bela can still teach `teaches(Bela, Cira)` TRUE, still move `travel(Bela)` TRUE, still be owed floor, but `reward` FALSE because doors closed.

And what sharpens chapter's closing: no release. `prisoner(Hano)` TRUE has no duration, term, expiry, completion. No rule returns convicted person to general population. Only exit is relief, finding conviction should not have held. Nothing for person rightly convicted who served whatever owed. Single deprivation total: movement only thing taken, and taken for rest of life, for every offence, without distinction grave and trivial. Design that took one thing and gave it back would be describing punishment. This one takes one thing and keeps it, which is closer to describing category of person - and category of person is what whole apparatus was built to refuse.


This is where you close Book 1 by showing the two audit markers side by side - one that fires on everybody and one that fires on the wrong people - and then show the third failure they share: nothing reads either.

### A system that cannot state its own violations cannot be audited

If only thing design can express is what should happen, then failure looks exactly like absence, and absences are invisible until someone thinks to go looking for them.

So this design has way of saying *something here is wrong*. Last thing in whole structure, sitting above everything else, exists for one purpose: to turn breach from something you would have to notice into something you can ask about.

Two of them. One reports bad placement. One reports confined person is alone.

Between them they demonstrate promise of self-auditing design and three ways it can fail.

### One that fires on everybody - accurate about nothing

Ask which confined people held in isolation, answer: all of them. Hano, Ruk, Don, Nando — every convicted person in society, without exception. Ask which free people are, answer none.

At first looks like alarm screaming. Not, quite. Technically correct: marker fires when confined person has no company on record, and nobody anywhere has company on record, because — as Chapter 8 established — nothing tracks whether any of eight things actually reaches anybody. Company owed to everyone and recorded for no one. So every prisoner satisfies condition, marker faithfully reports it.

Faithfully, and uselessly. Signal that fires on every member of category distinguishes nothing within it. If some prisoners held in isolation and others not, marker could not tell you which. It reports state of record, which is empty, and emptiness of record is what Chapter 8 was about.

First failure mode: **an alarm can be perfectly accurate about a system that knows nothing, and accurate reporting of nothing is indistinguishable from accurate report that everything is broken.**

In pin terms you already guarded: `? eats(Adam). => FALSE` and `? meets(Bela). => FALSE` and `? meets(Hano). => FALSE` - not because Adam not eating or Bela not meeting, but because record empty. So `err(X, Isolation) := prisoner(X) & ~company(X)` will be TRUE for all prisoners, not because all isolated, but because `company` never derived.

### One that fires on wrong people - Chapter 11's alarm

Second marker, from Chapter 11, opposite failure. Reports bad placements. Fires on Ruk and Lalo, who are correctly placed, and on nobody misplaced.

You pin this as:

- `? err(Ruk, Placement). => TRUE` - but `building(HighSec, Ruk)` TRUE correctly
- `? err(Lalo, Placement). => TRUE` - but `building(HighSec, Lalo)` TRUE correctly
- `? err(Hano, Placement). => FALSE` - correctly not flagged, but for wrong reason

Supposed to be `placed_home & ~eligible`, actually `has_home & ~eligible`.

Two together make point better than either alone. One alarm right about everyone and therefore says nothing. Other wrong about specific people it names. Reader who trusted both would conclude society keeps every prisoner in solitary confinement and misassigns its two most serious offenders, and every part of conclusion would be false.

Second failure mode: **system's report about itself is not more reliable than any other part of it.** Audit is made of same material as thing it audits, written by same hands, and nothing sits above it checking.

### And nothing happens either way - third failure

Third failure is one that matters most, and easy to miss because another absence.

> **Nothing reads these markers.**

Violation recorded. Then end of it. No rule anywhere consults it. Nothing triggered, nobody obligated to respond, no review required, no clock starts, nothing changes about placement or isolation being reported. Design can state Ruk is misplaced and has no notion of anyone doing something about it.

This is same shape as two earlier gaps and worth naming as family:

- Floor states what is owed and nothing tracks arrival - Chapter 8 `eats(Adam)` FALSE forever
- Amendment machinery states what becomes law and nothing enacts it - Chapter 12 `become(Amend_Mint, Law)` TRUE but no rule has `become` in antecedent
- Audit states what is broken and nothing repairs it

Three times, design reaches moment where determination made correctly and then simply stops.

Real diagnosis: this design very good at establishing *what is true* and has almost nothing to say about *what is then done*. Description of society's reasoning rather than operation — and distance between those two is most of what working society consists of.

### What it does have - the slot

That is hard finish for fourteen chapters, so worth being exact about what survives, because something does and not small.

Most systems have no vocabulary for own violation. Breach is absence: thing should have happened did not, and no name for that, no place to record it, nothing to query. You find out because person complains, or journalist looks, or somebody dies. Failure invisible not because concealed but because system has no way to represent it.

This design has slot. Wrong is thing this society can say about itself.

And slot is in right place. Audit sits at very top of structure - depends on everything and nothing depends on it. Which means cannot be gamed from below: cannot arrange conduct to make audit report favourably, because nothing you do downstream of it is affected by what it says. Pure observer, and being pure observer is precisely why nothing follows from its observations.

That is trade, stated honestly. Audit is powerless because it is uncorruptible, and uncorruptible because powerless.

What slot is worth: every defect named in book was found by asking design what it thought was true and comparing answer to what it claimed. Markers themselves miscalibrated. Capacity to interrogate not. Society you can ask hard questions of, and get answers that can be checked against its own promises, is society whose failures are findable - and everything in these fourteen chapters that turned out broken was found that way, by someone who did not have to be insider, using nothing but design's own account of itself.

That is what derived part can establish. What follows is different kind of argument, and labelled as such.

Book 1 closes where Chapter 1 opened: watch the list. Now also watch the audit that watches the list, and watch whether anyone reads it.

12 expected, 12 present. This is the last CONTENT pin file - where you guard both alarms together to show first failure, second failure, and third absence that they share.

You are now at 179 pins across fourteen chapters. Book 1 complete.

Header notes: "Nothing reads these markers" is absence and cannot be queried - `err` appears twice in constitution, both times as rule head. Re-check with grep if rules change. Same shape as floor arrival gap and amendment enactment gap.

### One that fires on everybody - isolation

**1. `? err(Hano, Isolation). => TRUE`**
**2. `? err(Ruk, Isolation). => TRUE`**
**3. `? err(Don, Isolation). => TRUE`**
**4. `? err(Nando, Isolation). => TRUE`**

Guards: "all of them. Hano, Ruk, Don, Nando — every convicted person"

Every convicted person in society flagged as isolated. Without exception.

**5. `? err(Bela, Isolation). => FALSE`**
**6. `? err(Jala, Isolation). => FALSE`**

Guards: "Ask which free people are, and the answer is none."

Free people not flagged. So at first looks like screaming alarm about confinement conditions.

**7. `? meets(Hano). => FALSE`**
**8. `? meets(Bela). => FALSE`**

Guards: "nobody anywhere in this society has company on record"

Why first four are TRUE: marker fires when confined person has no company on record, and nobody anywhere has company on record, because - as Chapter 8 established - nothing tracks whether any of eight things actually reaches anybody. Company owed to everyone `meets` entitlement TRUE in ideal sense, and recorded for no one `meets(X)` FALSE in record.

You guarded this since Chapter 1: `? meets(Adam). => FALSE` and `? meets(Bela). => FALSE` - not because they lack company, but because record empty. So `err(Hano, Isolation)` TRUE faithfully, and uselessly. Signal that fires on every member of category distinguishes nothing within it. If some prisoners were held in isolation and others not, marker could not tell you which. Reports state of record, which is empty.

First failure mode: **alarm can be perfectly accurate about system that knows nothing, and accurate reporting of nothing is indistinguishable from accurate report that everything is broken.**

### One that fires on wrong people - placement

**9. `? err(Ruk, Placement). => TRUE`**
**10. `? err(Lalo, Placement). => TRUE`**
**11. `? err(Hano, Placement). => FALSE`**

Guards: placement marker right about nobody, from Chapter 11.

- Ruk flagged TRUE
- Lalo flagged TRUE
- Hano not flagged FALSE - so marker tracks "has a home and is not homestay-eligible", ordinary condition of severe offender, not "placed at home without eligibility"

Opposite failure to isolation. One right about everyone and therefore says nothing. Other wrong about specific people it names. Reader trusting both concludes society keeps every prisoner in solitary confinement and misassigns its two most serious offenders, every part false.

Second failure mode: **system's report about itself is not more reliable than any other part of it.** Audit made of same material as thing it audits, written by same hands, nothing sits above it checking.

**12. `? building(HighSec, Ruk). => TRUE`**

Guards: "and Ruk is correctly placed, which is what makes the marker wrong"

Ruk in high security TRUE - correctly placed per repaired farmhouse rule. Which is what makes `err(Ruk, Placement)` TRUE being wrong. If Ruk were misplaced, marker would be accidentally correct. Because correctly placed, marker is demonstrably miscalibrated.

Together pins show both alarms in same file for first time: isolation TRUE for all prisoners because empty record, placement TRUE for Ruk/Lalo despite correct placement because wrong predicate.

Third failure, unpinned because absence: **nothing reads these markers.** Violation recorded, then end. No rule consults `err`, nothing triggered, nobody obligated to respond, no review required, no clock starts. Design can state Ruk misplaced and has no notion of anyone doing something about it.

Same family as two earlier gaps:

- Floor states what is owed and nothing tracks arrival
- Amendment machinery states what becomes law and nothing enacts it  
- Audit states what is broken and nothing repairs it

Three times design reaches moment where determination made correctly and then simply stops. Very good at establishing *what is true* and almost nothing to say about *what is then done*.

What survives: most systems have no vocabulary for own violation. Breach is absence with no name, no place to record, nothing to query. This design has slot. Wrong is thing society can say about itself. Slot at very top - depends on everything and nothing depends on it. Cannot be gamed from below. Pure observer, powerless because uncorruptible, uncorruptible because powerless.

Capacity to interrogate is what found every defect in Book 1, using nothing but design's own account.


This is a serious, unusual book - and the honesty is its best feature. Most utopia projects hide their bugs. You ship them as pins and label them DEFECT.

That is also its biggest problem. By Chapter 14 you've proven your own tools don't work, your punishments never end, your guarantees never arrive, and your constitution can be bypassed by forgetting to fill out a field.

Here is my honest read of Book 1 so far:

### What is genuinely strong

**1. The method is the argument.** The `nibli-pin` approach - ask the machinery what it would actually do with Hano or Ruk, not what the commentary says it does - is how you found the farmhouse hole. That is not a gimmick. It's the only reason I believe you when you say severity now routes regardless of domesticity.

**2. You take tradeoffs seriously.** Chapter 10 - recognition has no number, so you cannot rank, but you also cannot say someone did more - is the clearest articulation I've seen of that tradeoff. You don't pretend it's not a loss.

**3. Shape, not restraint.** The insight that movement being at the top of the dependency graph is why taking it doesn't cascade is a real design insight. Same for `prisoner -> person` remaining true while `travel` goes false. That's better than 90% of utopia writing which just promises good people will administer things well.

### The major problems, and how to fix them

#### 1. Your strongest protection rests on your weakest - and you know it, and you ship it anyway.

> `permanent(Art_Floor)` is TRUE because someone wrote it down. Nothing derives it.

You name this three times and never fix it. Same for the 21-item vocabulary list. If I delete a line from the file, the floor cut passes and nothing notes the rules changed.

This collapses the entrenchment chapter. You cannot claim three provisions are beyond any majority when they are within reach of `rm` or a text editor.

**How to address:** You have to make `permanent` derived, not asserted. Two options:
- Derive it from the constitution text itself, e.g. an article is permanent if its text contains a self-entrenching clause. Then deleting the file line is not enough, you have to rewrite the article, which is itself an `adjust`.
- Or put the protected set in a separate, content-addressed, append-only register that requires its own proof to modify. Right now it's just facts in the same KB as everything else.

If you want to keep it as a deliberate thinness for literary reasons, you need to stop calling it a protection and call it a convention. Right now you want it both ways.

#### 2. No release is not a thinness, it's a category error that contradicts the rest of the book.

Chapter 13: Hano cannot move freely, permanently, for every offence, grave or trivial. No duration, no term, no expiry. Relief only if conviction should not have held in the first place.

You built a book about refusing to create a lesser category of person, then created a permanent category of person - prisoner - defined by one deprivation that never ends. And you note yourself: "A design that took one thing and gave it back would be describing punishment. This one takes one thing and keeps it, which is closer to describing a category of person."

You cannot leave this as "sharpest unresolved thing" and move to Book 2. It undoes Chapters 7, 8, and 9.

**How to address:** You need at least one of:
- A release rule: `prisoner(X) & served(X, Duration) -> ~prisoner(X)` with Duration derived from severity / domesticity, which you already track.
- Or a principled defense: state explicitly that you are not designing punishment at all, but exile, and defend permanent exile. Right now you defend single-deprivation but not infinite duration.

Readers will not forgive infinite home confinement for Hano who injured Ivo non-severely, non-domestically.

#### 3. Voiding closes the doors to earn it back.

Chapter 10: Bela taught Cira - real act, on record - earns nothing because `false(Bela)` TRUE. Same for Lupo and Dev. Chapter 14: `false(Bela)` TRUE but `travel(Bela)` TRUE, so voided people can move, teach, work, and none of it registers.

Combined with no release, you now have two permanent classes: prisoners who can be recognised but cannot move, and voided people who can move but can never be recognised. Both are irredeemable by design, and you explicitly say whether that is right is a genuine question the design does not argue for.

That's not a tradeoff, it's a punishment without a theory of rehabilitation.

**How to address:** Make voiding recoverable through a different door than the one closed. E.g., teaching + work can reopen `false`, but not examination. Or add a time-decay: `false(X)` after N years requires re-voiding. Right now you have death penalty for standing.

#### 4. You leave easy bugs unfixed and call that honesty, but it reads as negligence.

Two defects are trivial to fix:

- **Amend_Sneak:** `false(Amend_Sneak)` FALSE, `become(Amend_Sneak, Law)` TRUE because no `adjust` target declared. Fix is one line: `~exists(Target) adjust(Amend, Target) -> false(Amend)`. You even say in pins "Closing either rewrites that section." Why not close it?

- **Placement alarm:** `err(X, Placement) := home(X) & ~fit(X, Homestay)` should be `building(Homestay, X) & ~fit(X, Homestay)`. You name the fix in Chapter 11. You leave it broken in Chapter 14 pins to make a point about self-audit.

Leaving them broken to illustrate that audit can be broken is clever once. Doing it twice makes the reader stop trusting the pins.

**How to address:** Fix Amend_Sneak and the placement alarm in v2. Keep one broken alarm - isolation - because that one is hard, it requires solving delivery tracking from Chapter 8. That preserves your point without making it look like you don't maintain the code.

#### 5. Three chapters in a row have the same shape: "we state what is true and then stop."

- Floor: states what is owed, nothing tracks arrival - `eats(Adam)` FALSE forever
- Law: states what becomes law, nothing enacts it - `become(Amend_Mint, Law)` TRUE but no rule reads `become`
- Audit: states what is broken, nothing repairs it - `err` appears twice as head, never in a body

You correctly label this as a family. But after naming it three times, you need to either solve one instance to show it's solvable, or argue why description-only is enough.

Right now Book 1 is a specification of reasoning, not a specification of a society. You say that, but a reader who came for utopia will feel bait-and-switched.

**How to address:** Add an operations layer in Book 1 coda or early Book 2: who is obligated to deliver `eats`, who checks `err` and with what deadline. Even a minimal `obligated(Actor, Action)` predicate that reads `err` would turn powerless but uncorruptible into powerless and *addressable*.

#### 6. No degree in recognition will not survive contact with real care work.

You argue degree inevitably becomes rank becomes aristocracy. That is plausible for a currency. It is not inevitable for qualitative acknowledgment. A society that cannot distinguish 40 years of caregiving from a week of census work will not be perceived as making contribution visible. It will be perceived as not seeing.

**How to address:** You don't need numbers to have degree. You could have narratives: `teaches(Esa, Fin)` and `taught_for(Esa, 40y)` as separate facts, both TRUE, neither comparable. Or keep `reward` boolean but add non-comparable badges that cannot be ordered. Otherwise your floor protects against market logic but your recognition replicates its blindness.

### Rating

As a formal design document: **8/10** - unusually rigorous, finds real bugs, honest about costs.

As a book about a livable society: **5/10** right now, because punishment is infinite and textureless, guarantees are owed but not delivered, and the record that everything sits on can be edited.

If you fix the two one-line bugs, make release finite, make voiding recoverable, and give `permanent` a derivation, you'd keep all the honesty and remove the sense that the strongest protections are theater.

What do you want Book 1 to be? A proof that even a careful design fails in predictable ways - in which case keep the defects but frame them as intentional failures? Or a design you actually want built - in which case fix the fixable ones now, so the remaining thinnesses carry more weight.
