# auth_totp_mail_enforce — 2FA by mail

Depends on: auth_totp, mail.

## `auth.totp.rate.limit.log` (defines)

TOTP rate limit logs

- `user_id` Many2one → `res.users` (required, readonly)
- `scope` Char (readonly)
- `ip` Char (readonly)
- `limit_type` Selection (readonly)

Public methods: `init`

## `res.config.settings` (extends)

- `auth_totp_enforce` Boolean “Enforce two-factor authentication”
- `auth_totp_policy` Selection “Two-factor authentication enforcing policy”

Public methods: `get_values`

## `res.users` (extends)


Extension points: `_get_totp_mail_code`, `_get_totp_mail_key`
