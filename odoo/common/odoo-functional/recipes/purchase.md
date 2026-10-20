# Purchase

A request for quotation (`purchase.order` in state `draft` or `sent`) becomes a purchase
order when confirmed. With `purchase_stock` it creates receipts (`stock.picking`); the
vendor bill (`account.move`, `in_invoice`) is made from the order and checked against
what was ordered or received. Vendor prices live in `product.supplierinfo`. Approval and
locking are per company.

```python
po = env['purchase.order'].search([('name', '=', 'P00042')])
print(po.read(['partner_id', 'state', 'amount_total', 'invoice_status', 'company_id']))
print(po.order_line.read(['product_id', 'product_qty', 'qty_received', 'qty_invoiced']))
print(po.picking_ids.mapped(lambda p: (p.name, p.state)), po.invoice_ids.mapped('name'))
c = po.company_id
print(c.po_double_validation, c.po_double_validation_amount, c.po_lock)
```

## States

`draft` (RFQ), `sent`, `to approve`, `purchase`, `cancel`. 16.0 to 18.0 also have `done`
(Locked); from 19.0 locking is the boolean `locked` and `done` is gone.

## Two-step approval

Orders at or above an amount, in the company currency, wait for a purchase manager
(`purchase.group_purchase_manager`).

```python
env['res.config.settings'].with_company(company).create({
    'po_order_approval': True,
    'po_double_validation_amount': 10000,
}).execute()
env.cr.commit()
```

- `po_order_approval` writes `po_double_validation` (`one_step` / `two_step`) on the
  company. Managers always approve directly.
- `button_confirm()` puts an order over the limit in `to approve`; a manager runs
  `button_approve()`.
- Lock confirmed orders: `lock_confirmed_po` (company `po_lock`: `edit` / `lock`).
- Who is a purchase manager is an access change: see `users-and-access.md`, ask first.

## Bill control

`purchase_method` on the product: `purchase` (bill ordered quantities) or `receive`
(bill received quantities). Services default to `purchase`.

- 16.0 to 18.0: default for new goods from setting `default_purchase_method` (Bill
  Control, kept as an `ir.default`). 19.0+: no setting; new goods take that default if
  one exists, else `receive`.
- Changing it on existing products changes what open orders are ready to bill: list the
  orders in `to invoice` first.

## Receipts

Confirming creates the receipt; validate it in Inventory, or:

```python
picking = po.picking_ids.filtered(lambda p: p.state not in ('done', 'cancel'))
for move in picking.move_ids:
    move.quantity = move.product_uom_qty   # 16.0: quantity_done
picking.button_validate()
env.cr.commit()
```

- `button_validate` may return a wizard (backorder, immediate transfer in 16.0) instead
  of finishing: read the return value. Validating stock is real inventory: only with
  the user's yes, and normally done by the warehouse.

## Vendor bills

```python
action = po.action_create_invoice()
bill = env['account.move'].browse(action.get('res_id')) or po.invoice_ids[-1:]
```

- The bill is a draft; quantities follow the bill control policy. Posting it is
  accounting: the user posts or confirms.
- A bill created first can be filled from the order on the bill form: the onchange
  fields `purchase_vendor_bill_id` and `purchase_id` (not stored) add the order's lines.
- `invoice_status` on the order: `no`, `to invoice`, `invoiced`.
- Three-way matching (`module_account_3way_match`) is Enterprise: it is in settings in
  every version but installs a module not in Community.

## Vendor prices

`product.supplierinfo`, on the template (`seller_ids`) or one variant (`product_id`).

```python
env['product.supplierinfo'].create({
    'partner_id': vendor.id, 'product_tmpl_id': template.id,
    'min_qty': 10, 'price': 4.20, 'currency_id': env.ref('base.EUR').id, 'delay': 5,
    'product_code': 'V-778', 'date_start': '2026-01-01',
})
env.cr.commit()
```

- The first line that matches vendor, quantity, dates and company wins, by `sequence`.
- `discount` from 17.0. Unit: `product_uom` (related to the product's purchase unit) in
  16.0 to 18.0; `product_uom_id` (own unit) in 19.0; `uom_id` in 20.0.
- Old prices: set `date_end` instead of deleting, so history stays readable.
