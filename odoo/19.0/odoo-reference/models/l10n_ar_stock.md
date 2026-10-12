# l10n_ar_stock — Argentinean - Stock

Depends on: l10n_ar, stock_account.

## `stock.picking` (extends)

- `l10n_ar_delivery_guide_number` Char “Delivery Guide No.” (readonly)
- `l10n_ar_cai_data` Json “CAI Data”
- `l10n_ar_allow_generate_delivery_guide` Boolean (compute=_compute_l10n_ar_delivery_guide_flags)
- `l10n_ar_allow_send_delivery_guide` Boolean (compute=_compute_l10n_ar_delivery_guide_flags)

Public methods: `l10n_ar_action_create_delivery_guide`, `l10n_ar_action_send_delivery_guide`

## `stock.picking.type` (extends)

- `l10n_ar_document_type_id` Many2one → `l10n_latam.document.type` “Document Type”
- `l10n_ar_cai_authorization_code` Char “CAI”
- `l10n_ar_cai_expiration_date` Date “CAI Expiration Date”
- `l10n_ar_sequence_number_start` Char “Sequence From”
- `l10n_ar_sequence_number_end` Char “Sequence To”
- `l10n_ar_delivery_sequence_prefix` Char “Delivery Guide Prefix” (compute=_compute_l10n_ar_stock_sequence_fields)
- `l10n_ar_next_delivery_number` Integer “Next Delivery Guide Number” (compute=_compute_l10n_ar_stock_sequence_fields)
- `l10n_ar_sequence_id` Many2one → `ir.sequence` “Delivery Guide Number Sequence”

Extension points: `_get_allowed_document_type_ids`
