"""`odoo-web-guidelines/guidelines/scss.md`: Odoo's own SCSS guideline, as it is."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Scss(Document):
    path = "odoo-web-guidelines/guidelines/scss.md"

    def render(self, version: OdooVersion) -> str:
        return self.read_upstream(self.path)
