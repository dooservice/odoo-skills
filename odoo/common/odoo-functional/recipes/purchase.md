# Purchase

A request for quotation (`purchase.order` in state `draft` or `sent`) becomes a purchase
order when confirmed. With `purchase_stock` it creates receipts (`stock.picking`); the
vendor bill (`account.move`, `in_invoice`) is made from the order and checked against
what was ordered or received. Vendor prices live in `product.supplierinfo`. Approval and
locking are per company. This recipe covers `purchase`, `purchase_stock` and the
Community purchase agreements (`purchase_requisition`: calls for tenders and blanket
orders; `purchase_alternative` for tenders in 20.0). Three-way matching is Enterprise and
left out.

## Before you start

- Apps: `purchase`; `purchase_stock` for receipts; `account` for bills;
  `purchase_requisition` for agreements (setting `module_purchase_requisition`, it
  installs a module: only with the user's yes).
- Settings (Purchase ‣ Configuration ‣ Settings), per company:
  - Two-step approval: orders at or above an amount, in the company currency, wait for
    a purchase manager (`purchase.group_purchase_manager`).

    ```python
    env['res.config.settings'].with_company(company).create({
        'po_order_approval': True,
        'po_double_validation_amount': 10000,
    }).execute()
    env.cr.commit()
    ```

    `po_order_approval` writes `po_double_validation` (`one_step` / `two_step`) on the
    company. Managers always approve directly. Who is a purchase manager is an access
    change: see `users-and-access.md`, ask first.
  - Lock confirmed orders: `lock_confirmed_po` (company `po_lock`: `edit` / `lock`).
  - Bill control: `purchase_method` on the product, `purchase` (bill ordered
    quantities) or `receive` (bill received quantities). Services default to
    `purchase`; in 16.0 and 17.0 only through the form, so a service created from a
    script gets the general default: pass `purchase_method`. 16.0 to 18.0: default for
    new goods from setting `default_purchase_method` (Bill Control, kept as an
    `ir.default`). 19.0+: no setting; new goods take that default if one exists, else
    `receive`. Changing it on existing products changes what open orders are ready to
    bill: list the orders in `to invoice` first.
- Read first:

```python
po = env['purchase.order'].search([('name', '=', 'P00042')])
print(po.read(['partner_id', 'state', 'amount_total', 'invoice_status', 'company_id']))
print(po.order_line.read(['product_id', 'product_qty', 'qty_received', 'qty_invoiced']))
print(po.picking_ids.mapped(lambda p: (p.name, p.state)), po.invoice_ids.mapped('name'))
c = po.company_id or env.company
print(c.po_double_validation, c.po_double_validation_amount, c.po_lock)
```

States: `draft` (RFQ), `sent`, `to approve`, `purchase`, `cancel`. 16.0 to 18.0 also
have `done` (Locked); from 19.0 locking is the boolean `locked` and `done` is gone.

## The standard flow

Odoo's documentation: the vendor's price on the product, then RFQ, send, confirm (and
approve), receive, bill.

1. **Record the vendor's price.** The product form, Purchase tab, Add a line; or
   Purchase ‣ Configuration ‣ Vendor Pricelists ‣ New. `product.supplierinfo`, on the
   template (`seller_ids`) or one variant (`product_id`).

   ```python
   env['product.supplierinfo'].create({
       'partner_id': vendor.id, 'product_tmpl_id': template.id,
       'min_qty': 10, 'price': 4.20, 'currency_id': (vendor.property_purchase_currency_id or company.currency_id).id, 'delay': 5,
       'product_code': 'V-778', 'date_start': '2026-01-01',
   })
   env.cr.commit()
   ```

   Leaves a price that new RFQ lines for this vendor and quantity take, and the vendor
   that the Buy route orders from.

   - `currency_id`: the vendor's purchase currency, else the company's. For another one,
     find it by ISO code, inactive ones included
     (`env['res.currency'].with_context(active_test=False).search([('name', '=', '<currency code>')])`);
     it must be active to be used.
   - The first line that matches vendor, quantity, dates and company wins, by
     `sequence`, then the largest `min_qty`, then the lowest price.
   - `discount` from 17.0. Unit: `product_uom` (related to the product's purchase unit)
     in 16.0 to 18.0; `product_uom_id` (own unit) in 19.0; `uom_id` in 20.0.
   - Old prices: set `date_end` instead of deleting, so history stays readable.

2. **Create the RFQ.** Purchase ‣ Orders ‣ Requests for Quotation ‣ New.

   ```python
   po = env['purchase.order'].create({
       'partner_id': vendor.id,
       'order_line': [(0, 0, {'product_id': product.id, 'product_qty': 10})],
   })
   env.cr.commit()
   ```

   Leaves an RFQ in `draft`, with the vendor price and its lead time on the line.

3. **Send it.** The RFQ's Send by Email button.

   ```python
   action = po.action_rfq_send()
   env['mail.compose.message'].with_context(action['context']).create({}).action_send_mail()
   env.cr.commit()
   ```

   Leaves the RFQ in `sent` and the email in the mail queue. On a copy of production,
   outgoing mail is usually off: say so.

4. **Confirm it.** The Confirm Order button; over the approval amount, a purchase
   manager's Approve Order.

   ```python
   po.button_confirm()
   if po.state == 'to approve':
       po.button_approve()   # only as a purchase manager, with the user's yes
   env.cr.commit()
   ```

   Leaves a purchase order in `purchase` and, with `purchase_stock` and storable
   products, a receipt. An order over the limit confirmed by a non-manager stays in
   `to approve` until a manager runs `button_approve()`.

5. **Receive.** The order's Receipt smart button (or Inventory ‣ Operations ‣ Transfers
   ‣ Receipts from 17.0), Validate.

   ```python
   picking = po.picking_ids.filtered(lambda p: p.state not in ('done', 'cancel'))
   for move in picking.move_ids:
       move.quantity = move.product_uom_qty   # 16.0: quantity_done
   res = picking.button_validate()
   env.cr.commit()
   ```

   Leaves the receipt `done`, `qty_received` on the lines and, with `receive` control,
   the order `to invoice`. `button_validate` may return a wizard (backorder, immediate
   transfer in 16.0) instead of finishing: read `res`. Validating stock is real
   inventory: only with the user's yes, and normally done by the warehouse.

6. **Bill.** The order's Create Bill button.

   ```python
   action = po.action_create_invoice()
   bill = env['account.move'].browse(action.get('res_id')) or po.invoice_ids[-1:]
   ```

   Leaves a draft vendor bill for the quantities the control policy allows and the
   order `invoiced`. Posting it is accounting: the user posts or confirms.
   `invoice_status` on the order: `no`, `to invoice`, `invoiced`.

## Variations

- **The bill first.** Invoicing ‣ Vendors ‣ Bills ‣ New, then the Auto-Complete field
  picks the order: the onchange fields `purchase_vendor_bill_id` and `purchase_id` (not
  stored) add the order's lines.

  ```python
  from odoo.tests import Form
  form = Form(env['account.move'].with_context(default_move_type='in_invoice'))
  form.partner_id = vendor
  form.purchase_vendor_bill_id = env['purchase.bill.union'].search([('purchase_order_id', '=', po.id)], limit=1)
  bill = form.save()
  ```

- **Call for tenders: alternative RFQs to several vendors.** Needs
  `purchase_requisition` (16.0 to 19.0; in 18.0 and 19.0 also the setting
  `group_purchase_alternatives`, "Purchase Alternatives") or `purchase_alternative`
  (20.0, setting `module_purchase_alternative`). On an RFQ, the Alternatives tab ‣ Create
  Alternative, once per vendor:

  ```python
  action = po.action_create_alternative()
  # 16.0-18.0
  wizard = env['purchase.requisition.create.alternative'].with_context(action['context']).create({'partner_id': vendor2.id, 'copy_products': True})
  # 19.0
  wizard = env['purchase.requisition.create.alternative'].with_context(action['context']).create({'partner_ids': [(6, 0, vendor2.ids)], 'copy_products': True})
  # 20.0
  wizard = env['purchase.alternative.create'].with_context(action['context']).create({'partner_ids': [(6, 0, vendor2.ids)], 'copy_products': True})
  wizard.action_create_alternative()
  env.cr.commit()
  ```

  Leaves a new RFQ for the other vendor, in the same group (`purchase_group_id`,
  `alternative_po_ids`). Send each one (step 3) and enter the prices they answer. Then
  Compare Product Lines and Choose the best line per product:

  ```python
  action = po.action_compare_alternative_lines()
  lines = env['purchase.order.line'].search(action['domain'])
  best = lines.sorted('price_unit')[:1]
  best.action_choose()
  env.cr.commit()
  ```

  Choosing sets the other orders' lines for that product to quantity 0. Confirm the
  chosen RFQ (step 4): `button_confirm()` returns a wizard asking what to do with the
  alternatives still open; cancel them (or keep them, to order more later):

  ```python
  res = chosen.button_confirm()
  if isinstance(res, dict):
      env[res['res_model']].with_context(res['context']).create({}).action_cancel_alternatives()
  env.cr.commit()
  ```

  Leaves the chosen order in `purchase` and the others `cancel`. The wizard is
  `purchase.requisition.alternative.warning` up to 19.0, `purchase.alternative.warning`
  in 20.0.

- **Blanket order: a long-term agreement with set prices.** Purchase ‣ Orders ‣ Blanket
  Orders (16.0, 17.0) or Purchase Agreements (18.0+) ‣ New, with `purchase_requisition`.

  ```python
  # 18.0+
  agreement = env['purchase.requisition'].create({
      'vendor_id': vendor.id, 'requisition_type': 'blanket_order', 'date_end': '2026-12-31',
      'line_ids': [(0, 0, {'product_id': product.id, 'product_qty': 1000, 'price_unit': 3.9})],
  })
  agreement.action_confirm()
  # 16.0 / 17.0
  agreement = env['purchase.requisition'].create({
      'vendor_id': vendor.id, 'type_id': env.ref('purchase_requisition.type_single').id, 'date_end': '2026-12-31 23:59:59',
      'line_ids': [(0, 0, {'product_id': product.id, 'product_qty': 1000, 'price_unit': 3.9})],
  })
  agreement.action_in_progress()
  env.cr.commit()
  ```

  Leaves the agreement `confirmed` (18.0+) or `ongoing` (16.0, 17.0) and a vendor price
  line for each product, linked to it (`purchase_requisition_id`), that replenishment
  uses. Every line needs a price and a quantity, or confirming fails. Then each order
  comes from the agreement's New Quotation button:

  ```python
  order = env['purchase.order'].create({'partner_id': agreement.vendor_id.id, 'requisition_id': agreement.id})
  order._onchange_requisition_id()
  env.cr.commit()
  ```

  Leaves an RFQ with the agreement's products and prices; set the quantities and go on
  from step 3. The agreement's `qty_ordered` adds up confirmed orders. Close it with
  `agreement.action_done()` (state `done`) when it ends; it refuses while linked RFQs
  are still open.
  - 16.0, 17.0: `date_end` is a datetime (Agreement Deadline), the agreement type is a
    record (`purchase.requisition.type`, only `type_single`, Blanket Order, in the data)
    whose `exclusive` setting cancels the other orders when one is confirmed.
  - 18.0+: `requisition_type` is `blanket_order` or `purchase_template` (Purchase
    Template, a reusable list of products to order; it creates no vendor prices), with
    `date_start` and `date_end` as dates.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Locked order | state `done` | state `done` | state `done` | boolean `locked` | same |
| Bill control default | setting `default_purchase_method` | same | same | `ir.default` if any, else `receive` | same |
| Create Bill with nothing received | error | error | error | draft bill, quantity 0 | same |
| Vendor price unit | `product_uom` | same | same | `product_uom_id` | `uom_id` |
| Vendor price `discount` | no | yes | yes | yes | yes |
| Validating a receipt | `quantity_done`; immediate transfer wizard | `quantity` | same | same | same |
| Alternative RFQs | `purchase_requisition` | same | same + `group_purchase_alternatives` | same as 18.0 | `purchase_alternative` |
| Alternatives wizard | `purchase.requisition.create.alternative` (`partner_id`) | same | same | same, `partner_ids` (several vendors at once) | `purchase.alternative.create` (`partner_ids`) |
| Agreement type | `type_id` record | same | `requisition_type` selection | same | same |
| Agreement confirm | `action_in_progress()` → `ongoing` | same | `action_confirm()` → `confirmed` | same | same |
| Menu: agreements | Purchase ‣ Orders ‣ Blanket Orders | same | Purchase ‣ Orders ‣ Purchase Agreements | same | same |
| Menu: receipts | Inventory ‣ Operations ‣ Transfers | Inventory ‣ Operations ‣ Transfers ‣ Receipts | same | same | same |
| Menu: units | Purchase ‣ Configuration ‣ Units of Measures ‣ Units of Measure | same | same | Purchase ‣ Configuration ‣ Products ‣ Units & Packagings | same |
| Menu: categories | Purchase ‣ Configuration ‣ Products ‣ Product Categories | same | same | Purchase ‣ Configuration ‣ Products ‣ Categories | same |
| Menu: variants | Purchase ‣ Products ‣ Product Variants | same | same | same | none |

The same in every version: Purchase ‣ Orders ‣ Requests for Quotation, Purchase ‣ Orders
‣ Purchase Orders, Purchase ‣ Orders ‣ Vendors, Purchase ‣ Products ‣ Products, Purchase
‣ Configuration ‣ Vendor Pricelists, Purchase ‣ Configuration ‣ Settings, Invoicing ‣
Vendors ‣ Bills.

## Verify

```python
print(po.state, po.invoice_status, [(l.product_qty, l.qty_received, l.qty_invoiced) for l in po.order_line])
print(po.picking_ids.mapped(lambda p: (p.name, p.state)), po.invoice_ids.mapped(lambda m: (m.move_type, m.state, m.amount_untaxed)))
```

The order is `purchase` with received and billed quantities equal to the ordered ones;
the receipt is `done` and the bill an `in_invoice` draft for the user to post.

## Pitfalls

- An order over the approval amount confirmed by a buyer stays in `to approve`: a
  manager must approve it.
- With `receive` control, Create Bill before the receipt is validated has nothing to
  bill: 16.0 to 18.0 raise "There is no invoiceable line"; 19.0+ create a draft bill
  with quantity 0. Validate the receipt first; remove such an empty draft with the
  user's yes.
- A vendor price in an inactive currency is not used.
- A blanket order line without price or quantity cannot be confirmed.
- Confirming one alternative leaves the others open unless the wizard cancels them.
- Three-way matching (`module_account_3way_match`) is in settings in every version but
  installs an Enterprise module, absent in Community.
