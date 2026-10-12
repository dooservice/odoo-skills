# pos_repair — POS - Repair

Depends on: pos_stock, repair.

## `sale.order.line` (extends)

- `is_repair_line` Boolean “Is linked to repair” (compute=_compute_is_repair_line)

## `stock.picking` (extends)


Extension points: `_create_move_from_pos_order_lines`
