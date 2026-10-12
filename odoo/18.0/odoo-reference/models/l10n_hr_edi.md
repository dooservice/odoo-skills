# l10n_hr_edi — Croatia - e-invoicing

Depends on: l10n_hr, account_edi_ubl_cii, account_peppol.

## `account.chart.template` (extends)


Extension points: `_get_hr_edi_account_tax`

## `account.edi.xml.ubl_hr` (defines)

CIUS HR

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_document_nsmap`, `_get_document_template`, `_get_invoice_node`

## `account.journal` (extends)

- `l10n_hr_business_premises_label` Char “Business premises label” (required)
- `l10n_hr_issuing_device_label` Char “Issuing device label” (required)
- `l10n_hr_business_premises_label_refund` Char “Business premises label (refund approval)” (required)
- `l10n_hr_issuing_device_label_refund` Char “Issuing device label (refund approval)” (required)
- `l10n_hr_mer_connection_state` Selection (related=company_id.l10n_hr_mer_connection_state)
- `l10n_hr_is_mer_journal` Boolean “Journal used for eRacun via MojEracun” (compute=_compute_l10n_hr_is_mer_journal)

Public methods: `l10n_hr_mer_get_message_status`, `l10n_hr_mer_get_new_documents`, `l10n_hr_mer_get_new_documents_all`

## `account.move` (extends)

- `l10n_hr_process_type` Selection “Business Process Type” (store, compute=_compute_l10n_hr_process_type)
- `l10n_hr_customer_defined_process_name` Char “Custom Process Name”
- `l10n_hr_fiscal_user_id` Many2one → `res.partner` “Fiscal User”
- `l10n_hr_operator_name` Char “Operator Label” (related=l10n_hr_fiscal_user_id.name)
- `l10n_hr_operator_oib` Char “Operator OIB” (related=l10n_hr_fiscal_user_id.l10n_hr_personal_oib)
- `l10n_hr_edi_addendum_id` One2many → `l10n_hr_edi.addendum` “HR EDI Addendum”
- `l10n_hr_invoice_sending_time` Datetime (related=l10n_hr_edi_addendum_id.invoice_sending_time)
- `l10n_hr_business_document_status` Selection (related=l10n_hr_edi_addendum_id.business_document_status)
- `l10n_hr_business_status_reason` Char (related=l10n_hr_edi_addendum_id.business_status_reason)
- `l10n_hr_fiscalization_number` Char (related=l10n_hr_edi_addendum_id.fiscalization_number)
- `l10n_hr_fiscalization_status` Selection (related=l10n_hr_edi_addendum_id.fiscalization_status)
- `l10n_hr_fiscalization_error` Char (related=l10n_hr_edi_addendum_id.fiscalization_error)
- `l10n_hr_fiscalization_request` Char (related=l10n_hr_edi_addendum_id.fiscalization_request)
- `l10n_hr_fiscalization_channel_type` Selection (related=l10n_hr_edi_addendum_id.fiscalization_channel_type)
- `l10n_hr_payment_reported_amount` Monetary (related=l10n_hr_edi_addendum_id.payment_reported_amount)
- `l10n_hr_payment_unreported` Boolean (compute=_compute_l10n_hr_payment_unreported)
- `l10n_hr_payment_method_type` Selection (related=l10n_hr_edi_addendum_id.payment_method_type)
- `l10n_hr_mer_document_eid` Char (related=l10n_hr_edi_addendum_id.mer_document_eid)
- `l10n_hr_mer_document_status` Selection (related=l10n_hr_edi_addendum_id.mer_document_status)

Public methods: `l10n_hr_edi_mer_action_fetch_status`, `l10n_hr_edi_mer_action_reject`, `l10n_hr_edi_mer_action_report_paid`

Extension points: `_check_l10n_hr_process_type`, `_get_invoice_reference_odoo_invoice`, `_get_l10n_hr_fiscal_user_id_domain`, `_get_l10n_hr_fiscalization_number`, `_get_ubl_cii_builder_from_xml_tree`

## `account.move.line` (extends)

- `l10n_hr_kpd_category_id` Many2one → `l10n_hr.kpd.category` “KPD category” (store, compute=_compute_l10n_hr_product_id_kpd)

## `account.move.send` (extends)


Extension points: `_check_move_constrains`, `_get_default_invoice_edi_format`

## `account.tax` (extends)

- `l10n_hr_tax_category_id` Many2one → `l10n.hr.tax.category` “Croatian Tax Expence Category”

## `l10n.hr.tax.category` (defines)

Croatian tax expence categories

- `name` Char “Name/Mark” (required)
- `code_untdid` Char “UNTDID code”
- `code_hr` Char “HR tax category code”
- `code_tax_scheme` Char “UNTDID tax scheme code”
- `category_name` Char “Categody code name”
- `description` Char “Description”

## `l10n_hr_edi.addendum` (defines)

EDI and fiscalization information for Croatian electronic invoicing

- `move_id` Many2one → `account.move` (required, index)
- `invoice_sending_time` Datetime “Time of invoicing”
- `business_document_status` Selection “Business document status”
- `business_status_reason` Char “Document rejection reason”
- `fiscalization_number` Char “Invoice fiscalization number”
- `fiscalization_status` Selection “Fiscalization status”
- `fiscalization_error` Char “Error reported for fiscalization”
- `fiscalization_request` Char “Fiscalization request ID”
- `fiscalization_channel_type` Selection “Delivery channel type”
- `currency_id` Many2one (related=move_id.currency_id)
- `payment_reported_amount` Monetary “Payment amount already reported to Tax Authority”
- `payment_method_type` Selection “Payment Method Type”
- `mer_document_eid` Char “MojEracun document ElectronicId”
- `mer_document_status` Selection “MojEracun document status”
- `mer_signed_xml_archived` Boolean “Signed XML archived”

## `product.template` (extends)

- `l10n_hr_kpd_category_id` Many2one → `l10n_hr.kpd.category` “KPD category”

## `l10n_hr.kpd.category` (defines)

Croatian KPD Category

- `name` Char “Code” (required)
- `sector` Char “Industry”
- `description` Char “Description”

## `res.company` (extends)

- `l10n_hr_mer_username` Char “MojEracun username”
- `l10n_hr_mer_password` Char “MojEracun password”
- `l10n_hr_mer_company_ident` Char “MojEracun CompanyId”
- `l10n_hr_mer_software_ident` Char “MojEracun SoftwareId”
- `l10n_hr_mer_connection_state` Selection “MojEracun connection status” (required, store, compute=_compute_l10n_hr_mojeracun_state)
- `l10n_hr_mer_connection_mode` Selection “MojEracun Operating mode”
- `l10n_hr_mer_purchase_journal_id` Many2one → `account.journal` “eracun Purchase Journal” (store, compute=_compute_l10n_hr_mer_purchase_journal_id)

Extension points: `_check_l10n_hr_mer_purchase_journal_id`

## `res.config.settings` (extends)

- `l10n_hr_mer_connection_state` Selection (related=company_id.l10n_hr_mer_connection_state)
- `l10n_hr_mer_connection_mode` Selection (related=company_id.l10n_hr_mer_connection_mode)
- `l10n_hr_mer_username` Char (related=company_id.l10n_hr_mer_username)
- `l10n_hr_mer_password` Char (related=company_id.l10n_hr_mer_password)
- `l10n_hr_mer_company_ident` Char (related=company_id.l10n_hr_mer_company_ident)
- `l10n_hr_mer_company_bu` Char (related=company_id.partner_id.l10n_hr_business_unit_code)
- `l10n_hr_mer_software_ident` Char (related=company_id.l10n_hr_mer_software_ident)
- `l10n_hr_mer_purchase_journal_id` Many2one (related=company_id.l10n_hr_mer_purchase_journal_id)

Public methods: `button_l10n_hr_activate_mojeracun`, `button_l10n_hr_deactivate_mojeracun`

## `res.partner` (extends)

- `invoice_sending_method` Selection
- `invoice_edi_format` Selection
- `l10n_hr_personal_oib` Char “Personal OIB”
- `l10n_hr_business_unit_code` Char “Business Unit Code”

Extension points: `_check_mojeracun_send_ubl_hr`, `_get_edi_builder`, `_get_suggested_invoice_edi_format`, `_get_ubl_cii_formats_info`

## `sequence.mixin` (extends)


Extension points: `_get_sequence_format_param`

## `l10n_hr_edi.mojeracun_reject_wizard` (defines)

MojEracun Reject Invoice Wizard

- `move_id` Many2one → `account.move` (required)
- `rejection_type` Selection “Rejection reason type” (required)
- `rejection_description` Char “Rejection reason description” (required)

Public methods: `button_reject_invoice`, `default_get`
