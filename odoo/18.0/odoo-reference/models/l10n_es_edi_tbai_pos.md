# l10n_es_edi_tbai_pos — Spain - Point of Sale + TicketBAI

Depends on: l10n_es_edi_tbai, point_of_sale.

## `pos.order` (extends)

- `l10n_es_tbai_state` Selection “TicketBAI status” (compute=_compute_l10n_es_tbai_state)
- `l10n_es_tbai_chain_index` Integer “TicketBAI chain index” (related=l10n_es_tbai_post_document_id.chain_index)
- `l10n_es_tbai_post_document_id` Many2one → `l10n_es_edi_tbai.document`
- `l10n_es_tbai_post_file` Binary “TicketBAI Post File” (related=l10n_es_tbai_post_document_id.xml_attachment_id.datas)
- `l10n_es_tbai_post_file_name` Char “TicketBAI Post Attachment Name” (related=l10n_es_tbai_post_document_id.xml_attachment_id.name)
- `l10n_es_tbai_is_required` Boolean “TicketBAI required” (related=company_id.l10n_es_tbai_is_enabled)
- `l10n_es_tbai_refund_reason` Selection “Invoice Refund Reason Code (TicketBai)”

Public methods: `action_pos_order_paid`, `get_l10n_es_pos_tbai_qrurl`, `l10n_es_tbai_retry_post`

Extension points: `_prepare_invoice_vals`

## `pos.session` (extends)


## `res.company` (extends)
