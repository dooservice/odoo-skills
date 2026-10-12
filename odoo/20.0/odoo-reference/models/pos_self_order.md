# pos_self_order — POS Self Order

Depends on: pos_restaurant, http_routing, link_tracker, google_address_autocomplete, base_geolocalize.

## `ir.http` (extends)


Public methods: `get_nearest_lang`

Extension points: `_get_translation_frontend_modules_name`

## `ir.ui.view` (extends)


Extension points: `_get_xml_ids_to_load`

## `mail.template` (extends)

Inherits: `pos.load.mixin`


## `pos.category` (extends)


## `pos.config` (extends)

- `status` Selection “Status” (compute=_compute_status)
- `self_ordering_url` Char (compute=_compute_self_ordering_url)
- `self_ordering_mode` Selection “Self Ordering Mode” (required)
- `self_ordering_service_mode` Selection “Self Ordering Service Mode” (required)
- `self_ordering_default_language_id` Many2one → `res.lang` “Default Language”
- `self_ordering_available_language_ids` Many2many → `res.lang` “Available Languages”
- `self_ordering_image_home_ids` Many2many → `ir.attachment` “Add Media”
- `self_ordering_image_background_ids` Many2many → `ir.attachment` “Set background image”
- `self_ordering_default_user_id` Many2one → `res.users` “Default User”
- `self_ordering_pay_after` Selection “Pay After:” (required)
- `self_ordering_image_brand` Image “Self Order Kiosk Image Brand”
- `self_ordering_image_brand_name` Char “Self Order Kiosk Image Brand Name”
- `has_paper` Boolean “Has paper”
- `self_ordering_primary_color` Char “Color”

Public methods: `action_close_kiosk_session`, `action_open_wizard`, `close_ui`, `create`, `get_dynamic_qr_url`, `get_kiosk_url`, `get_pos_qr_order_data`, `has_valid_self_payment_method`, `load_onboarding_kiosk_scenario`, `load_self_data`, `notify_session_state_changed`, `preview_self_order_app`, `write`

Extension points: `_check_default_user`, `_get_qr_code_data`, `_get_self_order_route`, `_get_self_order_url`, `_prepare_self_order_custom_btn`, `_prepare_self_order_splash_screen`

## `pos.load.mixin` (extends)


## `pos.order` (extends)

- `table_stand_number` Char “Table Stand Number”
- `self_ordering_table_id` Many2one → `restaurant.table` “Table reference” (readonly)
- `source` Selection

Public methods: `action_pos_order_cancel`, `action_send_self_order_receipt`, `cancel_order_from_pos`, `recompute_prices`, `remove_from_ui`, `sync_from_ui`

Extension points: `_check_combo_lines`, `_check_pos_order`, `_check_pos_order_lines`, `_check_pos_order_payment`, `_get_self_order_floating_name`

## `pos.order.line` (extends)

- `combo_id` Many2one → `product.combo` “Combo Reference”

Public methods: `create`, `write`

## `pos.payment.method` (extends)


## `pos.prep.line` (extends)


## `pos.prep.order` (extends)


## `pos.preset` (extends)

- `available_in_self` Boolean “Available in self”
- `service_at` Selection “Service at” (required)
- `delivery_from_address` Char “Sender address” (store, compute=_compute_delivery_from_address)
- `delivery_from_street` Char “Street”
- `delivery_from_city` Char “City”
- `delivery_from_zip` Char “Zip”
- `delivery_from_country_id` Many2one → `res.country` “Country”
- `delivery_from_state_id` Many2one → `res.country.state` “State”
- `delivery_from_latitude` Float “Latitude”
- `delivery_from_longitude` Float “Longitude”
- `delivery_max_distance_km` Float “Max radius”
- `delivery_distance_unit` Selection “Distance unit”
- `delivery_product_id` Many2one → `product.product` “Delivery Product”
- `delivery_product_price` Float “Fixed Price”
- `free_delivery_min_amount` Float “Free if order amount is above”
- `mail_template_id` Many2one → `mail.template` “Email Confirmation”

Public methods: `create`, `default_get`, `write`

Extension points: `_get_delivery_from_address_parts`

## `restaurant.table` (extends)

- `identifier` Char “Security Token” (required)

Extension points: `_get_identifier`

## `restaurant.floor` (extends)


## `pos_self_order.custom_link` (defines)

Custom links that the restaurant can configure to be displayed on the self order screen

Inherits: `pos.load.mixin`

- `name` Char “Label” (required)
- `url` Char “URL” (required)
- `pos_config_ids` Many2many → `pos.config` “Points of Sale”
- `style` Selection “Style” (required)
- `link_html` Html “Preview” (readonly, store, compute=_compute_link_html)
- `sequence` Integer “Sequence”

## `pos.session` (extends)


Public methods: `close_session_from_ui`

## `pos.snooze` (extends)

- `type` Selection

## `product.product` (extends)


Public methods: `write`

## `product.tag` (extends)


## `product.template` (extends)

- `self_order_available` Boolean “Available in Self Order”
- `self_order_visible` Boolean (compute=_compute_self_order_visible)

Public methods: `write`

## `res.config.settings` (extends)

- `pos_self_ordering_service_mode` Selection (required, related=pos_config_id.self_ordering_service_mode)
- `pos_self_ordering_mode` Selection (required, related=pos_config_id.self_ordering_mode)
- `pos_self_ordering_default_language_id` Many2one (related=pos_config_id.self_ordering_default_language_id)
- `pos_self_ordering_available_language_ids` Many2many (related=pos_config_id.self_ordering_available_language_ids)
- `pos_self_ordering_image_home_ids` Many2many (related=pos_config_id.self_ordering_image_home_ids)
- `pos_self_ordering_image_background_ids` Many2many (related=pos_config_id.self_ordering_image_background_ids)
- `pos_self_ordering_image_brand` Image (related=pos_config_id.self_ordering_image_brand)
- `pos_self_ordering_image_brand_name` Char (related=pos_config_id.self_ordering_image_brand_name)
- `pos_self_ordering_pay_after` Selection (required, related=pos_config_id.self_ordering_pay_after)
- `pos_self_ordering_default_user_id` Many2one (related=pos_config_id.self_ordering_default_user_id)
- `pos_self_ordering_primary_color` Char (related=pos_config_id.self_ordering_primary_color)

Public methods: `custom_link_action`, `generate_qr_codes_page`, `generate_qr_codes_zip`, `get_pos_qr_stands`, `pos_close_ui`, `preview_self_order_app`

## `res.country` (extends)

Inherits: `pos.load.mixin`


## `res.partner` (extends)


## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`
