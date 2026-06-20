# Contributing

Thanks for helping improve `contractor-bid`.

This project exists to make commercial subcontractor bid workflows more repeatable and easier for AI agents to work inside. Contributions should preserve that purpose: clear scope boundaries, source-backed outputs, deterministic scripts, and practical documents an estimator can review.

## Good First Contributions

- Improve starter scope profiles.
- Add a new CSI trade profile and matching skill.
- Improve README examples or diagrams.
- Add validation checks for common scope drift.
- Improve installer reliability across macOS, Linux, and Windows.
- Add tests around CLI commands and generated project structure.

Do not commit proprietary bid documents, customer names, private estimates, supplier quotes, or screenshots from private plan rooms.

## Local Setup

```bash
git clone https://github.com/ContractorKeith/contractor-bid.git
cd contractor-bid
python3 -m venv .venv
. .venv/bin/activate
pip install -e .
```

Recommended PDF tools:

```bash
brew install poppler
```

On Linux, install `poppler-utils` through your package manager. On Windows, use the installer script or install Poppler with `winget` or Chocolatey.

Check your environment:

```bash
contractor-bid doctor
```

## Test Before Opening A PR

```bash
PYTHONPATH=src python3 -m compileall src tests
PYTHONPATH=src python3 -m unittest discover -s tests -v
bash -n scripts/install.sh
git diff --check
```

If you change package data, run the installer into a temporary location:

```bash
tmp_home=$(mktemp -d)
tmp_bin=$(mktemp -d)
CONTRACTOR_BID_HOME="$tmp_home" CONTRACTOR_BID_BIN="$tmp_bin" scripts/install.sh
"$tmp_bin/contractor-bid" doctor
```

## Adding A Scope Profile

Add both files:

- `profiles/<profile-id>.json`
- `skills/<profile-id>-bid-scope/SKILL.md`

The profile should define:

- `trade_name`
- `csi_divisions`
- `scope_rule`
- `base_scope`
- `include_terms`
- `spec_sections`
- `quantity_units`
- `review_terms`
- `exclude_terms`
- `proposal_exclusions`

Keep built-in profiles generic. Company-specific rules belong in a user's workspace profile, not in the public starter profile.

## Pull Request Expectations

- Explain what changed and why.
- Include test output or explain why a check could not be run.
- Keep generated binary files out of the repo unless they are intentional public assets.
- Preserve public-safe examples. Use sanitized or fictional project names.
- Keep `AGENTS.md` as the canonical agent workflow. `CLAUDE.md` should stay a compatibility pointer.

## Project Boundaries

`contractor-bid` should help create a reviewable bid package. It should not claim to produce final pricing, legal review, code compliance, or contract acceptance without a qualified person reviewing the work.
