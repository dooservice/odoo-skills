# auth_passkey — Passkeys

Depends on: base_setup, web.

## `auth.passkey.key` (defines)

Passkey

- `name` Char (required)
- `credential_identifier` Char (required)
- `public_key` Char (required, compute=_compute_public_key)
- `sign_count` Integer

Public methods: `action_delete_passkey`, `action_rename_passkey`, `init`, `unlink`

Extension points: `_get_session_challenge`

## `auth.passkey.key.create` (defines)

Create a Passkey

- `name` Char “Name” (required)

Public methods: `make_key`

## `res.users` (extends)

- `auth_passkey_key_ids` One2many → `auth.passkey.key`

Public methods: `SELF_READABLE_FIELDS`, `action_create_passkey`

Extension points: `_check_credentials`, `_get_session_token_fields`, `_get_session_token_query_params`

## `res.users.identitycheck` (extends)

- `auth_method` Selection

Public methods: `action_use_password`

Extension points: `_check_identity`, `_get_default_auth_method`
