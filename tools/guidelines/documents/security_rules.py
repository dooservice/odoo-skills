"""`odoo-guidelines/guidelines/security.md`: access rows, record rules, groups, field groups and sudo."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .security_access import AccessBlocks
from .security_calls import AccessCalls
from .security_groups import GroupBlocks


class AccessRights(Document):
    """One template for every version; 20.0 carries Odoo's own `ir.access` text inside it."""

    path = "odoo-guidelines/guidelines/security.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **AccessBlocks().values(version),
            **GroupBlocks().values(version),
            **AccessCalls().values(version),
        }
