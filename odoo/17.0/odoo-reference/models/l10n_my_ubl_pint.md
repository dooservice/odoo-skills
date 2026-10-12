# l10n_my_ubl_pint — Malaysia - UBL PINT

Depends on: account_edi_ubl_cii.

## `account.edi.xml.pint_my` (defines)

Malaysian implementation of Peppol International (PINT) model for Billing

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_invoice_tax_totals_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_tax_unece_codes`

## `res.company` (extends)

- `sst_registration_number` Char (related=partner_id.sst_registration_number)
- `ttx_registration_number` Char (related=partner_id.ttx_registration_number)

## `base.document.layout` (extends)

- `account_fiscal_country_id` Many2one (related=company_id.account_fiscal_country_id)
- `sst_registration_number` Char (related=company_id.sst_registration_number)
- `ttx_registration_number` Char (related=company_id.ttx_registration_number)

## `res.partner` (extends)

- `ubl_cii_format` Selection
- `sst_registration_number` Char “SST”
- `ttx_registration_number` Char “TTx”

Extension points: `_get_edi_builder`
