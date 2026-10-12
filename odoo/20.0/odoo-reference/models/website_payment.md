# website_payment — Website Payment

Depends on: website, account_payment, portal.

## `payment.provider` (extends)

- `website_id` Many2one → `website`

Public methods: `copy`, `get_base_url`

## `res.config.settings` (extends)


Public methods: `action_w_payment_start_payment_onboarding`

Extension points: `_get_installed_providers_domain`
