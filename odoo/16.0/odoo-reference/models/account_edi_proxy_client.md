# account_edi_proxy_client — Proxy features for account_edi

Depends on: account_edi.

## `account.edi.format` (extends)


Extension points: `_get_proxy_identification`, `_get_proxy_user`

## `account_edi_proxy_client.user` (defines)

Account EDI proxy user

- `active` Boolean
- `id_client` Char (required)
- `company_id` Many2one → `res.company` “Company” (required)
- `edi_format_id` Many2one → `account.edi.format` (required)
- `edi_format_code` Char (readonly, related=edi_format_id.code)
- `edi_identification` Char (required)
- `private_key` Binary (required)
- `private_key_filename` Char (compute=_compute_private_key_filename)
- `refresh_token` Char

Extension points: `_get_create_user_edi_params`, `_get_demo_state`, `_get_route`, `_get_server_url`, `_get_server_url_new`

## `res.company` (extends)

- `account_edi_proxy_client_ids` One2many → `account_edi_proxy_client.user`
