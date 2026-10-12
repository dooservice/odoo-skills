# google_gmail — Google Gmail

Depends on: mail.

## `fetchmail.server` (extends)

Inherits: `google.gmail.mixin`

- `server_type` Selection

Public methods: `onchange_server_type`

Extension points: `_check_use_google_gmail_service`, `_get_connection_type`

## `google.gmail.mixin` (defines)

Google Gmail Mixin

- `active` Boolean
- `google_gmail_refresh_token` Char “Refresh Token”
- `google_gmail_access_token` Char “Access Token”
- `google_gmail_access_token_expiration` Integer “Access Token Expiration Timestamp”
- `google_gmail_uri` Char “URI” (compute=_compute_gmail_uri)

Public methods: `open_google_gmail_uri`

Extension points: `_get_gmail_csrf_token`

## `ir.mail_server` (extends)

Inherits: `google.gmail.mixin`

- `smtp_authentication` Selection

Extension points: `_check_use_google_gmail_service`

## `res.config.settings` (extends)

- `google_gmail_client_identifier` Char “Gmail Client Id”
- `google_gmail_client_secret` Char “Gmail Client Secret”

## `res.users` (extends)

- `outgoing_mail_server_type` Selection

Extension points: `_get_mail_server_setup_end_action`, `_get_mail_server_values`
