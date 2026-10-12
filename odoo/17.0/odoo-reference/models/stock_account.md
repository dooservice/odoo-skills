# stock_account — WMS Accounting

Depends on: stock, account.

## `account.chart.template` (extends)


Extension points: `_get_stock_account_journal`, `_get_stock_template_data`, `_post_load_data`

## `account.move` (extends)

- `stock_move_id` Many2one → `stock.move` “Stock Move”
- `stock_valuation_layer_ids` One2many → `stock.valuation.layer` “Stock Valuation Layer”

Public methods: `button_cancel`, `button_draft`, `copy_data`

Extension points: `_get_anglo_saxon_price_ctx`, `_get_invoiced_lot_values`, `_get_lines_onchange_currency`

## `account.move.line` (extends)

- `stock_valuation_layer_ids` One2many → `stock.valuation.layer` “Stock Valuation Layer”
- `cogs_origin_id` Many2one → `account.move.line`

Extension points: `_get_exchange_account`, `_get_exchange_journal`, `_get_gross_unit_price`, `_get_stock_valuation_layers`, `_get_valued_in_moves`

## `account.analytic.plan` (extends)


## `account.analytic.account` (extends)


## `product.template` (extends)

- `cost_method` Selection (readonly, related=categ_id.property_cost_method)
- `valuation` Selection (readonly, related=categ_id.property_valuation)

Public methods: `get_product_accounts`, `write`

Extension points: `_get_product_accounts`

## `product.product` (extends)

- `value_svl` Float (compute=_compute_value_svl)
- `quantity_svl` Float (compute=_compute_value_svl)
- `avg_cost` Monetary “Average Cost” (compute=_compute_value_svl)
- `total_value` Monetary “Total Value” (compute=_compute_value_svl)
- `company_currency_id` Many2one → `res.currency` (compute=_compute_value_svl)
- `stock_valuation_layer_ids` One2many → `stock.valuation.layer`
- `valuation` Selection (readonly, related=categ_id.property_valuation)
- `cost_method` Selection (readonly, related=categ_id.property_cost_method)

Public methods: `action_revaluation`, `write`

Extension points: `_create_fifo_vacuum_anglo_saxon_expense_entries`, `_create_fifo_vacuum_anglo_saxon_expense_entry`, `_get_fifo_candidates`, `_get_fifo_candidates_domain`, `_get_qty_taken_on_candidate`, `_get_valuation_layer_group_domain`, `_get_valuation_layer_group_fields_aggregate`, `_get_valuation_layer_groups`, `_prepare_fifo_vacuum_valuation_layer_values`, `_prepare_in_svl_vals`, `_prepare_out_svl_vals`, `_prepare_valuation_layer_field_values`

## `product.category` (extends)

- `property_valuation` Selection “Inventory Valuation” (required, company_dependent)
- `property_cost_method` Selection “Costing Method” (required, company_dependent)
- `property_stock_journal` Many2one → `account.journal` (company_dependent)
- `property_stock_account_input_categ_id` Many2one → `account.account` (company_dependent)
- `property_stock_account_output_categ_id` Many2one → `account.account` (company_dependent)
- `property_stock_valuation_account_id` Many2one → `account.account` (company_dependent)

Public methods: `onchange_property_cost`, `onchange_property_valuation`, `write`

Extension points: `_check_valuation_accounts`, `_create_default_stock_accounts_properties`, `_get_stock_account_property_field_names`

## `res.config.settings` (extends)

- `module_stock_landed_costs` Boolean “Landed Costs”
- `group_lot_on_invoice` Boolean “Display Lots & Serial Numbers on Invoices”
- `group_stock_accounting_automatic` Boolean “Automatic Stock Accounting”

Public methods: `set_values`

## `stock.location` (extends)

- `valuation_in_account_id` Many2one → `account.account`
- `valuation_out_account_id` Many2one → `account.account`

## `stock.move` (extends)

- `to_refund` Boolean “Update quantities on SO/PO”
- `account_move_ids` One2many → `account.move`
- `stock_valuation_layer_ids` One2many → `stock.valuation.layer`
- `analytic_account_line_ids` Many2many → `account.analytic.line`

Public methods: `action_get_account_moves`, `product_price_update_before_done`

