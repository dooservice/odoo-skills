# Point of Sale: restaurants and bars

A restaurant shop is a POS shop (`pos.config`) with `module_pos_restaurant` set: its
orders hang on tables (`restaurant.table`) drawn on floors (`restaurant.floor`), the
waiter sends each round to preparation printers in the kitchen or the bar, prints the bill
before payment, splits it, and takes tips. Needs `point_of_sale` and `pos_restaurant`.
Shops, payment methods, sessions and closing are in [point-of-sale.md](point-of-sale.md);
printers as devices in [pos-hardware.md](pos-hardware.md); customers ordering by
themselves in [pos-self-order.md](pos-self-order.md). The preparation display (kitchen
screen), table booking (`pos_restaurant_appointment`) and the IoT box are Enterprise and
left out.

**At a glance**

- Apps: `point_of_sale` and `pos_restaurant`.
- Names that change by version: floor to shop `pos_config_id` in 16.0, `pos_config_ids`
  17.0+; table `name` up to 17.0, `table_number` 18.0+; `is_table_management` 16.0 only;
  preparation printer `restaurant.printer` in 16.0, `pos.printer` 17.0+
  (`use_type='preparation'` 20.0); shop printers `is_order_printer`, `printer_ids` up to
  19.0, `preparation_devices`, `preparation_printer_ids` 20.0; `iface_splitbill` up to
  19.0; take-out by fiscal position up to 17.0, `takeaway`, `takeaway_fp_id` 18.0, presets
  19.0+; courses 19.0+ (`pos.course` 20.0).
- Sections: Before you start; The standard flow (1 make the shop a restaurant, 2 draw the
  floors and tables, 3 preparation printers, 4 bill printing and splitting, 5 tips, 6
  serve); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `pos_restaurant`. Ticking Is a Bar/Restaurant on a shop installs it at once
  (`button_immediate_install`): install it beforehand with the user's yes and restart the
  shell.
- Tips by card with tip adjustment after payment: `pos_restaurant_adyen` (16.0 to 19.0;
  part of `pos_adyen` in 20.0), see [pos-hardware.md](pos-hardware.md).
- Settings: Point of Sale ‣ Configuration ‣ Settings, pick the shop. The restaurant
  switches are the shop's own fields, written below on `pos.config`. Most of them are
  refused while the shop has a session not closed.
- Read first:

```python
for c in env['pos.config'].search([('module_pos_restaurant', '=', True)]):
    floors = c.floor_ids
    print(c.id, c.name, c.current_session_state, floors.mapped('name'), len(floors.table_ids),
          c.iface_tipproduct, c.tip_product_id.name, c.set_tip_after_payment, c.iface_printbill,
          c.preparation_devices, c.preparation_printer_ids.mapped('name'))
```

That is 20.0; up to 19.0 the printers are `is_order_printer` and `printer_ids`.

## The standard flow

The order of Odoo's restaurant documentation: the restaurant shop, its floors and tables,
the preparation printers, then service: order, send to the kitchen, bill, split, tip, pay.

1. **Make the shop a restaurant.** Point of Sale ‣ Configuration ‣ Settings, section
   Restaurant Mode (17.0+; PoS Interface in 16.0) ‣ Is a Bar/Restaurant. From 18.0
   `load_onboarding_restaurant_scenario` and `load_onboarding_bar_scenario` create a
   ready restaurant or bar shop with its cash journal and payment methods.

   ```python
   config = env['pos.config'].create({'name': 'Example Restaurant', 'module_pos_restaurant': True})
   print(config.floor_ids.mapped('name'), config.floor_ids.table_ids.ids)
   env.cr.commit()
   ```

   An existing shop without open session takes `config.write({'module_pos_restaurant':
   True})`. Leaves a restaurant shop with one floor named after the company and one table
   (17.0+; in 16.0 floors start empty and need Floors & Tables Map,
   `is_table_management`).
   Payment methods are added as in [point-of-sale.md](point-of-sale.md), step 2.

