#!/usr/bin/env python3
"""Regenerate the computed sections of 3-spine.md from the ENGINE's stratification.

The spine's chapter order is supposed to be *computed*, but the document has twice
gone stale because the numbers were transcribed by hand and the constitution moved
underneath them. This script owns the computed regions so that cannot happen again.

Usage:
    5-spine-gen.py constitution.nibli 3-spine.md            rewrite in place
    5-spine-gen.py constitution.nibli 3-spine.md --check    exit 1 if stale

Only text between `<!-- BEGIN GENERATED: name -->` and `<!-- END GENERATED: name -->`
is touched; hand-written prose is never rewritten.

[2026-07-31] STRATA NOW COME FROM THE ENGINE, via `nibli-pin --strata --kb`. This
script used to rebuild the dependency graph from the .nibli text with regexes — a
second implementation of nibli's stratifier, maintained by someone who could not see
it. It disagreed with the engine in three places, and two of the numbers it printed
were right only because two of its errors cancelled:

  - `entitled` read as base at stratum 0. The FLOOR branch synthesized the
    `P -> domain` edge but never registered the OUTER predicate as a head. The
    engine compiles the whole floor line to a rule whose head includes `entitled`,
    which puts it at stratum 2, derived.
  - `severe` read as stratum 0 with a "monotone cone". Its rules carry `~($a = $b)`,
    which the engine records as a NEGATIVE edge to the `equals` builtin — so it sits
    at stratum 1 and its cone is not negation-free. The old disequality guard
    dropped that conjunct entirely.
  - `derived_only` was a phantom node: the fact branch registered the declaration
    keyword as a predicate and never the name it quotes.

`derived_only` (phantom, +1) and `equals` (real, missed, -1) cancelled, so the
predicate total read 50 both ways and nobody noticed for weeks.

Two things are still read from the text, because neither is stratification and both
are unambiguous: which predicates are floor rights (the `event { }` lines), and the
rule count (arrows). Everything else — strata, base/derived, edges and their
polarity — is the engine's.
"""
import os
import re
import shutil
import subprocess
import sys
from collections import defaultdict

FLOOR = re.compile(r"^\s*([a-z_]+)\(\s*every\s+([a-z_]+)\s*,\s*event\s*\{\s*([a-z_]+)\s*\(")

# Compiler artifacts: the event anchor and the abstraction markers. Not authored,
# never shown. The engine lists them deliberately rather than filtering, so that a
# consumer's decision to drop them is visible here rather than hidden upstream.
def is_artifact(name):
    return name == "event" or name.startswith("__abs_")

# Present in the graph, not authored by anyone: `equals` exists because `~($a = $b)`
# is a real negative edge. It counts as a predicate and is NOT evidence.
BUILTINS = {"equals"}


def engine_strata(kb):
    """-> {pred: (stratum, is_base, [(dep, is_negative)])} from `nibli-pin --strata`."""
    pin = os.environ.get("NIBLI_PIN") or shutil.which("nibli-pin") or os.path.expanduser(
        "~/projects/dhilipsiva/nibli/target/release/nibli-pin")
    if not os.path.exists(pin):
        sys.exit(f"5-spine-gen: no nibli-pin at {pin} — build it release, or set NIBLI_PIN")
    r = subprocess.run([pin, "--strata", "--kb", kb], capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"5-spine-gen: nibli-pin --strata failed:\n{r.stdout}{r.stderr}")
    out = {}
    for line in r.stdout.splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        name, stratum, kind = parts[0], int(parts[1]), parts[2]
        edges = []
        if len(parts) > 3 and parts[3]:
            for e in parts[3].split(","):
                e = e.strip()
                if e:
                    edges.append((e[1:], e[0] == "-"))
        out[name] = (stratum, kind == "base", edges)
    if not out:
        sys.exit("5-spine-gen: nibli-pin --strata produced no rows")
    return out


