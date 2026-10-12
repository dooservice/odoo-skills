# purchase_requisition_stock — Purchase Requisition Stock

Depends on: purchase_requisition, purchase_stock.

## `purchase.order` (extends)

- `on_time_rate_perc` Float “OTD” (compute=_compute_on_time_rate_perc)

## `purchase.order.line` (extends)

- `on_time_rate_perc` Float “OTD” (related=order_id.on_time_rate_perc)

## `purchase.requisition` (extends)

- `warehouse_id` Many2one → `stock.warehouse` “Warehouse”
- `picking_type_id` Many2one → `stock.picking.type` (required)

## `purchase.requisition.line` (extends)

- `move_dest_id` Many2one → `stock.move`

Extension points: `_prepare_purchase_order_line`

## `stock.rule` (extends)


Extension points: `_prepare_purchase_order`

## `stock.move` (extends)

- `requisition_line_ids` One2many → `purchase.requisition.line`

Extension points: `_get_upstream_documents_and_responsibles`

## `stock.warehouse.orderpoint` (extends)


## `purchase.requisition.create.alternative` (extends)


Extension points: `_get_alternative_line_value`, `_get_alternative_values`
