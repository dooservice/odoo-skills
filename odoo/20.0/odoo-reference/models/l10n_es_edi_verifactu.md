# l10n_es_edi_verifactu — Spain - Veri*Factu

Depends on: l10n_es, certificate.

## `account.journal` (extends)


## `account.move` (extends)

- `l10n_es_edi_verifactu_required` Boolean “Veri*Factu Required” (related=company_id.l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_document_ids` One2many → `l10n_es_edi_verifactu.document` “Veri*Factu Documents”
- `l10n_es_edi_verifactu_state` Selection “Veri*Factu Status” (store, compute=_compute_l10n_es_edi_verifactu_state)
- `l10n_es_edi_verifactu_warning_level` Char “Veri*Factu Warning Level” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_warning` Html “Veri*Factu Warning” (compute=_compute_l10n_es_edi_verifactu_warning)
- `l10n_es_edi_verifactu_qr_code` Char “Veri*Factu QR Code” (compute=_compute_l10n_es_edi_verifactu_qr_code)
- `l10n_es_edi_verifactu_substituted_entry_id` Many2one → `account.move` “Substitution of” (readonly)
- `l10n_es_edi_verifactu_substitution_move_ids` One2many → `account.move` “Substituted by”

Public methods: `l10n_es_edi_verifactu_button_cancel`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_move_constraints`

## `account.tax` (extends)


## `certificate.certificate` (extends)

- `scope` Selection

## `res.company` (extends)

- `l10n_es_edi_verifactu_certificate_ids` One2many → `certificate.certificate` “Veri*Factu Certificates”
- `l10n_es_edi_verifactu_required` Boolean “Enable Veri*Factu”
- `l10n_es_edi_verifactu_test_environment` Boolean “Veri*Factu Test Environment”

## `res.config.settings` (extends)

- `l10n_es_edi_verifactu_required` Boolean (related=company_id.l10n_es_edi_verifactu_required)
- `l10n_es_edi_verifactu_certificate_ids` One2many (related=company_id.l10n_es_edi_verifactu_certificate_ids)
- `l10n_es_edi_verifactu_test_environment` Boolean (related=company_id.l10n_es_edi_verifactu_test_environment)

## `res.partner` (extends)


## `l10n_es_edi_verifactu.document` (defines)

Veri*Factu Document

- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `move_id` Many2one → `account.move` “Journal Entry” (readonly)
- `chain_index` Integer “Chain Index” (readonly)
- `document_type` Selection “Document Type” (required, readonly)
- `json_attachment_id` Many2one → `ir.attachment` “JSON Attachment” (readonly)
- `json_attachment_raw` Binary “JSON” (related=json_attachment_id.raw)
- `json_attachment_filename` Char “JSON Filename” (compute=_compute_json_attachment_filename)
- `xml_attachment_raw` Binary “XML” (compute=_compute_xml_attachment)
- `xml_attachment_filename` Char “XML Filename” (compute=_compute_xml_attachment)
- `errors` Html “Errors” (readonly)
- `response_csv` Char “Response CSV” (readonly)
- `state` Selection “Status” (readonly)
- `obligado_partner_id` Many2one → `res.partner` “Required to issue” (required, readonly)

Public methods: `action_download_xml`, `trigger_next_batch`

Extension points: `_check_record_values`, `_create_for_record`, `_get_batch_dict`, `_get_db_identifier`, `_get_document_dict`, `_get_last`, `_get_qr_code_img_url`, `_get_record_identifier`, `_get_state`, `_get_tax_details`

## `l10n_es_edi_verifactu.issuer` (defines)

Veri*Factu Issuer

- `company_id` Many2one → `res.company` (required)
- `obligado_partner_id` Many2one → `res.partner` (required)
- `next_batch_time` Datetime
- `chain_sequence_id` Many2one → `ir.sequence`

Extension points: `_get_chain_sequence`, `_get_last_document`, `_get_or_create`

## `account.move.reversal` (extends)


## `account.resequence.wizard` (extends)

- `l10n_es_edi_verifactu_required_in_prod` Boolean (compute=_compute_l10n_es_edi_verifactu_required_in_prod)
