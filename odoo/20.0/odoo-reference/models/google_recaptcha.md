# google_recaptcha — Google reCAPTCHA integration

Depends on: base_setup.

## `ir.http` (extends)


Public methods: `get_frontend_session_info`, `session_info`

## `res.config.settings` (extends)

- `enable_recaptcha` Boolean “Enable reCAPTCHA”
- `recaptcha_public_key` Char “Site Key”
- `recaptcha_private_key` Char “Secret Key”
- `recaptcha_min_score` Float “Minimum score”
