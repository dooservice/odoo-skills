# Mail servers

Outgoing mail goes through `ir.mail_server` records (SMTP); without one, Odoo uses the
server given in its configuration file, if any. Every email is first a `mail.mail` in a
queue that a scheduled action sends. Replies come back through an incoming server
(`fetchmail.server`), a redirection to Odoo's mail gateway, or DNS, and land on the record
whose alias they were sent to. The sender, catchall and bounce addresses come from the
alias domain. This recipe needs only the `mail` module; Gmail and Outlook OAuth
(`google_gmail`, `microsoft_outlook`) are named where they change a field, and the DNS of
the domain is outside Odoo.

## Before you start

- Apps: `mail` (installed with any app that sends email). `google_gmail` and
  `microsoft_outlook` add OAuth sign-in to both kinds of server.
- Settings: `external_email_server_default` (Custom Email Servers) shows the server
  buttons in Settings; records work through the ORM either way. Developer mode for
  Settings ‣ Technical ‣ Email.
- Credentials: ask the user for them; never print `smtp_pass` or `password` back.
- Read first:

```python
print(env['ir.mail_server'].search_read([], ['name', 'smtp_host', 'smtp_port', 'smtp_encryption', 'smtp_user', 'from_filter', 'sequence', 'active']))
print(env['fetchmail.server'].search_read([], ['name', 'server_type', 'server', 'state', 'object_id', 'active']))
print({state: env['mail.mail'].search_count([('state', '=', state)]) for state in ('outgoing', 'exception', 'sent')})
ICP = env['ir.config_parameter']
print(ICP.get_bool('database.is_neutralized') if hasattr(ICP, 'get_bool') else ICP.get_param('database.is_neutralized'))   # 20.0 / up to 19.0
```

A neutralized database sends nothing (see Pitfalls): check it before anything else.

## The standard flow

1. **Turn on custom email servers.** Settings ‣ General Settings ‣ Discuss (16.0, 17.0)
   or Emails (18.0 to 20.0) ‣ Custom Email Servers, then Save.

   ```python
   env['res.config.settings'].create({'external_email_server_default': True}).execute()
   env.cr.commit()
   ```

   Leaves the Outgoing and Incoming Email Servers buttons visible in that section.

2. **Add the outgoing server and test it.** Same section ‣ Outgoing Email Servers ‣ New
   (or Settings ‣ Technical ‣ Email ‣ Outgoing Mail Servers), fill the values of the
   email provider, set FROM Filtering, and click Test Connection.

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
   - `from_filter`: the addresses or domain this server may send as. One value in 16.0;
     a comma-separated list from 17.0. Odoo takes, by `sequence`, the first active
     server whose filter matches the sender's address, then its domain.
   - When no filter matches the sender, Odoo sends as the default address (for example
     `notifications@example.com`) through a server that accepts it, else through the
     first server without a filter. Users then see that address as sender: expected,
     not a bug.
   - `test_smtp_connection()` raises an error with the server's answer when it fails;
     a successful test does not prove the provider will accept every sender.

   Leaves an active server; mail is sent through it from the next queue run.

3. **Set the alias domain.** 17.0+: Settings ‣ General Settings ‣ Discuss (17.0) or
   Emails (18.0+) ‣ Alias Domain; in developer mode, Settings ‣ Technical ‣ Email ‣
   Alias Domains sets the Bounce, Catchall and Default From aliases. 16.0: the Alias
   Domain field in Settings ‣ General Settings ‣ Discuss; catchall, bounce and default
   from are system parameters (Settings ‣ Technical ‣ Parameters ‣ System Parameters).

   ```python
   # 17.0+
   domain = env['mail.alias.domain'].create({'name': 'example.com', 'default_from': 'notifications'})
   env['res.config.settings'].with_company(company).create({'alias_domain_id': domain.id}).execute()
   # 16.0
   env['res.config.settings'].create({'alias_domain': 'example.com'}).execute()
   env.cr.commit()
   ```

   - **16.0**: `alias_domain` is the parameter `mail.catchall.domain`;
     `mail.catchall.alias`, `mail.bounce.alias` and `mail.default.from` are parameters
     without a setting.
   - **17.0+**: a `mail.alias.domain` record per domain (`name`, `catchall_alias`,
     `bounce_alias`, `default_from`), linked to each company by `alias_domain_id`. The
     first alias domain created is given to every company.
   - Changing bounce, catchall or default from loses replies to emails already sent
     with the old addresses unless the mailbox still redirects them: ask first.

   Leaves the company sending as `<default from>@<domain>` and receiving replies on
   `<catchall>@<domain>`.

4. **Allow the server in the domain's DNS.** SPF, DKIM and DMARC of the domain must
   allow the SMTP server. That is outside Odoo: tell the user, and point them to their
   provider's documentation.

   Leaves nothing changed in Odoo.

