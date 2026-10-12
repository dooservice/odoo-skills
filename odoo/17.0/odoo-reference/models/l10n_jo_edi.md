# l10n_jo_edi — Jordan E-Invoicing

Depends on: account_edi_ubl_cii, l10n_jo.

## `account.edi.xml.ubl_21.jo` (defines)

UBL 2.1 (JoFotara)

Inherits: `account.edi.xml.ubl_21`


Public methods: `format_float`

Extension points: `_get_additional_document_reference_list`, `_get_billing_reference_vals`, `_get_country_vals`, `_get_currency_decimal_places`, `_get_delivery_vals_list`, `_get_document_allowance_charge_vals_list`, `_get_empty_party_vals`, `_get_invoice_line_allowance_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_price_vals`, `_get_invoice_line_tax_totals_vals_list`, `_get_invoice_line_vals`, `_get_invoice_monetary_total_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_payment_terms_vals_list`, `_get_invoice_tax_totals_vals_helper`, `_get_invoice_tax_totals_vals_list`, `_get_line_amount_before_discount_jod`, `_get_line_discount_jod`, `_get_line_edi_id`, `_get_line_taxable_amount`, `_get_partner_address_vals`, `_get_partner_contact_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_party_vals`, `_get_payment_method_code`, `_get_seller_supplier_party_vals`, `_get_tax_category_list`, `_get_unit_price_jod`, `_get_uom_unece_code`

## `account.move` (extends)

- `l10n_jo_edi_uuid` Char “Invoice UUID” (store, compute=_compute_l10n_jo_edi_uuid)
- `l10n_jo_edi_qr` Char “QR”
- `l10n_jo_edi_is_needed` Boolean (compute=_compute_l10n_jo_edi_is_needed)
- `l10n_jo_edi_state` Selection “JoFotara State”
- `l10n_jo_edi_error` Text “JoFotara Error” (readonly)
- `l10n_jo_edi_computed_xml` Binary “Jordan E-Invoice computed XML File” (compute=_compute_l10n_jo_edi_computed_xml)
- `l10n_jo_edi_xml_attachment_file` Binary “Jordan E-Invoice XML File”
- `l10n_jo_edi_xml_attachment_id` Many2one → `ir.attachment` “Jordan E-Invoice XML”
- `reversed_entry_id` Many2one

Public methods: `button_draft`, `download_l10n_jo_edi_computed_xml`

Extension points: `_get_invoice_payment_method_code`, `_get_invoice_scope_code`, `_get_invoice_tax_payer_type_code`, `_get_name_invoice_report`

## `account.tax` (extends)


## `ir.attachment` (extends)


## `res.company` (extends)

- `l10n_jo_edi_sequence_income_source` Char “JoFotara Sequence of Income Source”
- `l10n_jo_edi_secret_key` Char “JoFotara Secret Key”
- `l10n_jo_edi_client_identifier` Char “JoFotara Client ID”
- `l10n_jo_edi_taxpayer_type` Selection “JoFotara Taxpayer Type”

## `res.config.settings` (extends)

- `l10n_jo_edi_sequence_income_source` Char “JoFotara Sequence of Income Source” (related=company_id.l10n_jo_edi_sequence_income_source)
- `l10n_jo_edi_secret_key` Char “JoFotara Secret Key” (related=company_id.l10n_jo_edi_secret_key)
- `l10n_jo_edi_client_identifier` Char “JoFotara Client ID” (related=company_id.l10n_jo_edi_client_identifier)
- `l10n_jo_edi_taxpayer_type` Selection “JoFotara Taxpayer Type” (related=company_id.l10n_jo_edi_taxpayer_type)

## `account.move.send` (extends)

- `l10n_jo_edi_is_visible` Boolean (compute=_compute_l10n_jo_edi_is_visible)
- `l10n_jo_edi_is_enabled` Boolean “Send JoFotara e-invoice” (store, compute=_compute_l10n_jo_edi_is_enabled)

Extension points: `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`, `_get_wizard_vals_restrict_to`, `_get_wizard_values`
