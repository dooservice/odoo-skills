# Reaching the database

Configuration is done through the ORM, so that Odoo's computes, constraints and access
rules run. There are four ways in; use the first one the environment offers. Whatever the
way, read before writing, and get the user's yes before any change that touches many
records, access, accounting or users.

## 1. Tools that go through the ORM

When the environment gives you tools that read and write records (an MCP server, a
hosting platform's own tools), use them. They usually run as a given user, add
confirmation and limits, and log what was done. Check which user they act as: a tool
that runs as an administrator sees records a normal user does not.

## 2. `odoo-bin shell`

On the server, with the same configuration file as the running instance:

```bash
odoo-bin shell -d <db> -c /etc/odoo/odoo.conf --no-http <<'EOF'
partner = env['res.partner'].search([('vat', '=', 'ESA12345674')], limit=1)
print(partner.read(['name', 'property_payment_term_id']))
EOF
```

- `env` is ready in the script. It runs as the superuser: access rights and record
  rules do not apply, so it sees and can change everything.
- The shell does not serve web requests; `--no-http` says so in the configuration as
  well, and is harmless next to the running instance.
- Nothing is saved unless the script ends with `env.cr.commit()`. The shell rolls back
  what is left when it exits. `env.cr.rollback()` throws away everything since the last
  commit.
- Output is what you `print()`. Print ids and values, not whole recordsets.

### Dry run

Make the change, read the result, and roll back. Show the result to the user; run it
again with `env.cr.commit()` once they agree.

```python
partners = env['res.partner'].search([('country_id.code', '=', 'MX'), ('customer_rank', '>', 0)])
partners.write({'property_payment_term_id': env.ref('account.account_payment_term_30days').id})
print(len(partners), partners[:5].mapped('property_payment_term_id.name'))
env.cr.rollback()
```

Some actions do things a rollback cannot undo: sending email immediately, calling an
external service (payment provider, e-invoicing authority, webhook). Do not dry-run those.

### Acting as someone else

```python
user = env['res.users'].search([('login', '=', 'maria@example.com')])
orders = env['sale.order'].with_user(user)
print(orders.search_count([]))                      # what Maria sees

company = env['res.company'].search([('name', '=', 'Acme Mexico')])
env['account.journal'].with_company(company).create({...})   # created for that company
```

- `with_user(user)` applies that user's access rights and record rules. Use it to
  reproduce a complaint, never to make changes in their name without saying so.
- `with_company(company)` sets the current company: defaults (`company_id`,
  company-dependent fields such as a partner's payment terms or a product's accounts) are
  read and written for that company.
- From the shell, `with_user(user)` sees all of that user's companies. The web client
  only sees the companies ticked in the company switcher; reproduce it with
  `with_context(allowed_company_ids=[...])`.
- `sudo()` lifts access checks. The shell is already superuser; in code that runs as a
  user (a server action, an automation), `sudo()` lets the code reach what the user
  cannot. Use it for one precise read or write, never on a whole flow.

## 3. External API

When there is no shell (Odoo Online, a server reached only over HTTP), call the ORM methods over HTTP with an API key.

**API key.** In Odoo, open your own preferences from the user menu (top right), tab
"Account Security" (up to 18.0) or "Security" (19.0 and later), section API Keys, button
"New API Key" (up to 18.0), "Add API Key" (19.0) or "Create API Key" (20.0). The key replaces
the password in API calls and acts with that user's rights. Use a dedicated user with
only the groups the work needs. From 18.0 keys can carry an expiration date.

### XML-RPC (all supported versions)

```python
import xmlrpc.client

url, db, login, key = 'https://odoo.example.com', 'prod', 'admin@example.com', '<api key>'
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, login, key, {})
models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object', allow_none=True)

def call(model, method, *args, **kwargs):
    return models.execute_kw(db, uid, key, model, method, list(args), kwargs)

taxes = call('account.tax', 'search_read', [('type_tax_use', '=', 'sale')],
             fields=['name', 'amount', 'company_id'], context={'lang': 'en_US'})
call('res.partner', 'write', [7], {'property_payment_term_id': 3})
```

- Each call is its own transaction, committed when it succeeds. There is no rollback
  and no dry run: read first, and write the smallest change.
- `env.ref()` does not exist here. Find an XML id through `ir.model.data`:
  `call('ir.model.data', 'search_read', [('module', '=', 'account'), ('name', '=', 'account_payment_term_30days')], fields=['res_id'])`.
- Methods whose name starts with `_` cannot be called remotely.
- A method that returns `None` makes the server fail to send the answer, after the
  change was already saved. Read the records again rather than trusting the error.
- From 19.0, every `/xmlrpc`, `/xmlrpc/2` and `/jsonrpc` call logs a warning that these
  endpoints are deprecated and scheduled for removal in Odoo 22. They still work in 19.0
  and 20.0; prefer JSON-2 there.

### JSON-2 (19.0 and later)

One HTTP POST per method call: `POST /json/2/<model>/<method>`.

```python
import requests

url, db, key = 'https://odoo.example.com', 'prod', '<api key>'
session = requests.Session()
session.headers.update({'Authorization': f'bearer {key}', 'X-Odoo-Database': db})

def call(model, method, ids=(), context=None, **kwargs):
    body = {'ids': list(ids), 'context': context or {}, **kwargs}
    response = session.post(f'{url}/json/2/{model}/{method}', json=body)
    response.raise_for_status()
    return response.json()

taxes = call('account.tax', 'search_read', domain=[('type_tax_use', '=', 'sale')],
             fields=['name', 'amount'], context={'lang': 'en_US', 'allowed_company_ids': [1]})
call('res.partner', 'write', ids=[7], vals={'property_payment_term_id': 3})
settings = call('res.config.settings', 'create', vals_list=[{'group_multi_currency': True}])
call('res.config.settings', 'execute', ids=settings)
```

- `ids` are the records the method runs on, `context` the context, and every other key
  is a keyword argument of the method, by its Python name (`vals` for `write`,
  `vals_list` for `create`, `domain`/`fields`/`limit` for `search_read`).
- `X-Odoo-Database` is only needed when the server hosts more than one database.
- A method that returns records answers with their ids.
- Each call is its own transaction, as with XML-RPC.
- The `api_doc` module (19.0 and later, installed automatically) serves `/doc`: the
  models, fields and methods this user can call, with example requests.

## 4. SQL, to look only

For a question the ORM answers slowly or awkwardly (counts across companies, history of
a sequence, rows a user cannot see), read with SQL. Never write: SQL skips computes,
constraints, access rules, the ORM cache and the chatter.

```bash
psql -d <db> -c "BEGIN READ ONLY; SELECT state, count(*) FROM account_move GROUP BY state; ROLLBACK;"
```

```python
env.cr.execute("SELECT id, name->>'en_US' FROM account_tax WHERE company_id = %s", [company.id])
print(env.cr.fetchall())
```

- Translatable fields are `jsonb`, one key per language: `name->>'en_US'`.
- Company-dependent fields (a partner's payment terms, a product's income account) live
  in `ir_property` up to 17.0, and from 18.0 in a `jsonb` column keyed by company id.
- Over the external API there is no SQL; use `search_read` and `search_count`.
