# l10n_anz_ubl_pint — Australia & New Zealand - UBL PINT

Depends on: account_edi_ubl_cii_tax_extension.

## `account.edi.xml.pint_anz` (defines)

Australia & New Zealand implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_ids`, `_get_invoice_tax_totals_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`, `_get_tax_unece_codes`

## `res.partner` (extends)

- `ubl_cii_format` Selection

Extension points: `_get_edi_builder`
