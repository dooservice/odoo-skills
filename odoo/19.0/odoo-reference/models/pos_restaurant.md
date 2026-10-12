# pos_restaurant — Restaurant

Depends on: point_of_sale.

## `pos.config` (extends)

- `iface_splitbill` Boolean “Bill Splitting”
- `iface_printbill` Boolean “Bill Printing”
- `floor_ids` Many2many → `restaurant.floor` “Restaurant Floors”
- `set_tip_after_payment` Boolean “Set Tip After Payment”
- `default_screen` Selection “Default Screen”

Public methods: `create`, `load_onboarding_bar_scenario`, `load_onboarding_restaurant_scenario`, `write`

Extension points: `_get_default_demo_data_xml_id`, `_get_demo_data_loader_methods`, `_get_forbidden_change_fields`

## `pos.order` (extends)

- `table_id` Many2one → `restaurant.table` “Table” (readonly)
- `customer_count` Integer “Guests” (readonly)
- `course_ids` One2many → `restaurant.order.course` “Courses”

Public methods: `read_pos_data`

Extension points: `_get_open_order`

## `pos.order.line` (extends)

- `course_id` Many2one → `restaurant.order.course` “Course Ref”

## `pos.payment` (extends)


## `pos.preset` (extends)

- `use_guest` Boolean “Guest”

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

Public methods: `are_orders_still_in_draft`, `set_parent_id`

## `pos.session` (extends)


## `res.config.settings` (extends)

- `pos_floor_ids` Many2many (related=pos_config_id.floor_ids)
- `pos_iface_printbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_iface_splitbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_set_tip_after_payment` Boolean (store, compute=_compute_pos_set_tip_after_payment)
- `pos_default_screen` Selection (related=pos_config_id.default_screen)

## `restaurant.order.course` (defines)

POS Restaurant Order Course

Inherits: `pos.load.mixin`

- `fired` Boolean “Fired”
- `fired_date` Datetime “Fired Date”
- `uuid` Char “Uuid” (readonly)
- `index` Integer “Course index”
- `order_id` Many2one → `pos.order` “Order Ref” (required, index)
- `line_ids` One2many → `pos.order.line` “Order Lines” (readonly)

Public methods: `create`, `write`
