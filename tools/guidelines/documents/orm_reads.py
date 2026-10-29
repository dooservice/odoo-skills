"""What differs between versions in searching and reading records."""

from __future__ import annotations

from ..version import OdooVersion


class OrmReads:
    """The template values of the "Search and read" section of `orm.md`."""

    def __init__(self, version: OdooVersion) -> None:
        self.version = version

    def values(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "search_count": pick(
                v16=" `search(domain, count=True)` still works; write `search_count` instead.",
                v17_="",
            ),
            "search_fetch": pick(
                v16="To read fields of many records, iterate the recordset: reading one field "
                "loads the stored fields of the whole set in one query (prefetch). "
                "`search_fetch` and `fetch` do not exist in this version.",
                v17_="`search_fetch(domain, field_names)` searches and loads the given fields in "
                "one query, and `records.fetch(field_names)` loads them for records already in "
                "hand. Use them when you know what you will read; plain iteration also "
                "prefetches, but loads every prefetchable field.",
            ),
            "grouped_reads": self.grouped_reads(),
            "name_search_domain": pick(v16_18="args=None", v19_="domain=None"),
            "name_search_override": pick(
                v16="set `_rec_names_search`, or override `_name_search(name, args, operator, "
                "limit, name_get_uid)`.",
                v17="set `_rec_names_search`, or override `_name_search(name, domain, "
                "operator, limit, order)`.",
                v18_="set `_rec_names_search`, or override `_search_display_name(operator, "
                "value)`, which returns the domain of a search on `display_name`.",
            ),
            "display_name": pick(
                v16="`name_get()`; override it returning `[(id, name)]`.",
                v17="`_compute_display_name`; override it with `@api.depends` on what it\n"
                "  reads. `name_get` is deprecated: neither override nor call it.",
                v18_="`_compute_display_name`; override it with `@api.depends` on what it\n"
                "  reads. `name_get` does not exist in this version.",
            ),
            "fields_get_keys": pick(
                v16=" `fields_get_keys()` is deprecated: use `self._fields`.", v17_=""
            ),
            "get_xml_id": pick(
                v16=" `get_xml_id()` is deprecated: use `get_external_id()`.", v17_=""
            ),
        }

    def grouped_reads(self) -> str:
        return self.version.pick(
            v16="Aggregate in SQL with `read_group(domain, fields, groupby, lazy=True)`: one "
            "dict per group, with `<groupby>_count`, the aggregated fields and `__domain`. "
            "With `lazy=True` (the default) only the first `groupby` is applied. "
            "`_read_group` has the same signature in this version.",
            v17_18="Aggregate in SQL with `_read_group(domain, groupby, aggregates)`, which "
            "returns tuples with related records as recordsets: `for author, count in "
            "Book._read_group(domain, ['author_id'], ['__count'])`. Aggregates are "
            "`'field:sum'`, `'field:max'`, `'field:count_distinct'`, `'field:recordset'`, "
            "`'__count'`. `read_group` returns the dicts of the web client's grouped views; "
            "business code uses `_read_group`.",
            v19="Aggregate in SQL with `_read_group(domain, groupby, aggregates)`, which "
            "returns tuples with related records as recordsets: `for author, count in "
            "Book._read_group(domain, ['author_id'], ['__count'])`. Aggregates are "
            "`'field:sum'`, `'field:max'`, `'field:count_distinct'`, `'field:recordset'`, "
            "`'__count'`. `read_group` is deprecated; the web client's grouped views call "
            "`formatted_read_group` (from `web`).",
            v20="Aggregate in SQL with `_read_group(domain, groupby, aggregates)`, which "
            "returns tuples with related records as recordsets: `for author, count in "
            "Book._read_group(domain, ['author_id'], ['__count'])`. Aggregates are "
            "`'field:sum'`, `'field:max'`, `'field:count_distinct'`, `'field:recordset'`, "
            "`'__count'`. `read_group` takes the same arguments and returns ids instead of "
            "records, for RPC; the web client's grouped views call `formatted_read_group` "
            "(from `web`).",
        )
