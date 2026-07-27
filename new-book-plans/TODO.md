# TODO — the derived book

Tracker for the new book: a third artifact, derived from the nibli constitution,
written in plain English for a **primarily international/global audience**, with
the formalism invisible to the reader and the *data* the thing readers verify.

Plain bullets, never numbered. Work the FIRST remaining bullet; delete it entirely
when it fully lands, update it if only partly done. Ordered by dependency and
leverage, not by chapter order. One item at a time: do it, verify it, commit it.

The root `TODO.md` remains the tracker for the OLD `book.md` / `manifesto.md`.
This file governs the new book only.

**nibli handoff protocol.** dhilipsiva wrote nibli. When an item is blocked by an
engine bug or a missing KR construct, do not work around it in prose — the bullet
carries a ready-to-paste **HANDOFF PROMPT** for a Claude Code session in
`~/projects/dhilipsiva/nibli`. Hand it over, work the next unblocked bullet, and
resume when it lands.

**Provenance: 2026-07-27 verification pass.** Nine parallel verifications against
primary sources, plus the whole pin set re-run on the real engine (`nibli-host
--script`, release wasm, `NIBLI_FUEL=2e12`). What survived and what did not is
recorded per bullet. Headline: the *stratification and the exploit closures are
real and reproduce exactly*; the *harness, the harvest premise, and about a third
of the citations* do not.

---

## Blocking decisions — nothing should be drafted until these are settled

- **[AUTHOR-GATED] Decide the licence before a single chapter is committed.** This
  repo is **CC0 1.0** — an *irrevocable* dedication to the public domain (`LICENSE`
  lines 65, 86). Anything committed here is dedicated as committed; a later
  "actually I want a trade deal" cannot claw it back. `book.md` and `manifesto.md`
  are already out and that is fine. The new book is the decision. Options: draft in
  a private repo and publish only what you choose; keep this repo CC0 but put the
  new book under its own `LICENSE` in its own directory; or accept CC0 for it too
  and treat serialisation, not exclusivity, as the channel. This is not a legal
  opinion — but the choice must precede drafting, because the commit *is* the
  publication.

- **[AUTHOR-GATED] Pick ONE canonical rights floor and make the other artifacts
  cite it.** The plans said the floor had drifted three ways. Verification found it
  is **worse**: `book.md` alone carries at least five mutually inconsistent floors,
  and the sentence that actually does the firewall work names **seven** items, not
  the eleven `1.md` reports. The constitution has six (`secure, eats, dwell,
  healthy, learn, expresses`); the manifesto has five (`food, shelter, healthcare,
  education, mobility`) — security and expression absent, mobility promoted to the
  floor though the constitution derives it only as a defeasible permission. The
  floor is the one thing in the design that must not drift, and it has drifted
  inside a single file. Decide the canonical six (or seven), amend `utopia.nibli`
  if the answer is not what it currently says, and make everything else quote it.

- **[AUTHOR-GATED] Re-derive Part V — the harvest premise does not survive contact
  with the manuscript.** `3-spine.md` proposes lifting four `book.md` chapters
  intact. Two of them **are not chapters**: "The Five Joints" is a 192-word `##`
  section inside "Learning from Those Who Tried", and "The Calculation Problem" is
  a 540-word `##` section inside "Employment, Reimagined". The two real chapters
  carry **7 and 5** named cross-references to material the new book drops —
  against `1.md`'s own stated threshold that a chapter referencing six others is
  not harvestable. Worst case is the showpiece: the social-credit chapter's
  most-praised passage ("Those passages now state the bright line") points at three
  passages in three dropped chapters. Either rewrite these as new chapters that
  stand alone, or drop the harvest and let Part V be written fresh.

- **[AUTHOR-GATED] Title, and whether "Minimum Viable Society" comes across.** The
  old book's best coinage is MVS. For a global audience, decide whether the new
  book keeps it, and settle the title before the sample chapters go out.

