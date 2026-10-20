# Diagnosis: why does Odoo do X

Most "Odoo is wrong" reports are configuration doing exactly what it says. Reproduce
the case, read the records that decide it, find the one value that explains it, and only
then propose a change. Each section below is: symptom, what to read, usual causes, fix.

Read first, always: the exact document, the user, and the company.

```python
user = env['res.users'].search([('login', '=', 'maria@example.com')])
doc = env['account.move'].search([('name', '=', 'INV/2026/00042')])
print(user.company_id.name, user.company_ids.mapped('name'), doc.company_id.name)
```

Everything here reads. Changes go through the matching recipe, with the user's yes.

## Access error

Symptom: "You are not allowed to access/modify ... (model)" or "Due to security
restrictions...". The message names the model and the operation; in debug mode it also
lists the groups that would allow it and the rules that failed.

What to read: the user's groups, then the access rights and rules on that model.

```python
groups = user.all_group_ids if 'all_group_ids' in user else user.groups_id   # 19.0+ / up to 18.0
print(sorted(groups.mapped('full_name')))
Order = env['sale.order'].with_user(user)
order = env['sale.order'].browse(42)
```

Up to 19.0, model access is `ir.model.access` and row filters are `ir.rule`:

```python
print(Order.check_access_rights('write', raise_exception=False))            # 16.0, 17.0
print(order.with_user(user).has_access('write'))                            # 18.0+
for acl in env['ir.model.access'].search([('model_id.model', '=', 'sale.order')]):
    print(acl.group_id.full_name, acl.perm_read, acl.perm_write, acl.perm_create, acl.perm_unlink)
failing = env['ir.rule'].with_user(user)._get_failing(order.with_user(user), 'write')
print(failing.mapped(lambda r: (r.name, r.domain_force, r.groups.mapped('full_name'))))
```

In 20.0 both are one model, `ir.access` (group set: a permission; no group: a
restriction that applies to everyone):

```python
print(order.with_user(user).has_access('write'))
for access in env['ir.access'].search([('model_id.model', '=', 'sale.order')]):
    print(access.name, access.group_id.full_name, access.operation, access.domain)
print(env['ir.access'].with_user(user)._get_failed_accesses(order.with_user(user), 'write').mapped('name'))
```

Usual causes: the user lacks the application group (for example only
`sales_team.group_sale_salesman`, which sees its own orders, instead of
`sales_team.group_sale_salesman_all_leads`); the record belongs to a company the user
does not have; a custom rule or access added later.

Fix: give the right group (`users-and-access.md`). Change a rule only when the rule
itself is wrong, and say who else it affects.

## Record not visible

Symptom: "the invoice disappeared", "I cannot find the customer".

```python
rec = env['res.partner'].with_context(active_test=False).search([('name', 'ilike', 'Dupont')])
print(rec.read(['active', 'company_id']))
print(rec.with_user(user).with_context(active_test=False).search_count([('id', 'in', rec.ids)]))
action = env.ref('sale.action_quotations_with_onboarding')
print(action.domain, action.context)
```

Usual causes, in order:

- Archived: `active` is False. The default search hides archived records.
- Another company: `company_id` is a company the user does not have, or not ticked in
  the company switcher.
- A record rule (see Access error); `with_user(user)` returns fewer records than sudo.
- The menu's default filter: the action's `context` has `search_default_...`, such as
  "My Quotations" (`search_default_my_quotation`). The user removes the filter; nothing
  is wrong.

Fix: unarchive, add the company to the user, or explain the filter.

## Tax missing or wrong on an invoice line

```python
line = doc.invoice_line_ids.filtered(lambda l: l.product_id)[:1]
product = line.product_id
print(product.taxes_id.mapped(lambda t: (t.name, t.company_id.name)))      # sale taxes
print(product.supplier_taxes_id.mapped(lambda t: (t.name, t.company_id.name)))
fpos = doc.fiscal_position_id
print(fpos.name, fpos.auto_apply, fpos.country_id.code, fpos.vat_required)
print(line.tax_ids.mapped('name'), line._get_computed_taxes().mapped('name'))   # on the line / what Odoo would put now
print(doc.partner_id.with_company(doc.company_id).property_account_position_id.name)
```

The line takes the product's taxes of the invoice's company; with none, the default
taxes of the line's income or expense account (and in 16.0, failing that, the company's
default sale or purchase tax). The fiscal position then maps them.

Usual causes:

- The product has taxes only for another company (each company has its own taxes; from
  17.0 a branch also uses its parent company's taxes).
- A fiscal position replaced or removed it. Up to 18.0 the mapping is
  `fpos.tax_ids` (`account.fiscal.position.tax`: `tax_src_id` → `tax_dest_id`; an empty
  destination removes the tax). From 19.0 the fiscal position lists its taxes in
  `tax_ids`, and each foreign tax names the domestic ones it replaces in
  `original_tax_ids`.
- The fiscal position came from the partner (`property_account_position_id`, set by
  company) or was detected automatically (`auto_apply`, by country, country group, and
  `vat_required`). A partner without a VAT number or country misses the automatic one.
- The invoice came from a sales order: the line keeps the order line's taxes
  (`tax_id` up to 18.0, `tax_ids` from 19.0). Check the order.

Fix: correct the product, the mapping or the partner (`taxes-and-journals.md`,
`payment-terms-and-fiscal-positions.md`). Existing draft lines do not recompute by
themselves; posted invoices are not changed.

## Wrong price

```python
order = env['sale.order'].browse(42)
for line in order.order_line:
    print(line.product_id.display_name, line.product_uom_qty, line.price_unit,
          line.pricelist_item_id.display_name)
pricelist = order.pricelist_id
print(pricelist.name, pricelist.currency_id.name, order.partner_id.property_product_pricelist.name)
price, rule_id = pricelist._get_product_price_rule(line.product_id, line.product_uom_qty)
print(price, env['product.pricelist.item'].browse(rule_id).read(
    ['applied_on', 'min_quantity', 'date_start', 'date_end', 'compute_price']))
```

`pricelist_item_id` on the line is the rule that priced it. Rules are tried in the
model's order: the most specific `applied_on` first (`0_product_variant`, `1_product`,
`2_product_category`, `3_global`), then the highest `min_quantity`. The first rule that
matches wins.

