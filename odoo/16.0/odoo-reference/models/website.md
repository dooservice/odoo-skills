# website — Website

Depends on: digest, web, web_editor, http_routing, portal, social_media, auth_signup, mail, google_recaptcha, utm.

## `web_editor.assets` (extends)


Public methods: `make_scss_customization`

Extension points: `_get_custom_asset`, `_get_custom_attachment`

## `base.partner.merge.automatic.wizard` (extends)


## `ir.actions.server` (extends)

- `xml_id` Char “External ID” (compute=_compute_xml_id)
- `website_path` Char “Website Path”
- `website_url` Char “Website Url” (compute=_get_website_url)
- `website_published` Boolean “Available on the Website”

Extension points: `_get_eval_context`, `_get_website_url`

## `ir.asset` (extends)

- `key` Char
- `website_id` Many2one → `website`

Public methods: `filter_duplicate`, `write`

Extension points: `_get_active_addons_list`, `_get_related_assets`

## `ir.attachment` (extends)

- `key` Char
- `website_id` Many2one → `website`

Public methods: `create`, `get_serving_groups`

Extension points: `_get_serve_attachment`

## `ir.binary` (extends)


## `ir.http` (extends)


Public methods: `clear_caches`, `get_frontend_session_info`, `routing_map`

Extension points: `_get_converters`, `_get_default_lang`, `_get_error_html`, `_get_exception_code_values`, `_get_frontend_langs`, `_get_public_users`, `_get_translation_frontend_modules_name`, `_get_values_500_error`, `_get_web_editor_context`

## `base` (extends)


Public methods: `get_base_url`, `get_website_meta`

Extension points: `_get_base_lang`

## `ir.model.data` (extends)


## `ir.module.module` (defines)

Module

- `image_ids` One2many → `ir.attachment` “Screenshots” (readonly)
- `is_installed_on_current_website` Boolean (compute=_compute_is_installed_on_current_website)

Public methods: `button_choose_theme`, `button_refresh_theme`, `button_remove_theme`, `get_themes_domain`, `update_list`, `update_theme_images`, `write`

Extension points: `_get_module_data`, `_post_copy`

## `ir.qweb` (extends)


Extension points: `_get_asset_bundle`, `_get_asset_nodes`, `_get_template_cache_keys`, `_post_processing_att`, `_prepare_frontend_environment`

## `ir.qweb.field.contact` (extends)


Public methods: `get_available_options`

## `ir.qweb.field.html` (extends)


Public methods: `value_to_html`

## `ir.rule` (extends)


## `ir.ui.menu` (extends)


Public methods: `load_menus_root`

## `ir.ui.view` (extends)

Inherits: `website.seo.metadata`

- `website_id` Many2one → `website` “Website”
- `page_ids` One2many → `website.page`
- `first_page_id` Many2one → `website.page` “Website Page” (compute=_compute_first_page_id)
- `track` Boolean “Track”
- `visibility` Selection
- `visibility_password` Char
- `visibility_password_display` Char (compute=_get_pwd)

Public methods: `create`, `filter_duplicate`, `get_default_lang_code`, `get_related_views`, `name_get`, `save`, `unlink`, `write`

Extension points: `_create_all_specific_views`, `_create_website_specific_pages_for_view`, `_get_allowed_root_attrs`, `_get_base_lang`, `_get_cached_visibility`, `_get_combined_arch`, `_get_filter_xmlid_query`, `_get_inheriting_views`, `_get_inheriting_views_domain`, `_get_pwd`, `_get_top_level_view`, `_get_view_id`

## `website.seo.metadata` (defines)

SEO metadata

- `is_seo_optimized` Boolean “SEO optimized” (compute=_compute_is_seo_optimized)
- `website_meta_title` Char “Website meta title”
- `website_meta_description` Text “Website meta description”
- `website_meta_keywords` Char “Website meta keywords”
- `website_meta_og_img` Char “Website opengraph image”
- `seo_name` Char “Seo name”

Public methods: `get_website_meta`

## `website.cover_properties.mixin` (defines)

Cover Properties Website Mixin

- `cover_properties` Text “Cover Properties”

