"""`AUTHORING.md` of a guideline skill: Odoo's rules for writing a guideline, plus ours."""

from __future__ import annotations

from pathlib import Path

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion


class Authoring(Document):
    """Odoo's file as it is, its registration rule pointed at our template, then
    `templates/AUTHORING.md`: how a guideline is generated and checked here.
    """

    skill = ""
    registration = "- Add a row to the table in `SKILL.md`."
    heading = "## Registering the guideline"

    def template(self, version: OdooVersion) -> Path:
        return TEMPLATES / "AUTHORING.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {**super().values(version), "skill": self.skill}

    def render(self, version: OdooVersion) -> str:
        text = self.read_upstream(self.path)
        if self.registration not in text:
            raise ValueError(f"Odoo's {self.path} no longer has its registration rule")
        start = text.index(self.heading)
        after = text.find("\n## ", start + len(self.heading))
        rest = text[after:] if after > 0 else ""
        return text[:start] + self.ours() + rest + "\n" + super().render(version)

    def ours(self) -> str:
        """Our skills open with a short map by task and generate each file's section list."""
        return (
            f"{self.heading}\n\n"
            "- Add the guideline as a `#` section of the file of its domain: the section list\n"
            "  at the top of each file is generated from its headings.\n"
            "- Add a row to the task map of `SKILL.md`, through its template\n"
            f"  (`tools/guidelines/templates/{self.skill}/SKILL.md`), only for a new file or a\n"
            "  new kind of task; the map names files, not sections.\n"
            "- When a version-specific name matters more than the rest of the file, add it to\n"
            "  the file's key names at its top.\n"
        )


class GuidelinesAuthoring(Authoring):
    skill = "odoo-guidelines"
    path = "odoo-guidelines/AUTHORING.md"


class WebAuthoring(Authoring):
    skill = "odoo-web-guidelines"
    path = "odoo-web-guidelines/AUTHORING.md"
