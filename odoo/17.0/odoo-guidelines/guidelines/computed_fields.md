Key names in 17.0: `@api.depends` on every compute, assigning every record; `store`, `readonly=False`, `compute_sudo`, `precompute`, `recursive`; an `inverse` method to edit, a `search` method returning a domain list to filter; `related` for a plain copy.

Sections of this file:

- [Declare every dependency of a computed field](#declare-every-dependency-of-a-computed-field)
- [Write inverse and search methods for computed fields](#write-inverse-and-search-methods-for-computed-fields)
- [Use `related` for a plain copy of another record's field](#use-related-for-a-plain-copy-of-another-records-field)

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
  column and of recomputations; leave it off for values only displayed.
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
    return [('author_id.name', operator, value)]
```

- An inverse writes the edited value back to the stored fields it comes from; without
  `inverse`, a non-stored compute is read-only.
- A search method receives `(operator, value)` as written in the domain (`'='`, `'!='`, `'ilike'`, `'in'`, ...) and returns a domain on stored fields. Handle every operator a user can pick in the search panel, and raise `UserError` for the others.
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
