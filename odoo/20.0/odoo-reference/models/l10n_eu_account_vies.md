# l10n_eu_account_vies — VAT VIES Validation

Depends on: account.

## `res.country` (extends)

- `has_foreign_fiscal_position` Boolean (compute=_compute_has_foreign_fiscal_position)

## `res.partner` (extends)

- `vies_valid` Boolean “Intra-Community Valid” (store, compute=_compute_vies_valid)
- `perform_vies_validation` Boolean (compute=_compute_perform_vies_validation)

Public methods: `create`, `write`

Extension points: `_check_vies_update_iap`, `_check_vies_validity_iap`, `_create_contact_parent_company`, `_get_iap_vies_credentials`, `_get_iap_vies_endpoint`, `_get_vat_required_valid`
