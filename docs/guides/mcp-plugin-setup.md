# MCP And Agent Plugin Setup

`contractor-bid` has two layers:

1. The Python engine: `contractor_bid` plus the `contractor-bid` CLI.
2. The agent integration: `contractor-bid-mcp`, plugin manifests, slash commands, and skills.

Install the engine once, then connect your agent to the MCP server.

## Engine Install

Recommended:

```bash
pipx install "contractor-bid[mcp]"
```

This installs both commands:

```bash
contractor-bid doctor
contractor-bid-mcp
```

For a development checkout:

```bash
python3 -m pip install -e ".[mcp]"
```

Set a default workspace root when you want agents to resolve short project names:

```bash
export CONTRACTOR_BID_WORKSPACE="$HOME/contractor-bid-workspace"
```

If the variable is not set, MCP tools resolve relative paths from the agent process working
directory.

## Claude Code

Add the repo as its own marketplace, then install the plugin:

```text
/plugin marketplace add ContractorKeith/contractor-bid
/plugin install contractor-bid@contractor-bid
```

The plugin uses the installed `contractor-bid-mcp` command from your PATH. It does not call
scripts from a cloned repo.

## Codex

Codex can reuse the same skills and MCP server. The repo includes
`codex-marketplace.json` with Codex policy fields for local or Git-hosted install flows.

Use the same engine install first:

```bash
pipx install "contractor-bid[mcp]"
```

Then point Codex at this repo or a local checkout and use `.mcp.json` to register
`contractor-bid-mcp`.

## Cursor

The repo includes `.cursor-plugin/plugin.json` for direct repo/community install flows. Cursor
marketplace submission is a separate review step and should not block the v0.2.0 release.

Install the engine first:

```bash
pipx install "contractor-bid[mcp]"
```

Then connect Cursor to the repo plugin and MCP server.

## MCP Tools

The server exposes these tools:

| Tool | Purpose |
|---|---|
| `cb_doctor` | Check Python and PDF dependencies. |
| `cb_list_profiles` | List built-in and workspace profiles. |
| `cb_new_project` | Scaffold a bid project folder from a profile. |
| `cb_triage` | Extract PDF text and score candidate scope/spec pages. |
| `cb_build_packets` | Build scope/spec PDFs and `00-Bid-Scope-Summary.md`. |
| `cb_build_workbook` | Build `01-Takeoff-Worksheet-REV1.xlsx`. |
| `cb_check` | Validate deliverables and write `ALERTS.md` by default. |
| `cb_package_sendoff` | Build the supplier/internal-review sendoff folder and zip. |
| `cb_learn` | Append a correction to the workspace feedback log. |
| `cb_track_add` | Propose or confirm adding a bid to the tracker. |
| `cb_track_update` | Propose or confirm updating a tracked bid. |
| `cb_track_move` | Propose or confirm archiving a tracked bid. |
| `cb_track_list` | List active and archived tracker bids. |

Every tool returns structured data with:

- `status`
- `artifacts`
- `summary`
- `alerts`
- `next_suggested_tool`
- `data`

Tracker write tools require `confirm=true` before writing. Without it, they return a proposed
change summary for the agent to show the user first.

## Inspector Check

Use MCP Inspector against the installed server:

```bash
npx @modelcontextprotocol/inspector contractor-bid-mcp
```

Run `cb_doctor`, `cb_list_profiles`, and then the fixture workflow in the test suite:

```bash
python3 -m unittest tests.test_mcp_server
```

## Current Gaps

- `contractor-bid init` remains CLI-only because interactive prompts are not a good MCP fit.
- OCR is not included yet. Scanned image-only PDFs need OCR before triage can read them.
- Homebrew publishing needs the release tarball SHA after the v0.2.0 tag is cut.
