# purchase_repair — Purchase Repair

Depends on: repair, purchase_stock.

## `purchase.order` (extends)

- `repair_count` Integer “Count of source repairs” (compute=_compute_repair_count)

Public methods: `action_view_repair_orders`

Extension points: `_get_repair_orders`

## `repair.order` (extends)

- `purchase_count` Integer “Count of generated POs” (compute=_compute_purchase_count)

Public methods: `action_view_purchase_orders`

Extension points: `_get_purchase_orders`
