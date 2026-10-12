# l10n_gr_edi_delivery_note — Greece - myDATA Delivery Note

Depends on: l10n_gr_edi, stock, sale, sale_stock.

## `account.move` (extends)

- `l10n_gr_edi_correlated_picking_ids` Many2many → `stock.picking` “Correlated Delivery Notes” (compute=_compute_l10n_gr_edi_correlated_picking_ids)

## `l10n_gr_edi.document` (extends)

- `picking_id` Many2one → `stock.picking`
- `state` Selection

## `stock.move` (extends)

- `l10n_gr_edi_measurement_unit` Selection “myDATA Unit of Measure” (store, compute=_compute_l10n_gr_edi_measurement_unit)

Extension points: `_get_new_picking_values`

## `stock.picking` (extends)

- `is_greek_company` Boolean (compute=_compute_is_greek_company)
- `l10n_gr_edi_mark` Char “Mark” (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_document_ids` One2many → `l10n_gr_edi.document` (readonly)
- `l10n_gr_edi_state` Selection “myDATA Status” (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_attachment_id` Many2one → `ir.attachment` (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_alerts` Json (compute=_compute_l10n_gr_edi_alerts)
- `l10n_gr_edi_move_purpose` Selection “Move Purpose” (store)
- `l10n_gr_edi_other_move_purpose` Char
- `l10n_gr_edi_loading_address_street` Char
- `l10n_gr_edi_loading_address_number` Char
- `l10n_gr_edi_loading_address_zip` Char
- `l10n_gr_edi_loading_address_city` Char
- `l10n_gr_edi_delivery_address_street` Char
- `l10n_gr_edi_delivery_address_number` Char
- `l10n_gr_edi_delivery_address_zip` Char
- `l10n_gr_edi_delivery_address_city` Char
- `l10n_gr_edi_vehicle_number` Char “Vehicule number”

Public methods: `action_l10n_gr_edi_try_send_delivery_note`

Extension points: `_prepare_return_picking_default_values`
