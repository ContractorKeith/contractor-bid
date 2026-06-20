from __future__ import annotations

import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path

from contractor_bid.cli import main
from contractor_bid.util import read_json


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
                        "--scope-rule",
                        "Carry sample scope only.",
                        "--non-interactive",
                    ]
                ),
                0,
            )
            self.assertTrue((root / "profiles" / "sample-scope.json").exists())
            self.assertEqual(
                read_json(root / "profiles" / "sample-scope.json")["scope_rule"],
                "Carry sample scope only.",
            )
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

    def test_list_profiles_status_and_run_commands(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "bids" / "070126-fence-sample"

            stdout = StringIO()
            with redirect_stdout(stdout):
                self.assertEqual(main(["--root", str(root), "list-profiles"]), 0)
            self.assertIn("fences-gates - Fences and Gates", stdout.getvalue())

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

            stdout = StringIO()
            with redirect_stdout(stdout):
                self.assertEqual(
                    main(
                        [
                            "--root",
                            str(root),
                            "status",
                            str(project),
                            "--profile",
                            "fences-gates",
                            "--today",
                            "2026-06-29",
                        ]
                    ),
                    0,
                )
            self.assertIn("Deliverable", stdout.getvalue())
            self.assertFalse((project / "bid-package-working" / "ALERTS.md").exists())

            self.assertEqual(
                main(
                    [
                        "--root",
                        str(root),
                        "run",
                        str(project),
                        "--profile",
                        "fences-gates",
                        "--today",
                        "2026-06-29",
                    ]
                ),
                0,
            )
            self.assertTrue((project / "bid-package-working" / "ALERTS.md").exists())
            zips = list((project / "bid-package-working" / "supplier-sendoff").glob("*.zip"))
            self.assertEqual(len(zips), 1)

    def test_version_exits_zero(self) -> None:
        stdout = StringIO()
        with self.assertRaises(SystemExit) as raised, redirect_stdout(stdout):
            main(["--version"])
        self.assertEqual(raised.exception.code, 0)
        self.assertIn("contractor-bid 0.1.0", stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
