# Point of Sale: discounts, employees, sale orders, stock and receipts

The options a shop adds on top of selling: a global discount button, cashiers that log in
as employees, quotations and sale orders paid at the counter, how the POS moves stock and
ships later, event tickets, SMS receipts, the daily session report and loyalty programs in
the POS. Each is a switch of the shop (`pos.config`) and, most of the time, a small
module installed by that switch. Shops, payment methods and sessions are in
[point-of-sale.md](point-of-sale.md); restaurants in [pos-restaurant.md](pos-restaurant.md);
loyalty programs themselves in [loyalty-and-promotions.md](loyalty-and-promotions.md).
All of it is Community.

**At a glance**

- Apps: `pos_discount`, `pos_hr`, `pos_sale`, `pos_event` (18.0+), `pos_sms` (18.0+),
  `pos_loyalty`; 20.0 `pos_stock` and `pos_sale_stock`.
- Names that change by version: employee rights `employee_ids` in 16.0,
  `basic_employee_ids` and `advanced_employee_ids` 17.0 and 18.0, plus
  `minimal_employee_ids` 19.0, `manager_`, `cashier_`, `restrictive_`,
  `supervised_employee_ids` 20.0; stock in `point_of_sale` up to 19.0, `pos_stock` 20.0;
  `update_stock_quantities` defaults to `closing` up to 17.0, `real` 18.0+;
  `default_product_id` 20.0; session report `pos_daily_sales_reports` in 16.0,
  `point_of_sale` 17.0+; `gift_card_settings` up to 17.0.
- Sections: Before you start; The standard flow (1 global discount, 2 employees log in, 3
  sale orders in the POS, 4 stock from the POS, 5 ship later, 6 event tickets (18.0+), 7
  sMS receipts (18.0+), 8 session report (X and Z), 9 loyalty in the POS); Variations;
  Versions; Verify; Pitfalls.

## Before you start

- Apps: `pos_discount`, `pos_hr` (with `hr`), `pos_sale` (with `sale`, installed by
  itself when both apps are), `pos_event` (18.0+, with `event`), `pos_sms` (18.0+),
  `pos_loyalty` (with `loyalty`). In 20.0 stock in the POS is its own module, `pos_stock`
  (with `pos_sale_stock` for sale orders), installed by itself with Inventory; up to 19.0
  it is part of `point_of_sale`.
- Settings: Point of Sale ‣ Configuration ‣ Settings, pick the shop. The switches named
  `module_pos_*` on the shop (`module_pos_discount`, `module_pos_hr`, `module_pos_sms`)
  install their module at once when ticked: install it first, with the user's yes, and
  restart the shell. Most switches are refused while the shop has a session not closed.
- Read first:

```python
for c in env['pos.config'].search([]):
    print(c.id, c.name, c.current_session_state, c.module_pos_discount, c.module_pos_hr, c.module_pos_sms,
          c.picking_type_id.name, c.warehouse_id.name, c.ship_later)
print(env.company.point_of_sale_update_stock_quantities)
print(env['ir.module.module'].search_read([('name', 'in', ('pos_discount', 'pos_hr', 'pos_sale', 'pos_event', 'pos_sms', 'pos_loyalty', 'pos_stock'))], ['name', 'state']))
```

`module_pos_sms` exists from 18.0: drop it from the print on 16.0 and 17.0.

## The standard flow

Each step is independent: do the ones the shop needs.

1. **Global discount.** Settings, Global Discounts (`module_pos_discount`), then the
   default value (`discount_pc`, 10 by default) and the Discount Product
   (`discount_product_id`). The cashier presses Discount and the POS adds a negative line
   of that product for the percentage of the order.

   ```python
   config.write({'module_pos_discount': True, 'discount_pc': 5.0, 'discount_product_id': discount_product.id})
   env.cr.commit()
   ```

   Leaves a shop that refuses to open without a discount product. Discounts per line (Line Discounts, `manual_discount`, 17.0+) need no module.

