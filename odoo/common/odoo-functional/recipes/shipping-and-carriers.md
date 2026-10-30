# Shipping and carriers

A delivery method (`delivery.carrier`) prices the shipping of a sales order and follows its
delivery order (`stock.picking`) to the customer: the order gets a delivery line, the
delivery order gets the carrier, its weight and a tracking reference, and the shipping is
invoiced with the order. This recipe covers delivery methods in the back office (`delivery`,
and `stock_delivery` from 17.0), packages and weights, grouping deliveries in batches by
carrier (`delivery_stock_picking_batch` up to 19.0), dispatch with vehicles and docks
(`stock_fleet`, 18.0+), the text message sent when a delivery leaves (`stock_sms`) and cash
on delivery (19.0+). Creating a delivery method for the online shop is in
`website-and-ecommerce.md`; customers collecting in a store are in `pickup-in-store.md`.
Carrier connectors that print labels through a carrier's service are Enterprise or
specific to a few countries (Mondial Relay) and are left out: the methods here are
`fixed` and `base_on_rule`.

**At a glance**

- Apps: `sale_stock` and `delivery`. 16.0: `delivery` holds the sales and the stock part.
  17.0+: `delivery` is the sales part and `stock_delivery` the stock part, installed with
  it when `sale_stock` is there.
- Names that change by version: stock part in `delivery` 16.0, `stock_delivery` 17.0+;
  `shipping_weight`, `fixed_margin` 17.0+; `tracking_url`, `max_weight` 18.0+; Put in Pack
  `choose.delivery.package` up to 18.0, `stock.put.in.pack` 19.0+; package
  `stock.quant.package` up to 18.0, `stock.package` 19.0+; SMS `stock_move_sms_validation`
  up to 18.0, `stock_confirmation_type` 19.0+; docks `is_a_dock` 18.0, `dock_ids` 19.0+;
  `allow_cash_on_delivery` 19.0+; Shipping Methods menu up to 17.0, Delivery Methods
  18.0+.
- Sections: Before you start; The standard flow (1 create the delivery method, 2 add it to
  the quotation, 3 confirm the order, 4 record the tracking reference, 5 validate the
  delivery, 6 invoice); Variations; Versions; Verify; Pitfalls.

## Before you start

- Settings (Inventory ‣ Configuration ‣ Settings): Delivery Methods (`module_delivery`)
  installs `delivery`; Packages (`group_stock_tracking_lot`) for packages; Batch
  Transfers (`module_stock_picking_batch` up to 19.0, `group_stock_picking_batch` in
  20.0) for batches; Dispatch Management System (`module_stock_fleet`, 18.0, 19.0;
  Transport Management in 20.0) for vehicles; SMS Confirmation (`module_stock_sms`).
  Each `module_*` installs a module: only with the user's yes.
- Products need a weight (`weight`, product form, Inventory tab) for weight-based prices,
  package weights and vehicle loads.
- Read first:

```python
company = env.company
warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
print(env['ir.module.module'].search([('name', 'in', ['delivery', 'stock_delivery', 'delivery_stock_picking_batch', 'stock_fleet', 'stock_sms'])]).mapped(lambda m: (m.name, m.state)))
print(env['delivery.carrier'].search_read([('company_id', 'in', [company.id, False])], ['name', 'delivery_type', 'fixed_price', 'invoice_policy', 'integration_level', 'product_id', 'free_over', 'amount']))
print(warehouse.out_type_id.read(['print_label']))
order = env['sale.order'].search([('name', '=', 'S00042')])
print(order.carrier_id.name, order.order_line.filtered('is_delivery').read(['name', 'price_unit', 'qty_invoiced']))
print(order.picking_ids.read(['name', 'state', 'carrier_id', 'carrier_tracking_ref', 'weight', 'batch_id']))
```

## The standard flow

Odoo's documentation: a delivery method, added to the quotation, carried by the delivery
order, which is validated with its tracking reference; the shipping is invoiced with the
order.

