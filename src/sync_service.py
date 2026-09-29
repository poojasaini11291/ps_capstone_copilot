from __future__ import annotations

import shutil
from pathlib import Path

from src.validator import validate_markdown_file


def sync_valid_documents(source_dir: str | Path, target_dir: str | Path) -> dict:
    """Validate all markdown files and copy valid files to the target directory."""
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    if not source_path.exists() or not source_path.is_dir():
        return {
            "source_dir": str(source_path),
            "target_dir": str(target_path),
            "valid_files": [],
            "invalid_files": ["Source directory does not exist or is not a directory."],
            "copied_count": 0,
        }

    target_path.mkdir(parents=True, exist_ok=True)

    valid_files: list[str] = []
    invalid_files: list[str] = []

    for file_path in sorted(source_path.iterdir(), key=lambda item: item.name):
        if not file_path.is_file() or file_path.suffix.lower() != ".md":
            continue

        is_valid, message = validate_markdown_file(file_path)
        if not is_valid:
            invalid_files.append(f"{file_path.name}: {message}")
            continue

        destination = target_path / file_path.name
        shutil.copy2(file_path, destination)
        valid_files.append(file_path.name)

    return {
        "source_dir": str(source_path),
        "target_dir": str(target_path),
        "valid_files": valid_files,
        "invalid_files": invalid_files,
        "copied_count": len(valid_files),
    }
