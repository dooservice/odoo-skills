# Sales and CRM

Sales teams (`crm.team`, from `sales_team`) group salespeople; CRM opportunities
(`crm.lead`) move through stages (`crm.stage`); quotations (`sale.order`) follow the
company's quotation settings, become sales orders when confirmed, and are delivered and
invoiced according to each product's invoicing policy. Most of it is per company. This
recipe covers `crm`, `sale`, `sale_management`, `sale_crm` and `sale_stock`, all in
Community; online payment providers and subscriptions are left out.

## Before you start

- Apps: `crm` and `sale` (`sale_crm` links them, installed with both); `sale_management`
  for quotation templates; `sale_stock` for deliveries; `account` for invoices.
- Settings: quotation settings, per company (`with_company`), names from
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
| Default invoicing policy | `default_invoice_policy` (`order`, `delivery`) | 16.0–19.0; 20.0: `sale_invoice_policy` on the company |
| Multi Teams | `is_membership_multi` | all |
| Leads | `group_use_lead` | all |

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
- Invoicing policy: `invoice_policy` on the product, `order` (ordered quantities) or
  `delivery` (delivered quantities). Changing it on products already on confirmed orders
  changes what can be invoiced on those orders: list them first. For services,
  `sale_timesheet` and `sale_project` add `service_type` and `service_policy`
  (timesheets, milestones); read the selection in the version.
- Read first:

```python
print(env['crm.team'].search_read([], ['name', 'user_id', 'member_ids', 'company_id']))
print(env['crm.stage'].search_read([], ['name', 'sequence', 'is_won', 'fold']))
s = env['res.config.settings'].create({})
print(s.portal_confirmation_sign, s.portal_confirmation_pay, s.quotation_validity_days, s.group_discount_per_so_line)
```

## The standard flow

Odoo's documentation sets up the team and the pipeline, then follows one deal:
opportunity, quotation from the opportunity, send, confirm, mark won, deliver, invoice.

1. **Create the sales team and add its members.** CRM ‣ Configuration ‣ Sales Teams
   (also Sales ‣ Configuration ‣ Sales Teams; Teams in 20.0) ‣ New.

   ```python
   team = env['crm.team'].create({'name': 'Key accounts', 'user_id': leader.id, 'company_id': company.id})
   env['crm.team.member'].create([{'crm_team_id': team.id, 'user_id': u.id} for u in sellers])
   env.cr.commit()
   ```

   Leaves a team that its members' new opportunities and quotations take.

   - A user is in one team only, unless the setting `is_membership_multi` (Multi Teams)
     is on: adding them to a new team archives their other membership. Say so before
     moving people.
   - With `crm`, a team has `use_leads`, `use_opportunities` and an email alias
     (`alias_name`): mail to it creates leads for the team. See `mail-servers.md`.
   - The default team is `sales_team.team_sales_department`.

2. **Adapt the pipeline stages.** CRM ‣ Configuration ‣ Pipeline ‣ Stages.

   ```python
   # 16.0-18.0: 'team_id': team.id    19.0+: 'team_ids': [(6, 0, [team.id])]
   env['crm.stage'].create({'name': 'Demo done', 'sequence': 3, 'team_ids': [(6, 0, [team.id])]})
   env.cr.commit()
   ```

   Leaves a stage shown in that team's pipeline.

   - 16.0 to 18.0: a stage has `team_id`; empty means shared by all teams. 19.0+:
     `team_ids` (Many2many); empty means shared. 19.0 adds `rotting_threshold_days`.
   - `is_won` marks the won stage; `fold` folds it in the kanban.
   - Standard stages: `crm.stage_lead1` to `crm.stage_lead4` (New, Qualified,
     Proposition, Won). A stage that still has leads cannot be deleted (`stage_id` is
     `ondelete='restrict'`): move the leads first, or rename the stage.

3. **Create the opportunity.** CRM ‣ Sales ‣ My Pipeline ‣ New.

   ```python
   lead = env['crm.lead'].create({'name': 'Desks for Acme', 'type': 'opportunity', 'partner_id': customer.id,
       'team_id': team.id, 'user_id': seller.id, 'expected_revenue': 5000})
   env.cr.commit()
   ```

   Leaves an opportunity in the team's first stage.