1. **Create the delivery method.** Inventory ‣ Configuration ‣ Delivery ‣ Shipping
   Methods (16.0, 17.0) or Delivery Methods (18.0+); also Sales ‣ Configuration ‣ Sales
   Orders ‣ Shipping Methods (16.0, 17.0), Delivery Methods (18.0, 19.0), Sales ‣
   Configuration ‣ Deliveries (20.0); New.

   ```python
   carrier = env['delivery.carrier'].create({
       'name': 'Example Courier', 'delivery_type': 'fixed', 'fixed_price': 8.0,
       'product_id': env.ref('delivery.product_product_delivery').id,
       'invoice_policy': 'estimated',
   })
   env.cr.commit()
   ```

   Leaves a method that quotations can use.

   - `delivery_type`: `fixed` (one price per order) or `base_on_rule` (`price_rule_ids` on
     weight, volume, quantity or price; see `website-and-ecommerce.md`).
   - `product_id`: the service product of the delivery line; its taxes and income account
     apply to the shipping.
   - `invoice_policy`: `estimated` (the price on the quotation is invoiced) or `real` (the
     cost computed when the delivery is validated is written on the order).
   - `free_over` with `amount`: free from that order amount, shipping excluded.
   - `country_ids`, `state_ids`, `zip_prefix_ids` restrict where it ships; from 18.0 also
     `max_weight`, `max_volume`, `must_have_tag_ids`, `excluded_tag_ids`.
   - `tracking_url` (18.0+): a link with `<shipmenttrackingnumber>` where the tracking
     reference goes; the customer sees it in the portal.
   - `margin` (percentage) and, from 17.0, `fixed_margin` raise the computed price.

2. **Add it to the quotation.** On the quotation, the Add shipping button (20.0:
   Shipping), choose the method, Get rate, Add.

   ```python
   wizard = env['choose.delivery.carrier'].create({'order_id': order.id, 'carrier_id': carrier.id})
   wizard.update_price()
   wizard.button_confirm()
   env.cr.commit()
   ```

   Leaves `order.carrier_id` set and a delivery line (`is_delivery`) at the rated price.
   With `real` the line is at 0 and its description shows the estimated cost.

   - `update_price()` raises an error when the method cannot ship to the address (rules,
     countries, weight): show it to the user.
   - 17.0+: the wizard's `total_weight` comes from the order's `shipping_weight`, which
     the user may correct before Get rate.
   - A customer's usual method: `property_delivery_carrier_id` on the contact (Sales &
     Purchase tab), per company; the wizard proposes it.
   - Lines added after the shipping make the order show Update shipping cost
     (`recompute_delivery_price`): run the wizard again.

