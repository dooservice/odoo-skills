# website_event_sale — Online Event Ticketing

Depends on: website_event, event_sale, website_sale.

## `event.event.ticket` (extends)


## `product.product` (extends)

- `event_ticket_ids` One2many → `event.event.ticket` “Event Tickets”

Extension points: `_get_product_placeholder_filename`

## `product.template` (extends)


Extension points: `_get_product_types_allow_zero_price`

## `product.pricelist.item` (extends)


## `sale.order` (extends)


Extension points: `_prepare_order_line_values`

## `sale.order.line` (extends)


## `event.sale.report` (extends)

- `is_published` Boolean “Published Events” (readonly)
