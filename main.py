"""Pure Joy entry for make.fun ai-happy-01.

Delivers the bundled entry.png picture to the output directory,
byte for byte identical on every run. The picture: a laughing
child and a golden retriever puppy playing on green grass under
warm sunshine, confetti in the air, a rainbow behind them.
"""

import os
import shutil
from pathlib import Path


def main() -> None:
    """Copy entry.png next to this file into the output directory."""
    here = Path(__file__).resolve().parent
    source = here / "entry.png"
    if not source.is_file():
        raise FileNotFoundError(f"missing bundled image: {source}")

    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    destination = target_dir / "entry.png"
    shutil.copyfile(source, destination)
    print(f"wrote {destination} ({destination.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

# Deterministic: the same bundled picture lands in the output every run.
