# iap — In-App Purchase

Depends on: web, base_setup.

## `iap.account` (defines)

IAP Account

- `name` Char
- `service_id` Many2one → `iap.service` (required)
- `service_name` Char (related=service_id.technical_name)
- `service_price_description` Char (related=service_id.price_description)
- `service_locked` Boolean
- `description` Char (related=service_id.description)
- `account_token` Char
- `company_ids` Many2many → `res.company`
- `balance_amount` Float
- `balance` Char (compute=_compute_balance)
- `is_balance_below_warning_threshold` Boolean (compute=_compute_is_balance_below_warning_threshold)
- `warning_threshold` Float “Email Alert Threshold”
- `warning_user_ids` Many2many → `res.users` “Email Alert Recipients”
- `state` Selection (readonly)

Public methods: `action_buy_credits`, `action_open_iap_account`, `create`, `get`, `get_account_id`, `get_config_account_url`, `get_credits`, `get_credits_url`, `validate_warning_alerts`, `web_read`, `write`

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
- `price_description` Char
- `pack_ids` One2many → `iap.service.pack` “Service Packs”

## `iap.service.pack` (defines)

IAP Service Pack

- `name` Char (required, readonly)
- `display_name` Char (compute=_compute_display_name)
- `credit` Float (required, readonly)
- `price` Float “Sales Price (EUR)” (required, readonly)
- `service_id` Many2one → `iap.service` (required, readonly, index)
- `iap_service_pack_identifier` Integer (required, readonly)
