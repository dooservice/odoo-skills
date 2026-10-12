# l10n_do — Dominican Republic - Accounting

Depends on: account, l10n_latam_invoice_document.

## `account.move` (extends)

- `l10n_do_purchase_type` Selection “Purchase Type”
- `l10n_do_payment_type` Selection “Payment Type”

Extension points: `_get_l10n_latam_documents_domain`

## `account.tax` (extends)

- `l10n_do_isr_type` Selection “ISR Withholding Type”

## `res.partner` (extends)


Extension points: `_get_all_additional_identifiers_metadata`

## `account.chart.template` (extends)


Extension points: `_get_do_res_company`, `_get_do_template_data`
