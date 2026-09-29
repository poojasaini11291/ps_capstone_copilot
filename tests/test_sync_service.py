from pathlib import Path

from src.sync_service import sync_valid_documents


def test_sync_valid_documents_copies_only_valid_files(tmp_path: Path):
    source_dir = tmp_path / "source"
    target_dir = tmp_path / "target"
    source_dir.mkdir()

    valid_file = source_dir / "good.md"
    valid_file.write_text(
        "# Project Title\n\n## Overview\nThis is an overview.\n\n## Requirements\n- Must work\n",
        encoding="utf-8",
    )

    invalid_file = source_dir / "bad.md"
    invalid_file.write_text("# Project Title\n\n## Overview\nMissing requirements.\n", encoding="utf-8")

    result = sync_valid_documents(source_dir, target_dir)

    assert result["copied_count"] == 1
    assert result["valid_files"] == ["good.md"]
    assert len(result["invalid_files"]) == 1
    assert (target_dir / "good.md").exists()
    assert not (target_dir / "bad.md").exists()


def test_sync_valid_documents_handles_missing_source_directory(tmp_path: Path):
    missing_dir = tmp_path / "missing" 
    target_dir = tmp_path / "target"

    result = sync_valid_documents(missing_dir, target_dir)

    assert result["copied_count"] == 0
    assert "Source directory does not exist or is not a directory." in result["invalid_files"][0]
