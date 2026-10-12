# l10n_sg_ubl_pint — Singapore - UBL PINT

Depends on: l10n_sg.

## `account.edi.xml.pint_sg` (defines)

Singapore implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.move` (extends)


Extension points: `_get_import_file_type`

## `res.company` (extends)


## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
