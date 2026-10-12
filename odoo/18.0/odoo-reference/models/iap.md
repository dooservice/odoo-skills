# iap — In-App Purchases

Depends on: web, base_setup.

## `iap.account` (defines)

IAP Account

- `name` Char
- `service_id` Many2one → `iap.service` (required)
- `service_name` Char (related=service_id.technical_name)
- `service_locked` Boolean
- `description` Char (related=service_id.description)
- `account_token` Char
- `company_ids` Many2many → `res.company`
- `balance` Char (readonly)
- `warning_threshold` Float “Email Alert Threshold”
- `warning_user_ids` Many2many → `res.users` “Email Alert Recipients”
- `state` Selection (readonly)

Public methods: `action_buy_credits`, `create`, `get`, `get_account_id`, `get_config_account_url`, `get_credits`, `get_credits_url`, `is_running_test_suite`, `validate_warning_alerts`, `web_read`, `write`

Extension points: `_get_account_info`, `_get_account_information_from_iap`

## `iap.enrich.api` (defines)

IAP Lead Enrichment API


## `iap.service` (defines)

IAP Service

- `name` Char (required)
- `technical_name` Char (required, readonly)
- `description` Char (required)
- `unit_name` Char (required)
- `integer_balance` Boolean (required)
