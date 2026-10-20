"""`odoo-security/SKILL.md`: Odoo's security audit skill, edited for each version."""

from __future__ import annotations

from pathlib import Path
from string import Template

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion


class SecuritySkill(Document):
    """Odoo's 20.0 skill with a series of edits, each in `templates/odoo-security/edits/<name>/`.

    An edit's `upstream.md` is the passage of Odoo's text it replaces; each other file is
    the replacement for the versions its name spans, as in `OdooVersion.pick` (`v16_19.md`
    for 16 to 19). A version that no file spans keeps Odoo's passage.
    """

    path = "odoo-security/SKILL.md"
    edits = (
        "description", "access-list", "access-control", "domain", "raw-table", "raw-qweb",
        "escape-alias", "html-escape", "csrf-routes", "eval-sandbox", "orm-sql", "sql-identifiers",
    )

    def render(self, version: OdooVersion) -> str:
        text = self.read_upstream(self.path)
        for edit in self.edits:
            text = self.apply(text, TEMPLATES / "odoo-security" / "edits" / edit, version)
        return text

    def apply(self, text: str, folder: Path, version: OdooVersion) -> str:
        passage = self.read_fragment(folder / "upstream.md")
        if passage not in text:
            raise ValueError(f"Odoo's skill no longer has the passage of {folder.name}")
        replacement = self.replacement(folder, version)
        if replacement is None:
            return text
        return text.replace(passage, Template(replacement).substitute(self.values(version)))

    def replacement(self, folder: Path, version: OdooVersion) -> str | None:
        for candidate in sorted(folder.glob("v*.md")):
            if version.within(candidate.stem.removeprefix("v")):
                return self.read_fragment(candidate)
        return None

    def read_fragment(self, path: Path) -> str:
        return path.read_text(encoding="utf-8").removesuffix("\n")
