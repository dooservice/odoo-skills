# l10n_es_edi_verifactu — Spain - Veri*Factu

Depends on: l10n_es, certificate.

## `account.chart.template` (extends)


Extension points: `_get_es_verifactu_account_tax_es_canary_common`, `_get_es_verifactu_account_tax_es_common_mainland`

## `account.move` (extends)

- `l10n_es_edi_verifactu_required` Boolean “Veri*Factu Required” (related=company_id.l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_document_ids` One2many → `l10n_es_edi_verifactu.document` “Veri*Factu Documents”
- `l10n_es_edi_verifactu_state` Selection “Veri*Factu Status” (store, compute=_compute_l10n_es_edi_verifactu_state)
- `l10n_es_edi_verifactu_warning_level` Char “Veri*Factu Warning Level” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_warning` Html “Veri*Factu Warning” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_qr_code` Char “Veri*Factu QR Code” (compute=_compute_l10n_es_edi_verifactu_qr_code)
- `l10n_es_edi_verifactu_show_cancel_button` Boolean “Show Veri*Factu Cancel Button” (compute=_compute_l10n_es_edi_verifactu_show_cancel_button)
- `l10n_es_edi_verifactu_available_clave_regimens` Char “Available Veri*Factu Regime Key” (compute=_compute_l10n_es_edi_verifactu_available_clave_regimens)
- `l10n_es_edi_verifactu_clave_regimen` Selection “Veri*Factu Regime Key” (store, compute=_compute_l10n_es_edi_verifactu_clave_regimen)
- `l10n_es_edi_verifactu_substituted_entry_id` Many2one → `account.move` “Substitution of” (readonly)
- `l10n_es_edi_verifactu_substitution_move_ids` One2many → `account.move` “Substituted by”
- `l10n_es_edi_verifactu_refund_reason` Selection “Veri*Factu Refund Reason”

Public methods: `l10n_es_edi_verifactu_button_cancel`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `account.tax` (extends)

- `l10n_es_applicability` Selection “Applicability (Spain)”

## `certificate.certificate` (extends)

- `scope` Selection

## `res.company` (extends)

- `l10n_es_edi_verifactu_certificate_ids` One2many → `certificate.certificate` “Veri*Factu Certificates”
- `l10n_es_edi_verifactu_required` Boolean “Enable Veri*Factu”
- `l10n_es_edi_verifactu_test_environment` Boolean “Veri*Factu Test Environment”
- `l10n_es_edi_verifactu_chain_sequence_id` Many2one → `ir.sequence` “Veri*Factu Document Chain Sequence” (readonly)
- `l10n_es_edi_verifactu_next_batch_time` Datetime “Veri*Factu Next Batch Time” (readonly)
- `l10n_es_edi_verifactu_special_vat_regime` Selection “Veri*Factu VAT Regime”

## `res.config.settings` (extends)

- `l10n_es_edi_verifactu_required` Boolean (related=company_id.l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_certificate_ids` One2many (related=company_id.l10n_es_edi_verifactu_certificate_ids)
- `l10n_es_edi_verifactu_test_environment` Boolean (related=company_id.l10n_es_edi_verifactu_test_environment)
- `l10n_es_edi_verifactu_special_vat_regime` Selection (related=company_id.l10n_es_edi_verifactu_special_vat_regime)

## `res.partner` (extends)


## `l10n_es_edi_verifactu.document` (defines)

Veri*Factu Document

- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `move_id` Many2one → `account.move` “Journal Entry” (readonly)
- `chain_index` Integer “Chain Index” (readonly)
- `document_type` Selection “Document Type” (required, readonly)
- `json_attachment_id` Many2one → `ir.attachment` “JSON Attachment” (readonly)
- `json_attachment_base64` Binary “JSON” (related=json_attachment_id.datas)
- `json_attachment_filename` Char “JSON Filename” (compute=_compute_json_attachment_filename)
- `errors` Html “Errors” (readonly)
- `response_csv` Char “Response CSV” (readonly)
- `state` Selection “Status” (readonly)

Public methods: `trigger_next_batch`

Extension points: `_check_record_values`, `_create_for_record`, `_get_batch_dict`, `_get_db_identifier`, `_get_document_dict`, `_get_last`, `_get_qr_code_img_url`, `_get_record_identifier`, `_get_state`, `_get_tax_details`

## `account.move.reversal` (extends)

- `l10n_es_edi_verifactu_required` Boolean “Veri*Factu Required” (store, compute=_compute_l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_refund_reason` Selection “Veri*Factu Refund Reason” (store, compute=_compute_l10n_es_edi_verifactu_refund_reason)

Extension points: `_prepare_default_reversal`
