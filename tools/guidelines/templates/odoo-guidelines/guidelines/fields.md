# Fields

- Relational suffixes: `Many2one` -> `_id`, `One2many`/`Many2many` -> `_ids`.
- Give the comodel of a relational field as its first positional argument and every
  other attribute by keyword: `fields.Many2one('library.author', string="Author")`.
- `string` defaults to the field name capitalized (`date_due` -> "Date due"); set it
  only when that label is wrong. `help` is the tooltip.
- A field and a method can't share a name (same namespace); flag collisions.
- Extend a field of another module by redeclaring it in the `_inherit` class with only
  the attributes that change (`name = fields.Char(required=True)`): the ORM merges them
  into the original definition. Never copy the whole definition.
- Restrict sensitive fields with the `groups` attribute (comma-separated external
  ids); restricted fields are dropped from views and `fields_get`, and raise on
  direct read/write.
- Use **reserved** fields for their built-in behavior rather than reinventing
  them: `active` for archiving (via `action_archive`, not a custom boolean),
  `state` for lifecycle, `parent_id` + `parent_path` for trees (see
  [Hierarchies](models.md#store-hierarchies-with-_parent_store)), `company_id` for
  multi-company, `sequence` for manual ordering, `currency_id` for `Monetary` amounts.

# Field types

Every field type of $version, what it holds, and the attributes specific to it:

| Type | Holds | Specific attributes |
| --- | --- | --- |
| `fields.Boolean` | `True`/`False`; an empty value reads as `False` | |
| `fields.Char` | one line of text (`varchar`) | `size` (maximum length), `trim` (default `True`), `translate` |
| `fields.Text` | multi-line plain text | `translate` |
| `fields.Html` | HTML, read as `Markup` | `sanitize` (default `True`), `sanitize_overridable`, `sanitize_tags`, `sanitize_attributes`, `sanitize_style`, `strip_style`, `strip_classes`, `translate` |
| `fields.Integer` | a 32-bit integer (`int4`, at most 2,147,483,647) | sums when grouped |
| `fields.Float` | a float: `numeric` with `digits`, `double precision` without | `digits`$min_display_digits; sums when grouped |
| `fields.Monetary` | an amount in the currency of the record | `currency_field` (default `currency_id`); sums when grouped |
| `fields.Date` | a `datetime.date` | see [Dates and times](#store-datetimes-in-utc-and-dates-as-the-users-day) |
| `fields.Datetime` | a naive `datetime.datetime`, in UTC | see [Dates and times](#store-datetimes-in-utc-and-dates-as-the-users-day) |
| `fields.Binary` | bytes, base64 over RPC; kept in `ir.attachment` by default; not prefetched | `attachment` (default `True`) |
| `fields.Image` | a `Binary` holding an image, resized on write when a maximum is set | `max_width`, `max_height`, `verify_resolution` |
| `fields.Selection` | one key of a fixed list (`varchar`) | `selection`, `selection_add`, `ondelete` |
| `fields.Reference` | one record of one of several models, written as `'library.book,42'` | `selection` (the allowed models) |
| `fields.Many2one` | one record, through an `int4` foreign key | `ondelete`, `check_company`, `delegate`, `domain`, `context`, `$bypass_access` |
| `fields.One2many` | the records of the comodel whose `Many2one` points here; no column | `inverse_name` (required), `domain`, `context`, `$bypass_access` |
| `fields.Many2many` | records, through a relation table | `relation`, `column1`, `column2`, `check_company`, `domain`, `context`, `ondelete` |
| `fields.Many2oneReference` | an `int4` id whose model name is in another field (`res_model`/`res_id` pairs) | `model_field` (the `Char` holding the model name) |
| `fields.Json` | free JSON (`jsonb`) | see [Json and properties](#keep-json-for-data-the-orm-does-not-query) |
| `fields.Properties` | values of properties a user defines on a container record | `definition` |
| `fields.PropertiesDefinition` | on the container, the definition of those properties | |

# Field attributes

Attributes every type accepts, and what each one really does:

- `required=True`: `NOT NULL` in the database when existing rows allow it, and a
  required input in views.
- `readonly=True`: UI only. Code writes the field anyway; it is not a protection.
- `default`: a value, or a callable taking the model (`default=lambda self:
  self.env.company`). `default=None` removes a default inherited from the parent
  field.
- `index`: see [Index selectively](#index-selectively).
- `copy`: whether `copy` duplicates the value. `True` by default; `False` by default for
  `One2many`, for computed, related and company-dependent fields, and for a field named
  `state`.$copy_callable
- `store`: `True` by default; `False` by default for computed and related fields.
- `groups`: restricts read and write to members of the groups.
- `translate=True` on `Char`, `Text` and `Html`: one value per language, stored as
  `jsonb`. On `Html`, `translate=html_translate` (from `odoo.tools.translate`)
  translates term by term instead of the whole value.
- `company_dependent=True`: $company_dependent
- `tracking=True`: logs changes in the chatter; accepted only on models that inherit
  `mail.thread`.
- `$aggregator`: $aggregation
- `group_expand`: a method that adds empty groups when grouping by the field (kanban
  columns that must always show). $group_expand
- `change_default=True`: user-defined defaults (`ir.default`) of other fields may be
  conditioned on this field's value.
- `prefetch`: `False` keeps a heavy field out of the batch read that loads the other
  fields; a string names a prefetch group.
- `exportable=False` hides the field from export; `default_export_compatible=True`
  includes it by default in an import-compatible export.
$states$init_storage
# Relational fields

- `Many2one(ondelete=...)`: `'set null'` (default), `'restrict'` (default when
  `required=True`), or `'cascade'`. A required `Many2one` with `'set null'` raises at
  setup. From a `TransientModel` to a `Model`, a required `Many2one` defaults to
  `'cascade'`; a `Many2one` from a `Model` to a `TransientModel` is forbidden.
- `check_company=True` on every relation to a company-specific model, on a model with
  `_check_company_auto = True`; see
  [Make a model multi-company](multi_company.md#make-a-model-multi-company).
- `domain` and `context` on the field apply in every view; `domain` restricts the
  values offered, not the values code writes.
- `$bypass_access=True` on a `Many2one` or `One2many` makes searches through the
  field skip the access rules of the comodel; $bypass_access_note
- `delegate=True` on a `Many2one` is delegation inheritance (`_inherits`); see
  [Inheritance](models.md#pick-the-inheritance-mechanism-for-what-you-need).
- A `One2many` needs the `Many2one` named by `inverse_name` on the comodel, and reads
  it: the `One2many` itself has no column.
- Two `Many2many` fields between the same two models need explicit, different
  `relation` tables: with implicit names they would share one table, and the ORM
  refuses it. Give `column1` (this model) and `column2` (the comodel) with them.
- `Many2many(ondelete=...)` applies to the comodel's column of the relation table:
  `'cascade'` (default) or `'restrict'`.
- Write x2many values with `Command`; see
  [Write x2many values with Command](orm.md#write-x2many-values-with-command).

# Store datetimes in UTC and dates as the user's day

Store a `Datetime` in UTC and convert only for display; compute "today" for a `Date`
with `fields.Date.context_today(self)`, not `fields.Date.today()`.

## Why

- A `Datetime` is a naive `datetime` in UTC in Python and in the database; the web
  client converts it to the user's time zone. Mixing local times into it shifts values
  by the offset.
- `fields.Date.today()` and `fields.Datetime.now()` are the server's UTC date and time.
  Near midnight the user's day differs: `fields.Date.context_today(record)` is the date
  in the user's time zone (the `tz` of the context), and
  `fields.Datetime.context_timestamp(record, value)` converts a UTC value to it.

## Helpers

- Convert with `fields.Date.to_date(value)`, `fields.Datetime.to_datetime(value)` and
  `fields.Date.to_string(value)` / `fields.Datetime.to_string(value)` instead of
  parsing strings by hand.
- Shift and truncate with `fields.Date.add(value, months=1)`,
  `fields.Date.subtract(...)`, `fields.Date.start_of(value, 'month')` and
  `fields.Date.end_of(...)` (same names on `fields.Datetime`).

# Compare floats at their precision

Compare, round and test for zero a `Float` with `fields.Float.compare`,
`fields.Float.round` and `fields.Float.is_zero` at the precision of the data, and an
amount with `currency.compare_amounts`, `currency.round` and `currency.is_zero`; never
with `==`, `round()` or `if not amount`.

## Why

- Binary floats accumulate error: `0.1 + 0.2 == 0.3` is `False`. An amount has the
  precision of its currency; other values a `decimal.precision` record (`digits='Product
  Price'`, read with `self.env['decimal.precision'].precision_get(...)`). $uom_precision
- `fields.Float.compare(a, b, precision_digits=2)` returns a negative number, `0` or a
  positive number, like `cmp`: test it against `0`.

## Exceptions

- A `Float` without `digits` that is neither compared nor summed (a ratio only shown
  to the user) needs none of this.

# Declare every dependency of a computed field

Give a computed field one `_compute_<field>` method decorated with `@api.depends`
listing every field it reads (dotted paths for related records), and assign the field
on every record of `self`, in every branch.

```python
total = fields.Monetary(compute='_compute_total', store=True)

@api.depends('line_ids.price', 'line_ids.quantity')
def _compute_total(self):
    for book in self:
        book.total = sum(line.price * line.quantity for line in book.line_ids)
```

## Why

- A stored computed field is recomputed only when a field listed in `@api.depends`
  changes; a missing dependency leaves stale values in the database, with no error.
- A compute that leaves a record unassigned raises "Compute method failed to assign".
- `self` is a recordset: a compute that reads `self.x` directly breaks as soon as the
  ORM computes several records at once.

## What to know

- `store=True` makes the field searchable, sortable and groupable, at the cost of a
  column and of recomputations; leave it off for values only displayed.$compute_sql
- `readonly=False` on a stored compute makes the field editable: the compute fills
  it, the user can overwrite it, and it recomputes when a dependency changes. This
  replaces most `@api.onchange` methods.
- `compute_sudo`: a stored compute runs as superuser by default, a non-stored one as
  the current user. Set it explicitly when the value must or must not depend on the
  user's access rights.
- `precompute=True` on a stored compute computes it before the `INSERT` instead of
  after it. Use it on fields of lines created in batch through their parent; never on
  a field whose compute runs `search` or `_read_group`, and not on records created one
  by one, which then lose the batch prefetch. A `default` disables precomputation.
- `recursive=True` is required when a field depends on itself through a relation
  (`@api.depends('parent_id.complete_name')` computing `complete_name`).
- `@api.depends_context('company')` on a non-stored compute that reads the context; a
  stored compute must not depend on the context.
- One compute method may set several fields (each declares the same `compute`); it
  must assign all of them.
- No side effects in a compute: no `write` on other records, no `create`, no
  messages. The ORM decides when, how often and on which records it runs.

# Write inverse and search methods for computed fields

Give a computed field that users edit an `inverse` method, and a computed field that
users filter on a `search` method, instead of storing it only for that.

```python
author_name = fields.Char(
    compute='_compute_author_name',
    inverse='_inverse_author_name',
    search='_search_author_name',
)

def _inverse_author_name(self):
    for book in self:
        book.author_id.name = book.author_name

def _search_author_name(self, operator, value):
$search_example
```

- An inverse writes the edited value back to the stored fields it comes from; without
  `inverse`, a non-stored compute is read-only.
- $search_method
- Reusing one compute for several fields is fine; reusing one **inverse** is
  discouraged: while the inverse runs, every field sharing it is protected and reads
  as `False` when not cached, so the method sees wrong sibling values.

# Use `related` for a plain copy of another record's field

Declare a field that only shows a field of a related record as
`related='author_id.country_id'`, not as a compute.

- A related field is a computed field: not stored, read-only and not copied by
  default, and computed as superuser (give `related_sudo=False` to read it with the
  user's rights). `store=True` stores it; `readonly=False` writes changes through to
  the target record.
- `related` fields can't chain `One2many`/`Many2many` in the dependency path:
  the ORM does not reject it, it *silently truncates each x2many hop to its
  first record* and returns wrong data; reach the target through a `Many2one`
  (ending the chain on an x2many is fine).
- Attributes the field does not set (`string`, `help`, `selection`, `digits`,
  `comodel_name`) come from the target field.

# Keep `Json` for data the ORM does not query

Use `fields.Json` only for structured data the code reads and writes whole; use
`fields.Properties` for attributes users define, and real fields for anything searched,
grouped or validated.

- A `Json` field cannot be searched or indexed through the ORM, and a value must not
  be mutated in place: build a new value and assign it (`record.data = {**record.data,
  'key': value}`), or the change is never written.
- `book_properties = fields.Properties(definition='shelf_id.book_properties_definition')`
  stores on each record the values of properties whose definition lives in a
  `fields.PropertiesDefinition` field of a container (here the `Many2one` `shelf_id`):
  users add properties per container without changing the schema.$property_definition

# Extend a selection with `selection_add` and an `ondelete` policy

Add values to another module's `Selection` with `selection_add=[('value', "Label")]`
and an `ondelete={'value': policy}` entry for each new value; never redeclare the whole
`selection` list.

- `selection_add` keeps the values of every other module and places the new ones in
  the order given: `selection_add=[('lent', "Lent"), ('lost',)]` inserts `lent` before
  the existing `lost`.
- `ondelete` says what happens to the records holding a value when the module that
  added it is uninstalled: `'set null'` (default), `'cascade'` (delete them), `'set
  default'`, `'set <value>'`, or a callable receiving the records. A required
  selection field needs a policy other than `'set null'`.
- `selection` may name a method (`selection='_selection_target_model'`) for values
  computed at runtime; the values of a `Reference` field are model names.

# Index selectively

- `index=True` on fields that are both searched and selective (many distinct
  values). An index on a low-cardinality field (a boolean, a state) is wasted
  space and slows every write.
- `index` also accepts a type: `'btree_not_null'` (most values are empty, as on an
  optional `Many2one`) and `'trigram'` (for `ilike` searches on text). `True` is
  `'btree'`. `index` on a non-stored field does nothing.
- $custom_indexes

# Add stored fields to large tables cheaply

When you add a stored field to a model with many records, give it a `default` the
database can fill in one statement$init_storage_rule; a stored compute is
otherwise run for every existing record during the module update.