3. **Confirm the order.** The Confirm button (`sales-and-crm.md`).

   ```python
   order.action_confirm()
   env.cr.commit()
   ```

   Leaves the order in `sale` and its delivery order with `carrier_id` and `weight`. Every
   step of a multi-step delivery carries the carrier (the rules' `propagate_carrier`).

4. **Record the tracking reference.** The delivery order (Inventory ‣ Operations ‣
   Transfers in 16.0, Transfers ‣ Deliveries from 17.0), Additional Info tab, Shipping
   Information, Tracking Reference. 16.0 and 17.0 make it read-only once the delivery is
   done: type it before validating.

   ```python
   picking = order.picking_ids.filtered(lambda p: p.picking_type_code == 'outgoing' and p.state not in ('done', 'cancel'))
   picking.carrier_tracking_ref = 'TRK-0001'
   env.cr.commit()
   ```

   Leaves the reference on the delivery and, with `tracking_url` (18.0+), the tracking
   link (`carrier_tracking_url`) on the delivery and in the customer portal.

5. **Validate the delivery.** The delivery order, Validate.

   ```python
   for move in picking.move_ids:
       move.quantity = move.product_uom_qty
   res = picking.button_validate()
   env.cr.commit()
   ```

   16.0: the done quantity is `quantity_done`, not `quantity`.

   Leaves the delivery `done`. `res` may be a wizard (backorder, immediate transfer in
   16.0, SMS on first use, Collect Payment in 20.0): read it. Validating stock is real
   inventory: only with the user's yes, and normally done by the warehouse.

   On a delivery operation type with `print_label` (on for Delivery Orders), a method
   with `integration_level='rate_and_ship'` (the default) and no tracking reference yet,
   validation runs `send_to_shipper()`: it writes `carrier_price`, posts "Shipment sent to
   carrier" on the delivery and, with `real`, writes that cost on the order's delivery
   line. A delivery that already has a reference skips it.

6. **Invoice.** The order's Create Invoice (`sales-and-crm.md`). The delivery line is a
   service ordered once: it is invoiced with the first invoice of the order.

## Variations

- **Packages with their shipping weight.** Settings `group_stock_tracking_lot`; package
  types in Inventory ‣ Configuration ‣ Delivery ‣ Package Types (`base_weight`,
  `max_weight`). On a delivery with a carrier, Put in Pack asks for the package type and
  the shipping weight:

  19.0, 20.0:

  ```python
  picking.with_context(weight=2.5).action_put_in_pack(package_type_id=package_type.id)
  env.cr.commit()
  ```

  16.0 to 18.0, through the wizard `choose.delivery.package`:

  ```python
  res = picking.action_put_in_pack()
  if isinstance(res, dict) and res.get('res_model') == 'choose.delivery.package':
      env['choose.delivery.package'].with_context(res['context']).create({'delivery_package_type_id': package_type.id, 'shipping_weight': 2.5}).action_put_in_pack()
  env.cr.commit()
  ```

  Leaves the done quantities in a package (`stock.quant.package` up to 18.0,
  `stock.package` from 19.0) with `shipping_weight`. Lines of transfers with different
  carriers, or without one, cannot share a package.

- **Change the method after confirming.** Run the wizard of step 2 on the confirmed
  order: `set_delivery_line()` replaces the delivery line and writes the new carrier on
  the open deliveries (returns excluded). Done deliveries keep the old one.

- **Batch deliveries by carrier.** Batch transfers on (see `inventory.md`); then
  Inventory ‣ Configuration ‣ Warehouse Management ‣ Operations Types, Delivery Orders,
  Automatic Batches, group by Carrier:

  ```python
  warehouse.out_type_id.write({'auto_batch': True, 'batch_group_by_carrier': True, 'batch_max_weight': 500})
  env.cr.commit()
  ```

  Leaves confirmed deliveries of the same carrier grouped in one batch, up to the
  maximum weight (in the weight unit of the database). A batch needs two compatible
  deliveries to be created. `batch_group_by_carrier` and `batch_max_weight` come from
  `delivery_stock_picking_batch` (16.0 to 19.0, installed by itself with `delivery` and
  `stock_picking_batch`) and from `stock_delivery` in 20.0. Validate the batch as in
  `inventory.md`: each delivery goes through step 4.

- **Dispatch with vehicles and docks (18.0+).** Settings `module_stock_fleet` (it installs
  `stock_fleet`, and with it `stock_picking_batch` in 18.0, 19.0; 20.0 turns on
  `group_stock_picking_batch`). The
  load of each vehicle type: Fleet ‣ Configuration ‣ Models ‣ Categories, Max Weight
  (`weight_capacity`) and Max Volume (`volume_capacity`); the vehicle's category and
  driver come from the Fleet app. Docks: 18.0, a location with `is_a_dock`; 19.0+, the
  operation type's Docks (`dock_ids`), shown when `dispatch_management` is on (set on
  receipts and deliveries at install). On the batch, set the vehicle and the dock:

  ```python
  batch = env['stock.picking.batch'].create({
      'picking_type_id': warehouse.out_type_id.id, 'picking_ids': [(6, 0, pickings.ids)],
      'vehicle_id': vehicle.id, 'dock_id': dock.id,
  })
  batch.action_confirm()
  env.cr.commit()
  ```

  Leaves a batch with the driver (`driver_id`) and vehicle category from the vehicle, the
  load in `used_weight_percentage` and `used_volume_percentage`, the deliveries ordered
  by zip (`batch_sequence`), and their moves leaving from the dock. A batch with a
  `vehicle_category_id` and no `vehicle_id` is a third-party carrier.

- **Text message when the delivery leaves.** `stock_sms` is installed with Inventory and
  SMS. 16.0 to 18.0: on by default per company (`stock_move_sms_validation`); 19.0+: off
  until `stock_text_confirmation` (installing `stock_sms` turns it on for every company).

  19.0, 20.0:

  ```python
  env['res.config.settings'].create({
      'stock_text_confirmation': True, 'stock_confirmation_type': 'sms', 'module_stock_sms': True,
      'stock_sms_confirmation_template_id': env.ref('stock_sms.sms_template_data_stock_delivery').id,
  }).execute()
  env.cr.commit()
  ```

  16.0 to 18.0:

  ```python
  env['res.config.settings'].create({
      'stock_move_sms_validation': True,
      'stock_sms_confirmation_template_id': env.ref('stock_sms.sms_template_data_stock_delivery').id,
  }).execute()
  env.cr.commit()
  ```

  Leaves an SMS sent to the customer's phone (16.0 to 18.0: mobile or phone) on every
  validated delivery. The first validation in a company shows the `confirm.stock.sms`
  wizard: Confirm keeps it, Disable SMS turns it off. SMS go through Odoo's paid IAP
  service and need credits. The email equivalent is `stock_move_email_validation`.

