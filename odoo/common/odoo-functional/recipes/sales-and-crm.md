# Sales and CRM

Sales teams (`crm.team`, from `sales_team`) group salespeople; CRM pipelines
(`crm.lead`) move through stages (`crm.stage`); quotations (`sale.order`) follow the
company's quotation settings; invoicing follows each product's invoicing policy. Most of
it is per company.

```python
print(env['crm.team'].search_read([], ['name', 'user_id', 'member_ids', 'company_id']))
print(env['crm.stage'].search_read([], ['name', 'sequence', 'is_won', 'fold']))
s = env['res.config.settings'].create({})
print(s.portal_confirmation_sign, s.portal_confirmation_pay, s.quotation_validity_days, s.group_discount_per_so_line)
```

## Teams and members

```python
team = env['crm.team'].create({'name': 'Key accounts', 'user_id': leader.id, 'company_id': company.id})
env['crm.team.member'].create([{'crm_team_id': team.id, 'user_id': u.id} for u in sellers])
env.cr.commit()
```

- A user is in one team only, unless the setting `is_membership_multi` (Multi Teams) is
  on: adding them to a new team archives their other membership. Say so before moving
  people.
- With `crm`, a team has `use_leads`, `use_opportunities` and an email alias
  (`alias_name`): mail to it creates leads for the team. See `mail-servers.md`.
- The default team is `sales_team.team_sales_department`.

## CRM stages

- 16.0 to 18.0: a stage has `team_id`; empty means shared by all teams.
- 19.0+: `team_ids` (Many2many); empty means shared. 19.0 adds `rotting_threshold_days`.
- `is_won` marks the won stage; `fold` folds it in the kanban.

```python
# 16.0-18.0: 'team_id': team.id    19.0+: 'team_ids': [(6, 0, [team.id])]
env['crm.stage'].create({'name': 'Demo done', 'sequence': 3, 'team_ids': [(6, 0, [team.id])]})
env.cr.commit()
```

- Standard stages: `crm.stage_lead1` to `crm.stage_lead4` (New, Qualified, Proposition,
  Won). A stage that still has leads cannot be deleted (`stage_id` is `ondelete='restrict'`):
  move the leads first, or rename the stage.
- Leads mode (qualify before the pipeline): setting `group_use_lead`.

## Lost reasons

`crm.lost.reason` (`name`, `active`). Mark a lead lost with
`lead.action_set_lost(lost_reason_id=reason.id)` or the wizard `crm.lead.lost`.

## Quotation settings

Write them through settings, per company (`with_company`). Names from
`odoo-reference/settings.md`:

| Setting | Field | Versions |
|---|---|---|
| Online signature / payment | `portal_confirmation_sign`, `portal_confirmation_pay` | all; 17.0+ adds `prepayment_percent` |
| Quotation validity | `quotation_validity_days` (0 = no expiry from 17.0) | 16.0 also needs `use_quotation_validity_days` |
| Discounts on lines | `group_discount_per_so_line` | group in `product` 16.0–17.0, in `sale` 18.0+ |
| Default terms | `use_invoice_terms`, `invoice_terms`, `terms_type` (`plain`, `html`) | all |
| Lock confirmed orders | `group_auto_done_setting` | all |
| Pro-forma invoice | `group_proforma_sales` | all |
| Quotation templates | `group_sale_order_template` (`sale_management`) | 16.0–19.0 |
| Automatic invoice after online payment | `automatic_invoice` (16.0–19.0), `sale_automatic_invoice` (20.0) | |

```python
env['res.config.settings'].create({
    'portal_confirmation_sign': True,
    'quotation_validity_days': 30,  # 16.0: also 'use_quotation_validity_days': True
    'group_discount_per_so_line': True,
}).execute()
env.cr.commit()
```

- With `use_invoice_terms`, new quotations take `invoice_terms` (or the web page when
  `terms_type` is `html`) as their note, as invoices do.

## Invoicing policy

`invoice_policy` on the product: `order` (ordered quantities) or `delivery` (delivered
quantities). For services, `sale_timesheet` and `sale_project` add `service_type` and
`service_policy` (timesheets, milestones); read the selection in the version.

- Default for new products: setting `default_invoice_policy` (16.0 to 19.0, values
  `order`, `delivery`); in 20.0 `sale_invoice_policy` on the company.
- Changing the policy on products already on confirmed orders changes what can be
  invoiced on those orders: list them first.

## Down payments

The wizard `sale.advance.payment.inv` with `advance_payment_method` `delivered`
(regular invoice), `percentage` (`amount`) or `fixed` (`fixed_amount`).

```python
wizard = env['sale.advance.payment.inv'].with_context(active_model='sale.order', active_ids=order.ids).create({
    'advance_payment_method': 'percentage', 'amount': 30,
})
wizard.create_invoices()
env.cr.commit()
```

- 16.0: uses a down payment service product (parameter `sale.default_deposit_product_id`).
  When that product has no taxes (the one Odoo creates has none), `percentage` is taken
  from the total with taxes, not the untaxed amount: check the amount before posting.
- 17.0: the product is on the company, `sale_down_payment_product_id`.
- 18.0: no product.
- 19.0+: the account can be set on the company, `downpayment_account_id`.
- The final invoice deducts the down payments when `deduct_down_payments` is on (default).
