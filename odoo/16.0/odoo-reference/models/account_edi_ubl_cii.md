# account_edi_ubl_cii — Import/Export electronic invoices with UBL/CII

Depends on: account_edi.

## `account.edi.common` (defines)

Common functions for EDI documents: generate the data, the constraints, etc


Public methods: `format_float`

Extension points: `_check_required_fields`, `_check_xml_ecosio`, `_get_tax_category_list`, `_get_tax_unece_codes`, `_get_uom_unece_code`

## `account.edi.format` (extends)


Extension points: `_create_invoice_from_xml_tree`, `_get_move_applicability`, `_get_xml_builder`, `_prepare_invoice_report`

## `account.edi.xml.cii` (defines)

Factur-x/XRechnung CII 2.2.0

Inherits: `account.edi.common`


Extension points: `_check_non_0_rate_tax`, `_check_required_tax`, `_get_exchanged_document_vals`, `_get_import_document_amount_sign`, `_get_invoicing_period`, `_get_scheduled_delivery_time`

## `account.edi.xml.ubl_20` (defines)

UBL 2.0

Inherits: `account.edi.common`


Extension points: `_get_bank_address_vals`, `_get_country_vals`, `_get_delivery_vals_list`, `_get_document_allowance_charge_vals_list`, `_get_early_payment_discount_grouped_by_tax_rate`, `_get_financial_account_vals`, `_get_financial_institution_branch_vals`, `_get_financial_institution_vals`, `_get_import_document_amount_sign`, `_get_invoice_line_allowance_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_price_vals`, `_get_invoice_line_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_payment_terms_vals_list`, `_get_invoice_period_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`

## `account.edi.xml.ubl_21` (defines)

UBL 2.1

Inherits: `account.edi.xml.ubl_20`


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

## `ir.actions.report` (extends)


Extension points: `_get_edi_document_format_codes_for_pdf_embedding`

## `mail.template` (extends)


Extension points: `_get_edi_attachments`
