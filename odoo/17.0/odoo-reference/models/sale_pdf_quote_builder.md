# sale_pdf_quote_builder — Sales PDF Quotation Builder

Depends on: sale_management.

## `ir.actions.report` (extends)


Extension points: `_get_form_fields_mapping`, `_get_sol_form_fields_mapping`, `_get_sol_form_fields_names`

## `product.document` (extends)

- `attached_on` Selection

Extension points: `_check_attached_on_and_datas_compatibility`

## `res.company` (extends)

- `sale_header` Binary “Header pages”
- `sale_header_name` Char
- `sale_footer` Binary “Footer pages”
- `sale_footer_name` Char

## `sale.order` (extends)


## `sale.order.template` (extends)

- `sale_header` Binary “Header pages”
- `sale_header_name` Char
- `sale_footer` Binary “Footer pages”
- `sale_footer_name` Char

## `res.config.settings` (extends)

- `sale_header` Binary (related=company_id.sale_header)
- `sale_header_name` Char (related=company_id.sale_header_name)
- `sale_footer` Binary (related=company_id.sale_footer)
- `sale_footer_name` Char (related=company_id.sale_footer_name)
