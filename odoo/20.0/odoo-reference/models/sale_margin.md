# sale_margin — Margins in Sales Orders

Depends on: sale_management.

## `sale.order` (extends)

- `margin` Monetary “Margin” (store, compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (store, compute=_compute_margin)

## `sale.order.line` (extends)

- `margin` Float “Margin” (store, compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (store, compute=_compute_margin_percent)
- `purchase_price` Float “Unit Cost” (store, compute=_compute_purchase_price)

Extension points: `_get_discount`, `_get_product_qty`, `_get_subtotal`, `_prepare_template_line_values`

## `sale.order.template.line` (extends)

- `purchase_price` Float “Unit Cost”

Extension points: `_prepare_order_line_values`

## `sale.report` (extends)

- `margin` Monetary “Margin” (readonly)
- `margin_percent` Float “Margin (%)” (readonly)
- `purchase_price` Monetary “Expected Cost” (readonly)
