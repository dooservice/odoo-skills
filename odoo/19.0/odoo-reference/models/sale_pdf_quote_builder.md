# sale_pdf_quote_builder — Sales PDF Quotation Builder

Depends on: sale_management.

## `ir.actions.report` (extends)


Extension points: `_get_custom_value_from_order`, `_get_value_from_path`

## `product.document` (extends)

- `attached_on_sale` Selection
- `form_field_ids` Many2many → `sale.pdf.form.field` “Form Fields Included” (store, compute=_compute_form_field_ids)

Public methods: `action_open_pdf_form_fields`

Extension points: `_check_attached_on_and_datas_compatibility`

## `quotation.document` (defines)

Quotation's Headers & Footers

- `ir_attachment_id` Many2one → `ir.attachment` “Related attachment” (required)
- `document_type` Selection “Document Type” (required)
- `active` Boolean
- `sequence` Integer
- `quotation_template_ids` Many2many → `sale.order.template` “Quotation Templates”
- `form_field_ids` Many2many → `sale.pdf.form.field` “Form Fields Included” (store, compute=_compute_form_field_ids)
- `add_by_default` Boolean “Add By Default”

Public methods: `action_open_pdf_form_fields`, `create`

Extension points: `_check_pdf_validity`

## `sale.order` (extends)

- `available_quotation_document_ids` Many2many → `quotation.document` “Available Quotation Documents” (compute=_compute_available_quotation_document_ids)
- `is_pdf_quote_builder_available` Boolean (compute=_compute_is_pdf_quote_builder_available)
- `quotation_document_ids` Many2many → `quotation.document` “Headers/Footers”
- `customizable_pdf_form_fields` Json “Customizable PDF Form Fields”

Public methods: `get_update_included_pdf_params`

## `sale.order.line` (extends)

- `available_product_document_ids` Many2many → `product.document` “Available Product Documents” (compute=_compute_available_product_document_ids)
- `product_document_ids` Many2many → `product.document` “Product Documents”

## `sale.order.template` (extends)

- `quotation_document_ids` Many2many → `quotation.document` “Headers and footers”

## `sale.pdf.form.field` (defines)

Form fields of inside quotation documents.

- `name` Char “Form Field Name” (required, readonly)
- `document_type` Selection “Document Type” (required, readonly)
- `path` Char “Path”
- `product_document_ids` Many2many → `product.document` “Product Documents”
- `quotation_document_ids` Many2many → `quotation.document` “Quotation Documents”

Extension points: `_check_document_type_and_document_linked_compatibility`, `_check_form_field_name_follows_pattern`, `_check_valid_and_existing_paths`, `_create_or_update_form_fields_on_pdf_records`
