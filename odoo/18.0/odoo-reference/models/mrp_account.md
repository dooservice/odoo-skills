# mrp_account — Accounting - MRP

Depends on: mrp, stock_account.

## `account.move` (extends)

- `wip_production_ids` Many2many → `mrp.production` “Relevant WIP MOs”
- `wip_production_count` Integer “Manufacturing Orders Count” (compute=_compute_wip_production_count)

Public methods: `action_view_wip_production`

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

## `mrp.production` (extends)

- `extra_cost` Float “Extra Unit Cost”
- `show_valuation` Boolean (compute=_compute_show_valuation)

Public methods: `action_view_stock_valuation_layers`, `button_mark_done`, `write`

Extension points: `_get_backorder_mo_vals`, `_post_labour`

## `mrp.routing.workcenter` (extends)


## `mrp.workcenter` (extends)

Inherits: `analytic.mixin`

- `costs_hour_account_ids` Many2many → `account.analytic.account` (store, compute=_compute_costs_hour_account_ids)
- `expense_account_id` Many2one → `account.account` “Expense Account”

## `mrp.workcenter.productivity` (extends)

- `account_move_line_id` Many2one → `account.move.line`

## `mrp.workorder` (extends)

- `mo_analytic_account_line_ids` Many2many → `account.analytic.line`
- `wc_analytic_account_line_ids` Many2many → `account.analytic.line`

Public methods: `action_cancel`, `unlink`

Extension points: `_create_or_update_analytic_entry`, `_create_or_update_analytic_entry_for_record`, `_prepare_analytic_line_values`

## `product.template` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

Extension points: `_get_product_accounts`

## `product.product` (extends)


Public methods: `action_bom_cost`, `button_bom_cost`

## `product.category` (extends)

- `property_stock_account_production_cost_id` Many2one → `account.account` (company_dependent)

Extension points: `_get_stock_account_property_field_names`

## `stock.move` (extends)


Extension points: `_get_all_related_sm`, `_get_dest_account`, `_get_src_account`

## `report.mrp.report_mo_overview` (extends)


Extension points: `_get_unit_cost`

## `mrp.account.wip.accounting.line` (defines)

Account move line to be created when posting WIP account move

- `account_id` Many2one → `account.account`
- `label` Char “Label”
- `debit` Monetary “Debit” (store, compute=_compute_debit)
- `credit` Monetary “Credit” (store, compute=_compute_credit)
- `currency_id` Many2one → `res.currency`
- `wip_accounting_id` Many2one → `mrp.account.wip.accounting`

## `mrp.account.wip.accounting` (defines)

Wizard to post Manufacturing WIP account move

- `date` Date “Date”
- `reversal_date` Date “Reversal Date” (required, store, compute=_compute_reversal_date)
- `journal_id` Many2one → `account.journal` (required)
- `reference` Char “Reference”
- `line_ids` One2many → `mrp.account.wip.accounting.line` (store, compute=_compute_line_ids)
- `mo_ids` Many2many → `mrp.production`

Public methods: `confirm`, `default_get`

Extension points: `_get_line_vals`, `_get_overhead_account`
