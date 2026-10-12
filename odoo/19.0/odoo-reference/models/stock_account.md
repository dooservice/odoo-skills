# stock_account — WMS Accounting

Depends on: stock, account.

## `account.account` (extends)

- `account_stock_variation_id` Many2one → `account.account` “Variation Account”
- `account_stock_expense_id` Many2one → `account.account` “Expense Account”

## `account.chart.template` (extends)


Extension points: `_get_stock_account_account`, `_get_stock_account_journal`, `_get_stock_account_res_company`, `_get_stock_template_data`

## `account.move` (extends)

- `stock_move_ids` One2many → `stock.move` “Stock Move”

Public methods: `button_cancel`, `button_draft`, `copy_data`

Extension points: `_get_anglo_saxon_price_ctx`, `_get_invoiced_lot_values`, `_get_lines_onchange_currency`

## `account.move.line` (extends)

- `cogs_origin_id` Many2one → `account.move.line`

Extension points: `_get_cogs_qty`, `_get_cogs_value`, `_get_gross_unit_price`, `_get_lines_from_original_invoice`, `_get_posted_cogs_value`, `_get_stock_moves`

## `account.analytic.plan` (extends)


## `account.analytic.account` (extends)


## `product.template` (extends)

- `cost_method` Selection “Cost Method” (compute=_compute_cost_method)
- `valuation` Selection “Valuation” (compute=_compute_valuation)
- `lot_valuated` Boolean “Valuation by Lot/Serial” (store, compute=_compute_lot_valuated)
- `property_price_difference_account_id` Many2one → `account.account` (company_dependent)

Public methods: `get_product_accounts`, `write`

Extension points: `_get_price_diff_account`, `_get_product_accounts`

## `product.product` (extends)

- `avg_cost` Monetary “Average Cost” (compute=_compute_value)
- `total_value` Monetary “Total Value” (compute=_compute_value)
- `company_currency_id` Many2one → `res.currency` (compute=_compute_value)

Public methods: `create`, `write`

Extension points: `_get_last_in`, `_get_last_product_value`, `_get_moves_with_manual_value`, `_get_remaining_moves`, `_get_standard_price_at_date`, `_get_value_from_lots`

## `product.category` (extends)

- `anglo_saxon_accounting` Boolean “Use Anglo-Saxon Accounting” (compute=_compute_anglo_saxon_accounting)
- `property_valuation` Selection “Inventory Valuation” (company_dependent)
- `property_cost_method` Selection “Costing Method” (company_dependent)
- `property_stock_journal` Many2one → `account.journal` (company_dependent)
- `property_stock_valuation_account_id` Many2one → `account.account` (company_dependent)
- `property_price_difference_account_id` Many2one → `account.account` (company_dependent)
- `account_stock_variation_id` Many2one → `account.account` “Stock Variation Account” (related=property_stock_valuation_account_id.account_stock_variation_id)

Public methods: `write`

## `product.value` (defines)

Product Value

- `product_id` Many2one → `product.product` “Product” (index)
- `lot_id` Many2one → `stock.lot` “Lot”
- `move_id` Many2one → `stock.move` “Move”
- `value` Monetary “Value” (required)
- `company_id` Many2one → `res.company` “Company” (required, store, compute=_compute_company_id)
- `currency_id` Many2one → `res.currency` “Currency” (related=company_id.currency_id)
- `date` Datetime “Date” (required)
- `user_id` Many2one → `res.users` “User” (required)
- `description` Char “Description”
- `current_value` Monetary “Current Value” (related=move_id.value)
- `current_value_details` Char “Current Value Details” (compute=_compute_current_value_details)
- `current_value_description` Text “Current Value Description” (compute=_compute_value_description)
- `computed_value_description` Text “Computed Value Description” (compute=_compute_value_description)

Public methods: `create`

## `res.company` (extends)

- `account_stock_journal_id` Many2one → `account.journal` “Stock Journal”
- `account_stock_valuation_id` Many2one → `account.account` “Stock Valuation Account”
- `account_production_wip_account_id` Many2one → `account.account` “Production WIP Account”
- `account_production_wip_overhead_account_id` Many2one → `account.account` “Production WIP Overhead Account”
- `inventory_period` Selection “Inventory Period” (required)
- `inventory_valuation` Selection “Valuation”
- `cost_method` Selection “Cost Method” (required)

Public methods: `action_close_stock_valuation`, `stock_accounting_value`, `stock_value`

Extension points: `_action_close_stock_valuation`, `_get_accounts_by_product`, `_get_continental_realtime_variation_vals`, `_get_extra_balance`, `_get_last_closing_date`, `_get_location_valuation_vals`, `_get_stock_valuation_account_vals`, `_get_valuation_product_domain`, `_prepare_inventory_aml_vals`

## `res.config.settings` (extends)

- `module_stock_landed_costs` Boolean “Landed Costs”
- `group_lot_on_invoice` Boolean “Display Lots & Serial Numbers on Invoices”

