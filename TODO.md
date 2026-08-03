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
  legal collisions, costed transition) *and* the technology stack. Its tracker is
  `book-2/TODO.md` — collect there, do not work there while book-1 is active.
  book-1 references it once, at the end.
- **`book.md` and `manifesto.md`** — legacy, to be **deleted** once both new books
  are written. Nothing in this tracker improves them. The one obligation they carry
  is that no valuable material is lost on the way out; what still needs porting is
  itemised under **Legacy harvest** below (the 55 sourced references are already in
  `registry/claims.json`, and the five bright lines are swept — the result stands
  under **Standing facts and methods**; the clawback consequence it forced was ruled
  2026-08-02, bright line 2 standing narrowed).

**THE WORKING ORDER.** All fourteen chapter passes are complete (2026-08-02) and
their records live in git, not here. What remains runs in two phases plus
cross-cutting sections:

1. **Phase 1 — author-gated decisions.** First, because the chapters that flag
   these questions as open cannot close them until the decision above them is
   ruled — the ruling *is* what the chapter says — and because a lost decision
   costs more than any lost task; this section has been destroyed by tooling once
   and is watched accordingly.
2. **Phase 2 — engine handoffs (nibli).** Empty at the moment — nothing is pending
   upstream. It stays ahead of the writing because some of what the book has to
   concede is an engine limitation rather than a design choice, and it is dishonest
   to write the concession while the limitation is fixable.

The sections after the phases are cross-cutting: the remaining book-1 writing
(the opening note, Part V, the method part), the reach plan, the data work, the
legacy harvest, and a pointer to book-2's own tracker. **Standing facts and
methods** closes the file and holds knowledge, not tasks.

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
lands, so it is not re-proposed. **This section was destroyed by tooling once** — a
tracker-edit slice in `412e5a4` anchored on the next `---` after a separator an earlier
cleanup had removed, and swallowed 145 lines, all but one of them open; the loss went
unnoticed because nothing checks this file, and a later commit then described the
emptied section as "every earlier decision was ruled", which was false. Treat these as
the most expensive lines in the file. Line numbers cited inside bullets may predate
later edits — re-derive before trusting.

- **[AUTHOR-GATED] Decide whether book-1 opens with an epigraph.** At most **one**,
  original, plain translation, one sentence on who Bharati was, never as structure. The
  attribution is settled (2026-08-02): the poem is *Yoga Siddhi* (யோக சித்தி), the
  வரம் கேட்டல் stanzas, confirmed against Tamil-literature sources and consistent with
  `book.md`'s own appendix; the registry holds the reference (`bharati-yoga-siddhi`).
  This ruling also decides where the poem's full Tamil text and translations live after
  `book.md` is deleted — see the deletion gate under Legacy harvest.

- **[AUTHOR-GATED] EIU vs V-Dem — the democracy/happiness licensing fork.** The EIU
  index is non-redistributable — Our World in Data cannot export the series, so that
  escape hatch is foreclosed — and `LICENSING.md` commits the claim registry to CC0, so
  a CC-BY book with a public registry cannot ship those numbers. Cite-and-link keeps
  every figure intact but breaks the registry's promise that a reader can re-run it.
  Switching to **V-Dem** (openly licensed) means every number is re-derived: the r =
  0.52 attached to the V-Dem branch is quoted from a transcript, no V-Dem data is in
  the repo, and V-Dem's Regimes of the World categories are not EIU's four, so the
  regime table and the step sizes do not carry over — budget the re-derivation if
  the answer is V-Dem. The working analysis this decides the fate of is under **Data**
  below; the registry's `eiu-2026-democracy-index` entry is declared
  source-reference-only until this is ruled.


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
  gate before committing it** — the gate is now hard at zero. The subtitle itself is
  clean; a note that opens by naming the floor's size would not be.
  **The best evidence this note is load-bearing is on file** (`reviews/ai_review.md`):
  a sympathetic, capable reader finished the manuscript and concluded it is a teardown —
  *"a beautiful nightmare to show us what not to do."* The note has to tell a reader what
  they are holding before chapter 6 teaches them wrong: the confessions are the method,
  not the verdict.

