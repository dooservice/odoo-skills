# l10n_sa — Saudi Arabia - Accounting

Depends on: l10n_multilang, l10n_gcc_invoice.

## `account.chart.template` (extends)


Extension points: `_prepare_all_journals`

## `account.move` (extends)

- `l10n_sa_delivery_date` Date “Supply Date” (readonly)
- `l10n_sa_show_delivery_date` Boolean (compute=_compute_show_delivery_date)
- `l10n_sa_qr_code_str` Char “Zatka QR Code” (compute=_compute_qr_code_str)
- `l10n_sa_confirmation_datetime` Datetime “Confirmation Date” (readonly)

Public methods: `button_draft`, `get_l10n_sa_confirmation_datetime_sa_tz`

Extension points: `_get_l10n_sa_totals`
