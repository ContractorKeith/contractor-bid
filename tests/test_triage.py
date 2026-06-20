from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch

from contractor_bid.triage import compact, extract_page_text, extract_pdf_text_pages, pdf_count, triage_project
from contractor_bid.util import read_json, write_json


FIXTURES = Path(__file__).resolve().parent / "fixtures"


def profile() -> dict[str, object]:
    return {
        "profile_id": "fences-gates",
        "trade_name": "Fences and Gates",
        "include_terms": ["fence", "gate", "chain link", "32 31 13"],
        "base_scope": ["operator"],
        "spec_sections": ["32 31"],
        "review_terms": ["access control"],
        "exclude_terms": ["silt fence", "tree protection fence"],
        "quantity_units": ["LF", "EA"],
    }


class TriageTest(unittest.TestCase):
    def test_pdf_text_pages_match_per_page_extractor(self) -> None:
        pdf = FIXTURES / "triage-sample.pdf"
        pages = extract_pdf_text_pages(pdf, pdf_count(pdf))
        self.assertEqual(len(pages), 3)
        for page, text in enumerate(pages, start=1):
            self.assertEqual(compact(text), compact(extract_page_text(pdf, page)))

    def test_pdftotext_extracts_once_per_pdf_when_available(self) -> None:
        calls: list[list[str]] = []

        def fake_run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
            calls.append(cmd)
            Path(cmd[-1]).write_text("page one\fpage two\f", encoding="utf-8")
            return subprocess.CompletedProcess(cmd, 0, "", "")

        with (
            patch("contractor_bid.triage.shutil.which", return_value="/usr/bin/pdftotext"),
            patch("contractor_bid.triage.run", side_effect=fake_run),
        ):
            pages = extract_pdf_text_pages(Path("fake.pdf"), 2)

        self.assertEqual([compact(page) for page in pages], ["page one", "page two"])
        self.assertEqual(len(calls), 1)
        self.assertNotIn("-f", calls[0])
        self.assertNotIn("-l", calls[0])

    def test_triage_writes_suggested_sources_and_scanned_warning(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "070126-sample"
            bid_docs = project / "bid-docs"
            takeoff = project / "bid-package-working" / "takeoff"
            bid_docs.mkdir(parents=True)
            takeoff.mkdir(parents=True)
            shutil.copy2(FIXTURES / "triage-sample.pdf", bid_docs / "triage-sample.pdf")
            shutil.copy2(FIXTURES / "scanned-empty.pdf", bid_docs / "scanned-empty.pdf")
            write_json(
                takeoff / "scope-pages-sources.json",
                {
                    "project_name": "Sample",
                    "prepared": "2026-06-20",
                    "scope_note": "Carry only fence and gate scope.",
                    "bid_decision_summary": "TBD",
                    "what_to_open_first": [],
                    "scope_items": [],
                    "quantity_mentions": [],
                    "brand_or_product_mentions": [],
                    "access_or_interface_notes": [],
                    "not_in_base_scope": [],
                    "open_questions": [],
                    "no_spec_pages_found": "",
                    "scope_pages": [],
                    "spec_pages": [],
                    "excluded_or_reference_only": [],
                },
            )

            stdout = StringIO()
            with redirect_stdout(stdout):
                hits = triage_project(project, profile(), write_sources=True)

            self.assertTrue(hits)
            self.assertIn("looks scanned/image-only", stdout.getvalue())

            suggested = read_json(takeoff / "scope-pages-sources.suggested.json")
            self.assertGreaterEqual(len(suggested["scope_pages"]), 1)
            first = suggested["scope_pages"][0]
            self.assertEqual(first["source_pdf"], "bid-docs/triage-sample.pdf")
            self.assertEqual(first["pdf_page"], 1)
            self.assertEqual(first["sheet"], "A1.0")
            self.assertIn("chain link fence", first["evidence"])

            canonical = read_json(takeoff / "scope-pages-sources.json")
            self.assertEqual(canonical["scope_pages"], suggested["scope_pages"])
            candidate_pages = (takeoff / "candidate-pages.md").read_text(encoding="utf-8")
            self.assertIn("looks scanned/image-only", candidate_pages)

    def test_write_sources_does_not_overwrite_user_content(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            project = Path(tmp) / "070126-sample"
            bid_docs = project / "bid-docs"
            takeoff = project / "bid-package-working" / "takeoff"
            bid_docs.mkdir(parents=True)
            takeoff.mkdir(parents=True)
            shutil.copy2(FIXTURES / "triage-sample.pdf", bid_docs / "triage-sample.pdf")
            write_json(
                takeoff / "scope-pages-sources.json",
                {
                    "project_name": "Sample",
                    "scope_pages": [
                        {
                            "source_pdf": "bid-docs/manual.pdf",
                            "pdf_page": 9,
                            "sheet": "MANUAL",
                            "evidence": "user entered",
                        }
                    ],
                    "spec_pages": [],
                    "excluded_or_reference_only": [],
                },
            )

            triage_project(project, profile(), write_sources=True)

            canonical = read_json(takeoff / "scope-pages-sources.json")
            self.assertEqual(canonical["scope_pages"][0]["source_pdf"], "bid-docs/manual.pdf")


if __name__ == "__main__":
    unittest.main()
