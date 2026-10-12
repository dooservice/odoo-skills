# l10n_it_stock_ddt — l10n_it_stock_ddt

Depends on: l10n_it_edi, delivery, stock_account.

## `account.edi.format` (extends)


## `account.move` (extends)

- `l10n_it_ddt_ids` Many2many → `stock.picking` (compute=_compute_ddt_ids)
- `l10n_it_ddt_count` Integer (compute=_compute_ddt_ids)

Public methods: `get_linked_ddts`

Extension points: `_get_ddt_values`, `_prepare_fatturapa_export_values`

## `stock.picking` (extends)

- `l10n_it_transport_reason` Selection “Transport Reason”
- `l10n_it_transport_method` Selection “Transport Method”
- `l10n_it_transport_method_details` Char “Transport Note”
- `l10n_it_parcels` Integer “Parcels”
- `l10n_it_ddt_number` Char “DDT Number” (readonly)
- `l10n_it_show_print_ddt_button` Boolean (compute=_compute_l10n_it_show_print_ddt_button)

Extension points: `_action_done`

## `stock.picking.type` (extends)

- `l10n_it_ddt_sequence_id` Many2one → `ir.sequence`

Public methods: `create`, `write`

Extension points: `_get_dtt_ir_seq_vals`
