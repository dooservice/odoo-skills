# l10n_th — Thailand - Accounting

Depends on: account_qr_code_emv, account, l10n_account_withholding_tax.

## `account.move` (extends)

- `l10n_th_tax_invoice_ids` One2many → `l10n_th.tax.invoice` “Tax Invoices”
- `l10n_th_is_vat_registered` Boolean (related=company_id.l10n_th_is_vat_registered)

Public methods: `button_cancel`, `button_draft`

Extension points: `_create_l10n_th_tax_invoices_from_caba_entries`, `_get_exigible_invoice_lines`, `_get_name_invoice_report`, `_get_th_moves_domain`, `_get_th_tax_invoice_base_lines`, `_get_th_tax_invoice_line_data`, `_get_th_tax_invoice_totals`

## `account.partial.reconcile` (extends)


Extension points: `_create_tax_cash_basis_moves`

## `account.payment` (extends)

- `l10n_th_wth_condition` Selection “Withholding Condition” (store, compute=_compute_l10n_th_wth_condition)

Public methods: `action_download_50_tawi_bulk`, `action_l10n_th_print_50_tawi`

## `account.tax` (extends)

- `l10n_th_income_tax_type` Selection “Income Tax Type”
- `l10n_th_income_tax_type_others` Char “Other Type”

## `l10n_th.tax.invoice` (defines)

Tax Invoice Information

- `invoice_move_id` Many2one → `account.move` (required)
- `payment_move_id` Many2one → `account.move`
- `date` Date “Date”
- `tax_invoice_number` Char “Tax Invoice Number”
- `reference` Char “Reference”
- `total_amount` Monetary “Total Amount”
- `vat_amount` Monetary “VAT Amount”
- `amount_residual` Monetary “Amount Due”
- `total_on_payment_amount` Monetary “Total On Payment Amount”
- `is_partially_paid` Boolean “Partially Paid”
- `tax_group_amounts` Json “Tax Group Amounts”
- `tax_invoice_lines` Json “Tax Invoice Lines”
- `state` Selection “Status” (required, readonly)
- `currency_id` Many2one (related=invoice_move_id.currency_id)
- `company_id` Many2one (readonly, store, index, related=invoice_move_id.company_id)

Public methods: `action_print_tax_invoice_pdf`, `create`

Extension points: `_get_tax_invoice_document_title`

## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_for_qr_code_errors`, `_check_th_proxy`, `_get_emv_qr_code_names`, `_get_error_messages_for_qr`, `_get_merchant_account_info`

## `res.company` (extends)

- `l10n_th_is_vat_registered` Boolean “Thailand: VAT Registered”

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (readonly, related=company_id.account_fiscal_country_id)

## `res.partner` (extends)

- `l10n_th_branch_name` Char (compute=_compute_l10n_th_branch_name)
- `l10n_th_title` Selection “Title”
- `l10n_th_company_type` Selection “Company Type”
- `l10n_th_address_no_country` Char (compute=_compute_l10n_th_address_no_country)

## `account.chart.template` (extends)


Extension points: `_get_th_ir_sequence`, `_get_th_res_company`, `_get_th_template_data`

## `report.l10n_th.report_50_tawi` (defines)

50 Tawi Report


Extension points: `_get_report_values`

## `account.payment.register` (extends)

- `l10n_th_wth_condition` Selection “Withholding Condition” (store, compute=_compute_l10n_th_wth_condition)

Extension points: `_create_payment_vals_from_wizard`
