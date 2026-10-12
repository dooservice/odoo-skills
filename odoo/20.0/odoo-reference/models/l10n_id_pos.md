# l10n_id_pos — Indonesia - Point of Sale

Depends on: l10n_id, point_of_sale.

## `pos.order` (extends)

- `l10n_id_qris_transaction_ids` Many2many → `l10n_id.qris.transaction`

## `pos.payment.method` (extends)


Public methods: `l10n_id_verify_qris_status`

## `l10n_id.qris.transaction` (extends)


Extension points: `_get_record`, `_get_supported_models`
