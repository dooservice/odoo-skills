# Purchase from manufacturing, kits and agreements

What purchasing does when it meets manufacturing and stock: components bought for a
manufacturing order and kept linked to it, kits bought from a vendor and received as
their components, and purchase agreements tied to a warehouse and used by
replenishment. It covers `purchase_mrp` (installed by itself with `mrp` and
`purchase_stock`), `purchase_requisition_stock` (by itself with `purchase_requisition`
and `purchase_stock`) and, in 20.0, `purchase_alternative_stock` (by itself with
`purchase_alternative` and `purchase_stock`). The plain purchase flow, agreements and
alternatives are in `purchase.md`, routes and reordering rules in `inventory.md`, bills
of materials and manufacturing orders in `manufacturing.md`; this recipe only adds what
changes when they meet. All of it is Community.

**At a glance**

- Apps: `purchase`, `purchase_stock`, `mrp` (gives `purchase_mrp`);
  `purchase_requisition` (gives `purchase_requisition_stock`); 20.0:
  `purchase_alternative` (gives `purchase_alternative_stock`).
- Names that change by version: Make to order route unarchived by hand up to 18.0, setting
  `replenish_on_order` 19.0+; Buy route on the product up to 18.0, on the warehouse
  (`buy_to_resupply`) 19.0+; `created_purchase_line_id` in 16.0,
  `created_purchase_line_ids` 17.0+; alternatives from `purchase_requisition_stock` up to
  19.0, `purchase_alternative_stock` 20.0.
- Sections: Before you start; The standard flow (1 make the component bought on order, 2
  confirm the manufacturing order, 3 confirm the purchase, 4 receive the components);
  Variations; Versions; Verify; Pitfalls.

## Before you start

