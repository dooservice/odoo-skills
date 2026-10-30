# Project costs and profitability

A project collects its costs through its analytic account: the hours logged at each
employee's hourly cost, the purchase orders and vendor bills charged to it, the goods
delivered from stock for it and the components and work of its manufacturing orders. Up
to 19.0 the project's Updates view (Dashboard from 18.0) adds them up in a profitability
panel; in 20.0 Community the project shows its analytic items instead. Needs `project`
with `account` (Invoicing) and, for each source, `purchase`, `stock` or `mrp`; the bridge
modules (`project_account`, `project_purchase`, `project_stock`, `project_stock_account`,
`project_mrp`, `project_mrp_account`) install on their own. Creating the project, its
tasks and timesheets, and invoicing a customer is in `projects-and-timesheets.md`; sales
revenue in the panel comes from `sale_project` and `sale_timesheet` and is left to that
recipe. Budgets are Enterprise and left out.

**At a glance**

- Apps: `project`, `account`; `hr_timesheet`, `purchase`, `stock`, `mrp` for their costs;
  `project_account` 17.0+, `project_stock_account` and `project_mrp_account` 18.0+.
- Names that change by version: project analytic field `analytic_account_id` up to 17.0,
  `account_id` 18.0+; profitability in Project Updates up to 17.0, Dashboard 18.0 and
  19.0, Analytic Items 20.0; purchase linked by `analytic_distribution` up to 17.0,
  `purchase.order.project_id` 18.0+; transfers `project_id` + `analytic_costs` 18.0+;
  manufacturing order `analytic_account_id` 16.0, `analytic_distribution` 17.0,
  `project_id` 18.0+; hourly cost `hr_hourly_cost` up to 19.0, `hr` 20.0.
- Sections: Before you start; The standard flow (1 turn on analytic accounting, 2 give the
  project an analytic account, 3 set the hourly cost of each employee, 4 charge a purchase
  to the project, 5 charge goods from stock to the project (18.0+), 6 build for the
  project, 7 read the result); Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `project`, `account`; `hr_timesheet` for hours; `purchase`, `stock`, `mrp` for
  their costs. `project_account` exists from 17.0, `project_stock` and
  `project_stock_account` from 18.0, `project_mrp_account` from 18.0 (16.0, 17.0:
  `project_mrp` alone). `hr_hourly_cost` holds the employee's hourly cost up to 19.0; in
  20.0 the field is in `hr`.
- Settings: `group_analytic_accounting` (Invoicing ‣ Configuration ‣ Settings ‣
  Analytics, Analytic Accounting). Without it the analytic fields, the profitability
  panel's detail and the Analytic Items view stay hidden.
- Read first:

```python
print(env.ref('analytic.group_analytic_accounting') in env.ref('base.group_user').implied_ids)
print(env['project.project'].search_read([], ['name', 'account_id', 'allow_timesheets', 'company_id']))
print(env['hr.employee'].search_read([], ['name', 'hourly_cost', 'company_id']))
print(env['stock.picking.type'].search_read([('code', 'in', ['incoming', 'outgoing', 'mrp_operation'])], ['name', 'code', 'analytic_costs']))
```

This is 18.0+. In 16.0 and 17.0 read `analytic_account_id` instead of `account_id` and
drop the last line (`analytic_costs` does not exist).

## The standard flow

1. **Turn on analytic accounting.** Invoicing ‣ Configuration ‣ Settings ‣ Analytics,
   Analytic Accounting. Ask first: it shows analytic fields to every user.

   ```python
   env['res.config.settings'].create({'group_analytic_accounting': True}).execute()
   env.cr.commit()
   ```

