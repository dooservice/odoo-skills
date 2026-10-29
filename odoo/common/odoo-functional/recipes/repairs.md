# Repairs

A repair order (`repair.order`) takes a customer's product, adds the parts it consumes,
takes out the broken parts, and puts the repaired product back in stock or at the
customer's disposal, all through stock moves. In 16.0 the repair order carries its own
prices and invoices itself; from 17.0 parts are stock moves and the customer is charged
through a sales quotation made from the repair (20.0 can also invoice directly). This
recipe covers `repair`, `mrp_repair` (kits exploded into parts, manufacturing orders for
parts) and `purchase_repair` (18.0+: purchase orders for parts), all in Community. Field
service, the Helpdesk link and quality checks are Enterprise and left out.

## Before you start

- Apps: `repair` (Repairs). It depends on `sale_management` and `stock` (16.0 also on
  `account`; 17.0+ on `sale_stock`). `mrp_repair` installs itself with `repair` and
  `mrp`; `purchase_repair` (18.0+) with `repair` and `purchase_stock`.
- Settings: none of its own. `group_stock_production_lot` (`inventory.md`) when the
  products to repair or the parts have serial numbers.
- Access: repair orders need the stock user group (`stock.group_stock_user`); reporting
  and configuration need the stock manager group.
- Read first (17.0 to 20.0):

```python
company = env.company
warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
print(warehouse.repair_type_id.read(['name', 'default_location_src_id', 'default_location_dest_id', 'default_remove_location_dest_id', 'default_recycle_location_dest_id']))
print(env['repair.order'].search_read([('state', 'not in', ['done', 'cancel'])], ['name', 'product_id', 'partner_id', 'state', 'sale_order_id']))
```

  The first `print` shows the warehouse's repair operation type and its default
  locations. 16.0 has no repair operation type: read only the repair orders, with
  `invoice_method` and `invoice_id` instead of `sale_order_id`.

States:

| | 16.0 | 17.0 to 19.0 | 20.0 |
|---|---|---|---|
| New | `draft` (Quotation) | `draft` (New) | `draft` (New) |
| Confirmed | `confirmed`, `2binvoiced`, `ready` | `confirmed` | `confirmed` |
| In progress | `under_repair` | `under_repair` | none |
| Finished | `done` (Repaired) | `done` (Repaired) | `done` (Done) |
| Cancelled | `cancel` | `cancel` | `cancel` |

## The standard flow

Odoo's Repairs documentation: create the order with the product and the customer, add
the parts, quote the customer, confirm, repair, end, charge. 16.0 differs in steps 2, 3
and 6 and is shown where it happens.

1. **Create the repair order.** Repairs ‣ Orders ‣ New (16.0: the Repairs app opens the
   list, New).

   17.0 to 20.0:

   ```python
   repair = env['repair.order'].create({
       'partner_id': customer.id,
       'product_id': product.id,
       'lot_id': lot.id,
       'under_warranty': False,
   })
   env.cr.commit()
   ```

   `product_id` is the product to repair (optional); `lot_id` only when it is tracked.
   16.0: create the order with a form in step 2.

   Leaves a repair order in `draft`, numbered from the warehouse's repair operation type
   (`WH/RO/00001`, 17.0+) or from the `RO/` sequence (16.0).

   - 17.0+: `picking_type_id` defaults to the user's warehouse's `repair_type_id` and
     gives the locations: `location_id` (where the product to repair is), the parts'
     source and destination, and where removed and recycled parts go.
   - 16.0: `product_id` is required, `invoice_method` (`none`, `b4repair`,
     `after_repair`) decides when it is invoiced, and prices come from the
     customer's pricelist through onchanges: create it with a form (step 2).

