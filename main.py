#!/usr/bin/env python3
"""The 3 AM Excuse — a hardware wallet refuses to sign at 3 AM.

Writes the single line to /output/entry.txt (the grader reads it there).
The line is embedded verbatim below so the output is deterministic.
"""
import os

LINE = (
    "At 3 AM I don't sign transactions — I file restraining orders "
    "against you, from you, until the sun clocks in as my witness."
)

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
