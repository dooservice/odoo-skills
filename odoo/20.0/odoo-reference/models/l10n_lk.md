# l10n_lk — Sri Lanka - Accounting

Depends on: account, l10n_account_withholding_tax.

## `account.move` (extends)


Extension points: `_get_last_sequence`, `_get_name_invoice_report`, `_get_next_sequence_format`, `_get_sequence_format_param`, `_get_starting_sequence`

## `account.resequence.wizard` (extends)


## `res.company` (extends)

- `l10n_lk_vat_registered` Boolean “Sri Lanka: VAT Registered” (related=partner_id.l10n_lk_vat_registered)

## `res.partner` (extends)

- `l10n_lk_vat_registered` Boolean “Sri Lanka: VAT Registered” (store, compute=_compute_l10n_lk_vat_registered)

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_lk_account_account`, `_get_lk_account_journal`, `_get_lk_res_company`, `_get_lk_template_data`
