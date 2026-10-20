  Prefer `search`/`_read_group` and direct field access (not `read()`). For
  custom SQL over ORM-filtered rows, build the query with `_search(...)` and
  `Query.select(SQL(...))`: access rules and `active` handling stay in force.
