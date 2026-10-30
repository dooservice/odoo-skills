# Pickup in store

Online shop customers who collect their order in a store and may pay there. The store is
a warehouse (`stock.warehouse`) with an address; a delivery method of the pickup type
(`delivery.carrier`) offers it at checkout, and a "pay on site" payment provider
(`payment.provider`, code `custom`) lets the customer pay when collecting. The order's
delivery leaves from the chosen store's warehouse. This recipe covers
`website_sale_picking` (On Site Payments & Picking, 16.0 and 17.0) and
`website_sale_collect` (Click & Collect, 18.0+). The shop itself, its delivery methods and
providers are in `website-and-ecommerce.md`; shipping by carrier is in
`shipping-and-carriers.md`. Pickup in a Point of Sale shop is not part of these modules.

**At a glance**

- Apps: `website_sale` and `stock`; 16.0 also `website_sale_delivery`.
- Names that change by version: module `website_sale_picking` up to 17.0,
  `website_sale_collect` 18.0+; method type `onsite` up to 17.0, `in_store` 18.0+;
  `warehouse_id` up to 17.0, `warehouse_ids` 18.0+; `opening_hours` 18.0+; provider
  `custom_mode='onsite'` up to 17.0, `custom_mode='on_site'` 18.0+; provider switch
  `state` up to 19.0, `is_live` 20.0.
- Sections: Before you start; The standard flow (1 give each store an address, 2 set up
  the pickup method, 3 offer payment on site, 4 the customer orders, 5 hand over and get
  paid); Variations; Versions; Verify; Pitfalls.

## Before you start

- Settings (Website ‣ Configuration ‣ Settings, per website): On Site Payments & Picking
  (`module_website_sale_picking`, 16.0, 17.0) or Click & Collect
  (`module_website_sale_collect`, 18.0+). Each installs a module: only with the user's
  yes.

```python
website = env['website'].search([('name', '=', '<website name>')])
env['res.config.settings'].create({'website_id': website.id, 'module_website_sale_collect': True}).execute()
env.cr.commit()
```

  16.0, 17.0: the field is `module_website_sale_picking`.

- Read first:

  20.0:

```python
print(env['ir.module.module'].search([('name', '=', 'website_sale_collect')]).state)
print(env['stock.warehouse'].search_read([('company_id', '=', website.company_id.id)], ['name', 'code', 'partner_id', 'opening_hours']))
print(env['delivery.carrier'].search_read([('delivery_type', '=', 'in_store')], ['name', 'is_published', 'website_id', 'product_id', 'warehouse_ids']))
print(env['payment.provider'].search_read([('custom_mode', '=', 'on_site')], ['name', 'is_live', 'is_published', 'company_id']))
```

  18.0, 19.0: the same, with `state` instead of `is_live`. 16.0, 17.0:

```python
print(env['ir.module.module'].search([('name', '=', 'website_sale_picking')]).state)
print(env['stock.warehouse'].search_read([('company_id', '=', website.company_id.id)], ['name', 'code', 'partner_id']))
print(env['delivery.carrier'].search_read([('delivery_type', '=', 'onsite')], ['name', 'is_published', 'website_id', 'product_id', 'warehouse_id']))
print(env['payment.provider'].search_read([('custom_mode', '=', 'onsite')], ['name', 'state', 'is_published', 'company_id']))
```

## The standard flow

Odoo's documentation (Click & Collect from 18.0): the stores, the pickup method, the pay on
site provider; then the customer's order and its collection.

1. **Give each store an address.** Inventory ‣ Configuration ‣ Warehouse Management ‣
   Warehouses, the warehouse, Address (`partner_id`); 18.0+ also Opening Hours
   (`opening_hours`, a working schedule).

   ```python
   store = env['stock.warehouse'].search([('code', '=', 'WH2')])
   store.partner_id = env['res.partner'].create({
       'name': 'Example Shop', 'parent_id': store.company_id.partner_id.id, 'type': 'other',
       'street': 'Example Street 1', 'city': 'Example City', 'zip': '1000', 'country_id': country.id,
   })
   store.opening_hours = env.ref('resource.resource_calendar_std')
   env.cr.commit()
   ```

   16.0, 17.0: leave out `opening_hours`; the field does not exist.

   Leaves the store with its own address. A new warehouse takes the company's address:
   give each store its own contact instead of editing that one, which is the company's.
   18.0+ lists stores by distance to the customer: the address is geolocated
   (`base_geolocalize`, OpenStreetMap) the first time it is shown.

