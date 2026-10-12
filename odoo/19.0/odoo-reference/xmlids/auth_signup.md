# auth_signup — XML ids

## ir.actions.server

- `auth_signup.action_send_password_reset_instructions`

## ir.cron

- `auth_signup.ir_cron_auth_signup_send_pending_user_reminder`

## ir.ui.view

- `auth_signup.res_config_settings_view_form` — on res.config.settings inherits base_setup.res_config_settings_view_form
- `auth_signup.res_users_view_form` — on res.users inherits base.view_users_form
- `auth_signup.view_users_state_tree` — on res.users inherits base.view_users_tree
- `auth_signup.login` — inherits web.login
- `auth_signup.fields`
- `auth_signup.signup`
- `auth_signup.reset_password`
- `auth_signup.reset_password_email`
- `auth_signup.login_successful` — inherits web.login_successful

## mail.template

- `auth_signup.set_password_email`
- `auth_signup.mail_template_data_unregistered_users`
- `auth_signup.mail_template_user_signup_account_created`
- `auth_signup.portal_set_password_email`
