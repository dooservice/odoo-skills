"""`odoo-guidelines/guidelines/reports.md`: QWeb PDF reports, as Odoo's own skills say."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Reports(Document):
    path = "odoo-guidelines/guidelines/reports.md"

    def render(self, version: OdooVersion) -> str:
        return self.read_upstream(self.path)
