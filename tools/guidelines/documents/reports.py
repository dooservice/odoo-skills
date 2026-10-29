"""`odoo-guidelines/guidelines/reports.md`: QWeb PDF reports, Odoo's own rules followed by ours."""

from __future__ import annotations

from pathlib import Path

from ..constants import TEMPLATES
from ..document import Document
from ..version import OdooVersion
from .reports_values import ReportValues


class Reports(Document):
    """Odoo's `reports.md` as it is, then the sections of `qweb_pdf.md` filled in per version."""

    path = "odoo-guidelines/guidelines/reports.md"

    def template(self, version: OdooVersion) -> Path:
        return TEMPLATES / "odoo-guidelines/guidelines/qweb_pdf.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {**super().values(version), **ReportValues().values(version)}

    def render(self, version: OdooVersion) -> str:
        return self.read_upstream(self.path) + super().render(version)