2. **Employees log in.** Give each employee a PIN and a badge: Employees ‣ the
   employee ‣ Settings tab (HR Settings up to 17.0) ‣ PIN Code (`pin`) and Badge ID
   (`barcode`). Then Settings, Log in with Employees (`module_pos_hr`) and the lists of
   who logs in with which rights.

   20.0:

   ```python
   employees.write({'pin': '<4 digits from the user>'})
   config.write({
       'module_pos_hr': True,
       'manager_employee_ids': [(6, 0, managers.ids)],
       'cashier_employee_ids': [(6, 0, cashiers.ids)],
   })
   env.cr.commit()
   ```

   20.0 has four levels: `manager_employee_ids` (everything, closing included),
   `cashier_employee_ids` (sales, discounts, refunds), `restrictive_employee_ids` (sales
   and payment, no discounts, refunds or cancellations), `supervised_employee_ids` (sales;
   a higher level approves before payment). 19.0: `advanced_employee_ids` (manager
   rights), `basic_employee_ids`, `minimal_employee_ids`. 17.0, 18.0:
   `advanced_employee_ids`, `basic_employee_ids`. 16.0: one list, `employee_ids`. Empty
   lists mean every employee can log in. Leaves the POS opening on the employee screen;
   each order keeps its cashier (`employee_id`).

3. **Sale orders in the POS.** With `pos_sale`: Settings, section Sales: Sales Team
   (`crm_team_id`, the team that gets the POS orders in the Sales reports), Down Payment
   Product (`down_payment_product_id`), and in 20.0 Default Sale Product
   (`default_product_id`, for description-only sale lines). In the POS, the cashier opens
   Quotation/Order, picks a quotation or sale order of the customer and either settles it
   (its remaining lines go into the POS order) or applies a down payment (a percentage or
   an amount of the down payment product).

   ```python
   config.write({'crm_team_id': team.id, 'down_payment_product_id': down_payment_product.id})
   env.cr.commit()
   ```

   Then, after the sale:

   ```python
   so = env['sale.order'].browse(<sale order id>)
   print(so.state, so.amount_unpaid, so.pos_order_line_ids.mapped('order_id.name'),
         so.order_line.mapped(lambda l: (l.product_id.display_name, l.qty_delivered, l.qty_invoiced)))
   ```

   Leaves the sale order linked to the POS lines (`pos_order_line_ids`, each with
   `sale_order_origin_id`); a settled order counts the products as delivered and
   invoiced by the POS (in 20.0 the delivery part is `pos_sale_stock`). A confirmed sale
   order with a delivery not done gets its delivery cancelled or reduced for the settled
   quantities.

4. **Stock from the POS.** Settings, section Inventory: Operation Type
   (`picking_type_id`, the delivery type of the warehouse, set at creation), Warehouse
   (`warehouse_id`), and Inventory Management for the company
   (`point_of_sale_update_stock_quantities`: `real` creates a delivery per order;
   `closing`, one per session at closing).

   ```python
   env['res.config.settings'].create({'pos_config_id': config.id, 'update_stock_quantities': 'real'}).execute()
   config.write({'picking_type_id': picking_type.id})
   env.cr.commit()
   ```

   Leaves each paid order (or the closed session) with done deliveries from the
   operation type's source location. Default: `real` from 18.0, `closing` in 16.0 and
   17.0. Products tracked by lot or serial ask for the number at sale.

5. **Ship later.** Settings, Allow Ship Later (`ship_later`) with the warehouse, a route
   (`route_id`, optional) and Shipping Policy (`picking_policy`: `direct` or `one`). The
   cashier ticks Ship Later on the payment screen and sets a date (`shipping_date`); the
   order gets a delivery waiting for that date instead of a done one.

   ```python
   config.write({'ship_later': True, 'picking_policy': 'direct'})
   env.cr.commit()
   ```

6. **Event tickets (18.0+).** Install `pos_event`. The ticket product is a service whose
   Create on Order is Event Registration (`service_tracking='event'`),
   available in POS; the event's ticket (`event.event.ticket`) uses it. In the POS the
   event shows as a product; the cashier picks the ticket, fills the attendees and is
   paid.

   ```python
   ticket_product.write({'available_in_pos': True})
   order = env['pos.order'].browse(<order id>)
   print(order.attendee_count, order.lines.mapped('event_registration_ids.name'))
   ```

   Leaves one registration (`event.registration`) per attendee, linked to the order line
   (`pos_order_line_id`). Only tickets of events not finished and on sale load in the POS.

