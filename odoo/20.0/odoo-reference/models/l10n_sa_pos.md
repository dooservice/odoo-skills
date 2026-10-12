# l10n_sa_pos — Saudi Arabia - Point of Sale

Depends on: l10n_gcc_pos, l10n_sa.

## `pos.config` (extends)


Public methods: `open_ui`

## `pos.order` (extends)

- `l10n_sa_reason` Selection “ZATCA Reason”
- `l10n_sa_reason_value` Char (compute=_compute_l10n_sa_reason_value)

Extension points: `_get_l10n_sa_totals`, `_prepare_invoice_vals`

## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `compute_sa_qr_code`, `order_receipt_generate_data`
