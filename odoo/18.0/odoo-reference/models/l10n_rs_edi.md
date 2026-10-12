# l10n_rs_edi — Serbia - eFaktura E-invoicing

Depends on: account_edi_ubl_cii, l10n_rs.

## `account.edi.xml.ubl.rs` (defines)

UBL 2.1 (RS eFaktura)

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_customization_ids`, `_get_invoice_period_vals_list`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`

## `account.move` (extends)

- `l10n_rs_edi_uuid` Char “RS Invoice UUID” (store, compute=_compute_l10n_rs_edi_uuid)
- `l10n_rs_edi_is_eligible` Boolean (store, compute=_compute_l10n_rs_edi_is_eligible)
- `l10n_rs_edi_attachment_file` Binary “Serbian E-Invoice XML File”
- `l10n_rs_edi_attachment_id` Many2one → `ir.attachment` “eFaktura XML Attachment”
- `l10n_rs_edi_state` Selection “Serbia E-Invoice state” (readonly)
- `l10n_rs_edi_error` Text “Serbia E-Invoice error” (readonly)
- `l10n_rs_tax_date_obligations_code` Selection “Tax Date Obligations” (store, compute=_compute_l10n_rs_tax_date_obligations_code)
- `l10n_rs_edi_invoice` Char “Invoice Id”
- `l10n_rs_edi_sales_invoice` Char “Sales Invoice Id”
- `l10n_rs_edi_purchase_invoice` Char “Purchase Invoice Id”

Public methods: `button_draft`

## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`, `_get_invoice_extra_attachments`

## `res.company` (extends)

- `l10n_rs_edi_api_key` Char “eFaktura API Key”
- `l10n_rs_edi_demo_env` Boolean “Use Demo Environment”

## `res.config.settings` (extends)

- `l10n_rs_edi_api_key` Char (related=company_id.l10n_rs_edi_api_key)
- `l10n_rs_edi_demo_env` Boolean (related=company_id.l10n_rs_edi_demo_env)

## `res.partner` (extends)

- `l10n_rs_edi_registration_number` Char “Registration Number”
- `l10n_rs_edi_public_funds` Char “JBKJS”

Extension points: `_check_l10n_rs_edi_public_funds`, `_check_l10n_rs_edi_registration_number`

## `account.move.send.wizard` (extends)
