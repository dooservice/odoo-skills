# l10n_es_edi_verifactu_pos — Spain - Veri*Factu for Point of Sale

Depends on: l10n_es_edi_verifactu, point_of_sale.

## `account.move` (extends)


## `pos.config` (extends)

- `l10n_es_edi_verifactu_required` Boolean “Veri*Factu Required” (related=company_id.l10n_es_edi_verifactu_required)

## `pos.order` (extends)

- `l10n_es_edi_verifactu_required` Boolean “Veri*Factu Required” (related=company_id.l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_document_ids` One2many → `l10n_es_edi_verifactu.document` “Veri*Factu Documents”
- `l10n_es_edi_verifactu_state` Selection “Veri*Factu Status” (store, compute=_compute_l10n_es_edi_verifactu_state)
- `l10n_es_edi_verifactu_warning_level` Char “Veri*Factu Warning Level” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_warning` Html “Veri*Factu Warning” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_qr_code` Char “Veri*Factu QR Code” (compute=_compute_l10n_es_edi_verifactu_qr_code)
- `l10n_es_edi_verifactu_show_cancel_button` Boolean “Show Veri*Factu Cancel Button” (compute=_compute_l10n_es_edi_verifactu_show_cancel_button)
- `l10n_es_edi_verifactu_refund_reason` Selection “Veri*Factu Refund Reason”

Public methods: `action_pos_order_paid`, `l10n_es_edi_verifactu_button_cancel`, `l10n_es_edi_verifactu_button_send`

Extension points: `_prepare_invoice_vals`

## `pos.session` (extends)


## `res.company` (extends)


## `l10n_es_edi_verifactu.document` (extends)

- `pos_order_id` Many2one → `pos.order` “PoS Order” (readonly)
