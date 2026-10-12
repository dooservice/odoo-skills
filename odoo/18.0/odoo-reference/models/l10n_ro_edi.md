# l10n_ro_edi — Romania - E-invoicing

Depends on: account_edi_ubl_cii, l10n_ro.

## `account.edi.xml.ubl_ro` (defines)

CIUS RO

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_document_type_code_vals`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_party_tax_scheme_vals_list`

## `account.move` (extends)

- `l10n_ro_edi_document_ids` One2many → `l10n_ro_edi.document`
- `l10n_ro_edi_state` Selection “E-Factura Status” (store, compute=_compute_l10n_ro_edi_state)
- `l10n_ro_edi_attachment_id` Many2one → `ir.attachment`
- `l10n_ro_edi_index` Char “E-Factura Index” (readonly)

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `l10n_ro_edi.document` (defines)

Document object for tracking CIUS-RO XML sent to E-Factura

- `invoice_id` Many2one → `account.move` (required)
- `state` Selection “E-Factura Status” (required)
- `datetime` Datetime (required)
- `attachment_id` Many2one → `ir.attachment`
- `message` Char
- `key_loading` Char “E-Factura Index”
- `key_signature` Char
- `key_certificate` Char

Public methods: `action_l10n_ro_edi_download_signature`, `action_l10n_ro_edi_fetch_status`

## `res.company` (extends)

- `l10n_ro_edi_client_id` Char “eFactura Client ID”
- `l10n_ro_edi_client_secret` Char “Client Secret”
- `l10n_ro_edi_access_token` Char “Access Token”
- `l10n_ro_edi_refresh_token` Char “Refresh Token”
- `l10n_ro_edi_access_expiry_date` Date “Access Token Expiry Date”
- `l10n_ro_edi_refresh_expiry_date` Date “Refresh Token Expiry Date”
- `l10n_ro_edi_callback_url` Char (compute=_compute_l10n_ro_edi_callback_url)
- `l10n_ro_edi_test_env` Boolean “Use Test Environment”
- `l10n_ro_edi_oauth_error` Char

## `res.config.settings` (extends)

- `l10n_ro_edi_client_id` Char (related=company_id.l10n_ro_edi_client_id)
- `l10n_ro_edi_client_secret` Char (related=company_id.l10n_ro_edi_client_secret)
- `l10n_ro_edi_access_token` Char (related=company_id.l10n_ro_edi_access_token)
- `l10n_ro_edi_refresh_token` Char (related=company_id.l10n_ro_edi_refresh_token)
- `l10n_ro_edi_access_expiry_date` Date (related=company_id.l10n_ro_edi_access_expiry_date)
- `l10n_ro_edi_refresh_expiry_date` Date (related=company_id.l10n_ro_edi_refresh_expiry_date)
- `l10n_ro_edi_callback_url` Char (related=company_id.l10n_ro_edi_callback_url)
- `l10n_ro_edi_test_env` Boolean (related=company_id.l10n_ro_edi_test_env)
- `l10n_ro_edi_oauth_error` Char (related=company_id.l10n_ro_edi_oauth_error)

Public methods: `button_l10n_ro_edi_generate_token`

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_ubl_cii_formats_info`

## `account.move.send.wizard` (extends)