- Settings (Inventory ‣ Configuration ‣ Settings):
  - `group_stock_adv_location` (Multi-Step Routes): shows the Routes menu, the product's
    routes and the agreement's Operation Type.
  - Make to order for components, 19.0 and 20.0: `replenish_on_order` ("Replenish on
    Order (MTO)"), which unarchives the route `stock.route_warehouse0_mto`. 16.0 to 18.0
    have no setting: unarchive the route (step 1).

```python
env['res.config.settings'].create({'group_stock_multi_locations': True, 'group_stock_adv_location': True, 'replenish_on_order': True}).execute()
env.cr.commit()
```

  16.0 to 18.0: the same without `replenish_on_order`.

- Read first:

```python
company = env.company
warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
mto = env.ref('stock.route_warehouse0_mto')
print(mto.active, component.route_ids.mapped('name'))
print(component.seller_ids.read(['partner_id', 'price', 'min_qty', 'sequence', 'purchase_requisition_id']))
print(env['mrp.bom'].search_read([('product_tmpl_id', '=', kit.product_tmpl_id.id)], ['type', 'product_qty']))
print(env['purchase.requisition'].search_read([('vendor_id', '=', vendor.id)], ['name', 'state', 'picking_type_id']))
```

## The standard flow

Buying the components of a manufacturing order, the way Odoo's documentation sets it:
the component is bought on order, so confirming the manufacturing order creates the
request for quotation.

1. **Make the component bought on order.** 16.0 to 18.0: Inventory ‣ Configuration ‣
   Warehouse Management ‣ Routes, filter Archived, open Replenish on Order (MTO),
   Unarchive (19.0, 20.0: the setting above). Then on the component's form, Inventory
   tab, Routes: tick Replenish on Order (MTO) and, 16.0 to 18.0, Buy.

   19.0, 20.0 (the route is already active through `replenish_on_order`):

   ```python
   from odoo import Command
   mto = env.ref('stock.route_warehouse0_mto')
   component.product_tmpl_id.write({'route_ids': [Command.link(mto.id)]})
   env.cr.commit()
   ```

   16.0 to 18.0:

   ```python
   from odoo import Command
   mto = env.ref('stock.route_warehouse0_mto')
   mto.active = True
   buy = env.ref('purchase_stock.route_warehouse0_buy')
   component.product_tmpl_id.write({'route_ids': [Command.link(mto.id), Command.link(buy.id)]})
   env.cr.commit()
   ```

   Leaves a component that is ordered from its vendor each time a manufacturing order
   needs it. In 19.0 and 20.0 Buy is a route of the warehouse (`buy_to_resupply`), not
   of the product. The component needs a vendor price (`purchase.md` step 1).

2. **Confirm the manufacturing order.** Manufacturing ‣ Operations ‣ Manufacturing
   Orders ‣ New, Confirm (`manufacturing.md` step 5).

   ```python
   mo = env['mrp.production'].create({'product_id': finished.id, 'bom_id': bom.id, 'product_qty': 5})
   mo.action_confirm()
   env.cr.commit()
   ```

   Leaves the order `confirmed` and a draft request for quotation to the component's
   vendor, linked to the component move. The order shows a Purchases smart button
   (`action_view_purchase_orders`, `purchase_order_count`); the RFQ shows a
   Manufacturing one (`action_view_mrp_productions`, `mrp_production_count`).

3. **Confirm the purchase.** The order's Purchases smart button ‣ the RFQ ‣ Confirm Order
   (`purchase.md` step 4).

   ```python
   action = mo.action_view_purchase_orders()
   po = env['purchase.order'].browse(action.get('res_id')) or env['purchase.order'].search(action['domain'])
   po.button_confirm()
   env.cr.commit()
   ```

   Leaves the purchase order in `purchase` and a receipt whose moves feed the
   manufacturing order's component move. Several manufacturing orders confirmed for the
   same vendor add lines to the same open RFQ.

4. **Receive the components.** The receipt, Validate (`purchase.md` step 5).

   Leaves the receipt `done`; the components are reserved for the manufacturing order
   (`reservation_state` `assigned`), which goes on from `manufacturing.md` step 6.

## Variations

- **Buy a kit.** A product with a kit bill of materials (`type='phantom'`,
  `manufacturing.md`) bought from a vendor is received as its components. Put the
  vendor price on the kit and order the kit (`purchase.md` steps 1 to 4): the receipt
  lists the components, never the kit. After validating it, the kit line's
  `qty_received` counts only complete kits, and the bill (step 6 of `purchase.md`)
  bills those.

  ```python
  po = env['purchase.order'].create({'partner_id': vendor.id, 'order_line': [(0, 0, {'product_id': kit.id, 'product_qty': 10})]})
  po.button_confirm()
  print([(m.product_id.display_name, m.product_uom_qty) for m in po.picking_ids.move_ids])
  env.cr.commit()
  ```

  With automated valuation the kit's price is split among the components: by default
  equally, or by the Cost Share (%) column of the kit's bill (`cost_share` on
  `mrp.bom.line`, an optional column shown only on kit bills). The shares of a bill are
  all 0 or add up to 100, otherwise saving it fails.

  ```python
  bom.bom_line_ids[0].cost_share = 70
  bom.bom_line_ids[1].cost_share = 30
  env.cr.commit()
  ```

- **Components by reordering rule instead of on order.** A reordering rule on the
  component (`inventory.md` step 5) buys for stock, not for one manufacturing order:
  the RFQ is not linked to the order and no Purchases smart button appears. Choose it
  for components shared by many products; choose make to order for components bought
  per order.

- **A blanket order received in a given warehouse.** With `purchase_requisition_stock`
  the agreement has an Operation Type (`picking_type_id`, required, default the
  company's first receipt type; shown with `group_stock_adv_location`, editable only in
  draft). Every RFQ made from the agreement's New Quotation button takes it, so its
  receipt goes to that warehouse. Create the agreement as in `purchase.md`, adding it:

  ```python
  agreement.write({'picking_type_id': warehouse.in_type_id.id})
  env.cr.commit()
  ```

  A `warehouse_id` field also exists (default the main warehouse) but no form shows it
  and nothing uses it.

