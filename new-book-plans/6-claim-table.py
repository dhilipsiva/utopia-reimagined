#!/usr/bin/env python3
"""Extract the claim-to-query table from the pin files.

The table cannot be generated from the constitution — the constitution cannot
know which sentence of chapter 11 a query backs — so it is extracted from the
pin files, where every load-bearing sentence already sits as a comment beside
the query that holds it.

THE FORM, settled 2026-08-02 by measurement rather than backfill: a query's
claim is the NEAREST PRECEDING COMMENT BLOCK in its file — contiguous `#`
lines, skipping `# =>` verdict lines and `:` directives, walking past facts
and other queries. The strict comment-directly-above form would have demanded
~295 duplicative comments (many exhibits are one claim backed by several
queries); block inheritance covered all queries with zero edits when measured,
and zero of them inherited file-header or taxonomy boilerplate. That
measurement is now the invariant --check guards.

Usage:
  6-claim-table.py --check     exit 1 naming any query with no reachable claim
  6-claim-table.py             emit the markdown table to stdout
"""
import glob
import pathlib
import sys

FILES = sorted(glob.glob('book-1/*.pins.nibli')) + [
    'new-book-plans/rights-floor.pins.nibli'
]
BOILER = ('WHAT FALSE MEANS HERE', 'fidelity pins', 'KIND: CONTENT pin')


def claim_for(lines, qi):
    j = qi - 1
    while j >= 0:
        ln = lines[j].strip()
        if ln.startswith('# =>'):
            j -= 1
            continue
        if ln.startswith('#'):
            blk = []
            while (j >= 0 and lines[j].strip().startswith('#')
                   and not lines[j].strip().startswith('# =>')):
                blk.insert(0, lines[j].strip().lstrip('#').strip())
                j -= 1
            return ' '.join(b for b in blk if b)
        j -= 1
    return None


def rows():
    for f in FILES:
        lines = pathlib.Path(f).read_text(encoding='utf-8').splitlines()
        for i, ln in enumerate(lines):
            if not ln.startswith('? '):
                continue
            verdict = ''
            if i + 1 < len(lines) and lines[i + 1].startswith('# =>'):
                verdict = lines[i + 1][4:].strip()
            yield f, i + 1, ln[2:].rstrip('.').rstrip(), verdict, claim_for(lines, i)


def main():
    check = '--check' in sys.argv
    bad = []
    n = 0
    out = []
    last_file = last_claim = None
    for f, lineno, q, verdict, claim in rows():
        n += 1
        if not claim or any(b in claim for b in BOILER):
            bad.append(f'{f}:{lineno}: ? {q}.')
            continue
        if not check:
            if f != last_file:
                out.append(f'\n## {f}\n')
                out.append('| claim (from the pin comment) | query | verdict |')
                out.append('|---|---|---|')
                last_file, last_claim = f, None
            shown = '〃' if claim == last_claim else claim.replace('|', '\\|')
            out.append(f'| {shown} | `{q}` | {verdict} |')
            last_claim = claim
    if bad:
        print('queries with no reachable claim comment '
              '(write the claim as a # comment block above):', file=sys.stderr)
        for b in bad:
            print('  ' + b, file=sys.stderr)
        sys.exit(1)
    if check:
        print(f'{n} queries, every one reachable from a claim comment')
    else:
        print('# Claim-to-query table')
        print('\nExtracted from the pin files by 6-claim-table.py; '
              'a 〃 claim continues the row above.')
        print('\n'.join(out))


if __name__ == '__main__':
    main()
