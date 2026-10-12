# sale_purchase_stock — MTO Sale <-> Purchase

Depends on: sale_stock, purchase_stock, sale_purchase.

## `purchase.order` (extends)


Extension points: `_get_sale_orders`

## `purchase.order.line` (extends)


Extension points: `_get_sale_order_line_product`, `_prepare_purchase_order_line_from_procurement`, `_prepare_stock_moves`

## `sale.order` (extends)


Extension points: `_get_purchase_orders`

## `stock.move` (extends)


Extension points: `_get_description`

## `stock.rule` (extends)