Public methods: `write`

Extension points: `_get_background`

## `website.multi.mixin` (defines)

Multi Website Mixin

- `website_id` Many2one → `website` “Website” (index)

Public methods: `can_access_from_current_website`

## `website.published.mixin` (defines)

Website Published Mixin

- `website_published` Boolean “Visible on current website” (related=is_published)
- `is_published` Boolean “Is Published” (index)
- `can_publish` Boolean “Can Publish” (compute=_compute_can_publish)
- `website_url` Char “Website URL” (compute=_compute_website_url)

Public methods: `create`, `create_and_get_website_url`, `open_website_url`, `website_publish_button`, `write`

Extension points: `_get_can_publish_error_message`

## `website.published.multi.mixin` (defines)

Multi Website Published Mixin

Inherits: `website.published.mixin`, `website.multi.mixin`

- `website_published` Boolean (compute=_compute_website_published)

Public methods: `open_website_url`

## `website.searchable.mixin` (defines)

Website Searchable Mixin


## `res.company` (extends)

- `website_id` Many2one → `website` (store, compute=_compute_website_id)

Public methods: `action_open_website_theme_selector`, `google_map_img`, `google_map_link`

Extension points: `_check_active`, `_get_public_user`

## `res.config.settings` (extends)

- `website_id` Many2one → `website` “website”
- `website_name` Char “Website Name” (related=website_id.name)
- `website_domain` Char “Website Domain” (related=website_id.domain)
- `website_homepage_url` Char (related=website_id.homepage_url)
- `website_company_id` Many2one “Website Company” (related=website_id.company_id)
- `website_logo` Binary (related=website_id.logo)
- `language_ids` Many2many (related=website_id.language_ids)
- `website_language_count` Integer “Number of languages” (readonly, related=website_id.language_count)
- `website_default_lang_id` Many2one “Default language” (related=website_id.default_lang_id)
- `website_default_lang_code` Char “Default language code” (related=website_id.default_lang_id.code)
- `shared_user_account` Boolean “Shared Customer Accounts” (compute=_compute_shared_user_account)
- `website_cookies_bar` Boolean (related=website_id.cookies_bar)
- `google_analytics_key` Char “Google Analytics Key” (related=website_id.google_analytics_key)
- `google_search_console` Char “Google Search Console” (related=website_id.google_search_console)
- `plausible_shared_key` Char “Plausible auth Key” (related=website_id.plausible_shared_key)
- `plausible_site` Char “Plausible Site (e.g. domain.com)” (related=website_id.plausible_site)
- `cdn_activated` Boolean (related=website_id.cdn_activated)
- `cdn_url` Char (related=website_id.cdn_url)
- `cdn_filters` Text (related=website_id.cdn_filters)
- `auth_signup_uninvited` Selection (compute=_compute_auth_signup_uninvited)
- `favicon` Binary “Favicon” (related=website_id.favicon)
- `social_default_image` Binary “Default Social Share Image” (related=website_id.social_default_image)
- `group_multi_website` Boolean “Multi-website”
- `has_google_analytics` Boolean “Google Analytics” (compute=_compute_has_google_analytics)
- `has_google_search_console` Boolean “Console Google Search” (compute=_compute_has_google_search_console)
- `has_default_share_image` Boolean “Use a image by default for sharing” (compute=_compute_has_default_share_image)
- `has_plausible_shared_key` Boolean “Plausible Analytics” (compute=_compute_has_plausible_shared_key)
- `module_website_livechat` Boolean
- `module_marketing_automation` Boolean

Public methods: `action_open_robots`, `action_ping_sitemap`, `action_website_create_new`

## `res.lang` (extends)


Public methods: `action_activate_langs`, `get_available`, `write`

## `res.partner` (extends)

Inherits: `website.published.multi.mixin`

- `visitor_ids` One2many → `website.visitor` “Visitors”

Public methods: `google_map_img`, `google_map_link`

Extension points: `_get_name`

## `res.users` (extends)

- `website_id` Many2one → `website` (store, related=partner_id.website_id)

Public methods: `authenticate`

