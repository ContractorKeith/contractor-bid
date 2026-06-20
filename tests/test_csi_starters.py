from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

from contractor_bid.csi_starters import (
    ACTIVE_CSI_DIVISIONS_03_33,
    RESERVED_CSI_DIVISIONS_03_33,
    starter_profiles,
)
from contractor_bid.profile import render_skill
from contractor_bid.util import read_json


class CsiStarterCoverageTest(unittest.TestCase):
    def test_active_masterformat_divisions_03_33_have_starters(self) -> None:
        root = Path(__file__).resolve().parents[1]
        active = {seed["division"] for seed in ACTIVE_CSI_DIVISIONS_03_33}
        reserved = set(RESERVED_CSI_DIVISIONS_03_33)
        all_divisions_03_33 = {f"{number:02d}" for number in range(3, 34)}

        self.assertEqual(active | reserved, all_divisions_03_33)
        self.assertFalse(active & reserved)
        self.assertEqual(
            active,
            {
                "03",
                "04",
                "05",
                "06",
                "07",
                "08",
                "09",
                "10",
                "11",
                "12",
                "13",
                "14",
                "21",
                "22",
                "23",
                "25",
                "26",
                "27",
                "28",
                "31",
                "32",
                "33",
            },
        )

        titles = {seed["division"]: seed["title"] for seed in ACTIVE_CSI_DIVISIONS_03_33}
        for profile in starter_profiles():
            division = profile["csi_divisions"][0]
            profile_id = profile["profile_id"]
            with self.subTest(profile=profile_id):
                self.assertEqual(profile["trade_name"], f"Division {division} - {titles[division]}")
                self.assertTrue(profile_id.startswith(f"division-{division}-"))
                self.assertEqual(profile["spec_sections"][0], f"{division} 00 00")

                for field in (
                    "base_scope",
                    "include_terms",
                    "spec_sections",
                    "quantity_units",
                    "review_terms",
                    "exclude_terms",
                    "proposal_exclusions",
                ):
                    self.assertGreater(len(profile[field]), 0, field)

                profile_path = root / "profiles" / f"{profile_id}.json"
                example_path = root / "examples" / "profiles" / f"{profile_id}.json"
                skill_path = root / "skills" / f"{profile_id}-bid-scope" / "SKILL.md"

                self.assertEqual(read_json(profile_path), profile)
                self.assertEqual(read_json(example_path)["profile_id"], profile_id)
                self.assertEqual(skill_path.read_text(encoding="utf-8"), render_skill(profile))

    def test_csi_starter_generator_check_passes(self) -> None:
        root = Path(__file__).resolve().parents[1]
        result = subprocess.run(
            [sys.executable, "scripts/generate-csi-starters.py", "--check"],
            cwd=root,
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
