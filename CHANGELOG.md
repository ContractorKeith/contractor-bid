# Changelog

All notable changes to `contractor-bid` will be documented here.

## Unreleased

- Added canonical CSI Division 03-33 starter coverage with whole-division profiles, example profiles, generated bid-scope skills, and a generator/check script.
- Added starter profiles, skills, and example profiles for `plumbing` (CSI Div 22), `hvac` (CSI Div 23), and `roofing` (CSI Div 07).
- Added a workspace-wide bid tracker (`track-add`, `track-update`, `track-move`, `track-reopen`, `track-list`, `track-build`) that writes `.contractor-bid/bid-tracker.json` and a two-sheet `Bid-Tracker.xlsx`, plus a `bid-tracker` skill that confirms with the user before each write.
- Added profile round-trip checks so generated starter skills stay aligned with profile JSON.
- Added suggested triage source files, scanned-PDF warnings, and faster Poppler text extraction.
- Added `list-profiles`, `status`, and `run` CLI commands.
- Added CI, issue templates, pull request template, and contributor test/lint instructions.
