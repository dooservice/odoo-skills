# Memberships and partner levels

How a company sells memberships and keeps track of who is a member. Up to 18.0 the
Members app (`membership`) sells membership products with fixed start and end dates; the
invoice of that product creates a membership line (`membership.membership_line`) on the
contact, and its payment turns the contact into a paid member until the end date. In
19.0 `membership` is gone: `partnership` gives contacts a level (`res.partner.grade`)
with an optional pricelist, assigned by hand or by confirming a sale of a product that
carries the level; levels have no dates. Publishing members on the website is
`website_membership` (16.0 to 18.0) or `website_partnership` (20.0). Recurring
subscriptions are Enterprise and left out.

## Before you start

- Apps:
  - 16.0 to 18.0: `membership` (Members app, needs `account`); `website_membership` for
    the public directory (needs `website_sale`; in 16.0 also `association`, which adds
    Events).
  - 19.0 and 20.0: `partnership` (needs `crm` and `sale`), installed from CRM ‣
    Configuration ‣ Settings, Membership / Partnership (`module_partnership`); 20.0:
    `website_partnership`, Partners Website Page (`module_website_partnership`). In 19.0
    the public partner page belongs to `website_crm_partner_assign`
    (`lead-generation.md`).
- Settings: 19.0+: the name the company gives its affiliates, `partnership_label` on
  `res.company` (default `Members`); it also renames the menu CRM ‣ Configuration ‣
  <label>. 16.0 to 18.0: none.
- Users: the Members app menu needs `account.group_account_invoice` from 17.0 (no group
  in 16.0); its Reporting menu needs `base.group_partner_manager`.
- Read first:

19.0 and 20.0:

```python
print(env.company.partnership_label)
print(env['res.partner.grade'].search_read([], ['name', 'sequence', 'default_pricelist_id', 'partners_count']))
print(env['product.template'].search_read([('service_tracking', '=', 'partnership')], ['name', 'grade_id', 'list_price']))
```

16.0 to 18.0:

```python
print(env['product.template'].search_read([('membership', '=', True)],
      ['name', 'list_price', 'membership_date_from', 'membership_date_to', 'type']))
print(env['res.partner'].search_read([('membership_state', '!=', 'none')],
      ['name', 'membership_state', 'membership_start', 'membership_stop', 'free_member', 'associate_member']))
```

## The standard flow

From 19.0 Odoo's documentation follows one level: level, product that assigns it, sale.
Up to 18.0 it follows one membership: product, member, invoice, payment.

### 19.0 and 20.0: levels with `partnership`

1. **Create the levels.** CRM ‣ Configuration ‣ <label> ‣ Levels ‣ New: name, sequence
   and, optionally, the pricelist members of that level get (`pricelists.md`).

   ```python
   gold = env['res.partner.grade'].create({'name': 'Gold', 'sequence': 1, 'default_pricelist_id': member_pricelist.id})
   env.cr.commit()
   ```

   Leaves a level; Gold, Silver and Bronze exist after installing the module.

2. **Create the product that assigns the level.** Sales ‣ Products ‣ Products ‣ New: a
   service, Create on Order `Membership / Partnership`, Assigned Level.

   ```python
   tmpl = env['product.template'].create({
       'name': 'Gold membership', 'type': 'service', 'sale_ok': True,
       'service_tracking': 'partnership', 'grade_id': gold.id, 'list_price': 500,
   })
   env.cr.commit()
   ```

   Leaves a product whose sale assigns the level. `service_tracking` falls back to
   `no` when the product is not a service or not `sale_ok`.

3. **Sell it.** Sales ‣ Orders ‣ Quotations ‣ New with that product, then Confirm (the
   rest of the sale is `sales-and-crm.md`).

   ```python
   member = env['res.partner'].create({'name': 'Example Shop', 'is_company': True, 'email': 'shop@example.com'})
   order = env['sale.order'].create({
       'partner_id': member.id,
       'order_line': [(0, 0, {'product_id': tmpl.product_variant_id.id})],
   })
   order.action_confirm()
   env.cr.commit()
   ```

   Leaves the order in `sale` and the level on the customer's company
   (`commercial_partner_id.grade_id`); with a `default_pricelist_id`, its pricelist
   becomes the customer's pricelist. Lines that assign two different levels block the
   order.

