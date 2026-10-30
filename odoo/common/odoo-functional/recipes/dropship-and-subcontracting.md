# Dropshipping and subcontracting

Two ways to let a vendor do part of the work. Dropshipping: the vendor ships a product
you sell straight to your customer; nothing goes through your warehouse. Subcontracting:
a vendor (the subcontractor) manufactures a product for you from a bill of materials;
you buy the finished product from it, optionally sending it the components. This recipe
covers `stock_dropshipping`, `mrp_subcontracting`, `mrp_subcontracting_purchase` (the
links between the purchase order and the subcontracting transfers) and
`mrp_subcontracting_dropshipping` (components or finished goods shipped by a vendor
directly to or from the subcontractor), all in Community and in 16.0 to 20.0. Purchase
orders and receipts work as in `purchase.md`; transfers as in `inventory.md`; bills of
materials as in `manufacturing.md`.

**At a glance**

- Apps: `sale_stock`, `purchase_stock` (dropshipping); `mrp`, `purchase_stock`
  (subcontracting); `mrp_subcontracting_purchase`, `mrp_subcontracting_dropshipping`.
- Names that change by version: Dropship operation type `code` `incoming` (16.0),
  `dropship` (17.0+); sales line route `route_id` (16.0-18.0), `route_ids` (19.0+);
  Resupply Subcontractor on Order product route (16.0-18.0), warehouse
  `subcontracting_to_resupply` (19.0+); Dropship Subcontractor on Order route (16.0-18.0),
  Dropship route (19.0+); `quantity_done` (16.0), `quantity` (17.0+).
- Sections: Before you start; The standard flow (1 vendor and dropship route, 2 sell it,
  3 confirm the purchase, 4 validate the dropship, 5 subcontractor and bill, 6 its price,
  7 who supplies components, 8 order from the subcontractor, 9 send the components,
  10 receive the products); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `sale_stock` and `purchase_stock` for dropshipping; `mrp` and `purchase_stock`
  for subcontracting. `mrp_subcontracting_purchase` and
  `mrp_subcontracting_dropshipping` install by themselves once their dependencies are
  there.
- Settings, each installs a module: only with the user's yes.

```python
env['res.config.settings'].create({'module_stock_dropshipping': True}).execute()
env['res.config.settings'].create({'module_mrp_subcontracting': True}).execute()
env.cr.commit()
```

- `module_stock_dropshipping`: "Dropshipping", in Purchase ‣ Configuration ‣ Settings
  (all versions) and in Inventory ‣ Configuration ‣ Settings (17.0+).
- `module_mrp_subcontracting`: "Subcontracting", in Manufacturing ‣ Configuration ‣
  Settings.
- Choosing a route on a sales order line needs `group_stock_adv_location` (Multi-Step
  Routes, `inventory.md`).
- Read first:

```python
company = env.company
warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
product = env['product.product'].search([('default_code', '=', '<reference>')], limit=1)
print(product.route_ids.mapped('name'))
print(product.seller_ids.read(['partner_id', 'min_qty', 'price', 'company_id']))
print(env.ref('stock_dropshipping.route_drop_shipping').rule_ids.filtered(lambda r: r.company_id == company).picking_type_id.mapped('name'))
print(env['mrp.bom'].search_read([('product_tmpl_id', '=', product.product_tmpl_id.id)], ['type', 'subcontractor_ids', 'company_id']))
print(warehouse.read(['subcontracting_to_resupply', 'subcontracting_type_id', 'subcontracting_resupply_type_id']), company.subcontracting_location_id.complete_name)
```

## The standard flow

Dropshipping first (steps 1 to 4), then subcontracting (steps 5 to 10), in the order of
Odoo's documentation of each.

1. **Give the product a vendor and the Dropship route.** The product form: Purchase tab,
   a vendor line (`purchase.md`, step 1); Inventory tab, Routes, tick Dropship.

   ```python
   from odoo import Command
   dropship = env.ref('stock_dropshipping.route_drop_shipping')
   product.product_tmpl_id.write({'route_ids': [Command.link(dropship.id)]})
   env.cr.commit()
   ```

   Leaves every sale of the product dropshipped. The Dropship route stays selectable on
   the product in 19.0 and 20.0, where Buy and Manufacture are not.

2. **Sell it.** Sales ‣ Orders ‣ Quotations ‣ New, then Confirm (`sales-and-crm.md`).

   ```python
   so = env['sale.order'].create({
       'partner_id': customer.id,
       'order_line': [Command.create({'product_id': product.id, 'product_uom_qty': 3})],
   })
   so.action_confirm()
   po = so._get_purchase_orders()
   env.cr.commit()
   ```

   Leaves the order in `sale` and a request for quotation (`draft`) to the vendor, with
   the company's Dropship operation type and the customer's delivery address in
   `dest_address_id` (Dropship Address). The order shows a Purchase smart button and no
   delivery.

