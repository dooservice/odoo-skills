"""The opening block of a guideline file: what matters most in the version, then its sections."""

from __future__ import annotations

from pathlib import Path
from string import Template

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion


class HeadingAnchor:
    """The anchor GitHub gives a Markdown heading: lowercase, spaces as hyphens, other punctuation dropped."""

    def __init__(self, title: str) -> None:
        self.title = title

    def slug(self) -> str:
        kept = [character for character in self.title.lower() if character.isalnum() or character in "-_ "]
        return "".join(kept).replace(" ", "-")


class SectionIndex:
    """The headings of one level in a Markdown text, outside code blocks, as a list of links."""

    def __init__(self, text: str, level: int) -> None:
        self.text = text
        self.marker = "#" * level + " "

    def titles(self) -> list[str]:
        titles = []
        fenced = False
        for line in self.text.splitlines():
            if line.lstrip().startswith("```"):
                fenced = not fenced
            elif not fenced and line.startswith(self.marker):
                titles.append(line.removeprefix(self.marker).strip())
        return titles

    def markdown(self) -> str:
        links = [f"- [{title}](#{HeadingAnchor(title).slug()})" for title in self.titles()]
        return "Sections of this file:\n\n" + "\n".join(links)


class GuidedDocument(Document):
    """A guideline file that opens with its lead, then the list of its sections.

    The lead is `lead.<span>.md` in the folder named after the file (`guidelines/orm.md`
    reads `guidelines/orm/`), one fragment per range of versions, filled in with the
    document's values. `section_level` is the heading level the list shows.
    """

    section_level = 1
    lead_name = "lead"

    def body(self, version: OdooVersion) -> str:
        return super().render(version)

    def render(self, version: OdooVersion) -> str:
        body = self.body(version).strip("\n")
        index = SectionIndex(body, self.section_level).markdown()
        return f"{self.lead(version)}\n\n{index}\n\n{body}"

    def lead(self, version: OdooVersion) -> str:
        chosen = [fragment for fragment in self.leads() if version.within(self.span(fragment))]
        if len(chosen) != 1:
            raise ValueError(f"{len(chosen)} leads of {self.path} for {version.name}")
        text = chosen[0].read_text(encoding="utf-8")
        return Template(text).substitute(self.values(version)).strip("\n")

    def leads(self) -> list[Path]:
        folder = (TEMPLATES / self.path).with_suffix("")
        return sorted(folder.glob(f"{self.lead_name}.*.md"))

    @staticmethod
    def span(fragment: Path) -> str:
        return fragment.stem.split(".", 1)[1].removeprefix("v")
