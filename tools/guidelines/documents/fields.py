"""`odoo-guidelines/guidelines/fields.md`: field types, attributes, computes and indexes."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .fields_versions import FieldVersions


class Fields(Document):
    path = "odoo-guidelines/guidelines/fields.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        differences = FieldVersions(version)
        return {
            **super().values(version),
            **differences.attributes(),
            **differences.computes(),
            "custom_indexes": version.pick(
                v16_18="Multi-column or custom indexes are created in `init()` with "
                "`tools.create_index(self.env.cr, ...)`; see "
                "[SQL constraints and indexes](models.md#declare-sql-constraints-and-indexes-on-the-model)",
                v19_="Multi-column or custom indexes are model attributes "
                '(`_x_idx = models.Index("(a, b)")`, `models.UniqueIndex`; '
                "the attribute name must start with `_`); see "
                "[SQL constraints and indexes](models.md#declare-sql-constraints-and-indexes-on-the-model)",
            ),
            "min_display_digits": version.pick(
                v16_18="", v19_=", `min_display_digits` (the fewest decimals shown)"
            ),
            "bypass_access": version.pick(v16_18="auto_join", v19_="bypass_search_access"),
            "bypass_access_note": version.pick(
                v16_18="it also turns the search into an SQL join. Use it only when the "
                "comodel's record rules add nothing (lines always visible with their parent).",
                v19_="use it only when the comodel's record rules add nothing (lines always "
                "visible with their parent). `auto_join` does not exist in this version.",
            ),
            "uom_precision": version.pick(
                v16_18="A quantity has the precision of its unit "
                "(`precision_rounding=uom.rounding`, with the `uom` module).",
                v19_="A quantity is rounded and compared by its unit (`uom.round(value)`, "
                "`uom.compare(a, b)`, `uom.is_zero(value)`, with the `uom` module).",
            ),
            "property_definition": version.pick(
                v16="",
                v17_=" `get_property_definition('book_properties.<name>')` returns the "
                "definition of one property.",
            ),
        }
