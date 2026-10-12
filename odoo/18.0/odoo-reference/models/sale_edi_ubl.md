# sale_edi_ubl — Import electronic orders with UBL

Depends on: sale, account_edi_ubl_cii.

## `sale.edi.common` (defines)

Common functions for EDI orders

Inherits: `account.edi.common`


Extension points: `_get_partner_detail_str`

## `sale.edi.xml.ubl_bis3` (defines)

UBL BIS Ordering 3.0

Inherits: `sale.edi.common`, `account.edi.xml.ubl_bis3`


Extension points: `_get_line_xpaths`

## `sale.order` (extends)


Extension points: `_create_activity_set_details`, `_get_line_vals_list`, `_get_order_edi_decoder`, `_get_order_ubl_builder_from_xml_tree`
