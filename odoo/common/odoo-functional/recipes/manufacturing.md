# Manufacturing

Making products from components with the Manufacturing app (`mrp`). A bill of materials
(`mrp.bom`) says what a product is made of; a manufacturing order (`mrp.production`)
consumes components and produces the product through stock moves (`inventory.md`).
Master production schedule, PLM, quality and the shop floor are Enterprise and left out.
A done order is history: undo it with an unbuild order, never by editing its moves.

## Before you start

- Apps: `mrp`; `purchase_stock` for the Buy route of components.
- Settings: `group_mrp_routings` (work orders and work centers), `group_mrp_byproducts`,
  `group_unlocked_by_default`. `module_mrp_subcontracting` installs a module: only with
  the user's yes. `module_mrp_mps` and `module_mrp_plm` are Enterprise.
- Read first:

```python
company = env.company
warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
product = env['product.product'].search([('default_code', '=', '<reference>')], limit=1)
env['mrp.bom'].search_read([('product_tmpl_id', '=', product.product_tmpl_id.id)], ['type', 'product_id', 'product_qty', 'company_id', 'sequence', 'active'])
env['mrp.bom.line'].search_read([('bom_id.product_tmpl_id', '=', product.product_tmpl_id.id)], ['bom_id', 'product_id', 'product_qty'])
product.route_ids.mapped('name'), warehouse.read(['manufacture_steps', 'manufacture_to_resupply'])
env['mrp.production'].search_read([('product_id', '=', product.id), ('state', 'not in', ['done', 'cancel'])], ['name', 'state', 'product_qty', 'bom_id'])
env['mrp.workcenter'].search_read([('company_id', 'in', [company.id, False])], ['name', 'costs_hour', 'time_efficiency'])
```

## The standard flow

The menus below are the same in 16.0 to 20.0.

1. **Turn on work orders and by-products, if used.** Manufacturing ‣ Configuration ‣ Settings.

   ```python
   env['res.config.settings'].create({'group_mrp_routings': True, 'group_mrp_byproducts': True}).execute()
   env.cr.commit()
   ```

2. **Make the product manufacturable.** 16.0 to 18.0: Manufacturing ‣ Products ‣ Products,
   tab Inventory, Routes, tick Manufacture. New products get Buy by default, and Buy
   (route `sequence` 5) wins over Manufacture (10): take Buy off a product you make.

   ```python
   from odoo import Command
   manufacture = env.ref('mrp.route_warehouse0_manufacture')
   buy = env.ref('purchase_stock.route_warehouse0_buy')
   finished.product_tmpl_id.write({'route_ids': [Command.unlink(buy.id), Command.link(manufacture.id)]})
   env.cr.commit()
   ```

   19.0 and 20.0: no product step. Manufacture and Buy are routes of the warehouse
   (`manufacture_to_resupply`, `buy_to_resupply`, on by default), not selectable on a
   product (20.0 refuses the write above). A product with a bill of materials is
   manufactured, even when it also has a vendor price.

3. **Create the bill of materials.** Manufacturing ‣ Products ‣ Bills of Materials, New.

   ```python
   from odoo import Command
   bom = env['mrp.bom'].create({
       'product_tmpl_id': finished.product_tmpl_id.id, 'product_qty': 1, 'type': 'normal', 'company_id': company.id,
       'bom_line_ids': [
           Command.create({'product_id': component_a.id, 'product_qty': 4}),
           Command.create({'product_id': component_b.id, 'product_qty': 1}),
       ],
   })
   env.cr.commit()
   ```

   Line quantities are per `product_qty` units. `product_id` limits the bill to one
   variant; `company_id` empty shares it; the first bill by `sequence` wins.

4. **Operations, with work orders on.** Work centers in Manufacturing ‣ Configuration ‣
   Work Centers; operations in the bill's Operations tab. Each becomes a work order.

   ```python
   workcenter = env['mrp.workcenter'].create({'name': 'Assembly', 'costs_hour': 40, 'company_id': company.id})
   bom.write({'operation_ids': [Command.create({'name': 'Assemble', 'workcenter_id': workcenter.id, 'time_cycle_manual': 30})]})
   env.cr.commit()
   ```