2. **Draw the floors and tables.** In the POS: open the session, Floor screen ‣ the pencil
   (Edit Plan), add tables, set their seats, shape and position. Without a session:
   Point of Sale ‣ Configuration ‣ Floor Plans (developer mode in 16.0).

   18.0 to 20.0:

   ```python
   floor = env['restaurant.floor'].create({'name': 'Terrace', 'pos_config_ids': [(4, config.id)]})
   for number in range(1, 5):
       env['restaurant.table'].create({'floor_id': floor.id, 'table_number': number, 'seats': 4})
   print(floor.table_ids.mapped('display_name'))
   env.cr.commit()
   ```

   17.0:

   ```python
   floor = env['restaurant.floor'].create({'name': 'Terrace', 'pos_config_ids': [(4, config.id)]})
   for number in range(1, 5):
       env['restaurant.table'].create({'floor_id': floor.id, 'name': str(number), 'seats': 4})
   print(floor.table_ids.mapped('name'))
   env.cr.commit()
   ```

   16.0:

   ```python
   config.write({'is_table_management': True})
   floor = env['restaurant.floor'].create({'name': 'Terrace', 'pos_config_id': config.id})
   for number in range(1, 5):
       env['restaurant.table'].create({'floor_id': floor.id, 'name': str(number), 'seats': 4})
   print(floor.table_ids.mapped('name'))
   env.cr.commit()
   ```

   Leaves the floor in the shop's floor screen. A table's place on the plan is easier to
   set in the POS editor than by script (`position_h`, `position_v`, `width`, `height`
   up to 19.0; `floor_plan_layout` in 20.0).

3. **Preparation printers.** Create the printer (device setup in
   [pos-hardware.md](pos-hardware.md)) with the POS categories it prints, then tick it in
   the shop: Settings, Preparation Printers (17.0+; Kitchen Printers in 16.0).

   20.0:

   ```python
   printer = env['pos.printer'].create({
       'name': 'Kitchen',
       'use_type': 'preparation',
       'printer_type': 'epson_epos',
       'printer_ip': '<printer IP>',
       'product_categories_ids': [(6, 0, kitchen_categories.ids)],
   })
   config.write({'preparation_devices': True, 'preparation_printer_ids': [(4, printer.id)]})
   env.cr.commit()
   ```

   17.0 to 19.0 (the `epson_epos` type needs `pos_epson_printer` in 17.0 and 18.0):

   ```python
   printer = env['pos.printer'].create({
       'name': 'Kitchen',
       'printer_type': 'epson_epos',
       'epson_printer_ip': '<printer IP>',
       'product_categories_ids': [(6, 0, kitchen_categories.ids)],
   })
   config.write({'is_order_printer': True, 'printer_ids': [(4, printer.id)]})
   env.cr.commit()
   ```

   16.0: the same with `env['restaurant.printer']` (the `epson_epos` type needs
   `pos_epson_printer_restaurant`).

   Leaves the shop sending each new or changed line to the printers of its POS category
   when the waiter presses Order. The printers list is Point of Sale ‣ Orders ‣
   Preparation Printers (17.0 to 19.0, shown once a shop uses one), Point of Sale ‣
   Configuration ‣ Printers (20.0), Configuration ‣ Order Printers (16.0, developer mode).

4. **Bill printing and splitting.** Settings: Early Receipt Printing (`iface_printbill`)
   prints the bill before payment; Allow Bill Splitting (`iface_splitbill`, 16.0 to 19.0;
   always on in 20.0) pays some lines or guests apart.

   20.0: write `iface_printbill` alone.

   16.0 to 19.0:

   ```python
   config.write({'iface_printbill': True, 'iface_splitbill': True})
   env.cr.commit()
   ```

5. **Tips.** Settings, section Payment ‣ Tips (`iface_tipproduct`) with the tip product
   (`tip_product_id`, the `TIPS` service product by default). The cashier adds the tip on
   the payment screen; it becomes an order line of that product.

   ```python
   config.write({'iface_tipproduct': True})
   print(config.tip_product_id.display_name)
   env.cr.commit()
   ```

   Variation: Add tip after payment (`set_tip_after_payment`, needs tips on): the card is
   authorized, the tip is set later from the POS orders list, and the terminal captures
   the final amount (Adyen, see [pos-hardware.md](pos-hardware.md)).

6. **Serve.** In the POS: open the session (see [point-of-sale.md](point-of-sale.md)),
   pick the table, set the guests, add the products, press Order to send the round to the
   preparation printers, print the bill, split or pay, add the tip. A paid order frees the
   table.

   ```python
   orders = env['pos.order'].search([('config_id', '=', config.id), ('session_id.state', '=', 'opened')])
   print(orders.mapped(lambda o: (o.name, o.table_id.display_name, o.customer_count, o.state, o.tip_amount)))
   ```

   Leaves each paid order `paid` with its `table_id` and guests (`customer_count`), and,
   when tipped, `is_tipped` and `tip_amount`. Close the session as in
   [point-of-sale.md](point-of-sale.md).

