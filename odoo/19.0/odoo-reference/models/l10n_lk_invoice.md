# l10n_lk_invoice — Sri Lanka - Tax Invoice

Depends on: l10n_lk.

## `account.move` (extends)


Extension points: `_get_last_sequence`, `_get_name_invoice_report`, `_get_next_sequence_format`, `_get_sequence_format_param`, `_get_starting_sequence`

## `account.resequence.wizard` (extends)


## `res.company` (extends)

- `l10n_lk_vat_registered` Boolean “Sri Lanka: VAT Registered” (related=partner_id.l10n_lk_vat_registered)

## `res.partner` (extends)

- `l10n_lk_vat_registered` Boolean “Sri Lanka: VAT Registered” (store, compute=_compute_l10n_lk_vat_registered)
