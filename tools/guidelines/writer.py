"""Writes the files of one version's skills."""

from __future__ import annotations

from pathlib import Path

from .constants import SHOWS_TYPOGRAPHIC, TYPOGRAPHIC


class SkillWriter:
    def __init__(self, root: Path) -> None:
        self.root = root

    def write(self, relative: str, text: str) -> None:
        """One file, ending in a single newline; refused if it holds typographic punctuation."""
        path = self.root / relative
        text = text.strip("\n") + "\n"
        found = [mark for mark in TYPOGRAPHIC if mark in text]
        if found and path.name != SHOWS_TYPOGRAPHIC:
            raise SystemExit(f"typographic punctuation {found} in {path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text)
