# Counterfactual fixtures

Three copies of `../constitution.nibli`, each with **exactly one line deleted**. They exist
because of a limitation the tracker records: derivation is monotone and probe facts load
*on top* of the knowledge base, so **no probe can test a restriction**. Every "if we
narrowed this rule, pin X would flip" claim in the book and the tracker is an argument
until it is run against a file where the line is actually gone.

Regenerate any of them with:

```
K=new-book-plans/constitution.nibli
grep -vFx 'all $anyone: prisoner($anyone) -> person($anyone).' $K > no-person-line.nibli
grep -vFx 'public(Court).'                                     $K > no-public-court.nibli
grep -vFx 'choose(Electorate, Boss).'                          $K > no-choose-boss.nibli
```

**Use `-vFx`, and do not "fix" it back to a regex.** The version of this command that
stood here until v0.5 was `grep -v '^all \$anyone: …'`, and inside single quotes `\$` is a
literal backslash-dollar, so it matched nothing and wrote out a byte-identical copy of the
constitution. Anyone following the documented procedure destroyed the fixture, and the
three pins still passed, because a fixture that is a copy of the real file answers every
question the real file answers. `-F` (fixed string) and `-x` (whole line) cannot be
misread that way.

`diff` each against the constitution: exactly one line removed, nothing added. **Regenerate
after every constitution edit** — a stale fixture proves something about a file that no
longer exists, which is the failure mode these were built to answer. `verify.sh` now
enforces the one-line property before it runs the pins; it did not until v0.5, because the
guard assigned its result to a variable it never read.

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
