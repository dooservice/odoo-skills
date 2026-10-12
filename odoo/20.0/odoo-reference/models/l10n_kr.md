# l10n_kr — Republic of Korea - Accounting

Depends on: account.

## `account.move` (extends)

- `l10n_kr_issuance_type` Selection “Proof of Issuance” (store, compute=_compute_l10n_kr_issuance_type)
- `l10n_kr_edocument_number` Char “e-Document Number”

## `res.partner` (extends)

- `l10n_kr_default_issuance_type` Selection “Proof of Issuance”

## `account.chart.template` (extends)


Extension points: `_get_account_parent_xmlid`, `_get_kr_account_account`, `_get_kr_account_journal`, `_get_kr_res_company`, `_get_kr_template_data`
