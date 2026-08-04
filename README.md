# The Rights Nobody Has to Earn

*A design for a society worked out to the point where it catches its own failures.*

A worked design for a society in which a short list of basic things — safety, food,
shelter, care, learning, speech, belief, company — is owed to every person with no
qualifying condition. You do not have to work, contribute, belong, register or behave.

The design is written as a formal constitution, and the book's chapter order is computed
from it rather than chosen. Nothing goes into the book that the constitution does not
derive. That is also how the book finds its own defects, and it reports them: most of
what is owed never actually arrives, and the protection that does exist covers
imprisonment and stops there.

## What is here

| | |
|---|---|
| `book-1/` | the chapters, each with a sidecar of pinned queries against the constitution |
| `new-book-plans/constitution.nibli` | the constitution, in [nibli](https://github.com/dhilipsiva/nibli) KR |
| `new-book-plans/3-spine.md` | the computed chapter order — generated, not hand-written |
| `new-book-plans/assertion-surface-audit.md` | the generated inventory of derived relations and writable-premise risks |
| `new-book-plans/assertion-surface-contracts.json` | the reviewed authority, provenance, harm, challenge and risk contracts behind that audit |
| `new-book-plans/record-integrity-assurance-case.md` | the generated current/target argument for positive writes, effective absences, authorship, correction, witnessing, reconciliation, challenge and recovery |
| `new-book-plans/record-integrity-assurance-case.json` | the reviewed claims, evidence, premise coverage, defeaters, defaults and Book 2 assumptions behind that case |
| `new-book-plans/record-integrity-red-team.md` | the generated, executable T0 audit of release, adulthood, roster, carry, relief and forgiveness harms |
| `new-book-plans/record-integrity-red-team.json` | the reviewed route postures, snapshot deltas, expected results, limits and narrowness impacts behind that audit |
| `new-book-plans/counterfactual/` | copies of the constitution each missing one line, so "remove this and X breaks" is executed rather than argued |
| `verify.sh` | the one check |

```bash
./verify.sh          # everything, including pins, executable snapshots and counterfactuals
./verify.sh --quick  # schema/freshness checks; skips those three executable suites
python3 new-book-plans/9-record-integrity-red-team.py --check --execute
```

It exits non-zero on the first failure and names the claim that stopped being true.
That includes a new or reclassified rule head, a changed admission or ground-fact
snapshot, an unreviewed producer/consumer route in the assertion surface, or a
premise that has drifted out of the record-integrity case. The bounded red-team
reproduces selected current harms in constructed snapshots; it does not attribute
forgery, withholding or deletion. The assurance case's current verdict remains
deliberately **not established**: verification proves consequences from supplied
snapshots, not that a deployed record is authentic, complete, append-only or live,
and not that the checker authenticates its own source or toolchain.

A second book — how you would actually build this, organisationally and technically — is
planned and not started.

## Licence

Deliberately mixed: prose CC-BY-4.0, code MIT OR Apache-2.0, data CC0, and everything
committed before that decision irrevocably CC0 under the root `LICENSE`. See
[`LICENSING.md`](LICENSING.md) before adding files.
