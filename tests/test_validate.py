from __future__ import annotations

import tempfile
import unittest
from datetime import date
from pathlib import Path

from contractor_bid.validate import check_page_sources, empty_or_placeholder, parse_due_date, validate_project
from contractor_bid.util import write_json


class ValidateTest(unittest.TestCase):
    def test_bracketed_notes_are_not_placeholders_but_tbd_is(self) -> None:
        self.assertFalse(empty_or_placeholder("Gate operator [by others]"))
        self.assertTrue(empty_or_placeholder("TBD"))

    def test_page_sources_placeholder_scan_allows_bracketed_note(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            work = Path(tmp) / "bid-package-working"
            takeoff = work / "takeoff"
            takeoff.mkdir(parents=True)
            write_json(
                takeoff / "scope-pages-sources.json",
                {
                    "bid_decision_summary": "Gate operator [by others].",
                    "what_to_open_first": ["A1.0"],
                    "scope_items": ["gate"],
                    "not_in_base_scope": ["operator wiring by others"],
                    "no_spec_pages_found": "No separate specs in received docs.",
                },
            )
            warnings = check_page_sources(work)
            self.assertFalse(
                any("plain-English quick read" in warning for warning in warnings),
                warnings,
            )

    def test_due_date_math_reports_urgent_and_past(self) -> None:
        self.assertEqual(parse_due_date("070126-sample"), date(2026, 7, 1))
        profile = {"profile_id": "sample", "trade_name": "Sample", "exclude_terms": [], "review_terms": []}
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "070126-sample"
            work = project / "bid-package-working" / "takeoff"
            work.mkdir(parents=True)
            write_json(
                work / "scope-pages-sources.json",
                {
                    "bid_decision_summary": "ready",
                    "what_to_open_first": ["A1.0"],
                    "scope_items": ["scope"],
                    "not_in_base_scope": ["none"],
                    "no_spec_pages_found": "none",
                },
            )
            _out, _code, warnings, errors = validate_project(
                project,
                profile,
                today=date(2026, 6, 30),
                write=False,
            )
            self.assertEqual(errors, [])
            self.assertEqual(warnings, [])

            out, _code, _warnings, _errors = validate_project(
                project,
                profile,
                today=date(2026, 7, 2),
                write=True,
            )
            self.assertIn("1 day(s) past", out.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
