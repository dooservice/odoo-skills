# l10n_jo_edi — Jordan E-Invoicing

Depends on: account_edi_ubl_cii, l10n_jo.

## `account.edi.xml.ubl_21.jo` (defines)

UBL 2.1 (JoFotara)

Inherits: `account.edi.xml.ubl_21`


Public methods: `format_float`

Extension points: `_get_address_node`, `_get_document_allowance_charge_node`, `_get_line_discount_allowance_charge_node`, `_get_line_edi_id`, `_get_party_node`, `_get_tax_category_code`, `_get_tax_category_node`, `_get_tax_subtotal_node`

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
- `l10n_jo_edi_invoice_type` Selection “Invoice Type” (store, compute=_compute_l10n_jo_edi_invoice_type)

Public methods: `button_draft`, `download_l10n_jo_edi_computed_xml`

Extension points: `_get_fields_to_detach`, `_get_invoice_payment_method_code`, `_get_invoice_scope_code`, `_get_invoice_tax_payer_type_code`, `_get_name_invoice_report`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`, `_get_invoice_extra_attachments`, `_get_placeholder_mail_attachments_data`

## `account.tax` (extends)


## `ir.attachment` (extends)


## `res.company` (extends)

- `l10n_jo_edi_sequence_income_source` Char “JoFotara Sequence of Income Source”
- `l10n_jo_edi_secret_key` Char “JoFotara Secret Key”
- `l10n_jo_edi_client_identifier` Char “JoFotara Client ID”
- `l10n_jo_edi_taxpayer_type` Selection “JoFotara Taxpayer Type”
- `l10n_jo_edi_demo_mode` Boolean “JoFotara Demo Mode”

## `res.config.settings` (extends)

- `l10n_jo_edi_sequence_income_source` Char “JoFotara Sequence of Income Source” (related=company_id.l10n_jo_edi_sequence_income_source)
- `l10n_jo_edi_secret_key` Char “JoFotara Secret Key” (related=company_id.l10n_jo_edi_secret_key)
- `l10n_jo_edi_client_identifier` Char “JoFotara Client ID” (related=company_id.l10n_jo_edi_client_identifier)
- `l10n_jo_edi_taxpayer_type` Selection “JoFotara Taxpayer Type” (related=company_id.l10n_jo_edi_taxpayer_type)
- `l10n_jo_edi_demo_mode` Boolean “JoFotara Demo Mode” (related=company_id.l10n_jo_edi_demo_mode)
