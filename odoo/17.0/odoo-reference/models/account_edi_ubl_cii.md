# account_edi_ubl_cii — Import/Export electronic invoices with UBL/CII

Depends on: account.

## `account.edi.common` (defines)

Common functions for EDI documents: generate the data, the constraints, etc


Public methods: `format_float`

Extension points: `_check_required_fields`, `_check_xml_ecosio`, `_get_belgian_cocontractant_note`, `_get_currency_decimal_places`, `_get_tax_category_list`, `_get_tax_unece_codes`, `_get_uom_unece_code`

## `account.edi.xml.cii` (defines)

Factur-x/XRechnung CII 2.2.0

Inherits: `account.edi.common`


Extension points: `_check_non_0_rate_tax`, `_check_required_tax`, `_get_exchanged_document_vals`, `_get_import_document_amount_sign`, `_get_invoicing_period`, `_get_scheduled_delivery_time`

## `account.edi.xml.ubl_20` (defines)

UBL 2.0

Inherits: `account.edi.common`


Extension points: `_get_additional_document_reference_list`, `_get_bank_address_vals`, `_get_country_vals`, `_get_delivery_vals_list`, `_get_document_allowance_charge_vals_list`, `_get_document_type_code_vals`, `_get_early_payment_discount_grouped_by_tax_rate`, `_get_financial_account_vals`, `_get_financial_institution_branch_vals`, `_get_financial_institution_vals`, `_get_import_document_amount_sign`, `_get_invoice_line_allowance_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_price_vals`, `_get_invoice_line_tax_totals_vals_list`, `_get_invoice_line_vals`, `_get_invoice_monetary_total_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_payment_terms_vals_list`, `_get_invoice_period_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_note_vals_list`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`, `_get_partner_person_vals`, `_get_pricing_exchange_rate_vals_list`

## `account.edi.xml.ubl_21` (defines)

UBL 2.1

Inherits: `account.edi.xml.ubl_20`


Extension points: `_get_customization_ids`, `_get_selfbilling_customization_ids`

## `account.edi.xml.ubl_a_nz` (defines)

A-NZ BIS Billing 3.0

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`

## `account.edi.xml.ubl_bis3` (defines)

UBL BIS Billing 3.0.12

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_country_vals`, `_get_delivery_vals_list`, `_get_financial_institution_branch_vals`, `_get_invoice_line_allowance_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`

## `account.edi.xml.ubl_efff` (defines)

E-FFF (BE)

Inherits: `account.edi.xml.ubl_20`


## `account.edi.xml.ubl_nl` (defines)

SI-UBL 2.0 (NLCIUS)

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_invoice_line_allowance_vals_list`, `_get_invoice_payment_means_vals_list`, `_get_partner_address_vals`, `_get_tax_category_list`

## `account.edi.xml.ubl_sg` (defines)

SG BIS Billing 3.0

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_invoice_payment_means_vals_list`, `_get_partner_party_vals`, `_get_tax_category_list`, `_get_tax_sg_codes`

## `account.edi.xml.ubl_de` (defines)

BIS3 DE (XRechnung)

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_partner_party_vals`

## `account.move` (extends)

- `ubl_cii_xml_id` Many2one → `ir.attachment` “Attachment”
- `ubl_cii_xml_file` Binary “UBL/CII File”

Public methods: `action_group_ungroup_lines_by_tax`

Extension points: `_check_move_for_group_ungroup_lines_by_tax`, `_get_edi_decoder`, `_get_line_vals_group_by_tax`, `_get_ubl_cii_builder_from_xml_tree`, `_post_process_link_to_purchase_order`

## `ir.actions.report` (extends)


## `res.company` (extends)

- `invoice_is_ubl_cii` Boolean “Generate Peppol format by default”

## `res.config.settings` (extends)

- `invoice_is_ubl_cii` Boolean “Peppol format” (related=company_id.invoice_is_ubl_cii)

## `res.partner` (extends)

- `ubl_cii_format` Selection “Format” (store, compute=_compute_ubl_cii_format)
- `peppol_endpoint` Char “Peppol Endpoint” (store, compute=_compute_peppol_endpoint)
- `peppol_eas` Selection “Peppol e-address (EAS)” (store, compute=_compute_peppol_eas)
- `hide_peppol_fields` Boolean (compute=_compute_hide_peppol_fields)

Extension points: `_check_peppol_eas`, `_check_peppol_fields`, `_get_edi_builder`, `_get_peppol_endpoint_value`, `_get_ubl_cii_formats`

## `account.move.send` (extends)

- `enable_ubl_cii_xml` Boolean (compute=_compute_enable_ubl_cii_xml)
- `checkbox_ubl_cii_label` Char (compute=_compute_checkbox_ubl_cii_label)
- `checkbox_ubl_cii_xml` Boolean (store, compute=_compute_checkbox_ubl_cii_xml)
- `ubl_partner_warning` Char “Partner warning” (compute=_compute_ubl_warnings)
- `show_ubl_company_warning` Boolean “Company warning” (compute=_compute_ubl_warnings)

Extension points: `_get_invoice_edi_format`, `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`, `_get_ubl_available_attachments`, `_get_wizard_vals_restrict_to`, `_get_wizard_values`
