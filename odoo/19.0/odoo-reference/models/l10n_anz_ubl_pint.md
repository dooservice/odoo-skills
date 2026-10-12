# l10n_anz_ubl_pint — Australia & New Zealand - UBL PINT

Depends on: account_edi_ubl_cii.

## `account.edi.xml.pint_anz` (defines)

Australia & New Zealand implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.move` (extends)


Extension points: `_get_import_file_type`

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
