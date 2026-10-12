# account_update_tax_tags — Account - Allow updating tax grids

Depends on: account.

## `account.update.tax.tags.wizard` (defines)

Update Tax Tags Wizard

- `company_id` Many2one → `res.company` (required, readonly)
- `date_from` Date “Starting from” (required, store, compute=_compute_date_from)
- `display_lock_date_warning` Boolean (compute=_compute_display_lock_date_warning)

Public methods: `update_amls_tax_tags`
