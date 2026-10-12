# l10n_ro_cpv_code — Romania - CPV Code

Depends on: l10n_ro_edi.

## `account.edi.xml.ubl_ro` (extends)


## `l10n_ro.cpv.code` (defines)

CPV Code

- `code` Char “Code” (required)
- `name` Char “Name” (required)

## `product.template` (extends)

- `cpv_code_id` Many2one → `l10n_ro.cpv.code` “CPV Code”
