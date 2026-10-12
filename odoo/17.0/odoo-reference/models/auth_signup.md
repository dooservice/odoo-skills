# auth_signup — Signup

Depends on: base_setup, mail, web.

## `ir.http` (extends)


## `res.config.settings` (extends)

- `auth_signup_reset_password` Boolean “Enable password reset from Login page”
- `auth_signup_uninvited` Selection “Customer Account”
- `auth_signup_template_user_id` Many2one → `res.users` “Template user for new users created through signup”

## `res.partner` (extends)

- `signup_token` Char (compute=_compute_token)
- `signup_type` Char “Signup Token Type”
- `signup_expiration` Datetime
- `signup_valid` Boolean “Signup Token is Valid” (compute=_compute_signup_valid)
- `signup_url` Char “Signup URL” (compute=_compute_signup_url)

Public methods: `action_signup_prepare`, `init`, `signup_cancel`, `signup_get_auth_param`, `signup_prepare`, `signup_retrieve_info`

Extension points: `_get_signup_url_for_action`

## `res.users` (extends)

- `state` Selection “Status” (compute=_compute_state)

Public methods: `action_reset_password`, `authenticate`, `copy`, `create`, `reset_password`, `send_unregistered_user_reminder`, `signup`, `web_create_users`, `write`

Extension points: `_action_reset_password`, `_create_user_from_template`, `_get_signup_invitation_scope`, `_prepare_new_device_notice_values`
