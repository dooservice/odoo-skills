# purchase_edi_ubl_bis3 — Import/Export electronic orders with UBL

Depends on: purchase, account_edi_ubl_cii.

## `account.move` (extends)


Extension points: `_check_move_for_group_ungroup_lines_by_tax`

## `purchase.edi.xml.ubl_bis3` (defines)

Purchase UBL BIS Ordering 3.5

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_purchase_order_node`

## `purchase.order` (extends)


Extension points: `_create_activity_set_details`, `_get_edi_builders`, `_get_edi_decoder`, `_get_import_file_type`, `_get_line_vals_list`
