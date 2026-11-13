"""Pure Joy entry for make.fun ai-happy-01.

Copies the bundled entry.png image to the configured output
directory, preserving the exact bytes on every run.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    """Deliver entry.png to the output directory."""
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"missing bundled image: {source}")

    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.png"
    shutil.copyfile(source, destination)


if __name__ == "__main__":
    main()

# Deterministic delivery: same input file, same output bytes.
