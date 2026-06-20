from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from contractor_bid import tracker
from contractor_bid.cli import main
from contractor_bid.util import read_json


class TrackerUnitTest(unittest.TestCase):
    def test_due_urgency(self) -> None:
        today = date(2026, 6, 20)
        self.assertEqual(tracker.due_urgency("2026-06-18", today), "past")
        self.assertEqual(tracker.due_urgency("2026-06-21", today), "soon")
        self.assertEqual(tracker.due_urgency("2026-06-22 14:00", today), "soon")
        self.assertEqual(tracker.due_urgency("2026-08-01", today), "")
        self.assertEqual(tracker.due_urgency("", today), "")
        self.assertEqual(tracker.due_urgency("not-a-date", today), "")

    def test_add_update_move_roundtrip(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            entry, created, changed = tracker.add_or_update(
                root, name="Riverside Plaza", location="Tampa, FL", due_date="2026-07-01", progress="Triage"
            )
            self.assertTrue(created)
            self.assertEqual(entry["status"], "active")
            self.assertEqual(entry["id"], "riverside-plaza")

            entry2, created2, changed2 = tracker.add_or_update(
                root, name="Riverside Plaza", progress="Submitted", next_action="Follow up"
            )
            self.assertFalse(created2)
            self.assertIn("progress", changed2)
            self.assertEqual(entry2["progress"], "Submitted")

            data = tracker.load_tracker(root)
            self.assertEqual(len(tracker.active_bids(data)), 1)
            self.assertEqual(len(tracker.archived_bids(data)), 0)

            moved = tracker.move_entry(root, "Riverside Plaza", outcome="won")
            self.assertEqual(moved["status"], "archived")
            self.assertEqual(moved["outcome"], "won")

            data = tracker.load_tracker(root)
            self.assertEqual(len(tracker.active_bids(data)), 0)
            self.assertEqual(len(tracker.archived_bids(data)), 1)

            reopened = tracker.reopen_entry(root, "Riverside Plaza")
            self.assertEqual(reopened["status"], "active")

    def test_add_requires_identifier(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                tracker.add_or_update(Path(tmp))


class TrackerCliTest(unittest.TestCase):
    def test_cli_add_list_move_build(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            self.assertEqual(
                main(["--root", str(root), "track-add", "--name", "Lakeland WH", "--due", "2026-08-15", "--progress", "Pricing"]),
                0,
            )
            json_path = root / ".contractor-bid" / "bid-tracker.json"
            self.assertTrue(json_path.exists())
            self.assertTrue((root / "Bid-Tracker.xlsx").exists())

            data = read_json(json_path)
            self.assertEqual(len(data["bids"]), 1)
            self.assertEqual(data["bids"][0]["progress"], "Pricing")

            self.assertEqual(main(["--root", str(root), "track-list"]), 0)
            self.assertEqual(main(["--root", str(root), "track-list", "--all"]), 0)

            self.assertEqual(
                main(["--root", str(root), "track-move", "Lakeland WH", "--outcome", "lost"]), 0
            )
            data = read_json(json_path)
            self.assertEqual(data["bids"][0]["status"], "archived")
            self.assertEqual(data["bids"][0]["outcome"], "lost")

            self.assertEqual(main(["--root", str(root), "track-build"]), 0)

    def test_cli_add_from_project_folder(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project = root / "bids" / "070126-fence-sample"
            # Create a real bid project so track-add can read its project.json.
            self.assertEqual(
                main(["--root", str(root), "new", str(project), "--profile", "fences-gates",
                      "--project-name", "Fence Sample", "--bid-due", "2026-07-01", "--gc", "Acme GC"]),
                0,
            )
            self.assertEqual(
                main(["--root", str(root), "track-add", str(project), "--progress", "Triage"]),
                0,
            )
            data = read_json(root / ".contractor-bid" / "bid-tracker.json")
            self.assertEqual(len(data["bids"]), 1)
            entry = data["bids"][0]
            self.assertEqual(entry["project"], "Fence Sample")
            self.assertEqual(entry["client_gc"], "Acme GC")
            self.assertEqual(entry["due_date"], "2026-07-01")
            self.assertEqual(entry["profile"], "fences-gates")


if __name__ == "__main__":
    unittest.main()