5. **Receive replies.** Odoo recommends redirecting each mailbox (catchall, bounce and
   every alias) to Odoo; on a self-hosted server that needs the mail gateway script, set
   up by whoever runs the server. Otherwise add an incoming server per mailbox: Settings
   ‣ General Settings ‣ Discuss / Emails ‣ Incoming Email Servers (or Settings ‣
   Technical ‣ Email ‣ Incoming Mail Servers) ‣ New, then Test & Confirm. Prefer IMAP to
   POP.

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
   - `object_id` (Actions to Perform on Incoming Mails) only applies to mail that
     matches no alias and no thread; Odoo's guide leaves it empty for the catchall.
   - Fetching runs from the scheduled action `mail.ir_cron_mail_gateway_action`
     ("Mail: Fetchmail Service"), every 5 minutes by default: not instant.

   Leaves the server in state `done` (confirmed) after a successful login.

6. **Name the aliases.** Each alias is set on the record it feeds: a sales team (creates
   leads), a journal (creates vendor bills or invoices), a project. All aliases are in
   Settings ‣ Technical ‣ Email ‣ Aliases.

   ```python
   team = env.ref('sales_team.team_sales_department')
   team.write({'alias_name': 'leads', 'alias_contact': 'everyone'})
   env.cr.commit()
   ```

   The full address is `alias_name@<alias domain>`; `alias_contact`: `everyone`,
   `partners`, `followers`. The mailbox must exist (or redirect) on the mail server too.

   Leaves mail to that address creating or following up records of that model.

## Variations

- **One server for transactional mail, another for mass mailing.** Two outgoing servers;
  the transactional one gets the lower `sequence` (Priority). Email Marketing then picks
  its own server in its settings (Dedicated Server).
- **Gmail or Outlook with OAuth.** Install `google_gmail` or `microsoft_outlook` (with
  the user's yes), then choose Gmail or Outlook in the server's authentication; the
  sign-in is done from the form, not by script.
- **One sender for every email.** In developer mode, set Default From Alias on the alias
  domain to a full address (17.0+), or `mail.default.from` (16.0): every outgoing email
  is sent as that address.
- **Failed mail: fix the cause, then retry.** The queue is Settings ‣ Technical ‣
  Email ‣ Emails. `mail.mail.state`: `outgoing`, `sent`, `received`, `exception`,
  `cancel`; the scheduled action `mail.ir_cron_mail_scheduler_action` sends `outgoing`
  ones.

  ```python
  failed = env['mail.mail'].search([('state', '=', 'exception')], order='id desc', limit=20)
  print(failed.mapped(lambda m: (m.id, m.email_to, m.failure_type, m.failure_reason)))
  failed.action_retry()
  env.cr.commit()
  ```

  Fix the cause first (`failure_reason`): authentication, from not allowed, recipient
  invalid. `action_retry()` only puts `exception` mails back to `outgoing`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Settings section | Discuss | Discuss | Emails | Emails | Emails |
| Outgoing servers menu (developer mode) | Settings ‣ Technical ‣ Email ‣ Outgoing Mail Servers | same | same | same | same |
| Incoming servers menu (developer mode) | Settings ‣ Technical ‣ Email ‣ Incoming Mail Servers | same | same | same | same |
| Alias domain | `alias_domain` setting + system parameters | `mail.alias.domain`, Technical ‣ Email ‣ Alias Domains | same | same | same |
| `smtp_encryption` | `none`, `starttls`, `ssl` | same | same | adds `starttls_strict`, `ssl_strict` | as 19.0 |
| `smtp_authentication` `cli` | - | yes | yes | yes | yes |
| `from_filter` | one value | comma-separated list | same | same | same |
| `database.is_neutralized` read with | `get_param` | `get_param` | `get_param` | `get_param` | `get_bool` |
| Neutralization clears archived servers' user and password | - | - | - | - | yes |

## Verify

```python
server = env['ir.mail_server'].search([('name', '=', 'Company SMTP')])
print(server.read(['smtp_host', 'smtp_port', 'smtp_encryption', 'from_filter', 'active']))
print(env.company.alias_domain_id.read(['name', 'catchall_alias', 'bounce_alias', 'default_from']) if 'alias_domain_id' in env.company else env['ir.config_parameter'].get_param('mail.catchall.domain'))   # 17.0+ / 16.0
print(env.ref('mail.ir_cron_mail_scheduler_action').read(['active', 'nextcall']))
print({state: env['mail.mail'].search_count([('state', '=', state)]) for state in ('outgoing', 'exception')})
```

Then send a test document to the user's own address and watch it leave the queue.

## Pitfalls

- **Neutralized copies send nothing.** A neutralized database (a test or staging copy)
  has all mail servers archived, a dummy active server "neutralization - disable emails"
  on host `invalid`, incoming servers archived and scheduled actions off. From 20.0 the
  archived servers also lose their user and password. Mails queue up and fail. Check
  `database.is_neutralized` before diagnosing "emails do not leave", and do not
  re-activate real servers in a copy without the user's explicit yes: customers would
  receive test mail.
- **Sender rewritten to notifications@.** No server's `from_filter` matches the user's
  address. Add the domain to the filter only if the provider really allows it.
- **SPF, DKIM, DMARC missing**: mail leaves Odoo and lands in spam or bounces. Fix the
  DNS, not Odoo.
- **Retrying a long failed queue** sends old emails to customers. Ask first.
- **Changing catchall or bounce** without keeping the old mailboxes loses replies.