- **Cash on delivery (19.0+).** On the method, Cash on Delivery
  (`allow_cash_on_delivery`); the provider `delivery.payment_provider_cod` is enabled and
  published at install. A shop customer who picks it gets the order confirmed with a
  pending payment; the driver collects it. 19.0 publishes it at install; 20.0 does not:
  publish it from the provider's form, with the user's yes. 20.0: validating such a delivery opens a
  Collect Payment reminder (`pay.on.delivery`) with the amount due.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Stock part of delivery methods | `delivery` | `stock_delivery` | same | same | same |
| Order `shipping_weight`, wizard `total_weight` | no | yes | yes | yes | yes |
| `fixed_margin` | no | yes | yes | yes | yes |
| `tracking_url`, `max_weight`, `max_volume`, product tags | no | no | yes | yes | yes |
| Quotation button | Add shipping | same | same | same | Shipping |
| Put in Pack wizard | `choose.delivery.package` | same | same | `stock.put.in.pack` | same |
| Package model | `stock.quant.package` | same | same | `stock.package` | same |
| Batch by carrier, max weight | `delivery_stock_picking_batch` | same | same | same | `stock_delivery` |
| Vehicles and docks | no | no | `stock_fleet`, dock = location `is_a_dock` | `stock_fleet`, `dock_ids` on the operation type | same, setting Transport Management |
| SMS switch | `stock_move_sms_validation` (default on) | same | same | `stock_text_confirmation`, `stock_confirmation_type` | same |
| SMS number | mobile or phone | same | same | phone | phone |
| Cash on delivery | no | no | no | `allow_cash_on_delivery` | same, Collect Payment reminder |
| Menu: methods (Inventory) | Inventory ‣ Configuration ‣ Delivery ‣ Shipping Methods | same | Inventory ‣ Configuration ‣ Delivery ‣ Delivery Methods | same | same |
| Menu: methods (Sales) | Sales ‣ Configuration ‣ Sales Orders ‣ Shipping Methods | same | Sales ‣ Configuration ‣ Sales Orders ‣ Delivery Methods | same | Sales ‣ Configuration ‣ Deliveries |

The same in every version: Inventory ‣ Configuration ‣ Delivery ‣ Package Types;
Inventory ‣ Configuration ‣ Warehouse Management ‣ Operations Types; the Send to Shipper
button on a delivery not yet sent.

## Verify

```python
print(order.carrier_id.name, order.order_line.filtered('is_delivery').read(['name', 'price_unit', 'qty_invoiced']))
print(order.picking_ids.read(['name', 'state', 'carrier_id', 'carrier_tracking_ref', 'carrier_price', 'weight', 'batch_id']))
```

The order has one delivery line at the expected price; its delivery is `done` with the
carrier and the tracking reference; with `real`, the delivery line holds the cost of
`carrier_price`. For a batch, its deliveries share the carrier; for dispatch, the batch
shows the vehicle, driver and load.

## Pitfalls

- A method that cannot ship to the address is not offered, or Get rate fails: check its
  countries, zip prefixes, rules and (18.0+) maximum weight and tags.
- Products without weight make weight rules and vehicle loads 0.
- `real` with a `fixed` or `base_on_rule` method only recomputes the quoted price, and a
  tracking reference typed before validating skips `send_to_shipper()`, leaving the
  delivery line at 0: use `estimated` with these methods.
- A delivery operation type without `print_label` never runs `send_to_shipper()` at
  validation: use the Send to Shipper button.
- Changing the method on a confirmed order does not touch done deliveries.
- Returns do not keep the carrier: a return is not shipped by the method.
- Installing `stock_sms` sends a paid SMS on every validated delivery to a customer with
  a phone: confirm the user wants it, or turn it off.
- Mondial Relay (`delivery_mondialrelay`, `website_sale_mondialrelay`,
  `website_sale_delivery_mondialrelay`) is a carrier network of a few countries: not
  covered here.
