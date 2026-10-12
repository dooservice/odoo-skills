# l10n_in — Indian - Accounting

Depends on: account_tax_python, base_vat.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`, `_get_demo_data_attachment`, `_get_demo_data_config_settings`, `_get_demo_data_mail_message`, `_get_demo_data_move`, `_get_demo_data_partner`, `_get_demo_data_res_partner_category`, `_post_load_demo_data`

## `account.move` (extends)

- `l10n_in_gst_treatment` Selection “GST Treatment” (store, compute=_compute_l10n_in_gst_treatment)
- `l10n_in_state_id` Many2one → `res.country.state` “Place of supply” (store, compute=_compute_l10n_in_state_id)
- `l10n_in_gstin` Char “GSTIN”
- `l10n_in_shipping_bill_number` Char “Shipping bill number”
- `l10n_in_shipping_bill_date` Date “Shipping bill date”
- `l10n_in_shipping_port_code_id` Many2one → `l10n_in.port.code`
- `l10n_in_reseller_partner_id` Many2one → `res.partner`
- `l10n_in_journal_type` Selection “Journal Type” (related=journal_id.type)

Public methods: `unlink`

Extension points: `_get_name_invoice_report`

## `account.tax` (extends)

- `l10n_in_reverse_charge` Boolean “Reverse charge”

Extension points: `_get_generation_dict_from_base_line`, `_get_generation_dict_from_tax_line`

## `res.company` (extends)

- `l10n_in_upi_id` Char “UPI Id”
- `l10n_in_gst_state_warning` Char (related=partner_id.l10n_in_gst_state_warning)

Public methods: `action_update_state_as_per_gstin`, `create`, `write`

## `mail.message` (extends)

- `l10n_in_audit_log_preview` Html “Audit Preview” (compute=_compute_l10n_in_audit_log_preview)
- `l10n_in_audit_log_account_move_id` Many2one → `account.move` “Accounting Entry” (compute=_compute_l10n_in_audit_log_document_name)

## `l10n_in.port.code` (defines)

Indian port code

- `code` Char “Port Code” (required)
- `name` Char “Port” (required)
- `state_id` Many2one → `res.country.state` “State”

## `product.template` (extends)

- `l10n_in_hsn_code` Char “HSN/SAC Code”
- `l10n_in_hsn_description` Char “HSN/SAC Description”

## `res.config.settings` (extends)

- `group_l10n_in_reseller` Boolean “Manage Reseller(E-Commerce)”
- `module_l10n_in_edi` Boolean “Indian Electronic Invoicing”
- `module_l10n_in_edi_ewaybill` Boolean “Indian Electronic Waybill”
- `l10n_in_gsp` Selection “GSP”

Public methods: `get_values`

## `res.country.state` (extends)

- `l10n_in_tin` Char “TIN Number”

## `res.partner` (extends)

- `l10n_in_gst_treatment` Selection “GST Treatment”
- `l10n_in_pan` Char “PAN”
- `display_pan_warning` Boolean “Display pan warning” (compute=_compute_display_pan_warning)
- `l10n_in_gst_state_warning` Char (compute=_compute_l10n_in_gst_state_warning)

Public methods: `action_update_state_as_per_gstin`, `check_vat_in`, `onchange_company_type`, `onchange_vat`

## `account.chart.template` (extends)


Extension points: `_get_in_account_fiscal_position`, `_get_in_res_company`, `_get_in_template_data`, `_get_l10n_in_fiscal_tax_vals`

## `uom.uom` (extends)

- `l10n_in_code` Char “Indian GST UQC”
