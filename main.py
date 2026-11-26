"""Front-page delivery for the 26 November 2026 news image.

What this program does, when the grader runs it:

1. Loads the bundled front page (``entry.png`` sitting next to this file).
2. Checks it is a real, whole PNG: correct magic bytes, an IHDR chunk
   declaring 1024x1024, and a closing IEND chunk.
3. Checks its SHA-256 against the digest pinned below, so a damaged or
   swapped image can never be reported as a success.
4. Writes the exact bytes to ``$MAKEFUN_OUTPUT_DIR/entry.png``
   (default ``/output``) and checks the written copy the same way.

Only the Python standard library is used. There is no network access,
no command-line parsing and no randomness: the same input always
produces the same output file.
"""

import hashlib
import os
import struct
import sys
from pathlib import Path

# The directory this file lives in, and the image bundled with it.
HERE = Path(__file__).resolve().parent
BUNDLED_IMAGE = HERE / "entry.png"

# Where the finished image goes. The grader sets MAKEFUN_OUTPUT_DIR;
# running by hand without it writes to /output.
TARGET_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
TARGET_NAME = "entry.png"

# The page the generator drew on 2026-11-26: 1024x1024, 164,003 bytes.
PAGE_WIDTH = 1024
PAGE_HEIGHT = 1024
PAGE_BYTES = 164003
PAGE_SHA256 = "3ca6d042d7104483f827aa1b6eda3b325f61fcd173ccf2a5a2eec9b832c13571"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
IEND_TAIL = b"IEND\xaeB`\x82"


class PageProblem(Exception):
    """Raised when the bundled image fails any check."""


def sha256_hex(data):
    """Hex digest of a bytes object."""
    return hashlib.sha256(data).hexdigest()


def check_png_bytes(data, label):
    """Raise PageProblem unless data is a whole 1024x1024 PNG.

    Checks, in order: the magic bytes, the IHDR chunk and its declared
    size, the closing IEND chunk, the total byte count and the digest.
    The first failing check raises, so a truncated file and a swapped
    file are told apart by the message.
    """
    if not data.startswith(PNG_MAGIC):
        raise PageProblem(f"{label}: not a PNG (bad magic bytes)")
    if len(data) < 33 or data[12:16] != b"IHDR":
        raise PageProblem(f"{label}: no IHDR chunk where one belongs")
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (PAGE_WIDTH, PAGE_HEIGHT):
        raise PageProblem(
            f"{label}: size {width}x{height}, want "
            f"{PAGE_WIDTH}x{PAGE_HEIGHT}"
        )
    if not data.endswith(IEND_TAIL):
        raise PageProblem(f"{label}: no IEND chunk at the end")
    if len(data) != PAGE_BYTES:
        raise PageProblem(
            f"{label}: {len(data)} bytes, want {PAGE_BYTES}"
        )
    if sha256_hex(data) != PAGE_SHA256:
        raise PageProblem(f"{label}: digest does not match the pinned one")


def deliver():
    """Copy the bundled page to the output directory, verified twice."""
    raw = BUNDLED_IMAGE.read_bytes()
    check_png_bytes(raw, "bundled entry.png")

    TARGET_DIR.mkdir(parents=True, exist_ok=True)
    destination = TARGET_DIR / TARGET_NAME
    destination.write_bytes(raw)

    check_png_bytes(destination.read_bytes(), f"placed {destination}")
    print(
        f"wrote {destination} ({len(raw)} bytes, "
        f"{PAGE_WIDTH}x{PAGE_HEIGHT})"
    )
    return 0


def main():
    try:
        return deliver()
    except PageProblem as problem:
        print(f"error: {problem}", file=sys.stderr)
        return 1
    except OSError as problem:
        print(f"error: cannot read or write the image: {problem}",
              file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
