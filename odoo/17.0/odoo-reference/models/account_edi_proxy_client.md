# account_edi_proxy_client — Proxy features for account_edi

Depends on: account.

## `account_edi_proxy_client.user` (defines)

Account EDI proxy user

- `active` Boolean
- `id_client` Char (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `edi_identification` Char (required)
- `private_key` Binary (required)
- `private_key_filename` Char (compute=_compute_private_key_filename)
- `refresh_token` Char
- `proxy_type` Selection (required)
- `edi_mode` Selection “EDI operating mode”

Extension points: `_get_proxy_identification`, `_get_proxy_urls`, `_get_proxy_users`, `_get_server_url`

## `res.company` (extends)

- `account_edi_proxy_client_ids` One2many → `account_edi_proxy_client.user`
