# mrp_account — Accounting - MRP

Depends on: mrp, stock_account.

## `account.move.line` (extends)


Extension points: `_get_invoiced_qty_per_product`

## `account.analytic.account` (extends)

Analytic Account

- `production_ids` Many2many → `mrp.production`
- `production_count` Integer “Manufacturing Orders Count” (compute=_compute_production_count)
- `bom_ids` Many2many → `mrp.bom`
- `bom_count` Integer “BoM Count” (compute=_compute_bom_count)
- `workcenter_ids` Many2many → `mrp.workcenter`
- `workorder_count` Integer “Work Order Count” (compute=_compute_workorder_count)

Public methods: `action_view_mrp_bom`, `action_view_mrp_production`, `action_view_workorder`

## `account.analytic.line` (extends)

- `category` Selection

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection

## `mrp.bom` (extends)

Inherits: `analytic.mixin`

- `analytic_distribution_text` Text (company_dependent)
- `analytic_distribution` Json
- `analytic_account_ids` Many2many → `account.analytic.account` (compute=_compute_analytic_account_ids)

## `mrp.production` (extends)

Inherits: `analytic.mixin`

- `extra_cost` Float “Extra Unit Cost”
- `show_valuation` Boolean (compute=_compute_show_valuation)
- `analytic_account_ids` Many2many → `account.analytic.account` (store, compute=_compute_analytic_account_ids)

Public methods: `action_view_analytic_accounts`, `action_view_stock_valuation_layers`, `write`

Extension points: `_check_analytic`, `_get_backorder_mo_vals`

## `mrp.routing.workcenter` (extends)


## `mrp.workcenter` (extends)

Inherits: `analytic.mixin`

- `costs_hour_account_ids` Many2many → `account.analytic.account` (store, compute=_compute_costs_hour_account_ids)

## `mrp.workorder` (extends)

- `mo_analytic_account_line_ids` Many2many → `account.analytic.line`
- `wc_analytic_account_line_ids` Many2many → `account.analytic.line`

Public methods: `action_cancel`, `unlink`

Extension points: `_create_or_update_analytic_entry`, `_prepare_analytic_line_values`

## `product.template` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

Extension points: `_get_product_accounts`

## `product.product` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

## `product.category` (extends)

- `property_stock_account_production_cost_id` Many2one → `account.account` (company_dependent)

Public methods: `write`

Extension points: `_get_stock_account_property_field_names`

## `stock.move` (extends)


Extension points: `_get_all_related_sm`, `_get_analytic_distribution`, `_get_dest_account`, `_get_src_account`

## `stock.rule` (extends)


Extension points: `_prepare_mo_vals`

## `report.mrp.report_mo_overview` (extends)


Extension points: `_get_unit_cost`
