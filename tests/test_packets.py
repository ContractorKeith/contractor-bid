from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from contractor_bid.packets import build_packets
from contractor_bid.util import write_json


class PacketSummaryTest(unittest.TestCase):
    def test_empty_sources_summary_has_no_absolute_or_missing_packet_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "070126-example"
            takeoff = project / "bid-package-working" / "takeoff"
            takeoff.mkdir(parents=True)
            write_json(
                takeoff / "scope-pages-sources.json",
                {
                    "project_name": "Example",
                    "prepared": "2026-06-20",
                    "scope_note": "Carry only approved scope.",
                    "bid_decision_summary": "Not ready for packet extraction.",
                    "scope_pages": [],
                    "spec_pages": [],
                },
            )

            result = build_packets(project)
            summary = Path(result["summary"]).read_text(encoding="utf-8")

            self.assertNotIn(str(project), summary)
            self.assertNotIn("scope-pages.pdf` (0 page(s))", summary)
            self.assertNotIn("spec-pages.pdf` (0 page(s))", summary)
            self.assertNotIn("Open this first: `", summary)
            self.assertIn("Fill `bid-package-working/takeoff/scope-pages-sources.json`", summary)


if __name__ == "__main__":
    unittest.main()
