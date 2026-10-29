# Method decorators

Every decorator of `odoo.api` in 16.0, and what it is for:

| Decorator | Use it on |
| --- | --- |
| `@api.depends('field', 'partner_id.name')` | a compute method: every field it reads, dotted paths included; see [Computed fields](fields.md#declare-every-dependency-of-a-computed-field) |
| `@api.depends_context('company')` | a non-stored compute that reads context keys (`company`, `uid`, `lang`, `active_test`, or your own) |
| `@api.constrains('field', ...)` | a Python check that raises `ValidationError`; see [below](#validate-with-apiconstrains-and-know-what-it-does-not-see) |
| `@api.onchange('field', ...)` | form-only assistance; see [below](#use-apionchange-only-for-form-side-help) |
| `@api.model` | a method where `self` is the model, not records: it is called on `self.env['library.book']` and never reads `self`'s records |
| `@api.model_create_multi` | every `create` override; see [below](#override-create-with-apimodel_create_multi) |
| `@api.ondelete(at_uninstall=False)` | a check that forbids deleting some records; see [below](#block-deletion-with-apiondelete-not-an-unlink-override) |
| `@api.autovacuum` | a private method the daily `ir.autovacuum` cron calls for garbage collection; its name must start with `_` (asserted) |
| `@api.private` | a public method that must not be callable over RPC; see [Methods and extension points](orm.md#methods-and-extension-points) |
| `@api.returns('self', lambda value: value.id)` | core methods returning records, so that RPC callers get ids; overrides inherit it, and new methods do not need it |
| `@api.model_create_single` | nothing new: it wraps a `create` that takes one dict, creates records one by one and logs a warning; use `@api.model_create_multi` |

- An override repeats the decorator of the method it overrides (`@api.constrains`,
  `@api.onchange`, `@api.ondelete`, `@api.model`, `@api.model_create_multi`): the ORM
  reads it on the last override only, so an undecorated override silently stops being
  a constraint, an onchange or a batch `create`. `@api.depends` is the exception: the
  dependencies of every override of a compute method add up, so an override declares
  only the fields it starts reading.
- `@api.depends` and `@api.constrains` also accept one callable returning the field
  names (`@api.depends(lambda self: self._get_depends())`) when the list depends on
  the model; use it only then.
- `@api.readonly` does not exist in this version: every RPC call runs on a read-write cursor.

# Override `create` with `@api.model_create_multi`

Decorate every `create` override with `@api.model_create_multi`, take `vals_list`,
and call `super().create(vals_list)` once.

```python
@api.model_create_multi
def create(self, vals_list):
    for vals in vals_list:
        vals.setdefault('code', self._default_code())
    books = super().create(vals_list)
    books.filtered('is_published')._notify_readers()
    return books
```

## Why

- The decorator accepts both `create(vals)` and `create([vals, ...])` from callers
  and always hands the method a list, so one override serves both.
- `@api.model` on `create` turns it into `@api.model_create_single`: it still works, but creates the records one by one and logs a warning.
- Work done after `super()` runs once on the whole recordset; looping
  `super().create(vals)` per dict is one `INSERT` (and one round of computes) per
  record.

## Exceptions

- To pair each record with its values after `super()`, `zip(records, vals_list)`:
  `create` returns the records in the order of `vals_list`.

# Block deletion with `@api.ondelete`, not an `unlink` override

Put a business check that forbids deleting records in a method decorated with
`@api.ondelete(at_uninstall=False)`, named `_unlink_except_<condition>` (or
`_unlink_if_<condition>`), that raises `UserError`. Do not override `unlink` to raise.

```python
@api.ondelete(at_uninstall=False)
def _unlink_except_lent(self):
    if any(book.state == 'lent' for book in self):
        raise UserError(_("A lent book cannot be deleted."))
```

## Why

- An `unlink` override that raises also runs while the module is uninstalled, and
  then leaves the module's records and tables behind. With `at_uninstall=False` the
  check is skipped during uninstallation.

## Exceptions

- `at_uninstall=True` only for a check that must hold even when the module is removed
  (the last remaining language, a record the whole database depends on).
- Overriding `unlink` stays right for work that must happen on every deletion
  (cleaning related data), as long as it calls `super()` and does not raise for
  business reasons.

# Validate with `@api.constrains`, and know what it does not see

Write each Python invariant as a `@api.constrains('field', ...)` method that loops
over `self` and raises `ValidationError` with a translated message.

## Why and limits

- The method runs after `create` and `write`, only when one of the listed fields is
  in the values written. A field left out of `create` (absent from the form, not in
  the import) is not checked: if the absence of a value is the error, make the field
  `required` or check it in `create`.
- Dotted names (`partner_id.country_id`) never trigger it; the ORM only logs a
  warning. List fields of this model that are stored or have an inverse: a change on
  a related record does not trigger the check.
- It runs in Python on the records written; it does not protect against concurrent
  transactions or raw SQL. An invariant on a single row or uniqueness belongs in an
  SQL constraint or a unique index (see
  [SQL constraints and indexes](models.md#declare-sql-constraints-and-indexes-on-the-model)).

# Use `@api.onchange` only for form-side help

Use `@api.onchange` only to help the user while a form is being edited (prefill
a value, show a warning); compute any value that must also hold for records
created by code, imports or RPC with a computed field instead.

## Why

- An onchange runs only in the form view, on a pseudo-record holding the form's
  values. `create` and `write` from code never trigger it, so data written outside the
  form misses whatever it sets.
- A stored computed field with `readonly=False` covers both cases: it recomputes when
  its dependencies change, in the form and on the server, and the user can still
  overwrite it.

## Rules inside an onchange

- Assign fields on `self`; never call `create`, `write`, `unlink` or `search`
  with side effects there: the record may not exist yet.
- To warn the user, return `{'warning': {'title': ..., 'message': ...}}`: the web client
  shows a notification, or a dialog with `'type': 'dialog'`. Returning `{'domain': ...}` is deprecated and logs a warning: put the domain on the field or in the view.
- Only plain field names are supported: dotted names are ignored.
- A `One2many` or `Many2many` field cannot change itself through its own onchange.
