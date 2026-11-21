#!/usr/bin/env python3
"""Write one short, steadying text to /output/entry.txt.

The text is a small scene: a lighthouse keeper doing the same quiet
work he has done every dusk for thirty years. Nothing in it tells the
reader to relax; the calm is in the rhythm, the plain words, and the
light that goes on without hurrying.
"""

import os
from pathlib import Path

TEXT = (
    "The keeper trims the lamp at dusk, the same small work as every "
    "dusk for thirty years. Out there the sea does what it does. "
    "In here: oil, glass, a steady hand. The light goes on. "
    "It has never once needed to hurry to be seen."
)


def main() -> None:
    # The entry must be 1-280 Unicode characters and not only whitespace.
    assert 1 <= len(TEXT) <= 280 and TEXT.strip(), "entry text out of bounds"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
