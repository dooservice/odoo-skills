# Model classes and attributes

- `models.Model`: a persistent model with its own table. The default.
- `models.TransientModel`: a wizard. Its rows are deleted by the autovacuum after
  `_transient_max_hours` hours or beyond `_transient_max_count` rows (server options
  `transient_age_limit` and `osv_memory_count_limit`). It needs access rights like any
  model. A `Many2one` from a `Model` to it is forbidden.
- `models.AbstractModel`: no table; a mixin that other models list in `_inherit`
  (`mail.thread`), or a model of methods only (a report's `_get_report_values`).
- Every model sets `_description`, a human name (the ORM warns when it is missing).

Model attributes, set in the class body:

| Attribute | Meaning |
| --- | --- |
| `_name` | the model's name; see [Naming](python.md#naming-and-model-layout) |
| `_description` | its human name, shown to users |
| `_inherit` | the model(s) extended or reused; see [Inheritance](#pick-the-inheritance-mechanism-for-what-you-need) |
| `_inherits` | delegation: `{'library.item': 'item_id'}` |
| `_order` | the default order of `search`, as in SQL: `'sequence, name, id desc'`; only stored fields |
| `_rec_name` | the field used as display name (default `name`) |
| `_rec_names_search` | the fields searched by a search on the display name, such as a `Many2one` input: `['name', 'code']` |
| `_table` | the table name, when it must differ from `_name` with dots replaced |
| `_auto` | `False` to create no table: the model is an SQL view you create yourself |
| `_log_access` | `False` to drop `create_uid`, `create_date`, `write_uid`, `write_date`; keep it on a `TransientModel`, whose vacuum reads `write_date` |
| `_parent_name`, `_parent_store` | the parent field (default `parent_id`) and the materialized path; see [Hierarchies](#store-hierarchies-with-_parent_store) |
| `_active_name` | the archiving field, set by the ORM to `active` (or `x_active`) when it exists |
| `_fold_name` | the field folding a kanban column (default `fold`) |
| `_check_company_auto` | `True` to check company consistency on `create` and `write`; see [Multi-company](multi_company.md#make-a-model-multi-company) |
| `_allow_sudo_commands` | `False` to refuse x2many commands on this model from a `sudo()` or `with_user()` environment; for security-sensitive models |
| `_depends` | for an SQL view model, `{model: [fields]}` read by the view, flushed before each query |
| `_table_query` | for an SQL view model with `_auto = False`, the `SELECT` (a string, usually a property) the ORM reads as the table |
| `_register`, `_abstract`, `_transient` | set by the base classes; never set them yourself |
| `_sql_constraints` | SQL constraints; see [SQL constraints](#declare-sql-constraints-and-indexes-on-the-model) |

# Pick the inheritance mechanism for what you need

Choose among the three mechanisms by what the new code needs, and name it with the
attributes below and nothing else:

| You need | Write | Result |
| --- | --- | --- |
| to add fields or change methods of an existing model | `_inherit = 'library.book'` (no `_name`) | the same model and table, extended in place |
| a new model reusing another's fields and methods | `_name = 'library.ebook'` and `_inherit = 'library.book'`, or a list of mixins | a new model and table with its own copy of the fields; later extensions of `library.book` reach it too |
| a new model whose records each own a record of another model | `_inherits = {'library.item': 'item_id'}` and `item_id = fields.Many2one('library.item', required=True, ondelete='cascade')` | two tables; the parent's fields read and write through `item_id` |

## What to know

- In place extension (`_inherit` alone) is what modules do nearly always. The class
  name is free; `_name` repeated with the same value as `_inherit` is the same thing.
- `_inherit` takes a list to combine mixins. With a list, always set `_name`:
  `_name = 'library.book'` with `_inherit = ['library.book', 'mail.thread']` adds a
  mixin to an existing model. Without `_name`, a list of several models names the model after the Python class.
- Delegation (`_inherits`, or `delegate=True` on the `Many2one`) inherits fields only,
  **not** methods: `library.ebook` cannot call `library.item` methods on itself.
  Avoid it where you can; chained `_inherits` is unsupported, and it creates a parent
  record for every child.

# Override with `super()` and the same signature

An override calls `super()` once, with the arguments it received, and returns what
`super()` returned (or a superset); it never copies the parent's body.

```python
def action_lend(self):
    res = super().action_lend()
    self._notify_borrowers()
    return res
```

## Why

- Every installed module may override the same method; each override is one link of
  a chain through `super()`. Not calling it, or changing the arguments, drops the
  behavior of every module below.

## Exceptions

- Changing the arguments is the point of some overrides: adding keys to the `vals` of
  `write` or to the `default` of `copy_data` before calling `super()` is fine.

# Declare SQL constraints and indexes on the model

Enforce single-row invariants and uniqueness in the database: list them in `_sql_constraints` as `(name, definition, message)` triples, and create other indexes (several columns, partial) in `init()` with `tools.create_index`.

```python
_sql_constraints = [
    ('isbn_unique', 'UNIQUE(isbn)', "The ISBN must be unique."),
    ('pages_positive', 'CHECK(pages > 0)', "A book has at least one page."),
]

def init(self):
    tools.create_index(
        self.env.cr, 'library_book_shelf_state_index', self._table, ['shelf_id', 'state'],
    )
```

## Why

- A database constraint holds for every write, including concurrent transactions,
  imports and raw SQL; a Python check (`@api.constrains`) does not.
- The ORM creates, updates and drops these objects when the module is installed or
  updated. A violation during a client call reaches the user as a `ValidationError`
  carrying the message; in Python code it surfaces as an `IntegrityError` when the ORM
  flushes.

## Exceptions

- A check that reads other records or other models stays in `@api.constrains`.
- Adding a constraint to a table whose rows break it fails at update (logged, and the
  constraint is not created): migrate the data first.

# Store hierarchies with `_parent_store`

Give a tree model `_parent_store = True` and a `parent_path = fields.Char(index=True)`
field, and search the tree with `child_of` / `parent_of` instead of recursive Python.

- `parent_path` holds the ids from the root (`'1/5/12/'`): `child_of` and `parent_of`
  become one indexed query instead of one query per level.
- `_parent_name` names the parent field when it is not `parent_id`.
- Forbid cycles with a constraint: `@api.constrains('parent_id')` raising `ValidationError` when `not self._check_recursion()`.
- A computed field that depends on its parent's value
  (`@api.depends('parent_id.complete_name')`) needs `recursive=True`.

# Back reporting models by an SQL view

Back a reporting model by an SQL query, not by stored computes: set `_auto = False` and define `_table_query` (a `SELECT` returning one row per record, with an `id` column), or create the view in `init()` with `tools.drop_view_if_exists` and `CREATE OR REPLACE VIEW`.

- Declare every field the view outputs as `readonly=True`, and the source fields in
  `_depends`, so that pending writes on them are flushed before each search.
- Grant only `read` in its access rights: nothing can be written to a view.
