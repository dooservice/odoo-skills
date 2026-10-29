"""What differs between versions in model attributes and SQL objects."""

from __future__ import annotations

from ..version import OdooVersion


class ModelVersions:
    """The template values of `models.md` that are whole table rows or examples per version."""

    def __init__(self, version: OdooVersion) -> None:
        self.version = version

    def attributes(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "table_query_row": pick(
                v16="| `_table_query` | for an SQL view model with `_auto = False`, the `SELECT` "
                "(a string, usually a property) the ORM reads as the table |\n",
                v17_19="| `_table_query` | for an SQL view model with `_auto = False`, the `SELECT` "
                "(a string or `SQL`, usually a property) the ORM reads as the table |\n",
                v20="| `_table_sql` | for an SQL view model with `_auto = False`, a property "
                "returning the `SQL` `SELECT` the ORM reads as the table (`_table_query` no "
                "longer exists) |\n",
            ),
            "sql_objects_row": pick(
                v16_18="| `_sql_constraints` | SQL constraints; see "
                "[SQL constraints](#declare-sql-constraints-and-indexes-on-the-model) |\n",
                v19_="| `_<name> = models.Constraint(...)`, `models.Index(...)`, "
                "`models.UniqueIndex(...)` | SQL constraints and indexes; see "
                "[SQL constraints](#declare-sql-constraints-and-indexes-on-the-model) |\n",
            ),
            "sql_view": pick(
                v16_19="set `_auto = False` and define `_table_query` (a `SELECT` returning one "
                "row per record, with an `id` column), or create the view in `init()` with "
                "`tools.drop_view_if_exists` and `CREATE OR REPLACE VIEW`.",
                v20="set `_auto = False` and override the `_table_sql` property (an `SQL` "
                "`SELECT` returning one row per record, with an `id` column), or create the "
                "view in `init()` with `tools.drop_view_if_exists` and `CREATE OR REPLACE "
                "VIEW`.",
            ),
        }

    def sql_objects(self) -> dict[str, str]:
        pick = self.version.pick
        return {
            "sql_constraints": pick(
                v16_18="list them in `_sql_constraints` as `(name, definition, message)` "
                "triples, and create other indexes (several columns, partial) in `init()` with "
                "`tools.create_index`.",
                v19_="declare `models.Constraint`, `models.Index` and `models.UniqueIndex` as "
                "class attributes whose name starts with `_`; the database object is named "
                "`<table>_<name without the _>`. `_sql_constraints` is **ignored** in this "
                "version, with a warning in the log: the constraint is never created.",
            ),
            "sql_constraints_example": pick(
                v16_18="_sql_constraints = [\n"
                "    ('isbn_unique', 'UNIQUE(isbn)', \"The ISBN must be unique.\"),\n"
                "    ('pages_positive', 'CHECK(pages > 0)', \"A book has at least one page.\"),\n"
                "]\n\n"
                "def init(self):\n"
                "    tools.create_index(\n"
                "        self.env.cr, 'library_book_shelf_state_index', self._table, "
                "['shelf_id', 'state'],\n"
                "    )",
                v19_="_isbn_unique = models.Constraint('UNIQUE(isbn)', \"The ISBN must be "
                "unique.\")\n"
                "_pages_positive = models.Constraint('CHECK(pages > 0)', \"A book has at least "
                "one page.\")\n"
                "_shelf_state_idx = models.Index('(shelf_id, state)')\n"
                "_code_active_uniq = models.UniqueIndex(\n"
                "    '(code) WHERE active IS TRUE', \"An active book already has this code.\",\n"
                ")",
            ),
        }
