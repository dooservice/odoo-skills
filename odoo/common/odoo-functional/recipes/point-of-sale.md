# Point of Sale: shops, payment methods, sessions

A shop (`pos.config`) sells the products marked available in POS, with its own payment
methods (`pos.payment.method`), pricelists and fiscal positions. Cashiers sell inside a
session (`pos.session`), opened and closed with the cash counted in the drawer; closing
posts the session's accounting. Needs `point_of_sale` (with `account`). Card terminals,
online payment and restaurant features are separate modules. POS changed a lot between
versions, 20.0 most of all: check the version before running a snippet.

## Before you start

- Apps: `point_of_sale`. Terminals: a `pos_<provider>` module; online payment:
  `pos_online_payment` (17.0+). Ask before installing either: they need the provider's
  credentials.
- Settings: Point of Sale ‣ Configuration ‣ Settings shows one shop at a time (the
  `pos_config_id` field); its `pos_*` fields are the shop's own fields, written below on
  `pos.config` directly.
- Users: `point_of_sale.group_pos_user` (cashier), `point_of_sale.group_pos_manager`.
- Read first:

```python
for c in env['pos.config'].search([]):
    print(c.id, c.name, c.company_id.name, c.journal_id.name, c.payment_method_ids.mapped('name'),
          c.pricelist_id.name, c.cash_control, c.current_session_id.name, c.current_session_state)
print(env['pos.payment.method'].search_read([], ['name', 'type', 'journal_id', 'receivable_account_id', 'config_ids']))
print(env['pos.session'].search_read([('state', '!=', 'closed')], ['name', 'config_id', 'user_id', 'state', 'start_at']))
```

## The standard flow

1. **Create the shop.** Point of Sale ‣ Configuration ‣ Settings ‣ + New Shop (all
   versions), or Point of Sale ‣ Configuration ‣ Point of Sales ‣ New (17.0 to 19.0).

   ```python
   config = env['pos.config'].create({'name': '<shop name>', 'company_id': company.id})
   print(config.journal_id.name, config.payment_method_ids.mapped('name'), config.cash_control)
   env.cr.commit()
   ```

   Leaves a shop without session. It takes the existing bank methods and a cash method
   no other shop uses; from 18.0, when there are none, it creates Cash, Card and Customer
   Account. A second shop usually gets no cash method: step 2.

2. **Payment methods.** Point of Sale ‣ Configuration ‣ Payment Methods ‣ New: a name and
   a journal (a `cash` journal for cash, a `bank` journal for cards); then add it to the
   shop in Settings, section Payment. Use a dedicated cash journal per shop.

   ```python
   cash_journal = env['account.journal'].create({
       'name': '<shop name> cash', 'type': 'cash', 'code': '<short code>', 'company_id': company.id,
   })
   cash = env['pos.payment.method'].create({
       'name': 'Cash', 'type': 'cash', 'journal_id': cash_journal.id, 'company_id': company.id,
   })
   config.write({'payment_method_ids': [(4, cash.id)]})
   print(config.cash_control, cash.type)
   env.cr.commit()
   ```

   Leaves the shop with cash control on: `cash_control` is computed, true whenever the
   shop has a cash method. A method without journal is Customer Account
   (`type='pay_later'`): the order needs a customer and stays in their receivable.

3. **Products.** Point of Sale ‣ Products ‣ Products: tick Available in POS (Sales tab
   up to 17.0, Point of Sale checkbox from 18.0) and set the POS category, created in
   Point of Sale ‣ Configuration ‣ Products ‣ PoS Product Categories.

   ```python
   products.write({'available_in_pos': True, 'pos_categ_ids': [(4, pos_category.id)]})  # 16.0: 'pos_categ_id': pos_category.id
   env.cr.commit()
   ```

4. **Pricelists, fiscal positions, tax display.** Settings of the shop, sections Pricing
   and Accounting; Restrict Categories in the product section.

   ```python
   config.write({
       'limit_categories': True, 'iface_available_categ_ids': [(6, 0, pos_categories.ids)],
       'use_pricelist': True, 'pricelist_id': pricelist.id, 'available_pricelist_ids': [(6, 0, pricelists.ids)],
       'tax_regime_selection': True, 'default_fiscal_position_id': fiscal_position.id,
       'fiscal_position_ids': [(6, 0, fiscal_positions.ids)],
       'iface_tax_included': 'total',
   })
   env.cr.commit()
   ```

   `pricelist_id` must be among `available_pricelist_ids`, all in the shop's currency.
   `tax_regime_selection` lets the cashier pick a fiscal position (eat in, take away).
   Which taxes it maps is the localization's decision: see its localization skill if
   installed. `iface_tax_included`: `total` shows prices with taxes, `subtotal` without.

