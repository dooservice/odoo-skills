# l10n_sa_edi — Saudi Arabia - E-invoicing

Depends on: account_edi, account_edi_ubl_cii, l10n_sa, base_vat, certificate.

## `account.chart.template` (extends)


Extension points: `_get_sa_edi_account_tax`

## `account.edi.document` (extends)


Extension points: `_prepare_jobs`

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_move_applicability`, `_prepare_invoice_report`

## `account.edi.xml.ubl_21.zatca` (defines)

UBL 2.1 (ZATCA)

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_address_node`, `_get_document_allowance_charge_node`, `_get_partner_party_identification_number`, `_get_party_node`, `_get_prepayment_line_node`, `_get_prepayment_line_tax_total_node`, `_get_tax_category_code`, `_get_tax_exemption_reason`

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

- `l10n_sa_uuid` Char “Document UUID (SA)”
- `l10n_sa_invoice_signature` Char “Unsigned XML Signature”
- `l10n_sa_chain_index` Integer “ZATCA chain index” (readonly)
- `l10n_sa_edi_chain_head_id` Many2one → `account.move` “ZATCA chain stopping move” (readonly)

Public methods: `action_show_chain_head`, `button_draft`

Extension points: `_get_invoice_report_filename`, `_get_l10n_sa_totals`, `_get_report_base_filename`, `_prepare_tax_lines_for_taxes_computation`

## `account.move.line` (extends)


## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`

## `account.tax` (extends)

- `l10n_sa_is_retention` Boolean “Is Retention”
- `l10n_sa_exemption_reason_code` Selection “Exemption Reason Code”

Public methods: `onchange_amount`

## `certificate.certificate` (extends)


## `ir.attachment` (extends)


Extension points: `_get_posted_pdf_moves_to_check`

## `res.company` (extends)

- `l10n_sa_private_key_id` Many2one → `certificate.key` “ZATCA Private key”
- `l10n_sa_api_mode` Selection (required)
- `l10n_sa_edi_building_number` Char (compute=_compute_address)
- `l10n_sa_edi_plot_identification` Char (compute=_compute_address)
- `l10n_sa_edi_additional_identification_scheme` Selection (related=partner_id.l10n_sa_edi_additional_identification_scheme)
- `l10n_sa_edi_additional_identification_number` Char (related=partner_id.l10n_sa_edi_additional_identification_number)
- `l10n_sa_edi_is_production` Boolean “Is Production”

Public methods: `write`

Extension points: `_get_company_address_field_names`

## `res.config.settings` (extends)

- `l10n_sa_api_mode` Selection (related=company_id.l10n_sa_api_mode)

## `res.partner` (extends)

- `l10n_sa_edi_building_number` Char “Building Number”
- `l10n_sa_edi_plot_identification` Char “Plot Identification”
- `l10n_sa_edi_additional_identification_scheme` Selection “Identification Scheme”
- `l10n_sa_edi_additional_identification_number` Char “Identification Number (SA)”

Extension points: `_get_frontend_writable_fields`

## `l10n_sa_edi.otp.wizard` (defines)

Request ZATCA OTP

- `l10n_sa_renewal` Boolean “PCSID Renewal”
- `l10n_sa_otp` Char “OTP”
- `journal_id` Many2one → `account.journal` (required)

Public methods: `default_get`, `validate`