Extension points: `_action_cancel`, `_action_done`, `_create_dropshipped_returned_svl`, `_create_dropshipped_svl`, `_create_in_svl`, `_create_out_svl`, `_get_accounting_data_for_valuation`, `_get_all_related_aml`, `_get_all_related_sm`, `_get_analytic_distribution`, `_get_dest_account`, `_get_dropshipped_svl_vals`, `_get_in_move_lines`, `_get_in_svl_vals`, `_get_layer_candidates`, `_get_out_move_lines`, `_get_out_svl_vals`, `_get_partner_id_for_valuation_lines`, `_get_price_unit`, `_get_related_invoices`, `_get_src_account`, `_get_valued_types`, `_prepare_account_move_line`, `_prepare_account_move_vals`, `_prepare_analytic_line_values`, `_prepare_analytic_lines`, `_prepare_anglosaxon_account_move_vals`, `_prepare_common_svl_vals`, `_prepare_move_split_vals`

## `stock.move.line` (extends)


Public methods: `create`, `unlink`, `write`

Extension points: `_create_correction_svl`

## `stock.picking` (extends)

- `country_code` Char (related=company_id.account_fiscal_country_id.code)

Public methods: `action_view_stock_valuation_layers`

## `stock.quant` (extends)

- `value` Monetary “Value” (compute=_compute_value)
- `currency_id` Many2one → `res.currency` (compute=_compute_value)
- `accounting_date` Date “Accounting Date”
- `cost_method` Selection (related=product_categ_id.property_cost_method)

Public methods: `read_group`

Extension points: `_get_inventory_fields_write`, `_get_inventory_move_values`

## `stock.valuation.layer` (defines)

Stock Valuation Layer

- `company_id` Many2one → `res.company` (required, readonly)
- `product_id` Many2one → `product.product` (required, readonly)
- `categ_id` Many2one → `product.category` (store, related=product_id.categ_id)
- `product_tmpl_id` Many2one → `product.template` (related=product_id.product_tmpl_id)
- `quantity` Float “Quantity” (readonly)
- `uom_id` Many2one (required, readonly, related=product_id.uom_id)
- `currency_id` Many2one → `res.currency` (required, readonly, related=company_id.currency_id)
- `unit_cost` Float “Unit Value” (readonly)
- `value` Monetary “Total Value” (readonly)
- `remaining_qty` Float (readonly)
- `remaining_value` Monetary “Remaining Value” (readonly)
- `description` Char “Description” (readonly)
- `stock_valuation_layer_id` Many2one → `stock.valuation.layer` (readonly, index)
- `stock_valuation_layer_ids` One2many → `stock.valuation.layer`
- `stock_move_id` Many2one → `stock.move` (readonly, index)
- `account_move_id` Many2one → `account.move` (readonly)
- `account_move_line_id` Many2one → `account.move.line` (readonly)
- `reference` Char (related=stock_move_id.reference)
- `price_diff_value` Float “Invoice value correction with invoice currency”
- `warehouse_id` Many2one → `stock.warehouse` “Receipt WH” (compute=_compute_warehouse_id)

Public methods: `action_open_journal_entry`, `action_open_layer`, `action_open_reference`, `action_valuation_at_date`, `init`

Extension points: `_get_related_product`

## `stock.forecasted_product_product` (extends)


Extension points: `_get_report_header`

## `stock.return.picking` (extends)


Public methods: `default_get`

Extension points: `_prepare_move_default_values`

## `stock.return.picking.line` (extends)

- `to_refund` Boolean “Update quantities on SO/PO”

## `stock.quantity.history` (extends)


Public methods: `open_at_date`

## `stock.request.count` (extends)

- `accounting_date` Date “Accounting Date”

Extension points: `_get_values_to_write`

## `stock.valuation.layer.revaluation` (defines)

Wizard model to reavaluate a stock inventory for a product

- `company_id` Many2one → `res.company` (required, readonly)
- `currency_id` Many2one → `res.currency` (required, related=company_id.currency_id)
- `product_id` Many2one → `product.product` (required)
- `property_valuation` Selection (related=product_id.categ_id.property_valuation)
- `product_uom_name` Char “Unit of Measure” (related=product_id.uom_id.name)
- `current_value_svl` Float “Current Value” (related=product_id.value_svl)
- `current_quantity_svl` Float “Current Quantity” (related=product_id.quantity_svl)
- `added_value` Monetary “Added value” (required)
- `new_value` Monetary “New value” (compute=_compute_new_value)
- `new_value_by_qty` Monetary “New value by quantity” (compute=_compute_new_value)
- `reason` Char “Reason”
- `account_journal_id` Many2one → `account.journal`
- `account_id` Many2one → `account.account`
- `date` Date “Accounting Date”

Public methods: `action_validate_revaluation`, `default_get`
