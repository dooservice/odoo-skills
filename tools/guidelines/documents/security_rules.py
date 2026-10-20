"""`odoo-guidelines/guidelines/security.md`: access rows, record rules and groups."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class AccessRights(Document):
    """Odoo's own text for 20.0, whose `ir.access` model older versions do not have."""

    path = "odoo-guidelines/guidelines/security.md"

    def render(self, version: OdooVersion) -> str:
        if version.number == 20:
            return self.read_upstream(self.path).replace("Master unifies", "Odoo 20.0 unifies")
        return super().render(version)

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "category": version.pick(
                v16_18="`category_id` (an `ir.module.category`)",
                v19_="`privilege_id` (a `res.groups.privilege`)",
            ),
        }
