"""One line of earned pride: writes the entry to /output/entry.txt."""

from pathlib import Path

LINE = "The boy who couldn't read at eight read his little sister to sleep tonight, one slow page at a time, without skipping a word."


def main() -> None:
    # Gate: the entry must be 1-240 characters of non-blank UTF-8 text.
    if not 1 <= len(LINE) <= 240 or not LINE.strip():
        raise ValueError("entry line must be 1-240 characters")
    Path("/output").mkdir(parents=True, exist_ok=True)
    Path("/output/entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
