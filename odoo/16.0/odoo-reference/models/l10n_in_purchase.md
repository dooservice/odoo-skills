# l10n_in_purchase — Indian - Purchase Report(GST)

Depends on: l10n_in, purchase.

## `account.move` (extends)


## `purchase.order` (extends)

- `l10n_in_journal_id` Many2one → `account.journal` “Journal”
- `l10n_in_gst_treatment` Selection “GST Treatment” (store, compute=_compute_l10n_in_gst_treatment)

Public methods: `l10n_in_onchange_company_id`

Extension points: `_prepare_invoice`
