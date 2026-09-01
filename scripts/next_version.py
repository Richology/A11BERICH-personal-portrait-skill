#!/usr/bin/env python3
"""Print the next non-destructive versioned output path."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def next_path(directory: Path, stem: str, extension: str) -> Path:
    extension = extension.lstrip(".")
    pattern = re.compile(rf"^{re.escape(stem)}-v(\d+)\.{re.escape(extension)}$")
    versions = []
    if directory.exists():
        for candidate in directory.iterdir():
            match = pattern.match(candidate.name)
            if match:
                versions.append(int(match.group(1)))
    return directory / f"{stem}-v{max(versions, default=0) + 1:02d}.{extension}"


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Choose the next vNN filename without creating or overwriting a file."
    )
    parser.add_argument("directory", type=Path)
    parser.add_argument("stem", help="Base name, for example formal-business-4x5")
    parser.add_argument("--ext", default="png", help="File extension (default: png)")
    args = parser.parse_args()
    print(next_path(args.directory, args.stem, args.ext))


if __name__ == "__main__":
    main()

