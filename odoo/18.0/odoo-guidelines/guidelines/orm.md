# Recordsets, domains and context

- Use recordset methods (`filtered`, `grouped`, `mapped`, `sorted`) where they read better than a loop.
- Recordsets/collections are booleans: write `if records:` / `if some_list:`,
  not `if len(...)`.
- Don't read a non-relational field on a multi-record set (it raises); iterate
  or `mapped`. Conversely, guard single-record assumptions with `ensure_one()`.
- Combine domains with `odoo.osv.expression.AND([...])` / `OR([...])`; never
  hand-build `'&'`/`'|'` prefix-notation lists.
- Propagate context with `with_context(...)` (it's a frozendict, immutable);
  name custom context keys carefully and prefix module-specific ones (a stray
  `default_<field>` in context leaks into unrelated `create` calls).
- `with_context(key=value)` adds keys to the current context; `with_context(dict)`
  **replaces** the whole context with the dict. Use the keyword form unless dropping
  every other key is the point.

# Recordset operations

What each operation of a recordset does, and its trap:

| Operation | Returns | Note |
| --- | --- | --- |
| `self.env['library.book'].browse(ids)` | the records with these ids, without a query | it does not check that they exist: `exists()` does |
| `records.exists()` | the subset still in the database | call it on ids that may have been deleted (from a cron, a message, the URL) |
| `records.ids` | the list of ids | |
| `records.ensure_one()` | the record itself, or raises | first line of a method meant for one record (`action_*`) |
| `records.mapped('author_id.name')` | a list of values, or a recordset for relational fields (duplicates removed) | a callable works too |
| `records.filtered(...)` | the records matching | takes a callable or a field path (`'author_id.active'`) |
| `records.filtered_domain(domain)` | the records matching a domain, in memory | the same domain as `search`, evaluated on records already loaded |
| `records.sorted(key=None, reverse=False)` | the records sorted | `key` is a callable or one field name; without `key`, it runs a `search` to apply `_order` |
| `records.grouped('author_id')` | a dict `{key: records}` | a callable works too; in memory, no query |
| `a \| b`, `a & b`, `a - b` | union (without duplicates, in order), intersection, difference | `a + b` concatenates and keeps duplicates |
| `a.union(b, c)`, `a.concat(b, c)` | the same as `\|` and `+`, for several recordsets at once | |
| `record in records`, `a <= b`, `a < b` | membership and inclusion | compares ids, not values |
| `records.update(values)` | nothing; assigns each value on every record | on new records (onchange, `new`); on stored records it is a `write` per field |
| `self.env['library.book'].new(values)` | a record in memory only, with a `NewId` | to compute values (onchange) without creating anything; never stored |

# Environment and context switches

Each switch returns a new recordset on a new environment; `self` is unchanged:

- `sudo()`: bypasses access rights and record rules. Keep it on the smallest
  recordset and the shortest expression that needs it; never return sudoed records to
  the caller or the client. `sudo()` does not change the user: `self.env.user` stays
  the same, `self.env.su` is `True`.
- `with_user(user)`: runs as another user, with their rights (not superuser).
- `with_company(company)`: makes `company` the current company (`self.env.company`)
  and first allowed company, for defaults, company-dependent fields and rules.
- `with_context(...)`: changes the context; see
  [Recordsets, domains and context](#recordsets-domains-and-context). Common keys:
  `lang`, `tz`, `active_test=False` (include archived records), `default_<field>`,
  `tracking_disable` (on `mail.thread` models).
- `with_env(env)`: the same records on another environment (another cursor).
- `with_prefetch(prefetch_ids)`: sets which records are read together with these
  ones; rarely needed, the ORM prefetches the whole recordset being iterated.
- From the environment: `self.env.ref('module.xml_id')` (raises if missing; pass
  `raise_if_not_found=False` to get `None`), `self.env.user`, `self.env.company`,
  `self.env.companies` (all allowed), `self.env.lang`, `self.env.context`,
  `self.env.cr`.

# Search and read

- `search(domain, offset=0, limit=None, order=None)` returns records; set `limit` when
  you need only some, and `order` as in `_order`.
- `search_count(domain, limit=None)` counts in SQL; `limit` stops counting early when
  you only test a threshold. Never `len(search(...))`.
- `search_fetch(domain, field_names)` searches and loads the given fields in one query, and `records.fetch(field_names)` loads them for records already in hand. Use them when you know what you will read; plain iteration also prefetches, but loads every prefetchable field.
- `read(fields)` and `search_read(domain, fields)` return dicts: for RPC and
  controllers answering in JSON, not for business code, which uses records.
- Aggregate in SQL with `_read_group(domain, groupby, aggregates)`, which returns tuples with related records as recordsets: `for author, count in Book._read_group(domain, ['author_id'], ['__count'])`. Aggregates are `'field:sum'`, `'field:max'`, `'field:count_distinct'`, `'field:recordset'`, `'__count'`. `read_group` returns the dicts of the web client's grouped views; business code uses `_read_group`.
- `name_search(name, args=None, operator='ilike', limit=100)` returns
  `(id, display_name)` pairs, the suggestions of a `Many2one` input; to change what it
  matches, set `_rec_names_search`, or override `_search_display_name(operator, value)`, which returns the domain of a search on `display_name`.
- `name_create(name)` creates a record from its display name only (the "Create"
  entry of a `Many2one` input); it needs `_rec_name`.
- The display name comes from `_compute_display_name`; override it with `@api.depends` on what it
  reads. `name_get` does not exist in this version.
- `default_get` returns the defaults of a `create` (field defaults,
  `ir.default`, `default_<field>` context keys); override it to compute a default that
  depends on several fields or on the context, calling `super()` first.
- `fields_get(allfields, attributes)` describes the fields for clients.
- `get_metadata()` returns creation and update information and the external id;
  `get_external_id()` returns `{id: 'module.xml_id'}`.

# Write x2many values with `Command`

Write `One2many` and `Many2many` values with `Command` (`from odoo import Command`),
not with the bare `(0, 0, vals)` tuples.

| Command | Tuple | Effect |
| --- | --- | --- |
| `Command.create(vals)` | `(0, 0, vals)` | create a record and link it |
| `Command.update(id, vals)` | `(1, id, vals)` | write on a linked record |
| `Command.delete(id)` | `(2, id, 0)` | delete the record from the database |
| `Command.unlink(id)` | `(3, id, 0)` | remove the link only; on a `One2many`, the line is deleted when its `Many2one` has `ondelete='cascade'`, else that `Many2one` is emptied |
| `Command.link(id)` | `(4, id, 0)` | add a link to an existing record |
| `Command.clear()` | `(5, 0, 0)` | remove every link, with the same effect on `One2many` lines as `unlink` |
| `Command.set(ids)` | `(6, 0, ids)` | replace the links by exactly these records |

- Assigning a recordset (`book.tag_ids = tags`) is a `Command.set`; reading always
  returns records, never commands.
- A comodel with `_allow_sudo_commands = False` refuses commands sent from a `sudo()`
  or `with_user()` environment.

# Override `write`, `unlink` and `copy` in batch

Override `write`, `unlink` and `copy` for the whole recordset: loop over `self` only
for what differs per record, and call `super()` once.

```python
def write(self, vals):
    if 'shelf_id' in vals:
        self._check_shelf_capacity(vals['shelf_id'])
    return super().write(vals)
```

- `write(vals)` applies the same values to every record of `self`; never call `write`
  per record inside a loop when the values are the same.
- Test the keys of `vals` before doing expensive work: most writes do not touch the
  fields you care about.
- `unlink()`: put business checks in `@api.ondelete` (see
  [Block deletion](api.md#block-deletion-with-apiondelete-not-an-unlink-override)),
  not in `unlink`.
- `copy(default)` duplicates every record of `self` with one `create` and returns the copies in the same order.
- `copy_data(default)` returns the values `copy` will create; override it to
  change the values of the duplicate (`name` with " (copy)"), not `copy`. `copy` then calls `copy_translations` to copy the translations of the duplicated fields.
- Changing a value in `create` or `write` only for the form belongs in a compute or
  an onchange, not in the override.

# Check access rights in code

Check the current user's rights explicitly before code that bypasses them (`sudo()`) acts
on their behalf; the ORM checks them by itself only on calls made without `sudo()`.

- `records.check_access('write')` checks the access list of the model and the record rules on the records, and raises `AccessError`; `records.has_access('write')` returns a boolean instead, and `records._filtered_access('write')` the accessible subset. On an empty recordset they check the model only.
- `check_access_rights` and `check_access_rule` are deprecated: replace them with `check_access`.
- `check_field_access_rights(operation, field_names)` raises `AccessError` when a field of the list is restricted by `groups`; without names it returns the fields the user may access.
- Test the user's groups with `self.env.user.has_group('base.group_system')`, or `self.env.user.has_groups('base.group_user,!base.group_portal')` for the comma-separated syntax of `groups`. `user_has_groups` no longer exists.

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
`with_context(lang=...)`, or all languages at once with `get_field_translations(field_name, langs=None)` and `update_field_translations(field_name, {lang: value}, source_lang=...)`.

- `record.with_context(lang='fr_FR').name = "Titre"` writes the French value only.
- Writing a translatable field without `lang` in the context writes the value of the
  current language. The first value written is also stored as `en_US`, which every
  untranslated language falls back to.

# Archive with `action_archive`

Archive and restore records with `action_archive()` and `action_unarchive()` on a
model with an `active` field.

- `search` skips archived records unless the context has `active_test=False`; so do
  the x2many fields, unless their `context` says otherwise.
- `toggle_active()` inverts `active` on each record; call the explicit methods instead, which say what they do.
- Act on archiving in a `write` override that tests `'active' in vals`: both methods
  go through `write`.

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
