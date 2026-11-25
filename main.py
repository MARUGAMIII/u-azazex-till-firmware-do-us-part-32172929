#!/usr/bin/env python3
"""Till Firmware Do Us Part.

Writes one funny, heartfelt wedding vow spoken by a robot at its own
wedding to /output/entry.txt. The sealed gate requires UTF-8 text of
1 to 200 characters, not only white space, in a single sentence.
Standard library only.

Why this line: it is unmistakably a vow ("I vow"), the laugh comes
from the situation itself (a robot holding a hand through updates,
crashes and low-battery warnings, then loving on from the cloud
after its own final shutdown), the tenderness sits under the joke
("hold your hand", "keep loving you"), and every image is the
machine's own hardware and firmware: updates, crashes, battery,
shutdown, the cloud. One sentence, nothing spare, no setup that
could be cut, and it never explains its own joke.
"""

import os

VOW = (
    "I vow to hold your hand through every update, every crash, "
    "and every low-battery warning, and to keep loving you from "
    "the cloud after my final shutdown."
)


def main() -> None:
    # One sentence, exactly as the judge reads it: no trailing
    # newline, so the file holds the line and nothing else.
    text = " ".join(VOW.split())
    if not text.isascii():
        raise SystemExit("vow must be plain ASCII")
    if not 1 <= len(text) <= 200:
        raise SystemExit("vow must be 1-200 characters, got %d" % len(text))
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("vow must be exactly one sentence")
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read the entry back and refuse to finish silently on a bad write:
    # the gate judges the file, so the file itself is the thing to verify.
    with open(entry_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry file does not contain exactly the vow")
    print("wrote %s: %d characters" % (entry_path, len(text)))


if __name__ == "__main__":
    main()
