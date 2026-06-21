# Security Policy

`contractor-bid` is a local-first Python CLI and optional stdio MCP server for building
source-backed commercial bid workspaces. It is not a hosted service, does not collect
credentials, and does not send bid documents, estimates, supplier quotes, or customer files
to ContractorKeith.

## Supported Versions

Security fixes are handled on the latest public release and the `main` branch.

| Version | Supported |
| --- | --- |
| Latest release | Yes |
| `main` | Yes |
| Older releases | Best effort |

## Reporting a Vulnerability

Please report suspected vulnerabilities privately. Do not open a public issue for security
reports.

Preferred path:

1. Use GitHub private vulnerability reporting or a private GitHub Security Advisory for
   `ContractorKeith/contractor-bid`.
2. Include the affected version or commit, reproduction steps, impact, and any safe proof of
   concept.
3. Do not attach proprietary bid documents, supplier quotes, customer files, credentials, or
   private estimates. Use a sanitized fixture whenever possible.

If private vulnerability reporting is not available, contact the maintainer through the
ContractorKeith GitHub profile and request a private reporting channel.

Expected handling:

- Initial acknowledgement target: 3 business days.
- Triage target: 7 business days.
- Fix target: as soon as practical, based on severity and release impact.
- Public disclosure: after a fix or mitigation is available, unless active exploitation
  requires a different timeline.

## Security Scope

In scope:

- Python CLI and library code in `src/contractor_bid/`.
- Optional MCP server entry point and tool behavior.
- Installer scripts in `scripts/`.
- GitHub workflows, package metadata, plugin metadata, profiles, skills, templates, and
  examples shipped by this repository.

Out of scope:

- Third-party services and package registries.
- User-generated bid workspaces, private PDFs, supplier quotes, estimates, or local tracker
  data.
- Vulnerabilities that require malicious local shell access with no additional impact.
- Social engineering, spam, or denial-of-service reports without a concrete code or
  dependency issue.

## Security Model

- Bid documents and generated packages stay on the user's machine unless the user chooses to
  share them.
- The MCP server runs over stdio for trusted local agents. Do not expose it as a public
  network service or connect it to untrusted agent clients.
- The CLI may read and write files inside user-selected bid project folders. Treat source PDFs
  and generated workbooks as sensitive business data.
- The tool does not require GitHub CLI, cloud credentials, API keys, or a database for normal
  use.

## Repository Security Controls

This repository uses:

- CI tests and linting on pull requests.
- CodeQL code scanning.
- Dependency review through Dependabot alerts and update pull requests.
- Python dependency vulnerability checks with `pip-audit`.
- Python static security checks with `bandit`.
- Secret-pattern checks for committed credentials.

Maintainers should keep generated bid artifacts, real customer files, private tracker data,
and local feedback logs out of commits.
