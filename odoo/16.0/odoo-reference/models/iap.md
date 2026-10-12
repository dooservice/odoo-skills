# iap — In-App Purchases

Depends on: web, base_setup.

## `iap.account` (defines)

IAP Account

- `service_name` Char
- `account_token` Char
- `company_ids` Many2many → `res.company`

Public methods: `create`, `get`, `get_account_url`, `get_config_account_url`, `get_credits`, `get_credits_url`

## `iap.enrich.api` (defines)

IAP Lead Enrichment API


## `res.config.settings` (extends)
