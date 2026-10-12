# pos_restaurant — Restaurant

Depends on: point_of_sale.

## `pos.category` (extends)

- `course_id` Many2one → `pos.course` “Course” (index)

## `pos.config` (extends)

- `floor_ids` Many2many → `restaurant.floor` “Restaurant Floors”
- `default_screen` Selection “Default Screen”
- `use_course_allocation` Boolean “Enable Course Allocation”
- `use_show_items_on_course_ticket` Boolean “Show Items on Fired Course Ticket”
- `floor_plan_settings` Json “Floor Plan Settings”
- `floor_plan` Json “Floor Plan” (compute=_compute_floor_plan)

Public methods: `create`, `get_floor_plan`, `load_onboarding_bar_scenario`, `load_onboarding_restaurant_scenario`, `save_floor_plan`, `write`

Extension points: `_get_default_demo_data_xml_id`, `_get_demo_data_loader_methods`, `_get_forbidden_change_fields`

## `pos.course` (defines)

POS Course

Inherits: `pos.load.mixin`

- `name` Char “Course Name” (required)
- `sequence` Integer “Sequence”
- `category_ids` One2many → `pos.category` “Pos Category”

## `pos.order` (extends)

- `table_id` Many2one → `restaurant.table` “Table” (readonly)
- `customer_count` Integer “Guests” (readonly)
- `course_ids` One2many → `restaurant.order.course` “Courses”
- `duration` Char “Duration” (compute=_compute_duration)

Public methods: `read_pos_data`

Extension points: `_get_open_order`

## `pos.order.line` (extends)

- `course_id` Many2one → `restaurant.order.course` “Course Ref”

## `pos.preset` (extends)

- `use_guest` Boolean “Guest”

## `restaurant.floor` (defines)

Restaurant Floor

Inherits: `pos.load.mixin`

- `name` Char “Floor Name” (required)
- `pos_config_ids` Many2many → `pos.config` “Point of Sales”
- `table_ids` One2many → `restaurant.table` “Tables”
- `sequence` Integer “Sequence”
- `active` Boolean
- `floor_plan_layout` Json “Floor Plan Layout”

Public methods: `add_floor_plan_image`, `deactivate_floor`, `write`

## `restaurant.table` (defines)

Restaurant Table

Inherits: `pos.load.mixin`

- `floor_id` Many2one → `restaurant.floor` “Floor”
- `table_number` Integer “Table Number” (required)
- `seats` Integer “Seats”
- `parent_id` Many2one → `restaurant.table` “Parent Table”
- `parent_side` Selection “Parent Side”
- `active` Boolean “Active”
- `floor_plan_layout` Json “Floor Plan Layout”

Public methods: `are_orders_still_in_draft`, `set_parent_id`

## `pos.session` (extends)


## `product.template` (extends)


Public methods: `default_get`

## `res.config.settings` (extends)

- `pos_floor_ids` Many2many (related=pos_config_id.floor_ids)
- `pos_default_screen` Selection (related=pos_config_id.default_screen)
- `pos_use_course_allocation` Boolean (related=pos_config_id.use_course_allocation)
- `pos_use_show_items_on_course_ticket` Boolean (related=pos_config_id.use_show_items_on_course_ticket)

## `restaurant.order.course` (defines)

POS Restaurant Order Course

Inherits: `pos.load.mixin`

- `name` Char “Course Name” (readonly)
- `course_id` Many2one → `pos.course` “Course” (readonly)
- `fired` Boolean “Fired”
- `fired_date` Datetime “Fired Date”
- `uuid` Char “Uuid” (readonly)
- `index` Integer “Course index”
- `order_id` Many2one → `pos.order` “Order Ref” (required, index)
- `line_ids` One2many → `pos.order.line` “Order Lines” (readonly)

Public methods: `create`, `write`

## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`