5. **Open the session.** Point of Sale ‣ Dashboard ‣ New Session then Open Session (16.0
   to 18.0), Open Register (19.0+), counting the opening cash. Done by the cashier in the
   POS, not by script. Leaves the session `opened`.

6. **Sell.** In the POS. Each paid order is `paid`; an order with Invoice ticked and a
   customer gets a posted invoice at once.

7. **Close the session.** In the POS menu ‣ Close (16.0), Close Session (17.0, 18.0),
   Close Register (19.0+): count the cash, then close. Leaves the session `closed`, its
   orders `done`, and the accounting posted (`## Versions`). A session left open is closed
   the same way: Dashboard ‣ Continue Selling, then close. Point of Sale ‣ Orders ‣
   Sessions ‣ Close Session & Post Entries only shows once closing has started
   (`closing_control`).

8. **Invoice a paid order later.** Point of Sale ‣ Orders ‣ Orders ‣ the order ‣ add the
   customer ‣ Invoice.

   ```python
   order = env['pos.order'].browse(<order id>)
   order.write({'partner_id': partner.id, 'to_invoice': True})
   order.action_pos_order_invoice()
   print(order.account_move.name, order.account_move.state, order.state)
   env.cr.commit()
   ```

   Leaves a posted customer invoice (`order.account_move`), outside the session's sales.

## Variations

- **Close a forgotten session from a script**, when nobody can open the POS: only with the
  user's yes. Read the expected cash and ask what they counted:

  ```python
  session = env['pos.session'].browse(<session id>)
  print(session.state, session.order_ids.mapped('state'))
  print(session.get_closing_control_data().get('default_cash_details'))
  ```

  16.0 to 19.0:

  ```python
  if session.config_id.cash_control:
      session.post_closing_cash_details(<counted cash>)
  env.invalidate_all()
  session.update_closing_control_state_session('<closing note>')
  print(session.close_session_from_ui(), session.state, session.move_id.name)
  env.cr.commit()
  ```

  20.0, the counted cash keyed by the cash method:

  ```python
  cash = session.config_id.payment_method_ids.filtered(lambda m: m.type == 'cash')
  print(session.close_session_from_ui({cash.id: <counted cash>} if cash else {}), session.state)
  env.cr.commit()
  ```

- **Limit cash differences.** `set_maximum_difference` with `amount_authorized_diff`:
  above it, only a POS manager can close.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Shop at install | Shop | Shop | none | none | none |
| POS category on product | `pos_categ_id` | `pos_categ_ids` | `pos_categ_ids` | `pos_categ_ids` | `pos_categ_ids` |
| Cash method in two shops | allowed | refused | refused | refused | refused; also two cash methods in one shop |
| Session entries | `move_id` in `journal_id` (POSS, `general`) | same | same | same | customer invoices `sale_move_ids` / `refund_move_ids` in `closing_journal_id` (POSC), to `default_partner_id` |
| Cash at closing | `statement_line_ids` | same | same | same | statement `bank_statement_id` |
| Invoice journal | `invoice_journal_id` | same | same | same | `journal_id` (type `sale`) |
| Invoiced order state | `invoiced` | `invoiced` | `invoiced` | `done` | `paid`, `done` at closing |
| Accounting posted | at closing | at closing | at closing | at closing | at closing, and daily at `session_closing_daily_hour` while open |

Bank methods post one payment per method at closing in every version.

## Verify

```python
session = env['pos.session'].search([('config_id', '=', config.id)], order='id desc', limit=1)
moves = session.move_ids if 'move_ids' in session._fields else session.move_id   # 20.0 / up to 19.0
print(session.state, [(m.name, m.state, m.amount_total) for m in moves], session.order_ids.mapped('state'))
```

Then ask a cashier to open a session, sell once with each method, and close it.

## Pitfalls

- A shop or payment method with a session not closed refuses changes to most fields
  (payment methods, journals, pricelists): close the session first.
- In 20.0, closing without the counted cash counts zero and posts the whole drawer as a
  loss.
- Up to 19.0, without `env.invalidate_all()` after `post_closing_cash_details`, an
  expected amount read earlier is reused and a false difference is posted.
- Draft orders block closing: pay or cancel them in the POS.
- Never edit or reset a closed session's entries; correct with a refund in the POS or a
  new entry, with the accountant.
