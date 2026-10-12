# portal — Customer Portal

Depends on: web, web_editor, http_routing, mail, auth_signup.

## `ir.http` (extends)


Extension points: `_get_frontend_langs`, `_get_translation_frontend_modules_name`

## `ir.qweb` (extends)


Extension points: `_prepare_frontend_environment`

## `ir.ui.view` (extends)

- `customize_show` Boolean “Show As Optional Inherit”

## `mail.message` (extends)


Public methods: `portal_message_format`

## `mail.thread` (extends)

- `website_message_ids` One2many → `mail.message` “Website Messages”

## `portal.mixin` (defines)

Portal Mixin

- `access_url` Char “Portal Access URL” (compute=_compute_access_url)
- `access_token` Char “Security Token”
- `access_warning` Text “Access warning” (compute=_compute_access_warning)

Public methods: `action_share`, `get_portal_url`

Extension points: `_get_access_action`, `_get_share_url`

## `res.config.settings` (extends)

- `portal_allow_api_keys` Boolean “Customer API Keys” (compute=_compute_portal_allow_api_keys)

Public methods: `get_values`

## `res.partner` (extends)


Public methods: `can_edit_vat`

## `res.users.apikeys.description` (extends)


Public methods: `check_access_make_key`

## `portal.share` (defines)

Portal Sharing

- `res_model` Char “Related Document Model” (required)
- `res_id` Integer “Related Document ID” (required)
- `resource_ref` Reference “_selection_target_model” (compute=_compute_resource_ref)
- `partner_ids` Many2many → `res.partner` “Recipients” (required)
- `note` Text
- `share_link` Char “Link” (compute=_compute_share_link)
- `access_warning` Text “Access warning” (compute=_compute_access_warning)

Public methods: `action_send_mail`, `default_get`

## `portal.wizard` (defines)

Grant Portal Access

- `partner_ids` Many2many → `res.partner` “Partners”
- `user_ids` One2many → `portal.wizard.user` “Users” (store, compute=_compute_user_ids)
- `welcome_message` Text “Invitation Message”

Public methods: `action_open_wizard`

Extension points: `_action_open_modal`

## `portal.wizard.user` (defines)

Portal User Config

- `wizard_id` Many2one → `portal.wizard` “Wizard” (required)
- `partner_id` Many2one → `res.partner` “Contact” (required, readonly)
- `email` Char “Email”
- `user_id` Many2one → `res.users` “User” (compute=_compute_user_id)
- `login_date` Datetime “Latest Authentication” (related=user_id.login_date)
- `is_portal` Boolean “Is Portal” (compute=_compute_group_details)
- `is_internal` Boolean “Is Internal” (compute=_compute_group_details)
- `email_state` Selection “Status” (compute=_compute_email_state)

Public methods: `action_grant_access`, `action_invite_again`, `action_refresh_modal`, `action_revoke_access`

Extension points: `_create_user`, `_get_similar_users_domain`, `_get_similar_users_fields`
