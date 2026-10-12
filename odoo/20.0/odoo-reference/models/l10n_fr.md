# l10n_fr — France - Localizations

Depends on: base.

## `res.company` (extends)

- `l10n_fr_closing_sequence_id` Many2one → `ir.sequence` (readonly)
- `ape` Char “APE”
- `is_france_country` Boolean “Is Part of DOM-TOM” (compute=_compute_is_france_country)

Public methods: `create`, `write`

Extension points: `_create_secure_sequence`, `_get_france_country_codes`

## `res.partner` (extends)

- `l10n_fr_is_french` Boolean (compute=_compute_l10n_fr_is_french)