## The verification harness — build this before writing prose, so every later claim is checkable

- **Adopt nibli's own pinned-verdict format for the constitution's pins.** nibli
  already solved this: `determinism-corpus.nibli` annotates every query with
  `# => TRUE` and three separate CI legs assert against those annotations. The
  book's fidelity table should be the same artifact in the same format, not a
  Markdown table with green ticks. Convert `utopia-v2-run.nibli` to it.
  *Verified today:* every one of the fidelity table's seven rows is **true** on the
  engine (`person(Hano)` TRUE, `expresses(Hano)` TRUE, `travel(Hano)` FALSE,
  `travel(Adam)` FALSE, `travel(Jala)` TRUE, `prisoner(Jala)` FALSE, `eats(Adam)`
  FALSE, `healthy(Bela)` FALSE) — but **not one of them is reproducible from the
  committed artifacts**. That gap is the whole reason for this bullet.

- **Fix the run script: it loads the wrong constitution and records no
  expectations.** `utopia-v2-run.nibli` line 1 is `:load utopia.nibli` — it pins
  **v0.1**, not the v0.2 file it is named for. And it lists queries with no
  expected verdicts, so it cannot fail; it is a transcript, not a test. Six of the
  seven fidelity rows have no query in it at all.

- **Delete `run-kb.rs`, or make it the real runner — it cannot run the committed
  script.** It dispatches only `:load`, `:contradictions`, `?` and comments; the
  pin script is almost entirely `:proof-verbose` lines, which fall through to
  `assert_text` and produce **42 syntax errors and zero verdicts**. It is also
  wired into no `Cargo.toml`. `nibli-host --script` already does this job and does
  support `:proof-verbose` (but not `:contradictions` — pick one runner and make
  the script match it).

- **Make fuel exhaustion a hard failure, never a silent FALSE.** At default fuel,
  `travel(Hano)` and `travel(Jala)` return `RESOURCE_EXCEEDED (fuel)` — not TRUE,
  not FALSE. Any harness that treats "not TRUE" as FALSE would have scored the
  fidelity table green while proving nothing. nibli's own determinism gate
  explicitly **excludes** fuel-trapping queries as runtime-dependent. Pin
  `NIBLI_FUEL` in the harness, and fail loudly on `RESOURCE_EXCEEDED`.

- **Fix or replace `4-strata.py`.** The stratification it reports is **exactly
  right** — reproduced today: 34 predicates, 15 derived, 19 base-only, 26 rules,
  max stratum 3, strata membership matching `3-spine.md` line for line, with
  `authority` the only derived predicate whose cone is negation-free. But its
  parser takes only the *first* predicate on a fact line, so `secure`, `eats`,
  `healthy` and `learn` are **invisible to it** — the four floor rights the book's
  central finding is about are not in the 34. Finding (a) is true; the script did
  not compute it. Either extend the parser to see inside `event { … }` blocks, or
  stop presenting the finding as computed.

- **Write the claim-to-query table as a generated artifact, not a hand-maintained
  one.** One row per load-bearing sentence: sentence, query, expected verdict.
  Regenerated on every constitution change; any row whose verdict flips is a
  paragraph that has started lying. Private to the author — the reader never sees
  it. This is the Catala pattern and the `err(Lalo)` bug below is the argument for
  it.

## Constitution (KB) work