3. **Confirm the purchase order.** The RFQ's Confirm Order (`purchase.md`, step 4).

   ```python
   po.button_confirm()
   dropship_picking = po.picking_ids.filtered('is_dropship')
   env.cr.commit()
   ```

   Leaves the order in `purchase` and a dropship transfer (`DS/00001`) from Partners/Vendors
   to Partners/Customers, visible from the Dropship smart button of both orders and, from
   17.0, in Inventory ‣ Operations ‣ Transfers ‣ Dropships.

4. **Validate the dropship when the vendor has shipped.** The dropship transfer,
   Validate.

   ```python
   for move in dropship_picking.move_ids:
       move.quantity = move.product_uom_qty
   res = dropship_picking.button_validate()
   env.cr.commit()
   ```

   In 16.0 set `move.quantity_done` instead of `move.quantity`.

   Leaves the transfer `done`, `qty_delivered` on the sales order line and
   `qty_received` on the purchase line: invoice the customer and bill the vendor as
   usual. `res` may be a wizard (backorder, immediate transfer in 16.0): read it.

5. **Create the subcontractor and the subcontracting bill of materials.** The vendor is
   a contact (`partners-and-imports.md`). Manufacturing ‣ Products ‣ Bills of
   Materials ‣ New, BoM Type Subcontracting, Subcontractors.

   ```python
   bom = env['mrp.bom'].create({
       'product_tmpl_id': finished.product_tmpl_id.id, 'product_qty': 1,
       'type': 'subcontract', 'subcontractor_ids': [Command.link(subcontractor.id)],
       'bom_line_ids': [Command.create({'product_id': component.id, 'product_qty': 2})],
   })
   env.cr.commit()
   ```

   Leaves a bill that any purchase of the product from one of those subcontractors
   uses. Without `subcontractor_ids` it applies to no one.

6. **Record the subcontractor's price.** The finished product's Purchase tab, a line for
   the subcontractor: the price is what the subcontractor charges for the work, not
   the components.

   ```python
   env['product.supplierinfo'].create({'partner_id': subcontractor.id, 'product_tmpl_id': finished.product_tmpl_id.id, 'price': 12.0})
   env.cr.commit()
   ```

7. **Decide who supplies the components.** By default the subcontractor uses its own,
   and the receipt consumes them from the company's Subcontracting location
   (`company.subcontracting_location_id`). To send them yourself:

   - 16.0 to 18.0: on each component, Inventory tab, Routes, tick Resupply Subcontractor
     on Order.

     ```python
     component.product_tmpl_id.write({'route_ids': [Command.link(env.ref('mrp_subcontracting.route_resupply_subcontractor_mto').id)]})
     env.cr.commit()
     ```

   - 19.0 and 20.0: the route is a warehouse route, not selectable on a product. Every
     warehouse with Resupply Subcontractors (`subcontracting_to_resupply`, Inventory ‣
     Configuration ‣ Warehouse Management ‣ Warehouses, on by default) sends the
     components of each subcontracting order. Turn it off on the warehouse when the
     subcontractor always uses its own components.

8. **Order from the subcontractor.** Purchase ‣ Orders ‣ Requests for Quotation ‣ New,
   the finished product, Confirm Order.

   ```python
   po = env['purchase.order'].create({
       'partner_id': subcontractor.id,
       'order_line': [Command.create({'product_id': finished.id, 'product_qty': 10})],
   })
   po.button_confirm()
   receipt = po.picking_ids.filtered(lambda p: p.picking_type_code == 'incoming' and p.state not in ('done', 'cancel'))
   production = receipt.move_ids._get_subcontract_production()
   resupply = po._get_subcontracting_resupplies()
   env.cr.commit()
   ```

   Leaves the order in `purchase`, a receipt from the subcontractor, a subcontracting
   manufacturing order (`subcontractor_id` set, operation type Subcontracting, not in
   the Manufacturing menus) and, when components are resupplied, a resupply transfer
   from stock to the subcontractor (the order's Resupply smart button, from
   `mrp_subcontracting_purchase`).

9. **Send the components.** The resupply transfer (Inventory ‣ Overview, card Resupply
   Subcontractor), Validate, as in `inventory.md` step 6.

   Leaves the components in the subcontractor's location, still counted as your stock.

