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

    def template(self, version: OdooVersion) -> Path:
        return TEMPLATES / "AUTHORING.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {**super().values(version), "skill": self.skill}

    def render(self, version: OdooVersion) -> str:
        text = self.read_upstream(self.path)
        if self.registration not in text:
            raise ValueError(f"Odoo's {self.path} no longer has its registration rule")
        ours = (
            "- Add a row to the table in `SKILL.md`, through its template\n"
            f"  (`tools/guidelines/templates/{self.skill}/SKILL.md`)."
        )
        return text.replace(self.registration, ours) + "\n" + super().render(version)


class GuidelinesAuthoring(Authoring):
    skill = "odoo-guidelines"
    path = "odoo-guidelines/AUTHORING.md"


class WebAuthoring(Authoring):
    skill = "odoo-web-guidelines"
    path = "odoo-web-guidelines/AUTHORING.md"
