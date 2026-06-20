# Skills

Built-in starter skills live here for the included starter profiles.

Each scope skill mirrors a profile and gives Claude, Codex, or another agent the scope boundary, review terms, exclusion terms, and bid workflow for that subcontractor trade. The canonical CSI starters use `division-XX-*-bid-scope` names and cover every active MasterFormat division from 03 through 33.

Run `contractor-bid init` to generate a custom skill from a custom profile.

Run `python3 scripts/generate-csi-starters.py --check` from the repo root to verify the committed CSI starter profiles, examples, and skills are in sync.

## Workflow skills

- `bid-tracker` — keep the workspace-wide bid pipeline (`Bid-Tracker.xlsx`) current as the estimator works. Requires the agent to confirm with the user and show a change summary before every write.
