# auth_totp_mail — XML ids

## ir.actions.server

- `auth_totp_mail.action_invite_totp`
- `auth_totp_mail.action_activate_two_factor_authentication`

## ir.ui.view

- `auth_totp_mail.account_security_setting_update` — inherits mail.account_security_setting_update
- `auth_totp_mail.view_users_form` — on res.users inherits auth_totp.view_totp_form
- `auth_totp_mail.res_users_view_form` — on res.users inherits base.view_users_form_simple_modif

## mail.template

- `auth_totp_mail.mail_template_totp_invite`