Extension points: `_check_login`, `_get_email_domain`, `_get_login_domain`, `_get_login_order`, `_get_signup_invitation_scope`

## `theme.ir.asset` (defines)

Theme Asset

- `key` Char
- `name` Char (required)
- `bundle` Char (required)
- `directive` Selection
- `path` Char (required)
- `target` Char
- `active` Boolean
- `sequence` Integer (required)
- `copy_ids` One2many → `ir.asset` (readonly)

## `theme.ir.ui.view` (defines)

Theme UI View

- `name` Char (required)
- `key` Char
- `type` Char
- `priority` Integer (required)
- `mode` Selection
- `active` Boolean
- `arch` Text
- `arch_fs` Char
- `inherit_id` Reference
- `copy_ids` One2many → `ir.ui.view` (readonly)
- `customize_show` Boolean

Public methods: `compute_arch_fs`

## `theme.ir.attachment` (defines)

Theme Attachments

- `name` Char (required)
- `key` Char (required)
- `url` Char
- `copy_ids` One2many → `ir.attachment` (readonly)

## `theme.website.menu` (defines)

Website Theme Menu

- `name` Char (required)
- `url` Char
- `page_id` Many2one → `theme.website.page`
- `new_window` Boolean “New Window”
- `sequence` Integer
- `parent_id` Many2one → `theme.website.menu` (index)
- `mega_menu_content` Html
- `mega_menu_classes` Char
- `use_main_menu_as_parent` Boolean
- `copy_ids` One2many → `website.menu` (readonly)

## `theme.website.page` (defines)

Website Theme Page

- `url` Char
- `view_id` Many2one → `theme.ir.ui.view` (required)
- `website_indexed` Boolean “Page Indexed”
- `is_published` Boolean
- `header_overlay` Boolean
- `header_color` Char
- `header_visible` Boolean
- `footer_visible` Boolean
- `copy_ids` One2many → `website.page` (readonly)

## `theme.utils` (defines)

Theme Utils


Public methods: `disable_asset`, `disable_view`, `enable_asset`, `enable_header_off_canvas`, `enable_view`

Extension points: `_post_copy`

## `ir.ui.view` (extends)

- `theme_template_id` Many2one → `theme.ir.ui.view`

Public methods: `write`

## `ir.asset` (extends)

- `theme_template_id` Many2one → `theme.ir.asset`

## `ir.attachment` (extends)

- `key` Char
- `theme_template_id` Many2one → `theme.ir.attachment`

## `website.menu` (extends)

- `theme_template_id` Many2one → `theme.website.menu`

## `website.page` (extends)

- `theme_template_id` Many2one → `theme.website.page`

## `website` (defines)

Website

- `name` Char “Website Name” (required)
- `sequence` Integer
- `domain` Char “Website Domain”
- `company_id` Many2one → `res.company` “Company” (required)
- `language_ids` Many2many → `res.lang` “Languages” (required)
- `language_count` Integer “Number of languages” (compute=_compute_language_count)
- `default_lang_id` Many2one → `res.lang` “Default Language” (required)
- `auto_redirect_lang` Boolean “Autoredirect Language”
- `cookies_bar` Boolean “Cookies Bar”
- `configurator_done` Boolean
- `logo` Binary “Website Logo”
- `social_twitter` Char “Twitter Account”
- `social_facebook` Char “Facebook Account”
- `social_github` Char “GitHub Account”
- `social_linkedin` Char “LinkedIn Account”
- `social_youtube` Char “Youtube Account”
- `social_instagram` Char “Instagram Account”
- `social_default_image` Binary “Default Social Share Image”
- `has_social_default_image` Boolean (store, compute=_compute_has_social_default_image)
- `google_analytics_key` Char “Google Analytics Key”
- `google_search_console` Char
- `google_maps_api_key` Char “Google Maps API Key”
- `plausible_shared_key` Char
- `plausible_site` Char
- `user_id` Many2one → `res.users` “Public User” (required)
- `cdn_activated` Boolean “Content Delivery Network (CDN)”
- `cdn_url` Char “CDN Base URL”
- `cdn_filters` Text “CDN Filters”
- `partner_id` Many2one “Public Partner” (related=user_id.partner_id)
- `menu_id` Many2one → `website.menu` “Main Menu” (compute=_compute_menu)
- `homepage_url` Char
- `custom_code_head` Html “Custom <head> code”
- `custom_code_footer` Html “Custom end of <body> code”
- `robots_txt` Html “Robots.txt”
- `favicon` Binary “Website Favicon”
- `theme_id` Many2one → `ir.module.module`
- `specific_user_account` Boolean “Specific User Account”
- `auth_signup_uninvited` Selection “Customer Account”

