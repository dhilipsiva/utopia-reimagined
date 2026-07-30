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
| `new-book-plans/counterfactual/` | copies of the constitution each missing one line, so "remove this and X breaks" is executed rather than argued |
| `verify.sh` | the one check |

```bash
./verify.sh          # everything, including the pin suite
./verify.sh --quick  # everything else, about two seconds
```

It exits non-zero on the first failure and names the claim that stopped being true.

A second book — how you would actually build this, organisationally and technically — is
planned and not started.

## Licence

Deliberately mixed: prose CC-BY-4.0, code MIT OR Apache-2.0, data CC0, and everything
committed before that decision irrevocably CC0 under the root `LICENSE`. See
[`LICENSING.md`](LICENSING.md) before adding files.