2. **Give the project an analytic account.** Project ‣ open the project ‣ Settings tab,
   Analytic Account (`analytic_account_id` in 16.0, 17.0; `account_id` from 18.0).
   Turning on Timesheets on the project creates one named after it.

   ```python
   project = env['project.project'].browse(<project id>)
   if not project.account_id:
       project._create_analytic_account()
   account = project.account_id
   env.cr.commit()
   ```

   In 16.0 and 17.0 the field is `analytic_account_id`.

   Every cost below lands on this account; a project without one collects nothing.

3. **Set the hourly cost of each employee.** Employees ‣ open the employee ‣ HR Settings
   tab (Settings from 18.0) ‣ Hourly Cost.

   ```python
   employee = env['hr.employee'].browse(<employee id>)
   employee.hourly_cost = 40.0
   env.cr.commit()
   ```

   Each timesheet line logged afterwards gets `amount = -hours * hourly_cost`, in the
   employee's company currency. Lines logged before keep their amount until their hours,
   employee or account change.

4. **Charge a purchase to the project.** Purchase ‣ Orders ‣ Requests for Quotation ‣
   New. From 18.0 set Project (`project_id`, next to Source Document): every line takes
   the project's analytic distribution. In 16.0 and 17.0 set the Analytic column of each
   line to the project's account, or open the order from the project's Purchase Orders
   button, which fills it.

   18.0+:

   ```python
   po = env['purchase.order'].create({
       'partner_id': vendor.id, 'project_id': project.id,
       'order_line': [(0, 0, {'product_id': product.id, 'product_qty': 2, 'price_unit': 50.0})],
   })
   po.button_confirm()
   env.cr.commit()
   print(po.state, po.order_line.mapped('analytic_distribution'))
   ```

   16.0, 17.0:

   ```python
   po = env['purchase.order'].create({
       'partner_id': vendor.id,
       'order_line': [(0, 0, {'product_id': product.id, 'product_qty': 2, 'price_unit': 50.0,
                              'analytic_distribution': {str(account.id): 100}})],
   })
   po.button_confirm()
   env.cr.commit()
   ```

   Leaves the order `purchase`. The panel counts it as "to bill" until the vendor bill,
   which inherits the distribution, is posted; the bill's lines then post analytic lines
   on the account.

5. **Charge goods from stock to the project (18.0+).** Inventory ‣ Configuration ‣
   Operation Types ‣ Delivery Orders (or Receipts) ‣ Analytic Costs (`analytic_costs`),
   then on each transfer the Additional Info tab ‣ Project. The project's Tasks view
   shows From WH, To WH and Stock Moves at the top to list them.

   ```python
   delivery_type = env['stock.picking.type'].search([('code', '=', 'outgoing'), ('company_id', '=', project.company_id.id)], limit=1)
   delivery_type.analytic_costs = True
   src, dest = delivery_type.default_location_src_id, env.ref('stock.stock_location_customers')
   picking = env['stock.picking'].create({
       'picking_type_id': delivery_type.id, 'project_id': project.id, 'partner_id': project.partner_id.id,
       'location_id': src.id, 'location_dest_id': dest.id,
       'move_ids': [(0, 0, {'product_id': product.id, 'product_uom_qty': 1,
                            'location_id': src.id, 'location_dest_id': dest.id})],
   })
   picking.action_confirm()
   env.cr.commit()
   ```

   This is 19.0+. In 18.0 the move also needs `'name': product.display_name`.

   Validating the transfer (Validate, by the warehouse user) posts an analytic line of
   category `picking_entry` for the value of the goods; the panel shows it as Materials.
   Only transfers of an operation type with Analytic Costs count.

