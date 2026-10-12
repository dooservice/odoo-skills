# l10n_co — Colombia - Accounting

Depends on: account_debit_note, account.

## `res.partner` (extends)

- `l10n_co_dian_id_code` Char “CO Identification Type Code” (readonly, store, compute=_compute_l10n_co_dian_id)
- `l10n_co_dian_id_value` Char “CO Identification Number” (readonly, store, compute=_compute_l10n_co_dian_id)

Extension points: `_get_all_additional_identifiers_metadata`

## `account.chart.template` (extends)


Extension points: `_get_co_account_account`, `_get_co_res_company`, `_get_co_template_data`
