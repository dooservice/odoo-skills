# Lots, serial numbers, expiration dates and barcodes

A tracked product (`tracking`) is counted by lot (`stock.lot`, many units share one
number) or by serial number (one unit per number). Lots are given on receipts and
manufacturing orders, reserved on deliveries by the removal strategy, and their history
is the traceability report. With `product_expiry` each lot also carries an expiration
date and the dates derived from it (best before, removal, alert); FEFO reserves the lots
that expire first, expired lots stop being reserved, and validating a transfer or a
manufacturing order with an expired lot asks for confirmation (`mrp_product_expiry`).
Barcodes are read through the company's barcode nomenclature (`barcodes`); the GS1
nomenclature (`barcodes_gs1_nomenclature`) reads GS1-128 barcodes that carry product,
lot, quantity and dates. All of this is Community; the Barcode app (scanning in the
warehouse, `stock_barcode`) is Enterprise and left out. Turning on lots and the general
stock flow are in `inventory.md`.

## Before you start

- Apps: `stock` (it installs `barcodes` and `barcodes_gs1_nomenclature` with it);
  `product_expiry` for expiration dates; `mrp_product_expiry` installs itself when `mrp`
  and `product_expiry` are both there.
- Settings (Inventory ‣ Configuration ‣ Settings, Traceability section):

```python
env['res.config.settings'].create({
    'group_stock_production_lot': True,
    'module_product_expiry': True,
}).execute()
env.cr.commit()
```

- `group_stock_production_lot`: Lots & Serial Numbers (see `inventory.md`).
- `module_product_expiry`: Expiration Dates. It installs a module: only with the user's
  yes. From 17.0 the form clears it when lots are turned off.
- `group_lot_on_delivery_slip`: lots and serial numbers printed on delivery slips;
  `group_expiry_date_on_delivery_slip` (from `product_expiry`): their expiration dates too.
- `group_stock_lot_print_gs1`: Print GS1 Barcodes for Lots & Serial Numbers, on lot labels.
- Read first:

```python
company = env.company
product = env['product.product'].search([('default_code', '=', '<reference>')], limit=1)
print(product.read(['tracking', 'barcode', 'categ_id']))
print(product.product_tmpl_id.read(['use_expiration_date', 'expiration_time', 'use_time', 'removal_time', 'alert_time']))
env['stock.lot'].search_read([('product_id', '=', product.id)], ['name', 'product_qty', 'expiration_date', 'removal_date', 'alert_date'])
env['stock.quant'].search_read([('product_id', '=', product.id), ('location_id.usage', '=', 'internal')], ['location_id', 'lot_id', 'quantity', 'reserved_quantity'])
print(product.categ_id.removal_strategy_id.method, company.nomenclature_id.name)
```

The expiration fields and lot dates exist only with `product_expiry` installed.

## The standard flow

Odoo's documentation of lots, serial numbers and expiration dates: track the product,
give its expiration times, receive it with lots, deliver it by FEFO, follow a lot, act on
expiry alerts.

1. **Track the product by lot or serial number.** Inventory ‣ Products ‣ Products, the
   product, Inventory tab (Traceability).

   ```python
   tmpl = product.product_tmpl_id
   tmpl.write({'is_storable': True, 'tracking': 'lot'})
   env.cr.commit()
   ```

   That is 18.0 and later. In 16.0 and 17.0 write `detailed_type='product'` instead of
   `is_storable=True`.

   Leaves a product that every receipt, delivery and adjustment asks a lot for.

   - `tracking`: `lot`, `serial`, `none` (16.0 to 19.0); `lot`, `serial` or empty in 20.0,
     where the form's `store_by` sets it (`products-and-categories.md`).
   - Changing the tracking of a product with stock needs the user's yes: quantities
     already on hand keep no lot until an adjustment gives them one.
   - 19.0+: `serial_prefix_format` (Custom Lot/Serial) on the template sets the prefix of
     the numbers Odoo proposes; it writes the product's own sequence `lot_sequence_id`.