6. **Build for the project.** Manufacturing ‣ Operations ‣ Manufacturing Orders ‣ New.
   From 18.0 set Project on the Miscellaneous tab (a bill of materials with a Project
   fills it). In 16.0 set Analytic Account there to the project's account; in 17.0,
   Analytic Distribution.

   ```python
   mo = env['mrp.production'].create({'product_id': finished.id, 'product_qty': 1, 'bom_id': bom.id,
                                      'project_id': project.id})
   mo.action_confirm()
   env.cr.commit()
   ```

   This is 18.0+. In 17.0 pass `'analytic_distribution': {str(account.id): 100}` instead
   of `project_id`; in 16.0, `'analytic_account_id': account.id`.

   Leaves the order `confirmed`. Components consumed and work order time post analytic
   lines of category `manufacturing_order`, shown as Manufacturing Orders in the panel.
   In 20.0 the manufacturing operation type's Analytic Costs, on by default, must stay on.

7. **Read the result.** Up to 19.0: Project ‣ the project's kanban card ‣ Project Updates
   (Dashboard from 18.0); the right-hand panel lists costs and revenues by source, billed
   and to bill. 20.0: open the project and choose Analytic Items at the top (with
   Analytic Accounting on).

   ```python
   for line in env['account.analytic.line'].search([('account_id', '=', account.id)]):
       print(line.date, line.category, line.name, line.unit_amount, line.amount)
   ```

   In 16.0-19.0 also `print(project._get_profitability_items(with_action=False))` gives
   the panel's figures.

## Variations

- **Purchase from the project itself**: up to 17.0 the Purchase Orders button of the
  project panel; from 18.0 Purchase Orders at the top of the project's Tasks view. Both
  list orders whose lines carry the project's account or, from 18.0, whose Project is set.
- **Bills without a purchase order** (17.0+): a vendor bill line with the project's
  account in Analytic counts as a cost too, under Vendor Bills in the panel.
- **Projects in several plans**: from 18.0 a project holds one account per analytic plan
  (the plan's column on the project). The purchase line, transfer and manufacturing order
  take all of them; a plan marked mandatory for that document blocks validation until the
  project has an account in it.
- **Bills of materials per project (18.0+)**: Project on the bill of materials
  (Manufacturing ‣ Products ‣ Bills of Materials) sets it on every order made from it.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Project's analytic field | `analytic_account_id` | same | `account_id` (one column per plan) | same | same |
| Profitability panel | Project Updates | same, from `project_account` | Dashboard | same | none in Community: Analytic Items |
| Purchase linked by | line `analytic_distribution` | same | `purchase.order.project_id` | same | same |
| Stock transfers on the project | no | no | `project_id` + type `analytic_costs` | same | same, `analytic_costs` computed (off for receipts and deliveries) |
| Manufacturing order linked by | `analytic_account_id` | `analytic_distribution` | `project_id` (`project_mrp_account` for costs) | same | same, needs the type's `analytic_costs` (on by default) |
| Hourly cost field | `hr_hourly_cost` | same | same | same | `hr` |
| Hourly Cost tab | HR Settings | HR Settings | Settings | Settings | Settings |

## Verify

```python
project.invalidate_recordset()
account = project.account_id
totals = {}
for line in env['account.analytic.line'].search([('account_id', '=', account.id)]):
    totals[line.category] = totals.get(line.category, 0.0) + line.amount
print(project.name, account.name, totals)
print(project.purchase_orders_count)
```

This is 18.0+. In 16.0 and 17.0 use `project.analytic_account_id`.

## Pitfalls

- Costs appear only on the project's analytic account: a project without one (timesheets
  off and no account set) shows an empty panel. Set the account before the documents;
  documents created earlier keep their distribution.
- Changing an employee's hourly cost does not revalue past timesheets. To revalue them,
  edit their hours or employee from the interface, with the manager's yes.
- 18.0+: a transfer with a Project posts nothing until its operation type has Analytic
  Costs; in 20.0 this is off for receipts and deliveries by default.
- Stock valuation decides the amount of a transfer or manufacturing cost: a product
  without cost (`standard_price` 0) posts lines of amount 0. Check the product cost with
  the user.
- A mandatory analytic plan without an account on the project blocks confirming the
  manufacturing order (19.0+) or validating the transfer: set the plan's account on the
  project rather than turning the plan optional.