## Variations

- **Eat in or take out at another tax rate.** 18.0: Settings ‣ Eat in / Take out
  (`takeaway`) with the take-out fiscal position (`takeaway_fp_id`); prices must include
  taxes. 19.0+: presets (`pos.preset`, Point of Sale ‣ Configuration ‣ Presets): each
  preset carries a pricelist, a fiscal position and the identification it asks
  (`identification`: `none`, `name`, `address`); turn them on with `use_presets` and
  `available_preset_ids`, the one proposed first in `default_preset_id`. 16.0, 17.0: let
  the cashier pick the fiscal position (`tax_regime_selection`, see
  [point-of-sale.md](point-of-sale.md)). Presets, 19.0 and 20.0:

  ```python
  eat_in = env['pos.preset'].create({'name': 'Eat in'})
  take_out = env['pos.preset'].create({'name': 'Take out', 'fiscal_position_id': take_out_fp.id, 'identification': 'name'})
  config.write({'use_presets': True, 'available_preset_ids': [(6, 0, (eat_in | take_out).ids)], 'default_preset_id': eat_in.id})
  env.cr.commit()
  ```

- **A bar without floor screen.** 19.0+: Settings ‣ Default Screen (`default_screen`):
  `register` opens on the order screen; `tables` (default) on the floor plan.
- **Courses.** 19.0: the waiter groups lines into courses in the POS and fires them one by
  one (`restaurant.order.course`). 20.0: define the courses in Point of Sale ‣
  Configuration ‣ Products ‣ Courses (`pos.course`, linked to POS categories), and tick
  Enable Course Allocation (`use_course_allocation`) to place lines by category.
- **Internal notes for the kitchen.** 16.0, 17.0: Internal Notes
  (`iface_orderline_notes`). 18.0+: always on, with ready notes in Point of Sale ‣
  Configuration ‣ Note Models.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| New shop is a restaurant once `pos_restaurant` is installed | yes (default) | yes (default) | no | no | no |
| Floor to shop | `pos_config_id` | `pos_config_ids` | `pos_config_ids` | `pos_config_ids` | `pos_config_ids` |
| Table identifier | `name` | `name` | `table_number` | `table_number` | `table_number` |
| Default floor and table at creation | no | yes | yes | yes | yes |
| Floors map switch | `is_table_management` | always | always | always | always |
| Preparation printer model | `restaurant.printer` | `pos.printer` | `pos.printer` | `pos.printer` | `pos.printer`, `use_type='preparation'` |
| Shop printer fields | `is_order_printer`, `printer_ids` | same | same | same | `preparation_devices`, `preparation_printer_ids` |
| Bill splitting | `iface_splitbill` | same | same | same | always on |
| Take-out taxes | fiscal position choice | same | `takeaway`, `takeaway_fp_id` | presets | presets |
| Tip after payment field | `pos_restaurant` | same | same | same | `point_of_sale` |
| Courses | no | no | no | in the POS | `pos.course` |

## Verify

```python
config = env['pos.config'].browse(<shop id>)
print(config.module_pos_restaurant, [(f.name, f.table_ids.mapped('display_name')) for f in config.floor_ids])
orders = env['pos.order'].search([('config_id', '=', config.id)], order='id desc', limit=5)
print([(o.name, o.table_id.display_name, o.state, o.amount_total, o.tip_amount) for o in orders])
```

Then ask a waiter to open a table, send a round, check the ticket comes out at the right
printer, split the bill and pay it.

## Pitfalls

- 16.0, 17.0: once `pos_restaurant` is installed every new shop is created as a
  restaurant; pass `'module_pos_restaurant': False` for a retail shop.
- A shop with an open session refuses `floor_ids` and the restaurant switch: close the
  session first.
- Unticking Is a Bar/Restaurant (Floors & Tables Map in 16.0) unlinks every floor from
  the shop; link them again after turning it back on.
- A product whose POS category is in no printer's `product_categories_ids` never reaches
  the kitchen: check every category is covered.
- An Epson printer reached over plain HTTP from an HTTPS POS is blocked by the browser:
  see [pos-hardware.md](pos-hardware.md).
- Turning Tips off clears `tip_product_id` and `set_tip_after_payment`.
