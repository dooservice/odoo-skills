# sale_margin — Margins in Sales Orders

Depends on: sale_management.

## `sale.order` (extends)

- `margin` Monetary “Margin” (store, compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (store, compute=_compute_margin)

## `sale.order.line` (extends)

- `margin` Float “Margin” (store, compute=_compute_margin)
- `margin_percent` Float “Margin (%)” (store, compute=_compute_margin)
- `purchase_price` Float “Cost” (store, compute=_compute_purchase_price)

## `sale.report` (extends)

- `margin` Float “Margin”
