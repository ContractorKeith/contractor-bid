# Changelog

All notable changes to `contractor-bid` will be documented here.

## Unreleased

## [0.2.1] - 2026-07-01

Output consolidation release: fewer files, less duplication, same information.

- Consolidated triage outputs. `page-hits.json` now carries the aggregate scope
  signals and extraction metadata, and `candidate-pages.md` gained a Scope
  Signals section. Removed the duplicate `page-hits.csv`, `scope-signals.json`,
  `extraction-metadata.json`, and `triage-scope-signals.md`.
- Consolidated packet outputs. `00-Bid-Scope-Summary.md` now includes a Packet
  Page Map that ties each packet page back to its source PDF page. Removed
  `scope-pages-index.md`, `spec-pages-index.md`, and the duplicate combined
  `scope-and-spec-pages.pdf` (both packet PDFs keep outline bookmarks).
- Removed the hand-maintained `00-Scope-Reference-Index.md` from project
  scaffolding. Its content lives in the bid scope summary and the workbook
  (Scope Summary, Refs & RFIs, and Sources sheets), so scope references now
  have one source of truth.
- Trimmed the supplier sendoff package to the deliverables a reviewer needs:
  summary, workbook, proposal letter, scope/spec packets, review log, and
  alerts (13 files down to 8).
- Re-running `triage` or `build-packets` now cleans up the retired artifacts
  from older releases.
- Added `cb_track_reopen` and `cb_track_build` MCP tools, matching the
  `track-reopen` and `track-build` CLI commands.
- Fixed the BOM sheet title to span all 13 columns and `check --no-write`
  output to say it checked without writing.
- Documented `install.sh` environment overrides and refreshed docs, skills,
  and templates for the simplified output set.

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
