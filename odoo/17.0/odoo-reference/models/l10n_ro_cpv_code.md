# l10n_ro_cpv_code — Romania - CPV Code

Depends on: l10n_ro_efactura.

## `account.edi.xml.ubl_ro` (extends)


Extension points: `_get_invoice_line_item_vals`

## `l10n_ro.cpv.code` (defines)

CPV Code

- `code` Char “Code” (required)
- `name` Char “Name” (required)

## `product.template` (extends)

- `cpv_code_id` Many2one → `l10n_ro.cpv.code` “CPV Code”