- **The honesty paragraph goes in the opening note, and half of it is already in print.**
  book-1 has no introduction, so the destination this item used to name is gone. One half
  has landed: *the system proves what is owed, not that anything arrives* is stated hard in
  chapter 8, leaned on again in chapters 13 and 14. The other half is in no chapter — that
  a formalisation makes commitments **precise**, never **justified**; nothing in logic says
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
  "When the Pod Meets the State" is unsalvageable — 21 uses of "pod" in 2,092 words,
  and this book has no pods. The
  social-credit chapter is the best writing in the manuscript and unliftable, with seven
  named dependencies pointing at three chapters that will not exist.
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
  five-row summary table *is* the numeric self-grade in another notation, because one
  Survives plus three narrowed plus one Fails renders as "two and a half out of five"
  to any reader who wants it to, so no recap, no verdict word in a heading or the
  contents; and **every specification is a property
  of the finished society, never a task** — "allocation patterns by group are published
  in a form an outsider can check", never "set up an audit body", or the inclusion gate
  leaks out of the part that is exempt from only half of it.
  Two collisions to fix while drafting. One of the five joints is named **coercion**
  (what may be done to a person) and the coercion *concession* is assigned to the
  **state** joint (a body funded compulsorily) — same one-word-two-things problem as
  `standing`/`false`; disambiguate once in the frame with a forward reference. And the
  single book-2 pointer belongs at the end of the method part, not here.

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
  it names the body and says nothing compels it — which is the true state of the design
  and exactly the question this joint has to answer. The earned-time concession from the
  release ruling lands at the *coercion* joint next door: "voluntary" is structurally
  pressured when the alternative is longer confinement.

  **The texture ceiling, ruled 2026-08-02: four real channels, and no imagined people.**
  No record-person gets an inner life anywhere in this book, Part V included — inventing
  Cira's fear would fabricate exactly the kind of entry the record refuses to hold, and the
  restraint is the thesis performed; one Part V passage states it as chosen. Five of six
  reviewers asking for characterisation enters as citable evidence — a reader who felt the
  flatness has felt the design — never as a defect being repaired. The four channels: the
  author's first person (admitted, author-drafted, sessions edit mechanics only); the
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
  and the lesser-harm argument carries the defense. The section closes on the
  specification, per this bullet's own constraint: the operational layer book-2 must
  build — expiring, episode-scoped, one-way firewalled.

  **The objection docket is external and convergent** (`reviews/adoption_reviews.md`):
  four independent reviewers land on release/duration, delivery/obligor, audit teeth,
  degree/equity, and legitimacy/transition — plus two Part V objections from the
  engine-book review, the unenumerated-rights cage and proportionality-vs-structure.
  Part V answers these by name or it has not done its job. **One burden is Part V's alone
  and derivation cannot carry it**: *why this vocabulary* — the record's names are a
  stipulation, the book proves only what follows from them, and Part V either argues the
  choice or concedes it is one. Disclosure is done (chapter 1); justification is not.

- **The method part discloses the stress surface.** It sits inside the voice boundary —
  first person permitted, same supply protocol as the opening note and Part V. The suite's
  confidence register must not outrun its provenance: every probe, fixture and refusal was
  written by the author and AI sessions against a cast of dozens — no independent
  reimplementation, no external red-team, and the engine that blesses the book shares the
  book's author. The counterfactual fixtures and the upstream differential oracles narrow
  this and do not close it. One honest paragraph, beside the machinery it qualifies;
  anything stronger (soliciting an independent verification) is post-ship work and goes
  to the reach plan.

- **Write what the logic refused — in the method part, paired with chapter 7.** Re-verified
  2026-08-01: appending `all $x: prisoner($x) -> permits(Appeals, $x).` returns
  *"[Stratification Error] Unstratifiable negation: strongly-connected component containing
  'prisoner' -> 'permits' (negative)"*. A **universal right of appeal cannot be expressed**
  in this constitution. That is not a defeat; the machine refuses a thing the author wanted
  and can say exactly why. Ship the error message. **Not in Part V** — Part V is argument
  and evidence and stays jargon-free; an engine error message is formalism, which appears
  in exactly one place. **And the firewall it pairs with is chapter 7, not chapter 1** —
  chapter 1 carries a refusal of its own (Article 0a turning away the write of an
  unadmitted word) but that is assert-time closure, a different mechanism, and pairing
  with it would blur the symmetry. Chapter 7 is where the heresy law is refused by the
  stratifier, and chapter 7 now also carries the refused shield tightening, so the
  symmetry is already in print from the reader's side: the same stratifier refuses the author a universal right of appeal, an
  attacker a heresy law, and a designer a careful improvement. One mechanism, no special
  pleading, none of the outcomes chosen by whoever was writing that day.

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

- **Write the single book-2 pointer, at the very end — the end of the method part.**
  book-1 references book-2 exactly **once**, and the method part is the book's final
  element, so the pointer closes it. Not in the introduction, because a reader on page one
  has no idea whether they want the machinery, and a forward reference reads as an apology
  for the book they are holding. At the end it reads as an invitation. Keep the pointer
  plain: no tool names, no jargon, nothing a general reader must decode — it addresses
  whoever reached the last page, not only the readers who came for the formalism.

