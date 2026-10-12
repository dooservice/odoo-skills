# l10n_in_ewaybill_stock — Indian - E-waybill Stock

Depends on: l10n_in_stock, l10n_in_edi_ewaybill.

## `l10n.in.ewaybill` (defines)

e-Waybill

Inherits: `portal.mixin`, `mail.thread`, `mail.activity.mixin`

- `name` Char “e-Waybill Number” (readonly)
- `ewaybill_date` Date “e-Waybill Date” (readonly)
- `ewaybill_expiry_date` Date “e-Waybill Valid Upto” (readonly)
- `state` Selection “Status” (required, readonly)
- `picking_id` Many2one → `stock.picking`
- `move_ids` One2many (related=picking_id.move_ids)
- `picking_type_code` Selection (related=picking_id.picking_type_id.code)
- `document_date` Datetime “Document Date” (related=picking_id.date_done)
- `document_number` Char “Document” (related=picking_id.name)
- `company_id` Many2one → `res.company` (related=picking_id.company_id)
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
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position)
- `type_id` Many2one → `l10n.in.ewaybill.type` (required)
- `sub_type_code` Char (related=type_id.sub_type_code)
- `type_description` Char “Description”
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

Public methods: `action_export_json`, `action_print`, `action_set_to_challan`, `cancel_ewaybill`, `generate_ewaybill`, `reset_to_pending`

Extension points: `_check_configuration`, `_check_document_number`, `_check_gst_treatment`, `_check_lines`, `_check_partners`, `_check_transporter`, `_get_default_help_message`, `_get_gst_treatment`, `_get_l10n_in_ewaybill_line_details`, `_get_partner_state_code`, `_prepare_ewaybill_base_json_payload`, `_prepare_ewaybill_tax_details_json_payload`, `_prepare_ewaybill_transportation_json_payload`

## `stock.move` (extends)

Stock Move Ewaybill

- `l10n_in_ewaybill_id` One2many (related=picking_id.l10n_in_ewaybill_id)
- `company_currency_id` Many2one (related=company_id.currency_id)
- `ewaybill_price_unit` Monetary (store, compute=_compute_l10n_in_ewaybill_price_unit)
- `ewaybill_tax_ids` Many2many → `account.tax` “Taxes” (store, compute=_compute_l10n_in_tax_ids)

## `stock.picking` (extends)

- `l10n_in_ewaybill_id` One2many → `l10n.in.ewaybill` “Ewaybill”

Public methods: `action_l10n_in_ewaybill_create`, `action_open_l10n_in_ewaybill`

Extension points: `_get_l10n_in_ewaybill_form_action`

## `l10n.in.ewaybill.cancel` (defines)

Cancel Ewaybill

- `l10n_in_ewaybill_id` Many2one → `l10n.in.ewaybill` “Ewaybill” (required)
- `cancel_reason` Selection “Cancel Reason” (required)
- `cancel_remarks` Char “Cancel Remarks”

Public methods: `cancel_ewaybill`
