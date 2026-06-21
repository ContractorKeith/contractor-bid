# Documentation Plan

This docs site is organized around the questions a new subcontractor or agent builder is
likely to ask.

## Current Information Architecture

- Start Here: install, quick start, and first-bid walkthrough.
- Concepts: what the package produces and how reusable corrections work.
- Guides: the full bid workflow and agent/MCP setup.
- Reference: commands, CSI division starters, and security posture.
- Troubleshooting: common install, PDF, scope, workbook, and deploy problems.

## Near-Term Improvements

- Add screenshots of a generated bid workspace using sanitized fixture data.
- Add a complete sample project with fake PDFs and expected outputs.
- Generate the command reference from `argparse` so docs cannot drift from the CLI.
- Add separate pages for custom profile creation and bid tracker operations.
- Add a maintainer checklist for release docs updates.

## Documentation Rules

- Keep source-backed review boundaries explicit.
- Do not imply that triage output is final scope.
- Keep base bid, alternates, exclusions, and review-only scopes separate.
- Prefer repeatable commands and generated artifacts over conversational examples.
- Do not use real customer documents, supplier quotes, or private estimates in examples.
