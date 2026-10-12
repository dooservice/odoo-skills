# l10n_cn — China - Accounting

Depends on: base, account.

## `account.move` (extends)

- `fapiao` Char “Fapiao Number”
- `l10n_cn_differential_taxation_method` Selection “VAT Differential Taxation Method”
- `l10n_cn_output_vat_offset_origin_id` Many2one → `account.move` “Output VAT Offset Origin Entry”
- `l10n_cn_output_vat_offset_origin_line_ids` One2many → `account.move.line` “Output VAT Offset Origin Lines”
- `l10n_cn_output_vat_offset_move_ids` One2many → `account.move` “Output VAT Offset Entries”
- `l10n_cn_vat_differential_taxation` Boolean (related=company_id.l10n_cn_vat_differential_taxation)

Public methods: `action_open_l10n_cn_output_vat_offset_entries`, `button_draft`, `check_cn2an`

Extension points: `_check_fapiao`, `_check_l10n_cn_balance_deduction_info`, `_check_l10n_cn_output_vat_offset_direct_modification`, `_create_l10n_cn_output_vat_offset_moves`, `_prepare_l10n_cn_output_vat_offset_line_vals`

## `account.move.line` (extends)

- `l10n_cn_output_vat_offset_account_id` Many2one → `account.account` “Output VAT Offset Account”
- `l10n_cn_balance_deduction_ids` One2many → `l10n_cn.balance.deduction` “Balance Deductions”
- `l10n_cn_output_vat_offset_move_id` Many2one → `account.move` “Output VAT Offset Entry”
- `l10n_cn_differential_taxation_method` Selection (related=move_id.l10n_cn_differential_taxation_method)

Public methods: `action_open_l10n_cn_balance_deduction`, `action_reset_balance_deduction_to_draft`, `action_save_l10n_cn_balance_deduction`

Extension points: `_check_l10n_cn_balance_deduction_amount`, `_prepare_l10n_cn_output_vat_offset_move_vals`

## `l10n_cn.balance.deduction` (defines)

Balance Deduction Information

- `move_line_id` Many2one → `account.move.line` (required)
- `voucher_type` Selection “Voucher Type”
- `voucher_total` Monetary “Voucher Total”
- `deduct_amount` Monetary “Deduct Amount”
- `e_fapiao_number` Char “E-Fapiao Number”
- `receipt_code` Char “Receipt Code”
- `receipt_number` Char “Receipt Number”
- `voucher_number` Char “Voucher Number”
- `issue_date` Date “Issue Date”
- `remarks` Text “Remarks”
- `expense_account_id` Many2one → `account.account` “Expense Account”
- `company_id` Many2one (readonly, store, index, related=move_line_id.company_id)
- `currency_id` Many2one (related=move_line_id.currency_id)
- `accounting_date` Date “Accounting Date” (related=move_line_id.l10n_cn_output_vat_offset_move_id.date)
- `output_vat_offset_move_id` Many2one “Journal Entry” (related=move_line_id.l10n_cn_output_vat_offset_move_id)
- `invoice_number` Char “Invoice Number” (related=move_line_id.move_id.name)
- `fapiao_number` Char “Fapiao Number” (related=move_line_id.move_id.fapiao)
- `invoice_date` Date “Invoice Date” (related=move_line_id.invoice_date)
- `vat_differential_taxation` Selection “VAT Differential Taxation” (related=move_line_id.move_id.l10n_cn_differential_taxation_method)
- `product_id` Many2one “Product” (related=move_line_id.product_id)
- `tax_inclusive_amount` Monetary “Tax Inclusive Amount” (related=move_line_id.price_total)
- `move_type` Selection “Type” (related=move_line_id.move_id.move_type)

Extension points: `_check_amount`

## `res.company` (extends)

- `l10n_cn_output_vat_offset_account_id` Many2one → `account.account` “Output VAT Offset Account”
- `l10n_cn_output_vat_offset_journal_id` Many2one → `account.journal` “Output VAT Offset Journal”
- `l10n_cn_vat_differential_taxation` Boolean “VAT Differential Taxation”

## `res.config.settings` (extends)

- `l10n_cn_output_vat_offset_account_id` Many2one (related=company_id.l10n_cn_output_vat_offset_account_id)
- `l10n_cn_output_vat_offset_journal_id` Many2one (related=company_id.l10n_cn_output_vat_offset_journal_id)
- `l10n_cn_vat_differential_taxation` Boolean (related=company_id.l10n_cn_vat_differential_taxation)

## `account.chart.template` (extends)


Extension points: `_get_cn_account_account`, `_get_cn_res_company`, `_get_cn_template_data`

## `account.chart.template` (extends)


Extension points: `_get_cn_account_journal`, `_get_cn_common_res_company`, `_get_cn_common_template_data`

## `account.chart.template` (extends)


Extension points: `_get_cn_large_bis_account_account`, `_get_cn_large_bis_company`, `_get_cn_large_bis_template_data`

## `account.move.reversal` (extends)


Public methods: `default_get`
