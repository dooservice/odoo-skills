# l10n_es_edi_tbai — Spain - TicketBAI

Depends on: l10n_es_edi_sii.

## `account.edi.document` (extends)


Extension points: `_prepare_jobs`

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_l10n_es_tbai_invoice_xml`, `_get_move_applicability`

## `account.move` (extends)

- `l10n_es_tbai_chain_index` Integer “TicketBAI chain index” (readonly)
- `l10n_es_tbai_post_xml` Binary “Submission XML” (readonly)
- `l10n_es_tbai_cancel_xml` Binary “Cancellation XML” (readonly)
- `l10n_es_tbai_is_required` Boolean “TicketBAI required” (compute=_compute_l10n_es_tbai_is_required)
- `l10n_es_tbai_refund_reason` Selection “Invoice Refund Reason Code (TicketBai)”

Public methods: `button_draft`

Extension points: `_get_l10n_es_tbai_id`, `_get_l10n_es_tbai_qr`, `_get_l10n_es_tbai_sequence_and_number`, `_get_l10n_es_tbai_signature_and_date`, `_get_l10n_es_tbai_submitted_xml`, `_get_l10n_es_tbai_values_from_xml`, `_get_vendor_bill_tax_values`

## `ir.attachment` (extends)


Public methods: `action_download_xsd_files`

## `l10n_es_edi.certificate` (extends)


Extension points: `_get_key_pair`

## `res.company` (extends)

- `l10n_es_tbai_tax_agency` Selection “Tax Agency for TBAI”
- `l10n_es_tbai_license_html` Html “TicketBAI license” (compute=_compute_l10n_es_tbai_license_html)
- `l10n_es_tbai_chain_sequence_id` Many2one → `ir.sequence` “TicketBai account.move chain sequence” (readonly)

Extension points: `_get_l10n_es_tbai_last_posted_invoice`, `_get_l10n_es_tbai_license_dict`, `_get_l10n_es_tbai_next_chain_index`

## `res.config.settings` (extends)

- `l10n_es_tbai_tax_agency` Selection (related=company_id.l10n_es_tbai_tax_agency)

## `account.move.reversal` (extends)

- `l10n_es_tbai_is_required` Boolean “Is TicketBai required for this reversal” (readonly, compute=_compute_l10n_es_tbai_is_required)
- `l10n_es_tbai_refund_reason` Selection “Invoice Refund Reason Code (TicketBai)”

Extension points: `_prepare_default_reversal`

## `account.resequence.wizard` (extends)
