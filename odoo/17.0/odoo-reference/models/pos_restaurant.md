# pos_restaurant — Restaurant

Depends on: point_of_sale.

## `pos.config` (extends)

- `iface_splitbill` Boolean “Bill Splitting”
- `iface_printbill` Boolean “Bill Printing”
- `iface_orderline_notes` Boolean “Internal Notes”
- `floor_ids` Many2many → `restaurant.floor` “Restaurant Floors”
- `set_tip_after_payment` Boolean “Set Tip After Payment”
- `module_pos_restaurant` Boolean
- `module_pos_restaurant_appointment` Boolean “Table Booking”

Public methods: `create`, `get_tables_order_count_and_printing_changes`, `post_install_pos_localisation`, `setup_defaults`, `write`

Extension points: `_get_forbidden_change_fields`

## `pos.order.line` (extends)

- `note` Char “Internal Note added by the waiter.”

## `pos.order` (extends)

- `table_id` Many2one → `restaurant.table` “Table” (readonly)
- `customer_count` Integer “Guests” (readonly)

Public methods: `export_for_ui_table_draft`, `remove_from_ui`, `send_table_count_notification`, `set_no_tip`, `set_tip`

## `pos.payment` (extends)


## `restaurant.floor` (defines)

Restaurant Floor

- `name` Char “Floor Name” (required)
- `pos_config_ids` Many2many → `pos.config` “Point of Sales”
- `background_image` Binary “Background Image”
- `background_color` Char “Background Color”
- `table_ids` One2many → `restaurant.table` “Tables”
- `sequence` Integer “Sequence”
- `active` Boolean

Public methods: `create_from_ui`, `deactivate_floor`, `rename_floor`, `write`

## `restaurant.table` (defines)

Restaurant Table

- `name` Char “Table Name” (required)
- `floor_id` Many2one → `restaurant.floor` “Floor”
- `shape` Selection “Shape” (required)
- `position_h` Float “Horizontal Position”
- `position_v` Float “Vertical Position”
- `width` Float “Width”
- `height` Float “Height”
- `seats` Integer “Seats”
- `color` Char “Color”
- `active` Boolean “Active”

Public methods: `are_orders_still_in_draft`

## `pos.session` (extends)


Public methods: `get_onboarding_data`, `get_pos_ui_restaurant_floor`

Extension points: `_get_pos_ui_restaurant_floor`

## `res.config.settings` (extends)

- `pos_floor_ids` Many2many (related=pos_config_id.floor_ids)
- `pos_iface_orderline_notes` Boolean (related=pos_config_id.iface_orderline_notes)
- `pos_iface_printbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_iface_splitbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_set_tip_after_payment` Boolean (store, compute=_compute_pos_set_tip_after_payment)
- `pos_module_pos_restaurant_appointment` Boolean (related=pos_config_id.module_pos_restaurant_appointment)
