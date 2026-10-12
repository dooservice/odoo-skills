# mrp_account — Accounting - MRP

Depends on: mrp, stock_account.

## `account.move.line` (extends)


Extension points: `_get_invoiced_qty_per_product`

## `account.analytic.account` (extends)

Analytic Account

- `production_ids` One2many → `mrp.production` “Manufacturing Orders”
- `production_count` Integer “Manufacturing Orders Count” (compute=_compute_production_count)
- `bom_ids` One2many → `mrp.bom` “Bills of Materials”
- `bom_count` Integer “BoM Count” (compute=_compute_bom_count)
- `workcenter_ids` One2many → `mrp.workcenter` “Workcenters”
- `workorder_count` Integer “Work Order Count” (compute=_compute_workorder_count)

Public methods: `action_view_mrp_bom`, `action_view_mrp_production`, `action_view_workorder`

## `account.analytic.line` (extends)

- `category` Selection

## `mrp.bom` (extends)

- `analytic_account_id` Many2one → `account.analytic.account` (company_dependent)

## `mrp.workcenter.productivity` (extends)

- `cost_already_recorded` Boolean “Cost Recorded”

## `mrp.production` (extends)

- `extra_cost` Float “Extra Unit Cost”
- `show_valuation` Boolean (compute=_compute_show_valuation)
- `analytic_account_id` Many2one → `account.analytic.account` (store, compute=_compute_analytic_account_id)

Public methods: `action_view_analytic_account`, `action_view_stock_valuation_layers`, `write`

Extension points: `_get_backorder_mo_vals`

## `mrp.routing.workcenter` (extends)


## `mrp.workcenter` (extends)

- `costs_hour_account_id` Many2one → `account.analytic.account` “Analytic Account”

## `mrp.workorder` (extends)

- `mo_analytic_account_line_id` Many2one → `account.analytic.line`
- `wc_analytic_account_line_id` Many2one → `account.analytic.line`

Public methods: `action_cancel`, `unlink`

Extension points: `_create_or_update_analytic_entry`, `_prepare_analytic_line_values`

## `product.template` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

## `product.product` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

## `stock.move` (extends)


Extension points: `_get_analytic_account`, `_get_dest_account`, `_get_src_account`

## `stock.rule` (extends)


Extension points: `_prepare_mo_vals`
