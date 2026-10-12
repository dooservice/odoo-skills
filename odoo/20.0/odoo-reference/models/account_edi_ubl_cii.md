# account_edi_ubl_cii — Import/Export electronic invoices with UBL/CII

Depends on: account.

## `account.edi.cii` (defines)

Base helpers for CII

Inherits: `account.edi.common`


## `account.edi.common` (defines)

Common functions for EDI documents: generate the data, the constraints, etc


Public methods: `format_float`, `module_installed`

Extension points: `_check_customer_vat_match`, `_check_required_fields`, `_get_basis_qty`, `_get_belgian_cocontractant_note`, `_get_currency_decimal_places`, `_get_default_notes`, `_get_document_allowance_charge_xpaths`, `_get_document_type`, `_get_document_type_code_vals`, `_get_invoice_line_xpaths`, `_get_tax_category_code`, `_get_tax_exemption_reason`

## `account.edi.ubl` (defines)

Base helpers for UBL

Inherits: `account.edi.common`


Extension points: `_get_notes`

## `account.edi.ubl_cen_en16931` (defines)

UBL CEN-EN16931

Inherits: `account.edi.ubl`


## `account.edi.ubl_pint` (defines)

UBL PINT

Inherits: `account.edi.ubl`


## `account.edi.ubl_pint_eu` (defines)

UBL PINT-EU Layer

Inherits: `account.edi.ubl_pint`, `account.edi.ubl_cen_en16931`


## `account.edi.xml.cii` (defines)

Factur-x/ZUGFeRD CII 2.2.0

Inherits: `account.edi.cii`


Extension points: `_check_non_0_rate_tax`, `_check_required_tax`, `_get_document_allowance_charge_xpaths`, `_get_document_nsmap`, `_get_exchanged_document_vals`, `_get_import_document_amount_sign`, `_get_invoice_line_xpaths`, `_get_invoice_node`, `_get_invoicing_period`, `_get_line_xpaths`, `_get_postal_address`, `_get_scheduled_delivery_time`, `_get_tax_nodes`

## `account.edi.xml.ubl_20` (defines)

UBL 2.0

Inherits: `account.edi.ubl`


Public methods: `add_invoice_line_optional_nodes`, `add_invoice_optional_nodes`, `format_float`

Extension points: `_get_address_node`, `_get_document_allowance_charge_node`, `_get_document_allowance_charge_xpaths`, `_get_document_line_node`, `_get_document_nsmap`, `_get_document_template`, `_get_document_type_code_node`, `_get_financial_account_node`, `_get_import_document_amount_sign`, `_get_invoice_line_node`, `_get_invoice_line_xpaths`, `_get_invoice_node`, `_get_line_discount_allowance_charge_node`, `_get_line_fixed_tax_allowance_charge_nodes`, `_get_line_xpaths`, `_get_party_node`, `_get_postal_address`, `_get_product_xpaths`, `_get_tags_for_document_type`, `_get_tax_category_node`, `_get_tax_nodes`, `_get_tax_subtotal_node`, `_get_tax_total_node`

## `account.edi.xml.ubl_21` (defines)

UBL 2.1

Inherits: `account.edi.xml.ubl_20`


Extension points: `_get_invoice_node`

## `account.edi.xml.ubl_a_nz` (defines)

A-NZ BIS Billing 3.0

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.edi.xml.ubl_bis3` (defines)

UBL BIS Billing 3.0.12

Inherits: `account.edi.xml.ubl_21`, `account.edi.ubl_pint_eu`


Extension points: `_get_customization_id`

## `account.edi.xml.ubl_efff` (defines)

E-FFF (BE)

Inherits: `account.edi.xml.ubl_20`


## `account.edi.xml.ubl_nl` (defines)

SI-UBL 2.0 (NLCIUS)

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.edi.xml.ubl_sg` (defines)

SG BIS Billing 3.0

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.edi.xml.ubl_de` (defines)

BIS3 DE (XRechnung)

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_customization_id`

## `account.move` (extends)

- `has_grouped_lines` Boolean
- `ubl_cii_xml_file` Binary “UBL/CII File”
- `ubl_cii_xml_filename` Char “UBL/CII Filename” (compute=_compute_filename)
- `ubl_cii_xml_id` Many2one → `ir.attachment` “Attachment”

Public methods: `action_group_ungroup_lines_by_tax`

Extension points: `_check_move_for_group_ungroup_lines_by_tax`, `_get_edi_decoder`, `_get_fields_to_detach`, `_get_import_file_type`, `_get_invoice_legal_documents`, `_get_line_vals_group_by_tax`, `_get_line_vals_list`, `_get_specific_tax`, `_post_process_link_to_purchase_order`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_invoice_extra_attachments`, `_get_move_constraints`, `_get_placeholder_mail_attachments_data`, `_get_ubl_available_attachments`

## `account.tax` (extends)

- `ubl_cii_tax_category_code` Selection “Tax Category Code”
- `ubl_cii_tax_exemption_reason` Char “Tax Exemption Reason”
- `ubl_cii_tax_exemption_reason_code` Selection “Tax Exemption Reason Code”
- `ubl_cii_requires_exemption_reason` Boolean (compute=_compute_ubl_cii_requires_exemption_reason)

## `ir.actions.report` (extends)


## `res.company` (extends)

- `routing_scheme` Selection (related=partner_id.routing_scheme)
- `routing_endpoint` Char (related=partner_id.routing_endpoint)
- `routing_identifier` Char (related=partner_id.routing_identifier)

## `res.partner` (extends)

- `invoice_edi_format` Selection
- `is_ubl_format` Boolean (compute=_compute_is_ubl_format)
- `routing_scheme` Selection “Routing ID” (store, compute=_compute_routing_scheme_endpoint)
- `routing_endpoint` Char “Routing Endpoint” (store, compute=_compute_routing_scheme_endpoint)
- `routing_identifier` Char “EDI Routing Address” (compute=_compute_routing_identifier)
- `available_routing_schemes` Json (compute=_compute_available_routing_schemes)

Public methods: `create`, `write`

Extension points: `_get_all_identifiers`, `_get_all_identifiers_metadata`, `_get_edi_builder`, `_get_peppol_edi_format`, `_get_peppol_formats`, `_get_preferred_routing_identifier_vals`, `_get_suggested_peppol_edi_format`, `_get_suggested_ubl_cii_edi_format`, `_get_ubl_cii_edi_format`, `_get_ubl_cii_formats`, `_get_ubl_cii_formats_by_country`, `_get_ubl_cii_formats_info`

## `uom.uom` (extends)

- `unece_code` Char “UN/ECE Code”
- `is_unece_code_supported` Boolean (compute=_compute_is_unece_code_supported)

Public methods: `create`, `write`

Extension points: `_get_unece_code`, `_get_uom_from_unece_code`

## `account.move.send.wizard` (extends)
