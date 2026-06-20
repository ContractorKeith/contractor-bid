#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SRC_DIR = REPO_ROOT / "src"
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from contractor_bid.csi_starters import starter_profiles  # noqa: E402
from contractor_bid.profile import render_skill  # noqa: E402
from contractor_bid.util import read_json, write_json  # noqa: E402


def example_profile(profile: dict) -> dict:
    item = dict(profile)
    division = profile["csi_divisions"][0]
    item["company_name"] = f"Example Division {division} Contractor"
    return item


def expected_files(root: Path) -> dict[Path, str | dict]:
    expected: dict[Path, str | dict] = {}
    for profile in starter_profiles():
        profile_id = profile["profile_id"]
        expected[root / "profiles" / f"{profile_id}.json"] = profile
        expected[root / "examples" / "profiles" / f"{profile_id}.json"] = example_profile(profile)
        expected[root / "skills" / f"{profile_id}-bid-scope" / "SKILL.md"] = render_skill(profile)
    return expected


def check(root: Path) -> int:
    failures: list[str] = []
    for path, expected in expected_files(root).items():
        if not path.exists():
            failures.append(f"missing: {path.relative_to(root)}")
            continue
        if isinstance(expected, dict):
            actual = read_json(path)
            if actual != expected:
                failures.append(f"stale: {path.relative_to(root)}")
        else:
            actual = path.read_text(encoding="utf-8")
            if actual != expected:
                failures.append(f"stale: {path.relative_to(root)}")
    if failures:
        print("CSI starter generation check failed:")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("CSI starter profiles, examples, and skills are current.")
    return 0


def write(root: Path) -> int:
    count = 0
    for path, expected in expected_files(root).items():
        if isinstance(expected, dict):
            write_json(path, expected)
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8")
        count += 1
    print(f"Wrote {count} CSI starter profile, example, and skill files.")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Generate canonical CSI Division 03-33 starter profiles, examples, and skills."
    )
    parser.add_argument("--root", type=Path, default=REPO_ROOT, help="Repository root.")
    parser.add_argument("--check", action="store_true", help="Only check generated files.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if args.check:
        return check(root)
    return write(root)


if __name__ == "__main__":
    raise SystemExit(main())
