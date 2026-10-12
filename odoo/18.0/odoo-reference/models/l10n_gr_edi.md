# l10n_gr_edi — Greece - myDATA

Depends on: l10n_gr.

## `account.fiscal.position` (extends)

- `l10n_gr_edi_preferred_classification_ids` One2many → `l10n_gr_edi.preferred_classification` “Preferred myDATA Classification”

## `account.move` (extends)

- `l10n_gr_edi_mark` Char “Mark” (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_cls_mark` Char “Classification Mark” (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_document_ids` One2many → `l10n_gr_edi.document` (readonly)
- `l10n_gr_edi_state` Selection “myDATA Status” (store, compute=_compute_from_l10n_gr_edi_document_ids)
- `l10n_gr_edi_available_inv_type` Char (compute=_compute_l10n_gr_edi_available_inv_type)
- `l10n_gr_edi_correlation_id` Many2one → `account.move` “Correlated Invoice”
- `l10n_gr_edi_inv_type` Selection “myDATA Invoice Type” (store, compute=_compute_l10n_gr_edi_inv_type)
- `l10n_gr_edi_payment_method` Selection “Payment Method” (store, compute=_compute_l10n_gr_edi_payment_method)
- `l10n_gr_edi_alerts` Json (compute=_compute_l10n_gr_edi_alerts)
- `l10n_gr_edi_need_correlated` Boolean (compute=_compute_l10n_gr_edi_need_fields)
- `l10n_gr_edi_need_payment_method` Boolean (compute=_compute_l10n_gr_edi_need_fields)
- `l10n_gr_edi_enable_view_mydata` Boolean (compute=_compute_l10n_gr_edi_enable_fields)
- `l10n_gr_edi_enable_send_invoices` Boolean (compute=_compute_l10n_gr_edi_enable_fields)
- `l10n_gr_edi_enable_send_expense_classification` Boolean (compute=_compute_l10n_gr_edi_enable_fields)
- `l10n_gr_edi_attachment_id` Many2one → `ir.attachment` (store, compute=_compute_from_l10n_gr_edi_document_ids)

Public methods: `l10n_gr_edi_try_send_expense_classification`, `l10n_gr_edi_try_send_invoices`

Extension points: `_get_name_invoice_report`

## `account.move.line` (extends)

- `l10n_gr_edi_available_cls_category` Char (compute=_compute_l10n_gr_edi_available_cls_category)
- `l10n_gr_edi_available_cls_type` Char (compute=_compute_l10n_gr_edi_available_cls_type)
- `l10n_gr_edi_available_cls_vat` Char (compute=_compute_l10n_gr_edi_available_cls_type)
- `l10n_gr_edi_need_exemption_category` Boolean (compute=_compute_l10n_gr_edi_need_exemption_category)
- `l10n_gr_edi_detail_type` Selection “Detail Type” (store, compute=_compute_l10n_gr_edi_detail_type)
- `l10n_gr_edi_cls_category` Selection “myDATA Category” (store, compute=_compute_l10n_gr_edi_cls_category)
- `l10n_gr_edi_cls_type` Selection “myDATA Type” (store, compute=_compute_l10n_gr_edi_cls_type)
- `l10n_gr_edi_cls_vat` Selection “VAT Classification” (store, compute=_compute_l10n_gr_edi_cls_vat)
- `l10n_gr_edi_tax_exemption_category` Selection “Tax Exemption Category” (store, compute=_compute_l10n_gr_edi_tax_exemption_category)

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_all_extra_edis`

## `account.tax` (extends)

- `l10n_gr_edi_default_tax_exemption_category` Selection “Default Tax Exemption Category”

## `l10n_gr_edi.document` (defines)

Greece document object for tracking all sent XML to myDATA

- `move_id` Many2one → `account.move`
- `state` Selection “myDATA Status” (required)
- `datetime` Datetime
- `attachment_id` Many2one → `ir.attachment` “XML File”
- `message` Char
- `mydata_mark` Char
- `mydata_cls_mark` Char
- `mydata_url` Char

Public methods: `action_download`

## `l10n_gr_edi.preferred_classification` (defines)

Preferred myDATA classification combinations for a particular product

- `product_template_id` Many2one → `product.template`
- `fiscal_position_id` Many2one → `account.fiscal.position`
- `priority` Integer “Priority”
- `l10n_gr_edi_inv_type` Selection “Invoice Type”
- `l10n_gr_edi_cls_category` Selection “myDATA Category”
- `l10n_gr_edi_cls_type` Selection “myDATA Type”
- `l10n_gr_edi_available_inv_type` Char
- `l10n_gr_edi_available_cls_category` Char (compute=_compute_l10n_gr_edi_available_cls_category)
- `l10n_gr_edi_available_cls_type` Char (compute=_compute_l10n_gr_edi_available_cls_type)

Extension points: `_get_l10n_gr_edi_available_cls_category`, `_get_l10n_gr_edi_available_cls_type`, `_get_l10n_gr_edi_available_cls_vat`

## `product.template` (extends)

- `l10n_gr_edi_preferred_classification_ids` One2many → `l10n_gr_edi.preferred_classification` “Preferred myDATA Classification”

## `res.company` (extends)

- `l10n_gr_edi_aade_id` Char “AADE User ID”
- `l10n_gr_edi_aade_key` Char “AADE Subscription Key”
- `l10n_gr_edi_branch_number` Integer (related=partner_id.l10n_gr_edi_branch_number)
- `l10n_gr_edi_test_env` Boolean “Greece Test Environment”

## `res.config.settings` (extends)

- `l10n_gr_edi_aade_id` Char (related=company_id.l10n_gr_edi_aade_id)
- `l10n_gr_edi_aade_key` Char (related=company_id.l10n_gr_edi_aade_key)
- `l10n_gr_edi_branch_number` Integer (related=company_id.l10n_gr_edi_branch_number)
- `l10n_gr_edi_test_env` Boolean (related=company_id.l10n_gr_edi_test_env)

## `res.partner` (extends)

- `l10n_gr_edi_branch_number` Integer “Branch Number” (store, compute=_compute_l10n_gr_edi_branch_number)

## `account.move.reversal` (extends)


Extension points: `_prepare_default_reversal`
