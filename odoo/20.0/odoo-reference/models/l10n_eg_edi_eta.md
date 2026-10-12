# l10n_eg_edi_eta — Egypt E-Invoicing

Depends on: l10n_eg.

## `account.journal` (extends)

- `l10n_eg_branch_id` Many2one → `res.partner` “Branch”
- `l10n_eg_activity_type_id` Many2one → `l10n_eg_edi.activity.type`
- `l10n_eg_branch_identifier` Char “Branch ID”

## `account.move` (extends)

- `l10n_eg_long_id` Char “ETA Long ID” (compute=_compute_eta_long_id)
- `l10n_eg_qr_code` Char “ETA QR Code” (compute=_compute_eta_qr_code_str)
- `l10n_eg_uuid` Char “Document UUID” (store, compute=_compute_l10n_eg_edi_uuid)
- `l10n_eg_eta_json_doc_file` Binary “ETA JSON Document”
- `l10n_eg_eta_submission_ids` One2many → `l10n_eg_edi.eta.submission` “ETA Submissions”
- `l10n_eg_edi_api_mode` Selection “ETA Mode” (related=company_id.l10n_eg_edi_api_mode)
- `l10n_eg_edi_submission_state` Selection “ETA State” (store, compute=_compute_l10n_eg_edi_submission_values)
- `l10n_eg_signing_time` Datetime “Signing Time”
- `l10n_eg_is_signed` Boolean “Is Signed”

Public methods: `action_l10n_eg_cancel_invoice`, `action_post_sign_invoices`, `button_draft`, `l10n_eg_log_on_sign_failure`

Extension points: `_action_get_eta_invoice_pdf`, `_get_fields_to_detach`, `_get_l10n_eg_edi_alerts`, `_get_l10n_eg_eta_document_type`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `l10n_eg_edi.activity.type` (defines)

ETA code for activity type

- `name` Char (required)
- `code` Char (required)

## `l10n_eg_edi.eta.submission` (defines)

ETA Submission Details

- `move_id` Many2one → `account.move` “Invoice” (readonly)
- `eta_document_uuid` Char “Document UUID”
- `eta_document_longid` Char “Document Long ID”
- `eta_submission_id` Char “Submission ID”
- `state` Selection “State”
- `message` Char “Response Message”
- `eta_json_filename` Char “File”

Public methods: `action_resign`, `action_retry`

## `l10n_eg_edi.thumb.drive` (defines)

Thumb drive used to sign invoices in Egypt

- `user_id` Many2one → `res.users` (required)
- `company_id` Many2one → `res.company` (required)
- `certificate` Binary “ETA Certificate”
- `pin` Char “ETA USB Pin” (required)
- `access_token` Char (required)

Public methods: `action_set_certificate_from_usb`, `action_sign_invoices`, `set_certificate`, `set_signature_data`

Extension points: `_get_host`

## `ir.attachment` (extends)


## `product.template` (extends)

- `l10n_eg_eta_code` Char “Item code” (compute=_compute_l10n_eg_eta_code)

Public methods: `action_open_eta_codes_portal`, `create`

## `product.product` (extends)

- `l10n_eg_eta_code` Char “ETA Code” (company_dependent)

Public methods: `action_open_eta_codes_portal`

## `res.company` (extends)

- `l10n_eg_client_identifier` Char “ETA Client ID”
- `l10n_eg_client_secret` Char “ETA Client Secret”
- `l10n_eg_edi_api_mode` Selection “ETA Invoice Sending Mode”
- `l10n_eg_building_no` Char “Building No.” (compute=_compute_address)

Extension points: `_get_company_address_field_names`, `_get_invoicing_threshold`

## `res.config.settings` (extends)

- `l10n_eg_client_identifier` Char (related=company_id.l10n_eg_client_identifier)
- `l10n_eg_client_secret` Char (related=company_id.l10n_eg_client_secret)
- `l10n_eg_edi_api_mode` Selection (related=company_id.l10n_eg_edi_api_mode)

## `res.currency.rate` (extends)


## `res.partner` (extends)

- `l10n_eg_building_no` Char “Building No.”

Extension points: `_check_l10n_eg_missing_address_data`

## `l10n_eg_edi.uom.code` (defines)

ETA code for the unit of measures

- `name` Char (required)
- `code` Char (required)

## `uom.uom` (extends)

- `l10n_eg_unit_code_id` Many2one → `l10n_eg_edi.uom.code` “ETA Unit Code”

## `l10n_eg_edi.cancel.wizard` (defines)

Wizard to cancel an invoice in ETA

- `move_ids` Many2many → `account.move` (required)
- `l10n_eg_eta_cancellation_reason` Char “ETA Reason” (required)

Public methods: `action_cancel_invoice`
