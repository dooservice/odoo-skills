# l10n_sa — Saudi Arabia - Accounting

Depends on: l10n_gcc_invoice, account.

## `account.move` (extends)

- `l10n_sa_qr_code_str` Char “Zatka QR Code” (compute=_compute_qr_code_str)
- `l10n_sa_confirmation_datetime` Datetime “ZATCA Issue Date” (readonly)

Public methods: `get_l10n_sa_confirmation_datetime_sa_tz`, `write`

Extension points: `_get_iso_format_asia_riyadh_date`, `_get_l10n_sa_totals`, `_get_normalized_l10n_sa_confirmation_datetime`

## `ir.attachment` (extends)


Extension points: `_get_posted_pdf_moves_to_check`

## `account.chart.template` (extends)


Extension points: `_get_sa_account_account`, `_get_sa_account_journal`, `_get_sa_res_company`, `_get_sa_template_data`