- **Reframe the research brief's India-first assumptions for a global audience** — the
  brief is `new-book-plans/final-research.md`. India material stays
  as **evidence** — Aadhaar/PDS is among the strongest evidence the book has — but it is one
  case among several, not the frame, and every reference needs enough context for a reader
  who has never heard of a ration card. Unblocked by drafting Part V; that is the only place
  the India evidence lands.

- **Parts I–IV second expansion wave — blocked on new derived material.** The first wave
  (2026-08-02) took the fourteen chapters from 25,027 to 28,585 words and stopped where
  the verified-untold material stopped; re-run `wc -w book-1/[0-9]*.md` before trusting
  either figure. The wave's stop-map: chapters
  1, 4, 11, 13 and 14 held no verified-untold material worth prose on 2026-08-02 —
  start the second wave elsewhere unless a ruling has touched them since. The
  remaining distance to the ~38,000 target is not writable from the
  current constitution: it arrives as Phase 1 decisions land (each ruling is new derived
  material with prose waiting for it — the clawback, expungement, kinship and delivery
  rulings all rewrite or extend chapters), or the author revises the target down.
  Break-even for the length invariant (derived > 17,800) is already cleared either way;
  Part V's 12,000 must be justified by content, not ratio. Do not pad.

- **Add `LICENSE-MIT` + `LICENSE-APACHE` — now unblocked.** The condition ("when the
  harness and fetchers are written") is met: `registry/check.py`,
  `registry/fetch/worldbank.py` and `new-book-plans/6-claim-table.py` exist, the first
  two already carrying `SPDX-License-Identifier: MIT OR Apache-2.0` headers. Fetch both
  canonical texts (per `LICENSING.md`), mirror nibli's layout, and add the SPDX header
  to `6-claim-table.py` and `verify.sh` in the same commit.

---

## Reach — ruled 2026-08-02; the gate is the chapter pass, and every chapter now qualifies

Serialize in spine order from a dedicated domain, with the assembled book — opening note,
Part V, method part — as the capstone release rather than the first contact. Building in
public performs the thesis: the repo history is the proof of the method, serialization
recruits the red-team the method part admits it lacks, and defect pins turn known flaws
into declared features. **A chapter serializes only when its whole-chapter pass is
complete** — all fourteen passes are complete, so the sequencing constraint is
discharged and serialization can begin whenever the site exists.

- **The site.** A dedicated domain — **registering it is the author's own task** — plain,
  built from the Markdown that already exists; chapters in spine order; the repo and the
  one-command suite run linked from the front page. Platforms syndicate *from* it: CC-BY
  means they will copy regardless, so the canonical home must name itself.
- **The launch essay. [AUTHOR-GATED]** A standalone distillation for someone who will
  never read the book, carrying the thesis and the honest second half in miniature. *The
  Furnished Prison* is the standing headline candidate. First-person territory: the voice
  protocol applies — the author drafts, sessions edit mechanics only.
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

## Data

The registry (`registry/claims.json`, CC0), its staleness gate and the first fetcher
exist and run inside `verify.sh`; see `registry/README.md`. What remains:

- **The rendering step — build it beside the first prose that cites a registry id.**
  Nothing in book-1's derived chapters may carry a number (the counted-claims gate), so
  value-injection waits for the empirical writing it serves: Part V's worked example and
  book-2. Do not build it speculatively. More fetchers (WHO GHO, OWID, FAOSTAT…) land the
  same way — as entries need them.

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

- **Use the democracy/happiness dataset — but for the opposite claim to the obvious
  one.** Fate decided by the EIU-vs-V-Dem ruling in Phase 1; the analysis below is the
  working material either way. `demo-happy.txt` + `democracy_vs_happiness_144.csv` (144
  countries, EIU 2025 merged with WHR 2025 life evaluations). Every headline number
  re-derived and reproducing exactly: raw r = 0.5975, ρ = 0.6231, R² = 0.357; partial
  r | log GDP = 0.195; r(GDP, happiness | democracy) = 0.623; and the regime table to
  the digit (Authoritarian 45/4.94/1.11, Hybrid 29/5.07/0.95, Flawed 44/5.80/0.94,
  Full 26/6.82/0.51).
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
  - **Make it Part V's worked example of the method.** Take "democracy makes people
    happier", test it, and report: survives raw, narrows sharply under income control,
    and the floor version fails outright. The book demonstrating that discipline on a
    claim it would have loved is worth more than the claim.
  - When the ruling lands, record `demo-happy.txt` in the registry as "prior analysis,
    independently re-derived", with the CSV's provenance pinned: WHR 2025 (2022–2024
    average) merged with EIU 2025, 144 countries matched from EIU's 166 and WHR's 147.

