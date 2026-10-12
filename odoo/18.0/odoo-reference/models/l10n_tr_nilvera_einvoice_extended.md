# l10n_tr_nilvera_einvoice_extended — Türkiye - Nilvera E-Invoice Extended

Depends on: l10n_tr_nilvera_einvoice, contacts.

## `account.edi.xml.ubl.tr` (extends)


Extension points: `_get_invoice_line_delivery_vals`, `_get_invoice_line_tax_totals_vals_list`, `_get_invoice_line_vals`, `_get_invoice_monetary_total_vals`, `_get_invoice_tax_totals_vals_list`, `_get_ministry_vals`, `_get_partner_party_tax_scheme_vals_list`, `_get_tax_category_list`, `_get_tax_grouping_key`, `_get_tr_profile_id`, `_get_tr_tax_totals`

## `account.move` (extends)

- `l10n_tr_gib_invoice_scenario` Selection “Invoice Scenario”
- `l10n_tr_gib_invoice_type` Selection “GIB Invoice Type” (store, compute=_compute_l10n_tr_gib_invoice_type)
- `l10n_tr_is_export_invoice` Boolean “Is GIB Export”
- `l10n_tr_shipping_type` Selection “Shipping Method”
- `l10n_tr_exemption_code_id` Many2one → `l10n_tr_nilvera_einvoice_extended.account.tax.code` “Exemption Reason” (store, compute=_compute_l10n_tr_exemption_code_id)
- `l10n_tr_exemption_code_domain_list` Binary (compute=_compute_l10n_tr_exemption_code_domain_list)
- `l10n_tr_nilvera_customer_status` Selection “Partner Nilvera Status” (related=partner_id.l10n_tr_nilvera_customer_status)

Extension points: `_get_partner_l10n_tr_nilvera_customer_alias_name`

## `account.move.line` (extends)

- `l10n_tr_ctsp_number` Char “CTSP Number” (store, compute=_compute_l10n_tr_ctsp_number)

Extension points: `_check_l10n_tr_ctsp_number`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_l10n_tr_tax_company_tax_office_alert`, `_get_l10n_tr_tax_partner_address_alert`, `_get_l10n_tr_tax_partner_tax_office_alert`

## `account.tax` (extends)

- `l10n_tr_tax_withholding_code_id` Many2one → `l10n_tr_nilvera_einvoice_extended.account.tax.code` “Withholding Reason”

## `l10n_tr_nilvera_einvoice_extended.account.tax.code` (defines)

Turkish Tax Codes (GIB Codes)

- `name` Char “Reason” (required)
- `code` Integer “Reason Code” (required)
- `percentage` Float
- `code_type` Selection “Code Type” (required)

## `l10n_tr_nilvera_einvoice_extended.tax.office` (defines)

Turkish Tax Office

- `name` Char
- `code` Integer
- `state_id` Many2one → `res.country.state`
- `state_code` Char (related=state_id.code)

## `product.product` (extends)

- `l10n_tr_ctsp_number` Char “CTSP Number”

Extension points: `_check_l10n_tr_ctsp_number`

## `product.template` (extends)

- `l10n_tr_ctsp_number` Char “CTSP Number” (compute=_compute_l10n_tr_ctsp_number)

## `res.company` (extends)

- `l10n_tr_tax_office_id` Many2one (related=partner_id.l10n_tr_tax_office_id)
- `l10n_tr_nilvera_export_alias` Char “Nilvera Export Alias”

## `res.config.settings` (extends)

- `l10n_tr_nilvera_export_alias` Char “Nilvera Export Alias” (related=company_id.l10n_tr_nilvera_export_alias)

## `res.partner` (extends)

- `l10n_tr_tax_office_id` Many2one → `l10n_tr_nilvera_einvoice_extended.tax.office` “Turkish Tax Office”

## `account.chart.template` (extends)


Extension points: `_get_tr_withholding_account_tax`, `_get_tr_withholding_account_tax_code`
