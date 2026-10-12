# auth_oauth — OAuth2 Authentication

Depends on: base, web, base_setup, auth_signup.

## `auth.oauth.provider` (defines)

OAuth2 provider

- `name` Char “Provider name” (required)
- `client_id` Char “Client ID”
- `auth_endpoint` Char “Authorization URL” (required)
- `scope` Char
- `validation_endpoint` Char “UserInfo URL” (required)
- `data_endpoint` Char
- `enabled` Boolean “Allowed”
- `css_class` Char “CSS class”
- `body` Char “Login button label” (required)
- `sequence` Integer

## `ir.config_parameter` (extends)


Public methods: `init`

## `res.config.settings` (extends)

- `auth_oauth_google_enabled` Boolean “Allow users to sign in with Google”
- `auth_oauth_google_client_id` Char “Client ID”
- `server_uri_google` Char “Server uri”

Public methods: `get_uri`, `get_values`, `set_values`

## `res.users` (extends)

- `oauth_provider_id` Many2one → `auth.oauth.provider` “OAuth Provider”
- `oauth_uid` Char “OAuth User ID”
- `oauth_access_token` Char “OAuth Access Token” (readonly)

Public methods: `USER_PRIVATE_FIELDS`, `auth_oauth`

Extension points: `_check_credentials`, `_get_session_token_fields`
