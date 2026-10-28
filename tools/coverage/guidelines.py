"""The text of one version's guideline skills, and how a framework item is looked up in it.

The text is cut into dotted words: runs of letters, digits, `_` and `.`, so that
`@api.depends('name')` gives `api.depends` and `env['ir.actions.server']` gives
`ir.actions.server`. A dotted word also yields each run of its parts (`odoo.fields.Char`
gives `fields.Char`), and every part after the first is an attribute (`records.search`
and `.search(` give `search`). Inline code is a name alone or called in backticks
(`` `Many2one` ``, `` `with_context(...)` ``). Fragments such as `<kanban` or
`auth='public'` are looked up in the raw text.
"""

from __future__ import annotations

from pathlib import Path

from .constants import GUIDELINE_SKILLS, SKIPPED_DOCUMENTS


class GuidelineText:
    def __init__(self, version_folder: Path) -> None:
        documents = [
            path
            for skill in GUIDELINE_SKILLS
            for path in sorted((version_folder / skill).rglob("*.md"))
            if path.name not in SKIPPED_DOCUMENTS
        ]
        self.text = "\n".join(path.read_text(encoding="utf-8") for path in documents)
        self.words: set[str] = set()
        self.attributes: set[str] = set()
        for word in self.dotted_words():
            self.index(word.split("."))

    def dotted_words(self) -> list[str]:
        kept = "".join(char if char.isalnum() or char in "_." else " " for char in self.text)
        return [word.rstrip(".") for word in kept.split() if word.strip(".")]

    def index(self, parts: list[str]) -> None:
        """Indexes one dotted word; a leading dot (`.search(`) makes its first part an attribute."""
        self.attributes.update(parts[1:])
        parts = [part for part in parts if part]
        for start in range(len(parts)):
            for end in range(start + 1, len(parts) + 1):
                self.words.add(".".join(parts[start:end]))

    def has_word(self, word: str) -> bool:
        return word in self.words

    def has_attribute(self, name: str) -> bool:
        return name in self.attributes

    def has_code(self, name: str) -> bool:
        return self.contains(f"`{name}`", f"`{name}(")

    def contains(self, *fragments: str) -> bool:
        return any(fragment in self.text for fragment in fragments)
