# l10n_dk_oioubl — Denmark - E-invoicing

Depends on: account_edi_ubl_cii, l10n_dk.

## `account.edi.xml.oioubl_201` (defines)

OIOUBL 2.01

Inherits: `account.edi.xml.ubl_20`


Extension points: `_get_address_node`, `_get_currency_decimal_places`, `_get_document_type_code_node`, `_get_party_node`, `_get_tax_category_node`, `_get_tax_subtotal_node`

## `account.move` (extends)


Extension points: `_get_import_file_type`

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
