from __future__ import annotations

from pathlib import Path
from typing import Any

from .util import append_jsonl, now_iso


def record_feedback(
    root: Path,
    *,
    note: str,
    project: str | None = None,
    profile_id: str | None = None,
    category: str = "correction",
) -> Path:
    item: dict[str, Any] = {
        "timestamp": now_iso(),
        "category": category,
        "note": note,
    }
    if project:
        item["project"] = project
    if profile_id:
        item["profile_id"] = profile_id
    path = root / ".contractor-bid" / "feedback.jsonl"
    append_jsonl(path, item)

    lessons = root / ".contractor-bid" / "LESSONS.md"
    if not lessons.exists():
        lessons.write_text(
            "# Contractor Bid Lessons\n\n"
            "Agent instruction: review these corrections before starting a similar bid. "
            "When a correction should become permanent, update the scope profile, regenerated skill, "
            "templates, or scripts in a normal commit.\n\n",
            encoding="utf-8",
        )
    with lessons.open("a", encoding="utf-8") as fh:
        project_part = f" [{project}]" if project else ""
        profile_part = f" ({profile_id})" if profile_id else ""
        fh.write(f"- {item['timestamp']}{project_part}{profile_part}: {note}\n")
    return path
