# Counterfactual fixtures

Three copies of `../utopia-v2.nibli`, each with **exactly one line deleted**. They exist
because of a limitation the tracker records: derivation is monotone and probe facts load
*on top* of the knowledge base, so **no probe can test a restriction**. Every "if we
narrowed this rule, pin X would flip" claim in the book and the tracker is an argument
until it is run against a file where the line is actually gone.

Regenerate any of them with:

```
K=new-book-plans/utopia-v2.nibli
grep -v '^all \$anyone: prisoner(\$anyone) -> person(\$anyone)\.$' $K > no-person-line.nibli
grep -v '^public(Court)\.$'                                        $K > no-public-court.nibli
grep -v '^choose(Electorate, Boss)\.$'                             $K > no-choose-boss.nibli
```

`diff` each against the constitution: exactly one line, no other change. **Regenerate
after every constitution edit** — a stale fixture proves something about a file that no
longer exists, which is the failure mode these were built to answer.

| Fixture | Line removed | What it proves |
|---|---|---|
| `no-person-line.nibli` | `prisoner -> person` | Chapter 7's headline result. With the line, a heresy law is refused; without it the same law **loads**, and the whole population becomes imprisonable for belief. The clause that keeps prisoners human and the clause that keeps everyone's rights unconditional are the same clause. |
| `no-public-court.nibli` | `public(Court).` | The deletion axis of the fact-write trust base. One deleted line and `authority(Court)` goes FALSE, taking Sly's shield with it — `prisoner(Sly)` flips FALSE→TRUE. |
| `no-choose-boss.nibli` | `choose(Electorate, Boss).` | The same harm by the other route into standing. `authority(Boss)` goes FALSE and **Rebel — the file's own honest whistleblower — is jailed**, which is the whole of chapter 2's argument, undone by deleting one fact. |

Each has a paired `*.pins.nibli` asserting the flipped verdicts. Those pin files are
**expected to pass against their own fixture**, not against the constitution: they encode
what the world looks like once the line is gone. Run one with

```
nibli-pin --kb new-book-plans/counterfactual/no-person-line.nibli \
          new-book-plans/counterfactual/no-person-line.pins.nibli
```

`verify.sh` runs all three.
