# l10n_sa_edi — Saudi Arabia - E-invoicing

Depends on: account_edi_ubl_cii, l10n_sa, certificate.

## `account.chart.template` (extends)


## `account.chart.template` (extends)


Extension points: `_get_sa_edi_account_tax`

## `account.edi.xml.ubl_21.zatca` (defines)

UBL 2.1 (ZATCA)

Inherits: `zatca.ubl.mixin`, `account.edi.xml.ubl_21`


Extension points: `_get_prepayment_line_node`, `_get_prepayment_line_tax_total_node`

## `account.journal` (extends)

- `l10n_sa_csr` Binary
- `l10n_sa_csr_errors` Html “Onboarding Errors”
- `l10n_sa_compliance_csid_json` Char “CCSID JSON”
- `l10n_sa_production_csid_certificate_id` Many2one → `certificate.certificate` “PCSID Certificate”
- `l10n_sa_production_csid_json` Char “PCSID JSON”
- `l10n_sa_production_csid_validity` Datetime (related=l10n_sa_production_csid_certificate_id.date_end)
- `l10n_sa_compliance_csid_certificate_id` Many2one → `certificate.certificate` “CCSID certificate”
- `l10n_sa_compliance_checks_passed` Boolean “Compliance Checks Done”
- `l10n_sa_chain_sequence_id` Many2one → `ir.sequence` “ZATCA account.move chain sequence” (readonly)
- `l10n_sa_latest_submission_hash` Char “Latest Submission Hash”

## `account.move` (extends)

- `l10n_sa_edi_transaction_type_ids` Many2many → `l10n_sa_edi.transaction.type` “Transaction type” (store, compute=_compute_l10n_sa_edi_transaction_type_ids)
- `l10n_sa_is_csid_ready` Boolean (compute=_compute_l10n_sa_is_csid_ready)
- `l10n_sa_compliance_checks_passed` Boolean (related=journal_id.l10n_sa_compliance_checks_passed)

Public methods: `button_draft`

Extension points: `_get_invoice_report_filename`, `_get_l10n_sa_edi_invoice_type_code`, `_get_l10n_sa_journal`, `_get_l10n_sa_totals`, `_get_report_base_filename`, `_prepare_tax_lines_for_taxes_computation`

## `account.move.line` (extends)


## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `account.tax` (extends)

- `ubl_cii_tax_exemption_reason_code` Selection
- `l10n_sa_show_exemption_reason` Boolean (compute=_compute_l10n_sa_show_exemption_reason)

## `certificate.certificate` (extends)


## `ir.attachment` (extends)


Extension points: `_get_posted_pdf_moves_to_check`

## `l10n_sa_edi.document` (defines)

ZATCA Document

- `name` Char (related=attachment_id.name)
- `res_model` Selection “Invoice Type” (required, readonly)
- `res_id` Many2oneReference (required, readonly)
- `attachment_id` Many2one → `ir.attachment` (readonly)
- `state` Selection “ZATCA State” (readonly)
- `message` Html “ZATCA Errors/Warnings”
- `content` Binary (compute=_compute_content)
- `l10n_sa_chain_index` Integer “ZATCA chain index” (readonly)
- `l10n_sa_edi_log_ids` One2many → `l10n_sa_edi.log`
- `company_id` Many2one → `res.company` (required)
- `journal_id` Many2one → `account.journal` (required)
- `account_move_id` Many2one → `account.move` (compute=_compute_resource)

Public methods: `resource`

## `l10n_sa_edi.log` (defines)

ZATCA Log

- `l10n_sa_edi_document_id` Many2one → `l10n_sa_edi.document`
- `document_state` Selection (related=l10n_sa_edi_document_id.state)
- `state` Selection
- `attachment_name` Char
- `is_test` Boolean
- `message` Html
- `is_latest_log` Boolean (compute=_compute_is_latest_log)

Public methods: `action_retry`

## `l10n_sa_edi.transaction.type` (defines)

ZATCA Transaction Type

- `name` Char “Name” (required)
- `code` Selection “Code” (required)

## `res.company` (extends)

- `l10n_sa_private_key_id` Many2one → `certificate.key` “ZATCA Private key”
- `l10n_sa_api_mode` Selection (required)
- `l10n_sa_edi_building_number` Char (compute=_compute_address)
- `l10n_sa_edi_plot_identification` Char (compute=_compute_address)
- `l10n_sa_edi_additional_identification_scheme` Char (related=partner_id.l10n_sa_edi_additional_identification_scheme)
- `l10n_sa_edi_additional_identification_number` Char (related=partner_id.l10n_sa_edi_additional_identification_number)
- `l10n_sa_edi_is_production` Boolean “Is Production”

Public methods: `write`

Extension points: `_get_company_address_field_names`

## `res.config.settings` (extends)

- `l10n_sa_api_mode` Selection (related=company_id.l10n_sa_api_mode)

## `res.partner` (extends)

- `l10n_sa_edi_building_number` Char “Building Number”
- `l10n_sa_edi_plot_identification` Char “Secondary Number”
- `l10n_sa_edi_additional_identification_scheme` Char “Identification Scheme” (compute=_compute_l10n_sa_edi_additional_identification_fields)
- `l10n_sa_edi_additional_identification_number` Char “Identification Number (SA)” (compute=_compute_l10n_sa_edi_additional_identification_fields)

Extension points: `_get_frontend_writable_fields`

## `zatca.mixin` (extends)

- `l10n_sa_edi_supply_end_date` Date “Supply End Date”
- `l10n_sa_uuid` Char “Document UUID (SA)”
- `l10n_sa_invoice_signature` Char “Unsigned XML Signature”
- `l10n_sa_edi_document_id` Many2one → `l10n_sa_edi.document`
- `l10n_sa_edi_state` Selection (related=l10n_sa_edi_document_id.state)
- `l10n_sa_edi_log_ids` One2many (related=l10n_sa_edi_document_id.l10n_sa_edi_log_ids)
- `l10n_sa_chain_index` Integer (related=l10n_sa_edi_document_id.l10n_sa_chain_index)
- `l10n_sa_is_test` Boolean (store, compute=_compute_l10n_sa_is_test)

Extension points: `_get_l10n_sa_journal`

## `zatca.ubl.mixin` (defines)

ZATCA UBL Mixin


Extension points: `_get_address_node`, `_get_document_allowance_charge_node`, `_get_partner_party_identification_number`, `_get_party_node`, `_get_tax_category_code`, `_get_tax_exemption_reason`

## `l10n_sa_edi.otp.wizard` (defines)

Request ZATCA OTP

- `l10n_sa_renewal` Boolean “PCSID Renewal”
- `l10n_sa_otp` Char “OTP”
- `journal_id` Many2one → `account.journal` (required)

Public methods: `default_get`, `validate`
