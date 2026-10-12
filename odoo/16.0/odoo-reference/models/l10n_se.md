# l10n_se — Sweden - Accounting

Depends on: account, base_vat.

## `account.journal` (extends)

- `invoice_reference_model` Selection
- `l10n_se_invoice_ocr_length` Integer “OCR Number Length”

Extension points: `_check_l10n_se_invoice_ocr_length`

## `account.move` (extends)


Extension points: `_get_invoice_reference_se_ocr2`, `_get_invoice_reference_se_ocr2_invoice`, `_get_invoice_reference_se_ocr2_partner`, `_get_invoice_reference_se_ocr3`, `_get_invoice_reference_se_ocr3_invoice`, `_get_invoice_reference_se_ocr3_partner`, `_get_invoice_reference_se_ocr4`, `_get_invoice_reference_se_ocr4_invoice`, `_get_invoice_reference_se_ocr4_partner`

## `res.company` (extends)

- `org_number` Char (compute=_compute_org_number)

## `res.partner` (extends)

- `l10n_se_check_vendor_ocr` Boolean “Check Vendor OCR”
- `l10n_se_default_vendor_payment_ref` Char “Default Vendor Payment Ref”

Public methods: `onchange_l10n_se_default_vendor_payment_ref`
