"""One country's localization skill, and what it is missing."""

from __future__ import annotations

from pathlib import Path

from .constants import (
    LOCALIZATION_FILES,
    LOCALIZATION_SECTIONS,
    LOCALIZATIONS_FOLDER,
    TEMPLATE_FOLDER,
)


class Localization:
    """`localization/<country code>/odoo-l10n-<country code>/`."""

    def __init__(self, country_folder: Path) -> None:
        self.country = country_folder.name
        self.skill_folder = country_folder / f"odoo-l10n-{self.country}"

    @classmethod
    def all(cls) -> list[Localization]:
        if not LOCALIZATIONS_FOLDER.is_dir():
            return []
        folders = sorted(folder for folder in LOCALIZATIONS_FOLDER.iterdir() if folder.is_dir())
        return [cls(folder) for folder in folders if folder.name != TEMPLATE_FOLDER]

    @property
    def skill_name(self) -> str:
        return self.skill_folder.name

    def problems(self) -> list[str]:
        """What keeps this localization from being listed: missing files, sections out of place."""
        missing = [name for name in LOCALIZATION_FILES if not (self.skill_folder / name).is_file()]
        if missing:
            return [f"{self.skill_name}: missing {', '.join(missing)}"]
        return self.section_problems((self.skill_folder / "SKILL.md").read_text(encoding="utf-8"))

    def section_problems(self, skill: str) -> list[str]:
        headings = [line.strip() for line in skill.splitlines() if line.startswith("## ")]
        present = [heading for heading in headings if heading in LOCALIZATION_SECTIONS]
        absent = [section for section in LOCALIZATION_SECTIONS if section not in headings]
        problems = [f"{self.skill_name}: no '{section}' section" for section in absent]
        expected_order = [section for section in LOCALIZATION_SECTIONS if section in present]
        if present != expected_order:
            problems.append(f"{self.skill_name}: sections out of order, expected {expected_order}")
        if "<!--" in skill:
            problems.append(f"{self.skill_name}: the template's instructions are still in SKILL.md")
        return problems
