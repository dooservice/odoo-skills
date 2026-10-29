"""What differs between versions in field attributes and computed fields."""

from __future__ import annotations

from ..version import OdooVersion


class FieldVersions:
    """The template values of `fields.md` that are whole sentences per version."""

    def __init__(self, version: OdooVersion) -> None:
        self.version = version

    def attributes(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "copy_callable": pick(
                v16_19="",
                v20=" It may also be a callable `(record) -> value` that produces the copied value.",
            ),
            "company_dependent": pick(
                v16_17="one value per company, kept in `ir.property` records instead of a "
                "column: the field is not stored, so it cannot be sorted or grouped by.",
                v18_="one value per company, stored in a `jsonb` column keyed by company id; a "
                "company without a value falls back to the field's default in `ir.default`. "
                "Only on `Char`, `Text`, `Html`, `Boolean`, `Integer`, `Float`, `Date`, "
                "`Datetime`, `Selection` and `Many2one`, never `required` or `translate`.",
            ),
            "aggregator": pick(v16_17="group_operator", v18_="aggregator"),
            "aggregation": pick(
                v16_17="how the field aggregates in grouped views and `read_group`: "
                "`'sum'`, `'avg'`, `'min'`, `'max'`, `'count'`, `'count_distinct'`, "
                "`'bool_and'`, `'bool_or'`, or `False` for nothing. `aggregator` does not "
                "exist in this version.",
                v18_19="how the field aggregates in grouped views: `'sum'`, `'avg'`, `'min'`, "
                "`'max'`, `'count'`, `'count_distinct'`, `'bool_and'`, `'bool_or'`, or `False` "
                "for nothing. The old name `group_operator` still works with a deprecation "
                "warning; write `aggregator`.",
                v20="how the field aggregates in grouped views: `'sum'`, `'avg'`, `'min'`, "
                "`'max'`, `'count'`, `'count_distinct'`, `'bool_and'`, `'bool_or'`, or `False` "
                "for nothing. The old name `group_operator` no longer exists.",
            ),
            "group_expand": pick(
                v16_17="The method receives `(records_or_values, domain, order)` and returns "
                "the groups to show.",
                v18_="The method receives `(records_or_values, domain)` and returns the groups "
                "to show; on a `Selection`, `group_expand=True` shows every value.",
            ),
            "states": pick(
                v16="- `states={'done': [('readonly', True)]}` still works but is legacy: put "
                "the condition in the view instead.\n",
                v17="- `states` is ignored with a warning: put the condition in the view "
                "(`readonly=\"state == 'done'\"`).\n",
                v18_="",
            ),
            "init_storage": pick(
                v16_19="",
                v20="- `init_storage`: a method (or callable) that fills the column of existing "
                "rows in SQL when the column is created; it must not use the ORM, and a truthy "
                "return value makes the ORM recompute the field afterwards.\n",
            ),
            "init_storage_rule": pick(v16_19="", v20=", or an `init_storage` that fills it in SQL"),
        }

    def computes(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "compute_sql": pick(
                v16_19="",
                v20=" `compute_sql` (a method `(self, table)` returning an `SQL` expression "
                "of the value, with an explicit `compute_sudo`) makes a non-stored compute "
                "searchable and sortable without a column.",
            ),
            "search_example": pick(
                v16_18="    return [('author_id.name', operator, value)]",
                v19_="    if operator not in ('in', 'ilike'):\n"
                "        return NotImplemented\n"
                "    return Domain('author_id.name', operator, value)",
            ),
            "search_method": pick(
                v16_18="A search method receives `(operator, value)` as written in the domain "
                "(`'='`, `'!='`, `'ilike'`, `'in'`, ...) and returns a domain on stored "
                "fields. Handle every operator a user can pick in the search panel, and raise "
                "`UserError` for the others.",
                v19_="A search method receives `(operator, value)` after the ORM normalized "
                "the condition (`'='` becomes `'in'` with a list; a boolean condition becomes "
                "`'in'` with `[True]`), and returns a `Domain` (`from odoo.fields import Domain`) or a "
                "domain list on stored "
                "fields. For an operator it does not support it returns `NotImplemented`: the "
                "ORM then tries an equivalent one, such as the positive form of a negative "
                "operator.",
            ),
        }
