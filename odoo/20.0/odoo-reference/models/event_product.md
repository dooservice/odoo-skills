# event_product — Events Product

Depends on: event, product, account.

## `event.event` (extends)

- `currency_id` Many2one → `res.currency` “Currency” (readonly, related=company_id.currency_id)

## `event.event.ticket` (extends)

- `total_price_reduce_taxinc` Float “Total Price Reduce Tax inc” (compute=_compute_total_price_reduce_taxinc)
- `total_price_incl` Float “Total Price include” (compute=_compute_total_price_incl)

## `event.registration` (extends)

- `sale_status` Selection “Sale Status” (readonly, store, compute=_compute_registration_status)

## `event.type.ticket` (extends)

- `description` Text (store, compute=_compute_description)
- `product_id` Many2one → `product.product` “Product” (required, index)
- `currency_id` Many2one “Currency” (related=product_id.currency_id)
- `price` Float “Ticket Price” (store, compute=_compute_price)
- `price_reduce` Float “Price Reduce” (compute=_compute_price_reduce)
- `additional_product_ids` Many2many → `product.product` “Additional Products”
- `total_price` Float “Total Price” (compute=_compute_total_price)
- `total_price_reduce` Float “Total Price Reduce” (compute=_compute_price_reduce)

Extension points: `_get_event_ticket_fields_whitelist`

## `product.product` (extends)

- `event_ticket_ids` One2many → `event.event.ticket` “Event Tickets”

Extension points: `_check_event_ticket_service_tracking`

## `product.template` (extends)

- `service_tracking` Selection
