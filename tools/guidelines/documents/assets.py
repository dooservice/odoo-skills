"""`odoo-web-guidelines/guidelines/assets.md`: Odoo's own assets guideline, as it is."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Assets(Document):
    path = "odoo-web-guidelines/guidelines/assets.md"

    def render(self, version: OdooVersion) -> str:
        return self.read_upstream(self.path)
