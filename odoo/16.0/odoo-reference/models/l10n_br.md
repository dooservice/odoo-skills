# l10n_br — Brazilian - Accounting

Depends on: account, base_vat.

## `account.tax.template` (extends)

- `tax_discount` Boolean “Discount this Tax in Prince”
- `base_reduction` Float “Redution” (required)
- `amount_mva` Float “MVA Percent” (required)

## `account.tax` (extends)

- `tax_discount` Boolean “Discount this Tax in Prince”
- `base_reduction` Float “Redution” (required)
- `amount_mva` Float “MVA Percent” (required)

## `account.chart.template` (extends)


Extension points: `_get_fp_vals`

## `account.fiscal.position` (extends)

- `l10n_br_fp_type` Selection “Interstate Fiscal Position Type”

Extension points: `_get_fiscal_position`

## `account.fiscal.position.template` (extends)

- `l10n_br_fp_type` Selection “Interstate Fiscal Position Type”

## `res.company` (extends)

- `l10n_br_cpf_code` Char “CPF”
- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_nire_code` Char “NIRE”

## `res.partner` (extends)

- `l10n_br_cpf_code` Char “CPF”
- `l10n_br_ie_code` Char “IE”
- `l10n_br_im_code` Char “IM”
- `l10n_br_isuf_code` Char “SUFRAMA code”
