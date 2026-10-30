Key names in 17.0: XML-RPC (`/xmlrpc/2/common` `authenticate`, `/xmlrpc/2/object` `execute_kw`) or JSON-RPC (`POST /jsonrpc`), with the API key of a dedicated user; batch calls; `check_access_rights` and `check_access_rule` before `sudo()`.

Sections of this file:

- [Call Odoo from outside through the external API](#call-odoo-from-outside-through-the-external-api)
- [Authenticate integrations with an API key of a dedicated user](#authenticate-integrations-with-an-api-key-of-a-dedicated-user)
- [Expose only public, checked methods to RPC](#expose-only-public-checked-methods-to-rpc)
- [Batch external calls](#batch-external-calls)

# Call Odoo from outside through the external API

Scripts, integrations and other servers call model methods through
XML-RPC or JSON-RPC; never through the web client's `/web/dataset/call_kw`, whose
arguments and session handling are internal and change between versions.

- XML-RPC: `/xmlrpc/2/common` authenticates with
  `authenticate(db, login, api_key, {})`, which returns the user id (`False` when
  the credentials are wrong); `/xmlrpc/2/object` runs
  `execute_kw(db, uid, api_key, model, method, args, kwargs)`. The key is sent
  with every call.
- JSON-RPC: `POST /jsonrpc` with
  `{"jsonrpc": "2.0", "method": "call", "params": {"service": "object",
  "method": "execute_kw", "args": [db, uid, api_key, model, method, args, kwargs]}}`
  calls the same services.
- The `db` service (`/xmlrpc/2/db`) creates, duplicates and drops databases
  behind the master password; integrations never need it.

```python
import xmlrpc.client

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, login, api_key, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")
books = models.execute_kw(
    db, uid, api_key, "library.book", "search_read",
    [[("state", "=", "available")]],
    {"fields": ["name", "author_id"], "limit": 80, "context": {"lang": "en_US"}},
)
```

# Authenticate integrations with an API key of a dedicated user

An integration authenticates with an API key (`res.users.apikeys`) of a user
created for it, never with a person's password.

- Create the user with only the groups the integration needs; every call runs
  with that user's access rights and record rules, and its name appears in the
  chatter and `create_uid`/`write_uid` of what it changes.
- The user creates the key in Preferences > Account Security (the
  `res.users.apikeys.description` wizard). The key is shown once and stored
  hashed: keep it in the integration's secret store, never in a module, a data
  file or `ir.config_parameter`.
- The key replaces the password in `authenticate` and in every
  `execute_kw` call. A key made in the preferences has no scope and works for
  every RPC call of its user.
- Keys never expire: list and revoke the ones nobody uses.
- Revoke a leaked key in the user's Account Security preferences. Archiving the
  user disables all its keys at once; changing its password revokes none.

# Expose only public, checked methods to RPC

Every public method of a model can be called remotely by any user who can reach
the model, so a public method checks what it needs, and a method that must not
be called remotely is private.

- A name starting with `_` is refused by RPC, and so is a public name decorated
  with `@api.private`. Use `@api.private` for public helpers that other modules
  call but clients must not.
- A public method that writes with `sudo()` first checks the caller's rights
  with `check_access_rights` and `check_access_rule`, or a group with
  `self.env.user.has_group('module.group_xmlid')`.
- RPC calls a method with the arguments the client sends: validate their types
  and sizes like any user input.
- Return plain data: a recordset is converted to its ids and `None` cannot be
  marshalled by XML-RPC, so return `True` when there is nothing to say.

# Batch external calls

Each RPC call is one request and one transaction: send work in as few calls as
the data allows.

- Read with `search_read` (domain, `fields`, `limit`, `order`) instead of
  `search` then `read`; always pass `fields`, or every stored field is
  serialized.
- Create many records with one `create` call taking a list of values, which
  returns the list of ids.
- A call commits when it succeeds and rolls back entirely when it raises; two
  calls are two transactions, so an integration that needs all-or-nothing calls
  one server method that does the whole job.
- Pass the language, the companies and any other context explicitly instead of
  relying on the integration user's defaults, for example
  `{'context': {'lang': 'fr_FR', 'allowed_company_ids': [1]}}` in `kwargs`.
- The server already replays a call that hits a concurrent update. Retry on
  the client only after a network error, with backoff, and make those calls
  idempotent: look the record up by its external reference before creating it.
  A `UserError` or an access error fails the same way every time.
