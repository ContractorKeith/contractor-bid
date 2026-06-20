from __future__ import annotations

import json
import re
from datetime import date, datetime
from pathlib import Path
from typing import Any


PACKAGE_DIR = Path(__file__).resolve().parent
PACKAGE_ROOT = Path(__file__).resolve().parents[2]


def templates_dir() -> Path:
    for candidate in resource_dirs("templates"):
        if candidate.exists():
            return candidate
    return PACKAGE_ROOT / "templates"


def resource_dirs(name: str) -> list[Path]:
    return [
        PACKAGE_ROOT / name,
        PACKAGE_DIR / name,
    ]


def slugify(text: str, default: str = "project") -> str:
    slug = re.sub(r"[^A-Za-z0-9]+", "-", text).strip("-").lower()
    return slug or default


def today_iso() -> str:
    return date.today().isoformat()


def now_iso() -> str:
    return datetime.now().replace(microsecond=0).isoformat()


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def rel_display(path: Path, base: Path) -> str:
    try:
        return str(path.relative_to(base))
    except ValueError:
        return str(path)


def copy_template(src_name: str, dst: Path, replacements: dict[str, str] | None = None) -> None:
    src = templates_dir() / src_name
    text = src.read_text(encoding="utf-8")
    for key, value in (replacements or {}).items():
        text = text.replace(key, value)
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(text, encoding="utf-8")


def append_jsonl(path: Path, item: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(item, ensure_ascii=False) + "\n")


def markdown_table(headers: list[str], rows: list[list[Any]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        cleaned = [str(value).replace("\n", " ").replace("|", "\\|") for value in row]
        lines.append("| " + " | ".join(cleaned) + " |")
    return lines


def coerce_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        return [value] if value.strip() else []
    return [value]
