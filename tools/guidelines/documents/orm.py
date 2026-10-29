"""`odoo-guidelines/guidelines/orm.md`: recordsets, reads, writes, access, cache, transactions."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .orm_access import OrmAccess
from .orm_reads import OrmReads
from .orm_writes import OrmWrites


class Orm(Document):
    path = "odoo-guidelines/guidelines/orm.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        writes = OrmWrites(version)
        return {
            **super().values(version),
            **OrmReads(version).values(),
            **writes.records(),
            **OrmAccess(version).values(),
            **writes.cache(),
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
            "filtered_note": version.pick(
                v16_18="takes a callable or a field path (`'author_id.active'`)",
                v19_="takes a callable, a field path (`'author_id.active'`) or a `Domain`",
            ),
            "sorted_note": version.pick(
                v16_18="`key` is a callable or one field name; without `key`, it runs a "
                "`search` to apply `_order`",
                v19_="`key` is a callable or an order string (`'name desc, id'`); without "
                "`key`, it applies `_order`; both in memory",
            ),
            "grouped_row": version.pick(
                v16="",
                v17_="| `records.grouped('author_id')` | a dict `{key: records}` | a callable "
                "works too; in memory, no query |\n",
            ),
            "onchange_args": version.pick(
                v16="field_name, field_onchange", v17_="field_names, fields_spec"
            ),
        }
