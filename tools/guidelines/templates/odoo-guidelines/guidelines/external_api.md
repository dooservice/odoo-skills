# Call Odoo from outside through the external API

Scripts, integrations and other servers call model methods through
$external_api_name; never through the web client's `/web/dataset/call_kw`, whose
arguments and session handling are internal and change between versions.

$endpoints

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
$key_usage
$key_lifetime
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
  with $check_access_call, or a group with
  `self.env.user.has_group('module.group_xmlid')`.
- RPC calls a method with the arguments the client sends: validate their types
  and sizes like any user input.
- Return plain data: a recordset is converted to its ids and `None` cannot be
  marshalled by XML-RPC, so return `True` when there is nothing to say.$readonly_methods

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
  $context_example.
- The server already replays a call that hits a concurrent update. Retry on
  the client only after a network error, with backoff, and make those calls
  idempotent: look the record up by its external reference before creating it.
  A `UserError` or an access error fails the same way every time.
