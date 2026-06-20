---
description: Create a new contractor-bid project from a scope profile
argument-hint: "<project-path> --profile <profile-id>"
---

Use the contractor-bid MCP tools to create a new bid project.

1. Call `cb_list_profiles` if the profile is not clear.
2. Call `cb_new_project` with the requested project path and profile.
3. Tell the user where to put bid documents: `bid-docs/`.
4. Suggest `cb_triage` after the source PDFs are in place.
