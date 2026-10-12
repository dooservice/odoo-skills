# l10n_ke_edi_tremol — Kenya Tremol Device EDI Integration

Depends on: l10n_ke.

## `account.move` (extends)

- `l10n_ke_cu_datetime` Datetime “CU Signing Date and Time”
- `l10n_ke_cu_serial_number` Char “CU Serial Number”
- `l10n_ke_cu_invoice_number` Char “CU Invoice Number”
- `l10n_ke_cu_qrcode` Char “CU QR Code”
- `l10n_ke_cu_show_send_button` Boolean “Show Send to Tremol button” (compute=_compute_l10n_ke_cu_show_send_button)

Public methods: `l10n_ke_action_cu_post`, `l10n_ke_cu_responses`

## `account.move.send` (extends)


Extension points: `_get_alerts`, `_get_l10n_ke_edi_tremol_warning_message`, `_get_l10n_ke_edi_tremol_warning_moves`

## `res.company` (extends)

- `l10n_ke_cu_proxy_address` Char “Fiscal Device Proxy Address”

## `res.config.settings` (extends)

- `l10n_ke_cu_proxy_address` Char (related=company_id.l10n_ke_cu_proxy_address)

## `res.partner` (extends)

- `l10n_ke_exemption_number` Char “Exemption Number”

## `account.move.send.wizard` (extends)


Public methods: `action_send_and_print`
