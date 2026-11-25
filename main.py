"""One-line out-of-office reply entry.

Writes a single funny OOO line to /output/entry.txt.
Self-contained: no external files, no network.
"""

import os

LINE = "Out of office until Monday. My laptop died, my phone is in rice, and my motivation is in witness protection."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
