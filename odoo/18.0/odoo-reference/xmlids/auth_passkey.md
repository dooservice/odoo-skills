# auth_passkey — XML ids

## ir.actions.act_window

- `auth_passkey.action_auth_passkey_key_create`

## ir.rule

- `auth_passkey.rule_auth_passkey_key_user`
- `auth_passkey.rule_auth_passkey_key_admin`

## ir.ui.view

- `auth_passkey.auth_passkey_key_rename` — on auth.passkey.key
- `auth_passkey.auth_passkey_key_create_view_form` — on auth.passkey.key.create
- `auth_passkey.auth_passkey_login` — inherits web.login
- `auth_passkey.res_users_identitycheck_view_form_passkey` — on res.users.identitycheck inherits base.res_users_identitycheck_view_form
- `auth_passkey.auth_passkey_users_form` — on res.users inherits base.view_users_form
- `auth_passkey.auth_passkey_users_preferences` — on res.users inherits base.view_users_form_simple_modif
