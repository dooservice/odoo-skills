# auth_signup — Signup

Depends on: base_setup, mail, web.

## `ir.http` (extends)


## `res.config.settings` (extends)

- `auth_signup_reset_password` Boolean “Enable password reset from Login page”
- `auth_signup_uninvited` Selection “Customer Account”
- `auth_signup_template_user_id` Many2one → `res.users` “Template user for new users created through signup”

## `res.partner` (extends)

- `signup_type` Char “Signup Token Type”

Public methods: `action_signup_prepare`, `signup_cancel`, `signup_get_auth_param`, `signup_prepare`

Extension points: `_get_login_date`, `_get_partner_from_token`, `_get_signup_url`, `_get_signup_url_for_action`

## `res.users` (extends)

- `state` Selection “Status” (compute=_compute_state)

Public methods: `action_reset_password`, `copy`, `create`, `get_reset_password_link`, `reset_password`, `send_unregistered_user_reminder`, `signup`, `web_create_users`, `write`

Extension points: `_action_reset_password`, `_create_user_from_template`, `_get_signup_invitation_scope`
