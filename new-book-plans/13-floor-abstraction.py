#!/usr/bin/env python3
# SPDX-License-Identifier: MIT OR Apache-2.0
"""Run the rights-floor event projection against a minimal exact-source KB.

On 2026-08-05, clean release Nibli ``225bba4`` exhibited global witness-candidate
expansion when the full T3 constitution and an opaque ``event { ... }``
entitlement query shared one process.  Verify before relying on that engine
claim.  This harness temporarily isolates the query: it extracts the eight live
floor assertions verbatim, adds only the two live standing bridges and
representative facts needed by the contract, and runs the resulting fixture in
one fresh release ``nibli-pin`` process.

The result is a bounded engine regression for the exact extracted source.  It
does not prove that an opaque-abstraction query against the full constitution
is performant, authenticate any premise, or establish real-world delivery.

Usage:
    python3 new-book-plans/13-floor-abstraction.py --check
    python3 new-book-plans/13-floor-abstraction.py --check --execute
    python3 new-book-plans/13-floor-abstraction.py --fingerprints
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable, Sequence
from dataclasses import dataclass


ROOT = pathlib.Path(__file__).resolve().parents[1]
CONSTITUTION = ROOT / "new-book-plans/constitution.nibli"
EXPECTED_FLOORS = (
    "secure",
    "eats",
    "dwell",
    "healthy",
    "learn",
    "expresses",
    "believe",
    "meets",
)
HOSTILE_SANCTION = "all $x: person($x) & ~believe($x) -> prisoner($x)."
HOSTILE_PATTERN = r"'prisoner' -> 'believe'"
NON_FLOOR_CONTROL = "all $x: person($x) & ~home($x) -> prisoner($x)."
FLOOR_ASSERTION = re.compile(
    r"^entitled\(every person, event \{ (?P<predicate>[a-z][a-z0-9_]*)\(\) \}\)\.$"
)
FREE_TO_PERSON = re.compile(
    r"^all \$(?P<variable>[a-z][a-z0-9_]*): "
    r"free\(\$(?P=variable)\) -> person\(\$(?P=variable)\)\.$"
)
PRISONER_TO_PERSON = re.compile(
    r"^all \$(?P<variable>[a-z][a-z0-9_]*): "
    r"prisoner\(\$(?P=variable)\) -> person\(\$(?P=variable)\)\.$"
)
PASS_SUMMARY = re.compile(
    r"(?m)^nibli-pin:\s+PASS\s+[—-]\s+([0-9]+)\s+pins?\s*$"
)
TIMEOUT_SECONDS = 60
AUXILIARY_PIN_COUNT = 2
BOUNDARY = (
    "minimal exact-source engine regression only; this does not prove the full "
    "constitution's opaque-abstraction query is performant"
)


class FloorAbstractionError(RuntimeError):
    """Raised when the source shape, fixture, or engine result is unsafe."""


@dataclass(frozen=True)
class ExtractedFloor:
    predicate: str
    assertion: str


@dataclass(frozen=True)
class QueryCheck:
    expression: str
    expected: str
    purpose: str


@dataclass(frozen=True)
class Fixture:
    constitution_sha256: str
    floors: tuple[ExtractedFloor, ...]
    free_rule: str
    prisoner_rule: str
    knowledge_base: str
    pins: str
    pin_count: int


def sha256(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def read_constitution() -> tuple[bytes, str]:
    if CONSTITUTION.is_symlink():
        raise FloorAbstractionError("constitution may not be a symlink")
    try:
        source = CONSTITUTION.read_bytes()
    except OSError as exc:
        raise FloorAbstractionError(f"cannot read constitution: {exc}") from exc
    try:
        text = source.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise FloorAbstractionError("constitution is not valid UTF-8") from exc
    return source, text


def extract_floors(source: str) -> tuple[ExtractedFloor, ...]:
    floors: list[ExtractedFloor] = []
    universal_entitlements = [
        line
        for line in source.splitlines()
        if line.startswith("entitled(every person")
    ]
    for line in source.splitlines():
        match = FLOOR_ASSERTION.fullmatch(line)
        if match is not None:
            floors.append(ExtractedFloor(match.group("predicate"), line))
    predicates = tuple(floor.predicate for floor in floors)
    if predicates != EXPECTED_FLOORS:
        raise FloorAbstractionError(
            "live floor assertions must be the exact ordered set "
            f"{list(EXPECTED_FLOORS)}, got {list(predicates)}"
        )
    if len({floor.assertion for floor in floors}) != len(floors):
        raise FloorAbstractionError("live floor assertions contain a duplicate")
    if universal_entitlements != [floor.assertion for floor in floors]:
        raise FloorAbstractionError(
            "a live universal entitlement exists outside the canonical floor shape"
        )
    return tuple(floors)


def unique_live_rule(source: str, pattern: re.Pattern[str], label: str) -> str:
    matches = [line for line in source.splitlines() if pattern.fullmatch(line)]
    if len(matches) != 1:
        raise FloorAbstractionError(
            f"{label} must occur once as an exact live rule; found {len(matches)}"
        )
    return matches[0]


def query_checks(floors: Sequence[ExtractedFloor]) -> tuple[QueryCheck, ...]:
    checks: list[QueryCheck] = []
    for floor in floors:
        checks.append(
            QueryCheck(
                f"entitled(Bela, event {{ {floor.predicate}() }})",
                "TRUE",
                f"Bela receives the extracted {floor.predicate} floor entitlement.",
            )
        )
    checks.extend(
        (
            QueryCheck(
                "person(Hano)",
                "TRUE",
                "The extracted free-to-person bridge preserves Hano's standing.",
            ),
            QueryCheck(
                "entitled(Hano, event { eats() })",
                "TRUE",
                "Hano receives the food entitlement through free-to-person standing.",
            ),
            QueryCheck(
                "entitled(Adam, event { eats() })",
                "TRUE",
                "A directly registered person receives a representative floor entitlement.",
            ),
            QueryCheck(
                "entitled(Court, event { eats() })",
                "FALSE",
                "A name without personhood receives no floor entitlement.",
            ),
            QueryCheck(
                "entitled(Adam, event { home() })",
                "FALSE",
                "The non-floor home predicate is not projected as an entitlement.",
            ),
        )
    )
    for floor in floors:
        checks.append(
            QueryCheck(
                f"{floor.predicate}(Bela)",
                "FALSE",
                f"The {floor.predicate} event abstraction does not fabricate actuality.",
            )
        )
    expected_count = len(EXPECTED_FLOORS) * 2 + 5
    if len(checks) != expected_count:
        raise FloorAbstractionError(
            f"internal query contract drifted: expected {expected_count}, got {len(checks)}"
        )
    return tuple(checks)


def build_knowledge_base(
    floors: Sequence[ExtractedFloor], free_rule: str, prisoner_rule: str
) -> str:
    lines = [
        "# Minimal floor-abstraction fixture generated from the live constitution.",
        "# It is an engine regression, not a replacement constitution.",
        "",
        *(floor.assertion for floor in floors),
        free_rule,
        prisoner_rule,
        "",
        "person(Bela).",
        "person(Adam).",
        "free(Hano).",
        "",
    ]
    return "\n".join(lines)


def build_pins(checks: Sequence[QueryCheck]) -> str:
    pin_count = len(checks) + AUXILIARY_PIN_COUNT
    lines = [
        f":expect-pins {pin_count}",
        "# Minimal exact-source floor-event projection regression.",
        f"# Scope boundary: {BOUNDARY}.",
        "",
    ]
    for check in checks:
        lines.extend(
            (
                f"# {check.purpose}",
                f"? {check.expression}.",
                f"# => {check.expected}",
                "",
            )
        )
    lines.extend(
        (
            "# Control: the engine accepts the same sanction shape for non-floor home.",
            ":accept-scoped",
            NON_FLOOR_CONTROL,
            "",
            "# Missing a floor right may not become a route into confinement.",
            f":refuse reasoning /{HOSTILE_PATTERN}/",
            HOSTILE_SANCTION,
            "",
        )
    )
    return "\n".join(lines)


def validate_fixture(fixture: Fixture) -> None:
    expected_floor_lines = tuple(floor.assertion for floor in fixture.floors)
    kb_floor_lines = tuple(
        line
        for line in fixture.knowledge_base.splitlines()
        if FLOOR_ASSERTION.fullmatch(line) is not None
    )
    if kb_floor_lines != expected_floor_lines:
        raise FloorAbstractionError("minimal KB does not contain the exact extracted floors")
    if fixture.knowledge_base.count(fixture.free_rule) != 1:
        raise FloorAbstractionError("minimal KB lost the exact free-to-person bridge")
    if fixture.knowledge_base.count(fixture.prisoner_rule) != 1:
        raise FloorAbstractionError("minimal KB lost the exact prisoner-to-person bridge")
    if fixture.knowledge_base.count("person(Bela).") != 1:
        raise FloorAbstractionError("minimal KB must register Bela exactly once")
    if fixture.knowledge_base.count("person(Adam).") != 1:
        raise FloorAbstractionError("minimal KB must register Adam exactly once")
    if fixture.knowledge_base.count("free(Hano).") != 1:
        raise FloorAbstractionError("minimal KB must free Hano exactly once")
    if fixture.pins.count("\n? ") != fixture.pin_count - AUXILIARY_PIN_COUNT:
        raise FloorAbstractionError("generated query count differs from the pin contract")
    if fixture.pins.count("\n:refuse reasoning ") != 1:
        raise FloorAbstractionError("generated hostile-refusal contract drifted")
    if fixture.pins.count("\n:accept-scoped\n") != 1:
        raise FloorAbstractionError("generated non-floor sanction control drifted")
    if not fixture.pins.startswith(f":expect-pins {fixture.pin_count}\n"):
        raise FloorAbstractionError("generated :expect-pins declaration drifted")


def make_fixture() -> Fixture:
    source_bytes, source = read_constitution()
    floors = extract_floors(source)
    free_rule = unique_live_rule(source, FREE_TO_PERSON, "free-to-person bridge")
    prisoner_rule = unique_live_rule(
        source, PRISONER_TO_PERSON, "prisoner-to-person bridge"
    )
    checks = query_checks(floors)
    fixture = Fixture(
        constitution_sha256=sha256(source_bytes),
        floors=floors,
        free_rule=free_rule,
        prisoner_rule=prisoner_rule,
        knowledge_base=build_knowledge_base(floors, free_rule, prisoner_rule),
        pins=build_pins(checks),
        pin_count=len(checks) + AUXILIARY_PIN_COUNT,
    )
    validate_fixture(fixture)
    return fixture


def select_pin(cli_pin: pathlib.Path | None) -> pathlib.Path:
    if cli_pin is not None:
        candidate = cli_pin
    elif os.environ.get("NIBLI_PIN", "").strip():
        candidate = pathlib.Path(os.environ["NIBLI_PIN"].strip())
    elif os.environ.get("NIBLI_SRC", "").strip():
        candidate = (
            pathlib.Path(os.environ["NIBLI_SRC"].strip())
            / "target/release/nibli-pin"
        )
    else:
        on_path = shutil.which("nibli-pin")
        candidate = (
            pathlib.Path(on_path)
            if on_path
            else pathlib.Path.home()
            / "projects/dhilipsiva/nibli/target/release/nibli-pin"
        )
    candidate = candidate.expanduser().resolve()
    if not candidate.is_file() or not os.access(candidate, os.X_OK):
        raise FloorAbstractionError(
            f"release nibli-pin is missing or not executable: {candidate}"
        )
    if "target" in candidate.parts and "debug" in candidate.parts:
        raise FloorAbstractionError(f"debug nibli-pin is not accepted: {candidate}")
    return candidate


def output_tail(output: str, limit: int = 20) -> str:
    return "\n".join(output.splitlines()[-limit:])


def parse_engine_pass(output: str, expected_pins: int) -> None:
    clean = re.sub(
        r"(?im)^\s*[^\r\n]+:\s+[0-9]+\s+pins?,\s+0\s+findings?,\s+"
        r"0\s+harness errors?\s*$",
        "",
        output,
    )
    forbidden = re.search(
        r"(?im)(?:FINDING|HARNESS ERROR|NO LONGER REPRODUCE|TRACEBACK|PANIC)",
        clean,
    )
    if forbidden is not None:
        raise FloorAbstractionError(
            "engine output contains a failure marker:\n" + output_tail(output)
        )
    matches = PASS_SUMMARY.findall(output)
    if len(matches) != 1:
        raise FloorAbstractionError(
            "expected one nibli-pin PASS summary:\n" + output_tail(output)
        )
    actual = int(matches[0])
    if actual != expected_pins:
        raise FloorAbstractionError(
            f"nibli-pin ran {actual} pins, expected {expected_pins}"
        )


def execute_fixture(fixture: Fixture, pin: pathlib.Path) -> None:
    with tempfile.TemporaryDirectory(prefix="floor-abstraction-") as raw_temp:
        temp = pathlib.Path(raw_temp)
        kb_path = temp / "minimal-floor.nibli"
        pin_path = temp / "minimal-floor.pins.nibli"
        kb_path.write_text(fixture.knowledge_base, encoding="utf-8", newline="\n")
        pin_path.write_text(fixture.pins, encoding="utf-8", newline="\n")
        command = [str(pin), "--kb", str(kb_path), str(pin_path)]
        try:
            completed = subprocess.run(
                command,
                cwd=ROOT,
                text=True,
                encoding="utf-8",
                errors="replace",
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                timeout=TIMEOUT_SECONDS,
                check=False,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise FloorAbstractionError(f"cannot complete nibli-pin run: {exc}") from exc
    if completed.returncode != 0:
        raise FloorAbstractionError(
            f"nibli-pin exited {completed.returncode}:\n{output_tail(completed.stdout)}"
        )
    parse_engine_pass(completed.stdout, fixture.pin_count)


def fingerprints(fixture: Fixture) -> str:
    payload = {
        "constitution_sha256": fixture.constitution_sha256,
        "floor_assertions_sha256": sha256(
            ("\n".join(floor.assertion for floor in fixture.floors) + "\n").encode(
                "utf-8"
            )
        ),
        "floor_predicates": [floor.predicate for floor in fixture.floors],
        "minimal_kb_sha256": sha256(fixture.knowledge_base.encode("utf-8")),
        "pins_sha256": sha256(fixture.pins.encode("utf-8")),
        "pin_count": fixture.pin_count,
        "standing_bridges_sha256": sha256(
            f"{fixture.free_rule}\n{fixture.prisoner_rule}\n".encode("utf-8")
        ),
    }
    return json.dumps(payload, indent=2, sort_keys=True)


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="validate source and fixture shape")
    parser.add_argument(
        "--execute",
        action="store_true",
        help="run the minimal release-engine regression",
    )
    parser.add_argument(
        "--fingerprints",
        action="store_true",
        help="print exact-source fixture fingerprints",
    )
    parser.add_argument("--pin", type=pathlib.Path, help="explicit release nibli-pin path")
    args = parser.parse_args(list(argv) if argv is not None else None)
    if args.fingerprints and args.execute:
        raise FloorAbstractionError("--fingerprints and --execute are mutually exclusive")
    if args.pin is not None and not args.execute:
        raise FloorAbstractionError("--pin requires --execute")

    fixture = make_fixture()
    if args.fingerprints:
        print(fingerprints(fixture))
        return 0
    if args.execute:
        execute_fixture(fixture, select_pin(args.pin))
        print(
            f"13-floor-abstraction: PASS — {fixture.pin_count} minimal exact-source "
            "engine regressions"
        )
    else:
        print(
            "13-floor-abstraction: source and fixture shape current; "
            f"extracted {len(fixture.floors)} floor assertions; execution skipped"
        )
    print(f"Source: constitution SHA-256 {fixture.constitution_sha256}.")
    print(f"Scope: {BOUNDARY}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FloorAbstractionError as exc:
        print(f"13-floor-abstraction: {exc}", file=sys.stderr)
        raise SystemExit(1)
