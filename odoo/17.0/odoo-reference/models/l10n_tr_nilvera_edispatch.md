# l10n_tr_nilvera_edispatch — Türkiye - e-Irsaliye (e-Dispatch)

Depends on: l10n_tr_nilvera, stock, stock_account.

## `l10n_tr.nilvera.trailer.plate` (defines)

GİB Plate numbers

- `name` Char “GİB Plate Number”
- `plate_number_type` Selection “Plate Number” (required)

## `res.partner` (extends)

- `l10n_tr_nilvera_edispatch_customs_zip` Char “Customs ZIP”

## `stock.picking` (extends)

- `l10n_tr_nilvera_dispatch_type` Selection “Dispatch Type”
- `l10n_tr_nilvera_carrier_id` Many2one → `res.partner` “Carrier (TR)”
- `l10n_tr_nilvera_buyer_id` Many2one → `res.partner` “Buyer”
- `l10n_tr_nilvera_seller_supplier_id` Many2one → `res.partner` “Seller Supplier”
- `l10n_tr_nilvera_buyer_originator_id` Many2one → `res.partner` “Buyer Originator”
- `l10n_tr_nilvera_delivery_printed_number` Char “Printed Delivery Note Number”
- `l10n_tr_nilvera_delivery_date` Date “Printed Delivery Note Date”
- `l10n_tr_vehicle_plate` Many2one → `l10n_tr.nilvera.trailer.plate` “Vehicle Plate”
- `l10n_tr_nilvera_trailer_plate_ids` Many2many → `l10n_tr.nilvera.trailer.plate` “Trailer Plates”
- `l10n_tr_nilvera_driver_ids` Many2many → `res.partner` “Drivers”
- `l10n_tr_nilvera_delivery_notes` Char “Delivery Notes”
- `l10n_tr_nilvera_dispatch_state` Selection “e-Dispatch State”
- `l10n_tr_nilvera_edispatch_warnings` Json (compute=_compute_edispatch_warnings)

Public methods: `action_generate_l10n_tr_edispatch_xml`, `action_mark_l10n_tr_edispatch_status`, `button_validate`

## `stock.picking.type` (extends)
