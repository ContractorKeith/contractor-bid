# Changelog

All notable changes to `contractor-bid` will be documented here.

## Unreleased

## [0.2.0] - 2026-06-20

MCP and agent plugin distribution release.

- Added `contractor-bid-mcp`, a FastMCP stdio server installed with the optional
  `contractor-bid[mcp]` extra.
- Added MCP tools for doctor, profile listing, project creation, triage, packet
  building, workbook building, validation, sendoff packaging, learning feedback,
  and bid tracker operations.
- Added structured MCP responses with status, artifacts, summaries, alerts,
  next-tool hints, and data payloads.
- Added tracker write confirmation behavior for MCP tools so agents can show
  proposed changes before writing.
- Added Claude Code, Codex, and Cursor plugin metadata plus `.mcp.json` and
  slash command wrappers.
- Added a PyPI release workflow for tagged releases.
- Added Homebrew formula template and release packaging notes.
- Added MCP round-trip tests and read-only XML eval prompts for a sanitized
  fixture workflow.
- Documented `pipx install "contractor-bid[mcp]"` and agent plugin setup.

## [0.1.0] - 2026-06-20

First public testing release. Early access — feedback and contributions encouraged.

- Added canonical CSI Division 03-33 starter coverage with whole-division profiles, example profiles, generated bid-scope skills, and a generator/check script.
- Added starter profiles, skills, and example profiles for `plumbing` (CSI Div 22), `hvac` (CSI Div 23), and `roofing` (CSI Div 07).
- Added a workspace-wide bid tracker (`track-add`, `track-update`, `track-move`, `track-reopen`, `track-list`, `track-build`) that writes `.contractor-bid/bid-tracker.json` and a two-sheet `Bid-Tracker.xlsx`, plus a `bid-tracker` skill that confirms with the user before each write.
- Added profile round-trip checks so generated starter skills stay aligned with profile JSON.
- Added suggested triage source files, scanned-PDF warnings, and faster Poppler text extraction.
- Added `list-profiles`, `status`, and `run` CLI commands.
- Added CI, issue templates, pull request template, and contributor test/lint instructions.
