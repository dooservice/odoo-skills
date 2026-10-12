# auth_timeout — Auth Timeout

Depends on: auth_totp, auth_totp_mail, auth_passkey, bus.

## `auth_totp.device` (extends)


Extension points: `_get_trusted_device_age`

## `ir.http` (extends)


Public methods: `get_frontend_session_info`, `session_info`

Extension points: `_check_identity`

## `ir.websocket` (extends)


## `res.groups` (extends)

- `lock_timeout` Integer “Session timeout”
- `lock_timeout_mfa` Boolean “Require MFA on session timeout”
- `lock_timeout_inactivity` Integer “Inactivity timeout”
- `lock_timeout_inactivity_mfa` Boolean “Require MFA on inactivity timeout”
- `has_lock_timeout` Boolean (compute=_compute_has_lock_timeout)
- `lock_timeout_delay_unit` Selection (compute=_compute_lock_timeout_delay_unit)
- `lock_timeout_delay_in_unit` Integer (compute=_compute_lock_timeout_delay_unit)
- `lock_timeout_2fa_selection` Selection (compute=_compute_lock_timeout_2fa_selection)
- `has_lock_timeout_inactivity` Boolean (compute=_compute_lock_timeout_inactivity_bool)
- `lock_timeout_inactivity_delay_unit` Selection (compute=_compute_lock_timeout_inactivity_delay_unit)
- `lock_timeout_inactivity_delay_in_unit` Integer (compute=_compute_lock_timeout_inactivity_delay_unit)
- `lock_timeout_inactivity_2fa_selection` Selection (compute=_compute_lock_timeout_inactivity_2fa_selection)

Public methods: `create`, `unlink`, `write`

Extension points: `_get_lock_timeouts`

## `res.users` (extends)


Extension points: `_get_auth_methods`, `_get_lock_timeout_inactivity`, `_get_lock_timeouts`
