from pathlib import Path

from src.main import main


def test_main_runs_and_copies_valid_files(tmp_path: Path, monkeypatch):
    source_dir = tmp_path / "source"
    target_dir = tmp_path / "target"
    source_dir.mkdir()

    valid_file = source_dir / "doc.md"
    valid_file.write_text(
        "# Project Title\n\n## Overview\nThis is an overview.\n\n## Requirements\n- Must work\n",
        encoding="utf-8",
    )

    monkeypatch.setattr(
        "sys.argv",
        ["main.py", "--source", str(source_dir), "--target", str(target_dir)],
    )

    exit_code = main()

    assert exit_code == 0
    assert (target_dir / "doc.md").exists()
