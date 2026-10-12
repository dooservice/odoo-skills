# l10n_my_ubl_pint — Malaysia - UBL PINT

Depends on: account_edi_ubl_cii.

## `account.edi.xml.pint_my` (defines)

Malaysian implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.move` (extends)


Extension points: `_get_import_file_type`

## `res.company` (extends)

- `sst_registration_number` Char (related=partner_id.sst_registration_number)
- `ttx_registration_number` Char (related=partner_id.ttx_registration_number)

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `sst_registration_number` Char (related=company_id.sst_registration_number)
- `ttx_registration_number` Char (related=company_id.ttx_registration_number)

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `sst_registration_number` Char “SST”
- `ttx_registration_number` Char “TTx”

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`
