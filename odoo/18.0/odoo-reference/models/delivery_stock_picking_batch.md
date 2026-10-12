# delivery_stock_picking_batch — Delivery Stock Picking Batch

Depends on: stock_delivery, stock_picking_batch.

## `stock.picking.type` (extends)

- `batch_group_by_carrier` Boolean “Carrier”
- `batch_max_weight` Integer “Maximum weight”
- `weight_uom_name` Char “Weight unit of measure label” (readonly, compute=_compute_weight_uom_name)

Extension points: `_get_batch_group_by_keys`, `_get_default_weight_uom`

## `stock.picking` (extends)


Extension points: `_get_auto_batch_description`, `_get_possible_batches_domain`, `_get_possible_pickings_domain`

## `stock.picking.batch` (extends)
