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


Public methods: `action_w_payment_start_payment_onboarding`

Extension points: `_get_active_providers_domain`
