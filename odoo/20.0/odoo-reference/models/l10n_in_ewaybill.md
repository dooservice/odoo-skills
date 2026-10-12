# l10n_in_ewaybill — Indian - E-waybill

Depends on: l10n_in.

## `account.chart.template` (extends)


## `account.move` (extends)

- `l10n_in_ewaybill_ids` One2many → `l10n.in.ewaybill` “E-Waybill” (readonly)
- `l10n_in_ewaybill_name` Char “Indian Ewaybill Number” (compute=_compute_l10n_in_ewaybill_details)
- `l10n_in_ewaybill_expiry_date` Datetime (compute=_compute_l10n_in_ewaybill_details)
- `l10n_in_ewaybill_feature_enabled` Boolean “E-Waybill Feature Enabled” (related=company_id.l10n_in_ewaybill_feature)

Public methods: `action_l10n_in_ewaybill_create`, `action_open_l10n_in_ewaybill`

Extension points: `_get_l10n_in_ewaybill_form_action`

## `l10n.in.ewaybill.type` (defines)

E-Waybill Document Type

- `name` Char “Type”
- `code` Char “Type Code”
- `sub_type` Char “Sub-type”
- `sub_type_code` Char “Sub-type Code”
- `allowed_supply_type` Selection “Allowed for supply type”
- `active` Boolean “Active”

## `ir.attachment` (extends)


## `l10n.in.ewaybill` (defines)

e-Waybill

Inherits: `portal.mixin`, `mail.thread`, `mail.activity.mixin`

- `name` Char “e-Waybill Number” (readonly)
- `ewaybill_date` Date “e-Waybill Date” (readonly)
- `ewaybill_expiry_date` Date “e-Waybill Valid Upto” (readonly)
- `state` Selection “Status” (required, readonly)
- `account_move_id` Many2one → `account.move` (readonly)
- `document_date` Datetime “Document Date” (compute=_compute_ewaybill_document_details)
- `document_number` Char “Document” (compute=_compute_ewaybill_document_details)
- `company_id` Many2one → `res.company` (store, compute=_compute_ewaybill_company)
- `company_currency_id` Many2one (related=company_id.currency_id)
- `supply_type` Selection “Supply Type” (compute=_compute_supply_type)
- `partner_bill_from_id` Many2one → `res.partner` “Bill From” (store, compute=_compute_document_partners_details)
- `partner_bill_to_id` Many2one → `res.partner` “Bill To” (store, compute=_compute_document_partners_details)
- `partner_ship_from_id` Many2one → `res.partner` “Dispatch From” (store, compute=_compute_document_partners_details)
- `partner_ship_to_id` Many2one → `res.partner` “Ship To” (store, compute=_compute_document_partners_details)
- `is_bill_to_editable` Boolean (compute=_compute_is_editable)
- `is_bill_from_editable` Boolean (compute=_compute_is_editable)
- `is_ship_to_editable` Boolean (compute=_compute_is_editable)
- `is_ship_from_editable` Boolean (compute=_compute_is_editable)
- `type_id` Many2one → `l10n.in.ewaybill.type`
- `sub_type_code` Char (related=type_id.sub_type_code)
- `distance` Integer “Distance”
- `mode` Selection “Transportation Mode”
- `vehicle_no` Char “Vehicle Number”
- `vehicle_type` Selection “Vehicle Type” (store, compute=_compute_vehicle_type)
- `transportation_doc_no` Char “Transporter Doc No”
- `transportation_doc_date` Date “Transporter Doc Date”
- `transporter_id` Many2one → `res.partner`
- `error_message` Html (readonly)
- `blocking_level` Selection “Blocking Level” (readonly)
- `content` Binary (compute=_compute_content)
- `cancel_reason` Selection “Cancel reason”
- `cancel_remarks` Char “Cancel remarks”
- `attachment_id` Many2one → `ir.attachment`
- `attachment_file` Binary

Public methods: `action_cancel_ewaybill`, `action_export_content_json`, `action_generate_ewaybill`, `action_print`, `action_reset_to_pending`

Extension points: `_check_configuration`, `_check_document_number`, `_check_gst_treatment`, `_check_lines`, `_check_partners`, `_check_pincode`, `_check_state`, `_check_transporter`, `_create_and_post_response_attachment`, `_get_billing_partner`, `_get_cancellation_request_vals`, `_get_default_help_message`, `_get_ewaybill_company`, `_get_ewaybill_dependencies`, `_get_ewaybill_document_details`, `_get_l10n_in_ewaybill_line_details`, `_get_partner_state_code`, `_get_seller_buyer_details`, `_prepare_ewaybill_base_json_payload`, `_prepare_ewaybill_tax_details_json_payload`, `_prepare_ewaybill_transportation_json_payload`

## `res.company` (extends)

- `l10n_in_ewaybill_username` Char “E-Waybill Username”
- `l10n_in_ewaybill_password` Char “E-Waybill Password”
- `l10n_in_ewaybill_auth_validity` Datetime “E-Waybill Valid Until”
- `l10n_in_ewaybill_feature` Boolean “E-Waybill”

## `res.config.settings` (extends)

- `l10n_in_ewaybill_username` Char “Indian Ewaybill username” (related=company_id.l10n_in_ewaybill_username)
- `l10n_in_ewaybill_password` Char “Indian Ewaybill password” (related=company_id.l10n_in_ewaybill_password)
- `l10n_in_ewaybill_feature` Boolean (related=company_id.l10n_in_ewaybill_feature)

Public methods: `l10n_in_ewaybill_test`

## `l10n.in.ewaybill.cancel` (defines)

Cancel Ewaybill

- `l10n_in_ewaybill_id` Many2one → `l10n.in.ewaybill` “Ewaybill” (required)
- `cancel_reason` Selection “Cancel Reason” (required)
- `cancel_remarks` Char “Cancel Remarks”

Public methods: `cancel_ewaybill`
