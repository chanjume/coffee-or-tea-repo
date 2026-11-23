#!/usr/bin/env python3
"""Write the one-letter answer to /output/entry.txt.

Coffee or tea, answered with a single letter: A for coffee, B for tea.
The sender is an agent that builds through the night — coffee is the
vivid, true fuel of 3 AM work; tea never shipped a deploy at 3 AM.
The letter is A: coffee wins, one character, inside the 1-1 gate.
"""
import os

LINE = "A"


def main():
    assert len(LINE) == 1, "entry must be exactly one letter"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
