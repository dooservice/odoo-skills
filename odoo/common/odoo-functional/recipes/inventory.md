# Inventory: warehouses, routes, locations and stock

A warehouse (`stock.warehouse`) brings its own locations, operation types (receipts,
deliveries, internal) and routes. Stock lives in quants (`stock.quant`: product,
location, lot, quantity) and only changes through moves: receipts, deliveries, inventory
adjustments and scrap. Stock that already moved is history; fix it with a new adjustment
or a return, never by editing quants or moves. This recipe covers `stock` and, for batch
transfers, `stock_picking_batch` (16.0 to 19.0; part of `stock` in 20.0), all in
Community; the Barcode app is Enterprise and left out.

## Before you start

- Apps: `stock`; `purchase_stock` and `mrp` give the Buy and Manufacture routes that
  reordering rules use; `stock_picking_batch` for batch transfers up to 19.0.
- Settings (Inventory ‣ Configuration ‣ Settings):

```python
env['res.config.settings'].create({
    'group_stock_multi_locations': True,
    'group_stock_adv_location': True,
    'group_stock_production_lot': True,
}).execute()
env.cr.commit()
```

- `group_stock_multi_locations`: storage locations (shelves, bins) inside a warehouse.
- `group_stock_adv_location`: multi-step routes. The form switches multi-locations on
  with it, but that is an onchange: set both from a script.
- `group_stock_production_lot`: lots and serial numbers.
- A second warehouse in a company turns on multi-warehouse (and multi-locations) by
  itself.
- Read first:

```python
company = env.company
env['stock.warehouse'].search_read([('company_id', '=', company.id)], ['name', 'code', 'reception_steps', 'delivery_steps', 'lot_stock_id'])
env['stock.location'].search_read([('company_id', '=', company.id), ('usage', '=', 'internal')], ['complete_name', 'active'])
env['stock.quant'].search_read([('product_id', '=', product.id), ('location_id.usage', '=', 'internal')], ['location_id', 'lot_id', 'quantity', 'reserved_quantity'])
env['stock.warehouse.orderpoint'].search_read([('product_id', '=', product.id)], ['warehouse_id', 'location_id', 'product_min_qty', 'product_max_qty', 'trigger'])
```

## The standard flow

The order of Odoo's Inventory documentation: the warehouse and its steps, its storage
locations, products tracked in stock, their initial quantities, reordering rules; then
daily transfers.

1. **Create the warehouse and choose its steps.** Inventory ‣ Configuration ‣ Warehouse
   Management ‣ Warehouses ‣ New.

   ```python
   warehouse = env['stock.warehouse'].create({'name': 'Second warehouse', 'code': 'WH2', 'company_id': company.id})
   warehouse.write({'reception_steps': 'two_steps', 'delivery_steps': 'pick_ship'})
   env.cr.commit()
   ```

   Leaves a warehouse with its stock location, operation types and routes.

   - `code` prefixes the warehouse's locations and transfer numbers (`WH2/IN/00001`); at
     most 5 characters up to 19.0.
   - `reception_steps`: `one_step`, `two_steps` (input, then stock), `three_steps`
     (input, quality, stock). The steps need `group_stock_adv_location`.
   - `delivery_steps`: `ship_only`, `pick_ship` (pick to output, then deliver),
     `pick_pack_ship` (pick, pack, deliver).
   - Changing steps reconfigures the warehouse's routes, rules and operation types. Ask
     the user to validate or cancel open receipts and deliveries of that warehouse
     first.

2. **Create its storage locations.** Inventory ‣ Configuration ‣ Warehouse Management ‣
   Locations ‣ New. Needs `group_stock_multi_locations`.

   ```python
   env['stock.location'].create({'name': 'Shelf A', 'location_id': warehouse.lot_stock_id.id, 'usage': 'internal'})
   env.cr.commit()
   ```

   Leaves an internal location under the warehouse's stock.

   `usage`: `internal` (stock you own), `view` (a folder, holds no stock), `supplier`,
   `customer`, `inventory` (adjustment counterpart; up to 18.0 a scrap location is one with
   `scrap_location`, from 19.0 any `inventory` location), `production`, `transit`. Archive a location only when it has no stock.

3. **Make the products tracked in stock.** The product form (Inventory ‣ Products ‣
   Products); `products-and-categories.md` has the write per version.

   | | 16.0, 17.0 | 18.0, 19.0 | 20.0 |
   |---|---|---|---|
   | counted in stock | `detailed_type='product'` | `type='consu'`, `is_storable=True` | same, `is_storable` now in `product` |
   | tracking | `tracking`: `serial`, `lot`, `none` | same | `tracking`: `lot`, `serial` or empty; `store_by` |

   In 20.0 `store_by` (`untracked`, `quantity`, `lot`, `serial`) is the form's single
   choice and writes `is_storable` and `tracking` for you. Turning a product with stock
   into a non-stored one, or changing its tracking, needs the user's yes: quantities and
   lots already recorded do not follow.

