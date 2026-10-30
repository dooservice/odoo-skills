# Check access rights in code

Check the current user's rights explicitly before code that bypasses them (`sudo()`) acts
on their behalf; the ORM checks them by itself only on calls made without `sudo()`.

$access_checks
- $field_access
- $user_groups

# Flush and invalidate around raw SQL

Before raw SQL reads a table, flush the pending ORM writes of the fields it reads;
after raw SQL writes, invalidate the cache of what it changed.

```python
self.env['library.book'].flush_model(['shelf_id', 'state'])
self.env.cr.execute(...)
self.env['library.book'].invalidate_model(['state'])
```

- The ORM delays writes until a flush: before a `search`, at commit, or when asked.
  Raw SQL that does not flush reads stale rows.
- `flush_model(fnames)` flushes fields of a whole model, `flush_recordset(fnames)` of
  some records, `self.env.flush_all()` everything.
- `invalidate_model(fnames)`, `invalidate_recordset(fnames)` and
  `self.env.invalidate_all()` drop cached values so the next read queries the
  database.
- After a raw `UPDATE` of fields that other fields depend on, call
  `records.modified(fnames)` so the ORM recomputes the dependent stored fields.$deprecated_cache$clear_caches

# Translate field values with the translation API

Read and write the value of a translatable field in another language with
`with_context(lang=...)`, or all languages at once with $translation_methods.

- `record.with_context(lang='fr_FR').name = "Titre"` writes the French value only.
- Writing a translatable field without `lang` in the context writes the value of the
  current language. The first value written is also stored as `en_US`, which every
  untranslated language falls back to.

# Lock rows you are about to change

When concurrent transactions may update the same records (counters, a queue), lock the
rows before changing them: $locking

# Import, export and other public methods

- `load(fields, data)` imports rows like the import screen (external ids, relation
  names) and returns ids and messages; `export_data(fields)` is its counterpart.
  Use them for data exchange, not for business logic.
- `get_base_url()` returns the base URL for links to a record (`web.base.url`, or
  the record's website when `website` is installed); use it in mails and reports
  instead of building URLs from the request.
- `is_transient()` says whether the model is a `TransientModel`.
- `init()` runs at each module install or update, after the table is created; it
  creates SQL objects the fields cannot (views, special indexes).
- `onchange(values, $onchange_args)` is the web client's entry point for form
  changes; never call it from business code.

# Methods and extension points

- Methods are private (`_` prefix) by default. A public name is an RPC entry
  point: make one only when it must be callable from outside, and decorate
  with `@api.private` a public name that must not be exposed.
- Logic that another module actually overrides goes in its own small method
  (`self._get_partner_domain()`); other modules extend methods, not lines.
  Don't pre-split for extension points that don't exist yet.
- An override calls `super()` and passes its arguments through unchanged; see
  [Override with super()](models.md#override-with-super-and-the-same-signature).
- Don't use `odoo.http.request` in models: it is absent in crons, RPC, tests
  and the shell. Pass what the model needs in from the controller.

# Transactions and exceptions

- **Never** call `cr.commit()` / `cr.rollback()` unless you opened your own
  cursor; the framework owns the transaction. Any unavoidable commit needs an
  explicit comment justifying it.
- Catch **specific** exceptions over the smallest possible block; let unexpected
  ones propagate to the framework. To recover from framework exceptions, wrap the
  work in `with self.env.cr.savepoint():` (more than 64 savepoints in one
  transaction degrades PostgreSQL, so bound batch sizes).
- Errors for the user are `UserError` / `ValidationError` / `AccessError` with a
  translated message; never a bare `Exception`.
