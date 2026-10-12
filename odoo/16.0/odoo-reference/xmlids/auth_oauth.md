# auth_oauth — XML ids

## auth.oauth.provider

- `auth_oauth.provider_openerp`
- `auth_oauth.provider_facebook`
- `auth_oauth.provider_google`

## ir.actions.act_window

- `auth_oauth.action_oauth_provider`

## ir.ui.menu

- `auth_oauth.menu_oauth_providers` — OAuth Providers

## ir.ui.view

- `auth_oauth.view_oauth_provider_form` — on auth.oauth.provider
- `auth_oauth.view_oauth_provider_tree` — on auth.oauth.provider
- `auth_oauth.view_users_form` — on res.users inherits base.view_users_form
- `auth_oauth.res_config_settings_view_form` — on res.config.settings inherits base_setup.res_config_settings_view_form
- `auth_oauth.providers`
- `auth_oauth.login` — inherits web.login
- `auth_oauth.signup` — inherits auth_signup.signup
- `auth_oauth.reset_password` — inherits auth_signup.reset_password
