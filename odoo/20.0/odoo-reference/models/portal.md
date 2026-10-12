# portal — Customer Portal

Depends on: auth_signup, base_address_extended, html_editor, http_routing, mail, web.

## `ir.http` (extends)


Public methods: `get_frontend_session_info`

Extension points: `_get_translation_frontend_modules_name`

## `ir.qweb` (extends)


Extension points: `_prepare_environment`

## `ir.ui.view` (extends)

- `customize_show` Boolean “Show As Optional Inherit”

## `mail.message` (extends)


Public methods: `portal_message_format`

## `mail.thread` (extends)


Extension points: `_get_allowed_access_params`, `_get_thread_with_access`

## `portal.entry` (defines)

Portal Entry

- `name` Char “Title of Card” (required)
- `url` Char “Target URL”
- `description` Text “Description of Card”
- `image` Binary “Image”
- `sequence` Integer “sequence”
- `placeholder_count` Char “Placeholder Count”
- `category` Char “Category”
- `show_in_portal` Boolean “Show in Portal”
- `is_config_card` Boolean “Config Card”

## `portal.mixin` (defines)

Portal Mixin

- `access_url` Char “Portal Access URL” (compute=_compute_access_url)
- `access_token` Char “Security Token”
- `access_warning` Text “Access warning” (compute=_compute_access_warning)

Public methods: `action_share`, `get_portal_url`

Extension points: `_get_access_action`, `_get_share_url`

## `res.config.settings` (extends)

- `portal_allow_api_keys` Boolean “Customer API Keys”

## `res.country` (extends)


Extension points: `_get_address_fields`, `_get_address_format_fields_mapping`, `_get_cities_data`, `_get_cities_fields_to_fetch`, `_get_partner_city_field`, `_get_vat_label`

## `res.partner` (extends)


Extension points: `_check_billing_address`, `_check_delivery_address`, `_get_current_partner`, `_get_delivery_address_domain`, `_get_frontend_writable_fields`, `_get_mandatory_address_fields`, `_get_mandatory_billing_address_fields`, `_get_mandatory_delivery_address_fields`, `_get_required_address_fields`

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
