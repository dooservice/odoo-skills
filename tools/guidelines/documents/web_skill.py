"""`odoo-web-guidelines/SKILL.md`: the web guidelines skill and its table of sections."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class WebSkill(Document):
    path = "odoo-web-guidelines/SKILL.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        """`major` is the version as in a heading's anchor: `#the-web-framework-in-180`."""
        return {**super().values(version), "major": str(version.number)}