2. **Give its expiration times.** Same tab, tick Expiration Date, then the Dates group.
   Needs `product_expiry` and a tracked product.

   ```python
   tmpl.write({
       'use_expiration_date': True,
       'expiration_time': 30,   # days after receipt or production until the goods expire
       'use_time': 10,          # best before: days before the expiration date
       'removal_time': 5,       # removal: days before the expiration date
       'alert_time': 7,         # alert: days before the expiration date
   })
   env.cr.commit()
   ```

   Leaves a product whose new lots get `expiration_date` = receipt date +
   `expiration_time`, and `use_date`, `removal_date`, `alert_date` that many days before
   it. Lots that already exist keep their dates. Setting the tracking to none (20.0: empty)
   turns `use_expiration_date` off.

3. **Remove by FEFO.** Inventory ‣ Configuration ‣ Products ‣ Product Categories (19.0+:
   Categories), the category, Force Removal Strategy; or on a location
   (Inventory ‣ Configuration ‣ Warehouse Management ‣ Locations, needs
   `group_stock_multi_locations`).

   ```python
   product.categ_id.removal_strategy_id = env.ref('product_expiry.removal_fefo')
   env.cr.commit()
   ```

   Leaves reservations ordered by `removal_date` (First Expiry First Out). The category
   is shared: count its products before changing it. Without a strategy the location's
   applies, else FIFO (`stock.removal_fifo`).

4. **Receive with lots.** The receipt (Inventory ‣ Operations ‣ Transfers ‣ Receipts
   from 17.0), the line's details: a Lot/Serial Number Name and, with `product_expiry`,
   its Expiration Date; for serials, Generate Serials (16.0: Assign Serial Numbers).

   ```python
   picking.action_assign()
   move = picking.move_ids.filtered(lambda m: m.product_id == product)
   move.move_line_ids.write({
       'lot_name': 'LOT-0001',
       'expiration_date': '2027-06-30 00:00:00',
       'quantity': move.product_uom_qty,
   })
   res = picking.button_validate()
   env.cr.commit()
   ```

   That is 17.0 and later; in 16.0 the done quantity of a line is `qty_done`, not
   `quantity`. `expiration_date` needs `product_expiry`; leave it out and the lot takes
   the receipt date plus `expiration_time`.

   Serial numbers, one line each, from a first number:

   ```python
   move._generate_serial_numbers('SN-0001', next_serial_count=5)
   env.cr.commit()
   ```

   That is 17.0 and later. In 16.0 the button opens the wizard `stock.assign.serial`:

   ```python
   env['stock.assign.serial'].create({'move_id': move.id, 'next_serial_number': 'SN-0001', 'next_serial_count': 5}).generate_serial_numbers()
   env.cr.commit()
   ```

   Leaves the receipt `done` and a `stock.lot` per name, with its dates, holding the
   quantity. Receipts create lots (`use_create_lots` on the operation type); deliveries
   take existing ones (`use_existing_lots`). As in `inventory.md`, `button_validate` may
   return a wizard: read `res`. Validating stock is real inventory: only with the user's
   yes.

5. **Deliver.** The delivery, Check Availability: Odoo reserves lots by the removal
   strategy. Change the lot of a line to send another one.

   ```python
   delivery.action_assign()
   print(delivery.move_line_ids.mapped(lambda ml: (ml.lot_id.name, ml.quantity)))
   for move in delivery.move_ids:
       move.quantity = move.product_uom_qty
   res = delivery.button_validate()
   env.cr.commit()
   ```

   That is 17.0 and later. In 16.0 the reserved quantity of a line is `reserved_uom_qty`
   and the done quantity of a move is `quantity_done`. To send another lot, write its
   `lot_id` on the move line before validating, with the user's yes.

   Leaves the delivery `done` and the lots on the customer's side. If a line holds a lot
   past its expiration date (19.0+: also past its removal date), `res` is the wizard
   `expiry.picking.confirmation`: Confirm delivers it anyway, Proceed except for expired
   only validates the other transfers. Show it to the user; never confirm an expired lot
   on their behalf:

   ```python
   if isinstance(res, dict) and res.get('res_model') == 'expiry.picking.confirmation':
       wizard = env['expiry.picking.confirmation'].with_context(res['context']).create({})
       print(wizard.description)
   ```

   With the user's yes, `wizard.process()` delivers the expired lot;
   `wizard.process_no_expired()` validates only the other transfers.

