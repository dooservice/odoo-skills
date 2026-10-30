Key names in 19.0: JSON-2, `POST /json/2/<model>/<method>` with `Authorization: bearer <api key>` and arguments by name; XML-RPC and `/jsonrpc` are deprecated; `/doc` lists what the database exposes; the API key of a dedicated user.

Sections of this file:

- [Call Odoo from outside through the external API](#call-odoo-from-outside-through-the-external-api)
- [Authenticate integrations with an API key of a dedicated user](#authenticate-integrations-with-an-api-key-of-a-dedicated-user)
- [Expose only public, checked methods to RPC](#expose-only-public-checked-methods-to-rpc)
- [Batch external calls](#batch-external-calls)

# Call Odoo from outside through the external API

Scripts, integrations and other servers call model methods through
the JSON-2 API; never through the web client's `/web/dataset/call_kw`, whose
arguments and session handling are internal and change between versions.

- JSON-2: `POST /json/2/<model>/<method>` with the headers
  `Authorization: bearer <api key>` and `X-Odoo-Database: <db>` (needed when the
  server hosts several databases) and a JSON body. The body holds `ids` (the
  records the method runs on), `context`, and every method argument **by
  name**: `search_read` takes `domain` and `fields`, `create` takes
  `vals_list`. The response body is the return value (recordsets become ids);
  errors come back as JSON with a 4xx/5xx status. Sending `ids` to an
  `@api.model` method is refused with 422.
- The `/doc` page (module `api_doc`, for users in its access group) lists the
  models, fields and methods the current database exposes.
- `/xmlrpc/2/common`, `/xmlrpc/2/object` and `/jsonrpc` still answer, served by
  the auto-installed `rpc` module, but they are deprecated: each call logs a
  warning and they are scheduled for removal in Odoo 22. Write new clients
  against JSON-2 and migrate old ones.
- The `db` service (`/xmlrpc/2/db`) creates, duplicates and drops databases
  behind the master password; integrations never need it.

```python
import requests

response = requests.post(
    f"{url}/json/2/library.book/search_read",
    headers={"Authorization": f"bearer {api_key}", "X-Odoo-Database": db},
    json={
        "domain": [["state", "=", "available"]],
        "fields": ["name", "author_id"],
        "limit": 80,
        "context": {"lang": "en_US"},
    },
    timeout=30,
)
response.raise_for_status()
books = response.json()
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
- The key goes in the `Authorization: bearer` header of each JSON-2 call (or
  replaces the password on the deprecated endpoints). A key made in the
  preferences has no scope and works for every RPC call of its user.
- A key has an `expiration_date`. Only administrators create keys without
  one; other users are limited to the longest `api_key_duration` (days) of
  their groups. An integration renews its own key with
  `res.users.apikeys.generate(key, scope, name, expiration_date)` then
  `revoke(old_key)`: allowed to administrators, and to other users once the
  system parameter `base.enable_programmatic_api_keys` is set.
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
  with `check_access('write')`, or a group with
  `self.env.user.has_group('module.group_xmlid')`.
- RPC calls a method with the arguments the client sends: validate their types
  and sizes like any user input.
- Return plain data: a recordset is converted to its ids and `None` cannot be
  marshalled by XML-RPC, so return `True` when there is nothing to say.
- Decorate with `@api.readonly` a method that never writes: JSON-2 and the
  web client then run it on a read-only cursor.

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
  `"context": {"lang": "fr_FR", "allowed_company_ids": [1]}` in the body.
- The server already replays a call that hits a concurrent update. Retry on
  the client only after a network error, with backoff, and make those calls
  idempotent: look the record up by its external reference before creating it.
  A `UserError` or an access error fails the same way every time.
