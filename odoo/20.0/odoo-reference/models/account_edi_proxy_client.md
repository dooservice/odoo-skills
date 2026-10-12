# account_edi_proxy_client — Proxy features for account_edi

Depends on: account, certificate.

## `account_edi_proxy_client.user` (defines)

Account EDI proxy user

- `active` Boolean
- `id_client` Char (required)
- `company_id` Many2one → `res.company` “Company” (required, index)
- `edi_identification` Char (required)
- `private_key_id` Many2one → `certificate.key` “Private Key” (required)
- `refresh_token` Char
- `is_token_out_of_sync` Boolean “Token Out of Sync”
- `token_sync_version` Integer “Token Sync Version”
- `proxy_type` Selection (required)
- `edi_mode` Selection “EDI operating mode”

Extension points: `_get_iap_params`, `_get_proxy_identification`, `_get_proxy_urls`, `_get_proxy_users`, `_get_server_url`

## `res.company` (extends)

- `account_edi_proxy_client_ids` One2many → `account_edi_proxy_client.user`
