# l10n_ch — Switzerland - Accounting

Depends on: account, l10n_multilang, base_iban, l10n_din5008.

## `account.bank.statement.line` (extends)


## `account.move` (extends)

- `l10n_ch_isr_subscription` Char (compute=_compute_l10n_ch_isr_subscription)
- `l10n_ch_isr_subscription_formatted` Char (compute=_compute_l10n_ch_isr_subscription)
- `l10n_ch_isr_number` Char (store, compute=_compute_l10n_ch_isr_number)
- `l10n_ch_isr_number_spaced` Char (compute=_compute_l10n_ch_isr_number_spaced)
- `l10n_ch_isr_optical_line` Char (compute=_compute_l10n_ch_isr_optical_line)
- `l10n_ch_isr_valid` Boolean (compute=_compute_l10n_ch_isr_valid)
- `l10n_ch_isr_sent` Boolean
- `l10n_ch_currency_name` Char “Currency Name” (readonly, related=currency_id.name)
- `l10n_ch_isr_needs_fixing` Boolean (compute=_compute_l10n_ch_isr_needs_fixing)
- `l10n_ch_is_qr_valid` Boolean (compute=_compute_l10n_ch_qr_is_valid)

Public methods: `action_invoice_sent`, `l10n_ch_action_print_qr`, `message_post`, `space_qrr_reference`, `space_scor_reference`, `split_total_amount`

Extension points: `_get_invoice_reference_ch_invoice`, `_get_invoice_reference_ch_partner`, `_get_isrb_id_number`, `_get_l10n_ch_isr_optical_amount`

## `account.journal` (extends)

- `invoice_reference_model` Selection

## `account.chart.template` (extends)


## `ir.actions.report` (extends)


Public methods: `apply_qr_code_ch_cross_mask`, `get_available_barcode_masks`, `get_paperformat`

## `res.partner.bank` (extends)

- `l10n_ch_postal` Char “Swiss Postal Account” (store, compute=_compute_l10n_ch_postal)
- `l10n_ch_qr_iban` Char “QR-IBAN” (store, compute=_compute_l10n_ch_qr_iban)
- `l10n_ch_isr_subscription_chf` Char “CHF ISR Subscription Number”
- `l10n_ch_isr_subscription_eur` Char “EUR ISR Subscription Number”
- `l10n_ch_show_subscription` Boolean (compute=_compute_l10n_ch_show_subscription)

Public methods: `create`, `retrieve_acc_type`, `write`

Extension points: `_check_for_qr_code_errors`, `_check_postal_num`, `_check_subscription_num`, `_get_available_qr_methods`, `_get_partner_address_lines`, `_get_qr_code_generation_params`, `_get_qr_vals`, `_get_supported_account_types`

## `res.company` (extends)

- `l10n_ch_isr_preprinted_account` Boolean “Preprinted account” (compute=_compute_l10n_ch_isr)
- `l10n_ch_isr_preprinted_bank` Boolean “Preprinted bank” (compute=_compute_l10n_ch_isr)
- `l10n_ch_isr_print_bank_location` Boolean “Print bank location”
- `l10n_ch_isr_scan_line_left` Float “Scan line horizontal offset (mm)” (compute=_compute_l10n_ch_isr)
- `l10n_ch_isr_scan_line_top` Float “Scan line vertical offset (mm)” (compute=_compute_l10n_ch_isr)

## `res.config.settings` (extends)

- `l10n_ch_isr_preprinted_account` Boolean “Preprinted account” (related=company_id.l10n_ch_isr_preprinted_account)
- `l10n_ch_isr_preprinted_bank` Boolean “Preprinted bank” (related=company_id.l10n_ch_isr_preprinted_bank)
- `l10n_ch_isr_print_bank_location` Boolean “Print bank on ISR” (required, related=company_id.l10n_ch_isr_print_bank_location)
- `l10n_ch_isr_scan_line_left` Float “Horizontal offset” (related=company_id.l10n_ch_isr_scan_line_left)
- `l10n_ch_isr_scan_line_top` Float “Vertical offset” (related=company_id.l10n_ch_isr_scan_line_top)

## `report.l10n_ch.qr_report_main` (defines)

Swiss QR-bill report


Extension points: `_get_report_values`

## `l10n_ch.qr_invoice.wizard` (defines)

Handles problems occurring while creating multiple QR-invoices at once

- `nb_qr_inv` Integer (readonly)
- `nb_isr_inv` Integer (readonly)
- `nb_classic_inv` Integer (readonly)
- `qr_inv_text` Text (readonly)
- `isr_inv_text` Text (readonly)
- `classic_inv_text` Text (readonly)

Public methods: `action_view_faulty_invoices`, `default_get`, `print_all_invoices`

## `account.setup.bank.manual.config` (extends)
