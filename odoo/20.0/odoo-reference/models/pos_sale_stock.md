# pos_sale_stock — POS - Sales Stock

Depends on: pos_stock, pos_sale.

## `pos.order` (extends)


Public methods: `sync_from_ui`

## `pos.order.line` (extends)


Extension points: `_get_qty_to_move`

## `sale.order` (extends)


## `sale.order.line` (extends)


Extension points: `_get_qty_procurement`, `_get_read_converted_extra_items`, `_prepare_qty_delivered`

## `stock.picking` (extends)


Extension points: `_create_move_from_pos_order_lines`

## `sale.report` (extends)
