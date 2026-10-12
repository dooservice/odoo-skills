# l10n_tw_edi_ecpay — Taiwan - E-invoicing

Depends on: l10n_tw.

## `account.move` (extends)

- `l10n_tw_edi_file_id` Many2one → `ir.attachment`
- `l10n_tw_edi_file` Binary “Ecpay JSON File” (readonly)
- `l10n_tw_edi_ecpay_invoice_id` Char “Ecpay Invoice Number” (readonly)
- `l10n_tw_edi_related_number` Char “Related Number” (readonly, store)
- `l10n_tw_edi_state` Selection “Invoice Status” (readonly)
- `l10n_tw_edi_love_code` Char “Love Code” (store, compute=_compute_love_code)
- `l10n_tw_edi_is_print` Boolean “Get Printed Version” (store, compute=_compute_is_print)
- `l10n_tw_edi_carrier_type` Selection “Carrier Type” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_carrier_number` Char “Carrier Number” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_carrier_number_2` Char “Carrier Number 2” (store, compute=_compute_carrier_info)
- `l10n_tw_edi_invoice_type` Selection “Ecpay Invoice Type” (store, compute=_compute_l10n_tw_edi_invoice_type)
- `l10n_tw_edi_clearance_mark` Selection “Clearance Mark”
- `l10n_tw_edi_zero_tax_rate_reason` Selection “Zero Tax Rate Reason”
- `l10n_tw_edi_is_zero_tax_rate` Boolean “Is Zero Tax Rate” (compute=_compute_l10n_tw_edi_is_zero_tax_rate)
- `l10n_tw_edi_invoice_create_date` Datetime “Creation Date” (readonly)
- `l10n_tw_edi_refund_state` Selection “Refund State” (readonly)
- `l10n_tw_edi_refund_agreement_type` Selection “Refund invoice Agreement Type”
- `l10n_tw_edi_allowance_notify_way` Selection “Allowance Notify Way”
- `l10n_tw_edi_invalidate_reason` Char “Invalidate Reason” (readonly)
- `l10n_tw_edi_refund_invoice_number` Char “Refund Invoice Number” (readonly)
- `l10n_tw_edi_is_b2b` Boolean “Is B2B” (compute=_compute_l10n_tw_edi_is_b2b)

Public methods: `button_draft`, `button_request_cancel`

Extension points: `_get_mail_thread_data_attachments`

## `account.move.line` (extends)

- `l10n_tw_edi_ecpay_item_sequence` Integer “Item Sequence” (readonly)

## `account.move.send` (extends)


Extension points: `_get_all_extra_edis`

## `account.tax` (extends)

- `l10n_tw_edi_tax_type` Selection “Ecpay Tax Type” (store, compute=_compute_l10n_tw_edi_tax_type)
- `l10n_tw_edi_special_tax_type` Selection “Ecpay Special Tax Type”

Extension points: `_check_special_tax_type_constrains`

## `res.company` (extends)

- `l10n_tw_edi_ecpay_staging_mode` Boolean “Staging mode”
- `l10n_tw_edi_ecpay_merchant_id` Char “MerchantID”
- `l10n_tw_edi_ecpay_hashkey` Char “Hashkey”
- `l10n_tw_edi_ecpay_hashIV` Char “HashIV”

## `res.config.settings` (extends)

- `l10n_tw_edi_ecpay_staging_mode` Boolean (related=company_id.l10n_tw_edi_ecpay_staging_mode)
- `l10n_tw_edi_ecpay_merchant_id` Char (related=company_id.l10n_tw_edi_ecpay_merchant_id)
- `l10n_tw_edi_ecpay_hashkey` Char (related=company_id.l10n_tw_edi_ecpay_hashkey)
- `l10n_tw_edi_ecpay_hashIV` Char (related=company_id.l10n_tw_edi_ecpay_hashIV)

## `res.partner` (extends)

- `invoice_edi_format` Selection

## `account.move.reversal` (extends)

- `l10n_tw_edi_refund_agreement_type` Selection “Agreement Type”
- `l10n_tw_edi_allowance_notify_way` Selection “Allowance Notify Way”
- `l10n_tw_edi_ecpay_invoice_id` Char (compute=_compute_from_moves)
- `l10n_tw_edi_is_b2b` Boolean (compute=_compute_from_moves)

Public methods: `reverse_moves`

Extension points: `_prepare_default_reversal`

## `l10n_tw_edi.invoice.cancel` (defines)

Implements cancelling an ecpay invoice.

- `invoice_id` Many2one → `account.move` “Document To Cancel” (required, readonly)
- `reason` Char (required)

Public methods: `button_request_cancel`

## `l10n_tw_edi.invoice.print` (defines)

Implements printingan ecpay invoice.

- `invoice_id` Many2one → `account.move` “Document To Print” (required, readonly)
- `print_format_b2c` Selection “Print Format (B2C)”
- `print_format_b2b` Selection “Print Format (B2B)”
- `l10n_tw_edi_is_b2b` Boolean “Is B2B” (related=invoice_id.l10n_tw_edi_is_b2b)

Public methods: `button_print`
