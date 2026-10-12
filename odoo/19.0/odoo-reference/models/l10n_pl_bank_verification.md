# l10n_pl_bank_verification — Poland - Accounting - Bank Account Verification

Depends on: l10n_pl.

## `account.payment` (extends)

- `l10n_pl_verification_id` Many2one → `l10n_pl.bank.account.verification` “PL Bank Verification” (readonly, store, compute=_compute_l10n_pl_verification_id)
- `l10n_pl_verification_status` Selection (related=l10n_pl_verification_id.verification_status)
- `l10n_pl_verification_timestamp` Datetime (related=l10n_pl_verification_id.verification_timestamp)
- `l10n_pl_verification_request_id` Char (related=l10n_pl_verification_id.verification_request_id)

## `l10n_pl.bank.account.verification` (defines)

PL Bank Account Verification

- `verification_status` Selection “Verification Status” (required, readonly)
- `verification_timestamp` Datetime “Verification Timestamp” (readonly)
- `verification_date` Date (store, compute=_compute_verification_date)
- `verification_request_id` Char “Correlation ID” (readonly)
- `partner_bank_id` Many2one → `res.partner.bank` “Bank Account” (readonly)
- `partner_bank_account_number` Char (readonly, store, compute=_compute_partner_bank_account_number)
- `partner_id` Many2one → `res.partner` “Partner” (readonly)
- `partner_vat` Char (readonly, store, compute=_compute_partner_vat)

Extension points: `_get_creation_vals`, `_get_partner_from_identifier`

## `account.payment.register` (extends)

- `l10n_pl_bank_verification_ids` Many2many → `l10n_pl.bank.account.verification` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_bank_verification_invalid_bank_account_ids` Many2many → `res.partner.bank` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_not_found_partner_ids` Many2many → `res.partner` (compute=_compute_l10n_pl_bank_verification)
- `l10n_pl_incomplete_data_partner_ids` Many2many → `res.partner` (compute=_compute_l10n_pl_bank_verification)

Extension points: `_create_payment_vals_from_batch`, `_create_payment_vals_from_wizard`, `_get_partner_bank_from_batch`