7. **SMS receipts (18.0+).** Settings, SMS Enabled (`module_pos_sms`) and Receipt template
   (`sms_receipt_template_id`, a `sms.template` of `pos.order`). On the receipt screen the
   cashier types the customer's phone and sends. SMS are paid IAP credits.

   ```python
   config.write({'module_pos_sms': True, 'sms_receipt_template_id': env.ref('pos_sms.sms_template_data_point_of_sale').id})
   env.cr.commit()
   ```

8. **Session report (X and Z).** Point of Sale ‣ Reporting ‣ Session Report, pick the
   session, print: the sales, payments, taxes and cash moves of one session (X while it
   is open, Z once closed). 16.0 needs `pos_daily_sales_reports`; from 17.0 it is in
   `point_of_sale`.

   ```python
   wizard = env['pos.daily.sales.reports.wizard'].create({'pos_session_id': session.id})
   print(wizard.generate_report()['report_name'])
   ```

9. **Loyalty in the POS.** Programs are set up in
   [loyalty-and-promotions.md](loyalty-and-promotions.md). On each program, Point of Sale
   (`pos_ok`) and the shops (`pos_config_ids`, empty means every shop with the same
   currency). In the POS, rewards apply when the order meets the rules, and the cashier
   scans or types coupon and gift card codes. 16.0, 17.0: Settings, Gift Cards settings
   (`gift_card_settings`: `create_set` prints new cards, `scan_use` sells pre-printed
   ones).

   ```python
   program.write({'pos_ok': True, 'pos_config_ids': [(6, 0, config.ids)]})
   env.cr.commit()
   ```

## Variations

- **Several sales teams for several shops.** Give each shop its own `crm_team_id`: the
  team's dashboard shows the open sessions and the session sales of its shops.
- **One delivery per session.** `update_stock_quantities = 'closing'` creates the
  deliveries at closing only; faster for shops with many orders, but stock shown during
  the day does not include the open session's sales.
- **Employees without an Odoo user.** With `pos_hr`, only the session's user needs a login;
  the other cashiers are employees with a PIN.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Employee rights fields | `employee_ids` | `basic_employee_ids`, `advanced_employee_ids` | same | adds `minimal_employee_ids` | `manager_`, `cashier_`, `restrictive_`, `supervised_employee_ids` |
| Stock in the POS | `point_of_sale` | same | same | same | `pos_stock`, `pos_sale_stock` |
| Default `update_stock_quantities` | `closing` | `closing` | `real` | `real` | `real` |
| Default sale product | no | no | no | no | `default_product_id` |
| Event tickets | no | no | `pos_event` | same | same |
| SMS receipts | no | no | `pos_sms` | same | same |
| Session report | `pos_daily_sales_reports` | `point_of_sale` | same | same | same |
| Gift card setting on the shop | `gift_card_settings` | same | none | none | none |

## Verify

```python
config = env['pos.config'].browse(<shop id>)
print(config.module_pos_discount, config.discount_product_id.name, config.module_pos_hr, config.crm_team_id.name,
      config.picking_type_id.name, config.ship_later)
orders = env['pos.order'].search([('config_id', '=', config.id)], order='id desc', limit=5)
print([(o.name, o.state, o.employee_id.name, o.picking_ids.mapped('state')) for o in orders])
```

Then ask a cashier to log in with a PIN, give a global discount, settle a quotation and
sell a ship-later order, and check the deliveries.

## Pitfalls

- Global Discounts with no discount product: the shop refuses to open (`A discount product
  is needed to use the Global Discount feature.`).
- `module_pos_discount` and `module_pos_hr` cannot change while the shop has a session
  not closed.
- A product with negative stock does not stop a POS sale: the delivery goes through and
  the quant goes negative; fix it with an inventory adjustment.
- SMS without IAP credits are not sent and the POS shows an error.
