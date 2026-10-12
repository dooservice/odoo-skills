# auth_totp — Two-Factor Authentication (TOTP)

Depends on: web.

## `auth_totp.device` (defines)

Authentication Device

Inherits: `res.users.apikeys`


Extension points: `_check_credentials_for_uid`, `_get_trusted_device_age`

## `auth.totp.rate.limit.log` (defines)

TOTP rate limit logs

- `user_id` Many2one → `res.users` (required, readonly)
- `ip` Char (readonly)
- `limit_type` Selection (readonly)

## `res.users` (extends)

- `totp_secret` Char (compute=_compute_totp_secret)
- `totp_last_counter` Integer
- `totp_enabled` Boolean “Two-factor authentication” (compute=_compute_totp_enabled)
- `totp_trusted_device_ids` One2many → `auth_totp.device` “Trusted Devices”

Public methods: `SELF_READABLE_FIELDS`, `action_totp_disable`, `action_totp_enable_wizard`, `change_password`, `init`, `revoke_all_devices`

Extension points: `_check_credentials`, `_get_session_token_fields`

## `auth_totp.wizard` (defines)

2-Factor Setup Wizard

- `user_id` Many2one → `res.users` (required, readonly)
- `secret` Char (required, readonly)
- `url` Char (readonly, store, compute=_compute_qrcode)
- `qrcode` Binary (readonly, store, compute=_compute_qrcode)
- `code` Char “Verification Code”

Public methods: `enable`
