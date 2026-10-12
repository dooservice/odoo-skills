# l10n_dk_oioubl — Denmark - E-invoicing

Depends on: account_edi_ubl_cii, l10n_dk.

## `account.edi.xml.oioubl_201` (defines)

OIOUBL 2.01

Inherits: `account.edi.xml.ubl_20`


Extension points: `_get_currency_decimal_places`, `_get_document_type_code_vals`, `_get_invoice_monetary_total_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_payment_terms_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`

## `account.move` (extends)


Extension points: `_get_ubl_cii_builder_from_xml_tree`

## `res.partner` (extends)

- `ubl_cii_format` Selection

Extension points: `_get_edi_builder`