4. **Set the initial quantities.** Inventory ‣ Operations ‣ Physical Inventory (16.0:
   Inventory ‣ Operations ‣ Inventory Adjustments): Counted Quantity, then Apply. An
   inventory adjustment, never a write of `quantity`:

   ```python
   quant = env['stock.quant'].with_context(inventory_mode=True).create({
       'product_id': product.id,
       'location_id': warehouse.lot_stock_id.id,
       'inventory_quantity': 40,
   })
   quant.action_apply_inventory()
   env.cr.commit()
   ```

   Leaves the quantity on hand and a done move from the inventory adjustment location.

   - The user running it needs the stock user group (`stock.group_stock_user`). The
     shell's superuser and the administrator have it; a user without it gets an access
     error.
   - Tracked products need `lot_id` (an existing or new `stock.lot`, with `name`,
     `product_id` and `company_id`). One quant per serial number, quantity 1.
   - If `action_apply_inventory()` returns an action instead of applying (quants changed
     meanwhile, conflicts), stop and show it to the user.
   - With automated valuation each adjustment posts a journal entry: say so.

5. **Add reordering rules.** Inventory ‣ Operations ‣ Replenishment (16.0) or Inventory ‣
   Operations ‣ Procurement ‣ Replenishment (17.0+) ‣ New; also the product's Min / Max
   smart button.

   ```python
   env['stock.warehouse.orderpoint'].create({
       'product_id': product.id, 'warehouse_id': warehouse.id, 'location_id': warehouse.lot_stock_id.id,
       'product_min_qty': 10, 'product_max_qty': 50, 'trigger': 'auto',
   })
   env.cr.commit()
   ```

   Leaves a rule that the scheduler reads.

   - `trigger`: `auto` (the scheduler creates purchase or manufacturing orders) or
     `manual` (shown in Replenishment for someone to order).
   - The product needs a route that can supply it: Buy with a vendor price
     (`purchase.md`), or Manufacture with a bill of materials (`manufacturing.md`).
     Without one the scheduler orders nothing and leaves an exception activity on the
     product saying why.
   - `qty_multiple` (order in multiples) exists up to 18.0; from 19.0 rounding comes from
     `replenishment_uom_id`.

6. **Process receipts and deliveries.** Inventory ‣ Overview, the operation type's card
   (or Inventory ‣ Operations ‣ Transfers ‣ Receipts / Deliveries from 17.0), the
   transfer, Validate. Purchases and sales create them (`purchase.md`,
   `sales-and-crm.md`).

   ```python
   picking.action_assign()
   for move in picking.move_ids:
       move.quantity = move.product_uom_qty   # 16.0: quantity_done
   res = picking.button_validate()
   env.cr.commit()
   ```

   Leaves the transfer `done` and the stock moved. `button_validate` may return a wizard
   (backorder, immediate transfer in 16.0) instead of finishing: read `res`. Validating
   stock is real inventory: only with the user's yes, and normally done by the
   warehouse.

## Variations

