# l10n_fr — France - Accounting

Depends on: base_iban, base_vat, account.

## `res.company` (extends)

- `l10n_fr_closing_sequence_id` Many2one → `ir.sequence` (readonly)
- `siret` Char “SIRET” (related=partner_id.siret)
- `ape` Char “APE”
- `is_france_country` Boolean “Is Part of DOM-TOM” (compute=_compute_is_france_country)
- `l10n_fr_rounding_difference_loss_account_id` Many2one → `account.account`
- `l10n_fr_rounding_difference_profit_account_id` Many2one → `account.account`

Public methods: `create`, `write`

Extension points: `_create_secure_sequence`, `_get_france_country_codes`, `_get_unalterable_country`

## `res.partner` (extends)

- `siret` Char “SIRET”

## `account.chart.template` (extends)


Extension points: `_get_fr_account_journal`, `_get_fr_reconcile_model`, `_get_fr_res_company`, `_get_fr_template_data`
