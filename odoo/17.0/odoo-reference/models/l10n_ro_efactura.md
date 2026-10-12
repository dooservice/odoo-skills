# l10n_ro_efactura — Romania - Send E-Factura

Depends on: l10n_ro_edi.

## `account.move` (extends)

- `l10n_ro_edi_document_ids` One2many → `l10n_ro_edi.document`
- `l10n_ro_edi_state` Selection “E-Factura Status” (store, compute=_compute_l10n_ro_edi_state)
- `l10n_ro_edi_attachment_id` Many2one → `ir.attachment`

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

## `account.move.send` (extends)

- `l10n_ro_edi_send_enable` Boolean (compute=_compute_l10n_ro_edi_send_enable)
- `l10n_ro_edi_send_readonly` Boolean (compute=_compute_l10n_ro_edi_send_readonly)
- `l10n_ro_edi_send_checkbox` Boolean “Send E-Factura to SPV” (store, compute=_compute_l10n_ro_edi_send_checkbox)
- `l10n_ro_edi_warnings` Char (compute=_compute_l10n_ro_edi_warnings)

Extension points: `_get_wizard_values`
