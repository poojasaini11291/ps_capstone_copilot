from pathlib import Path

from src.validator import validate_markdown_file


def test_valid_markdown_file(tmp_path: Path):
    file_path = tmp_path / "valid.md"
    file_path.write_text("# Project Title\n\n## Overview\nThis is an overview.\n\n## Requirements\n- Must work", encoding="utf-8")

    is_valid, message = validate_markdown_file(file_path)

    assert is_valid is True
    assert message == "Valid markdown file"


def test_invalid_markdown_file_missing_section(tmp_path: Path):
    file_path = tmp_path / "invalid.md"
    file_path.write_text("# Project Title\n\n## Overview\nThis is an overview.\n", encoding="utf-8")

    is_valid, message = validate_markdown_file(file_path)

    assert is_valid is False
    assert "Missing required sections" in message


def test_invalid_markdown_file_missing_title(tmp_path: Path):
    file_path = tmp_path / "missing_title.md"
    file_path.write_text(
        "## Overview\nThis is an overview.\n\n## Requirements\n- Must work\n",
        encoding="utf-8",
    )

    is_valid, message = validate_markdown_file(file_path)

    assert is_valid is False
    assert "Missing title heading" in message


def test_invalid_markdown_file_empty_content(tmp_path: Path):
    file_path = tmp_path / "empty.md"
    file_path.write_text("", encoding="utf-8")

    is_valid, message = validate_markdown_file(file_path)

    assert is_valid is False
    assert "empty" in message.lower()


def test_missing_file_returns_error(tmp_path: Path):
    missing_file = tmp_path / "missing.md"

    is_valid, message = validate_markdown_file(missing_file)

    assert is_valid is False
    assert "File not found" in message
