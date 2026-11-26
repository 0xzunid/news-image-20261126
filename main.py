"""26 November 2026 news-image entry.

The grader runs this file. It places the front page bundled with this
repository (``entry.png``) into the output directory
(``$MAKEFUN_OUTPUT_DIR``, default ``/output``) and then proves the
placed file is the real thing: its PNG header must read 1024x1024 and
its SHA-256 must equal the pinned digest of the bundled image.

Python standard library only. No network, no arguments, no randomness.
"""

import hashlib
import os
import shutil
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLED = ROOT / "entry.png"
OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
WANT_DIMS = (1024, 1024)
# SHA-256 of entry.png as drawn on 2026-11-26. A damaged or swapped
# bundled image is caught here before anything is reported as done.
ENTRY_DIGEST = "3ca6d042d7104483f827aa1b6eda3b325f61fcd173ccf2a5a2eec9b832c13571"


def digest_of(path):
    """Hex SHA-256 of a file, read in 64 KiB chunks."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            chunk = fh.read(1 << 16)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def ihdr_dims(path):
    """(width, height) from the PNG IHDR chunk, or None if not a PNG."""
    with open(path, "rb") as fh:
        head = fh.read(33)
    if len(head) < 33 or head[:8] != b"\x89PNG\r\n\x1a\n":
        return None
    if head[12:16] != b"IHDR":
        return None
    return struct.unpack(">II", head[16:24])


def digests_match(placed):
    """True when both the placed copy and the bundle match the pinned digest."""
    if digest_of(placed) != ENTRY_DIGEST:
        print("placed copy digest mismatch", file=sys.stderr)
        return False
    if digest_of(BUNDLED) != ENTRY_DIGEST:
        print("bundled image digest mismatch", file=sys.stderr)
        return False
    return True


def confirm_written(placed):
    """True when the placed copy is a genuine 1024x1024 copy of the bundle.

    Header size first, then the digests, so a damaged bundle fails here too.
    """
    dims = ihdr_dims(placed)
    if dims != WANT_DIMS:
        print(f"bad size {dims}, expected {WANT_DIMS}", file=sys.stderr)
        return False
    return digests_match(placed)


def place_entry():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    placed = OUT_DIR / "entry.png"
    shutil.copyfile(BUNDLED, placed)

    if not confirm_written(placed):
        return 1

    print(f"wrote {placed} ({placed.stat().st_size} bytes, "
          f"{WANT_DIMS[0]}x{WANT_DIMS[1]})")
    return 0


if __name__ == "__main__":
    raise SystemExit(place_entry())
