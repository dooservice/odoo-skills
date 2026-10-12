# l10n_ro_edi — Romania - E-invoicing

Depends on: account_edi_ubl_cii, l10n_ro.

## `account.edi.xml.ubl_ro` (defines)

CIUS RO

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_document_type_code_vals`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_party_tax_scheme_vals_list`

## `res.partner` (extends)

- `ubl_cii_format` Selection

Extension points: `_get_edi_builder`
