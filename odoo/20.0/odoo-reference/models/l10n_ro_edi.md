# l10n_ro_edi — Romania - E-invoicing

Depends on: account_edi_ubl_cii, l10n_ro.

## `account.edi.xml.ubl_ro` (defines)

CIUS RO

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_document_type_code_node`

## `account.move` (extends)

- `l10n_ro_edi_document_ids` One2many → `l10n_ro_edi.document`
- `l10n_ro_edi_state` Selection “E-Factura Status” (store, compute=_compute_l10n_ro_edi_state)
- `l10n_ro_edi_index` Char “E-Factura Index” (readonly)

Public methods: `action_l10n_ro_edi_fetch_invoices`

Extension points: `_get_import_file_type`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `l10n_ro_edi.document` (defines)

Document object for tracking CIUS-RO XML sent to E-Factura

- `invoice_id` Many2one → `account.move` (required, readonly)
- `state` Selection “E-Factura Status” (required, readonly)
- `datetime` Datetime (required, readonly)
- `message` Char (readonly)
- `key_signature` Char (readonly)
- `key_certificate` Char (readonly)
- `key_download` Char “Document download key” (readonly)
- `attachment` Binary (readonly)
- `show_fetch_status_button` Boolean (compute=_compute_show_fetch_status_button)

Public methods: `action_l10n_ro_edi_download_attachment`, `action_l10n_ro_edi_fetch_status`

## `l10n_ro.cpv.code` (defines)

CPV Code

- `code` Char “Code” (required)
- `name` Char “Name” (required)

## `product.template` (extends)

- `cpv_code_id` Many2one → `l10n_ro.cpv.code` “CPV Code”

## `res.company` (extends)

- `l10n_ro_edi_client_id` Char “eFactura Client ID”
- `l10n_ro_edi_client_secret` Char “Client Secret”
- `l10n_ro_edi_access_token` Char “Access Token”
- `l10n_ro_edi_refresh_token` Char “Refresh Token”
- `l10n_ro_edi_access_expiry_date` Date “Access Token Expiry Date”
- `l10n_ro_edi_refresh_expiry_date` Date “Refresh Token Expiry Date”
- `l10n_ro_edi_callback_url` Char (compute=_compute_l10n_ro_edi_callback_url)
- `l10n_ro_edi_test_env` Boolean “Use Test Environment”
- `l10n_ro_edi_anaf_imported_inv_journal_id` Many2one → `account.journal` “Select journal for SPV imported bills” (store, compute=_compute_l10n_ro_edi_anaf_imported_inv_journal)

## `res.config.settings` (extends)

- `l10n_ro_edi_client_id` Char (related=company_id.l10n_ro_edi_client_id)
- `l10n_ro_edi_client_secret` Char (related=company_id.l10n_ro_edi_client_secret)
- `l10n_ro_edi_access_token` Char (related=company_id.l10n_ro_edi_access_token)
- `l10n_ro_edi_refresh_token` Char (related=company_id.l10n_ro_edi_refresh_token)
- `l10n_ro_edi_access_expiry_date` Date (related=company_id.l10n_ro_edi_access_expiry_date)
- `l10n_ro_edi_refresh_expiry_date` Date (related=company_id.l10n_ro_edi_refresh_expiry_date)
- `l10n_ro_edi_callback_url` Char (related=company_id.l10n_ro_edi_callback_url)
- `l10n_ro_edi_test_env` Boolean (related=company_id.l10n_ro_edi_test_env)
- `l10n_ro_edi_anaf_imported_inv_journal_id` Many2one (related=company_id.l10n_ro_edi_anaf_imported_inv_journal_id)

Public methods: `button_l10n_ro_edi_generate_token`

## `res.partner` (extends)

- `invoice_edi_format` Selection

Extension points: `_get_edi_builder`, `_get_preferred_routing_identifier_vals`, `_get_ubl_cii_formats_info`

## `l10n_ro_edi.account_move_fetch_invoices.wizard` (defines)

Wizard to select date to fetch the invoices from

- `start_date` Date “Synchronize from” (required)
- `nb_days` Integer (compute=_compute_nb_days)

Public methods: `action_l10n_ro_edi_fetch_invoices_from_date`

Extension points: `_check_start_date`

## `account.move.send.wizard` (extends)
