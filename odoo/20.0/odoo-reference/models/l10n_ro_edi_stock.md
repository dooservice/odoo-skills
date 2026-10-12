# l10n_ro_edi_stock — Romania - E-Transport

Depends on: stock_delivery, l10n_ro_edi.

## `delivery.carrier` (extends)

- `l10n_ro_edi_stock_partner_id` Many2one → `res.partner` “Partner”

## `l10n_ro_edi.document` (extends)

- `invoice_id` Many2one
- `picking_id` Many2one → `stock.picking`
- `batch_id` Many2one → `stock.picking.batch`
- `state` Selection
- `message` Char “Message”
- `l10n_ro_edi_stock_uit` Char
- `l10n_ro_edi_stock_load_id` Char

## `stock.picking` (extends)

- `l10n_ro_edi_stock_document_ids` One2many → `l10n_ro_edi.document`
- `l10n_ro_edi_stock_document_uit` Char “eTransport UIT” (compute=_compute_l10n_ro_edi_stock_current_document_uit)
- `l10n_ro_edi_stock_state` Selection “eTransport Status” (store, compute=_compute_l10n_ro_edi_stock_current_document_state)
- `l10n_ro_edi_stock_operation_type` Selection “eTransport Operation Type”
- `l10n_ro_edi_stock_available_operation_scopes` Char (compute=_compute_l10n_ro_edi_stock_available_operation_scopes)
- `l10n_ro_edi_stock_operation_scope` Selection “Operation Scope”
- `l10n_ro_edi_stock_vehicle_number` Char “Vehicle Number”
- `l10n_ro_edi_stock_trailer_1_number` Char “Trailer 1 Number”
- `l10n_ro_edi_stock_trailer_2_number` Char “Trailer 2 Number”
- `l10n_ro_edi_stock_available_start_loc_types` Char (compute=_compute_l10n_ro_edi_stock_available_location_types)
- `l10n_ro_edi_stock_start_loc_type` Selection “Start Location Type” (store, compute=_compute_l10n_ro_edi_stock_default_location_type)
- `l10n_ro_edi_stock_available_end_loc_types` Char (compute=_compute_l10n_ro_edi_stock_available_location_types)
- `l10n_ro_edi_stock_end_loc_type` Selection “End Location Type” (store, compute=_compute_l10n_ro_edi_stock_default_location_type)
- `l10n_ro_edi_stock_start_bcp` Selection “Start Border Crossing Point”
- `l10n_ro_edi_stock_start_customs_office` Selection “Start Customs Office”
- `l10n_ro_edi_stock_end_bcp` Selection “End Border Crossing Point”
- `l10n_ro_edi_stock_end_customs_office` Selection “End Customs Office”
- `l10n_ro_edi_stock_remarks` Text “Remarks”
- `l10n_ro_edi_stock_enable` Boolean (compute=_compute_l10n_ro_edi_stock_enable)
- `l10n_ro_edi_stock_enable_send` Boolean (compute=_compute_l10n_ro_edi_stock_enable_send)
- `l10n_ro_edi_stock_enable_fetch` Boolean (compute=_compute_l10n_ro_edi_stock_enable_fetch)
- `l10n_ro_edi_stock_enable_amend` Boolean (compute=_compute_l10n_ro_edi_stock_enable_amend)
- `l10n_ro_edi_stock_fields_readonly` Boolean (compute=_compute_l10n_ro_edi_stock_fields_readonly)

Public methods: `action_l10n_ro_edi_stock_fetch_status`, `action_l10n_ro_edi_stock_send_etransport`, `button_validate`

## `stock.picking.batch` (extends)

- `l10n_ro_edi_stock_document_ids` One2many → `l10n_ro_edi.document`
- `l10n_ro_edi_stock_document_uit` Char “eTransport UIT” (compute=_compute_l10n_ro_edi_stock_current_document_uit)
- `l10n_ro_edi_stock_state` Selection “eTransport Status” (store, compute=_compute_l10n_ro_edi_stock_current_document_state)
- `l10n_ro_edi_stock_operation_type` Selection “eTransport Operation Type”
- `l10n_ro_edi_stock_available_operation_scopes` Char (compute=_compute_l10n_ro_edi_stock_available_operation_scopes)
- `l10n_ro_edi_stock_operation_scope` Selection “Operation Scope”
- `l10n_ro_edi_stock_vehicle_number` Char “Vehicle Number”
- `l10n_ro_edi_stock_trailer_1_number` Char “Trailer 1 Number”
- `l10n_ro_edi_stock_trailer_2_number` Char “Trailer 2 Number”
- `l10n_ro_edi_stock_available_start_loc_types` Char (compute=_compute_l10n_ro_edi_stock_available_location_types)
- `l10n_ro_edi_stock_start_loc_type` Selection “Start Location Type” (store, compute=_compute_l10n_ro_edi_stock_default_location_type)
- `l10n_ro_edi_stock_available_end_loc_types` Char (compute=_compute_l10n_ro_edi_stock_available_location_types)
- `l10n_ro_edi_stock_end_loc_type` Selection “End Location Type” (store, compute=_compute_l10n_ro_edi_stock_default_location_type)
- `l10n_ro_edi_stock_start_bcp` Selection “Start Border Crossing Point”
- `l10n_ro_edi_stock_start_customs_office` Selection “Start Customs Office”
- `l10n_ro_edi_stock_end_bcp` Selection “End Border Crossing Point”
- `l10n_ro_edi_stock_end_customs_office` Selection “End Customs Office”
- `l10n_ro_edi_stock_remarks` Text “Remarks”
- `l10n_ro_edi_stock_enable` Boolean (compute=_compute_l10n_ro_edi_stock_enable)
- `l10n_ro_edi_stock_enable_send` Boolean (compute=_compute_l10n_ro_edi_stock_enable_send)
- `l10n_ro_edi_stock_enable_fetch` Boolean (compute=_compute_l10n_ro_edi_stock_enable_fetch)
- `l10n_ro_edi_stock_enable_amend` Boolean (compute=_compute_l10n_ro_edi_stock_enable_amend)
- `l10n_ro_edi_stock_fields_readonly` Boolean (compute=_compute_l10n_ro_edi_stock_fields_readonly)

Public methods: `action_done`, `action_l10n_ro_edi_stock_fetch_status`, `action_l10n_ro_edi_stock_send_etransport`