2. **Add the parts.** The Parts tab, Add a line: Type `Add` (a new part, consumed),
   `Remove` (the broken part, taken out) or `Recycle` (17.0+: a part taken out and
   reusable).

   17.0 to 20.0:

   ```python
   from odoo import Command
   repair.write({'move_ids': [
       Command.create({'repair_line_type': 'add', 'product_id': part.id, 'product_uom_qty': 1}),
       Command.create({'repair_line_type': 'remove', 'product_id': broken_part.id, 'product_uom_qty': 1}),
   ]})
   env.cr.commit()
   ```

   Leaves stock moves on the order (`move_ids`), with locations set by the type:

   | Type | From | To |
   |---|---|---|
   | `add` | stock (`location_id` of the operation type) | production (virtual) |
   | `remove` | production | scrap (19.0+: the company's inventory location) |
   | `recycle` | production | stock |

   20.0 also has a Services tab for labour:
   `'repair_service_line_ids': [Command.create({'product_id': service.id, 'quantity': 2})]`
   (service products only). Up to 19.0 labour goes on the quotation (step 3).

   16.0: parts are `repair.line` (`operations`, Type `add` or `remove`) with a price, and
   labour is `repair.fee` (`fees_lines`, the Operations and Fees tabs). Build the order
   with a form so prices and taxes follow the pricelist:

   ```python
   from odoo.tests import Form
   form = Form(env['repair.order'])
   form.product_id = product
   form.partner_id = customer
   form.invoice_method = 'after_repair'
   with form.operations.new() as line:
       line.type = 'add'
       line.product_id = part
       line.product_uom_qty = 1
   with form.fees_lines.new() as fee:
       fee.product_id = service
       fee.product_uom_qty = 2
   repair = form.save()
   env.cr.commit()
   ```

   `remove` lines get price 0 and go from production to the scrap location.

3. **Quote the customer.** 17.0+: the Create Quotation button (20.0: Quote), then
   send and confirm the quotation as in `sales-and-crm.md`.

   17.0 to 20.0:

   ```python
   action = repair.action_create_sale_order()
   order = repair.sale_order_id
   env.cr.commit()
   ```

   Leaves a quotation (`sale.order` in `draft`) for the customer, with one line per
   `add` part (and per service line in 20.0) and the repair linked to it. Labour up to
   19.0: add a service line on the quotation. Lines added or changed on the repair later
   follow on the quotation. With `under_warranty`, part lines are priced 0. The
   order's parts make no delivery: the repair consumes them.

   16.0: the Send Quotation button, or Print Quotation.

   ```python
   action = repair.action_send_mail()
   env['mail.compose.message'].with_context(action['context']).create({}).action_send_mail()
   env.cr.commit()
   ```

   The quotation is the repair order itself; it stays `draft`.

4. **Confirm the repair.** The Confirm Repair button.

   20.0:

   ```python
   repair.action_validate()
   env.cr.commit()
   ```

   16.0 to 19.0:

   ```python
   res = repair.action_validate()
   if isinstance(res, dict):
       env[res['res_model']].with_context(res['context']).create({}).action_done()
   env.cr.commit()
   ```

   Leaves the repair `confirmed` and the parts' moves confirmed (reserved when in stock;
   Check availability, `action_assign()`, retries). Up to 19.0, when the product to
   repair is not in `location_id`, `action_validate` returns the wizard
   `stock.warn.insufficient.qty.repair` instead; its `action_done()` confirms anyway, so
   run it only with the user's yes. 16.0 with `b4repair` leaves it `2binvoiced` until
   invoiced (step 6).

