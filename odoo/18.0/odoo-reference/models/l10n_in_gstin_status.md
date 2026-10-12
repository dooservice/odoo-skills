# l10n_in_gstin_status — Indian - Check GST Number Status

Depends on: l10n_in.

## `account.move` (extends)

- `l10n_in_partner_gstin_status` Boolean “GST Status” (compute=_compute_l10n_in_partner_gstin_status_and_date)
- `l10n_in_show_gstin_status` Boolean (compute=_compute_l10n_in_show_gstin_status)
- `l10n_in_gstin_verified_date` Date (compute=_compute_l10n_in_partner_gstin_status_and_date)

Public methods: `l10n_in_verify_partner_gstin_status`

## `res.partner` (extends)

- `l10n_in_gstin_verified_status` Boolean “GST Status”
- `l10n_in_gstin_verified_date` Date “GSTIN Verified Date”

Public methods: `action_l10n_in_verify_gstin_status`