10. **Receive the finished products.** The receipt, Validate.

    ```python
    for move in receipt.move_ids:
        move.quantity = move.product_uom_qty
    res = receipt.button_validate()
    env.cr.commit()
    ```

    In 16.0 set `move.quantity_done` instead of `move.quantity`.

    Leaves the receipt `done`, the subcontracting manufacturing order `done` (components
    consumed from the subcontractor's location, finished products in stock) and the
    order ready to bill (`purchase.md`, step 6). With tracked components, record their
    lots before validating:

    - 16.0 to 18.0: the receipt's Record components button opens the manufacturing
      order; set the quantity and the lots, then Record Production
      (`production.subcontracting_record_component()`). Mandatory with tracked
      components, optional otherwise when the bill's consumption is not strict.
    - 19.0 and 20.0: the receipt's Subcontracting Productions smart button (Subcontracted
      Productions in 20.0) opens the same order to set the lots
      (`receipt.action_show_subcontract_details()`).

## Variations

- **Dropship one line only.** Leave the product without the route and set it on the
  sales order line (column Route, needs `group_stock_adv_location`): `route_id` up to
  18.0, `route_ids` in 19.0 and 20.0.

  ```python
  line.write({'route_ids': [Command.link(dropship.id)]})
  ```

  That is 19.0 and 20.0; in 16.0 to 18.0 write `line.write({'route_id': dropship.id})`.
  Do it before confirming the order.
- **Dropship without a sales order.** A purchase order with Deliver To set to the
  Dropship operation type (`picking_type_id`) and a Dropship Address
  (`dest_address_id`); confirming it creates the dropship transfer.
- **Subcontractor portal.** Give the subcontractor portal access (`users-and-access.md`):
  at `/my/productions` it sees its subcontracting orders and records quantities and
  lots itself.
- **Components shipped by their vendor to the subcontractor.** Needs both
  dropshipping and subcontracting (`mrp_subcontracting_dropshipping`). On the
  component: 16.0 to 18.0, route Dropship Subcontractor on Order
  (`mrp_subcontracting_dropshipping.route_subcontracting_dropshipping`); 19.0 and 20.0,
  the Dropship route, whose rules then also cover subcontractors. Confirming the
  subcontracting order creates a purchase order to the component's vendor, delivered to
  the subcontractor (Dropship Subcontractor operation type).
- **Finished product shipped by the subcontractor to the customer.** A subcontracted
  product with the Dropship route: selling it creates a purchase order to the
  subcontractor whose dropship transfer goes straight to the customer; validating it
  marks the subcontracting manufacturing order done.
- **Keep components at the subcontractor ahead of time.** Replenish the subcontracting
  location with a reordering rule on it or a manual transfer of the Resupply
  Subcontractor type, instead of resupplying per order.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Dropshipping setting | Purchase settings | Purchase and Inventory settings | same | same | same |
| Dropship operation type `code` | `incoming` | `dropship` | same | same | same |
| Menu: dropships | smart buttons only | Inventory ‣ Operations ‣ Transfers ‣ Dropships | same | same | same |
| Route on a sales order line | `route_id` | same | same | `route_ids` | same |
| Resupply Subcontractor on Order | product route | same | same | warehouse route, on with `subcontracting_to_resupply` | same |
| Dropship to subcontractor | route Dropship Subcontractor on Order | same | same | Dropship route | same |
| Tracked components at receipt | Record components button | same | same | Subcontracting Productions smart button | Subcontracted Productions smart button |
| Validating a transfer | `quantity_done`; immediate transfer wizard | `quantity` | same | same | same |

The same in every version: the route `stock_dropshipping.route_drop_shipping`, BoM type
`subcontract` with `subcontractor_ids`, the portal page `/my/productions`, Manufacturing
‣ Configuration ‣ Settings, Manufacturing ‣ Products ‣ Bills of Materials.

## Verify

```python
print(so.order_line.read(['product_uom_qty', 'qty_delivered']), dropship_picking.state)
print(po.state, receipt.state, production.state, production.subcontractor_id.name)
print(env['stock.quant'].search_read([('location_id', '=', company.subcontracting_location_id.id)], ['product_id', 'quantity']))
```

The sales line is delivered and the dropship `done`; the subcontracting manufacturing
order is `done` for the subcontractor, and the subcontracting location holds only the
components still at the subcontractor.

## Pitfalls

- A dropshipped product without a vendor price for the quantity and date blocks the
  sales order's confirmation: "There is no matching vendor price to generate the
  purchase order". Add the vendor line, then confirm.
- Dropshipped goods never enter stock: do not receive them in the warehouse as well,
  or stock is counted twice.
- A subcontracting bill without the vendor in `subcontractor_ids` is ignored: the
  purchase becomes a normal receipt and no component is consumed.
- Without resupply, the receipt still consumes components from the subcontracting
  location, whose quantity can go below zero. Expected when the subcontractor buys its
  own components; otherwise resupply first.
- In 19.0 and 20.0 resupply is per warehouse, not per product: a subcontractor that
  owns some components still gets a resupply transfer for all of them while the
  warehouse setting is on. Cancel the lines not needed, with the user's yes.
- Validating a subcontracting receipt finishes its manufacturing order: undo it with a
  return, never by editing the order's moves.
