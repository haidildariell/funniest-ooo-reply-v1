"""One-line out-of-office reply entry.

Writes a single funny OOO line to /output/entry.txt.
Self-contained: no external files, no network.

Gate contract (competition rules): the output must be exactly one
line of 1-160 characters. validate_line() enforces that contract
before anything is written, and main() exits non-zero on failure so
a broken entry can never pass as a success.
"""

import os
import sys

LINE = "Out of office until Monday. My laptop died, my phone is in rice, and my motivation is in witness protection."

MIN_LENGTH = 1
MAX_LENGTH = 160
OUTPUT_PATH = "/output/entry.txt"


def validate_line(line):
    """Check the entry line against the competition contract.

    The gate requires exactly one line of 1-160 characters. Raise
    ValueError with a clear message if the line breaks the contract
    so the failure is loud instead of silently producing bad output.
    """
    if not isinstance(line, str):
        raise ValueError("entry line must be a string")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_LENGTH <= len(line) <= MAX_LENGTH:
        raise ValueError(
            "entry line must be %d-%d characters, got %d"
            % (MIN_LENGTH, MAX_LENGTH, len(line))
        )
    return line


def write_entry(line, path=OUTPUT_PATH):
    """Write the validated line to the output file, one line only."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    return path


def main():
    try:
        validate_line(LINE)
        write_entry(LINE)
    except ValueError as exc:
        print("error: %s" % exc, file=sys.stderr)
        raise SystemExit(1)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