- **Replenishment orders under a blanket order.** Confirming a blanket order creates a
  vendor price per line linked to it (`purchase_requisition_id`). When replenishment (a
  reordering rule or make to order) picks that vendor price, the RFQ it creates carries
  the agreement (`requisition_id`), the agreement's name as vendor reference
  (`partner_ref`) and its currency, and is grouped only with RFQs of the same
  agreement. The vendor price is chosen like any other (`purchase.md` step 1, by
  `sequence` first): to make replenishment use the agreement, give its vendor price the
  lowest `sequence`, with the user's yes.

  ```python
  info = env['product.supplierinfo'].search([('purchase_requisition_id', '=', agreement.id), ('product_id', '=', component.id)])
  info.sequence = min(component.seller_ids.mapped('sequence')) - 1
  env.cr.commit()
  ```

- **Alternatives of a replenishment RFQ.** Creating alternatives (`purchase.md`, call
  for tenders) from an RFQ made by replenishment or by a manufacturing order copies its
  operation type and, from 17.0, its link to the moves it supplies (`move_dest_ids`):
  whichever alternative is confirmed still feeds that order. In 16.0 only the operation
  type and procurement group are copied. The Alternatives tab and Compare Product Lines
  show each vendor's on-time delivery rate (OTD, `on_time_rate_perc`, hidden when the
  vendor has no history); in 20.0 this comes from `purchase_alternative_stock`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Make to order route | archived, unarchive by hand | same | same | setting `replenish_on_order` | same |
| Buy route on the component | on product | on product | on product | warehouse (`buy_to_resupply`) | same |
| MTO component without vendor price | confirming the manufacturing order fails | same | same | the component falls back to stock, no RFQ | same |
| Move to RFQ link | `created_purchase_line_id` | `created_purchase_line_ids` | same | same | same |
| Alternatives keep `move_dest_ids` | no | yes | yes | yes | yes |
| OTD on alternatives from | `purchase_requisition_stock` | same | same | same | `purchase_alternative_stock` |
| `purchase_alternative_stock` | none | none | none | none | yes |

The same in every version: the Purchases and Manufacturing smart buttons, the Cost
Share (%) column, the agreement's Operation Type, Manufacturing ‣ Operations ‣
Manufacturing Orders, Inventory ‣ Configuration ‣ Warehouse Management ‣ Routes.

## Verify

```python
print(mo.purchase_order_count, mo.reservation_state, [(m.product_id.display_name, m.state) for m in mo.move_raw_ids])
print(po.mrp_production_count, po.state, po.picking_ids.mapped(lambda p: (p.name, p.state)))
print([(l.product_id.display_name, l.product_qty, l.qty_received, l.qty_invoiced) for l in kit_po.order_line])
print(env['purchase.order'].search_read([('requisition_id', '=', agreement.id)], ['name', 'partner_ref', 'picking_type_id', 'state']))
```

The manufacturing order counts its purchase, the purchase its manufacturing order; the
kit line's received quantity equals the complete kits received; orders under the
agreement carry it and its operation type.

## Pitfalls

- 16.0 to 18.0: a component with Replenish on Order (MTO) but without Buy, or without a
  vendor price, blocks confirming the manufacturing order. Add the route or the price.
- 19.0 and 20.0: the same missing vendor price confirms the order silently and buys
  nothing; the component waits for stock. Check the Purchases smart button after
  confirming.
- Make to order with the route archived does nothing: 16.0 to 18.0 need the route
  unarchived, 19.0 and 20.0 the setting.
- Cancelling a manufacturing order leaves its RFQ as it is, with an exception activity
  on it: cancel or adjust the RFQ with the user's yes.
- A kit partly received is not partly billed: `qty_received` counts complete kits only.
  Receive the missing components or bill by hand.
- Cost shares that do not add up to 100 make the bill of materials fail to save.
- A blanket order's vendor price loses to cheaper or earlier vendor prices in
  replenishment unless its `sequence` comes first.
