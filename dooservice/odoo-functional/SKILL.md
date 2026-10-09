---
name: odoo-functional
description: >-
  Configuring Odoo without code in a dooservice functional session: changing
  settings, companies, users, access groups, standard modules, sequences,
  taxes, email templates, automations and data through the ORM in dooservice
  shell, with read-only psql for diagnosis. Use for any configuration,
  data-fix or "why does Odoo do X" request in this session.
---

# Configuring Odoo without code

Everything here is data in this environment's database, changed through the ORM so
Odoo's own checks, computes and access rules run. No module is written or modified.

## Find before changing

- Read the current state first: the record, its fields, who uses it.
  `dooservice shell` then `env['res.company'].search_read([], ['name', 'currency_id'])`.
- `psql` is **read-only** here: use it to look, never to change.
- A setting in Settings is usually a `res.config.settings` field backed by an
  `ir.config_parameter`, a company field, or a group (`group_*` fields imply a group on
  `base.group_user`). Find which with
  `env['res.config.settings']._fields['<field>']` (look at `config_parameter`,
  `related`, `implied_group`).
- Standard module sources are in `/usr/lib/python3/dist-packages/odoo/addons` for
  reference: views tell you field names, data files tell you XML ids.

## Change through the ORM

```bash
dooservice shell <<'PY'
company = env.ref('base.main_company')
company.write({'phone': '+1 555 0100'})
env.cr.commit()
PY
```

- End every script that changes data with `env.cr.commit()`, or nothing is saved.
- Settings: create and execute a `res.config.settings` so its side effects run:
  `env['res.config.settings'].create({'<field>': True}).execute()`.
- Prefer `env.ref('<module>.<xml_id>')` to searching by name.
- Records are shared: a tax, a journal or a pricelist changed here changes it for every
  document that uses it. Say so before changing one in use.

## Confirm before

Before anything that touches many records (mass updates, deletions, archiving, access
rights, record rules, accounting configuration with posted entries), tell the user:
what will change, on which records, how many, and how to undo it. Wait for a yes.
Prefer archiving (`active=False`) to deleting.

## What configuration can do

- Users, groups and access: `res.users`, `res.groups`, record rules (`ir.rule`).
- Companies, currencies, fiscal positions, taxes, journals, payment terms.
- Sequences (`ir.sequence`), email templates (`mail.template`), reports' paper formats.
- Automations: server actions (`ir.actions.server`), automated actions
  (`base.automation`, when installed), scheduled actions (`ir.cron`; disabled in a
  neutralized clone).
- Standard modules: `dooservice install <module>` then `dooservice restart`.
- System parameters: `env['ir.config_parameter'].sudo().set_param(key, value)`.

## What needs code

A new model, a new stored field in a module, a report layout, an override of
behaviour, an integration: say plainly that it needs development, in a code session
with the project's repository. Offer the closest configuration instead when there is
one (a server action, an automated action, a custom filter, a mail template).

## After a change

- Installing or updating a module: `dooservice restart`, then `dooservice logs -n 200`.
- Ask the user to check it in the browser (`echo $DOOSERVICE_BUILD_URL`).
- Summarize what was changed, with the records and values, so it can be repeated in
  production by the user: configuration does not travel there on its own.
