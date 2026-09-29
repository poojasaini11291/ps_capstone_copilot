from __future__ import annotations

from pathlib import Path

REQUIRED_HEADINGS = [
    "# ",
    "## Overview",
    "## Requirements",
]


def validate_markdown_file(file_path: str | Path) -> tuple[bool, str]:
    """Validate that a markdown file includes the required sections."""
    path = Path(file_path)

    if not path.exists():
        return False, f"File not found: {path}"

    if path.is_dir():
        return False, f"Expected a file, got a directory: {path}"

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return False, f"Unable to read file '{path}': {exc}"

    if not content.strip():
        return False, "File is empty"

    missing = []
    if not any(line.startswith("# ") for line in content.splitlines()):
        missing.append("Missing title heading")

    for heading in ("## Overview", "## Requirements"):
        if heading not in content:
            missing.append(f"Missing required section: {heading}")

    if missing:
        if len(missing) == 1 and missing[0].startswith("Missing required section:"):
            return False, f"Missing required sections: {missing[0].split(': ', 1)[1]}"
        if len(missing) == 1 and missing[0] == "Missing title heading":
            return False, "Missing title heading"
        return False, "; ".join(["Missing required sections", *missing])

    return True, "Valid markdown file"


def list_markdown_files(source_dir: str | Path) -> list[Path]:
    """Return all markdown files in a directory."""
    source_path = Path(source_dir)
    if not source_path.exists():
        return []
    if not source_path.is_dir():
        return []

    return sorted(
        [file for file in source_path.iterdir() if file.is_file() and file.suffix.lower() == ".md"],
        key=lambda p: p.name,
    )
