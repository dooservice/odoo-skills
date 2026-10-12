# auth_totp_mail — 2FA Invite mail

Depends on: auth_totp, mail.

## `auth_totp.device` (extends)


Public methods: `unlink`

## `ir.http` (extends)


Extension points: `_check_identity`

## `res.config.settings` (extends)

- `auth_totp_enforce` Boolean “Enforce two-factor authentication”
- `auth_totp_policy` Selection “Two-factor authentication enforcing policy”

Public methods: `get_values`

## `res.users` (extends)


Public methods: `action_open_my_account_settings`, `action_totp_invite`, `authenticate`, `get_totp_invite_url`, `write`

Extension points: `_check_credentials`, `_get_totp_mail_code`, `_get_totp_mail_key`