- **Fix `err/2`: it fires on correctly-placed prisoners.** Verified on the engine:
  `err(Lalo, Placement)` is **TRUE** — but Lalo is severe+family and Article 6
  routes him correctly to `building(HighSec, Lalo)` (also TRUE). The rule
  `home($x) & ~fit($x, Homestay) -> err($x, Placement)` reads *"has a home"* as
  *"was placed at home"*. Any severe offender who happens to have a home trips a
  false breach. It works for Ruk (TRUE, intended) and Hano (FALSE, intended) and
  false-positives on Lalo. The author's own pin script queries `err(Lalo,
  Placement)` — with no expected value, so nothing caught it. Fix: separate the
  *fact* of having a home from the *decision* to place someone there.

- **Write the fact-write trust base as a file-level section — it is the
  constitution's actual security model.** The adversarial re-audit confirmed
  **15 further exploits** on the engine beyond the three disclosed, and they share
  one root cause: *nibli cannot make a predicate derived-only, so every gate v0.2
  calls "derived" is still assertable.* Verified attacks: `authority(Pax).`
  reopens E1a verbatim (`defend(Don)` TRUE, `prisoner(Don)` FALSE);
  `fit(Ruk, Homestay).` silences E3's breach marker; two asserted
  `permits(Review, ·)` facts defeat Article 8's headline claim outright and void an
  innocent (`false(Ara)` TRUE, `lose(Points, Ara)` TRUE) using sock puppets the
  Electorate never seated. Others worth naming: `rotten/1` is a single-writer
  universal void; `broken(Court).` is a one-fact universal amnesty; one asserted
  `deceive` jails the file's own honest whistleblower Rebel; Article 9's `adjust`
  is self-declared by the proposer, so a target-less amendment enacts
  unconditionally. The file discloses this hole for `permanent()` only (lines
  150–154). Promote it: list **every** predicate whose direct assertion breaks a
  stated guarantee — `permits(Review,·)`, `permits(Appeals,·)`, `authority`, `fit`,
  `defend`, `rotten`, `deceive`, `severe`, `family`, `broken`, `parent`, `teaches`,
  `work`, `adjust`, `permanent`.

- **Restore v0.1's stratification note to Article 7 — its deletion is a live
  landmine.** v0.1 carried: *"(No `person(_)` condition: person depends on prisoner
  via Art 1, and prisoner uses `~defend` — that would form an unstratifiable
  negative cycle.)"* v0.2 dropped it. Adding `person($w)` to the shield rule is the
  most natural tightening anyone would reach for, and it is **rejected atomically**
  — the replacement silently vanishes and the *original permissive rule stays in
  force*. That is precisely the "a permissive rule left in place keeps its exploit"
  failure the v0.2 header warns about, now reachable through the stratifier rather
  than through oversight.

- **Decide what to do about the fail-open shield window.** `defend(Sly)` TRUE /
  `prisoner(Sly)` FALSE is verified and working as designed — a defendant who
  exposes a real authority stays free until Review adjudicates. The plans call this
  a disclosed cost; the audit calls the disclosure understated. Bound it, or state
  the bound honestly in the chapter.

- **Grow the provisioning layer, or write Part I to stop where it stops.** Verified:
  `eats(Adam)` FALSE, `healthy(Bela)` FALSE, and — new today — `secure(Bela)` FALSE,
  `learn(Cira)` FALSE. The gap is uniform across all four zero-rule floor rights.
  Not denial; no rule connects an obligation to any fact about anything reaching a
  person. The obligation layer is complete and the delivery layer does not exist.
  Chapters 1–2 are writable now; a "does it actually arrive" chapter is not. Keep
  this visible in the prose either way — it is the single most credibility-buying
  admission the book has.

- **Widen kinship beyond `parent/2`.** The multi-sig independence check excludes
  only parents; spouses and siblings co-sign freely. Disclosed in v0.1, still open.

- **Give `rotten` an expiry, rehabilitation, or appeal path.** A single void is
  currently perpetual and compounds — no route back. For a constitution whose
  thesis is that sanctions are defeasible, that is a contradiction in the machine.

## nibli handoffs — blocked on engine work

- **HANDOFF: derived-only (intensional) predicates.** This is the root cause of 13
  of the 15 new exploits and it defeats the constitution's central security claim.
  Prompt to paste into a nibli session:
  > In nibli KR, a predicate that appears as a rule head can still be asserted
  > directly as a fact — a rule *adds* a derivation path, it never *removes*
  > assertability. I need the opposite for a constitutional model: a way to declare
  > a predicate **derived-only**, so that any attempt to assert it as a ground fact
  > is a compile/assert-time error, and its only route to TRUE is derivation.
  > Concretely, in `utopia.nibli` I derive `permits(Review, X)` from
  > `choose(Electorate, X) & ~rotten(X) & ~broken(X)`, and the whole point is that
  > nobody can hand themselves a credential — but `permits(Review, Sock).` still
  > works and voids an innocent party through the multi-sig rule. Same for
  > `authority/1` and `fit/2`. Please add an EDB/IDB separation: a declaration
  > (syntax your call) marking a predicate intensional, enforced fail-closed at
  > assert time, with a clear error. Needs to survive retraction/rebuild and behave
  > the same on all three runtimes. Please also say whether this interacts with
  > stratification or the fact-store replay.

- **HANDOFF (verify need first): exact minor-unit arithmetic.** The plans claim any
  quantitative treatment of contribution is blocked because "engine float
  comparison is tolerant". That is only half right — nibli has **both** tolerant
  (`sum`) and exact (`num_equal`/`dunli`) comparison, plus a guarded `quotient`
  with an exact divide-by-zero rule, all over f64. Before asking for anything,
  settle whether the book needs merit arithmetic at all: the old book already
  decided merit points are earn-only recognition with the arithmetic *deliberately
  absent*. If that holds, this item is **moot — delete it**. If the new book wants
  summed or compared quantities, the ask is integer/decimal minor units so that
  exact totals are representable without float error.

## Data — "latest data, by script" is a build system nobody has written yet

- **Build the data pipeline before writing the empirical chapters.** The stated
  requirement is that the book depends on the latest data *as much as possible,
  achieved through scripting* — but `final-research.md` is a hand-assembled static
  snapshot, and today's pass found the predictable result: figures two tax years
  stale, a superseded working paper, market data from 2015. Design: one machine-
  readable claim registry (claim id, value, units, source, retrieval date, fetch
  script); fetchers against sources that have APIs (World Bank, WHO GHO, UNEP,
  IEA, OWID, FAOSTAT); a rendering step that injects current values into the prose;
  and a **staleness gate** that fails the build when a figure's source has a newer
  edition than the one pinned. Where a number can only come from a paper, the
  registry pins the version and the retrieval date so the drift is visible.

- **Give the reader a verification path, since they cannot see the logic.** The
  formalism stays invisible — so what the reader verifies is data. Ship the claim
  registry as the public artifact: every number in the book, its primary source,
  the date it was fetched, and the script that fetches it. This is the thing that
  earns the trust, and it is the honest substitute for showing the constitution.

- **Re-cite everything against the published versions.** Muralidharan, Niehaus &
  Sukhtankar is no longer a working paper — it is *Review of Economics and
  Statistics* 107(2): 372–392 (2025). Expect several others to have moved similarly.

## Correcting the research brief — each is a discrete, committable fix

- **Rewrite the social-choice paragraph — it is the most damaging error in the
  brief.** The claim that score voting "escapes Gibbard–Satterthwaite's ordinal
  frame", with the gloss *"it is always optimal for a voter to give the best
  candidate the highest possible score"*, is unsourceable and inverts the result:
  **Gibbard's 1973 game-form theorem applies directly to score voting, and score
  voting is manipulable**. The quoted sentence describes strategic exaggeration,
  not strategyproofness. Also: Arrow's theorem needs the **transitive-social-
  ordering** condition the brief drops (relaxing it is a real escape route);
  Gibbard–Satterthwaite needs **determinism/single-valuedness** (randomised schemes
  escape, per Gibbard 1977); Black (1948) gives the *Arrow* escape on single-peaked
  domains but **Moulin (1980)** gives the strategyproofness escape, with the
  McKelvey–Schofield caveat that it dies in multiple dimensions; and the
  "two-thirds is neither manipulable nor dictatorial" quote has no source — the
  substance is the **two-outcome** restriction, not the supermajority threshold.
  The defensible claim in this vicinity is the sincere-favourite criterion. Getting
  this wrong is what gets the book dismissed by exactly the readers it wants.

- **Fix the Housing First bullet — two outright errors.** The AJPM Community Guide
  economic review is **Jacob et al. (2022)**, not "Chapman et al. (2021)". And
  "decreased homelessness by 88% versus 47% for Treatment First" misdescribes what
  the CPSTF review reports. Re-derive both from source before the sentence is used.

- **Fix the Muralidharan quotation — it is a splice presented as verbatim.** The
  sentence given as "verbatim from the abstract" appears in **no** version of the
  abstract: it welds the February 2020 abstract (which says **10%**) onto a
  **10.6%** figure that comes from the body of the September 2021 revision. Related
  number fixes: "~2 million lost access" should be **1.5–2 million**; "~1.6 million
  (13% of beneficiaries)" should be **1.7 million** (1.2 million under the paper's
  conservative assumption), and the 13 is a percentage-*point* increase in treated
  blocks only. The "almost 90% genuine" figure — the brief's self-declared
  strongest datapoint — is **88%**, is labelled *"purely descriptive"* and
  non-causal by its own authors, and covers **1.44 lakh** deletions in 10 study
  districts, not the 11 lakh statewide cancellations.

- **Reframe Santoshi Kumari around what is documented.** The *cancellation* is
  documented (card struck off 22 July 2017; the block development officer confirmed
  the Aadhaar-seeding failure; rations refused for months before). The *cause of
  death* is **officially disputed** — a district team reported malaria, the family
  was reportedly harassed for "defaming the village", and no court has adjudicated
  it. Lead with the documented chain, note the dispute in the same breath. Stating
  "died of prolonged hunger" as uncontested is one search away from being caught,
  and this case is the emotional anchor of the strongest chapter.

- **Replace the Mandela Rules "authoritative gloss" — it is a blog post.** Rule 3
  is quoted **word-for-word correctly** (verified against A/RES/70/175), and the
  soft-law characterisation is right and quotable from operative paragraph 8 of the
  adopting resolution. But the line offered as "one authoritative gloss" — *"the
  deprivation of liberty is the only permissible restriction imposed by a lawful
  sentence…"* — traces verbatim to a **December 2025 personal legal blog**.
  Replace with **Principle 5 of the UN Basic Principles for the Treatment of
  Prisoners** (GA res. 45/111, 1990), which says the same thing with standing.
  Also: "normalisation" is genuinely UNODC's gloss but is one of five principles,
  not "the" governing one, and the word appears nowhere in the Rules.

- **Fix the collateral-consequences and whistleblower numbers.** USCCR says
  employment-related consequences are *"most (roughly 70%)"*, not "60–70%"; the
  44,000 count is a 2019 snapshot that has drifted (the inventory now says "more
  than 40,000"; an independent 2022 count found 48,229). The ECI figures are
  misstated: 79% and 61% are among employees **who reported misconduct**, not all
  employees, and the 61% (10-country median, 2021) and 46% (42-country, 2020 and
  2023 waves) are **not comparable** — they must not be narrated as a decline.

- **Fix four misattributed quotations.** The Langdell *"study the things to be
  defined, rather than ready-made definitions"* line is **Young B. Smith (1913)**,
  not Langdell — legal historians will catch it instantly. Both anti-utopian quotes
  are **Scruton (2010)**, not "Popper/Scruton"; the second is a secondary-source
  paraphrase, and Popper's argument is structurally different and should be stated
  separately. The *"never an informational or even a computational problem"* line
  is **Nguyen's** QJAE sentence, not Boettke/Candela/Truitt's. The "elaborates too
  little on how to accomplish" complaint belongs to **neither** the Lowy Institute
  (whose review is favourable throughout) nor Global Policy Journal as quoted.

- **Restate Krugman honestly — he prescribes the opposite of concealment.** The
  brief says "Two Cheers for Formalism" prescribes the author's workflow. Krugman's
  step (3), which the brief omits, is *"Publish the intuition, the math, and the
  evidence — all three."* Steps (4)–(5) are an *additional* obligation, not a
  substitute. The stronger and honest framing: **the public nibli repo is what
  discharges Krugman's step (3)** — the apparatus is inspectable by anyone who
  wants it and invisible to everyone who does not.

- **Smaller citation fixes.** Roberts, *The Price of Everything*, PUP — first
  edition **2008** (pbk. 2009). Bregman: **Little, Brown (US) ~288pp / Bloomsbury
  (UK) 336pp**, English edition first from The Correspondent (April 2016), and the
  proposal is a **15-hour** week. HBS formalised the case method in the **early
  1920s** (Donham; "case system" adopted 1922), not mid-century — and the
  decision-forcing-case quote traces only to Wikipedia and governs *instructors*,
  not authors. Cottrell & Cockshott argue **labour-time** calculation is tractable,
  which is narrower than "solve the equations fast enough".

- **Cut or rebuild the Indian-market paragraph — and remove one defamation risk.**
  Lower priority now the audience is global, but if any of it survives: the figures
  come from the **Nielsen India Book Market Report 2015**, superseded by the 2022
  Nielsen BookData/FIP edition (**24,000+ publishers**, trade at **4%** of the
  print market). "Trade books in Indian languages account for roughly half of all
  sales" is **wrong** — the 2015 figure was 45% of *trade* sales only. And calling
  **Rupa** an "ideologically-aligned right-wing press" is unsupported and
  defamatory-adjacent: it is a 1936 general trade house and co-owner of Aleph.
  Delete that characterisation regardless of what else survives.

## Framing and structure

- **Reframe the whole brief's India-first assumptions for a global audience.** The
  research brief recommends foregrounding Bharathi and an India-first publishing
  route; the audience decision overrides that. India material stays as **evidence**
  — Aadhaar/PDS is among the strongest evidence the book has — but it is one case
  among several, not the frame, and every reference needs enough context for a
  reader who has never heard of a ration card.

- **Fix the poem attribution before it reaches print.** `1.md` attributes the
  manifesto's frame to Bharathiar's *நின்னைச் சரணடைந்தேன்*. That string appears
  **nowhere** in any of the three artifacts. `book.md`'s appendix attributes the
  poem to *Yoga Siddhi* ("Varam Kettal"), stanzas 4–5, and the manifesto's own Part
  2 Ch 1 epigraph is நின்னைச் **சிலவரங்கள் கேட்பேன்** — which `1.md` appears to
  have garbled into a title. Settle the correct name with a Tamil-literature
  source. If Bharathi survives at all in the new book it is as **one** framing
  epigraph — original, plain translation, one sentence on who he was — never as
  structure.

- **Write the introduction's honesty paragraph early, not last.** Two things belong
  there and both are load-bearing: that a formalisation makes commitments *precise*,
  never *justified* — nothing in logic says the floor should contain expression and
  not water — and that the system proves what is **owed**, not that anything
  **arrives**. Say both plainly or the book is dishonest; saying them is also the
  most disarming move available.

- **Draft Chapter 1 ("The Floor Nobody Computes") as the proof of method.** Short:
  the six obligations, why unconditionality is structural rather than promised (no
  rule can reach `obligated` — it appears in no rule head and no rule body, so
  nothing derives it and nothing can retract it), and the argument that computing
  eligibility is where denial lives. Ship it with its pinned-verdict file, and use
  it to prove the harness works end to end before Chapter 2.
