# l10n_sa_edi_pos — Saudi Arabia - E-invoicing (Simplified)

Depends on: l10n_sa_pos, l10n_sa_edi.

## `account.edi.xml.ubl_21.zatca` (extends)


## `account.move` (extends)


Public methods: `l10n_sa_pos_ensure_invoice_pdf`

## `l10n_sa_edi.document` (extends)

- `pos_order_id` Many2one → `pos.order` (compute=_compute_resource)

## `pos.order` (extends)

- `l10n_sa_invoice_qr_code_str` Char “ZATCA QR Code” (related=account_move.l10n_sa_qr_code_str)
- `l10n_sa_invoice_edi_state` Selection “Electronic invoicing” (related=account_move.l10n_sa_edi_state)

Extension points: `_get_l10n_sa_journal`

## `res.company` (extends)


## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`
