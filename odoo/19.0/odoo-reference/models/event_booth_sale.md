# event_booth_sale — Events Booths Sales

Depends on: event_booth, event_sale.

## `account.move` (extends)


## `event.booth` (extends)

- `event_booth_registration_ids` One2many → `event.booth.registration`
- `sale_order_line_registration_ids` Many2many → `sale.order.line` “SO Lines with reservations”
- `sale_order_line_id` Many2one → `sale.order.line` “Final Sale Order Line”
- `sale_order_id` Many2one (readonly, related=sale_order_line_id.order_id)
- `is_paid` Boolean “Is Paid”

Public methods: `action_set_paid`, `action_view_sale_order`

Extension points: `_get_booth_multiline_description`

## `event.booth.category` (extends)

- `product_id` Many2one → `product.product` “Product” (required)
- `price` Float “Price” (store, compute=_compute_price)
- `price_incl` Float “Price incl” (compute=_compute_price_incl)
- `currency_id` Many2one (related=product_id.currency_id)
- `price_reduce` Float “Price Reduce” (compute=_compute_price_reduce)
- `price_reduce_taxinc` Float “Price Reduce Tax inc” (compute=_compute_price_reduce_taxinc)
- `image_1920` Image (store, compute=_compute_image_1920)

Extension points: `_check_service_tracking`

## `event.booth.registration` (defines)

Event Booth Registration

- `sale_order_line_id` Many2one → `sale.order.line` “Sale Order Line” (required, index)
- `event_booth_id` Many2one → `event.booth` “Booth” (required, index)
- `partner_id` Many2one → `res.partner` (store, related=sale_order_line_id.order_partner_id)
- `contact_name` Char “Contact Name” (store, compute=_compute_contact_name)
- `contact_email` Char “Contact Email” (store, compute=_compute_contact_email)
- `contact_phone` Char “Contact Phone” (store, compute=_compute_contact_phone)

Public methods: `action_confirm`

Extension points: `_get_fields_for_booth_confirmation`

## `event.type.booth` (extends)

- `product_id` Many2one (related=booth_category_id.product_id)
- `price` Float (store, related=booth_category_id.price)
- `currency_id` Many2one (related=booth_category_id.currency_id)

Extension points: `_get_event_booth_fields_whitelist`

## `product.product` (extends)


Extension points: `_check_service_tracking_for_event_booths`

## `product.template` (extends)

- `service_tracking` Selection

Extension points: `_check_service_tracking_for_event_booths`, `_prepare_service_tracking_tooltip`

## `sale.order` (extends)

- `event_booth_ids` One2many → `event.booth` “Booths”
- `event_booth_count` Integer “Booth Count” (compute=_compute_event_booth_count)

Public methods: `action_confirm`, `action_view_booth_list`

Extension points: `_get_product_catalog_domain`

## `sale.order.line` (extends)

- `event_booth_category_id` Many2one → `event.booth.category` “Booths Category”
- `event_booth_pending_ids` Many2many → `event.booth` “Pending Booths” (compute=_compute_event_booth_pending_ids)
- `event_booth_registration_ids` One2many → `event.booth.registration` “Confirmed Registration”
- `event_booth_ids` One2many → `event.booth` “Confirmed Booths”

Extension points: `_check_event_booth_registration_ids`, `_get_display_price`, `_get_sale_order_line_multiline_description_sale`

## `event.booth.configurator` (defines)

Event Booth Configurator

- `product_id` Many2one → `product.product` “Product” (readonly)
- `sale_order_line_id` Many2one → `sale.order.line` “Sale Order Line” (readonly)
- `event_id` Many2one → `event.event` “Event” (required)
- `event_booth_category_available_ids` Many2many (readonly, related=event_id.event_booth_category_available_ids)
- `event_booth_category_id` Many2one → `event.booth.category` “Booth Category” (required, store, compute=_compute_event_booth_category_id)
- `event_booth_ids` Many2many → `event.booth` “Booth” (required, store, compute=_compute_event_booth_ids)

Extension points: `_check_if_no_booth_ids`
