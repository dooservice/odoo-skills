# l10n_jp_ubl_pint — Japan - UBL PINT

Depends on: account_edi_ubl_cii.

## `account.edi.xml.ubl_21` (extends)


Extension points: `_get_customization_ids`

## `account.edi.xml.pint_jp` (defines)

Japanese implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_invoice_period_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_party_legal_entity_vals_list`

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
