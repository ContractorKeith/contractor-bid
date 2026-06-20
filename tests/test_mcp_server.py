from __future__ import annotations

import py_compile
import shutil
import tempfile
import unittest
from pathlib import Path

from contractor_bid import __version__
try:
    from contractor_bid.mcp_server import (
        cb_build_packets,
        cb_build_workbook,
        cb_check,
        cb_list_profiles,
        cb_new_project,
        cb_package_sendoff,
        cb_track_add,
        cb_track_list,
        cb_triage,
        mcp,
    )
    HAS_MCP = True
except (ImportError, SystemExit):
    HAS_MCP = False
from contractor_bid.util import read_json


FIXTURES = Path(__file__).resolve().parent / "fixtures"


class McpServerTest(unittest.TestCase):
    def test_server_compiles_and_registers_planned_tools(self) -> None:
        py_compile.compile("src/contractor_bid/mcp_server.py", doraise=True)
        tool_names = {tool.name for tool in mcp._tool_manager.list_tools()}
        self.assertGreaterEqual(
            tool_names,
            {
                "cb_doctor",
                "cb_new_project",
                "cb_triage",
                "cb_build_packets",
                "cb_build_workbook",
                "cb_check",
                "cb_package_sendoff",
                "cb_learn",
                "cb_track_add",
                "cb_track_update",
                "cb_track_move",
                "cb_track_list",
                "cb_list_profiles",
            },
        )
        triage_tool = mcp._tool_manager.get_tool("cb_triage")
        self.assertIsNotNone(triage_tool)
        self.assertIn("project", triage_tool.parameters["properties"])
        self.assertIn("description", triage_tool.parameters["properties"]["project"])

    def test_mcp_round_trip_bid_workflow(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            project_rel = "bids/070126-mcp-sample"
            project = root / project_rel

            profiles = cb_list_profiles(workspace_root=str(root))
            self.assertEqual(profiles["status"], "ok")
            self.assertTrue(
                any(row["profile_id"] == "fences-gates" for row in profiles["data"]["profiles"])
            )

            created = cb_new_project(
                project_rel,
                "fences-gates",
                workspace_root=str(root),
                project_name="MCP Sample",
                bid_due="2026-07-01 14:00",
            )
            self.assertEqual(created["status"], "ok")
            self.assertTrue((project / "bid-package-working").exists())

            shutil.copy2(FIXTURES / "triage-sample.pdf", project / "bid-docs" / "triage-sample.pdf")
            triage = cb_triage(
                project_rel,
                "fences-gates",
                workspace_root=str(root),
                write_sources=True,
            )
            self.assertEqual(triage["status"], "ok")
            self.assertGreaterEqual(triage["data"]["candidate_pages"], 1)

            sources = read_json(project / "bid-package-working" / "takeoff" / "scope-pages-sources.json")
            self.assertGreaterEqual(len(sources["scope_pages"]), 1)

            packets = cb_build_packets(project_rel, workspace_root=str(root))
            self.assertEqual(packets["status"], "ok")
            self.assertTrue((project / "bid-package-working" / "scope-pages.pdf").exists())

            workbook = cb_build_workbook(
                project_rel,
                workspace_root=str(root),
                profile="fences-gates",
            )
            self.assertEqual(workbook["status"], "ok")
            self.assertTrue(
                (project / "bid-package-working" / "01-Takeoff-Worksheet-REV1.xlsx").exists()
            )

            check = cb_check(
                project_rel,
                "fences-gates",
                workspace_root=str(root),
                today="2026-06-29",
            )
            self.assertIn(check["status"], {"ok", "warning"})
            self.assertTrue((project / "bid-package-working" / "ALERTS.md").exists())

            sendoff = cb_package_sendoff(project_rel, workspace_root=str(root))
            self.assertEqual(sendoff["status"], "ok")
            self.assertTrue(sendoff["data"]["zip"].endswith(".zip"))
            self.assertTrue(Path(sendoff["data"]["zip"]).exists())

    def test_tracker_tools_require_confirmation_before_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)

            proposal = cb_track_add(
                workspace_root=str(root),
                name="Tracker Sample",
                due="2026-07-01",
                progress="Triage",
            )
            self.assertEqual(proposal["status"], "warning")
            self.assertFalse((root / ".contractor-bid" / "bid-tracker.json").exists())

            written = cb_track_add(
                workspace_root=str(root),
                name="Tracker Sample",
                due="2026-07-01",
                progress="Triage",
                confirm=True,
            )
            self.assertEqual(written["status"], "ok")
            self.assertTrue((root / ".contractor-bid" / "bid-tracker.json").exists())

            listed = cb_track_list(workspace_root=str(root))
            self.assertEqual(listed["status"], "ok")
            self.assertEqual(len(listed["data"]["active"]), 1)

    def test_version_bumped_for_mcp_release(self) -> None:
        self.assertEqual(__version__, "0.2.0")


if __name__ == "__main__":
    unittest.main()
