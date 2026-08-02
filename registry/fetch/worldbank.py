#!/usr/bin/env python3
# SPDX-License-Identifier: MIT OR Apache-2.0
"""Fetch a World Bank indicator's most recent non-null value.

Usage:
  worldbank.py <INDICATOR> <COUNTRY> [--write <claims.json> --id <entry-id>]

Without --write, prints the value, year and retrieval date. With --write,
updates the registry entry in place: sets `value`, stamps `retrieved`, and
appends the observation year to `notes`-adjacent field `observation_year`.

This is the exemplar fetcher for the registry's fetched-by-script class: the
script is the provenance, the registry pins what it wrote and when, and the
staleness gate (registry/check.py) flags fetchable entries whose `retrieved`
date has fallen behind.
"""
import json
import sys
import urllib.request
from datetime import date


def fetch(indicator, country):
    url = (f"https://api.worldbank.org/v2/country/{country}/indicator/"
           f"{indicator}?format=json&per_page=100")
    with urllib.request.urlopen(url, timeout=60) as r:
        meta, rows = json.load(r)
    for row in rows:  # newest first
        if row.get("value") is not None:
            return float(row["value"]), int(row["date"])
    raise SystemExit(f"no non-null value for {indicator}/{country}")


def main():
    args = sys.argv[1:]
    if len(args) < 2:
        raise SystemExit(__doc__)
    indicator, country = args[0], args[1]
    value, year = fetch(indicator, country)
    today = date.today().isoformat()
    if "--write" in args:
        path = args[args.index("--write") + 1]
        entry_id = args[args.index("--id") + 1]
        with open(path, encoding="utf-8") as f:
            reg = json.load(f)
        entry = next(c for c in reg["claims"] if c["id"] == entry_id)
        entry["value"] = value
        entry["observation_year"] = year
        entry["retrieved"] = today
        with open(path, "w", encoding="utf-8") as f:
            json.dump(reg, f, indent=2, ensure_ascii=False)
            f.write("\n")
        print(f"{entry_id}: {value} ({year}), retrieved {today} — written")
    else:
        print(f"{indicator}/{country}: {value} (observation year {year}, "
              f"retrieved {today})")


if __name__ == "__main__":
    main()