4. **Follow the members.** CRM ‣ Configuration ‣ <label> ‣ Levels: each level's count
   opens its contacts; on a pricelist, the stat button lists the contacts that use it.
   Contacts can be grouped by Level.

   Leaves nothing changed. A level stays until someone changes it: there is no end
   date or renewal.

### 16.0 to 18.0: Members app

1. **Create the membership product.** Members ‣ Configuration ‣ Membership Products ‣
   New: name, Membership Duration (from and to, both required in the form) and
   Membership Fee.

   ```python
   tmpl = env['product.template'].create({
       'name': 'Annual membership', 'membership': True, 'type': 'service',
       'membership_date_from': '2026-01-01', 'membership_date_to': '2026-12-31',
       'list_price': 120, 'taxes_id': [(6, 0, sale_taxes.ids)],
   })
   membership = tmpl.product_variant_id
   env.cr.commit()
   ```

   This is 18.0; in 16.0 and 17.0 write `'detailed_type': 'service'` instead of
   `'type': 'service'`.

   Leaves a service product with `membership` on; the menu only lists products with
   `membership` and `type='service'`. The dates are calendar dates, not a duration: next
   year needs a new product (or new dates on this one).

2. **Create the member.** Members ‣ Members ‣ New (a contact form with a Membership
   tab).

   ```python
   member = env['res.partner'].create({'name': 'Example Shop', 'is_company': True, 'email': 'shop@example.com'})
   env.cr.commit()
   ```

   Leaves a contact with `membership_state` `none`. Contacts created from this menu
   have Free Member ticked by default (the action's `default_free_member`): untick it
   for a paying member, or step 3 refuses to invoice.

3. **Invoice the membership.** On the contact, Membership tab, Buy Membership: choose
   the product, adjust Member Price, Invoice Membership.

   ```python
   wizard = env['membership.invoice'].with_context(active_ids=member.ids).create({
       'product_id': membership.id, 'member_price': 120,
   })
   action = wizard.membership_invoice()
   invoice = env['account.move'].browse(action['domain'][0][2])
   env.cr.commit()
   ```

   Leaves a draft customer invoice with one line and a membership line on the contact
   in `waiting`. The contact needs an invoice address and must not be a free member.

4. **Post the invoice.** The invoice's Confirm button.

   ```python
   invoice.action_post()
   env.cr.commit()
   ```

   Leaves the membership line and the contact in `invoiced`. Posting is accounting:
   the user posts or confirms.

5. **Register the payment.** The invoice's Pay button (Register Payment).

   ```python
   env['account.payment.register'].with_context(active_model='account.move', active_ids=invoice.ids).create({
       'journal_id': bank_journal.id,
   }).action_create_payments()
   env.cr.commit()
   ```

   Leaves the line in `paid` (invoice `payment_state` `in_payment` or `paid`) and the
   contact in `paid` while today is between the line's `date_from` and `date_to`;
   `membership_start` and `membership_stop` show the period.

6. **Follow the members.** Members ‣ Members (filter Members: `invoiced`, `paid`,
   `free`) and Members ‣ Reporting (Members Analysis, `report.membership`: waiting,
   invoiced, paid and the pending and earned amounts).

   Leaves nothing changed. The daily action Membership: update memberships
   (`membership.ir_cron_update_membership`) recomputes `invoiced` and `paid` contacts, so
   an expired membership becomes `old` the day after `date_to`.

## Variations

- **Free member (up to 18.0).** Tick Free Member on the contact: `membership_state`
  becomes `free` without an invoice. Buy Membership is hidden for them.

  ```python
  member.free_member = True
  env.cr.commit()
  ```

- **Associate member (up to 18.0).** On the contact, Associate Member points to another
  member (a person to their company): the contact takes that member's state. A cycle
  is refused.
- **Sell the membership from Sales or the shop (up to 18.0).** Any customer invoice
  line with a membership product creates the membership line, whatever created the
  invoice: a sales order invoiced as in `sales-and-crm.md`, or an eCommerce order. The
  line's `date_from` becomes the invoice date when the invoice falls inside the
  product's period.
- **Cancel a membership (up to 18.0).** Reset the invoice to draft and cancel it: the
  line takes `date_cancel` and `canceled`. Resetting it to draft again clears the date.
- **Assign a level by hand (19.0+).** On the contact, Partner Level (`grade_id`, next to
  Website). Through `write` the level's pricelist is set too; two different pricelists
  in the same write raise an error.

  ```python
  member.write({'grade_id': gold.id})
  print(member.specific_property_product_pricelist.name)
  env.cr.commit()
  ```

- **Members directory, 16.0 to 18.0.** With `website_membership`: publish the membership
  product (Published on its form) and the member (the contact's Published button,
  `is_published`). `/members` lists published contacts with a paid membership line
  valid today, grouped by product and country, plus published free members; the map
  shows companies only.
- **Partners page, 20.0.** With `website_partnership`: publish the level (its Published
  button, on by default) and the contact. `/partners` lists published contacts with an
  active level, grouped by level; options of the page restrict it to companies or add
  search. 19.0: the same page comes with `website_crm_partner_assign`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Module | `membership` | `membership` | `membership` | `partnership` | `partnership` |
| Model of a membership | `membership.membership_line` with dates | same | same | `grade_id` on the contact, no dates | same |
| Members menu | Members (no group) | Members (`account.group_account_invoice`) | same | CRM ‣ Configuration ‣ <label> ‣ Levels | same |
| Membership product | `detailed_type='service'`, `membership` | same | `type='service'`, `membership` | `service_tracking='partnership'`, `grade_id` | same |
| How it is assigned | invoice line of the product | same | same | confirming the sale, or by hand | same |
| Public page | `website_membership`, `/members` | same | same | `website_crm_partner_assign`, `/partners` | `website_partnership`, `/partners` |
| Bundle with Events | `association` | none | none | none | none |

## Verify

19.0 and 20.0:

```python
print(member.commercial_partner_id.grade_id.name, member.commercial_partner_id.specific_property_product_pricelist.name)
```

16.0 to 18.0:

```python
member.invalidate_recordset()
print(member.membership_state, member.membership_start, member.membership_stop)
print([(l.membership_id.name, l.state, l.date_from, l.date_to, l.account_invoice_id.name) for l in member.member_lines])
```

From 19.0 the company has the level and its pricelist; up to 18.0 the contact is `paid`
with the product's period.

## Pitfalls

- A contact created from Members ‣ Members is a free member by default; Buy Membership
  then raises "Partner is a free Member". Untick Free Member first.
- A posted but unpaid invoice leaves the member `invoiced`, and `/members` shows only
  `paid` lines: register the payment, or reconcile the bank line, before expecting the
  member on the website.
- Membership products carry fixed dates. Invoicing last year's product after its
  `date_to` gives a line already expired: the contact stays `old`. Create next period's
  product before the renewals.
- `membership_state` is stored and moves with the date only through the daily action:
  on a copy of production with scheduled actions off, states stay as they were.
- 19.0+: creating a contact with `grade_id` does not set the level's pricelist (only
  `write` does). Create, then write the level.
- 19.0+: the level goes to the commercial partner (the company), not to the person on
  the order.
- `membership` does not exist in 19.0: its dates, free members and associate members
  have no equivalent in `partnership`. Check what the customer relies on before planning
  an upgrade.
- 16.0: `website_membership` depends on `association`, which installs Events. Say so
  before installing it.
