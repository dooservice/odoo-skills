"""One skill folder and the budgets its description, body and files must fit."""

from __future__ import annotations

from pathlib import Path

from .constants import (
    BODY_LIMITS,
    DEFAULT_BODY_LIMIT,
    DESCRIPTION_LIMIT,
    EXEMPT_FILES,
    EXEMPT_FOLDERS,
    FILE_LIMIT,
    REFERENCE_SKILL,
    REPOSITORY,
    SKILL_FILE,
)
from .measure import Measure
from .skill_text import SkillText


class Skill:
    """A folder holding a SKILL.md and the files it points to."""

    def __init__(self, folder: Path) -> None:
        self.folder = folder
        self.text = SkillText((folder / SKILL_FILE).read_text(encoding="utf-8"))

    @property
    def name(self) -> str:
        return self.folder.name

    def label(self, path: Path) -> str:
        return str(path.relative_to(REPOSITORY))

    def is_exempt(self, path: Path) -> bool:
        if self.name != REFERENCE_SKILL:
            return False
        relative = path.relative_to(self.folder)
        return relative.parts[0] in EXEMPT_FOLDERS or str(relative) in EXEMPT_FILES

    def files(self) -> list[Path]:
        found = sorted(self.folder.rglob("*.md"))
        return [path for path in found if path.name != SKILL_FILE or path.parent != self.folder]

    def budgeted_files(self) -> list[Path]:
        return [path for path in self.files() if not self.is_exempt(path)]

    def texts(self) -> dict[str, str]:
        texts = {self.label(self.folder / SKILL_FILE): self.text.body()}
        for path in self.budgeted_files():
            texts[self.label(path)] = path.read_text(encoding="utf-8")
        return texts

    def measures(self) -> list[Measure]:
        skill_label = self.label(self.folder / SKILL_FILE)
        measures = [
            Measure(f"{skill_label} (description)", len(self.text.description()), DESCRIPTION_LIMIT),
            Measure(
                f"{skill_label} (body)",
                len(self.text.body()),
                BODY_LIMITS.get(self.name, DEFAULT_BODY_LIMIT),
            ),
        ]
        for path in self.budgeted_files():
            size = len(path.read_text(encoding="utf-8"))
            measures.append(Measure(self.label(path), size, FILE_LIMIT))
        return measures
