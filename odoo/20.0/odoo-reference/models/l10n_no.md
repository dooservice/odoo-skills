# l10n_no — Norway - Accounting

Depends on: account, account_edi_ubl_cii.

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.move` (extends)


Extension points: `_get_invoice_reference_no_invoice`, `_get_invoice_reference_no_partner`, `_get_kid_number`

## `account.tax` (extends)

- `l10n_no_standard_code` Char “Standard Tax Code”

## `res.company` (extends)

- `l10n_no_bronnoysund_number` Char (related=partner_id.l10n_no_bronnoysund_number)

## `res.partner` (extends)

- `l10n_no_bronnoysund_number` Char “Register of Legal Entities (Brønnøysund Register Center)” (compute=_compute_l10n_no_bronnoysund_number)

## `account.chart.template` (extends)


Extension points: `_get_no_res_company`, `_get_no_template_data`
