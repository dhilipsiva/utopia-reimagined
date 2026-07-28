#!/usr/bin/env python3
"""Regenerate the computed sections of 3-spine.md directly from the constitution.

The spine's chapter order is supposed to be *computed*, but the document has twice
gone stale because the numbers were transcribed by hand and the constitution moved
underneath them. This script owns the computed regions so that cannot happen again.

Usage:
    5-spine-gen.py utopia-v2.nibli 3-spine.md            rewrite in place
    5-spine-gen.py utopia-v2.nibli 3-spine.md --check    exit 1 if stale

Only text between `<!-- BEGIN GENERATED: name -->` and `<!-- END GENERATED: name -->`
is touched; hand-written prose is never rewritten.

Unlike 4-strata.py this sees the floor. `entitled(every person, event { P() }).`
compiles to a rule with `person` in the body, so it contributes a `P -> person`
edge — the fact 4-strata.py structurally cannot observe, and the reason it reported
the floor at stratum 0 when the engine puts it at 2.
"""
import re
import sys
from collections import defaultdict

LIT = re.compile(r"(~?)\s*([a-z_][A-Za-z0-9_]*)\s*\(")
FLOOR = re.compile(r"^\s*([a-z_]+)\(\s*every\s+([a-z_]+)\s*,\s*event\s*\{\s*([a-z_]+)\s*\(")
STRUCTURAL = {"derived_only"}  # declarations, not evidence


def strip_quant(s):
    while True:
        m = re.match(r"^all\s+\$[A-Za-z0-9_]+\s*:\s*", s)
        if not m:
            return s
        s = s[m.end():]


def parse(path):
    """-> (rules, all_preds, head_preds, floor_preds, floor_domain)"""
    rules, all_preds, head_preds, floor_preds = [], set(), set(), []
    floor_domain = None
    for raw in open(path):
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        line = line.rstrip(".")

        # A floor line is a universal whose event body becomes a rule head.
        fm = FLOOR.match(line)
        if fm and "->" not in line:
            outer, domain, inner = fm.groups()
            floor_domain = domain
            floor_preds.append(inner)
            all_preds.update({outer, domain, inner})
            head_preds.add(inner)
            rules.append((inner, [(False, domain)]))
            continue

        if "->" in line:
            body_s, head_s = line.split("->", 1)
            hm = LIT.search(head_s)
            if not hm:
                continue
            head = hm.group(2)
            head_preds.add(head)
            all_preds.add(head)
            body = []
            for part in strip_quant(body_s.strip()).split("&"):
                part = part.strip()
                if "=" in part and not LIT.search(part):
                    continue
                m = LIT.search(part)
                if not m:
                    continue
                body.append((part.lstrip().startswith("~"), m.group(2)))
                all_preds.add(m.group(2))
            rules.append((head, body))
        else:
            m = LIT.search(strip_quant(line))
            if m:
                all_preds.add(m.group(2))
    return rules, all_preds, head_preds, floor_preds, floor_domain


def stratify(rules, all_preds):
    stratum = {p: 0 for p in all_preds}
    for _ in range(len(all_preds) + 2):
        changed = False
        for head, body in rules:
            for neg, p in body:
                want = stratum[p] + 1 if neg else stratum[p]
                if stratum[head] < want:
                    stratum[head] = want
                    changed = True
        if not changed:
            break
    else:
        sys.exit("UNSTRATIFIABLE")
    return stratum


def cone_monotone(deps, p, seen=None):
    seen = seen if seen is not None else set()
    if p in seen:
        return True
    seen.add(p)
    for neg, q in deps.get(p, []):
        if neg or not cone_monotone(deps, q, seen):
            return False
    return True


def render(kb):
    rules, all_preds, head_preds, floor, domain = parse(kb)
    stratum = stratify(rules, all_preds)
    deps = defaultdict(list)
    for head, body in rules:
        deps[head].extend(body)
    base = {p for p in all_preds if p not in head_preds}
    by_s = defaultdict(list)
    for p in all_preds:
        by_s[stratum[p]].append(p)

    ev = sorted(base - STRUCTURAL - {"entitled"})
    out = []
    out.append(f"| measurement | predicates | derived | rules | strata |")
    out.append(f"|---|---|---|---|---|")
    out.append(f"| computed from the constitution | **{len(all_preds)}** | "
               f"**{len(head_preds)}** | **{len(rules)}** | "
               f"**{max(stratum.values()) + 1}** |")
    out.append("")
    out.append(f"The floor is **{len(floor)}** rights — `" + "`, `".join(floor) +
               f"` — each derived from `{domain}`, which is why they sit at stratum "
               f"{stratum[floor[0]]} rather than 0. That is the firewall: being "
               f"inside the `{domain}` cone is what makes a punishing rule a "
               f"negative cycle.")
    out.append("")
    out.append("| Stratum | Predicates |")
    out.append("|---|---|")
    for s in sorted(by_s):
        names = sorted(by_s[s] - set() if isinstance(by_s[s], set) else by_s[s])
        marked = []
        for p in names:
            if p in floor:
                marked.append(f"**{p}**")
            elif p not in base and cone_monotone(deps, p):
                marked.append(f"`{p}` *(monotone cone)*")
            else:
                marked.append(f"`{p}`")
        out.append(f"| **{s}** | " + ", ".join(marked) + " |")
    out.append("")
    out.append(f"Evidence predicates ({len(ev)}), the complete list of what the "
               f"world may report: `" + "`, `".join(ev) + "`.")
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
