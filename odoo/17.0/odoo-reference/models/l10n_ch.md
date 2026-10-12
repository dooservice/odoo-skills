# l10n_ch — Switzerland - Accounting

Depends on: account, base_iban, l10n_din5008.

## `account.move` (extends)

- `l10n_ch_is_qr_valid` Boolean (compute=_compute_l10n_ch_qr_is_valid)

Public methods: `get_l10n_ch_qrr_number`, `l10n_ch_action_print_qr`, `space_qrr_reference`, `space_scor_reference`

Extension points: `_get_invoice_reference_ch_invoice`, `_get_invoice_reference_ch_partner`

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.payment` (extends)

- `l10n_ch_reference_warning_msg` Char (compute=_compute_l10n_ch_reference_warning_msg)

## `ir.actions.report` (extends)


Public methods: `apply_qr_code_ch_cross_mask`, `get_available_barcode_masks`, `get_paperformat`

## `res.partner.bank` (extends)

- `l10n_ch_qr_iban` Char “QR-IBAN” (store, compute=_compute_l10n_ch_qr_iban)
- `l10n_ch_display_qr_bank_options` Boolean (compute=_compute_l10n_ch_display_qr_bank_options)

Public methods: `create`, `write`

Extension points: `_check_for_qr_code_errors`, `_get_available_qr_methods`, `_get_error_messages_for_qr`, `_get_partner_address_lines`, `_get_qr_code_generation_params`, `_get_qr_vals`

## `account.chart.template` (extends)


Extension points: `_get_ch_res_company`, `_get_ch_template_data`

## `report.l10n_ch.qr_report_main` (defines)

Swiss QR-bill report


Extension points: `_get_report_values`

## `l10n_ch.qr_invoice.wizard` (defines)

Handles problems occurring while creating multiple QR-invoices at once

- `nb_qr_inv` Integer (readonly)
- `nb_classic_inv` Integer (readonly)
- `qr_inv_text` Text (readonly)
- `classic_inv_text` Text (readonly)

Public methods: `action_view_faulty_invoices`, `default_get`, `print_all_invoices`

## `account.setup.bank.manual.config` (extends)

- `l10n_ch_display_qr_bank_options` Boolean (compute=_compute_l10n_ch_display_qr_bank_options)