## `stock.location` (extends)

- `valuation_account_id` Many2one → `account.account`
- `is_valued_internal` Boolean “Is valued inside the company” (compute=_compute_is_valued)
- `is_valued_external` Boolean “Is valued outside the company” (compute=_compute_is_valued)

## `stock.lot` (extends)

- `lot_valuated` Boolean (readonly, related=product_id.lot_valuated)
- `avg_cost` Monetary “Average Cost” (readonly, compute=_compute_value)
- `total_value` Monetary “Total Value” (compute=_compute_value)
- `company_currency_id` Many2one → `res.currency` (compute=_compute_value)
- `standard_price` Float “Cost” (company_dependent)

Public methods: `create`, `write`

## `stock.move` (extends)

- `to_refund` Boolean “Update quantities on SO/PO”
- `company_currency_id` Many2one → `res.currency` “Company Currency” (readonly, related=company_id.currency_id)
- `value` Monetary “Value”
- `value_justification` Text “Value Description” (compute=_compute_value_justification)
- `value_computed_justification` Text “Computed Value Description” (compute=_compute_value_justification)
- `value_manual` Monetary “Manual Value” (compute=_compute_value_manual)
- `standard_price` Float “Standard Price” (compute=_compute_standard_price)
- `price_unit` Float “Price Unit”
- `is_in` Boolean “Is Incoming (valued)” (store, compute=_compute_is_in)
- `is_out` Boolean “Is Outgoing (valued)” (store, compute=_compute_is_out)
- `is_dropship` Boolean “Is Dropship” (store, compute=_compute_is_dropship)
- `is_valued` Boolean “Is Valued” (compute=_compute_is_valued)
- `remaining_qty` Float “Remaining Quantity” (compute=_compute_remaining_qty)
- `remaining_value` Monetary “Remaining Value” (compute=_compute_remaining_value)
- `analytic_account_line_ids` Many2many → `account.analytic.line`
- `account_move_id` Many2one → `account.move`

Public methods: `action_adjust_valuation`, `create`, `search_remaining_qty`

Extension points: `_action_done`, `_create_account_move`, `_create_analytic_move`, `_get_account_move_line_vals`, `_get_aml_value`, `_get_analytic_distribution`, `_get_cogs_price_unit`, `_get_in_move_lines`, `_get_manual_value`, `_get_move_directions`, `_get_out_move_lines`, `_get_partner_id_for_valuation_lines`, `_get_price_unit`, `_get_price_unit_delivery`, `_get_price_unit_dropshipped`, `_get_related_invoices`, `_get_value`, `_get_value_data`, `_get_value_from_account_move`, `_get_value_from_extra`, `_get_value_from_production`, `_get_value_from_quotation`, `_get_value_from_returns`, `_get_value_from_std_price`, `_get_valued_consigned_qty`, `_get_valued_qty`, `_get_valued_types`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`

## `stock.move.line` (extends)


Public methods: `create`, `unlink`, `write`

## `stock.picking` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)

Extension points: `_check_backdate_allowed`

## `stock.picking.type` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)

## `stock.quant` (extends)

- `value` Monetary “Value” (compute=_compute_value)
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `accounting_date` Date “Accounting Date”
- `cost_method` Selection “Cost Method” (compute=_compute_cost_method)

Extension points: `_get_inventory_fields_write`, `_get_inventory_move_values`

## `stock.avco.report` (defines)

Stock AVCO Justifier

- `date` Date “Date” (required)
- `user_id` Many2one → `res.users` “User” (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `currency_id` Many2one → `res.currency` “Currency” (related=company_id.currency_id)
- `product_id` Many2one → `product.product` “Product” (required)
- `reference` Char “Reference” (required)
- `description` Text “Description” (required)
- `res_model_name` Selection “Resource Model Name” (required)
- `quantity` Float “Added Quantity” (required)
- `value` Float “Value” (required)
- `added_value` Float “Added Value” (compute=_compute_cumulative_fields)
- `total_quantity` Float “Total Quantity” (compute=_compute_cumulative_fields)
- `total_value` Float “Total Value” (compute=_compute_cumulative_fields)
- `avco_value` Float “AVCO Value” (compute=_compute_cumulative_fields)
- `justification` Text “Justification” (compute=_compute_justification)

Public methods: `init`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`

## `stock_account.stock.valuation.report` (defines)

Stock Valuation


Public methods: `action_print_as_pdf`, `action_print_as_xlsx`, `get_report_values`

Extension points: `_get_report_data`, `_get_report_values`

## `stock.inventory.adjustment.name` (extends)

- `accounting_date` Date “Accounting Date”
- `should_show_accounting_date` Boolean (compute=_compute_should_show_accounting_date)

Extension points: `_get_quants_context`

## `stock.return.picking.line` (extends)

- `to_refund` Boolean “Update quantities on SO/PO”

Extension points: `_prepare_move_default_values`
