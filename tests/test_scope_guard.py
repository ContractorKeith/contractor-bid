from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from contractor_bid.util import write_json
from contractor_bid.workbook import build_workbook


class ScopeGuardTest(unittest.TestCase):
    def test_included_row_with_excluded_term_raises(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "070126-sample"
            takeoff = project / "bid-package-working" / "takeoff"
            takeoff.mkdir(parents=True)
            write_json(
                takeoff / "sample.json",
                {
                    "project_name": "Sample",
                    "bom": [
                        {
                            "section": "32",
                            "item": "Bollard",
                            "description": "Provide bollard at gate opening.",
                            "qty": 1,
                            "uom": "EA",
                            "status": "Included",
                        }
                    ],
                    "scope_specs": [],
                },
            )

            with self.assertRaisesRegex(ValueError, "excluded by profile"):
                build_workbook(
                    project,
                    profile={
                        "profile_id": "fences-gates",
                        "trade_name": "Fences and Gates",
                        "exclude_terms": ["bollard"],
                        "review_terms": [],
                    },
                )


if __name__ == "__main__":
    unittest.main()
