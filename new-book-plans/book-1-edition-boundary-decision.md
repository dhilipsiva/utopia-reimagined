<!-- SPDX-License-Identifier: CC-BY-4.0 -->

# Book 1 Edition-Boundary Decision

> **Status: draft for author ratification.** This is a publication decision,
> not a constitutional change. It neither replaces the 2026-08-02 reach ruling
> nor authorises changing a public edition in place.

## 1. Decision required

The 2026-08-02 reach ruling remains sound for the **pass-complete,
pre-expansion verified kernel**: its chapters passed in spine order, and public
serialization can recruit the red-team the book needs. The 2026-08-03 mandate,
however, creates a different artifact: a new constitution, regenerated spine,
new pins and counterfactuals, possible reordering, and revised prose.

A completed pass is therefore version-specific. It remains evidence for an
immutable baseline; it is not a pass for a changed chapter or for a new spine.
The unresolved question is whether the expansion replaces, follows, or delays
the public baseline.

## 2. Non-negotiable publication contract

Every public edition or preview must identify:

1. **Edition and source:** a stable tag or commit, canonical source location,
   and an immutable assembled artifact.
2. **Verification state:** whether the full suite passed against that exact
   source, plus its date and known external-assurance limits.
3. **Scope:** whether it is the verified narrow kernel, an expanded draft, or a
   later comprehensive interface. No baseline may be called comprehensive under
   the new mandate.
4. **Revision path:** stable citation/URL policy, public changelog, correction
   route, and an explicit rule against silent page replacement.
5. **Print policy:** a print edition is immutable and identifies its edition and
   source. A mutable web page is not a print edition by another name.
6. **Deferred-work pointer:** before v1 freezes, audit any reference to an
   unpublished later book. It must state a scope boundary, not promise publication
   order. If an already frozen edition contains such a promise and the order
   changes, preserve its text and publish a dated, immutable status note beside it.
   An expanded Book 1 v2 is not the separate operational book it once pointed to.

## 3. Available choices

| Choice | Benefit | Cost / condition |
| --- | --- | --- |
| **A. Freeze and release the verified kernel as v1; build the expansion as v2.** | Preserves a reproducible object for readers to test and keeps the red-team benefit of building in public. | Readers need clear scope labelling; v2 must earn fresh passes, spine order, and public claims. |
| **B. Hold all publication until v2 is complete.** | One public edition and no split attention. | Gives up the near-term red-team and reach rationale for an open-ended expansion. |
| **C. Run a living public v2 serial.** | Invites early review of the expanded design. | Permitted only as immutable, versioned previews alongside a stable baseline; otherwise readers cannot cite or test what they read. |

## 4. Recommended ruling

**Choose A, with C available as a later, explicitly labelled v2-preview mode.**
Release the current book as an immutable **pre-expansion verified kernel**
edition. Start the constitutional expansion as v2; it must not silently revise
or overwrite v1 pages. If the author chooses public v2 serialization, each post
must identify its v2 draft status, source version, affected claims, and revision
history, and must preserve accessible prior versions.

This preserves both truths: the current book is a real, verified object worth
public testing, and it is not yet the comprehensive constitution the new mandate
requires.

Before v1 freezes, resolve its final-page Book 2 pointer under the deferred-work
contract. If it is already frozen when publication order changes, add a dated
status note rather than silently rewriting the source.

## 5. Fresh-pass rule for v2

No expansion rule family may inherit v1 publication clearance. Before an affected
v2 chapter is serialized, the change needs its own constitution/spine/pin and
counterfactual validation, narrowness-impact disposition, prose revision, and
whole-chapter reader pass. The resulting v2 serialization order comes from its
regenerated spine, not the v1 order.

The existing v1 edition remains useful evidence even where v2 later retires a
claim. A revision must name the difference; it may not make the older source
disappear.

## 6. Ratification choices

- [ ] **A. Release immutable v1; develop v2 separately (recommended).** Decide
  whether v2 previews are permitted after their fresh-pass rule is met.
- [ ] **B. Hold public release for v2.** State what event ends the hold and how
  red-team review is otherwise obtained.
- [ ] **C. Begin versioned public v2 previews now.** Supply the non-negotiable
  publication contract before the first post; v1 remains separately accessible.

When the author chooses, record the qualifying ruling in `CLAUDE.md`; `TODO.md`
owns the open decision until then.
