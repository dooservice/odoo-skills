"""`odoo-guidelines/guidelines/version.md`: what one Odoo version has, row by row."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .interface_version_notes import InterfaceVersionNotes


class VersionNotes(Document):
    path = "odoo-guidelines/guidelines/version.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **self.models(version),
            **self.server(version),
            **InterfaceVersionNotes().values(version),
        }

    def models(self, version: OdooVersion) -> dict[str, str]:
        return {
            "display_name": version.pick(
                v16="override `name_get()` (returns `[(id, name)]`)",
                v17="override `_compute_display_name` (with `@api.depends`); "
                "`name_get` is deprecated and no longer builds it",
                v18_="override `_compute_display_name`; `name_get` does not exist",
            ),
            "grouped_reads": version.pick(
                v16="`read_group(domain, fields, groupby, lazy=...)`, returns dicts",
                v17_18="`_read_group(domain, groupby, aggregates)`, returns tuples; "
                "`read_group` stays for the web client",
                v19="`_read_group(domain, groupby, aggregates)`, returns tuples; `read_group` is deprecated",
                v20="`read_group(domain, groupby, aggregates)` and `_read_group`, both return tuples",
            ),
            "field_aggregation": version.pick(
                v16_17="`group_operator='sum'`",
                v18_19="`aggregator='sum'` (`group_operator` is a deprecated alias)",
                v20="`aggregator='sum'`",
            ),
            "sql_constraints": version.pick(
                v16_18="`_sql_constraints = [(name, definition, message)]`; indexes with `index=True` "
                "or `index='btree_not_null'`/`'trigram'`",
                v19_='model attributes `_x_check = models.Constraint("CHECK (...)", "msg")`, '
                "`models.Index(...)`, `models.UniqueIndex(...)`; `_sql_constraints` is ignored "
                "with a warning",
            ),
            "domains": version.pick(
                v16_18="lists; combine with `odoo.osv.expression.AND([...])` / `OR([...])`",
                v19_="`from odoo.fields import Domain`; `Domain(...) & Domain(...)`, `Domain.AND/OR`",
            ),
            "translations": version.pick(
                v16_17='`from odoo import _, _lt`; `_("...")`, `_lt` for module-level constants',
                v18_='`self.env._("...")`; `_lt = LazyTranslate(__name__)` for module-level constants; '
                "bare `_` still works",
            ),
        }

    def server(self, version: OdooVersion) -> dict[str, str]:
        return {
            "python": version.pick(
                v16="3.7 or newer", v17_19="3.10 or newer", v20="3.12 or newer"
            ),
            "group_categories": version.pick(
                v16_18="`category_id` on `res.groups` (an `ir.module.category`)",
                v19_="`privilege_id` on `res.groups` (a `res.groups.privilege`)",
            ),
            "access_rights": version.pick(
                v16_19="`security/ir.model.access.csv` plus `ir.rule` records",
                v20="`security/ir.access.csv` (`ir.access`, one model for ACLs and record rules)",
            ),
            "route_types": version.pick(
                v16_18="`type='http'` or `type='json'`",
                v19="`'http'`, `'jsonrpc'` (`'json'` is a deprecated alias), `'json2'`",
                v20="`'http'`, `'jsonrpc'`, `'json2'`",
            ),
            "route_auth": version.pick(
                v16_17="`user`, `public`, `none`",
                v18_="`user`, `public`, `none`, `bearer`",
            ),
            "test_tags": version.pick(
                v16_19="`at_install`: write `@tagged('post_install', '-at_install')` on business tests",
                v20="`post_install`",
            ),
        }
