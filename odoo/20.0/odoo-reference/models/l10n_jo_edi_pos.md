# l10n_jo_edi_pos — Jordan Accounting EDI for POS

Depends on: l10n_jo_edi, pos_edi_ubl.

## `account.move` (extends)


## `pos.edi.xml.ubl_21.jo` (defines)

UBL 2.1 (JoFotara) for PoS Orders

Inherits: `pos.edi.xml.ubl_21`


Public methods: `format_float`

Extension points: `_get_address_node`, `_get_party_node`, `_get_payment_method_code`, `_get_pos_order_line_id`, `_get_pos_order_line_node`, `_get_pos_order_node`, `_get_tax_category_code`, `_get_tax_category_node`, `_get_tax_subtotal_node`, `_get_tax_total_node`

## `pos.order` (extends)

- `l10n_jo_edi_pos_return_reason` Char “Return Reason”
- `l10n_jo_edi_pos_enabled` Boolean (related=company_id.l10n_jo_edi_pos_enabled)
- `l10n_jo_edi_pos_uuid` Char “Order UUID” (store, compute=_compute_l10n_jo_edi_pos_uuid)
- `l10n_jo_edi_pos_qr` Char “QR”
- `l10n_jo_edi_pos_state` Selection “JoFotara State”
- `l10n_jo_edi_pos_error` Text “JoFotara Error” (readonly)
- `l10n_jo_edi_pos_computed_xml` Binary “Jordan E-Invoice computed XML File” (compute=_compute_l10n_jo_edi_pos_computed_xml)
- `l10n_jo_edi_pos_xml_attachment_id` Many2one → `ir.attachment` “Jordan E-Invoice XML”

Public methods: `action_pos_order_paid`, `button_l10n_jo_edi_pos`, `download_l10n_jo_edi_pos_computed_xml`

Extension points: `_get_order_payment_method_code`, `_get_order_scope_code`, `_get_order_tax_payer_type_code`, `_prepare_invoice_vals`

## `pos.payment.method` (extends)

- `country_code` Char (related=company_id.country_id.code)
- `l10n_jo_edi_pos_is_cash` Boolean “JoFotara Cash” (store, compute=_compute_l10n_jo_edi_pos_is_cash)

## `res.company` (extends)

- `l10n_jo_edi_pos_enabled` Boolean
- `l10n_jo_edi_pos_testing_mode` Boolean

## `res.config.settings` (extends)

- `l10n_jo_edi_pos_enabled` Boolean (related=company_id.l10n_jo_edi_pos_enabled)
- `l10n_jo_edi_pos_testing_mode` Boolean (related=company_id.l10n_jo_edi_pos_testing_mode)

## `pos.order.receipt` (extends)

Point of Sale Order Receipt Generator


Public methods: `order_receipt_generate_data`
