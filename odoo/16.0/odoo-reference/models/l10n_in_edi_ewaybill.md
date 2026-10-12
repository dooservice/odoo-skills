# l10n_in_edi_ewaybill — Indian - E-waybill

Depends on: l10n_in_edi.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_l10n_in_edi_ewaybill_line_details`, `_get_l10n_in_edi_saler_buyer_party`, `_get_move_applicability`

## `account.move` (extends)

- `l10n_in_type_id` Many2one → `l10n.in.ewaybill.type`
- `l10n_in_distance` Integer “Distance”
- `l10n_in_mode` Selection “Transportation Mode”
- `l10n_in_vehicle_no` Char “Vehicle Number”
- `l10n_in_vehicle_type` Selection “Vehicle Type”
- `l10n_in_transportation_doc_no` Char “E-waybill Document Number”
- `l10n_in_transportation_doc_date` Date “Document Date”
- `l10n_in_transporter_id` Many2one → `res.partner`
- `l10n_in_edi_ewaybill_direct_api` Boolean “E-waybill(IN) direct API” (compute=_compute_l10n_in_edi_ewaybill_direct)
- `l10n_in_edi_ewaybill_show_send_button` Boolean “Show Send E-waybill Button” (compute=_compute_l10n_in_edi_ewaybill_show_send_button)

Public methods: `button_cancel_posted_moves`, `l10n_in_edi_ewaybill_send`

Extension points: `_get_l10n_in_edi_ewaybill_response_json`

## `l10n.in.ewaybill.type` (defines)

E-Waybill Document Type

- `name` Char “Type”
- `code` Char “Type Code”
- `sub_type` Char “Sub-type”
- `sub_type_code` Char “Sub-type Code”
- `allowed_supply_type` Selection “Allowed for supply type”
- `active` Boolean “Active”

Public methods: `name_get`

## `res.company` (extends)

- `l10n_in_edi_ewaybill_username` Char “E-Waybill (IN) Username”
- `l10n_in_edi_ewaybill_password` Char “E-Waybill (IN) Password”
- `l10n_in_edi_ewaybill_auth_validity` Datetime “E-Waybill (IN) Valid Until”

## `res.config.settings` (extends)

- `l10n_in_edi_ewaybill_username` Char “Indian EDI Stock username” (related=company_id.l10n_in_edi_ewaybill_username)
- `l10n_in_edi_ewaybill_password` Char “Indian EDI Stock password” (related=company_id.l10n_in_edi_ewaybill_password)

Public methods: `l10n_in_edi_ewaybill_test`
