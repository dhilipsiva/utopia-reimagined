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
KB=new-book-plans/constitution.nibli
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
# ground fact) moves this and falsifies the nine prose places that name it.
n=$(grep -o 'Evidence predicates ([0-9]*)' "$SPINE" | grep -o '[0-9]*')
[ "$n" = "23" ] && pass "evidence vocabulary is 23" \
  || fail "evidence vocabulary is $n, not 23" "chapters 1, 3 and 5 describe the list; re-read them against it"

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

# ── 3b. counted claims in the prose — a RATCHET, not a gate ──────────────────
# Every counting claim in this book that has been checked was WRONG, not merely
# stale: "every convicted person" named four of seven; "one person verifiably has
# shelter" was four; "everything else on both lists is identical" differed in four
# places; "the four cases exhaust the combinations" covered seven of eight. The
# design also keeps moving — the evidence list went 21 -> 22 in one commit, the
# floor may stop being eight, and more than one thing may become takeable — so a
# number in the prose is a maintenance liability with a bad accuracy record.
#
# The rule is NOT "delete numbers", which only makes the prose vaguer. It is
# **state the rule that produces the count**: "shelter derives for every confined
# person and for nobody else" beats "four people have shelter" — stable under cast
# changes, more informative, and it is what the book is actually about.
#
# This is a ratchet because ~38 sites exist today and they are fixed chapter by
# chapter as each is revised. It fails only if the count GOES UP. Lower BASELINE
# in the same commit that removes sites; when it reaches 0, make this a hard gate.
COUNTED='\b(eleven|twelve|thirteen|fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|hundred)([- ][a-z]+)?\b|\beight\b|\bexactly one\b|\bone thing\b|\bsingle deprivation\b'
# Rhetorical durations are not claims about this design; they never go stale.
COUNTED_OK='(thirty|forty|fifty|hundred) (year|second|minute|mile)'
BASELINE=25
n=$(grep -rniE "$COUNTED" book-1/*.md | grep -viE "$COUNTED_OK" | wc -l)
if [ "$n" -gt "$BASELINE" ]; then
  fail "counted claims in the prose rose to $n (baseline $BASELINE)" \
"$(grep -rniE "$COUNTED" book-1/*.md | grep -viE "$COUNTED_OK" | tail -5)
       State the rule that produces the count, do not count the instances."
elif [ "$n" -lt "$BASELINE" ]; then
  fail "counted claims fell to $n — lower BASELINE to $n in verify.sh, same commit" \
       "the ratchet only holds if it is tightened when sites are removed"
else
  pass "counted claims held at $BASELINE (ratchet; lower it as chapters are revised)"
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
# `reward` is here by DECISION, not by observation: recognition feeds nothing, so
# it can never become an input to a ranking of persons. See the counting guard
# below — the two together are what "recognition is never ranked" reduces to.
#
# `building` is a decision too, and a different kind from the rest of this list.
# The others record that nothing happens to follow from a fact. This one is
# chapter 13's central admission made checkable: the design fixes WHERE a
# convicted person is and says nothing about what happens there, and the proof
# of that is that the placement is read by nothing. Note what it cuts against —
# if conditions vocabulary is ever admitted, a rule granting facility-specific
# protections would legitimately read `building` and this guard would fail. That
# is intended. Removing it should be a deliberate act with the chapter rewritten
# in the same commit, not a quiet consequence of some other edit.
# `err` LEFT this list in v0.8 and `obliged` took its place. The audit now feeds
# an obligation (Article 8b), so "nothing reads err" is false by design — chapter
# 14 says so. What still has to hold is that the chain ENDS: nothing reads the
# duty either. If `obliged` ever gains a reader the design has grown a third
# link, and chapter 14's closing argument has to be rewritten around it rather
# than quietly outgrown. That is what this line is guarding.
for p in owe become travel obliged lose reward building; do
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

# ── 4c. INVARIANT 1: a floor right may be noticed, never acted on ────────────
# The constitution states this at :103 and until v0.8 nothing enforced it — and
# the version nobody enforced was WRONG. It said a floor predicate must appear in
# no rule body at all, and Article 6's isolation marker has broken that since
# v0.1: `prisoner($p) & ~meets($p) -> err($p, Isolation)` reads `meets`. The
# blanket ban also forbade the one thing that marker does, which is notice that a
# floor right did not arrive — the only delivery check in the file.
#
# So the rule is narrower and this enforces the narrow form: a floor right may be
# read ONLY into `err`. Noticing is allowed; acting on it is not.
#
# The stratifier does NOT make this check for you. It refuses `~eats -> prisoner`
# because that is a negative cycle through the person cone, and it accepts
# `~eats -> reward` and `~eats -> building` quite happily. Those are the rules
# this guard exists for, and nothing else in the suite would see them.
step "the floor is noticed, never acted on (INVARIANT 1)"
for p in secure eats dwell healthy learn expresses believe meets; do
  bad=$(awk -F'->' -v p="(^|[^a-z])$p\\\\(" '/^[^#]/ && /->/ && $1 ~ p && $2 !~ /err\(/ {print NR": "$0}' "$KB")
  [ -z "$bad" ] || fail "$p is read into something other than err — INVARIANT 1" \
    "$bad
       A floor right may be noticed (head err) and never acted on. See constitution :103."
done
noticed=$(awk -F'->' '/^[^#]/ && /->/ && $2 ~ /err\(/ && $1 ~ /(^|[^a-z])(secure|eats|dwell|healthy|learn|expresses|believe|meets)\(/ {c++} END{print c+0}' "$KB")
[ "$noticed" -ge 1 ] || fail "the noticing check is vacuous" \
  "no floor right is read into err at all, so the guard above proves nothing — \
Article 6's isolation marker should be one"
pass "floor rights reach only err ($noticed such rule, none reaching a consequence)"

# ── 4b. no counted degree on the reward side ─────────────────────────────────
# The digit ban above stops a quantity being WRITTEN. This stops one being
# COUNTED, which is the cheaper route and the one chapter 10 points at directly:
# degree needs no arithmetic here, only the same relation twice with the two
# objects held apart. Severity is built exactly that way (:452-453), and the
# cast already supplies the reward-side mirror — Cira has two teachers — so
# "count what a person was taught" is one rule away and always has been.
#
# Chapter 10 now says that will not be built, so this is where that stops being
# a sentence. It is a PATTERN guard on the zero-vocabulary route, not a proof: a
# rule may still count by inventing a new name for a learning record (`studies`
# is in the corpus, unused). That route is caught upstream instead — a new
# evidence name moves the count off 23 and trips the check at the top of this
# file. Between them the two doors are covered; neither alone is.
selfjoin() { awk -F'->' -v p="$1" '/^[^#]/ && /->/ { s=$1; n=gsub(p, "", s); if (n>=2) print NR": "$0 }' "$KB"; }
ctl=$(selfjoin 'judge' | wc -l)
[ "$ctl" -ge 1 ] || fail "the counting guard is broken" "positive control /judge/ returned 0; the multi-sig rule joins it twice"
pass "positive control: /judge/ is joined with itself in $ctl rule"
for p in 'teaches' 'work[(]'; do
  n=$(selfjoin "$p" | wc -l)
  [ "$n" = "0" ] && pass "no rule counts ${p%%[*} entries" \
    || fail "${p%%[*} is now joined with itself — that is counted degree on the reward side" \
            "$(selfjoin "$p") — chapter 10 says this will not be built"
done

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
# The staleness guard used to assign `d` and never read it, so a fixture that had
# drifted — or been regenerated by the README's own command, which matched nothing
# and produced a byte-identical copy — passed green while proving nothing. Compare
# CONTENT, not a line count: `grep -c ''` reads a delete-plus-add as no change.
for f in no-person-line no-public-court no-choose-boss; do
  removed=$(diff "$KB" "$CF/$f.nibli" | grep -c '^<')
  added=$(diff "$KB" "$CF/$f.nibli" | grep -c '^>')
  [ "$removed" = "1" ] && [ "$added" = "0" ] \
    || fail "$f is not the constitution minus exactly one line" \
            "$removed removed, $added added — regenerate it from $KB per $CF/README.md"
  out=$("$PIN" --kb "$CF/$f.nibli" "$CF/$f.pins.nibli" 2>&1)
  echo "$out" | grep -q 'PASS' && pass "$f" \
    || fail "$f" "$(echo "$out" | tail -3) — is the fixture stale? regenerate it from $KB"
done

printf '\n\033[32mall checks passed\033[0m\n'