def text_facts(kb):
    """The two things that are not stratification: floor identity and rule count."""
    floor, domain, rules = [], None, 0
    for raw in open(kb):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "->" in line:
            rules += 1
            continue
        m = FLOOR.match(line.rstrip("."))
        if m:
            domain = m.group(2)
            floor.append(m.group(3))
            # A floor line IS a rule: `entitled(every person, event { P() })`
            # compiles to one, which is why the engine reports `entitled` as
            # derived. Counting only arrows undercounts by exactly the floor.
            rules += 1
        elif re.search(r"\bevery\s+[a-z_]+", line):
            # Any other universally quantified line compiles to a rule too —
            # `owe(State, Provision, every person).` is one. Until 2026-08-02
            # only the floor's event{} shape was recognised, so a bare `every`
            # form was silently counted as neither rule nor fact and the
            # figure the method part prints came back one low per such line.
            rules += 1
    return floor, domain, rules


def render(kb):
    g = engine_strata(kb)
    floor, domain, rules = text_facts(kb)
    real = {p: v for p, v in g.items() if not is_artifact(p)}
    base = {p for p, (_, b, _) in real.items() if b}
    strata = {p: v[0] for p, v in real.items()}
    by_s = defaultdict(list)
    for p, sn in strata.items():
        by_s[sn].append(p)

    def cone_monotone(p, seen=None):
        """No negative edge anywhere in p's cone. Walks the engine's own polarity."""
        seen = seen or set()
        if p in seen:
            return True
        seen.add(p)
        for dep, neg in g.get(p, (0, True, []))[2]:
            if neg or not cone_monotone(dep, seen):
                return False
        return True

    ev = sorted(base - BUILTINS)
    out = []
    out.append("| measurement | predicates | derived | rules | strata |")
    out.append("|---|---|---|---|---|")
    out.append(f"| computed from the constitution | **{len(real)}** | "
               f"**{len(real) - len(base)}** | **{rules}** | "
               f"**{max(strata.values()) + 1}** |")
    out.append("")
    out.append(f"The floor is **{len(floor)}** rights — `" + "`, `".join(floor) +
               f"` — each derived from `{domain}`, which is why they sit at stratum "
               f"{strata[floor[0]]} rather than 0. That is the firewall: being "
               f"inside the `{domain}` cone is what makes a punishing rule a "
               f"negative cycle.")
    out.append("")
    out.append("| Stratum | Predicates |")
    out.append("|---|---|")
    for sn in sorted(by_s):
        marked = []
        for p in sorted(by_s[sn]):
            if p in floor:
                marked.append(f"**{p}**")
            elif p not in base and cone_monotone(p):
                marked.append(f"`{p}` *(monotone cone)*")
            else:
                marked.append(f"`{p}`")
        out.append(f"| **{sn}** | " + ", ".join(marked) + " |")
    out.append("")
    out.append(f"Evidence predicates ({len(ev)}), the complete list of what the "
               f"world may report: `" + "`, `".join(ev) + "`.")
    out.append("")
    out.append("Strata, base/derived and edge polarity are the engine's, via "
               "`nibli-pin --strata`. Two filters are this document's choice and are "
               "named so they are visible: the compiler artifacts `event` and "
               "`__abs_<hash>` are dropped, and `equals` — which exists because "
               "`~($a = $b)` is a real negative edge — counts as a predicate but is "
               "not evidence, since nobody writes it.")
    return "\n".join(out)


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    kb, doc = sys.argv[1], sys.argv[2]
    check = "--check" in sys.argv
    body = render(kb)
    src = open(doc).read()
    pat = re.compile(
        r"(<!-- BEGIN GENERATED: stratification -->)(.*?)(<!-- END GENERATED: stratification -->)",
        re.S)
    if not pat.search(src):
        sys.exit(f"{doc}: no generated region — add the BEGIN/END markers first")
    new = pat.sub(lambda m: m.group(1) + "\n" + body + "\n" + m.group(3), src)
    if check:
        if new != src:
            print(f"{doc} is STALE — rerun without --check")
            sys.exit(1)
        print(f"{doc} is current")
        return
    if new != src:
        open(doc, "w").write(new)
        print(f"{doc}: regenerated")
    else:
        print(f"{doc}: already current")


if __name__ == "__main__":
    main()