- **Publish the registry with the book, not just in the repo.** The formalism stays
  invisible, so what the reader verifies is the data — which only works if the registry is
  reachable from the page they are reading. Front matter names it and gives the URL, every
  figure in the prose resolves to a registry id, and the registry ships CC0. This is the
  thing that earns the trust and the honest substitute for showing the constitution.

---

## Legacy harvest — before `book.md` and `manifesto.md` are deleted

- **Harvest the nine historical cases.** New Harmony and the labour exchange, China's
  work-point villages, the kibbutzim, Nyerere's Ujamaa, Chile's Cybersyn, Auroville,
  Mondragon, WIR, Kerala's People's Plan — 2,264 words, researched, sourced, and
  mechanism-independent; their references are already registry entries. **Re-point them
  when porting:** book-1 does not tell the story of people who tried to build a better
  society — that is transition. Each case enters as evidence about a *failure mode of a
  functioning design*, never as an attempt narrative. Nowhere to put them until Part V
  exists.

- **Harvest the day-in-the-life technique, not the prose.** The three vignettes are at
  `book.md:981-984` (merit points), `1395-1398` (shelter, mobility, communication) and
  `2560-2563` (governance) — all three verified in place. All three are second-person and
  generic and two are MVS-framed, so nothing ports verbatim. What book-1 is missing is
  the **domestic** register: a household carried through food, care, housing and crisis,
  rather than a defendant carried through a procedure. **Ruled 2026-08-02: Part V gets
  one** — generic second person, never a cast name, per the texture ceiling. What remains
  here is the harvest itself: the technique, not the prose.

- **The last floor correction waits on Part V: privacy is not argued down anywhere.**
  book-1 has one incidental use of the word ("a private person", chapter 4), and the
  argument that encoding privacy as a defeasible right lands it at stratum 3 and destroys
  the single-deprivation theorem is Part V material.

- **Then delete both files, in one commit, with the harvest manifest in the body.** Not
  before. Still outstanding ahead of the deletion: the nine cases and the domestic
  vignette (both land with Part V), the privacy argument (Part V), and a decided home for
  the poem's full Tamil text and translations (decided with the epigraph ruling in
  Phase 1). Already discharged: the 55 references (in `registry/claims.json`) and the
  five bright lines (swept; result under Standing facts). The commit message is the
  record of what was taken and what was consciously dropped.

---

## book-2

book-2 has its own tracker: `book-2/TODO.md` — unordered until its chapters are
decided, seeded from the hold list that used to live here plus the adoption reviews
(`reviews/adoption_reviews.md`). The discipline is unchanged: **do not work book-2 items
while book-1 is active**; collect there, rule here.

---

## Standing facts and methods — not tasks, and not history

Landed work is not recorded here; that is what git is for. What survives is the small
set of things a command cannot teach you and a rename cannot re-derive.

```
./verify.sh                 # ~5 min (2026-08-02, 500+ pins): spine, evidence count,
                            #   jargon, counted-claims hard gate, claim-comment check,
                            #   registry check, absences, INVARIANT 1, the arity and
                            #   counting guards, control scope, engine build, the pin
                            #   suite with its cross-file :expect-pins reconciliation,
                            #   and the counterfactual fixtures in their three diff
                            #   classes — line deleted, line changed, line added
./verify.sh --quick         # ~2 s: everything except the pin suite AND the
                            #   counterfactuals — never sufficient after a constitution
                            #   edit
./verify.sh --only <file>   # one pin file, engine rebuilt, --allow-shell passed, and
                            #   the fixture's own KB chosen for counterfactual files;
                            #   partial by design — full run before committing
./verify.sh --table         # emit the claim-to-query table extracted from the pins
```

Prefer it to any check by hand. It exits non-zero on the first failure and names the
claim that stopped being true — including exit 3, the failure that is good news: a
pinned `:defect` stopped reproducing, and the script names it a REPAIR, not a
regression, because the response is to drop the marker and rewrite the prose that
called it a flaw, never to debug the harness. Use the **release** `nibli-pin`, never
`nibli-host`. The script builds the engine itself and prints the commit, because a
stale binary is invisible here — the pins check the constitution, not the engine, so an
out-of-date build returns the same green and the same runtime. **Gate on its exit
status, never on its output**: piping to `tail` swallows the exit, and `echo $?`
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
