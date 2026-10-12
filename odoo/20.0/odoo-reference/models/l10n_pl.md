# l10n_pl — Poland - Accounting

Depends on: account, account_edi_ubl_cii.

## `account.move` (extends)

- `l10n_pl_vat_b_spv` Boolean “B_SPV”
- `l10n_pl_vat_b_spv_dostawa` Boolean “B_SPV_Dostawa”
- `l10n_pl_vat_b_mpv_prowizja` Boolean “B_MPV_Prowizja”

Extension points: `_get_accounting_date_source`, `_get_invoice_currency_rate_date`

## `account.payment` (extends)

- `l10n_pl_verification_id` Many2one → `l10n_pl.bank.account.verification` “PL Bank Verification” (readonly, store, compute=_compute_l10n_pl_verification_id)
- `l10n_pl_verification_status` Selection (related=l10n_pl_verification_id.verification_status)
- `l10n_pl_verification_timestamp` Datetime (related=l10n_pl_verification_id.verification_timestamp)
- `l10n_pl_verification_request_id` Char (related=l10n_pl_verification_id.verification_request_id)

## `l10n_pl.bank.account.verification` (defines)

PL Bank Account Verification

- `verification_status` Selection “Verification Status” (required, readonly)
- `verification_timestamp` Datetime “Verification Timestamp” (readonly)
- `verification_date` Date (store, compute=_compute_verification_date)
- `verification_request_id` Char “Correlation ID” (readonly)
- `partner_bank_id` Many2one → `res.partner.bank` “Bank Account” (readonly)
- `partner_bank_account_number` Char (readonly, store, compute=_compute_partner_bank_account_number)
- `partner_id` Many2one → `res.partner` “Partner” (readonly)
- `partner_vat` Char (readonly, store, compute=_compute_partner_vat)

Extension points: `_get_creation_vals`, `_get_partner_from_identifier`

## `l10n_pl.l10n_pl_tax_office` (defines)

Tax Office in Poland

- `code` Char “Code” (required)
- `name` Char “Description” (required)

## `product.template` (extends)

- `l10n_pl_vat_gtu` Selection “GTU Codes”

## `res.company` (extends)

- `l10n_pl_reports_tax_office_id` Many2one → `l10n_pl.l10n_pl_tax_office` “Tax Office”

## `res.config.settings` (extends)

- `l10n_pl_reports_tax_office_id` Many2one (related=company_id.l10n_pl_reports_tax_office_id)

## `res.partner` (extends)

- `l10n_pl_links_with_customer` Boolean “Links With Company”

## `account.chart.template` (extends)


Extension points: `_get_pl_account_account`, `_get_pl_res_company`, `_get_pl_template_data`

## `account.payment.register` (extends)

- `l10n_pl_bank_verification_ids` Many2many → `l10n_pl.bank.account.verification` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_bank_verification_invalid_bank_account_ids` Many2many → `res.partner.bank` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_not_found_partner_ids` Many2many → `res.partner` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_incomplete_data_partner_ids` Many2many → `res.partner` (compute=_compute_l10n_pl_bank_verification)

Extension points: `_create_payment_vals_from_batch`, `_create_payment_vals_from_wizard`, `_get_partner_bank_from_batch`
