# l10n_es_edi_tbai — Spain - TicketBAI

Depends on: l10n_es, certificate.

## `account.move` (extends)

- `l10n_es_tbai_state` Selection “TicketBAI status” (compute=_compute_l10n_es_tbai_state)
- `l10n_es_tbai_chain_index` Integer “TicketBAI chain index” (related=l10n_es_tbai_post_document_id.chain_index)
- `l10n_es_tbai_post_document_id` Many2one → `l10n_es_edi_tbai.document` (readonly)
- `l10n_es_tbai_cancel_document_id` Many2one → `l10n_es_edi_tbai.document` (readonly)
- `l10n_es_tbai_post_file` Binary “TicketBAI Post File” (related=l10n_es_tbai_post_document_id.xml_attachment_id.datas)
- `l10n_es_tbai_post_file_name` Char “TicketBAI Post Attachment Name” (related=l10n_es_tbai_post_document_id.xml_attachment_id.name)
- `l10n_es_tbai_cancel_file` Binary “TicketBAI Cancel File” (related=l10n_es_tbai_cancel_document_id.xml_attachment_id.datas)
- `l10n_es_tbai_cancel_file_name` Char “TicketBAI Cancel File Name” (related=l10n_es_tbai_cancel_document_id.xml_attachment_id.name)
- `l10n_es_tbai_is_required` Boolean “TicketBAI required” (compute=_compute_l10n_es_tbai_is_required)
- `l10n_es_tbai_refund_reason` Selection “Invoice Refund Reason Code (TicketBai)”
- `l10n_es_tbai_reversed_ids` Many2many → `account.move` “Refunded Vendor Bills”

Public methods: `button_draft`, `l10n_es_tbai_cancel`, `l10n_es_tbai_resend_bill`, `l10n_es_tbai_send_bill`

## `account.move.line` (extends)


## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`, `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`

## `certificate.certificate` (extends)

- `scope` Selection

## `ir.attachment` (extends)


## `l10n_es_edi_tbai.document` (defines)

TicketBAI Document

- `name` Char (required, readonly)
- `date` Date (required, readonly)
- `xml_attachment_id` Many2one → `ir.attachment` “XML Attachment” (readonly)
- `company_id` Many2one → `res.company` (required)
- `state` Selection “status” (readonly)
- `chain_index` Integer (readonly)
- `response_message` Text (readonly)
- `is_cancel` Boolean (readonly)

Extension points: `_check_can_post`, `_get_crc8`, `_get_header_values`, `_get_importe_desglose_es_partner`, `_get_importe_desglose_foreign_partner`, `_get_recipient_values`, `_get_refunded_values`, `_get_regime_code_value`, `_get_sale_values`, `_get_sender_values`, `_get_tbai_id`, `_get_tbai_qr`, `_get_tbai_seq_from_name`, `_get_tbai_sequence_and_number`, `_get_tbai_sequence_and_number_purchase`, `_get_tbai_signature_and_date`, `_get_values_from_xml`, `_get_xml`, `_post_to_agency`, `_post_to_web_service`, `_prepare_post_params_ar_gi`, `_prepare_post_params_bi`

## `res.company` (extends)

- `l10n_es_tbai_certificate_id` Many2one → `certificate.certificate` “Certificate (TicketBAI)” (store, compute=_compute_l10n_es_tbai_certificate)
- `l10n_es_tbai_certificate_ids` One2many → `certificate.certificate`
- `l10n_es_tbai_tax_agency` Selection “Tax Agency for TBAI”
- `l10n_es_tbai_license_html` Html “TicketBAI license” (compute=_compute_l10n_es_tbai_license_html)
- `l10n_es_tbai_chain_sequence_id` Many2one → `ir.sequence` “TicketBai account.move chain sequence” (readonly)
- `l10n_es_tbai_test_env` Boolean “TBAI Test Mode”
- `l10n_es_tbai_is_enabled` Boolean (compute=_compute_l10n_es_tbai_is_enabled)

Extension points: `_get_l10n_es_tbai_last_chained_document`, `_get_l10n_es_tbai_license_dict`, `_get_l10n_es_tbai_next_chain_index`

## `res.config.settings` (extends)

- `l10n_es_tbai_certificate_ids` One2many (related=company_id.l10n_es_tbai_certificate_ids)
- `l10n_es_tbai_tax_agency` Selection (related=company_id.l10n_es_tbai_tax_agency)
- `l10n_es_tbai_test_env` Boolean (related=company_id.l10n_es_tbai_test_env)

## `account.move.reversal` (extends)

- `l10n_es_tbai_is_required` Boolean “Is TicketBai required for this reversal” (readonly, compute=_compute_l10n_es_tbai_is_required)
- `l10n_es_tbai_refund_reason` Selection “Invoice Refund Reason Code (TicketBai)”

Extension points: `_prepare_default_reversal`