Usual causes: a rule with dates that ended or not started (`date_start`, `date_end`);
a `min_quantity` above the quantity ordered; a more specific rule shadowing the one the
user edited; the order's pricelist is not the one the user thinks (the pricelist is set
when the order is created and does not follow later changes on the customer); another
currency; the quantity is in a different unit of measure (`product_uom` up to 18.0,
`product_uom_id` from 19.0).

Fix: correct the rule (`pricelists.md`). Existing order lines keep their price until the
user updates prices on the order.

## Automation or scheduled action not running

```python
rule = env['base.automation'].search([('name', 'ilike', 'confirmation')])
print(rule.read(['active', 'trigger', 'filter_pre_domain', 'filter_domain', 'last_run']))
print(rule.trigger_field_ids.mapped('name'))
cron = env['ir.cron'].with_context(active_test=False).search([('cron_name', 'ilike', 'reminder')])
print(cron.read(['active', 'nextcall', 'lastcall', 'interval_number', 'interval_type', 'user_id']))
print(env['ir.config_parameter'].sudo().get_param('database.is_neutralized'))
```

Usual causes:

- Inactive. A neutralized copy turns off every scheduled action except the autovacuum.
- `filter_pre_domain` (the record before the change) or `filter_domain` (after) does
  not match the record.
- `trigger_field_ids` is set and none of those fields changed.
- Timed rules (`on_time` and, from 17.0, `on_time_created`, `on_time_updated`) run from
  the scheduled action `base_automation.ir_cron_data_base_automation_check`, which must
  be active.
- Scheduled action: `nextcall` in the future (it is UTC); up to 17.0 `numbercall` reached
  0 (it is 1 by default; -1 means forever); from 18.0 it was turned off after failing at
  least 5 times over 7 days (`failure_count`, `first_failure_date`).
- The server runs with `max_cron_threads = 0`, or the job failed: the error is in the
  server log.

Fix: reactivate or correct the domain. Run a scheduled action once to see its error:
`cron.method_direct_trigger()` (it runs as the cron's user and commits).

## Email not sent

```python
mails = env['mail.mail'].search([('subject', 'ilike', 'INV/2026/00042')])
print(mails.read(['state', 'failure_reason', 'email_to', 'mail_server_id', 'scheduled_date']))
print(env['ir.mail_server'].with_context(active_test=False).search_read([], ['name', 'smtp_host', 'active', 'from_filter']))
print(env.ref('mail.ir_cron_mail_scheduler_action').read(['active', 'nextcall']))
```

`state`: `outgoing` (waiting in the queue), `sent`, `exception` (failed: read
`failure_reason`), `cancel`. Sent mails are usually deleted (`auto_delete`), so no row
can mean "sent".

Usual causes: the queue's scheduled action is off (neutralized copy); no active outgoing
server, or the neutralization one (`smtp_host` "invalid"); the server refuses the sender
address (`from_filter`); the recipient has no email.

Fix: `mail-servers.md`. Retry failed mails with `mails.action_retry()` once the cause is
fixed. Never reactivate servers in a copy of production.

## Field not shown

```python
Model = env['res.partner']
print(Model._fields['vat'].groups)                     # groups set on the field in Python
views = env['ir.ui.view'].search([('model', '=', 'res.partner'), ('arch_db', 'ilike', 'name="vat"')])
print([(v.id, v.name, v.inherit_id.name, v.get_external_id()[v.id]) for v in views])
arch = Model.with_user(user).get_views([(False, 'form')])['views']['form']['arch']
print('name="vat"' in arch)
```

Usual causes: `groups="..."` on the field in the view or in Python (the user lacks the
group); `invisible` on a condition (16.0 writes it in `attrs`, 17.0 and later directly);
an inherited view, often one without an XML id (made in the interface), that hides or
replaces it; the module that adds the field is not installed. Find standard views and
their groups in `odoo-reference/xmlids/<addon>.md`.

Fix: give the group, or archive the custom view that hides the field. Do not edit
standard views; an update restores them.

## Numbering skipped or out of order

```python
seq = env['ir.sequence'].search([('code', '=', 'sale.order')])
print(seq.read(['implementation', 'number_next_actual', 'prefix', 'use_date_range', 'company_id']))
```

Usual causes: `standard` sequences take numbers from PostgreSQL and lose one whenever a
transaction rolls back (an error on save, a cancelled wizard); `no_gap` avoids that at
the cost of locking. Documents deleted after numbering. One sequence per company.
Invoices and journal entries are numbered from their journal, not from `ir.sequence`:
see `taxes-and-journals.md`.

Fix: explain the gap; switch to `no_gap` only where the law or the user requires it.
Never lower `number_next_actual` without the user saying so.
