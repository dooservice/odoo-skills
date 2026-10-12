# product_expiry — Products Expiration Date

Depends on: stock.

## `product.product` (extends)

- `free_qty` Float
- `virtual_available` Float

## `product.template` (extends)

- `use_expiration_date` Boolean “Use Expiration Date”
- `expiration_time` Integer “Expiration Date”
- `use_time` Integer “Best Before Date”
- `removal_time` Integer “Removal Date”
- `alert_time` Integer “Alert Date”

Public methods: `write`

## `stock.lot` (extends)

- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)
- `expiration_date` Datetime “Expiration Date” (store, compute=_compute_expiration_date)
- `use_date` Datetime “Best before Date” (store, compute=_compute_dates)
- `removal_date` Datetime “Removal Date” (store, compute=_compute_dates)
- `alert_date` Datetime “Alert Date” (store, compute=_compute_dates)
- `product_expiry_alert` Boolean (compute=_compute_product_expiry_alert)
- `product_expiry_reminded` Boolean “Expiry has been reminded”

## `res.config.settings` (extends)

- `group_expiry_date_on_delivery_slip` Boolean “Display Expiration Dates on Delivery Slips”

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `stock.move` (extends)

- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)

Public methods: `action_generate_lot_line_vals`

Extension points: `_get_available_quantity`, `_get_formating_options`

## `stock.move.line` (extends)

- `expiration_date` Datetime “Expiration Date” (store, compute=_compute_expiration_date)
- `removal_date` Datetime “Removal Date” (store, compute=_compute_removal_date)
- `is_expired` Boolean (related=lot_id.product_expiry_alert)
- `use_expiration_date` Boolean “Use Expiration Date” (related=product_id.use_expiration_date)

Extension points: `_prepare_new_lot_vals`

## `stock.picking` (extends)


Extension points: `_action_generate_expired_wizard`, `_check_expired_lots`

## `stock.quant` (extends)

- `expiration_date` Datetime (store, related=lot_id.expiration_date)
- `removal_date` Datetime (store, related=lot_id.removal_date)
- `use_expiration_date` Boolean (related=product_id.use_expiration_date)
- `available_quantity` Float

Extension points: `_get_gs1_barcode`, `_get_removal_strategy_order`

## `stock.rule` (extends)


Extension points: `_get_scheduler_tasks_to_do`

## `report.stock.quantity` (extends)


Extension points: `_get_product_qty_col`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_expired_quant_domain`, `_get_quant_domain`, `_get_report_header`, `_prepare_report_line`

## `stock.traceability.report` (extends)


## `expiry.picking.confirmation` (defines)

Confirm Expiry

- `lot_ids` Many2many → `stock.lot` (required, readonly)
- `picking_ids` Many2many → `stock.picking` (readonly)
- `description` Char “Description” (compute=_compute_descriptive_fields)
- `show_lots` Boolean “Show Lots” (compute=_compute_descriptive_fields)

Public methods: `process`, `process_no_expired`

## `lot.label.layout` (extends)


Extension points: `_prepare_label_values`, `_prepare_lot_gs1_barcode_extra_data`
