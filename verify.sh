#!/usr/bin/env bash
# verify.sh — the one check for book-1. First failure wins.
#
# This project's recurring failure mode is a hand-maintained number going stale:
# the spine went stale twice, the evidence count moved from 21 to 22 undetected,
# a pin-file NOTE drifted from its own file, and a proportion cap was computed
# against a spine that did not exist. Every check below exists because one of
# those actually happened.
#
#   ./verify.sh          full run, includes the pin suite (~15 min)
#   ./verify.sh --quick  everything except the pin suite (~2 s)
#
# NEVER use nibli-host: its wasm predates the derived_only and entitled corpus
# entries, so it silently drops the rights floor and all nine gate closures and
# then reports a clean run over a constitution it is not reading.

set -uo pipefail
cd "$(dirname "$0")"

PIN="${NIBLI_PIN:-$HOME/projects/dhilipsiva/nibli/target/release/nibli-pin}"
KB=new-book-plans/utopia-v2.nibli
SPINE=new-book-plans/3-spine.md
CF=new-book-plans/counterfactual
QUICK=0
[ "${1:-}" = "--quick" ] && QUICK=1

pass() { printf '  \033[32mok\033[0m   %s\n' "$1"; }
fail() { printf '  \033[31mFAIL\033[0m %s\n' "$1"; [ -n "${2:-}" ] && printf '       %s\n' "$2"; exit 1; }
step() { printf '\n\033[1m%s\033[0m\n' "$1"; }

# ── 1. the spine is regenerated from the constitution ────────────────────────
step "spine"
out=$(python3 new-book-plans/5-spine-gen.py "$KB" "$SPINE" --check 2>&1) \
  && pass "3-spine.md is current" \
  || fail "3-spine.md is stale" "$out — rerun 5-spine-gen.py without --check"

# ── 2. chapter 1's headline number ───────────────────────────────────────────
# Only the generated block is machine-owned. A new PREDICATE name (not a new
# ground fact) pushes this to 22 and falsifies chapter 1 in nine places.
n=$(grep -o 'Evidence predicates ([0-9]*)' "$SPINE" | grep -o '[0-9]*')
[ "$n" = "21" ] && pass "evidence vocabulary is 21" \
  || fail "evidence vocabulary is $n, not 21" "chapter 1 says twenty-one in nine places"

# ── 3. no formalism leaks into Parts I-V ─────────────────────────────────────
step "prose"
# The pattern is wider than the tracker's original. Negative-controlled: the old
# one missed "stratifier" — the likeliest leak of all, since it is the word the
# tracker itself uses constantly. `strat` alone is too greedy (it matches
# "demonstrate"), hence the three explicit stems.
JARGON="nibli|predicat|stratum|strata|stratif|compil|assert|rule head|quantif|derivation|knowledge base|first-order|negation|conjunct"
if hits=$(grep -rniE "$JARGON" book-1/*.md); then
  fail "jargon in a derived chapter" "$hits"
else
  pass "jargon sweep clean across $(ls book-1/*.md | wc -l) chapters"
fi

# ── 4. the absence claims ────────────────────────────────────────────────────
# Each is a load-bearing sentence that no query can hold. Test the rule BODIES:
# a bare grep also matches the predicate's own rule head, which is a check that
# can never fail. The positive control proves the command still works.
step "absences (nothing reads these)"
body() { awk -F'->' -v p="$1" '/^[^#]/ && /->/ && $1 ~ p {print NR": "$0}' "$KB"; }
ctl=$(body 'false' | wc -l)
[ "$ctl" -ge 1 ] || fail "absence check is broken" "positive control /false/ returned 0 lines; it should return 5"
pass "positive control: /false/ appears in $ctl rule bodies"
for p in owe become travel err lose; do
  n=$(body "$p" | wc -l)
  [ "$n" = "0" ] && pass "nothing reads $p" \
    || fail "$p is now read by a rule" "$(body "$p") — the prose saying nothing follows from it is now false"
done
# recognition carries no quantity anywhere
if grep -vE '^\s*#' "$KB" | grep -qE '[0-9]'; then
  fail "a digit appeared in an enacted line" "chapter 10 turns on there being no arithmetic"
else
  pass "no arithmetic in the constitution"
fi

# ── 5. the pin suites ────────────────────────────────────────────────────────
if [ "$QUICK" = "1" ]; then
  printf '\n\033[33mskipped\033[0m the pin suite (--quick)\n'
  exit 0
fi
step "pins (~15 min)"
[ -x "$PIN" ] || fail "no nibli-pin at $PIN" "build it release, or set NIBLI_PIN"

declared=$(grep -h ':expect-pins' new-book-plans/rights-floor.pins.nibli book-1/*.pins.nibli | awk '{s+=$2} END {print s}')
out=$("$PIN" --kb "$KB" new-book-plans/rights-floor.pins.nibli book-1/*.pins.nibli 2>&1)
echo "$out" | grep -E 'pins,|✗' | sed 's/^/  /'
echo "$out" | grep -q 'FINDING\|HARNESS ERROR' && fail "a pinned property regressed"
ran=$(echo "$out" | sed -n 's/.*PASS — \([0-9]*\) pins.*/\1/p')
[ -n "$ran" ] || fail "the suite did not report a PASS line"
[ "$ran" = "$declared" ] && pass "$ran pins, 0 findings — matches the sum of :expect-pins" \
  || fail "ran $ran pins but the files declare $declared" "a file was added or dropped from the run"

# ── 6. the counterfactuals ───────────────────────────────────────────────────
# Derivation is monotone and probe facts load on top, so no probe can test a
# restriction. These are the only way a "remove this line and X breaks" claim in
# the book is executed rather than argued. Regenerate after any KB edit.
step "counterfactuals"
for f in no-person-line no-public-court no-choose-boss; do
  d=$(diff <(grep -c '' "$KB") <(grep -c '' "$CF/$f.nibli") >/dev/null; echo $?)
  out=$("$PIN" --kb "$CF/$f.nibli" "$CF/$f.pins.nibli" 2>&1)
  echo "$out" | grep -q 'PASS' && pass "$f" \
    || fail "$f" "$(echo "$out" | tail -3) — is the fixture stale? regenerate it from $KB"
done

printf '\n\033[32mall checks passed\033[0m\n'
