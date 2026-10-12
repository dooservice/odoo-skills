# l10n_eg_edi_eta — Egypt E-Invoicing

Depends on: account_edi, l10n_eg.

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_move_applicability`

## `account.journal` (extends)

- `l10n_eg_branch_id` Many2one → `res.partner` “Branch”
- `l10n_eg_activity_type_id` Many2one → `l10n_eg_edi.activity.type`
- `l10n_eg_branch_identifier` Char “ETA Branch ID”

## `account.move` (extends)

- `l10n_eg_long_id` Char “ETA Long ID” (compute=_compute_eta_long_id)
- `l10n_eg_qr_code` Char “ETA QR Code” (compute=_compute_eta_qr_code_str)
- `l10n_eg_submission_number` Char “Submission ID” (store, compute=_compute_eta_response_data)
- `l10n_eg_uuid` Char “Document UUID” (store, compute=_compute_eta_response_data)
- `l10n_eg_eta_json_doc_file` Binary “ETA JSON Document”
- `l10n_eg_signing_time` Datetime “Signing Time”
- `l10n_eg_is_signed` Boolean

Public methods: `action_get_eta_invoice_pdf`, `action_post_sign_invoices`, `button_draft`

Extension points: `_get_fields_to_detach`

## `l10n_eg_edi.activity.type` (defines)

ETA code for activity type

- `name` Char (required)
- `code` Char (required)

## `l10n_eg_edi.thumb.drive` (defines)

Thumb drive used to sign invoices in Egypt

- `user_id` Many2one → `res.users` (required)
- `company_id` Many2one → `res.company` (required)
- `certificate` Binary “ETA Certificate”
- `pin` Char “ETA USB Pin” (required)
- `access_token` Char (required)

Public methods: `action_set_certificate_from_usb`, `action_sign_invoices`, `set_certificate`, `set_signature_data`

Extension points: `_get_host`

## `product.template` (extends)

- `l10n_eg_eta_code` Char “ETA Item code” (compute=_compute_l10n_eg_eta_code)

Public methods: `create`

## `product.product` (extends)

- `l10n_eg_eta_code` Char “ETA Code”

## `res.company` (extends)

- `l10n_eg_client_identifier` Char “ETA Client ID”
- `l10n_eg_client_secret` Char “ETA Secret”
- `l10n_eg_production_env` Boolean “In Production Environment”
- `l10n_eg_invoicing_threshold` Float “Invoicing Threshold”

## `res.config.settings` (extends)

- `l10n_eg_client_identifier` Char (related=company_id.l10n_eg_client_identifier)
- `l10n_eg_client_secret` Char (related=company_id.l10n_eg_client_secret)
- `l10n_eg_production_env` Boolean (related=company_id.l10n_eg_production_env)
- `l10n_eg_invoicing_threshold` Float (related=company_id.l10n_eg_invoicing_threshold)

## `res.currency.rate` (extends)


## `res.partner` (extends)

- `l10n_eg_building_no` Char “Building No.”

## `l10n_eg_edi.uom.code` (defines)

ETA code for the unit of measures

- `name` Char (required)
- `code` Char (required)

## `uom.uom` (extends)

- `l10n_eg_unit_code_id` Many2one → `l10n_eg_edi.uom.code` “ETA Unit Code”
