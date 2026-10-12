# l10n_sg_ubl_pint — Singapore - UBL PINT

Depends on: account_edi_ubl_cii_tax_extension.

## `account.edi.xml.ubl_21` (extends)


Extension points: `_get_customization_ids`

## `account.edi.xml.pint_sg` (defines)

Singapore implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_additional_document_reference_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`

## `account.move` (extends)


## `account.tax` (extends)

- `ubl_cii_tax_category_code` Selection

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
