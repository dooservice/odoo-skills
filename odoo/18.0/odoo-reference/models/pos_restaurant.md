# pos_restaurant — Restaurant

Depends on: point_of_sale.

## `account.fiscal.position` (extends)


## `pos.config` (extends)

- `iface_splitbill` Boolean “Bill Splitting”
- `iface_printbill` Boolean “Bill Printing”
- `floor_ids` Many2many → `restaurant.floor` “Restaurant Floors”
- `set_tip_after_payment` Boolean “Set Tip After Payment”
- `module_pos_restaurant_appointment` Boolean “Table Booking”
- `takeaway` Boolean “Takeaway”
- `takeaway_fp_id` Many2one → `account.fiscal.position` “Alternative Fiscal Position”

Public methods: `create`, `load_onboarding_bar_scenario`, `load_onboarding_restaurant_scenario`, `write`

Extension points: `_get_forbidden_change_fields`

## `pos.order` (extends)

- `table_id` Many2one → `restaurant.table` “Table” (readonly)
- `customer_count` Integer “Guests” (readonly)
- `takeaway` Boolean “Take Away”

Public methods: `action_pos_order_cancel`, `remove_from_ui`, `send_table_count_notification`, `sync_from_ui`

Extension points: `_get_open_order`

## `pos.payment` (extends)


## `restaurant.floor` (defines)

Restaurant Floor

Inherits: `pos.load.mixin`

- `name` Char “Floor Name” (required)
- `pos_config_ids` Many2many → `pos.config` “Point of Sales”
- `background_image` Binary “Background Image”
- `background_color` Char “Background Color”
- `table_ids` One2many → `restaurant.table` “Tables”
- `sequence` Integer “Sequence”
- `active` Boolean
- `floor_background_image` Image “Floor Background Image”

Public methods: `deactivate_floor`, `rename_floor`, `sync_from_ui`, `write`

## `restaurant.table` (defines)

Restaurant Table

Inherits: `pos.load.mixin`

- `floor_id` Many2one → `restaurant.floor` “Floor”
- `table_number` Integer “Table Number” (required)
- `shape` Selection “Shape” (required)
- `position_h` Float “Horizontal Position”
- `position_v` Float “Vertical Position”
- `width` Float “Width”
- `height` Float “Height”
- `seats` Integer “Seats”
- `color` Char “Color”
- `parent_id` Many2one → `restaurant.table` “Parent Table”
- `active` Boolean “Active”

Public methods: `are_orders_still_in_draft`

## `pos.session` (extends)


## `res.config.settings` (extends)

- `pos_floor_ids` Many2many (related=pos_config_id.floor_ids)
- `pos_iface_printbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_iface_splitbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_set_tip_after_payment` Boolean (store, compute=_compute_pos_set_tip_after_payment)
- `pos_module_pos_restaurant_appointment` Boolean (related=pos_config_id.module_pos_restaurant_appointment)
- `pos_takeaway` Boolean (related=pos_config_id.takeaway)
- `pos_takeaway_fp_id` Many2one (related=pos_config_id.takeaway_fp_id)
