"""`odoo-guidelines/guidelines/fields.md`: declaring fields, their indexes and aggregation."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Fields(Document):
    path = "odoo-guidelines/guidelines/fields.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "custom_indexes": version.pick(
                v16_18="multi-column or custom indexes are created in `init()` with "
                "`tools.create_index(self.env.cr, ...)`",
                v19_="multi-column or custom indexes are model attributes "
                '(`_x_idx = models.Index("(a, b)")`, `models.UniqueIndex`; '
                "the attribute name must start with `_`)",
            ),
            "aggregation": version.pick(
                v16_17="`group_operator=`", v18_="`aggregator=`"
            ),
        }
