# sale_edi_ubl — Import electronic orders with UBL

Depends on: sale, account_edi_ubl_cii.

## `product.product` (extends)


Extension points: `_get_product_domain_search_order`, `_get_retrieval_product_search_plan`

## `sale.edi.xml.ubl_bis3` (defines)

Sale BIS Ordering 3.5

Inherits: `account.edi.xml.ubl_bis3`


Extension points: `_get_product_xpaths`, `_get_sale_order_node`

## `sale.order` (extends)


Extension points: `_create_activity_set_details`, `_get_edi_builders`, `_get_edi_decoder`, `_get_import_file_type`, `_get_line_vals_list`
