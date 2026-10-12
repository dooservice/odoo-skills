# iap — In-App Purchases

Depends on: web, base_setup.

## `iap.account` (defines)

IAP Account

- `name` Char
- `service_name` Char (readonly)
- `account_token` Char
- `company_ids` Many2many → `res.company`
- `account_info_id` Many2one → `iap.account.info` (compute=_compute_info)
- `account_info_ids` One2many → `iap.account.info` “Accounts from IAP”
- `balance` Char (compute=_compute_balance)
- `description` Char (related=account_info_id.description)
- `warn_me` Boolean (related=account_info_id.warn_me)
- `warning_threshold` Float (related=account_info_id.warning_threshold)
- `warning_email` Char (related=account_info_id.warning_email)
- `show_token` Boolean

Public methods: `action_buy_credits`, `action_toggle_show_token`, `create`, `get`, `get_config_account_url`, `get_credits`, `get_credits_url`, `get_services`, `get_view`, `write`

## `iap.account.info` (defines)

IAP Account Info

- `account_id` Many2one → `iap.account` “IAP Account”
- `account_token` Char
- `balance` Float “Balance”
- `account_uuid_hashed` Char “Account UUID”
- `service_name` Char “Related Service”
- `description` Char
- `warn_me` Boolean “Warn me”
- `warning_threshold` Float “Threshold”
- `warning_email` Char
- `unit_name` Char

## `iap.enrich.api` (defines)

IAP Lead Enrichment API
