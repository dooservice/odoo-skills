# l10n_in — Indian - Accounting

Depends on: account_tax_python, base_vat, account_debit_note, account, iap.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`, `_get_demo_data_attachment`, `_get_demo_data_config_settings`, `_get_demo_data_mail_message`, `_get_demo_data_move`, `_get_demo_data_partner`, `_get_demo_data_res_partner_category`, `_post_load_demo_data`

## `account.account` (extends)

- `l10n_in_tds_tcs_section_id` Many2one → `l10n_in.section.alert` “TCS/TDS Section”
- `l10n_in_tds_feature_enabled` Boolean (store, compute=_compute_tds_tcs_features)
- `l10n_in_tcs_feature_enabled` Boolean (store, compute=_compute_tds_tcs_features)

## `account.move` (extends)

- `l10n_in_gst_treatment` Selection “GST Treatment” (store, compute=_compute_l10n_in_gst_treatment)
- `l10n_in_state_id` Many2one → `res.country.state` “Place of supply” (store, compute=_compute_l10n_in_state_id)
- `l10n_in_gstin` Char “GSTIN”
- `l10n_in_shipping_bill_number` Char “Shipping bill number”
- `l10n_in_shipping_bill_date` Date “Shipping bill date”
- `l10n_in_shipping_port_code_id` Many2one → `l10n_in.port.code`
- `l10n_in_reseller_partner_id` Many2one → `res.partner` “Reseller”
- `l10n_in_journal_type` Selection “Journal Type” (related=journal_id.type)
- `l10n_in_warning` Json (compute=_compute_l10n_in_warning)
- `l10n_in_is_gst_registered_enabled` Boolean (related=company_id.l10n_in_is_gst_registered)
- `l10n_in_tds_deduction` Selection “TDS Deduction” (related=commercial_partner_id.l10n_in_pan_entity_id.tds_deduction)
- `l10n_in_is_withholding` Boolean “Is Indian TDS Entry”
- `l10n_in_withholding_ref_move_id` Many2one → `account.move` “Indian TDS Ref Move” (readonly)
- `l10n_in_withholding_ref_payment_id` Many2one → `account.payment` “Indian TDS Ref Payment” (readonly)
- `l10n_in_withhold_move_ids` One2many → `account.move` “Indian TDS Entries”
- `l10n_in_withholding_line_ids` One2many → `account.move.line` “Indian TDS Lines” (compute=_compute_l10n_in_withholding_line_ids)
- `l10n_in_total_withholding_amount` Monetary “Total Indian TDS Amount” (compute=_compute_l10n_in_total_withholding_amount)
- `l10n_in_display_higher_tcs_button` Boolean “Display higher TCS button” (compute=_compute_l10n_in_display_higher_tcs_button)
- `l10n_in_tds_feature_enabled` Boolean (related=company_id.l10n_in_tds_feature)
- `l10n_in_tcs_feature_enabled` Boolean (related=company_id.l10n_in_tcs_feature)
- `l10n_in_partner_gstin_status` Boolean “GST Status” (compute=_compute_l10n_in_partner_gstin_status_and_date)
- `l10n_in_show_gstin_status` Boolean (compute=_compute_l10n_in_show_gstin_status)
- `l10n_in_gstin_verified_date` Date (compute=_compute_l10n_in_partner_gstin_status_and_date)

Public methods: `action_l10n_in_apply_higher_tax`, `action_l10n_in_withholding_entries`, `l10n_in_verify_partner_gstin_status`

Extension points: `_get_l10n_in_invalid_tax_lines`, `_get_l10n_in_invoice_label`, `_get_l10n_in_seller_buyer_party`, `_get_l10n_in_tax_details_by_line_code`, `_get_l10n_in_tds_tcs_applicable_sections`, `_get_name_invoice_report`, `_get_sections_aggregate_sum_by_pan`, `_get_sync_stack`, `_get_tcs_applicable_lines`

## `account.journal` (extends)


## `account.move.line` (extends)

- `l10n_in_hsn_code` Char “HSN/SAC Code” (store, compute=_compute_l10n_in_hsn_code)
- `l10n_in_gstr_section` Selection “GSTR Section”
- `l10n_in_withhold_tax_amount` Monetary “TDS Tax Amount” (compute=_compute_l10n_in_withhold_tax_amount)
- `l10n_in_tds_tcs_section_id` Many2one (related=account_id.l10n_in_tds_tcs_section_id)

Extension points: `_get_l10n_in_gstr_section`, `_get_l10n_in_tax_tag_ids`

## `account.payment` (extends)

- `l10n_in_withhold_move_ids` One2many → `account.move` “Indian Payment TDS Entries”
- `l10n_in_total_withholding_amount` Monetary (compute=_compute_l10n_in_total_withholding_amount)
- `l10n_in_tds_feature_enabled` Boolean (related=company_id.l10n_in_tds_feature)

Public methods: `action_l10n_in_withholding_entries`

## `account.tax` (extends)

- `l10n_in_reverse_charge` Boolean “Reverse charge”
- `l10n_in_gst_tax_type` Selection (compute=_compute_l10n_in_gst_tax_type)
- `l10n_in_is_lut` Boolean “LUT”
- `l10n_in_tax_type` Selection “Indian Tax Type”
- `l10n_in_section_id` Many2one → `l10n_in.section.alert` “Section”
- `l10n_in_tds_feature_enabled` Boolean (related=company_id.l10n_in_tds_feature)
- `l10n_in_tcs_feature_enabled` Boolean (related=company_id.l10n_in_tcs_feature)

Extension points: `_prepare_base_line_for_taxes_computation`

## `res.company` (extends)

- `l10n_in_upi_id` Char “UPI Id”
- `l10n_in_hsn_code_digit` Selection “HSN Code Digit” (store, compute=_compute_l10n_in_hsn_code_digit)
- `l10n_in_edi_production_env` Boolean “Indian Production Environment”
- `l10n_in_pan_entity_id` Many2one “PAN” (store, related=partner_id.l10n_in_pan_entity_id)
- `l10n_in_pan_type` Selection “PAN Type” (related=l10n_in_pan_entity_id.type)
- `l10n_in_tan` Char “TAN” (related=partner_id.l10n_in_tan)
- `l10n_in_gst_state_warning` Char (related=partner_id.l10n_in_gst_state_warning)
- `l10n_in_tds_feature` Boolean “TDS” (store, compute=_compute_l10n_in_parent_based_features)
- `l10n_in_tcs_feature` Boolean “TCS” (store, compute=_compute_l10n_in_parent_based_features)
- `l10n_in_withholding_account_id` Many2one → `account.account` “TDS Account”
- `l10n_in_withholding_journal_id` Many2one → `account.journal` “TDS Journal”
- `l10n_in_is_gst_registered` Boolean “Registered Under GST” (store, compute=_compute_l10n_in_parent_based_features)
- `l10n_in_gstin_status_feature` Boolean “Check GST Number Status”

Public methods: `action_update_state_as_per_gstin`, `create`, `onchange_vat`, `write`

## `iap.account` (extends)


## `l10n_in.pan.entity` (defines)

Indian PAN Entity

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “PAN” (required)
- `type` Selection (readonly, store, compute=_compute_type)
- `partner_ids` One2many → `res.partner` “Partners”
- `tds_deduction` Selection “TDS Deduction”
- `tds_certificate` Binary “TDS Certificate”
- `tds_certificate_filename` Char “TDS Certificate Filename”
- `msme_type` Selection “MSME/Udyam Registration Type”
- `msme_number` Char “MSME/Udyam Registration Number”

Public methods: `create`, `write`

Extension points: `_check_pan_name`

## `account.report` (extends)


## `l10n_in.section.alert` (defines)

indian section alert

- `name` Char “Section Name”
- `tax_source_type` Selection “Tax Source Type”
- `consider_amount` Selection “Consider” (required)
- `is_per_transaction_limit` Boolean “Per Transaction”
- `per_transaction_limit` Float “Per Transaction limit”
- `is_aggregate_limit` Boolean “Aggregate”
- `aggregate_limit` Float “Aggregate limit”
- `aggregate_period` Selection “Aggregate Period”
- `l10n_in_section_tax_ids` One2many → `account.tax` “Taxes”
- `tax_report_line_id` Many2one → `account.report.line` “Tax Report Line”

Extension points: `_get_warning_message`

## `l10n_in.port.code` (defines)

Indian port code

- `code` Char “Port Code” (required)
- `name` Char “Port” (required)
- `state_id` Many2one → `res.country.state` “State”

## `product.template` (extends)

- `l10n_in_hsn_code` Char “HSN/SAC Code”
- `l10n_in_hsn_warning` Text “HSC/SAC warning” (compute=_compute_l10n_in_hsn_warning)
- `l10n_in_is_gst_registered_enabled` Boolean (compute=_compute_l10n_in_is_gst_registered_enabled)

## `res.config.settings` (extends)

- `group_l10n_in_reseller` Boolean “Manage Reseller(E-Commerce)”
- `l10n_in_edi_production_env` Boolean “Indian Production Environment” (related=company_id.l10n_in_edi_production_env)
- `l10n_in_gsp` Selection “GSP”
- `l10n_in_hsn_code_digit` Selection (related=company_id.l10n_in_hsn_code_digit)
- `l10n_in_tds_feature` Boolean (related=company_id.l10n_in_tds_feature)
- `l10n_in_tcs_feature` Boolean (related=company_id.l10n_in_tcs_feature)
- `l10n_in_withholding_account_id` Many2one (related=company_id.l10n_in_withholding_account_id)
- `l10n_in_withholding_journal_id` Many2one (related=company_id.l10n_in_withholding_journal_id)
- `l10n_in_tan` Char (related=company_id.l10n_in_tan)
- `l10n_in_is_gst_registered` Boolean (related=company_id.l10n_in_is_gst_registered)
- `l10n_in_gstin` Char “GST Number” (related=company_id.vat)
- `l10n_in_gstin_status_feature` Boolean (related=company_id.l10n_in_gstin_status_feature)
- `l10n_in_gst_efiling_feature` Boolean “GST E-Filing & Matching Feature”
- `l10n_in_fetch_vendor_edi_feature` Boolean “Fetch Vendor E-Invoiced Document”
- `l10n_in_enet_vendor_batch_payment_feature` Boolean “ENet Vendor Batch Payment”
- `module_l10n_in_reports` Boolean “GST E-Filing & Matching”
- `module_l10n_in_edi` Boolean “Indian Electronic Invoicing”
- `module_l10n_in_ewaybill` Boolean “Indian Electronic Waybill”

Public methods: `get_values`, `l10n_in_edi_buy_iap`, `reload_template`, `set_values`

## `res.country.state` (extends)

- `l10n_in_tin` Char “TIN Number”

## `res.partner` (extends)

- `l10n_in_gst_treatment` Selection “GST Treatment”
- `l10n_in_pan_entity_id` Many2one → `l10n_in.pan.entity` “PAN”
- `l10n_in_tan` Char “TAN”
- `display_pan_warning` Boolean “Display pan warning” (compute=_compute_display_pan_warning)
- `l10n_in_gst_state_warning` Char (compute=_compute_l10n_in_gst_state_warning)
- `l10n_in_is_gst_registered_enabled` Boolean (compute=_compute_l10n_in_gst_registered_and_status)
- `l10n_in_gstin_verified_status` Boolean “GST Status”
- `l10n_in_gstin_verified_date` Date “GSTIN Verified Date”
- `l10n_in_gstin_status_feature_enabled` Boolean (compute=_compute_l10n_in_gst_registered_and_status)

Public methods: `action_l10n_in_verify_gstin_status`, `action_update_state_as_per_gstin`, `check_vat_in`, `create`, `onchange_vat`, `write`

## `account.chart.template` (extends)


Extension points: `_get_in_account_cash_rounding`, `_get_in_account_fiscal_position`, `_get_in_res_company`, `_get_in_template_data`, `_get_l10n_in_fiscal_tax_vals`, `_post_load_data`

## `uom.uom` (extends)

- `l10n_in_code` Char “Indian GST UQC”

## `l10n_in.withhold.wizard` (defines)

Withhold Wizard

- `reference` Char “Reference”
- `type_name` Char “Type” (compute=_compute_type_name)
- `related_move_id` Many2one → `account.move` “Invoice/Bill” (readonly)
- `related_payment_id` Many2one → `account.payment` “Payment” (readonly)
- `tds_deduction` Selection “TDS Deduction” (compute=_compute_tds_deduction)
- `company_id` Many2one → `res.company` “Company” (compute=_compute_company_id)
- `currency_id` Many2one “Currency” (related=company_id.currency_id)
- `journal_id` Many2one → `account.journal` “Journal” (required, store, compute=_compute_journal)
- `date` Date “Date”
- `l10n_in_tds_tax_type` Char “Indian Tax Type” (compute=_compute_l10n_in_tds_tax_type)
- `l10n_in_withholding_warning` Json “Withholding warning” (compute=_compute_l10n_in_withholding_warning)
- `base` Monetary “Base Amount” (store, compute=_compute_base)
- `tax_id` Many2one → `account.tax` “TDS Section” (required, store, compute=_compute_tax_id)
- `amount` Monetary “TDS Amount” (compute=_compute_amount)

Public methods: `action_create_and_post_withhold`, `default_get`

Extension points: `_check_amounts`, `_get_withhold_type`, `_prepare_withhold_header`, `_prepare_withhold_move_lines`