4. **Create the quotation from the opportunity.** The opportunity's New Quotation button
   (from `sale_crm`). It opens a quotation with the opportunity's customer, team and
   origin, the same as Sales ‣ Orders ‣ Quotations ‣ New with those fields filled.

   ```python
   action = lead.action_sale_quotations_new()
   order = env['sale.order'].with_context(action['context']).create({
       'order_line': [(0, 0, {'product_id': product.id, 'product_uom_qty': 5})],
   })
   env.cr.commit()
   ```

   Leaves a quotation in `draft`, linked by `opportunity_id`; prices come from the
   customer's pricelist (`pricelists.md`), validity from `quotation_validity_days`.

5. **Send it.** The quotation's Send by Email button, which opens the composer with the
   quotation's email template.

   ```python
   action = order.action_quotation_send()
   env['mail.compose.message'].with_context(action['context']).create({}).action_send_mail()
   env.cr.commit()
   ```

   Leaves the quotation in `sent`, the message in its chatter and the email in the mail
   queue. On a copy of production outgoing mail is usually off: say so.

6. **Confirm it.** The Confirm button (or the customer signs or pays online, with
   `portal_confirmation_sign` / `portal_confirmation_pay`).

   ```python
   order.action_confirm()
   env.cr.commit()
   ```

   Leaves a sales order in `sale` and, with `sale_stock` and storable products, a
   delivery ready to process. With `group_auto_done_setting` it is also locked (state
   `done` in 16.0, boolean `locked` from 17.0).

7. **Mark the opportunity won.** The opportunity's Won button.

   ```python
   lead.action_set_won_rainbowman()
   env.cr.commit()
   ```

   Leaves the opportunity in the won stage with probability 100. Confirming the order
   does not do it.

8. **Deliver.** The order's Delivery smart button (or Inventory ‣ Operations ‣ Transfers
   ‣ Deliveries from 17.0), Validate.

   ```python
   picking = order.picking_ids.filtered(lambda p: p.state not in ('done', 'cancel'))
   for move in picking.move_ids:
       move.quantity = move.product_uom_qty   # 16.0: quantity_done
   res = picking.button_validate()
   env.cr.commit()
   ```

   Leaves the delivery `done` and `qty_delivered` on the order lines. `button_validate`
   may return a wizard (backorder, immediate transfer in 16.0) instead of finishing:
   read `res`. Validating stock is real inventory: only with the user's yes, and
   normally done by the warehouse (`inventory.md`).

9. **Invoice.** The order's Create Invoice button, Regular invoice.

   ```python
   wizard = env['sale.advance.payment.inv'].with_context(active_model='sale.order', active_ids=order.ids).create({
       'advance_payment_method': 'delivered',
   })
   wizard.create_invoices()
   env.cr.commit()
   ```

   Leaves a draft customer invoice for what the policy allows (ordered or delivered
   quantities) and `invoice_status` `invoiced` on the order. Posting it is accounting:
   the user posts or confirms.

## Variations

- **Leads first.** With `group_use_lead`, mail and web forms create leads (CRM ‣ Leads)
  that are qualified and converted into opportunities before step 3.
- **A quotation without CRM.** Sales ‣ Orders ‣ Quotations ‣ New, then steps 5, 6, 8
  and 9.
- **Lost.** `crm.lost.reason` (`name`, `active`), in CRM ‣ Configuration ‣ Pipeline ‣
  Lost Reasons. Mark a lead lost with `lead.action_set_lost(lost_reason_id=reason.id)`
  or the wizard `crm.lead.lost` (the Lost button).
