# l10n_fr — France - Accounting

Depends on: account, base_iban, base_vat.

## `account.chart.template` (extends)


Extension points: `_prepare_all_journals`

## `res.partner` (extends)

- `siret` Char “SIRET”

## `res.company` (extends)

- `l10n_fr_closing_sequence_id` Many2one → `ir.sequence` (readonly)
- `siret` Char “SIRET” (related=partner_id.siret)
- `ape` Char “APE”
- `is_france_country` Boolean “Is Part of DOM-TOM” (compute=_compute_is_france_country)

Public methods: `create`, `write`

Extension points: `_create_secure_sequence`, `_get_france_country_codes`, `_get_unalterable_country`
