# l10n_es_edi_facturae — Spain - Facturae EDI

Depends on: l10n_es.

## `account.chart.template` (extends)


Extension points: `_get_es_facturae_account_tax`

## `account.move` (extends)

- `l10n_es_edi_facturae_xml_id` Many2one → `ir.attachment` “Facturae Attachment”
- `l10n_es_edi_facturae_xml_file` Binary “Facturae File”
- `l10n_es_edi_facturae_reason_code` Selection “Spanish Facturae EDI Reason Code”

Extension points: `_get_edi_decoder`

## `account.tax` (extends)

- `l10n_es_edi_facturae_tax_type` Selection “Spanish Facturae EDI Tax Type”

## `l10n_es_edi_facturae.certificate` (defines)

Facturae Digital Certificate

- `content` Binary “PFX Certificate” (required)
- `password` Char
- `serial_number` Char (readonly, index)
- `date_start` Datetime (readonly)
- `date_end` Datetime (readonly)
- `company_id` Many2one → `res.company` (required, readonly)

Public methods: `create`

## `res.company` (extends)

- `l10n_es_edi_facturae_residence_type` Char “Facturae EDI Residency Type Code” (related=partner_id.l10n_es_edi_facturae_residence_type)
- `l10n_es_edi_facturae_certificate_id` One2many → `l10n_es_edi_facturae.certificate` “Facturae EDI signing certificate”

## `res.partner` (extends)

- `l10n_es_edi_facturae_residence_type` Char “Facturae EDI Residency Type Code” (readonly, compute=_compute_l10n_es_edi_facturae_residence_type)

## `uom.uom` (extends)

- `l10n_es_edi_facturae_uom_code` Selection “Spanish EDI Units” (required)

## `account.move.reversal` (extends)

- `l10n_es_edi_facturae_reason_code` Selection “Spanish Facturae EDI Reason Code”

Public methods: `reverse_moves`

Extension points: `_get_ref_string`

## `account.move.send` (extends)

- `l10n_es_edi_facturae_enable_xml` Boolean (compute=_compute_l10n_es_edi_facturae_enable_xml)
- `l10n_es_edi_facturae_checkbox_xml` Boolean “Generate Facturae edi file” (company_dependent)

Extension points: `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`, `_get_wizard_vals_restrict_to`, `_get_wizard_values`
