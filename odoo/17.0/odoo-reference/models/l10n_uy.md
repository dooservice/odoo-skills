# l10n_uy — Uruguay - Accounting

Depends on: account, l10n_latam_invoice_document, l10n_latam_base.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`, `_post_load_demo_data`

## `account.move` (extends)


Extension points: `_get_l10n_latam_documents_domain`, `_get_last_sequence_domain`, `_get_starting_sequence`

## `account.tax` (extends)

- `l10n_uy_tax_category` Selection “Tax Category”

## `l10n_latam.document.type` (extends)


## `l10n_latam.identification.type` (extends)

- `l10n_uy_dgi_code` Char “DGI Code”

## `res.company` (extends)


## `res.partner` (extends)


Public methods: `check_vat`

## `account.chart.template` (extends)


Extension points: `_get_uy_account_journal`, `_get_uy_res_company`, `_get_uy_template_data`
