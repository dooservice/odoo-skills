# l10n_es_edi_sii — Spain - SII EDI Suministro de Libros

Depends on: l10n_es, account_edi.

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_move_applicability`

## `account.move` (extends)

- `l10n_es_edi_is_required` Boolean “Is the Spanish EDI needed” (compute=_compute_l10n_es_edi_is_required)
- `l10n_es_edi_csv` Char “CSV return code”
- `l10n_es_registration_date` Date “Registration Date”

Extension points: `_check_edi_documents_for_reset_to_draft`

## `account.move.send` (extends)


Extension points: `_get_mail_attachment_from_doc`

## `l10n_es_edi.certificate` (defines)

Personal Digital Certificate

- `content` Binary “File” (required)
- `password` Char
- `date_start` Datetime (readonly)
- `date_end` Datetime (readonly)
- `company_id` Many2one → `res.company` (required)

Public methods: `create`

Extension points: `_get_es_current_datetime`

## `res.company` (extends)

- `l10n_es_edi_certificate_id` Many2one → `l10n_es_edi.certificate` “Certificate (ES)” (store, compute=_compute_l10n_es_edi_certificate)
- `l10n_es_edi_certificate_ids` One2many → `l10n_es_edi.certificate`
- `l10n_es_edi_tax_agency` Selection “Tax Agency for SII”
- `l10n_es_edi_test_env` Boolean “Test Mode”

## `res.config.settings` (extends)

- `l10n_es_edi_certificate_ids` One2many (related=company_id.l10n_es_edi_certificate_ids)
- `l10n_es_edi_tax_agency` Selection (related=company_id.l10n_es_edi_tax_agency)
- `l10n_es_edi_test_env` Boolean (related=company_id.l10n_es_edi_test_env)

## `account.resequence.wizard` (extends)
