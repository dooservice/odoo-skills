# website_sale_collect — Click & Collect

Depends on: base_geolocalize, payment_custom, website_sale_stock.

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `warehouse_ids` Many2many → `stock.warehouse` “Stores”

Public methods: `create`, `in_store_rate_shipment`, `write`

Extension points: `_check_in_store_dm_has_warehouses_when_published`, `_check_warehouses_have_same_company`, `_get_delivery_estimate_supported_types`, `_get_in_store_default_vals`, `_get_pickup_locations`

## `payment.method` (extends)


Extension points: `_get_pay_on_delivery_method_codes`

## `payment.provider` (extends)

- `custom_mode` Selection

Public methods: `copy_data`

Extension points: `_get_default_payment_method_codes`, `_get_pay_on_delivery_provider_codes`

## `payment.transaction` (extends)


Extension points: `_get_status_message`

## `product.template` (extends)


Extension points: `_get_additional_combination_info`

## `res.config.settings` (extends)


Public methods: `action_view_in_store_delivery_methods`

## `sale.order` (extends)

- `delivery_type` Selection (related=carrier_id.delivery_type)

Public methods: `set_pickup_location`

Extension points: `_get_insufficient_stock_data`, `_get_preferred_delivery_method`, `_prepare_in_store_default_location_data`

## `sale.order.line` (extends)


Extension points: `_get_shop_warning_stock`

## `stock.warehouse` (extends)

- `opening_hours` Many2one → `resource.calendar` “Opening Hours”

Extension points: `_get_exceptional_closing_dates`, `_get_pickup_next_open_date`, `_prepare_pickup_availability_data`, `_prepare_pickup_location_data`

## `website` (extends)

- `in_store_dm_id` Many2one → `delivery.carrier` “In-store Delivery Method” (compute=_compute_in_store_dm_id)

Extension points: `_create_cart`, `_get_max_in_store_product_available_qty`, `_get_product_available_qty`
