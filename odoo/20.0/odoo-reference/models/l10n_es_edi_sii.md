# l10n_es_edi_sii — Spain - SII EDI Suministro de Libros

Depends on: certificate, l10n_es.

## `account.move` (extends)

- `l10n_es_registration_date` Date “Registration Date”
- `l10n_es_edi_sii_document_ids` One2many → `l10n_es_edi_sii.document` “SII Documents”
- `l10n_es_edi_is_required` Boolean “Is the Spanish EDI needed” (compute=_compute_l10n_es_edi_is_required)
- `l10n_es_edi_sii_state` Selection “Spain SII Status” (compute=_compute_l10n_es_edi_sii_data)
- `l10n_es_edi_csv` Char “CSV” (compute=_compute_l10n_es_edi_sii_data)
- `l10n_es_edi_sii_error` Html “SII Error” (compute=_compute_l10n_es_edi_sii_data)

Public methods: `action_l10n_es_send_sii`, `action_l10n_es_sii_send_in_batch`, `button_request_cancel`

## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`

## `certificate.certificate` (extends)

- `scope` Selection

## `l10n_es_edi_sii.document` (defines)

SII Document

- `move_id` Many2one → `account.move` (required)
- `company_id` Many2one → `res.company` (related=move_id.company_id)
- `state` Selection “State” (required)
- `csv` Char “CSV”
- `attachment_id` Many2one → `ir.attachment` “SII JSON Payload”
- `response_message` Html “Response”
- `sii_json_file` Binary “Download JSON” (compute=_compute_sii_json_file)
- `sii_json_filename` Char “JSON Filename” (compute=_compute_sii_json_file)
- `xml_attachment_raw` Binary “XML” (compute=_compute_xml_attachment)
- `xml_attachment_filename` Char “XML Filename” (compute=_compute_xml_attachment)

Public methods: `action_download_json`, `action_download_xml`

Extension points: `_get_agency_urls`, `_get_attachment_name`, `_get_web_service_header`, `_post_to_agency`, `_post_to_web_service`

## `res.company` (extends)

- `l10n_es_sii_certificate_id` Many2one → `certificate.certificate` “Certificate (SII)” (store, compute=_compute_l10n_es_sii_certificate)
- `l10n_es_sii_certificate_ids` One2many → `certificate.certificate`
- `l10n_es_sii_tax_agency` Selection “Tax Agency for SII”
- `l10n_es_sii_test_env` Boolean “SII Test Mode”

## `res.config.settings` (extends)

- `l10n_es_sii_certificate_ids` One2many (related=company_id.l10n_es_sii_certificate_ids)
- `l10n_es_sii_tax_agency` Selection (related=company_id.l10n_es_sii_tax_agency)
- `l10n_es_sii_test_env` Boolean (related=company_id.l10n_es_sii_test_env)

## `account.move.send.wizard` (extends)
