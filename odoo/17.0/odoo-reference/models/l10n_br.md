# l10n_br — Brazilian - Accounting

Depends on: account, base_vat, l10n_latam_base, l10n_latam_invoice_document.

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

## `res.company` (extends)

- `l10n_br_cpf_code` Char “CPF”
- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_nire_code` Char “NIRE”

## `res.partner` (extends)

- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_isuf_code` Char “SUFRAMA code”

## `account.chart.template` (extends)


Extension points: `_get_br_account_journal`, `_get_br_res_company`, `_get_br_template_data`

## `account.move.reversal` (extends)
