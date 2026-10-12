# microsoft_outlook — Microsoft Outlook

Depends on: mail.

## `fetchmail.server` (extends)

Inherits: `microsoft.outlook.mixin`

- `server_type` Selection

Public methods: `onchange_server_type`

Extension points: `_check_use_microsoft_outlook_service`, `_get_connection_type`

## `ir.mail_server` (extends)

Inherits: `microsoft.outlook.mixin`

- `smtp_authentication` Selection

Extension points: `_check_use_microsoft_outlook_service`

## `microsoft.outlook.mixin` (defines)

Microsoft Outlook Mixin

- `is_microsoft_outlook_configured` Boolean “Is Outlook Credential Configured” (compute=_compute_is_microsoft_outlook_configured)
- `microsoft_outlook_refresh_token` Char “Outlook Refresh Token”
- `microsoft_outlook_access_token` Char “Outlook Access Token”
- `microsoft_outlook_access_token_expiration` Integer “Outlook Access Token Expiration Timestamp”
- `microsoft_outlook_uri` Char “Authentication URI” (compute=_compute_outlook_uri)

Public methods: `open_microsoft_outlook_uri`

Extension points: `_get_microsoft_endpoint`, `_get_outlook_csrf_token`

## `res.config.settings` (extends)

- `microsoft_outlook_client_identifier` Char “Outlook Client Id”
- `microsoft_outlook_client_secret` Char “Outlook Client Secret”
