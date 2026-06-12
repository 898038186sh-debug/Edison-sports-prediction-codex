#!/usr/bin/env python3
"""Lightweight validation for the Sports Prediction Codex Skill repository."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THIS_FILE = Path(__file__).resolve()

JSON_FILES = [
    ROOT / ".agents/plugins/marketplace.json",
    ROOT / "plugins/sports-prediction-codex-plugin/.codex-plugin/plugin.json",
]

# Only flag secret-like assignments, not documentation that merely says "do not commit secrets".
SECRET_ASSIGNMENT_RE = re.compile(
    r"(?i)(api[_-]?key|secret|token|password|private[_-]?key)\s*[:=]\s*['\"]?[A-Za-z0-9_\-./+=]{12,}"
)
PRIVATE_KEY_RE = re.compile(r"BEGIN (RSA|OPENSSH|EC|DSA|PRIVATE) KEY")

# These are risky when used promotionally. Lines containing clear negation/instruction are allowed.
RISKY_LANGUAGE_RE = re.compile(
    r"(guaranteed win|100% win|lock of the day|sure bet|risk-free|稳赚|稳赢|包赢|必中|绝对准确)",
    re.IGNORECASE,
)
NEGATION_RE = re.compile(
    r"(not|never|do not|don't|no |avoid|forbid|forbidden|prohibit|without|不是|不要|不能|禁止|避免|不得)",
    re.IGNORECASE,
)

SKIP_DIRS = {".git", "node_modules", "vendor", "__pycache__", "work", "outputs"}


def iter_text_files():
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.resolve() == THIS_FILE:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".zip", ".pdf"}:
            continue
        yield path


def validate_json():
    ok = True
    for path in JSON_FILES:
        if not path.exists():
            print(f"MISSING JSON: {path.relative_to(ROOT)}")
            ok = False
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
            print(f"OK JSON: {path.relative_to(ROOT)}")
        except json.JSONDecodeError as exc:
            print(f"INVALID JSON: {path.relative_to(ROOT)}: {exc}")
            ok = False
    return ok


def scan_patterns():
    ok = True
    for path in iter_text_files():
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if SECRET_ASSIGNMENT_RE.search(line) or PRIVATE_KEY_RE.search(line):
                print(f"POSSIBLE SECRET: {path.relative_to(ROOT)}:{i}: {line[:160]}")
                ok = False
            if RISKY_LANGUAGE_RE.search(line) and not NEGATION_RE.search(line):
                print(f"POSSIBLE PROMOTIONAL RISKY LANGUAGE: {path.relative_to(ROOT)}:{i}: {line[:160]}")
                ok = False
    return ok


def main():
    json_ok = validate_json()
    pattern_ok = scan_patterns()
    if json_ok and pattern_ok:
        print("Validation completed with no required-action findings.")
        return 0
    print("Validation completed with findings. Review the messages above.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
