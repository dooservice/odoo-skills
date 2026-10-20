# Mail servers

Outgoing mail goes through `ir.mail_server` records (SMTP); without one, Odoo uses the
server given in its configuration file, if any. Every email is first a `mail.mail` in a
queue that a scheduled action sends. Replies come back through an incoming server
(`fetchmail.server`) or a mail gateway, and land on the record whose alias they were
sent to. The sender, catchall and bounce addresses come from the alias domain.

```python
print(env['ir.mail_server'].search_read([], ['name', 'smtp_host', 'smtp_port', 'smtp_encryption', 'smtp_user', 'from_filter', 'sequence', 'active']))
print(env['fetchmail.server'].search_read([], ['name', 'server_type', 'server', 'state', 'object_id', 'active']))
print(env['mail.mail'].read_group([], ['state'], ['state']))
print(env['ir.config_parameter'].get_param('database.is_neutralized'))
```

## Outgoing server

```python
server = env['ir.mail_server'].create({
    'name': 'Company SMTP', 'smtp_host': 'smtp.example.com', 'smtp_port': 587,
    'smtp_encryption': 'starttls', 'smtp_authentication': 'login',
    'smtp_user': 'odoo@example.com', 'smtp_pass': '...', 'from_filter': 'example.com',
})
server.test_smtp_connection()
env.cr.commit()
```

- `smtp_encryption`: `none`, `starttls`, `ssl` in 16.0 to 18.0. From 19.0 `starttls`
  and `ssl` encrypt without checking the certificate; `starttls_strict` and
  `ssl_strict` also validate it. Prefer the strict ones in 19.0+.
- `smtp_authentication`: `login`, `certificate`; 17.0+ adds `cli`. `google_gmail` and
  `microsoft_outlook` add `gmail` and `outlook` (OAuth), set up from the form.
- `from_filter`: the addresses or domain this server may send as. One value in 16.0; a
  comma-separated list from 17.0. Odoo takes, by `sequence`, the first active server
  whose filter matches the sender's address, then its domain.
- When no filter matches the sender, Odoo sends as the default address (for example
  `notifications@example.com`) through a server that accepts it, else through the first
  server without a filter. Users then see that address as sender: expected, not a bug.
- Ask the user for credentials; never print `smtp_pass` back.

## Sender, catchall and bounce

- **16.0**: system parameters through settings: `alias_domain` (parameter
  `mail.catchall.domain`); `mail.catchall.alias`, `mail.bounce.alias` and
  `mail.default.from` are parameters without a setting.
- **17.0+**: a `mail.alias.domain` record per domain (`name`, `catchall_alias`,
  `bounce_alias`, `default_from`), linked to each company by `alias_domain_id` (setting
  `alias_domain_id`).

```python
# 17.0+
domain = env['mail.alias.domain'].create({'name': 'example.com', 'default_from': 'notifications'})
env['res.config.settings'].with_company(company).create({'alias_domain_id': domain.id}).execute()
# 16.0
env['res.config.settings'].create({'alias_domain': 'example.com'}).execute()
env.cr.commit()
```

- The DNS (SPF, DKIM, DMARC) of the domain must allow the SMTP server. That is outside
  Odoo: tell the user.

## Incoming mail and aliases

```python
fetch = env['fetchmail.server'].create({
    'name': 'Sales inbox', 'server_type': 'imap', 'server': 'imap.example.com', 'port': 993,
    'is_ssl': True, 'user': 'sales@example.com', 'password': '...',
    'object_id': env.ref('crm.model_crm_lead').id,
})
fetch.button_confirm_login()
env.cr.commit()
```

- `server_type`: `imap`, `pop`, `local`; Gmail and Outlook add OAuth types.
- `object_id` only applies to mail that matches no alias and no thread.
- Aliases: `alias_name` on a sales team (creates leads), on a journal (creates vendor
  bills or invoices), on a project. The full address is `alias_name@<alias domain>`.
  `alias_contact`: `everyone`, `partners`, `followers`.
- The settings checkbox `external_email_server_default` (Custom Email Servers) shows the
  server menus in Settings; records work through the ORM either way.

## The queue

`mail.mail.state`: `outgoing`, `sent`, `received`, `exception`, `cancel`. The scheduled
action `mail.ir_cron_mail_scheduler_action` sends `outgoing` ones.

```python
failed = env['mail.mail'].search([('state', '=', 'exception')], order='id desc', limit=20)
print(failed.mapped(lambda m: (m.id, m.email_to, m.failure_type, m.failure_reason)))
failed.action_retry()
env.cr.commit()
```

- Fix the cause first (`failure_reason`): authentication, from not allowed, recipient
  invalid. `action_retry()` only puts `exception` mails back to `outgoing`.
- Many old failures: ask before retrying all, they go to real customers.

## Neutralized copies send nothing

A neutralized database (a test or staging copy) has all mail servers archived, a dummy
active server "neutralization - disable emails" on host `invalid`, incoming servers
archived and scheduled actions off. Mails queue up and fail. Check
`database.is_neutralized` before diagnosing "emails do not leave", and do not
re-activate real servers in a copy without the user's explicit yes: customers would
receive test mail.
