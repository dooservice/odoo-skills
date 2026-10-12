# l10n_vn_edi_viettel_pos — Vietnam - POS E-invoicing

Depends on: l10n_vn_edi_viettel, point_of_sale.

## `account.move` (extends)


Public methods: `l10n_vn_edi_fetch_invoice_files`

Extension points: `_get_invoice_legal_documents`

## `pos.config` (extends)

- `l10n_vn_auto_send_to_sinvoice` Boolean “Auto-send to SInvoice”
- `l10n_vn_pos_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “POS Symbol” (store, compute=_compute_l10n_vn_pos_symbol)

## `pos.order` (extends)

- `l10n_vn_credit_note_reason` Char “Credit Note Reason”
- `l10n_vn_has_sinvoice_pdf` Boolean “SInvoice PDF Available” (compute=_compute_sinvoice_has_pdf)
- `l10n_vn_sinvoice_state` Selection (related=account_move.l10n_vn_edi_invoice_state)

Extension points: `_create_invoice`, `_prepare_invoice_vals`

## `pos.session` (extends)


## `res.company` (extends)

- `l10n_vn_pos_default_symbol` Many2one → `l10n_vn_edi_viettel.sinvoice.symbol` “Default PoS Symbol”

## `res.config.settings` (extends)

- `l10n_vn_edi_pos_default_symbol` Many2one “Default PoS Symbol” (related=company_id.l10n_vn_pos_default_symbol)
- `pos_l10n_vn_pos_symbol` Many2one (related=pos_config_id.l10n_vn_pos_symbol)
- `pos_l10n_vn_auto_send_to_sinvoice` Boolean (related=pos_config_id.l10n_vn_auto_send_to_sinvoice)

## `res.partner` (extends)
