# l10n_es_edi_facturae_adm_centers — Spain - Facturae EDI - Administrative Centers Patch

Depends on: l10n_es_edi_facturae.

## `account.move` (extends)


## `l10n_es_edi_facturae_adm_centers.ac_role_type` (defines)

Administrative Center Role Type

- `code` Char (required)
- `name` Char (required)

## `res.partner` (extends)

- `type` Selection
- `l10n_es_edi_facturae_ac_center_code` Char “Code”
- `l10n_es_edi_facturae_ac_role_type_ids` Many2many → `l10n_es_edi_facturae_adm_centers.ac_role_type` “Roles”
- `l10n_es_edi_facturae_ac_physical_gln` Char “Physical GLN”
- `l10n_es_edi_facturae_ac_logical_operational_point` Char “Logical Operational Point”