6. **Follow a lot.** Inventory ‣ Products ‣ Lots/Serial Numbers (18.0+: Lots / Serial
   Numbers), the lot: Location (where it is), Transfers (its deliveries), Traceability
   (every move up and down, through manufacturing).

   ```python
   lot = env['stock.lot'].search([('product_id', '=', product.id), ('name', '=', 'LOT-0001')])
   env['stock.move.line'].search_read([('lot_id', '=', lot.id), ('state', '=', 'done')], ['date', 'reference', 'location_id', 'location_dest_id', 'quantity'])
   print(lot.delivery_ids.mapped('partner_id.name'))
   ```

   That is 17.0 and later; in 16.0 read `qty_done` instead of `quantity`.

   Leaves nothing changed. For a recall, `delivery_ids` lists the transfers that sent the
   lot to customers.

7. **Act on expiry alerts.** The lots list, filter Expiration Alerts (alert date
   reached); the stock list (Inventory ‣ Reporting ‣ Stock) has the same filter (19.0+:
   Expired Lots, Alert Lots). The scheduler also leaves an activity on each lot in stock
   whose alert date is reached, for the product's responsible.

   ```python
   from odoo import fields
   env['stock.lot'].search_read([('alert_date', '<=', fields.Datetime.now()), ('product_qty', '>', 0)], ['name', 'product_id', 'expiration_date', 'product_qty'])
   env['stock.lot']._alert_date_exceeded()   # what the scheduler runs
   env.cr.commit()
   ```

   Leaves one activity per lot (`product_expiry_reminded` set, never repeated). Scrap the
   expired quantities (`inventory.md`) with the user's yes.

## Variations

- **Lots in manufacturing.** A tracked component asks its lot on the manufacturing
  order; a tracked finished product gets one from the order's Generate button
  (`manufacturing.md` has the order):

  ```python
  production.action_generate_serial()
  res = production.button_mark_done()
  env.cr.commit()
  ```

  The lot lands in `lot_producing_ids` from 19.0, in `lot_producing_id` up to 18.0. The new lot takes its expiration date from `expiration_time`. With
  `mrp_product_expiry`, a component lot past its expiration date makes
  `button_mark_done` return `expiry.picking.confirmation` instead of finishing; with the
  user's yes `env['expiry.picking.confirmation'].with_context(res['context']).create({}).confirm_produce()`
  produces anyway. For serials of a quantity above 1, 19.0+ return a wizard to enter
  them.

- **A lot's dates by hand.** On the lot form, change Expiration Date: best before,
  removal and alert move by the same difference. Write `expiration_date` on the lot
  through the ORM for the same effect.

- **Lot fields of your own.** 17.0+: Lot Properties on the product
  (`lot_properties_definition`), filled per lot (`lot_properties`), for data such as a
  vendor's batch reference. `ref` (Internal Reference) is on the lot in every version.

