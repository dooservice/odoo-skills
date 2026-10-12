# stock_account — WMS Accounting

Depends on: stock, account.

## `account.move` (extends)

- `stock_move_ids` One2many → `stock.move` “Stock Move”
- `closing_datetime` Datetime “Closing Date”
- `product_value_id` One2many → `product.value`

Public methods: `action_show_product_value`, `button_cancel`, `button_draft`, `copy_data`

Extension points: `_get_invoiced_lot_values`, `_get_lines_onchange_currency`

## `account.move.line` (extends)

- `stock_move_id` Many2one → `stock.move`
- `cogs_move_ids` Many2many → `stock.move` “COGS stock moves” (compute=_compute_cogs_move_ids)

Extension points: `_get_cogs_qty`, `_get_cogs_value`

## `account.analytic.plan` (extends)


## `account.analytic.account` (extends)


## `product.template` (extends)

- `cost_method` Selection
- `lot_valuated` Boolean “Valuation by Lot/Serial” (store, compute=_compute_lot_valuated)

Public methods: `write`

## `product.product` (extends)

- `avg_cost` Monetary “Average Cost” (compute=_compute_value)
- `total_value` Monetary “Total Value” (compute=_compute_value)
- `company_currency_id` Many2one → `res.currency` (compute=_compute_value)

Public methods: `create`, `write`

Extension points: `_get_fifo_stack`, `_get_fifo_value`, `_get_last_in`, `_get_last_product_value`, `_get_remaining_moves`, `_get_std_price_history_by_product`, `_get_stock_moves_with_valuation_by_product`

## `product.category` (extends)

- `property_cost_method` Selection
- `anglo_saxon_accounting` Boolean “Use Anglo-Saxon Accounting” (compute=_compute_anglo_saxon_accounting)

Public methods: `write`

## `product.value` (defines)

Product Value

- `product_id` Many2one → `product.product` “Product” (index)
- `product_tracking` Selection (related=product_id.tracking)
- `lot_id` Many2one → `stock.lot` “Lot”
- `move_id` Many2one → `stock.move` “Move”
- `quantity` Float “Quantity”
- `old_cost` Float “Old Unit Cost”
- `new_cost` Float “New Unit Cost”
- `old_value` Monetary “Old Value”
- `new_value` Monetary “New Value”
- `adjustment` Monetary “Adjustment” (compute=_compute_adjustment)
- `value` Monetary “Value” (required)
- `company_id` Many2one → `res.company` “Company” (required, store, index, compute=_compute_company_id)
- `currency_id` Many2one → `res.currency` “Currency” (related=company_id.currency_id)
- `date` Datetime “Date” (required)
- `user_id` Many2one → `res.users` “User” (required)
- `description` Char “Description”
- `current_value` Monetary “Current Value” (related=move_id.value)
- `current_value_details` Char “Current Value Details” (compute=_compute_current_value_details)
- `current_value_description` Text “Current Value Description” (compute=_compute_value_description)
- `computed_value_description` Text “Computed Value Description” (compute=_compute_value_description)
- `account_move_id` Many2one → `account.move` “Account Move”

Public methods: `action_open_account_move`, `create`

## `res.company` (extends)

- `account_production_wip_account_id` Many2one → `account.account` “Production WIP Account”
- `account_production_wip_overhead_account_id` Many2one → `account.account` “Production WIP Overhead Account”
- `cost_method` Selection

Public methods: `get_inventory_value`, `use_stock_account`, `write`

Extension points: `_get_closing_date_field`, `_get_closing_move_extra_aml_vals`, `_get_closing_move_extra_vals`, `_get_inventory_valuation_products`, `_get_last_closing_date`, `_get_location_valuation_vals`

## `res.config.settings` (extends)

- `module_stock_landed_costs` Boolean “Landed Costs”
- `group_lot_on_invoice` Boolean “Display Lots & Serial Numbers on Invoices”

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `stock.location` (extends)

- `valuation_account_id` Many2one → `account.account`
- `is_valued` Boolean “Is valued inside the company” (compute=_compute_is_valued)

## `stock.lot` (extends)

- `lot_valuated` Boolean (readonly, related=product_id.lot_valuated)
- `avg_cost` Monetary “Average Cost” (readonly, compute=_compute_value)
- `total_value` Monetary “Total Value” (compute=_compute_value)
- `company_currency_id` Many2one → `res.currency` (compute=_compute_value)
- `standard_price` Float “Cost” (company_dependent)

Public methods: `create`, `write`

## `stock.move` (extends)

- `cogs_aml_ids` Many2many → `account.move.line` “COGS lines” (compute=_compute_cogs_aml_ids)
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
- `origin_company_id` Many2one → `res.company` “Origin Company” (compute=_compute_origin_company_id)
- `order_partner_id` Many2one → `res.partner` (compute=_compute_order_partner_id)
- `analytic_account_line_ids` Many2many → `account.analytic.line`
- `account_move_id` Many2one → `account.move`
- `invoice_line_ids` One2many → `account.move.line`
- `product_value_ids` One2many → `product.value`

Public methods: `action_adjust_valuation`, `search_remaining_qty`, `write`

Extension points: `_action_done`, `_action_reset_to_draft`, `_action_reset_to_progress`, `_create_account_move`, `_create_analytic_move`, `_get_account_move_line_vals`, `_get_analytic_distribution`, `_get_in_move_lines`, `_get_manual_value`, `_get_move_directions`, `_get_origin_company_domains`, `_get_out_move_lines`, `_get_partner_id_for_valuation_lines`, `_get_price_unit`, `_get_price_unit_delivery`, `_get_price_unit_dropshipped`, `_get_value`, `_get_value_data`, `_get_value_from_account_move`, `_get_value_from_extra`, `_get_value_from_previous_company`, `_get_value_from_production`, `_get_value_from_quotation`, `_get_value_from_returns`, `_get_value_from_std_price`, `_get_valued_qty`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`

## `stock.move.line` (extends)


Public methods: `create`, `unlink`, `write`

## `stock.picking` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)

Extension points: `_check_backdate_allowed`, `_prepare_return_move_default_values`

## `stock.picking.type` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)

## `stock.quant` (extends)

- `value` Monetary “Value” (compute=_compute_value)
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `accounting_date` Date “Accounting Date”
- `cost_method` Selection “Cost Method” (compute=_compute_cost_method)

Extension points: `_get_inventory_fields_write`, `_get_inventory_move_values`

## `account.stock.valuation.report` (extends)


Extension points: `_get_extra_stock_valuation_aml_vals`, `_get_inventory_loss_aml_vals`, `_get_report_data`

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

## `stock.inventory.adjustment.name` (extends)

- `accounting_date` Date “Accounting Date”
- `should_show_accounting_date` Boolean (compute=_compute_should_show_accounting_date)

Extension points: `_get_quants_context`
