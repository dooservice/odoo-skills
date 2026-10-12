# l10n_in — Indian - Accounting

Depends on: account_tax_python, base_vat.

## `account.chart.template` (extends)


Extension points: `_get_demo_data`

## `account.journal` (extends)

- `l10n_in_gstin_partner_id` Many2one → `res.partner` “GSTIN Unit”

Public methods: `name_get`

## `account.move.line` (extends)


Public methods: `init`

## `account.tax` (extends)

- `l10n_in_reverse_charge` Boolean “Reverse charge”

Extension points: `_get_generation_dict_from_base_line`, `_get_generation_dict_from_tax_line`

## `account.move` (extends)

- `amount_total_words` Char “Total (In Words)” (compute=_compute_amount_total_words)
- `l10n_in_gst_treatment` Selection “GST Treatment” (store, compute=_compute_l10n_in_gst_treatment)
- `l10n_in_state_id` Many2one → `res.country.state` “Place of supply” (store, compute=_compute_l10n_in_state_id)
- `l10n_in_gstin` Char “GSTIN”
- `l10n_in_shipping_bill_number` Char “Shipping bill number” (readonly)
- `l10n_in_shipping_bill_date` Date “Shipping bill date” (readonly)
- `l10n_in_shipping_port_code_id` Many2one → `l10n_in.port.code` (readonly)
- `l10n_in_reseller_partner_id` Many2one → `res.partner` (readonly)
- `l10n_in_journal_type` Selection “Journal Type” (related=journal_id.type)

Public methods: `unlink`

Extension points: `_get_name_invoice_report`

## `account.chart.template` (extends)


Extension points: `_prepare_all_journals`

## `account.tax.template` (extends)

- `l10n_in_reverse_charge` Boolean “Reverse charge”

Extension points: `_get_tax_vals`

## `mail.message` (extends)

- `l10n_in_audit_log_preview` Html “Description” (compute=_compute_l10n_in_audit_log_preview)
- `l10n_in_audit_log_account_move_id` Many2one → `account.move` “Journal Entry” (compute=_compute_l10n_in_audit_log_document_name)

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
- `l10n_in_gsp` Selection “GSP”

Public methods: `get_values`

## `res.country.state` (extends)

- `l10n_in_tin` Char “TIN Number”

## `res.partner` (extends)

- `l10n_in_gst_treatment` Selection “GST Treatment”

Public methods: `check_vat_in`, `onchange_company_type`, `onchange_vat`

## `uom.uom` (extends)

- `l10n_in_code` Char “Indian GST UQC”
