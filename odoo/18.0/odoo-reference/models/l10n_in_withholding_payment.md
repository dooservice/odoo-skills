# l10n_in_withholding_payment — Indian - TDS For Payment

Depends on: l10n_in_withholding.

## `account.move` (extends)

- `l10n_in_withholding_ref_payment_id` Many2one → `account.payment` “Indian TDS Ref Payment” (readonly)

## `account.payment` (extends)

- `l10n_in_withhold_move_ids` One2many → `account.move` “Indian Payment TDS Entries”
- `l10n_in_total_withholding_amount` Monetary (compute=_compute_l10n_in_total_withholding_amount)

## `l10n_in.withhold.wizard` (extends)


Extension points: `_prepare_withhold_header`
