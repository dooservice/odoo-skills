# l10n_in_ewaybill_stock — Indian - E-waybill Stock

Depends on: l10n_in_stock, l10n_in_ewaybill.

## `l10n.in.ewaybill` (extends)

- `state` Selection
- `type_description` Char “Description”
- `picking_id` Many2one → `stock.picking`
- `move_ids` One2many (related=picking_id.move_ids)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position)

Public methods: `action_print`, `action_reset_to_pending`, `action_set_to_challan`

Extension points: `_check_lines`, `_check_state`, `_get_ewaybill_company`, `_get_ewaybill_dependencies`, `_get_ewaybill_document_details`, `_get_l10n_in_ewaybill_line_details`, `_get_seller_buyer_details`, `_prepare_ewaybill_base_json_payload`, `_prepare_ewaybill_tax_details_json_payload`

## `stock.move` (extends)

Stock Move Ewaybill

- `l10n_in_ewaybill_ids` One2many (related=picking_id.l10n_in_ewaybill_ids)
- `company_currency_id` Many2one (related=company_id.currency_id)
- `ewaybill_price_unit` Monetary (store, compute=_compute_l10n_in_ewaybill_price_unit)
- `ewaybill_tax_ids` Many2many → `account.tax` “Taxes” (store, compute=_compute_l10n_in_tax_ids)

## `stock.picking` (extends)

- `l10n_in_ewaybill_ids` One2many → `l10n.in.ewaybill` “Ewaybill”
- `l10n_in_ewaybill_name` Char “Indian Ewaybill Number” (compute=_compute_l10n_in_ewaybill_details)
- `l10n_in_ewaybill_feature_enabled` Boolean (related=company_id.l10n_in_ewaybill_feature)

Public methods: `action_l10n_in_ewaybill_create`, `action_open_l10n_in_ewaybill`

Extension points: `_get_l10n_in_ewaybill_form_action`
