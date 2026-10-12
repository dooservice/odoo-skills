# microsoft_account — Microsoft Users

Depends on: base_setup.

## `microsoft.service` (defines)

Microsoft Service


Public methods: `generate_refresh_token`

Extension points: `_get_auth_endpoint`, `_get_authorize_uri`, `_get_calendar_scope`, `_get_microsoft_client_id`, `_get_microsoft_tokens`, `_get_token_endpoint`

## `res.users` (extends)

- `microsoft_calendar_rtoken` Char “Microsoft Refresh Token”
- `microsoft_calendar_token` Char “Microsoft User token”
- `microsoft_calendar_token_validity` Datetime “Microsoft Token Validity”