Public methods: `action_dashboard_redirect`, `button_go_website`, `configurator_apply`, `configurator_get_footer_links`, `configurator_init`, `configurator_recommended_themes`, `configurator_set_menu_links`, `configurator_skip`, `copy_menu_hierarchy`, `create`, `create_and_redirect_configurator`, `get_cdn_url`, `get_client_action`, `get_client_action_url`, `get_cta_data`, `get_current_website`, `get_suggested_controllers`, `get_template`, `get_theme_snippet_lists`, `get_unique_key`, `get_unique_path`, `get_website_page_ids`, `image_url`, `is_menu_cache_disabled`, `is_public_user`, `is_view_active`, `new_page`, `pager`, `rule_is_enumerable`, `search_pages`, `search_url_dependencies`, `unlink`, `viewref`, `website_domain`, `write`

Extension points: `_check_homepage_url`, `_check_snippet_used`, `_get_alternate_languages`, `_get_cached`, `_get_cached_values`, `_get_canonical_url`, `_get_canonical_url_localized`, `_get_current_website_id`, `_get_html_fields_attributes`, `_get_html_fields_attributes_blacklist`, `_get_menu_ids`, `_get_plausible_script_url`, `_get_plausible_server`, `_get_plausible_share_url`, `_get_snippets_assets`, `_get_website_pages`

## `website.configurator.feature` (defines)

Website Configurator Feature

- `sequence` Integer
- `name` Char
- `description` Char
- `icon` Char
- `iap_page_code` Char
- `website_config_preselection` Char
- `page_view_id` Many2one → `ir.ui.view`
- `module_id` Many2one → `ir.module.module`
- `feature_url` Char
- `menu_sequence` Integer
- `menu_company` Boolean

Extension points: `_check_module_xor_page_view`

## `website` (extends)


## `ir.model` (extends)

Models

- `website_form_access` Boolean “Allowed to use in forms”
- `website_form_default_field_id` Many2one → `ir.model.fields`
- `website_form_label` Char “Label for form action”
- `website_form_key` Char

Public methods: `get_authorized_fields`, `get_compatible_form_models`

Extension points: `_get_form_writable_fields`

## `ir.model.fields` (extends)

Fields

- `website_form_blacklisted` Boolean “Blacklisted in web forms” (index)

Public methods: `formbuilder_whitelist`, `init`

## `website.menu` (defines)

Website Menu

- `name` Char “Menu” (required)
- `url` Char “Url”
- `page_id` Many2one → `website.page`
- `new_window` Boolean “New Window”
- `sequence` Integer
- `website_id` Many2one → `website`
- `parent_id` Many2one → `website.menu` (index)
- `child_id` One2many → `website.menu` “Child Menus”
- `parent_path` Char (index)
- `is_visible` Boolean “Is Visible” (compute=_compute_visible)
- `is_mega_menu` Boolean
- `mega_menu_content` Html
- `mega_menu_classes` Char

Public methods: `clean_url`, `create`, `get_tree`, `name_get`, `save`, `unlink`, `write`

## `website.page` (defines)

Page

Inherits: `website.published.multi.mixin`, `website.searchable.mixin`

- `url` Char “Page URL”
- `view_id` Many2one → `ir.ui.view` “View” (required)
- `website_indexed` Boolean “Is Indexed”
- `date_publish` Datetime “Publishing Date”
- `menu_ids` One2many → `website.menu`
- `is_in_menu` Boolean (compute=_compute_website_menu)
- `is_homepage` Boolean “Homepage” (compute=_compute_is_homepage)
- `is_visible` Boolean “Is Visible” (compute=_compute_visible)
- `header_overlay` Boolean
- `header_color` Char
- `header_visible` Boolean
- `footer_visible` Boolean
- `website_id` Many2one (store, related=view_id.website_id)
- `arch` Text (related=view_id.arch)

