"""`odoo-web-guidelines/guidelines/assets.md`: Odoo's own assets guideline, then bundles per version."""

from __future__ import annotations

from ..version import OdooVersion
from .spanned import SpannedDocument


class Assets(SpannedDocument):
    """Odoo's file opens the template as `$upstream`, kept as it is."""

    path = "odoo-web-guidelines/guidelines/assets.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {**super().values(version), "upstream": self.read_upstream(self.path).strip("\n")}
