# l10n_sa_edi_pos — Saudi Arabia - E-invoicing (Simplified)

Depends on: l10n_sa_pos, l10n_sa_edi.

## `account.edi.format` (extends)


Extension points: `_get_move_applicability`

## `account.edi.xml.ubl_21.zatca` (extends)


## `account.move` (extends)


Public methods: `l10n_sa_pos_ensure_invoice_pdf`

## `pos.config` (extends)


Public methods: `open_ui`

## `pos.order` (extends)

- `l10n_sa_invoice_qr_code_str` Char “ZATCA QR Code” (related=account_move.l10n_sa_qr_code_str)
- `l10n_sa_invoice_edi_state` Selection “Electronic invoicing” (related=account_move.edi_state)

## `res.company` (extends)
