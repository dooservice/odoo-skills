# website_sale_delivery — eCommerce Delivery

Depends on: website_sale, delivery, website_sale_stock.

## `delivery.carrier` (extends)

Inherits: `website.published.multi.mixin`

- `website_description` Text “Description for Online Quotations” (related=product_id.description_sale)

## `res.country` (extends)


Public methods: `get_website_sale_countries`, `get_website_sale_states`

## `sale.order` (extends)

- `amount_delivery` Monetary “Delivery Amount” (store, compute=_compute_amount_delivery)

Extension points: `_check_carrier_quotation`, `_get_delivery_methods`

## `sale.order.line` (extends)
