# website_sale_wishlist — Shopper's Wishlist

Depends on: website_sale.

## `product.wishlist` (defines)

Product Wishlist

- `partner_id` Many2one → `res.partner` “Owner”
- `product_id` Many2one → `product.product` “Product” (required)
- `currency_id` Many2one → `res.currency` (readonly, related=website_id.currency_id)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist”
- `price` Monetary “Price”
- `website_id` Many2one → `website` (required)
- `active` Boolean (required)

Public methods: `current`

Extension points: `_check_wishlist_from_session`

## `res.partner` (extends)

- `wishlist_ids` One2many → `product.wishlist` “Wishlist”

## `product.template` (extends)


## `product.product` (extends)


## `res.users` (extends)


Extension points: `_check_credentials`