2. **Set up the pickup method.** 16.0, 17.0: Website ‣ Configuration ‣ Settings, Picking
   sites (`picking_site_ids`), one method per store. 18.0+: installing Click & Collect
   creates "Pick up in store" (`website_sale_collect.carrier_pick_up_in_store`) with every
   warehouse of the company; open it from the setting's link or from the delivery
   methods menu (`website-and-ecommerce.md`), Stores tab.

   18.0+:

   ```python
   carrier = env.ref('website_sale_collect.carrier_pick_up_in_store')
   carrier.write({'warehouse_ids': [(6, 0, stores.ids)], 'is_published': True})
   env.cr.commit()
   ```

   16.0, 17.0, one method per store:

   ```python
   carrier = env['delivery.carrier'].create({
       'name': 'Pickup at Example Shop', 'delivery_type': 'onsite', 'warehouse_id': store.id,
       'product_id': env.ref('website_sale_picking.onsite_delivery_product').id,
       'website_id': website.id, 'is_published': True,
   })
   env.cr.commit()
   ```

   Leaves a published pickup method. Its price is the sales price of its product (0 by
   default). 18.0+: a published `in_store` method needs at least one store, all of its
   company; writing `delivery_type='in_store'` clears its countries, states and zip
   prefixes.

3. **Offer payment on site.** Website ‣ Configuration ‣ eCommerce ‣ Payment Providers
   (16.0 to 19.0) or Payments (20.0): Pay in Store (16.0, 17.0,
   `website_sale_picking.payment_provider_onsite`) or Pay on Site (18.0+,
   `website_sale_collect.payment_provider_on_site`); enable and publish it.

   20.0:

   ```python
   provider = env.ref('website_sale_collect.payment_provider_on_site')
   provider.write({'is_live': True, 'is_published': True})
   env.cr.commit()
   ```

   16.0 to 19.0 (16.0, 17.0: `website_sale_picking.payment_provider_onsite`):

   ```python
   provider = env.ref('website_sale_collect.payment_provider_on_site')
   provider.write({'state': 'enabled', 'is_published': True})
   env.cr.commit()
   ```

   Leaves the provider offered at checkout only when the order is collected in a store.
   It is optional: customers may pay online with another provider and still collect.

4. **The customer orders.** In the shop, the customer chooses the pickup method and a
   store at the delivery step, then pays online or chooses to pay on site. There is no
   ORM equivalent: ask the user to test it in a private window.

   Leaves, with pay on site, a pending transaction and:
   - 18.0+: the order confirmed (`sale`), its `warehouse_id` the chosen store, the
     delivery order in that warehouse.
   - 16.0, 17.0: a quotation in `sent` with `warehouse_id` from the method; confirm it
     (`order.action_confirm()`, the Confirm button) once the store accepts it.

5. **Hand over and get paid.** When the customer collects, validate the delivery
   (`shipping-and-carriers.md`, step 5) and invoice the order (`sales-and-crm.md`). The
   payment taken in the store is registered on the invoice by accounting. 20.0: validating
   the delivery shows the Collect Payment reminder with the amount due, and the payment
   is recorded when the order is settled in Point of Sale.

## Variations

- **Pickup only from one store (18.0+).** Keep one warehouse in `warehouse_ids`.
- **Stock per store (18.0+).** With a warehouse set on the website (Website ‣
  Configuration ‣ Settings, `website_warehouse_id`) the product page and the store
  selector show what each store has in stock.
- **Pay online, collect in store.** Leave the pay on site provider unpublished: the
  pickup method stays, payment goes through the online providers.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Module | `website_sale_picking` | same | `website_sale_collect` | same | same |
| Setting | `module_website_sale_picking` | same | `module_website_sale_collect` | same | same |
| Method type | `onsite` | same | `in_store` | same | same |
| Stores on the method | `warehouse_id` (one) | same | `warehouse_ids` (several) | same | same |
| Opening hours on the warehouse | no | no | `opening_hours` | same | same |
| Provider | `website_sale_picking.payment_provider_onsite`, `custom_mode='onsite'` | same | `website_sale_collect.payment_provider_on_site`, `custom_mode='on_site'` | same | same |
| Provider published at install | no | no | no | yes | yes |
| Order paid on site | quotation `sent` | same | confirmed | same | same, Collect Payment reminder |
| Provider switch | `state` | same | same | same | `is_live` |

## Verify

```python
orders = env['sale.order'].search([('carrier_id.delivery_type', 'in', ['onsite', 'in_store']), ('website_id', '=', website.id)], order='id desc', limit=5)
print(orders.read(['name', 'state', 'warehouse_id', 'carrier_id']))
print(orders.picking_ids.read(['name', 'state', 'picking_type_id']))
print(orders.transaction_ids.read(['provider_id', 'state', 'amount']))
```

Each pickup order points to the chosen store's warehouse, its delivery is in that
warehouse, and a pay on site transaction is `pending` until the payment is registered.

## Pitfalls

- A store whose address cannot be geolocated gets no real coordinates and is sorted by
  a wrong distance (18.0+): complete the street, city, zip and country.
- A published `in_store` method without stores cannot be saved: add a warehouse first.
- The pay on site provider published but not enabled (or not live in 20.0) is not
  offered.
- 16.0, 17.0: orders paid on site wait as quotations: someone must confirm them, or no
  delivery is prepared.
- Stock of a store is reserved only once the order is confirmed: a busy store may sell
  what another customer is collecting.
