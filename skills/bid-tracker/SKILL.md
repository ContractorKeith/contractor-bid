---
name: bid-tracker
description: Keep the workspace bid tracker current as the estimator works across bids. Use when a bid is started, its progress/next-action/due-date changes, it is submitted, or it is won/lost/completed. ALWAYS confirm with the user before writing.
---

# Bid Tracker

A single, easy-to-read spreadsheet of every bid in flight, plus an archive of finished ones.
It spans the whole workspace, not one project.

- **Source of truth:** `.contractor-bid/bid-tracker.json` (deterministic; edited only through the CLI).
- **Readable output:** `Bid-Tracker.xlsx` at the workspace root, regenerated after every change.
  - Sheet 1 **Active Bids** — Project, Location, Due, Progress, Next Action, Client / GC, Updated.
  - Sheet 2 **Archived & Completed** — Project, Location, Due, Outcome, Client / GC, Closed.
- Due dates within 2 days are amber, past-due are red. Progress/outcome cells are color-coded.
- When a bid is finished, it **moves** from Active to Archived — it is not duplicated.

## The permission rule (do not skip)

**Never write to the bid tracker silently.** Before running any tracker command that changes data
(`track-add`, `track-update`, `track-move`, `track-reopen`), you MUST:

1. Show the user a one-line **summary of the exact change** you intend to make.
2. **Wait for explicit confirmation** ("yes" / "go ahead"). If the user does not confirm, do not run it.
3. After running, repeat back the tool's confirmation line so the user sees what was written.

Read-only commands (`track-list`, `track-build`) do not require permission.

### Summary format to show before updating

```
Bid tracker update — please confirm:
  Bid:      <project name>
  Action:   add | update | move-to-archived | reopen
  Changes:  <field>: <old> → <new>   (one line per field)
  Result:   Active Bids / Archived & Completed
Proceed? (yes / no)
```

Example:

```
Bid tracker update — please confirm:
  Bid:      Riverside Plaza Fence
  Action:   update
  Changes:  Progress: Pricing → Submitted
            Next Action: Finish BOM → Follow up with GC Friday
  Result:   stays on Active Bids
Proceed? (yes / no)
```

## When to propose an update

Offer an update (then wait for confirmation) when:

- A new bid project is created (`contractor-bid new …`) → propose `track-add <project-folder>`.
- You learn the **due date**, location, or GC contact → propose `track-update`.
- Progress moves a stage: `New → Triage → Takeoff → Pricing → Submitted → Won/Lost/No-Bid`.
- The **next action** changes after triage, takeoff, a check run, or an RFI.
- The bid is **submitted** → set Progress `Submitted`.
- The bid is **won, lost, no-bid, or otherwise done** → propose `track-move --outcome …`
  (moves it to Archived & Completed).

## Commands

```bash
# Add from a bid project folder (pulls name, location, due, GC from project.json):
contractor-bid track-add bids/070126-riverside-plaza --progress Triage --next "Run triage"

# Add manually (no project folder yet):
contractor-bid track-add --name "Riverside Plaza Fence" --location "Tampa, FL" \
  --due "2026-07-01 14:00" --gc "Acme GC — John" --progress New

# Update fields on an existing bid (match by project name or id):
contractor-bid track-update "Riverside Plaza Fence" --progress Submitted --next "Follow up Friday"

# Finish a bid -> moves it to the Archived & Completed sheet:
contractor-bid track-move "Riverside Plaza Fence" --outcome won   # won | lost | no-bid | completed

# Bring an archived bid back to Active:
contractor-bid track-reopen "Riverside Plaza Fence"

# Read-only (no permission needed):
contractor-bid track-list            # active bids in the terminal
contractor-bid track-list --all      # include archived/completed
contractor-bid track-build           # just regenerate Bid-Tracker.xlsx
```

Run these from the workspace root (the folder holding `profiles/` and `.contractor-bid/`), or pass
`--root <workspace>`.

## Guardrails

- **Do not invent values.** Pull project name / location / due / GC from `project.json` or from what
  the user actually said. Leave a field blank rather than guessing.
- Keep "Progress" short — a single stage word — so the sheet stays readable on one screen.
- One bid = one row. Never duplicate a bid across both sheets; use `track-move` / `track-reopen`.
- The tracker holds the user's real bid pipeline (project names, GC contacts). It is gitignored;
  do not commit `Bid-Tracker.xlsx` or `.contractor-bid/bid-tracker.json`.
