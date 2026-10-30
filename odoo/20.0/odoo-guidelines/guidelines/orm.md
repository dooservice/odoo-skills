Key names in 20.0: domains are `odoo.fields.Domain` (`&`, `|`, `~`, `Domain.AND`); `_read_group(domain, groupby, aggregates)`; `_compute_display_name`; `Command`; `records.grouped('author_id')`; `search_fetch(domain, field_names)`; `action_unarchive`.

Sections of this file:

- [Recordsets, domains and context](#recordsets-domains-and-context)
- [Recordset operations](#recordset-operations)
- [Environment and context switches](#environment-and-context-switches)
- [Search and read](#search-and-read)
- [Write x2many values with `Command`](#write-x2many-values-with-command)
- [Override `write`, `unlink` and `copy` in batch](#override-write-unlink-and-copy-in-batch)
- [Archive with `action_archive`](#archive-with-action_archive)

# Recordsets, domains and context

- Use recordset methods (`filtered`, `grouped`, `mapped`, `sorted`) where they read better than a loop.
- Recordsets/collections are booleans: write `if records:` / `if some_list:`,
  not `if len(...)`.
- Don't read a non-relational field on a multi-record set (it raises); iterate
  or `mapped`. Conversely, guard single-record assumptions with `ensure_one()`.
- Combine domains with `odoo.fields.Domain`: the `&`, `|`, `~` operators for
  domains written inline, `Domain.AND`/`Domain.OR` for a list of domains you
  already hold. Never hand-build `'&'`/`'|'` prefix-notation lists.
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
| `records.filtered(...)` | the records matching | takes a callable, a field path (`'author_id.active'`) or a `Domain` |
| `records.filtered_domain(domain)` | the records matching a domain, in memory | the same domain as `search`, evaluated on records already loaded |
| `records.sorted(key=None, reverse=False)` | the records sorted | `key` is a callable or an order string (`'name desc, id'`); without `key`, it applies `_order`; both in memory |
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
- Aggregate in SQL with `_read_group(domain, groupby, aggregates)`, which returns tuples with related records as recordsets: `for author, count in Book._read_group(domain, ['author_id'], ['__count'])`. Aggregates are `'field:sum'`, `'field:max'`, `'field:count_distinct'`, `'field:recordset'`, `'__count'`. `read_group` takes the same arguments and returns ids instead of records, for RPC; the web client's grouped views call `formatted_read_group` (from `web`).
- `name_search(name, domain=None, operator='ilike', limit=100)` returns
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
  change the values of the duplicate (`name` with " (copy)"), not `copy`.
- Changing a value in `create` or `write` only for the form belongs in a compute or
  an onchange, not in the override.

# Archive with `action_archive`

Archive and restore records with `action_archive()` and `action_unarchive()` on a
model with an `active` field.

- `search` skips archived records unless the context has `active_test=False`; so do
  the x2many fields, unless their `context` says otherwise.
- `toggle_active()` no longer exists: call `action_archive` or `action_unarchive`.
- Act on archiving in a `write` override that tests `'active' in vals`: both methods
  go through `write`.
