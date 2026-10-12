# l10n_latam_base — LATAM Localization Base

Depends on: contacts, base_vat.

## `l10n_latam.identification.type` (defines)

Identification Types

- `sequence` Integer
- `name` Char (required)
- `description` Char
- `active` Boolean
- `is_vat` Boolean
- `country_id` Many2one → `res.country`

## `res.company` (extends)


Public methods: `create`

## `res.partner` (extends)

- `l10n_latam_identification_type_id` Many2one → `l10n_latam.identification.type` “Identification Type”
- `is_vat` Boolean (related=l10n_latam_identification_type_id.is_vat)
- `vat` Char “Identification Number”

Extension points: `_check_vat`, `_get_frontend_writable_fields`