5. **Repair.** Start Repair (17.0 to 19.0; 16.0 from `confirmed` or `ready`), record the
   parts actually used, then End Repair.

   20.0 (no Start Repair):

   ```python
   for move in repair.move_ids:
       move.quantity = move.product_uom_qty
       move.picked = True
   res = repair.action_repair_end()
   env.cr.commit()
   ```

   17.0 to 19.0:

   ```python
   repair.action_repair_start()
   for move in repair.move_ids:
       move.quantity = move.product_uom_qty
       move.picked = True
   res = repair.action_repair_end()
   env.cr.commit()
   ```

   16.0 (the lines' quantities are the ones used):

   ```python
   repair.action_repair_start()
   res = repair.action_repair_end()
   env.cr.commit()
   ```

   Leaves the repair `done`, the part moves `done`, and a move of the repaired product in
   its location (`move_id`) for traceability. Parts left at quantity 0 are cancelled.
   When a quantity differs from the demand, `res` is a wizard instead of the end: 17.0
   `repair.warn.uncomplete.move`, 20.0 `repair.consumption.warning` (18.0 and 19.0 ask
   in the browser, and the method ends it directly). Read `res`. A tracked product needs
   `lot_id`, or ending fails. 16.0 with `after_repair` leaves it `2binvoiced`.

6. **Charge the customer.** 17.0+: confirm the quotation and invoice it from the sales
   order (`sales-and-crm.md`). Delivered quantities on the part lines come from the
   repair's done moves.

   20.0 can invoice without a quotation: the Invoice button, when there is a customer
   and no quotation.

   ```python
   action = repair.action_create_invoice()
   invoice = repair.invoice_ids[-1:]
   env.cr.commit()
   ```

   16.0: the Create Invoice button, when the repair is `2binvoiced`.

   ```python
   repair.action_repair_invoice_create()
   invoice = repair.invoice_id
   env.cr.commit()
   ```

   Leaves a draft customer invoice (`out_invoice`); 16.0 moves the repair to `ready`
   (`b4repair`) or `done` (`after_repair`). Posting it is accounting: the user posts or
   confirms. Several 16.0 repairs at once: select them in the list, Actions ‣ Create
   invoices (`repair.order.make_invoice`, Group by partner invoice address).

## Variations

- **Repair a returned product.** The customer sends the product back with a return of
  its delivery (`inventory.md`). On the return, the Repair button (16.0 to 18.0) or
  Actions ‣ Create Repair (19.0+) opens a repair order linked to it (`picking_id`).
  16.0 to 18.0 show the button only when the receiving operation type has
  `is_repairable` ("Create Repair Orders from Returns"): on Returns in 16.0
  (`warehouse.return_type_id`), on Receipts from 17.0 (`warehouse.in_type_id`); set it
  in Inventory ‣ Configuration ‣ Warehouse Management ‣ Operations Types. The repair's
  Returned flag (`is_returned`) is on once the return is done.

  19.0 and 20.0:

  ```python
  action = return_picking.action_repair_return()
  repair = env['repair.order'].with_context(action['context']).create({'product_id': product.id, 'lot_id': lot.id})
  env.cr.commit()
  ```

  17.0 and 18.0, the flag first:

  ```python
  warehouse.in_type_id.is_repairable = True
  action = return_picking.action_repair_return()
  repair = env['repair.order'].with_context(action['context']).create({'product_id': product.id, 'lot_id': lot.id})
  env.cr.commit()
  ```

  16.0: the same, with the flag on `warehouse.return_type_id`.

- **Repair sold as a service (17.0+).** A product whose sales order creates the repair:
  17.0, 18.0 the product's Create Repair box (`create_repair`, goods or services); 19.0+
  a service with Create on Order set to Repair Order (`service_tracking='repair'`).
  Confirming the sales order creates one confirmed repair order per line (one per unit
  for serial-tracked goods), linked by `sale_order_id` and `sale_order_line_id`;
  cancelling the line cancels it.

  19.0 and 20.0, on a product of type `service`:

  ```python
  template.service_tracking = 'repair'
  env.cr.commit()
  ```

  17.0 and 18.0: `template.create_repair = True` instead.

- **Under warranty (17.0+).** Tick Under Warranty (`under_warranty`) on the repair: part
  lines on the quotation (and, in 20.0, on the invoice) are priced 0. 16.0 only records
  the Warranty Expiration date (`guarantee_limit`); set prices to 0 by hand.

- **Repair a kit (`mrp_repair`).** Adding a part whose bill of materials is a kit
  (`manufacturing.md`) replaces the line by its components, for every type. Services in
  the kit are skipped.

- **Parts bought or made on order (18.0+, `purchase_repair`, `mrp_repair`).** A part with
  the Replenish on Order (MTO) route and a way to supply it (Buy with a vendor price,
  `purchase.md`; or a bill of materials, `manufacturing.md`) is ordered when the repair
  is confirmed. Unarchive the route first (Inventory ‣ Configuration ‣ Warehouse
  Management ‣ Routes, archived filter; needs `group_stock_adv_location`):

  19.0 and 20.0 (Buy and Manufacture are warehouse routes, not product routes):

  ```python
  from odoo import Command
  mto = env.ref('stock.route_warehouse0_mto')
  mto.active = True
  part.product_tmpl_id.route_ids = [Command.link(mto.id)]
  env.cr.commit()
  ```

  18.0, with Buy (or Manufacture, `mrp.route_warehouse0_manufacture`) on the part too:

  ```python
  from odoo import Command
  mto = env.ref('stock.route_warehouse0_mto')
  mto.active = True
  buy = env.ref('purchase_stock.route_warehouse0_buy')
  part.product_tmpl_id.route_ids = [Command.link(mto.id), Command.link(buy.id)]
  env.cr.commit()
  ```

  Leaves, at confirmation, an RFQ or a manufacturing order for the part, linked both
  ways: the repair's Purchase Orders and Manufacturing smart buttons
  (`purchase_count`, `production_count`), and Repairs on the purchase and manufacturing
  orders (`repair_count`). The warehouse's rule for it is `repair_mto_pull_id`. 17.0 has
  no such rule: parts are taken from stock and replenished by reordering rules.

- **Tags and reporting.** Repairs ‣ Configuration ‣ Repair Orders Tags (`repair.tags`,
  `tag_ids`); Repairs ‣ Reporting ‣ Repairs.

- **Cancel or start again.** Cancel Repair (`action_repair_cancel()`), not on a done
  repair; Set to Draft (`action_repair_cancel_draft()`) from cancelled. 17.0+ cancelling
  sets the linked quotation line to quantity 0.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Parts | `repair.line` (`operations`), `add`/`remove`, priced | stock moves (`move_ids`, `repair_line_type`), `add`/`remove`/`recycle` | same | same | same |
| Labour | `repair.fee` (`fees_lines`) | on the quotation | same | same | `repair.service.line` (Services tab) |
| Charging | `invoice_method`, Create Invoice | Create Quotation, sales order | same | same | Quote, or Invoice (`action_create_invoice`) |
| Start Repair, `under_repair` | yes | yes | yes | yes | no: End Repair from `confirmed` |
| Product to repair | required | optional | same | same | same |
| Warranty | `guarantee_limit` date | `under_warranty` prices 0 | same | same | same, also invoice |
| Repair operation type | none | `repair_type_id` (`repair_operation`) | same | same | same |
| Removed parts go to | scrap location | same | same | company's inventory location | `scrap_location_id` |
| Repair from a return | Repair button, Returns type `is_repairable` | Repair button, Receipts type `is_repairable` | same as 17.0 | Actions ‣ Create Repair on any transfer | same |
| Repair from a sales order | no | `create_repair` | same | `service_tracking='repair'` | same |
| Parts ordered on confirmation | no | no | MTO: RFQ or manufacturing order | same | same |
| Unit of the product to repair | `product_uom` | same | same | same | `uom_id` |
| Menu: orders | Repairs (the app) | Repairs ‣ Orders | same | same | same |
| Menu: overview | none | none | Repairs ‣ Overview | none | none |
| Menu: products | none | none | Repairs ‣ Configuration ‣ Products, Product Variants | same | Repairs ‣ Configuration ‣ Products |

The same in every version: Repairs ‣ Reporting ‣ Repairs, Repairs ‣ Configuration ‣
Repair Orders Tags.

## Verify

17.0 to 20.0:

```python
print(repair.read(['state', 'product_id', 'lot_id', 'sale_order_id']))
print(repair.move_ids.mapped(lambda m: (m.product_id.display_name, m.repair_line_type, m.quantity, m.state, m.location_dest_id.display_name)))
print(repair.move_id.state, repair.sale_order_id.state, repair.sale_order_id.invoice_status)
```

16.0:

```python
print(repair.read(['state', 'product_id', 'lot_id', 'invoice_method', 'invoice_id']))
print(repair.operations.mapped(lambda l: (l.product_id.display_name, l.type, l.product_uom_qty, l.state, l.location_dest_id.display_name)))
print(repair.move_id.state, repair.invoice_id.state)
```

The repair is `done`, its `add` parts are `done` into production and its removed parts in
scrap, the repaired product's move is `done`, and the quotation (or invoice) carries the
parts and labour to charge.

## Pitfalls

- Confirming up to 19.0 asks about an insufficient quantity when the product to repair
  is not in the repair location: normal for a product you do not stock; confirm it or
  receive the product first with a return.
- Ending with parts at quantity 0 cancels those parts silently: record the quantities
  used first.
- A serial-tracked product to repair without `lot_id` cannot be ended.
- 17.0+ there is no invoice on the repair (except 20.0's Invoice button): charge through
  the sales order; a repair without a customer cannot get a quotation.
- A quotation already linked blocks Create Quotation again; edit the existing one.
- `action_validate`, `action_repair_end` and the 16.0 invoicing can return a wizard
  instead of finishing: read the result.
- Parts on order need the MTO route active and on the part, plus a vendor price or a bill
  of materials; otherwise they wait for stock.