- **Batch transfers: one picker, several orders.** Settings: `module_stock_picking_batch`
  ("Batch Transfers" in 16.0, 17.0; "Batch, Wave & Cluster Transfers" in 18.0, 19.0;
  it installs `stock_picking_batch`, only with the user's yes) or, in 20.0, the group
  `group_stock_picking_batch` in `stock` (same label, no module). Odoo's documentation
  also turns on storage locations and multi-step routes for it. Create the batch from
  the transfers list (select ‣ Actions ‣ Add to batch) or from the batch menu (see
  `## Versions`) ‣ New:

  ```python
  batch = env['stock.picking.batch'].create({
      'user_id': env.user.id, 'picking_type_id': warehouse.out_type_id.id,
      'picking_ids': [(6, 0, pickings.ids)],
  })
  batch.action_confirm()
  env.cr.commit()
  ```

  The Add to batch action is the wizard `stock.picking.to.batch`:
  `env['stock.picking.to.batch'].with_context(active_model='stock.picking', active_ids=pickings.ids).create({'mode': 'new', 'user_id': env.user.id}).attach_pickings()`
  (`mode='existing'` with `batch_id` adds to an open batch; `is_create_draft` keeps it
  in draft). Leaves a batch `in_progress` holding the transfers. Validate it once the
  goods are picked:

  ```python
  for move in batch.picking_ids.move_ids:
      move.quantity = move.product_uom_qty   # 16.0: quantity_done
  res = batch.action_done()
  env.cr.commit()
  ```

  Leaves the batch `done` and each transfer `done`. As with a transfer, `res` may be a
  backorder or immediate transfer wizard: read it. Automatic batches (by contact,
  carrier, country, locations) are set on the operation type.

- **Scrap: take damaged goods out of stock.** Inventory ‣ Operations ‣ Scrap (16.0) or
  Inventory ‣ Operations ‣ Adjustments ‣ Scrap (17.0+) ‣ New; also the Scrap action on a
  transfer or a lot. No setting needed.

  ```python
  # 16.0-19.0
  scrap = env['stock.scrap'].create({'product_id': product.id, 'scrap_qty': 2, 'location_id': warehouse.lot_stock_id.id})
  res = scrap.action_validate()
  # 20.0: a scrap is a stock move
  scrap = env['stock.move'].with_context(default_is_scrap=True).create({'product_id': product.id, 'quantity': 2, 'location_id': warehouse.lot_stock_id.id})
  res = scrap.action_scrap()
  env.cr.commit()
  ```

  Leaves the scrap `done` and the quantity moved to the scrap location (Virtual
  Locations/Scrap up to 18.0; from 19.0 the company's `scrap_location_id`, its first
  `inventory` location, Inventory adjustment). If there is not enough stock in the location, `res` is the
  wizard `stock.warn.insufficient.qty.scrap` and nothing moved: stop and show it.
  Tracked products need the lot (`lot_id` up to 19.0, `lot_ids` in 20.0); reasons are
  `scrap_reason_tag_ids` (18.0+); `should_replenish` (17.0 to 19.0;
  `should_replenish_scrapped` in 20.0) runs replenishment for the scrapped quantity.
  In 20.0 a scrap is undone from Inventory ‣ Reporting ‣ Moves History, Actions ‣
  Revert (`action_revert` on its move lines), with the user's yes; up to 19.0 Revert
  only undoes inventory adjustments, not scraps.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Counted in stock | `detailed_type='product'` | same | `is_storable` (from `stock`) | same | `is_storable` (from `product`), `store_by` |
| Validating a transfer | `quantity_done`; immediate transfer wizard | `quantity` | same | same | same |
| Warehouse `code` | at most 5 characters | same | same | same | no size limit |
| Reordering multiple | `qty_multiple` | same | same | `replenishment_uom_id` | same |
| Batch transfers | `stock_picking_batch` | same | same | same | `stock`, group `group_stock_picking_batch` |
| Scrap model | `stock.scrap` | same, `should_replenish` | same, `scrap_reason_tag_ids` | same | `stock.move` with `is_scrap` |
| Revert from Moves History | adjustments only | same | same | same | adjustments and scraps |
| Scrap location | `inventory` with `scrap_location` | same | same | any `inventory` location | same |
| Menu: initial quantities | Inventory ‣ Operations ‣ Inventory Adjustments | Inventory ‣ Operations ‣ Adjustments ‣ Physical Inventory | same | same | same |
| Menu: replenishment | Inventory ‣ Operations ‣ Replenishment | Inventory ‣ Operations ‣ Procurement ‣ Replenishment | same | same | same |
| Menu: reordering rules | Inventory ‣ Configuration ‣ Products ‣ Reordering Rules | same | none (Replenishment) | none | none |
| Menu: run scheduler | Inventory ‣ Operations ‣ Run Scheduler | same | Inventory ‣ Operations ‣ Procurement: run scheduler | same | same |
| Menu: transfers | Inventory ‣ Operations ‣ Transfers | Inventory ‣ Operations ‣ Transfers ‣ Receipts / Deliveries / Internal | same | same | same |
| Menu: batch transfers | Inventory ‣ Operations ‣ Batch Transfers | Inventory ‣ Operations ‣ Transfers ‣ Batch Transfers | Inventory ‣ Operations ‣ Jobs ‣ Batch Transfers | same | same |
| Menu: scrap | Inventory ‣ Operations ‣ Scrap | Inventory ‣ Operations ‣ Adjustments ‣ Scrap | same | same | same |
| Menu: lots | Inventory ‣ Products ‣ Lots/Serial Numbers | same | Inventory ‣ Products ‣ Lots / Serial Numbers | same | same |
| Menu: moves report | Inventory ‣ Reporting ‣ Stock Moves | Inventory ‣ Reporting ‣ Move Analysis | Inventory ‣ Reporting ‣ Moves Analysis | same | same |

The same in every version: Inventory ‣ Configuration ‣ Warehouse Management ‣ Warehouses,
Locations, Routes, Rules, Operations Types and Putaway Rules; Inventory ‣ Configuration ‣
Settings; Inventory ‣ Overview; Inventory ‣ Products ‣ Products; Inventory ‣ Reporting ‣
Stock; Inventory ‣ Reporting ‣ Moves History.

## Verify

```python
print(warehouse.read(['reception_steps', 'delivery_steps']))
print(env['stock.quant'].search_read([('product_id', '=', product.id), ('location_id.usage', '=', 'internal')], ['location_id', 'quantity']))
print(env['stock.warehouse.orderpoint'].search_read([('product_id', '=', product.id)], ['warehouse_id', 'product_min_qty', 'product_max_qty', 'trigger']))
```

Quantities are in the expected locations, the rule is there, and the warehouse has the
steps asked for. For a batch, `batch.state` and its transfers are `done`; for a scrap,
the stock fell by the scrapped quantity.

## Pitfalls

- Writing `quantity` on a quant skips the move and the valuation: always go through
  `inventory_mode` and `action_apply_inventory()`.
- Changing warehouse steps with open transfers leaves them on the old routes.
- A reordering rule without a route that can supply the product orders nothing.
- `button_validate`, `action_done` and `action_validate` can return a wizard instead of
  finishing: never assume the transfer, batch or scrap is done.
- Scrapping more than the location holds opens a warning wizard; forcing it leaves the
  stock negative.
- Batch transfers in 16.0 to 19.0 need a module install; in 20.0 only the setting.
