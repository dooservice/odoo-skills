# l10n_be — Belgium - Accounting

Depends on: account, account_edi_ubl_cii, base_iban, base_vat.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.move` (extends)


Extension points: `_get_invoice_reference_be_invoice`, `_get_invoice_reference_be_partner`

## `account.tax` (extends)

- `tax_scope` Selection

## `res.partner` (extends)


## `account.chart.template` (extends)


Extension points: `_get_bank_fees_reco_account`, `_get_be_account_account`, `_get_be_account_journal`, `_get_be_reconcile_model`, `_get_be_res_company`, `_get_be_template_data`, `_post_load_data`

## `account.chart.template` (extends)


Extension points: `_get_be_asso_res_company`, `_get_be_asso_template_data`

## `account.chart.template` (extends)


Extension points: `_get_be_comp_res_company`, `_get_be_comp_template_data`
