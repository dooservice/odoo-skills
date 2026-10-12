# l10n_sa_edi — Saudi Arabia - E-invoicing

Depends on: account_edi, account_edi_ubl_cii, account_debit_note, l10n_sa, base_vat, certificate.

## `account.chart.template` (extends)


Extension points: `_get_sa_edi_account_tax`

## `account.edi.document` (extends)


Extension points: `_prepare_jobs`

## `account.edi.format` (extends)


Extension points: `_check_move_configuration`, `_get_move_applicability`, `_prepare_invoice_report`

## `account.edi.xml.ubl_21.zatca` (defines)

UBL 2.1 (ZATCA)

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_delivery_vals_list`, `_get_document_allowance_charge_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_payment_terms_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_tax_category_list`, `_get_tax_unece_codes`

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
- `l10n_sa_serial_number` Char “Serial Number”
- `l10n_sa_latest_submission_hash` Char “Latest Submission Hash”

## `account.move` (extends)

- `l10n_sa_uuid` Char “Document UUID (SA)”
- `l10n_sa_invoice_signature` Char “Unsigned XML Signature”
- `l10n_sa_chain_index` Integer “ZATCA chain index” (readonly)

Public methods: `button_draft`

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
- `l10n_sa_additional_identification_scheme` Selection (related=partner_id.l10n_sa_additional_identification_scheme)
- `l10n_sa_additional_identification_number` Char (related=partner_id.l10n_sa_additional_identification_number)

Public methods: `write`

Extension points: `_get_company_address_field_names`

## `res.config.settings` (extends)

- `l10n_sa_api_mode` Selection (related=company_id.l10n_sa_api_mode)

## `res.partner` (extends)

- `l10n_sa_edi_building_number` Char “Building Number”
- `l10n_sa_edi_plot_identification` Char “Plot Identification”
- `l10n_sa_additional_identification_scheme` Selection “Identification Scheme”
- `l10n_sa_additional_identification_number` Char “Identification Number (SA)”

## `account.debit.note` (extends)


Public methods: `create_debit`

## `account.move.reversal` (extends)


Public methods: `reverse_moves`

## `l10n_sa_edi.otp.wizard` (defines)

Request ZATCA OTP

- `l10n_sa_renewal` Boolean “PCSID Renewal”
- `l10n_sa_otp` Char “OTP”
- `journal_id` Many2one → `account.journal` (required)

Public methods: `default_get`, `validate`
