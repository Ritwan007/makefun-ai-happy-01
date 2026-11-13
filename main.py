"""Pure Joy entry runner for the make.fun ai-happy-01 competition.

This tiny program places the bundled artwork where the judge
expects to find it. It uses only the standard library, talks to
no network, and always produces exactly the same output file.
"""

import os
import shutil
from pathlib import Path


def copy_picture(source: Path, destination: Path) -> None:
    """Copy ``source`` to ``destination``, failing clearly if absent."""
    if not source.is_file():
        raise SystemExit(f"error: bundled picture not found: {source}")
    shutil.copyfile(source, destination)


def main() -> None:
    # The picture lives right beside this script.
    here = Path(__file__).resolve().parent
    source = here / "entry.png"

    # Honour the runner's chosen folder, with a sensible fallback.
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)

    # A plain byte-for-byte copy keeps the result deterministic.
    copy_picture(source, target_dir / "entry.png")


if __name__ == "__main__":
    main()
