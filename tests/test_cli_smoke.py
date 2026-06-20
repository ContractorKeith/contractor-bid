from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from contractor_bid.cli import main


class CliSmokeTest(unittest.TestCase):
    def test_init_new_build_check_package(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "bids" / "070126-sample"

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "init",
                        "--profile",
                        "sample-scope",
                        "--company",
                        "Sample Sub",
                        "--trade",
                        "Sample Scope",
                        "--divisions",
                        "09",
                        "--base-scope",
                        "sample work",
                        "--include-terms",
                        "sample,scope",
                        "--review-terms",
                        "review-only",
                        "--exclude-terms",
                        "excluded work",
                        "--non-interactive",
                    ]
                ),
                0,
            )
            self.assertTrue((root / "profiles" / "sample-scope.json").exists())
            self.assertTrue((root / "skills" / "sample-scope-bid-scope" / "SKILL.md").exists())

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "new",
                        str(project),
                        "--profile",
                        "sample-scope",
                        "--project-name",
                        "Sample Project",
                        "--bid-due",
                        "2026-07-01 14:00",
                    ]
                ),
                0,
            )
            self.assertTrue((project / "bid-docs").exists())
            self.assertTrue((project / "bid-package-working" / "takeoff" / "scope-pages-sources.json").exists())

            self.assertEqual(main(["build-packets", str(project)]), 0)
            self.assertTrue((project / "bid-package-working" / "00-Bid-Scope-Summary.md").exists())

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "build-workbook",
                        str(project),
                        "--profile",
                        "sample-scope",
                    ]
                ),
                0,
            )
            self.assertTrue((project / "bid-package-working" / "01-Takeoff-Worksheet-REV1.xlsx").exists())

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "check",
                        str(project),
                        "--profile",
                        "sample-scope",
                        "--today",
                        "2026-06-29",
                    ]
                ),
                0,
            )
            self.assertTrue((project / "bid-package-working" / "ALERTS.md").exists())

            self.assertEqual(main(["package-sendoff", str(project)]), 0)
            zips = list((project / "bid-package-working" / "supplier-sendoff").glob("*.zip"))
            self.assertEqual(len(zips), 1)

    def test_builtin_profile_loads_without_workspace_profile(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "bids" / "070126-fence-sample"

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "new",
                        str(project),
                        "--profile",
                        "fences-gates",
                        "--project-name",
                        "Fence Sample",
                    ]
                ),
                0,
            )
            self.assertTrue((project / ".agent" / "skills" / "fences-gates-bid-scope" / "SKILL.md").exists())


if __name__ == "__main__":
    unittest.main()
