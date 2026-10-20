"""`odoo-guidelines/guidelines/orm.md`: recordsets, computes, extension points, transactions."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion


class Orm(Document):
    path = "odoo-guidelines/guidelines/orm.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            "recordset_methods": version.pick(
                v16="`filtered`, `mapped`, `sorted`",
                v17_="`filtered`, `grouped`, `mapped`, `sorted`",
            ),
            "combining_domains": version.pick(
                v16_18="Combine domains with `odoo.osv.expression.AND([...])` / `OR([...])`; never\n"
                "  hand-build `'&'`/`'|'` prefix-notation lists.",
                v19_="Combine domains with `odoo.fields.Domain`: the `&`, `|`, `~` operators for\n"
                "  domains written inline, `Domain.AND`/`Domain.OR` for a list of domains you\n"
                "  already hold. Never hand-build `'&'`/`'|'` prefix-notation lists.",
            ),
            "constraints": self.constraints(version),
            "display_name": version.pick(
                v16="`name_get()`; override it returning `[(id, name)]`.",
                v17_="`_compute_display_name`; override it with\n"
                "  `@api.depends` on what it reads, never `name_get`.",
            ),
        }

    def constraints(self, version: OdooVersion) -> str:
        return version.pick(
            v16_18="enforce invariants with `@api.constrains` or `_sql_constraints = [(name,\n"
            "  definition, message)]`.",
            v19_="enforce invariants with `@api.constrains` or SQL constraints declared as model\n"
            '  attributes (`_x_check = models.Constraint("CHECK (...)", "msg")`; the\n'
            "  attribute name must start with `_`). Indexes are declared the same way\n"
            "  (`_x_index = models.Index(...)`, `models.UniqueIndex(...)`). `_sql_constraints`\n"
            "  is **ignored** with a log warning in this version: the constraint is never created.",
        )
