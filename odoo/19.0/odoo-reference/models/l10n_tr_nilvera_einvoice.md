# l10n_tr_nilvera_einvoice — Türkiye - Nilvera E-Invoice

Depends on: l10n_tr_nilvera, account_edi_ubl_cii.

## `account.edi.xml.ubl.tr` (defines)

UBL-TR 1.2

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_address_node`, `_get_import_document_amount_sign`, `_get_party_identification_node_list`, `_get_party_node`, `_get_tax_category_code`, `_get_tax_category_node`, `_get_tax_subtotal_node`

## `account.journal` (extends)


Public methods: `button_fetch_in_einvoices`, `button_refresh_out_einvoices_status`

Extension points: `_check_api_key`

## `account.move` (extends)

- `l10n_tr_nilvera_uuid` Char “Nilvera Document UUID” (readonly)
- `l10n_tr_nilvera_send_status` Selection “Nilvera Status” (readonly)

Public methods: `button_draft`, `l10n_tr_nilvera_get_pdf`

Extension points: `_get_import_file_type`, `_get_invoice_nilvera_pdf_report_filename`, `_get_nilvera_last_fetch_date`, `_get_partner_l10n_tr_nilvera_customer_alias_name`, `_get_ubl_cii_builder_from_xml_tree`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_invoice_extra_attachments`, `_get_l10n_tr_tax_company_tax_office_alert`, `_get_l10n_tr_tax_partner_address_alert`, `_get_l10n_tr_tax_partner_tax_office_alert`

## `res.partner.category` (extends)


Extension points: `_get_categories_from_xml_ids`, `_get_l10n_tr_official_categories`, `_get_l10n_tr_official_mandatory_categories`
