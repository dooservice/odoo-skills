# purchase_requisition_stock — Purchase Requisition Stock

Depends on: purchase_requisition, purchase_stock.

## `purchase.order` (extends)


## `purchase.requisition` (extends)

- `warehouse_id` Many2one → `stock.warehouse` “Warehouse”
- `picking_type_id` Many2one → `stock.picking.type` (required)

## `purchase.requisition.line` (extends)

- `move_dest_id` Many2one → `stock.move`

Extension points: `_prepare_purchase_order_line`

## `stock.rule` (extends)


Extension points: `_get_supplier_requisition`, `_prepare_purchase_order`

## `stock.move` (extends)

- `requisition_line_ids` One2many → `purchase.requisition.line`

Extension points: `_get_upstream_documents_and_responsibles`
