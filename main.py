"""make.fun ai-happy-01 entry program.

Copies the picture bundled in this repository to the harness output
path as entry.png. Standard library only, no network, deterministic:
the same bytes come out on every run.
The picture was produced for this competition and is stored in the repo as entry.png.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
OUTPUT_NAME = "entry.png"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, OUTPUT_NAME))


if __name__ == "__main__":
    main()