- **Down payments.** At step 9, the wizard `sale.advance.payment.inv` with
  `advance_payment_method` `delivered` (regular invoice), `percentage` (`amount`) or
  `fixed` (`fixed_amount`).

  ```python
  wizard = env['sale.advance.payment.inv'].with_context(active_model='sale.order', active_ids=order.ids).create({
      'advance_payment_method': 'percentage', 'amount': 30,
  })
  wizard.create_invoices()
  env.cr.commit()
  ```

  - 16.0: uses a down payment service product (parameter
    `sale.default_deposit_product_id`). When that product has no taxes (the one Odoo
    creates has none), `percentage` is taken from the total with taxes, not the untaxed
    amount: check the amount before posting.
  - 17.0: the product is on the company, `sale_down_payment_product_id`.
  - 18.0: no product.
  - 19.0+: the account can be set on the company, `downpayment_account_id`.
  - The final invoice deducts the down payments when `deduct_down_payments` is on
    (default).
- **Invoice before delivering.** Products with `invoice_policy='order'` can be invoiced
  right after step 6.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Stage team | `team_id` | `team_id` | `team_id` | `team_ids`, `rotting_threshold_days` | `team_ids` |
| Quotation validity | needs `use_quotation_validity_days` | 0 = no expiry | same | same | same |
| `group_discount_per_so_line` in | `product` | `product` | `sale` | `sale` | `sale` |
| Default invoicing policy | setting `default_invoice_policy` | same | same | same | company `sale_invoice_policy` |
| Automatic invoice | `automatic_invoice` | same | same | same | `sale_automatic_invoice` |
| Locked order | state `done` | `locked` boolean | same | same | same |
| Validating a delivery | `quantity_done`; immediate transfer wizard | `quantity` | same | same | same |
| Down payment product | parameter `sale.default_deposit_product_id` | company `sale_down_payment_product_id` | none | none; company `downpayment_account_id` | same as 19.0 |
| Menu: sales teams (Sales) | Sales ‣ Configuration ‣ Sales Teams | same | same | same | Sales ‣ Configuration ‣ Teams |
| Menu: quotation templates | Sales ‣ Configuration ‣ Sales Orders ‣ Quotation Templates | same | same | same | Sales ‣ Configuration ‣ Sales Orders ‣ Templates |
| Menu: orders to invoice | Sales ‣ To Invoice ‣ Orders to Invoice | same | same | same | none (filter Sales ‣ Orders ‣ Orders) |
| Menu: deliveries | Inventory ‣ Operations ‣ Transfers | Inventory ‣ Operations ‣ Transfers ‣ Deliveries | same | same | same |
| Menu: activity types (CRM) | CRM ‣ Configuration ‣ Activity Types | same | CRM ‣ Configuration ‣ Activities ‣ Activity Types | same | same |

The same in every version: CRM ‣ Configuration ‣ Sales Teams, CRM ‣ Configuration ‣
Teams Members, CRM ‣ Configuration ‣ Pipeline ‣ Stages, CRM ‣ Configuration ‣ Pipeline ‣
Lost Reasons, CRM ‣ Sales ‣ My Pipeline, CRM ‣ Leads, CRM ‣ Configuration ‣ Settings,
Sales ‣ Orders ‣ Quotations, Sales ‣ Orders ‣ Orders, Sales ‣ Configuration ‣ Settings,
Invoicing ‣ Customers ‣ Invoices.

## Verify

```python
print(lead.stage_id.name, lead.probability, order.opportunity_id.name)
print(order.state, order.invoice_status, [(l.product_id.display_name, l.product_uom_qty, l.qty_delivered, l.qty_invoiced) for l in order.order_line])
print(order.picking_ids.mapped(lambda p: (p.name, p.state)), order.invoice_ids.mapped(lambda m: (m.name, m.state, m.amount_untaxed)))
```

The opportunity is won; the order is `sale` with delivered and invoiced quantities equal
to the ordered ones; the delivery is `done` and the invoice a draft for the user to post.

## Pitfalls

- Moving a user to a team without Multi Teams archives their other membership.
- A stage written with `team_id` in 19.0+ (or `team_ids` before) fails.
- With `invoice_policy='delivery'`, Create Invoice before the delivery is validated
  raises an error: validate the delivery, or change the policy with the user's yes.
- A down payment percentage in 16.0 with an untaxed deposit product is computed on the
  total with taxes.
- Quotations sent from a copy of production stay in the mail queue.
- Confirming the order does not mark the opportunity won, and winning the opportunity
  does not confirm the order: do both.