Public methods: `action_page_debug_view`, `clone_page`, `copy`, `get_website_meta`, `unlink`, `write`

Extension points: `_get_most_specific_pages`

## `website.route` (defines)

All Website Route

- `path` Char “Route”

## `website.rewrite` (defines)

Website rewrite

- `name` Char “Name” (required)
- `website_id` Many2one → `website` “Website” (index)
- `active` Boolean
- `url_from` Char “URL from” (index)
- `route_id` Many2one → `website.route`
- `url_to` Char “URL to”
- `redirect_type` Selection “Action”
- `sequence` Integer

Public methods: `create`, `name_get`, `refresh_routes`, `unlink`, `write`

Extension points: `_check_url_to`

## `website.snippet.filter` (defines)

Website Snippet Filter

Inherits: `website.published.multi.mixin`

- `name` Char (required)
- `action_server_id` Many2one → `ir.actions.server`
- `field_names` Char (required)
- `filter_id` Many2one → `ir.filters`
- `limit` Integer (required)
- `website_id` Many2one → `website` “Website”
- `model_name` Char “Model name” (compute=_compute_model_name)

Extension points: `_check_data_source_is_provided`, `_check_field_names`, `_check_limit`, `_get_field_name_and_type`, `_get_filter_meta_data`, `_get_hardcoded_sample`, `_get_website_currency`, `_prepare_sample`, `_prepare_sample_records`, `_prepare_values`

## `website.track` (defines)

Visited Pages

- `visitor_id` Many2one → `website.visitor` (required, readonly, index)
- `page_id` Many2one → `website.page` (readonly, index)
- `url` Text “Url” (index)
- `visit_datetime` Datetime “Visit Date” (required, readonly)

## `website.visitor` (defines)

Website Visitor

- `name` Char “Name” (related=partner_id.name)
- `access_token` Char (required)
- `website_id` Many2one → `website` (readonly)
- `partner_id` Many2one → `res.partner` “Contact” (store, compute=_compute_partner_id)
- `partner_image` Binary (related=partner_id.image_1920)
- `country_id` Many2one → `res.country` (readonly)
- `country_flag` Char “Country Flag” (related=country_id.image_url)
- `lang_id` Many2one → `res.lang` “Language”
- `timezone` Selection “Timezone”
- `email` Char “Email” (compute=_compute_email_phone)
- `mobile` Char “Mobile” (compute=_compute_email_phone)
- `visit_count` Integer “# Visits” (readonly)
- `website_track_ids` One2many → `website.track` “Visited Pages History” (readonly)
- `visitor_page_count` Integer “Page Views” (compute=_compute_page_statistics)
- `page_ids` Many2many → `website.page` “Visited Pages” (compute=_compute_page_statistics)
- `page_count` Integer “# Visited Pages” (compute=_compute_page_statistics)
- `last_visited_page_id` Many2one → `website.page` “Last Visited Page” (compute=_compute_last_visited_page_id)
- `create_date` Datetime “First Connection” (readonly)
- `last_connection_datetime` Datetime “Last Connection” (readonly)
- `time_since_last_action` Char “Last action” (compute=_compute_time_statistics)
- `is_connected` Boolean “Is connected ?” (compute=_compute_time_statistics)

Public methods: `action_send_mail`, `name_get`

Extension points: `_check_for_message_composer`, `_get_access_token`, `_get_visitor_from_request`, `_get_visitor_timezone`, `_prepare_message_composer_context`

## `base.language.install` (extends)

- `website_ids` Many2many → `website` “Websites to translate”

Public methods: `default_get`, `lang_install`

## `portal.wizard.user` (extends)


Extension points: `_get_similar_users_domain`, `_get_similar_users_fields`

## `website.robots` (defines)

Robots.txt Editor

- `content` Text

Public methods: `action_save`