- **Barcode nomenclature.** Inventory ‣ Configuration ‣ Products ‣ Barcode
  Nomenclatures (developer mode). A nomenclature (`barcode.nomenclature`) is a list of
  rules (`barcode.rule`: `type`, `encoding`, `pattern`, `sequence`) that tell product,
  weight, lot, location or package barcodes apart. The company uses one
  (`res.company.nomenclature_id`, default `barcodes.default_barcode_nomenclature`); in
  Community its setting is only in Point of Sale settings (`barcode_nomenclature_id`)
  and, 17.0+, Events; the Inventory one belongs to the Enterprise Barcode app. Switching
  to GS1 changes how every scanner of the company reads barcodes: only with the user's
  yes.

  ```python
  company.nomenclature_id = env.ref('barcodes_gs1_nomenclature.default_gs1_nomenclature')
  env.cr.commit()
  ```

  The GS1 nomenclature (`is_gs1_nomenclature`) reads GS1-128 barcodes by application
  identifier: `01` product (GTIN), `10` lot, `21` serial, `17` expiration date, `15`
  best before date, `30`/`37` quantity, and others; `gs1_separator_fnc1` is the FNC1
  separator. Product barcodes (`barcode` on the product, unique) must then be valid
  GTINs. Lot labels print a GS1 barcode with `group_stock_lot_print_gs1`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Tracked product | `detailed_type='product'`, `tracking` | same | `is_storable`, `tracking` | same | `tracking` empty for none; `store_by` |
| Done quantity on a line | `qty_done` | `quantity` | same | same | same |
| Generate serials | wizard `stock.assign.serial` | `_generate_serial_numbers(first, count)` | same | same | same, from the product's `lot_sequence_id` |
| Custom lot/serial prefix | no | no | no | `serial_prefix_format` | same |
| Lot properties | no | `lot_properties` | same | same | same |
| Reservation skips expired lots | no | past `expiration_date` | same | past `removal_date` | same |
| Expired lot warning on delivery | past expiration date | same | same | past expiration or removal date | same |
| Fresh quantities (forecast without lots to remove) | no | no | no | yes | yes |
| Stock list filters | Expiration Alerts | same | same | Expired Lots, Alert Lots | same |
| Alert activity type | `product_expiry.mail_activity_type_alert_date_reached` | same | same | To-Do, summary Alert Date Reached | same |
| Finished product lot (MO) | `lot_producing_id` | same | same | `lot_producing_ids` | same |
| Menu: lots | Inventory ‣ Products ‣ Lots/Serial Numbers | same | Inventory ‣ Products ‣ Lots / Serial Numbers | same | same |
| Menu: categories | Inventory ‣ Configuration ‣ Products ‣ Product Categories | same | same | Inventory ‣ Configuration ‣ Products ‣ Categories | same |
| Nomenclature setting (Community) | Point of Sale | Point of Sale, Events | same | same | same |

The same in every version: Inventory ‣ Configuration ‣ Settings; Inventory ‣
Configuration ‣ Products ‣ Barcode Nomenclatures (developer mode); the lot's Location,
Transfers and Traceability buttons; the FEFO strategy `product_expiry.removal_fefo`; the
wizard `expiry.picking.confirmation`.

## Verify

```python
lot = env['stock.lot'].search([('product_id', '=', product.id), ('name', '=', 'LOT-0001')])
print(lot.read(['product_qty', 'expiration_date', 'use_date', 'removal_date', 'alert_date', 'product_expiry_alert']))
print(env['stock.quant'].search_read([('lot_id', '=', lot.id), ('location_id.usage', '=', 'internal')], ['location_id', 'quantity']))
print(company.nomenclature_id.parse_barcode('0105901234123457' + '10LOT-0001'))   # GS1: product and lot read apart
```

The lot holds the received quantity in stock, its dates follow the product's times, and
a FEFO delivery reserved the lot with the earliest removal date.

## Pitfalls

- Expiration fields stay hidden on an untracked product: track it first.
- New expiration times apply to new lots only; correct existing lots one by one.
- FEFO on a category nobody set leaves FIFO: deliveries ship fresh lots first.
- 16.0 still reserves expired lots: check the alert filter before delivering.
- Up to 18.0 a lot past its removal date but not yet expired is still reserved and
  delivered without warning; 19.0+ stop at the removal date.
- A lot name is unique per product and company: a second receipt with the same name adds
  to the same lot. A serial number takes one unit: receiving it twice is refused or
  warned about.
- Switching the company to the GS1 nomenclature with non-GTIN product barcodes makes
  scanners stop finding products.
