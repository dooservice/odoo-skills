# eCommerce extras

What the online shop adds on top of the basics of `website-and-ecommerce.md`: stock
shown on the product page and out-of-stock rules (`website_sale_stock`), back-in-stock
alerts, the wishlist (`website_sale_wishlist`, `website_sale_stock_wishlist`), product
comparison by attributes (`website_sale_comparison`), files delivered with a product
(digital products) and address autocomplete at checkout. From 20.0 the wishlist and the
comparison are part of `website_sale`. Product data itself is in
`products-and-categories.md`; stock in `inventory.md`.

**At a glance**

- Apps: `website_sale`, `website_sale_stock`; `website_sale_wishlist`,
  `website_sale_comparison` (in `website_sale` from 20.0); `website_sale_digital` (16.0);
  `website_sale_autocomplete` (up to 19.0).
- Names that change by version: stock defaults `allow_out_of_stock_order` (16.0-18.0),
  `default_allow_out_of_stock_order` (19.0+); wishlist and comparison setting (16.0-18.0),
  module from Apps (19.0), in `website_sale` (20.0); digital files `website_sale_digital`
  (16.0), `attached_on` (17.0), `attached_on_sale` (18.0+); storable
  `detailed_type='product'` (16.0, 17.0), `is_storable` (18.0+).
- Sections: Before you start; The standard flow (1 warehouse of the website, 2 stock rules
  per product, 3 wishlist, 4 comparison); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `website_sale`; `website_sale_stock` installs itself with `stock`. Up to 18.0
  the wishlist and comparison are settings in Website ‣ Configuration ‣ Settings
  (`module_website_sale_wishlist`, `module_website_sale_comparison`); in 19.0 they are
  installed from Apps; in 20.0 they need nothing. 16.0 digital files:
  `module_website_sale_digital`. Address autocomplete up to 19.0:
  `module_website_sale_autocomplete`. Ask before installing.
- Settings (Website ‣ Configuration ‣ Settings, per website, pass `website_id`):
  `website_warehouse_id`; the defaults for new products `allow_out_of_stock_order`,
  `available_threshold`, `show_availability` (16.0 to 18.0), named
  `default_allow_out_of_stock_order`, `default_available_threshold`,
  `default_show_availability` from 19.0.
- Read first:

```python
print(env['website'].search_read([], ['name', 'warehouse_id']))
print(env['product.template'].search_read([('is_published', '=', True), ('is_storable', '=', True)],
      ['name', 'allow_out_of_stock_order', 'show_availability', 'available_threshold'], limit=20))
```

`is_storable` is 18.0+; up to 17.0 filter `('detailed_type', '=', 'product')`.

## The standard flow

1. **Warehouse of the website.** Website ‣ Configuration ‣ Settings, Inventory section.

   20.0, 19.0:

   ```python
   website = env['website'].search([('name', '=', '<website name>')])
   env['res.config.settings'].create({
       'website_id': website.id,
       'website_warehouse_id': env['stock.warehouse'].search([('company_id', '=', website.company_id.id)], limit=1).id,
       'default_allow_out_of_stock_order': False,
       'default_show_availability': True,
       'default_available_threshold': 5,
   }).execute()
   env.cr.commit()
   ```

   18.0, 17.0, 16.0: the same without the `default_` prefix.

   Leaves the shop counting the free quantity of that warehouse (all warehouses of the
   company when empty), and new products refusing orders when out of stock.

2. **Stock rules per product.** Website ‣ eCommerce ‣ Products ‣ Products, the product,
   Sales tab, next to the ribbon: Out-of-Stock (Continue Selling), Show Available Qty
   with its threshold, the out-of-stock message (storable products only).

   ```python
   product = env['product.template'].search([('default_code', '=', '<internal reference>')])
   product.write({'allow_out_of_stock_order': False, 'show_availability': True,
                  'available_threshold': 5, 'out_of_stock_message': '<p>Back next week.</p>'})
   env.cr.commit()
   ```

   Leaves the product page showing "Only 3 left" under 5 units and blocking the cart at
   0. Visitors can leave their email to be told when it is back in stock.

3. **Wishlist.** Visitors click the heart on a product; logged-in customers keep it
   across sessions, guests for the session. The wishlist page is `/shop/wishlist`.

   ```python
   print(env['product.wishlist'].read_group([], ['product_id'], ['product_id'], limit=10))
   ```

   With stock (`website_sale_stock_wishlist` up to 19.0), a wishlisted product that is
   out of stock offers the back-in-stock alert.

4. **Comparison.** Group attributes in categories: Website ‣ eCommerce ‣ Products ‣
   Attribute Categories, then set `category_id` on each attribute. Visitors add
   products to compare (`/shop/compare`) and see a table by category.

   ```python
   cat = env['product.attribute.category'].create({'name': 'Dimensions'})
   env['product.attribute'].search([('name', 'in', ['Width', 'Height'])]).write({'category_id': cat.id})
   env.cr.commit()
   ```

## Variations

- **Digital products.** 16.0 (`website_sale_digital`): attach the file on the product
  (Files smart button) with `product_downloadable`; the buyer downloads it from the
  portal once paid. 17.0+: the product's Documents smart button (`product.document`),
  visible on the order when `attached_on` (17.0) or `attached_on_sale` (18.0+) is
  `sale_order`; the buyer downloads it from the confirmed order in the portal.
- **Hide out-of-stock products** (20.0): `group_unpublish_out_of_stock` in the shop
  settings.
- **Address autocomplete at checkout.** Up to 19.0 `website_sale_autocomplete` with a
  Google Places key (`google_places_api_key`; 19.0 `website_google_places_api_key`);
  20.0 `website_address_autocomplete`. The key comes from the user's Google account;
  see `website-content.md`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Stock defaults in settings | `allow_out_of_stock_order`... | same | same | `default_...` | `default_...`, in `website_sale` |
| Wishlist | setting | setting | setting | module from Apps | in `website_sale` |
| Comparison | setting | setting | setting | module from Apps | in `website_sale` |
| Digital files | `website_sale_digital` | product documents, `attached_on` | `attached_on_sale` | same | same |
| Storable product | `detailed_type='product'` | same | `is_storable` | same | same |
| Hide out-of-stock | no | no | no | no | `group_unpublish_out_of_stock` |

## Verify

```python
product.invalidate_recordset()
print(website.warehouse_id.name, product.allow_out_of_stock_order, product.show_availability, product.available_threshold)
print(env['product.attribute'].search_read([('category_id', '!=', False)], ['name', 'category_id']))
```

Then ask the user to open the product in a private window and try to add more than the
available quantity.

## Pitfalls

- The shop counts free quantity (on hand minus reserved) of the website's warehouse;
  stock in another warehouse does not count.
- `allow_out_of_stock_order` True sells what is not there; check with the user before
  turning it on for many products.
- Services and consumables have no stock: the rules apply only to storable products.
- The Google Places key is billed by Google per request; restrict it to the website's
  domain.
