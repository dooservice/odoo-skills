"""`odoo-guidelines/SKILL.md`: what the skill covers, and which section to read when."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class GuidelinesSkill(Document):
    path = "odoo-guidelines/SKILL.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "version_anchor": f"what-odoo-{version.number}0-has",
        }
