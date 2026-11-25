#!/usr/bin/env python3
"""The One-Liner Groan-Off — one original dad joke, one line, max 140 chars."""

ENTRY = "The remote and I have a great relationship. It never argues \u2014 it just changes the subject."


def validate(text: str) -> None:
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 140):
        raise ValueError("entry must be 1-140 characters")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with white space")


def main() -> None:
    validate(ENTRY)
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("written entry does not match the entry in memory")


if __name__ == "__main__":
    main()
