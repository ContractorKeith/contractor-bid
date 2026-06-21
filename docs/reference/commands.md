# Command Reference

Run:

```bash
contractor-bid --help
```

to see the current CLI surface.

## Setup And Discovery

| Command | Purpose |
|---|---|
| `contractor-bid doctor` | Check Python package, optional PDF tools, and local environment. |
| `contractor-bid list-profiles` | List built-in and workspace scope profiles. |
| `contractor-bid init` | Create a reusable custom profile and matching bid-scope skill. |

## Bid Project Pipeline

| Command | Purpose |
|---|---|
| `contractor-bid new <project> --profile <profile>` | Scaffold a bid project. |
| `contractor-bid triage <project> --profile <profile> --render` | Extract PDF text, score likely scope/spec pages, and optionally render candidate page images. |
| `contractor-bid build-packets <project>` | Build scope/spec packet PDFs and `00-Bid-Scope-Summary.md` from approved source pages. |
| `contractor-bid build-workbook <project> --profile <profile>` | Build `01-Takeoff-Worksheet-REV1.xlsx` from takeoff JSON. |
| `contractor-bid check <project> --profile <profile>` | Validate required artifacts, due date, addenda, and scope guardrails. |
| `contractor-bid status <project> --profile <profile>` | Show readiness without writing `ALERTS.md`. |
| `contractor-bid package-sendoff <project>` | Build the supplier/internal-review sendoff folder and zip. |
| `contractor-bid run <project> --profile <profile>` | Rebuild packets, workbook, alerts, and sendoff after human-filled source/takeoff files are ready. |

## Learning And Corrections

| Command | Purpose |
|---|---|
| `contractor-bid learn --note "..."` | Record a correction or lesson in the workspace feedback log. |

Only turn a correction into a durable profile or script rule after confirming it should apply
beyond the current bid.

## Bid Tracker

| Command | Purpose |
|---|---|
| `contractor-bid track-add` | Add or update a bid in the workspace tracker. |
| `contractor-bid track-update` | Update fields on a tracked bid. |
| `contractor-bid track-move` | Move a bid to archived/completed. |
| `contractor-bid track-reopen` | Reopen an archived bid. |
| `contractor-bid track-list` | List active and optionally archived bids. |
| `contractor-bid track-build` | Regenerate `Bid-Tracker.xlsx` from tracker JSON. |

Tracker source data is stored in `.contractor-bid/bid-tracker.json`; the readable spreadsheet
is `Bid-Tracker.xlsx`. Both are ignored by the public repo because they can contain real bid
pipeline data.

!!! warning "Agent confirmation rule"
    Agents should show a one-line tracker change summary and wait for user confirmation before
    running tracker write commands.
