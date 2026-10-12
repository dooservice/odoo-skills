# l10n_br — Brazilian - Accounting

Depends on: account, account_qr_code_emv, base_address_extended, l10n_latam_base, l10n_latam_invoice_document.

## `account.chart.template` (extends)


Extension points: `_get_demo_data_move`

## `account.tax` (extends)

- `tax_discount` Boolean “Discount this Tax in Price”
- `base_reduction` Float “Redution” (required)
- `amount_mva` Float “MVA Percent” (required)

## `account.fiscal.position` (extends)

- `l10n_br_fp_type` Selection “Interstate Fiscal Position Type”

Extension points: `_get_fiscal_position`

## `account.journal` (extends)

- `l10n_br_invoice_serial` Char “Series”

## `account.move` (extends)


Extension points: `_get_last_sequence_domain`

## `l10n_br.zip.range` (defines)

Brazilian city zip range

- `city_id` Many2one → `res.city` “City” (required)
- `start` Char “From” (required)
- `end` Char “To” (required)

Extension points: `_check_range`

## `res.city` (extends)

- `l10n_br_zip_range_ids` One2many → `l10n_br.zip.range` “Zip Ranges”
- `l10n_br_zip_ranges` Char “Frontend Zip Ranges” (compute=_compute_l10n_br_zip_ranges)

## `res.company` (extends)

- `l10n_br_cpf_code` Char “CPF”
- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_nire_code` Char “NIRE”

## `res.partner` (extends)

- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_isuf_code` Char “SUFRAMA code”

## `res.partner.bank` (extends)

- `proxy_type` Selection

Extension points: `_check_br_proxy`, `_check_for_qr_code_errors`, `_get_additional_data_field`, `_get_error_messages_for_qr`, `_get_merchant_account_info`, `_get_qr_code_vals_list`

## `account.chart.template` (extends)


Extension points: `_get_br_account_journal`, `_get_br_res_company`, `_get_br_template_data`

## `account.move.reversal` (extends)
