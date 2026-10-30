"""How much text each layer of the skills of one version holds, in words and approximate tokens."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .constants import CHARACTERS_PER_TOKEN, SIZE_VERSION, SKILLS_FOLDER


@dataclass(frozen=True)
class Layer:
    title: str
    texts: list[str]

    @property
    def words(self) -> int:
        return sum(len(text.split()) for text in self.texts)

    @property
    def tokens(self) -> int:
        return sum(len(text) for text in self.texts) // CHARACTERS_PER_TOKEN

    @property
    def largest(self) -> int:
        return max(len(text) for text in self.texts) // CHARACTERS_PER_TOKEN


class SkillFile:
    """A `SKILL.md`, split into the description in its front matter and the rest."""

    def __init__(self, path: Path) -> None:
        lines = path.read_text().splitlines()
        end = lines.index("---", 1)
        header = lines[1:end]
        start = next(index for index, line in enumerate(header) if line.startswith("description:"))
        stop = next((index for index, line in enumerate(header[start + 1:], start + 1)
                     if not line.startswith(" ")), len(header))
        self.description = " ".join(line.strip() for line in header[start:stop]).removeprefix("description: >-")
        self.body = "\n".join(lines[end + 1:])


class SkillSizes:
    """The layers an agent meets, from what it always sees to what it searches."""

    def __init__(self, version: str = SIZE_VERSION) -> None:
        self.folders = [SKILLS_FOLDER / version, SKILLS_FOLDER / "common"]

    def texts(self, pattern: str) -> list[str]:
        return [path.read_text() for folder in self.folders for path in sorted(folder.glob(pattern))]

    def layers(self) -> list[Layer]:
        skills = [SkillFile(path) for folder in self.folders for path in sorted(folder.glob("*/SKILL.md"))]
        reference = [text for pattern in ("odoo-reference/*.md", "odoo-reference/*/*.md")
                     for text in self.texts(pattern) if not text.startswith("---")]
        return [
            Layer("Descriptions (always in context)", [skill.description for skill in skills]),
            Layer("SKILL.md bodies (when a skill loads)", [skill.body for skill in skills]),
            Layer("Guideline topic files (opened by topic)", self.texts("*-guidelines/guidelines/*.md")),
            Layer("Functional recipes (opened by flow)",
                  self.texts("odoo-functional/recipes/*.md") + self.texts("odoo-functional/connect.md")),
            Layer("Reference (searched, never read whole)", reference),
        ]
