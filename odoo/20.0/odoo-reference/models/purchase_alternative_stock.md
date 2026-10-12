# purchase_alternative_stock — Purchase Alternative Stock

Depends on: purchase_alternative, purchase_stock.

## `purchase.order` (extends)

- `on_time_rate_perc` Float “OTD” (compute=_compute_on_time_rate_perc)

## `purchase.order.line` (extends)

- `on_time_rate_perc` Float “OTD” (related=order_id.on_time_rate_perc)

## `purchase.alternative.create` (extends)


Extension points: `_get_alternative_line_value`, `_get_alternative_values`
