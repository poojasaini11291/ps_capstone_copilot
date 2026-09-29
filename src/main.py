from __future__ import annotations

import argparse

from src.sync_service import sync_valid_documents


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate and sync Markdown documentation files.")
    parser.add_argument("--source", required=True, help="Source directory containing Markdown files")
    parser.add_argument("--target", required=True, help="Target directory for valid files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = sync_valid_documents(args.source, args.target)

    print(f"Source directory: {result['source_dir']}")
    print(f"Target directory: {result['target_dir']}")
    print(f"Copied files: {result['copied_count']}")

    if result["valid_files"]:
        print("Valid files:")
        for name in result["valid_files"]:
            print(f"- {name}")

    if result["invalid_files"]:
        print("Invalid files:")
        for message in result["invalid_files"]:
            print(f"- {message}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
