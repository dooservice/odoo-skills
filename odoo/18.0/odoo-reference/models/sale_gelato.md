# sale_gelato — Gelato

Depends on: sale_management, delivery.

## `delivery.carrier` (extends)

- `delivery_type` Selection
- `gelato_shipping_service_type` Selection “Gelato Shipping Service Type” (required)

Public methods: `available_carriers`, `gelato_rate_shipment`

## `product.document` (extends)

- `is_gelato` Boolean (readonly)

## `product.product` (extends)

- `gelato_product_uid` Char (readonly)

## `product.template` (extends)

- `gelato_template_ref` Char “Gelato Template Reference”
- `gelato_product_uid` Char “Gelato Product UID” (readonly, compute=_compute_gelato_product_uid)
- `gelato_image_ids` One2many → `product.document` “Gelato Print Images” (readonly)
- `gelato_missing_images` Boolean “Missing Print Images” (compute=_compute_gelato_missing_images)

Public methods: `action_sync_gelato_template_info`

Extension points: `_create_attributes_from_gelato_info`, `_create_print_images_from_gelato_info`, `_get_product_document_domain`, `_get_related_fields_variant_template`

## `res.company` (extends)

- `gelato_api_key` Char “Gelato API Key”
- `gelato_webhook_secret` Char “Gelato Webhook Secret”

## `res.partner` (extends)


## `sale.order` (extends)


Public methods: `action_confirm`, `action_open_delivery_wizard`

Extension points: `_create_order_on_gelato`

## `sale.order.line` (extends)


Public methods: `create`, `write`

## `res.config.settings` (extends)

- `module_sale_gelato` Boolean “Gelato”
- `gelato_api_key` Char (related=company_id.gelato_api_key)
- `gelato_webhook_secret` Char (related=company_id.gelato_webhook_secret)
