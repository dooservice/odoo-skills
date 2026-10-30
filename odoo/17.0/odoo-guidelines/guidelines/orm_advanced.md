Key names in 17.0: `records.check_access_rights('write')` and `records.check_access_rule('write')` before `sudo()`; `flush_model`/`invalidate_model` around raw SQL; `tools.ormcache`; `cr.commit()` never; `with self.env.cr.savepoint():`.

Sections of this file:

- [Check access rights in code](#check-access-rights-in-code)
- [Flush and invalidate around raw SQL](#flush-and-invalidate-around-raw-sql)
- [Translate field values with the translation API](#translate-field-values-with-the-translation-api)
- [Lock rows you are about to change](#lock-rows-you-are-about-to-change)
- [Import, export and other public methods](#import-export-and-other-public-methods)
- [Methods and extension points](#methods-and-extension-points)
- [Transactions and exceptions](#transactions-and-exceptions)

# Check access rights in code

Check the current user's rights explicitly before code that bypasses them (`sudo()`) acts
on their behalf; the ORM checks them by itself only on calls made without `sudo()`.

- `records.check_access_rights('write')` checks the access list (`ir.model.access`) of the model; `records.check_access_rule('write')` checks the record rules on the records: call both. With `raise_exception=False`, `check_access_rights` returns a boolean instead of raising.
- `records._filter_access_rules('write')` returns the accessible subset.
- `check_field_access_rights(operation, field_names)` raises `AccessError` when a field of the list is restricted by `groups`; without names it returns the fields the user may access.
- Test the user's groups with `self.env.user.has_group('base.group_system')`; `self.user_has_groups('base.group_user,!base.group_portal')` takes the comma-separated syntax of `groups`.

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
  `records.modified(fnames)` so the ORM recomputes the dependent stored fields.
- After changing data that a `tools.ormcache` method caches, call `self.env.registry.clear_cache()`; `clear_caches()` is deprecated.

# Translate field values with the translation API

Read and write the value of a translatable field in another language with
`with_context(lang=...)`, or all languages at once with `get_field_translations(field_name, langs=None)` and `update_field_translations(field_name, {lang: value})`.

- `record.with_context(lang='fr_FR').name = "Titre"` writes the French value only.
- Writing a translatable field without `lang` in the context writes the value of the
  current language. The first value written is also stored as `en_US`, which every
  untranslated language falls back to.

# Lock rows you are about to change

When concurrent transactions may update the same records (counters, a queue), lock the
rows before changing them: run `SELECT id FROM <table> WHERE id IN %s FOR UPDATE NOWAIT` with `self.env.cr.execute` inside `with self.env.cr.savepoint():`, and turn the lock error into a retry or a `UserError`. A queue takes only the free rows with `FOR UPDATE SKIP LOCKED`.

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
- `onchange(values, field_names, fields_spec)` is the web client's entry point for form
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
