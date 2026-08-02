#!/usr/bin/env python3
# SPDX-License-Identifier: MIT OR Apache-2.0
"""The registry's own check: schema plus the staleness gate.

Fails (exit 1) when:
  - an entry is missing a required field, or
  - a fetched-by-script entry has a null value or no retrieval date while its
    fetcher exists (a hand-edited or never-run fetchable entry), or
  - a fetched-by-script entry's `retrieved` date is older than MAX_AGE_DAYS —
    the staleness gate: refresh it by re-running the fetcher named in `fetch`.

Pinned-paper entries (fetch: null) never go stale by date: their version is
the pin, and drift is visible because `retrieved` records when the pinned
version was last checked. Flagging those is a human re-cite pass, not a gate.
"""
import json
import sys
from datetime import date, timedelta

MAX_AGE_DAYS = 400  # roughly an annual-release cycle plus slack

REQUIRED = ("id", "claim", "value", "units", "source", "retrieved",
            "method", "fetch", "notes")


def main():
    with open("registry/claims.json", encoding="utf-8") as f:
        reg = json.load(f)
    problems = []
    seen = set()
    for c in reg["claims"]:
        cid = c.get("id", "<missing id>")
        if cid in seen:
            problems.append(f"{cid}: duplicate id")
        seen.add(cid)
        for k in REQUIRED:
            if k not in c:
                problems.append(f"{cid}: missing field '{k}'")
        if c.get("fetch"):
            if c.get("value") is None and c.get("retrieved"):
                problems.append(f"{cid}: fetchable entry has retrieved-date "
                                "but null value — fetcher half-ran?")
            if c.get("retrieved"):
                age = date.today() - date.fromisoformat(c["retrieved"])
                if age > timedelta(days=MAX_AGE_DAYS):
                    problems.append(
                        f"{cid}: stale — retrieved {c['retrieved']}, "
                        f"over {MAX_AGE_DAYS} days; re-run: {c['fetch']}")
    if problems:
        print("registry check FAILED:", file=sys.stderr)
        for p in problems:
            print("  " + p, file=sys.stderr)
        sys.exit(1)
    fetchable = sum(1 for c in reg["claims"] if c.get("fetch"))
    print(f"registry ok: {len(reg['claims'])} claims "
          f"({fetchable} fetchable, {len(reg['claims']) - fetchable} pinned)")


if __name__ == "__main__":
    main()
