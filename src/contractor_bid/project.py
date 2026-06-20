from __future__ import annotations

from pathlib import Path
from typing import Any

from .profile import render_skill
from .util import copy_template, slugify, today_iso, write_json


def ensure_workspace(root: Path) -> None:
    (root / ".contractor-bid").mkdir(parents=True, exist_ok=True)
    (root / "profiles").mkdir(exist_ok=True)
    (root / "skills").mkdir(exist_ok=True)
    config = root / ".contractor-bid" / "config.json"
    if not config.exists():
        write_json(
            config,
            {
                "schema_version": 1,
                "created": today_iso(),
                "profiles_dir": "profiles",
                "skills_dir": "skills",
                "default_project_root": ".",
            },
        )


def create_project(
    *,
    project_dir: Path,
    profile: dict[str, Any],
    project_name: str | None = None,
    bid_due: str | None = None,
    gc: str | None = None,
    address: str | None = None,
) -> list[Path]:
    project_dir.mkdir(parents=True, exist_ok=True)
    work = project_dir / "bid-package-working"
    takeoff = work / "takeoff"
    bid_docs = project_dir / "bid-docs"
    for folder in (bid_docs, work, takeoff):
        folder.mkdir(parents=True, exist_ok=True)

    (bid_docs / ".gitkeep").touch(exist_ok=True)

    slug = slugify(project_name or project_dir.name)
    display_name = project_name or project_dir.name
    replacements = {
        "{{PROJECT_NAME}}": display_name,
        "{{TRADE_NAME}}": profile["trade_name"],
        "{{COMPANY_NAME}}": profile["company_name"],
        "{{SCOPE_RULE}}": profile["scope_rule"],
        "{{BID_DUE}}": bid_due or "TBD",
        "{{GC}}": gc or "TBD",
        "{{ADDRESS}}": address or "TBD",
        "{{PREPARED_DATE}}": today_iso(),
        "{{PROFILE_ID}}": profile["profile_id"],
    }

    copy_template("project-readme-template.md", project_dir / "README.md", replacements)
    copy_template(
        "00-scope-reference-index-template.md",
        work / "00-Scope-Reference-Index.md",
        replacements,
    )
    copy_template("02-proposal-letter-template.md", work / "02 - Proposal Letter.md", replacements)
    copy_template(
        "scope-pages-sources-template.json",
        takeoff / "scope-pages-sources.json",
        replacements,
    )
    copy_template("takeoff-template.json", takeoff / f"{slug}.json", replacements)
    copy_template("review-pages-template.md", takeoff / "review-pages.md", replacements)

    write_json(
        project_dir / "project.json",
        {
            "schema_version": 1,
            "project_name": display_name,
            "project_slug": slug,
            "bid_due": bid_due or "",
            "gc": gc or "",
            "address": address or "",
            "scope_profile": profile["profile_id"],
            "created": today_iso(),
        },
    )

    skill_dir = project_dir / ".agent" / "skills" / f"{profile['profile_id']}-bid-scope"
    skill_dir.mkdir(parents=True, exist_ok=True)
    (skill_dir / "SKILL.md").write_text(render_skill(profile), encoding="utf-8")

    return [
        bid_docs,
        work / "00-Scope-Reference-Index.md",
        work / "02 - Proposal Letter.md",
        takeoff / "scope-pages-sources.json",
        takeoff / f"{slug}.json",
        project_dir / "project.json",
        skill_dir / "SKILL.md",
    ]
