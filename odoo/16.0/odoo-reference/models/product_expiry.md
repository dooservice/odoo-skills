# product_expiry — Products Expiration Date

Depends on: stock.

## `product.product` (extends)


Public methods: `action_open_quants`

## `product.template` (extends)

- `use_expiration_date` Boolean “Use Expiration Date”
- `expiration_time` Integer “Expiration Date”
- `use_time` Integer “Best Before Date”
- `removal_time` Integer “Removal Date”
- `alert_time` Integer “Alert Date”

## `stock.lot` (extends)

- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)
- `expiration_date` Datetime “Expiration Date” (store, compute=_compute_expiration_date)
- `use_date` Datetime “Best before Date” (store, compute=_compute_dates)
- `removal_date` Datetime “Removal Date” (store, compute=_compute_dates)
- `alert_date` Datetime “Alert Date” (store, compute=_compute_dates)
- `product_expiry_alert` Boolean (compute=_compute_product_expiry_alert)
- `product_expiry_reminded` Boolean “Expiry has been reminded”

## `procurement.group` (extends)


## `res.config.settings` (extends)

- `group_expiry_date_on_delivery_slip` Boolean “Display Expiration Dates on Delivery Slips”

## `stock.move` (extends)

- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)

## `stock.move.line` (extends)

- `expiration_date` Datetime “Expiration Date” (store, compute=_compute_expiration_date)
- `is_expired` Boolean (related=lot_id.product_expiry_alert)
- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)

Extension points: `_get_value_production_lot`

## `stock.picking` (extends)


Extension points: `_action_generate_expired_wizard`, `_check_expired_lots`

## `stock.quant` (extends)

- `removal_date` Datetime (store, related=lot_id.removal_date)
- `use_expiration_date` Boolean (readonly, related=product_id.use_expiration_date)

Extension points: `_get_inventory_fields_create`, `_get_inventory_fields_write`, `_get_removal_strategy_order`

## `expiry.picking.confirmation` (defines)

Confirm Expiry

- `lot_ids` Many2many → `stock.lot` (required, readonly)
- `picking_ids` Many2many → `stock.picking` (readonly)
- `description` Char “Description” (compute=_compute_descriptive_fields)
- `show_lots` Boolean “Show Lots” (compute=_compute_descriptive_fields)

Public methods: `process`, `process_no_expired`
