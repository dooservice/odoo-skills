# l10n_es_edi_facturae — Spain - Facturae EDI

Depends on: certificate, l10n_es.

## `account.chart.template` (extends)


Extension points: `_get_es_facturae_account_tax_es_common`

## `account.move` (extends)

- `l10n_es_edi_facturae_xml_id` Many2one → `ir.attachment` “Facturae Attachment”
- `l10n_es_edi_facturae_xml_file` Binary “Facturae File”
- `l10n_es_edi_facturae_reason_code` Selection “Spanish Facturae EDI Reason Code” (store, compute=_compute_l10n_es_edi_facturae_reason_code)
- `l10n_es_invoicing_period_start_date` Date “Invoice Period Start Date”
- `l10n_es_invoicing_period_end_date` Date “Invoice Period End Date”
- `l10n_es_payment_means` Selection “Payment Means” (store, compute=_compute_l10n_es_payment_means)
- `l10n_es_original_invoice_credited` Char “Original Invoice Credited” (store)

Public methods: `action_invoice_download_facturae`, `get_extra_print_items`

Extension points: `_get_edi_decoder`, `_get_fields_to_detach`, `_get_import_file_type`, `_get_invoice_legal_documents`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_default_extra_edis`, `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`

## `account.tax` (extends)

- `l10n_es_edi_facturae_tax_type` Selection “Spanish Facturae EDI Tax Type”

## `certificate.certificate` (extends)

- `scope` Selection

## `res.company` (extends)

- `l10n_es_edi_facturae_residence_type` Char “Facturae EDI Residency Type Code” (related=partner_id.l10n_es_edi_facturae_residence_type)
- `l10n_es_edi_facturae_certificate_ids` One2many → `certificate.certificate` “Facturae EDI signing certificate”

## `l10n_es_edi_facturae.ac_role_type` (defines)

Administrative Center Role Type

- `code` Char (required)
- `name` Char (required)

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `type` Selection
- `l10n_es_edi_facturae_ac_center_code` Char “Code”
- `l10n_es_edi_facturae_ac_role_type_ids` Many2many → `l10n_es_edi_facturae.ac_role_type` “Roles”
- `l10n_es_edi_facturae_ac_physical_gln` Char “Physical GLN”
- `l10n_es_edi_facturae_ac_logical_operational_point` Char “Logical Operational Point”
- `l10n_es_edi_facturae_residence_type` Char “Facturae EDI Residency Type Code” (readonly, compute=_compute_l10n_es_edi_facturae_residence_type)

## `uom.uom` (extends)

- `l10n_es_edi_facturae_uom_code` Selection “Spanish EDI Units” (required)

## `account.move.reversal` (extends)

- `l10n_es_edi_facturae_reason_code` Selection “Spanish Facturae EDI Reason Code”

Public methods: `reverse_moves`

Extension points: `_prepare_default_reversal`

## `account.move.send.wizard` (extends)


Public methods: `action_send_and_print`
