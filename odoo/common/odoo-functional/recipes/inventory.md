# Inventory: warehouses, routes, locations and stock

A warehouse (`stock.warehouse`) brings its own locations, operation types (receipts,
deliveries, internal) and routes. Stock lives in quants (`stock.quant`: product, location,
lot, quantity) and only changes through moves: receipts, deliveries, and inventory
adjustments. Stock that already moved is history; fix it with a new adjustment or a
return, never by editing quants or moves.

## Read first

```python
company = env.company
env['stock.warehouse'].search_read([('company_id', '=', company.id)], ['name', 'code', 'reception_steps', 'delivery_steps', 'lot_stock_id'])
env['stock.location'].search_read([('company_id', '=', company.id), ('usage', '=', 'internal')], ['complete_name', 'active'])
env['stock.quant'].search_read([('product_id', '=', product.id), ('location_id.usage', '=', 'internal')], ['location_id', 'lot_id', 'quantity', 'reserved_quantity'])
env['stock.warehouse.orderpoint'].search_read([('product_id', '=', product.id)], ['warehouse_id', 'location_id', 'product_min_qty', 'product_max_qty', 'trigger'])
```

## Settings

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
- A second warehouse in a company turns on multi-warehouse (and multi-locations) by itself.

## A warehouse and its steps

```python
warehouse = env['stock.warehouse'].create({'name': 'Monterrey', 'code': 'MTY', 'company_id': company.id})
warehouse.write({'reception_steps': 'two_steps', 'delivery_steps': 'pick_ship'})
env.cr.commit()
```

- `code` prefixes the warehouse's locations and transfer numbers (`MTY/IN/00001`); at
  most 5 characters up to 19.0.
- `reception_steps`: `one_step`, `two_steps` (input, then stock), `three_steps` (input,
  quality, stock).
- `delivery_steps`: `ship_only`, `pick_ship` (pick to output, then deliver),
  `pick_pack_ship` (pick, pack, deliver).
- Changing steps reconfigures the warehouse's routes, rules and operation types. Ask
  the user to validate or cancel open receipts and deliveries of that warehouse first.

## Locations

```python
env['stock.location'].create({'name': 'Shelf A', 'location_id': warehouse.lot_stock_id.id, 'usage': 'internal'})
env.cr.commit()
```

`usage`: `internal` (stock you own), `view` (a folder, holds no stock), `supplier`,
`customer`, `inventory` (adjustment counterpart), `production`, `transit`. Archive a
location only when it has no stock.

## Stock products

| | 16.0, 17.0 | 18.0, 19.0 | 20.0 |
|---|---|---|---|
| counted in stock | `detailed_type='product'` | `type='consu'`, `is_storable=True` | same, `is_storable` now in `product` |
| tracking | `tracking`: `serial`, `lot`, `none` | same | `tracking`: `lot`, `serial` or empty; `store_by` |

In 20.0 `store_by` (`untracked`, `quantity`, `lot`, `serial`) is the form's single choice
and writes `is_storable` and `tracking` for you. Turning a product with stock into a
non-stored one, or changing its tracking, needs the user's yes: quantities and lots
already recorded do not follow.

## Initial quantities

An inventory adjustment, never a write of `quantity`:

```python
quant = env['stock.quant'].with_context(inventory_mode=True).create({
    'product_id': product.id,
    'location_id': warehouse.lot_stock_id.id,
    'inventory_quantity': 40,
})
quant.action_apply_inventory()
env.cr.commit()
```

- `inventory_mode` only works for a user in the stock user group: run as that user
  (`env(user=user.id)`), not as the superuser.
- Tracked products need `lot_id` (an existing or new `stock.lot`, with `name`,
  `product_id` and `company_id`). One quant per serial number, quantity 1.
- If `action_apply_inventory()` returns an action instead of applying (quants changed
  meanwhile, conflicts), stop and show it to the user.
- With automated valuation each adjustment posts a journal entry: say so.

## Reordering rules

```python
env['stock.warehouse.orderpoint'].create({
    'product_id': product.id, 'warehouse_id': warehouse.id, 'location_id': warehouse.lot_stock_id.id,
    'product_min_qty': 10, 'product_max_qty': 50, 'trigger': 'auto',
})
env.cr.commit()
```

- `trigger`: `auto` (the scheduler creates purchase or manufacturing orders) or `manual`
  (shown in Replenishment for someone to order).
- The product needs a route that can supply it: Buy with a vendor, or Manufacture with a
  bill of materials. Without one the rule does nothing.
- `qty_multiple` (order in multiples) exists up to 18.0; from 19.0 rounding comes from
  `replenishment_uom_id`.
