# website_payment — Website Payment

Depends on: website, account_payment, portal.

## `account.payment` (extends)

- `is_donation` Boolean “Is Donation” (related=payment_transaction_id.is_donation)

## `payment.provider` (extends)

- `website_id` Many2one → `website`

Public methods: `copy`, `get_base_url`

Extension points: `_get_compatible_providers`

## `payment.transaction` (extends)

- `is_donation` Boolean “Is donation”

Extension points: `_post_process`

## `res.config.settings` (extends)

- `providers_state` Selection (compute=_compute_providers_state)
- `first_provider_label` Char (compute=_compute_providers_state)
- `is_stripe_supported_country` Boolean (related=company_id.country_id.is_stripe_supported_country)

Public methods: `action_activate_stripe`, `action_configure_first_provider`

Extension points: `_get_activated_providers`
