# l10n_account_withholding_tax — Withholding Tax

Depends on: account.

## `account.chart.template` (extends)


## `account.move` (extends)

- `amount_residual` Monetary
- `withholding_total_amount_currency` Monetary (store, compute=_compute_withholding_total_amount)
- `withholding_deducted_amount_currency` Monetary (store, compute=_compute_deducted_withholding_amount)
- `withholding_residual_amount_currency` Monetary (compute=_compute_residual_withholding_amount)
- `withholding_net_residual_amount_currency` Monetary “Net Due Amount” (compute=_compute_withholding_net_residual_amount)

Public methods: `is_withhold_entry`

Extension points: `_prepare_payments_widget_reconciled_info`, `_prepare_product_base_line_for_taxes_computation`

## `account.payment` (extends)

- `display_withholding` Boolean (compute=_compute_display_withholding)
- `withhold` Selection
- `withholding_line_ids` One2many → `account.payment.withholding.line` “Withholding Lines”
- `withholding_payment_account_id` Many2one (related=payment_method_line_id.payment_account_id)
- `outstanding_account_id` Many2one
- `withholding_hide_tax_base_account` Boolean (compute=_compute_withholding_hide_tax_base_account)
- `withholding_amount` Monetary “Withholding Amount” (compute=_compute_withholding_amount)
- `withholding_net_amount` Monetary “Net Amount” (compute=_compute_withholding_net_amount)
- `withholding_hide_name` Boolean (compute=_compute_withholding_hide_name)

Extension points: `_check_payment_method_line_id`, `_get_trigger_fields_to_synchronize`, `_prepare_move_liquidity_lines`, `_prepare_move_withholding_lines`

## `account.payment.withholding.line` (defines)

Payment withholding line

Inherits: `account.withholding.line`

- `payment_id` Many2one → `account.payment` (required, index)

Extension points: `_get_comodel_partner`, `_get_valid_liquidity_accounts`, `_prepare_withholding_amls_create_values`

## `account.tax` (extends)

- `is_withholding_tax` Boolean “Withhold”
- `withholding_sequence_id` Many2one → `ir.sequence` “Withholding Sequence”

Extension points: `_check_amount_type`

## `account.withholding.line` (defines)

withholding line

Inherits: `analytic.mixin`

- `name` Char “Sequence Number”
- `placeholder_value` Char
- `placeholder_type` Selection (required, store, compute=_compute_placeholder_type)
- `previous_placeholder_type` Selection (store, compute=_compute_placeholder_type)
- `type_tax_use` Char (compute=_compute_type_tax_use)
- `tax_id` Many2one → `account.tax` (required, index)
- `withholding_sequence_id` Many2one (related=tax_id.withholding_sequence_id)
- `source_base_amount_currency` Monetary
- `source_base_amount` Monetary
- `source_tax_amount_currency` Monetary
- `source_tax_amount` Monetary
- `source_currency_id` Many2one → `res.currency`
- `source_tax_id` Many2one → `account.tax`
- `original_base_amount` Monetary (compute=_compute_original_amounts)
- `original_tax_amount` Monetary (compute=_compute_original_amounts)
- `base_amount` Monetary “Withholding base” (store, compute=_compute_base_amount)
- `amount` Monetary “Withholding amount” (store, compute=_compute_amount)
- `account_id` Many2one → `account.account` (required, store, compute=_compute_account_id)
- `comodel_percentage_paid_factor` Float (compute=_compute_comodel_percentage_paid_factor)
- `comodel_date` Date (compute=_compute_comodel_date)
- `comodel_payment_type` Selection (compute=_compute_comodel_payment_type)
- `company_id` Many2one → `res.company` (required, store, index, compute=_compute_company_id)
- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `comodel_company_currency_id` Many2one (related=company_id.currency_id)
- `comodel_currency_id` Many2one → `res.currency` (required, compute=_compute_comodel_currency_id)

Extension points: `_get_comodel_partner`, `_get_grouping_key`, `_get_valid_liquidity_accounts`, `_get_withholding_tax_domain`, `_prepare_base_line_for_taxes_computation`, `_prepare_withholding_amls_create_values`, `_prepare_withholding_lines_commands`

## `product.template` (extends)


## `res.company` (extends)

- `withholding_tax_base_account_id` Many2one → `account.account` “Withholding Tax Base”

## `res.config.settings` (extends)

- `withholding_tax_base_account_id` Many2one (related=company_id.withholding_tax_base_account_id)

## `account.payment.register` (extends)

- `display_withholding` Boolean (compute=_compute_display_withholding)
- `withhold` Selection
- `withholding_line_ids` One2many → `account.payment.register.withholding.line` “Withholding Lines” (store, compute=_compute_withholding_line_ids)
- `withholding_net_amount` Monetary “Net Amount” (store, compute=_compute_withholding_net_amount)
- `withholding_default_account_id` Many2one (related=journal_id.default_account_id)
- `withholding_outstanding_account_id` Many2one → `account.account` “Outstanding Account” (store, compute=_compute_withholding_outstanding_account_id)
- `withholding_payment_account_id` Many2one (related=payment_method_line_id.payment_account_id)
- `withholding_hide_tax_base_account` Boolean (compute=_compute_withholding_hide_tax_base_account)
- `withholding_hide_name` Boolean (compute=_compute_withholding_hide_name)

Public methods: `default_get`

Extension points: `_create_payment_vals_from_wizard`, `_get_default_withhold`, `_get_total_amount_in_wizard_currency`

## `account.payment.register.withholding.line` (defines)

Payment register withholding line

Inherits: `account.withholding.line`

- `payment_register_id` Many2one → `account.payment.register` (required)

Extension points: `_get_comodel_partner`, `_get_valid_liquidity_accounts`, `_prepare_withholding_amls_create_values`
