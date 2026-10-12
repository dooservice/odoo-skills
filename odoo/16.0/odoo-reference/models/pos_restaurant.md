# pos_restaurant — Restaurant

Depends on: point_of_sale.

## `pos.config` (extends)

- `iface_splitbill` Boolean “Bill Splitting”
- `iface_printbill` Boolean “Bill Printing”
- `iface_orderline_notes` Boolean “Internal Notes”
- `floor_ids` One2many → `restaurant.floor` “Restaurant Floors”
- `printer_ids` Many2many → `restaurant.printer` “Order Printers”
- `is_table_management` Boolean “Floors & Tables”
- `is_order_printer` Boolean “Order Printer”
- `set_tip_after_payment` Boolean “Set Tip After Payment”
- `module_pos_restaurant` Boolean

Public methods: `add_cash_payment_method`, `get_tables_order_count`, `write`

Extension points: `_get_forbidden_change_fields`

## `pos.order.line` (extends)

- `note` Char “Internal Note added by the waiter.”
- `uuid` Char “Uuid” (readonly)
- `mp_skip` Boolean “Skip line when sending ticket to kitchen printers.”

## `pos.order` (extends)

- `table_id` Many2one → `restaurant.table` “Table”
- `customer_count` Integer “Guests”
- `multiprint_resume` Char “Multiprint Resume”

Public methods: `get_table_draft_orders`, `remove_from_ui`, `set_no_tip`, `set_tip`

Extension points: `_get_domain_for_draft_orders`, `_get_fields_for_draft_order`, `_get_fields_for_order_line`, `_get_fields_for_payment_lines`, `_get_order_lines`, `_get_pack_lot_lines`, `_get_payment_lines`, `_get_payments_lines_list`, `_prepare_order_line`

## `pos.payment` (extends)


## `restaurant.floor` (defines)

Restaurant Floor

- `name` Char “Floor Name” (required)
- `pos_config_id` Many2one → `pos.config` “Point of Sale”
- `background_image` Binary “Background Image”
- `background_color` Char “Background Color”
- `table_ids` One2many → `restaurant.table` “Tables”
- `sequence` Integer “Sequence”
- `active` Boolean

Public methods: `write`

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

Public methods: `create_from_ui`

## `restaurant.printer` (defines)

Restaurant Printer

- `name` Char “Printer Name” (required)
- `printer_type` Selection “Printer Type”
- `proxy_ip` Char “Proxy IP Address”
- `product_categories_ids` Many2many → `pos.category` “Printed Product Categories”

## `pos.session` (extends)


Extension points: `_get_pos_ui_restaurant_floor`, `_get_pos_ui_restaurant_printer`

## `res.config.settings` (extends)

- `pos_floor_ids` One2many (related=pos_config_id.floor_ids)
- `pos_iface_orderline_notes` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_iface_printbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_iface_splitbill` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_is_order_printer` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_is_table_management` Boolean (store, compute=_compute_pos_module_pos_restaurant)
- `pos_printer_ids` Many2many (related=pos_config_id.printer_ids)
- `pos_set_tip_after_payment` Boolean (store, compute=_compute_pos_set_tip_after_payment)

Extension points: `_get_floors_domain`
