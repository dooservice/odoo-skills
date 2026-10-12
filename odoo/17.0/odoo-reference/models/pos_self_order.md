# pos_self_order — POS Self Order

Depends on: pos_restaurant, http_routing.

## `ir.http` (extends)


Public methods: `get_nearest_lang`

Extension points: `_get_translation_frontend_modules_name`

## `pos.config` (extends)

- `status` Selection “Status” (compute=_compute_status)
- `self_ordering_url` Char (compute=_compute_self_ordering_url)
- `self_ordering_takeaway` Boolean “Takeaway”
- `self_ordering_alternative_fp_id` Many2one → `account.fiscal.position` “Alternative Fiscal Position”
- `self_ordering_mode` Selection “Self Ordering Mode” (required)
- `self_ordering_service_mode` Selection “Service” (required)
- `self_ordering_default_language_id` Many2one → `res.lang` “Default Language”
- `self_ordering_available_language_ids` Many2many → `res.lang` “Available Languages”
- `self_ordering_image_home_ids` Many2many → `ir.attachment` “Add images”
- `self_ordering_default_user_id` Many2one → `res.users` “Default User”
- `self_ordering_pay_after` Selection “Pay After:” (required)
- `self_ordering_image_brand` Image “Self Order Kiosk Image Brand”
- `self_ordering_image_brand_name` Char “Self Order Kiosk Image Brand Name”
- `access_token` Char “Security Token” (required, readonly)

Public methods: `action_close_kiosk_session`, `action_open_kiosk`, `action_open_wizard`, `create`, `preview_self_order_app`, `write`

Extension points: `_check_default_user`, `_get_access_token`, `_get_allowed_payment_methods`, `_get_available_categories`, `_get_available_products`, `_get_combos_data`, `_get_kitchen_printer`, `_get_qr_code_data`, `_get_self_order_custom_links`, `_get_self_order_route`, `_get_self_order_url`, `_get_self_ordering_attachment`, `_get_self_ordering_data`, `_get_self_ordering_image`, `_get_self_ordering_payment_methods_data`

## `pos.order.line` (extends)

- `combo_parent_id` Many2one → `pos.order.line` “Combo Parent”
- `combo_line_ids` One2many → `pos.order.line` “Combo Lines”
- `combo_id` Many2one → `pos.combo` “Combo line reference”

Public methods: `write`

## `pos.order` (extends)

- `table_stand_number` Char “Table Stand Number”
- `take_away` Boolean “Take Away”

Public methods: `create_from_ui`, `export_for_ui_table_draft`, `get_standalone_self_order`, `remove_from_ui`

Extension points: `_get_shared_orders`

## `pos.payment.method` (extends)


## `restaurant.table` (extends)

- `identifier` Char “Security Token” (required)

Extension points: `_get_identifier`, `_get_self_order_data`

## `pos_self_order.custom_link` (defines)

Custom links that the restaurant can configure to be displayed on the self order screen

- `name` Char “Label” (required)
- `url` Char “URL” (required)
- `pos_config_ids` Many2many → `pos.config` “Points of Sale”
- `style` Selection “Style” (required)
- `link_html` Html “Preview” (readonly, store, compute=_compute_link_html)
- `sequence` Integer “Sequence”

## `pos.session` (extends)


Public methods: `create`

Extension points: `_create_pos_self_sessions_sequence`

## `product.template` (extends)

- `self_order_available` Boolean “Available in Self Order”
- `description_self_order` Html “Product Description for Self Order”

Public methods: `write`

## `product.product` (extends)


Public methods: `write`

Extension points: `_get_attributes`, `_get_name`, `_get_price_info`, `_get_price_unit_after_fp`, `_get_product_for_ui`, `_get_self_order_data`

## `res.config.settings` (extends)

- `pos_self_ordering_takeaway` Boolean (related=pos_config_id.self_ordering_takeaway)
- `pos_self_ordering_service_mode` Selection (required, related=pos_config_id.self_ordering_service_mode)
- `pos_self_ordering_mode` Selection (required, related=pos_config_id.self_ordering_mode)
- `pos_self_ordering_alternative_fp_id` Many2one (related=pos_config_id.self_ordering_alternative_fp_id)
- `pos_self_ordering_default_language_id` Many2one (related=pos_config_id.self_ordering_default_language_id)
- `pos_self_ordering_available_language_ids` Many2many (related=pos_config_id.self_ordering_available_language_ids)
- `pos_self_ordering_image_home_ids` Many2many (related=pos_config_id.self_ordering_image_home_ids)
- `pos_self_ordering_image_brand` Image (related=pos_config_id.self_ordering_image_brand)
- `pos_self_ordering_image_brand_name` Char (related=pos_config_id.self_ordering_image_brand_name)
- `pos_self_ordering_pay_after` Selection (required, related=pos_config_id.self_ordering_pay_after)
- `pos_self_ordering_default_user_id` Many2one (related=pos_config_id.self_ordering_default_user_id)

Public methods: `custom_link_action`, `generate_qr_codes_page`, `generate_qr_codes_zip`, `preview_self_order_app`, `update_access_tokens`
