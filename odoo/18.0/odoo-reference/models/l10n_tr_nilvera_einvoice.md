# l10n_tr_nilvera_einvoice — Türkiye - Nilvera E-Invoice

Depends on: l10n_tr_nilvera, account_edi_ubl_cii.

## `account.edi.xml.ubl.tr` (defines)

UBL-TR 1.2

Inherits: `account.edi.xml.ubl_21`


Extension points: `_get_additional_document_reference_list`, `_get_country_vals`, `_get_delivery_vals_list`, `_get_document_allowance_charge_vals_list`, `_get_invoice_currency_exchange_rate`, `_get_invoice_line_allowance_vals_list`, `_get_invoice_line_item_vals`, `_get_invoice_line_price_vals`, `_get_invoice_line_vals`, `_get_invoice_monetary_total_vals`, `_get_invoice_payment_means_vals_list`, `_get_invoice_period_vals_list`, `_get_invoice_tax_totals_vals_list`, `_get_partner_address_vals`, `_get_partner_party_identification_vals_list`, `_get_partner_party_legal_entity_vals_list`, `_get_partner_party_tax_scheme_vals_list`, `_get_partner_person_vals`, `_get_pricing_exchange_rate_vals_list`, `_get_tax_category_list`

## `account.journal` (extends)


Public methods: `l10n_tr_nilvera_get_documents`, `l10n_tr_nilvera_get_message_status`

## `account.move` (extends)

- `l10n_tr_nilvera_uuid` Char “Nilvera Document UUID” (readonly)
- `l10n_tr_nilvera_send_status` Selection “Nilvera Status” (readonly)

Public methods: `button_draft`

Extension points: `_get_partner_l10n_tr_nilvera_customer_alias_name`, `_get_ubl_cii_builder_from_xml_tree`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_l10n_tr_tax_company_tax_office_alert`, `_get_l10n_tr_tax_partner_address_alert`, `_get_l10n_tr_tax_partner_tax_office_alert`

## `res.partner.category` (extends)


Extension points: `_get_categories_from_xml_ids`, `_get_l10n_tr_official_categories`, `_get_l10n_tr_official_mandatory_categories`