5. **Create and confirm the order.** Manufacturing ‣ Operations ‣ Manufacturing Orders,
   New, Confirm; then Check availability (Reserve in 20.0).

   ```python
   mo = env['mrp.production'].create({'product_id': finished.id, 'bom_id': bom.id, 'product_qty': 5})
   mo.action_confirm()
   mo.action_assign()
   print(mo.name, mo.state, mo.reservation_state, [(m.product_id.display_name, m.product_uom_qty) for m in mo.move_raw_ids])
   env.cr.commit()
   ```

   Leaves the order `confirmed`; components are reserved when `reservation_state` is
   `assigned`. If not, ask before producing (stock would go negative).

6. **Do the work orders.** Work Orders tab, Start then Done on each.

   ```python
   for workorder in mo.workorder_ids:
       workorder.button_start()
       workorder.button_finish()
   env.cr.commit()
   ```

   Leaves the work orders `done` and the order `to_close`.

7. **Produce.** Mark as Done (16.0), Produce All (17.0 to 19.0), Produce (20.0).

   ```python
   res = mo.button_mark_done()
   if isinstance(res, dict) and res.get('res_model') == 'mrp.immediate.production':
       res = env['mrp.immediate.production'].with_context(res['context']).create({}).process()
   env.cr.commit()
   ```

   Leaves the order `done`, whole quantity produced (16.0 confirms through the wizard
   of the second line). If `res` is still a wizard (consumption differs, backorder, lots
   or serials), stop and show it to the user.

## Variations

- **Kit** (`type='phantom'`): never manufactured; selling or delivering it moves its
  components, and its available quantity is computed from theirs.
- **By-products**: `'byproduct_ids': [Command.create({'product_id': p.id, 'product_qty': 1})]` on the bill.
- **Replenished orders**: a reordering rule (`inventory.md`) or make to order creates
  the orders, through the routes of step 2.
- **Picking steps**: warehouse `manufacture_steps` (Inventory ‣ Configuration ‣ Warehouse
  Management ‣ Warehouses): `mrp_one_step`, `pbm` (pick, then manufacture), `pbm_sam`
  (pick, manufacture, store).
- **Undo a done order**, with the user's yes: Manufacturing ‣ Operations ‣ Unbuild Orders,
  `env['mrp.unbuild'].create({'mo_id': mo.id, 'product_id': mo.product_id.id, 'product_qty': mo.product_qty}).action_unbuild()`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Manufacture route | on product | on product | on product | warehouse | warehouse |
| Unit on bill and lines | `product_uom_id` | same | same | same | `uom_id` |
| `consumption` on bill (`flexible`, `warning`, `strict`) | yes | yes | yes | yes | no |
| `produce_delay`, `days_to_prepare_mo` | product | bill | bill | bill | bill |
| company `manufacturing_lead` | yes | yes | yes | no | no |
| `group_mrp_workorder_dependencies`, `group_mrp_reception_report` | yes | yes | yes | yes | no |
| produce button | Mark as Done (+ wizard) | Produce All | Produce All | Produce All | Produce |

## Verify

```python
print(mo.state, finished.qty_available, component_a.qty_available, component_b.qty_available)
print([(m.product_id.display_name, m.state, m.location_id.complete_name, m.location_dest_id.complete_name) for m in mo.move_raw_ids | mo.move_finished_ids])
```

`done`; the product rose by the order quantity, each component fell by line quantity ×
order quantity; all moves `done`, stock → production for components and back for the product.

## Pitfalls

- 16.0 to 18.0: replenishment buys instead of manufacturing while the product keeps
  Buy. Take Buy off (step 2).
- Changing a bill does not change confirmed orders: they keep their components. Ask
  before changing a bill with open orders; archive an old bill (`active=False`) rather
  than delete it.
