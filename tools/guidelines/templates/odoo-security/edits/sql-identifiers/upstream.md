  values as **parameters** (psycopg2 formats them, including a tuple for
  `IN %s`), or use the `odoo.tools.SQL` wrapper. For dynamic **identifiers**
  (table/column names, which can't be parameters) use `SQL.identifier(name)`,
  which validates the name (via `assert`, so a `-O` deployment skips the
  check; still never feed it raw user input).
