# website — Website

Depends on: digest, web, html_editor, http_routing, portal, social_media, auth_signup, mail, google_recaptcha, utm, html_builder.

## `website.assets` (defines)

Assets Utils


Public methods: `make_scss_customization`, `reset_asset`, `save_asset`

Extension points: `_get_content_from_url`, `_get_custom_asset`, `_get_custom_attachment`, `_get_data_from_url`

## `base.partner.merge.automatic.wizard` (extends)


## `digest.digest` (extends)

- `kpi_website_visitor_count` Boolean “Visitors”
- `kpi_website_visitor_count_value` Integer (compute=_compute_kpi_website_visitors_count_value)
- `kpi_website_track_count` Boolean “Tracked Page Views”
- `kpi_website_track_count_value` Integer (compute=_compute_kpi_website_track_count_value)

Extension points: `_get_kpi_custom_settings`

## `website.html.text.processor` (defines)

HTML Text Processor Abstract Model


Extension points: `_get_processing_cache`, `_get_rendered_snippets_content`, `_get_snippet_content`

## `ir.access` (extends)


Extension points: `_get_access_context`

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

Extension points: `_get_active_addons_list`, `_get_asset_bundle_url`, `_get_asset_params`, `_get_related_assets`

## `ir.attachment` (extends)

- `key` Char
- `website_id` Many2one → `website`

Public methods: `create`, `get_serving_groups`

Extension points: `_get_mimetype_exempt_groups`, `_get_serve_attachment`

## `ir.binary` (extends)


## `ir.http` (extends)


Public methods: `get_frontend_session_info`, `routing_map`

Extension points: `_get_converters`, `_get_default_lang`, `_get_editor_context`, `_get_error_html`, `_get_exception_code_values`, `_get_public_users`, `_get_rewrites`, `_get_translation_frontend_modules_name`, `_get_values_500_error`, `_get_visitor_from_request`, `_post_dispatch`

## `base` (extends)


Public methods: `get_base_url`, `get_website_meta`

Extension points: `_get_base_lang`

## `ir.model.data` (extends)


## `ir.module.module` (extends)

Module

- `image_ids` One2many → `ir.attachment` “Screenshots” (readonly)
- `is_installed_on_current_website` Boolean (compute=_compute_is_installed_on_current_website)

Public methods: `button_choose_theme`, `button_refresh_theme`, `button_remove_theme`, `get_themes_domain`, `update_list`, `update_theme_images`, `write`

Extension points: `_create_model_data`, `_get_module_data`, `_post_copy`

## `ir.qweb` (extends)


Extension points: `_get_template`, `_get_template_cache_keys`, `_post_processing_att`

## `ir.qweb.field.contact` (extends)


Public methods: `get_available_options`

## `ir.qweb.field.html` (extends)


Public methods: `value_to_html`

Extension points: `_post_processing_att`

## `ir.ui.menu` (extends)


Public methods: `load_menus_root`

## `ir.ui.view` (extends)

Inherits: `website.seo.metadata`

- `website_id` Many2one → `website` “Website”
- `page_ids` One2many → `website.page`
- `controller_page_ids` One2many → `website.controller.page`
- `first_page_id` Many2one → `website.page` “Website Page” (compute=_compute_first_page_id)
- `track` Boolean “Track”
- `visibility` Selection (required)
- `visibility_password` Char
- `visibility_password_display` Char (compute=_get_pwd)

Public methods: `create`, `extract_embedded_fields`, `extract_oe_structures`, `filter_duplicate`, `get_default_lang_code`, `get_related_views`, `get_view_hierarchy`, `replace_arch_section`, `save`, `save_embedded_field`, `save_oe_structure`, `to_empty_oe_structure`, `to_field_ref`, `unlink`, `write`

Extension points: `_create_all_specific_views`, `_create_website_specific_pages_for_view`, `_get_allowed_root_attrs`, `_get_base_lang`, `_get_cached_template_prefetched_keys`, `_get_cached_visibility`, `_get_filter_xmlid_query`, `_get_inheriting_views`, `_get_inheriting_views_domain`, `_get_pwd`, `_get_snippet_addition_view_key`, `_get_template_domain`, `_get_template_minimal_cache_keys`, `_get_template_order`, `_get_used_names_domain`

## `website.seo.metadata` (defines)

SEO metadata

- `is_seo_optimized` Boolean “SEO optimized” (store, compute=_compute_is_seo_optimized)
- `website_meta_title` Char “Website meta title”
- `website_meta_description` Text “Website meta description”
- `website_meta_keywords` Char “Website meta keywords”
- `website_meta_og_img` Char “Website opengraph image”
- `seo_name` Char “Seo name”

Public methods: `get_website_meta`, `get_website_meta_i18n_value`

Extension points: `_get_website_meta_translations`

## `website.trackable.mixin` (defines)

Website Trackable Mixin


Extension points: `_get_extra_tracking_values`

## `website.cover_properties.mixin` (defines)

Cover Properties Website Mixin

- `cover_properties` Text “Cover Properties”

Public methods: `write`

Extension points: `_get_background`, `_get_image_url`

## `website.page_visibility_options.mixin` (defines)

Website page/record specific visibility options

- `header_visible` Boolean
- `footer_visible` Boolean
- `breadcrumb_visible` Boolean

## `website.page_options.mixin` (defines)

Website page/record specific options

Inherits: `website.page_visibility_options.mixin`

- `header_overlay` Boolean
- `header_color` Char
- `header_text_color` Char
- `breadcrumb_overlay` Boolean
- `breadcrumb_color` Char
- `breadcrumb_text_color` Char

## `website.multi.mixin` (defines)

Multi Website Mixin

- `website_id` Many2one → `website` “Website” (index)

## `website.located.mixin` (defines)

Website Located Mixin

- `website_url` Char “Website URL” (compute=_compute_website_url)
- `website_absolute_url` Char “Website Absolute URL” (compute=_compute_website_absolute_url)

## `website.structured_data.mixin` (defines)

Website Structured Data Mixin


Extension points: `_get_breadcrumb_items`, `_get_jsonld_dict`, `_prepare_jsonld_vals`

## `website.published.mixin` (defines)

Website Published Mixin

Inherits: `website.located.mixin`

- `website_published` Boolean “Visible on current website” (related=is_published)
- `is_published` Boolean “Is Published” (index)
- `publish_on` Datetime “Auto publish on”
- `published_date` Datetime “Published date”
- `can_publish` Boolean “Can Publish” (compute=_compute_can_publish)

Public methods: `action_unschedule`, `create`, `create_and_get_website_url`, `open_website_url`, `website_publish_button`, `write`

Extension points: `_check_for_action_post_publish`, `_get_can_publish_error_message`

## `website.published.multi.mixin` (defines)

Multi Website Published Mixin

Inherits: `website.published.mixin`, `website.multi.mixin`

- `website_published` Boolean (compute=_compute_website_published)

Public methods: `open_website_url`

## `website.searchable.mixin` (defines)

Website Searchable Mixin


Extension points: `_get_search_highlight_handlers`

## `base` (extends)


## `res.company` (extends)

- `website_id` Many2one → `website` (store, compute=_compute_website_id)

Public methods: `action_open_website_theme_selector`, `google_map_img`, `google_map_link`

Extension points: `_check_active`

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
- `cookie_policy_id` Many2one “Cookie Policy Page” (related=website_id.cookie_policy_id)
- `has_cookie_policy` Boolean (compute=_compute_has_cookie_policy)
- `website_block_third_party_domains` Boolean “Block 3rd-party domains” (related=website_id.block_third_party_domains)
- `google_analytics_key` Char “Google Analytics Key” (related=website_id.google_analytics_key)
- `google_search_console` Char “Google Search Console Key” (related=website_id.google_search_console)
- `plausible_shared_key` Char “Plausible auth Key” (related=website_id.plausible_shared_key)
- `plausible_site` Char “Plausible Site (e.g. domain.com)” (related=website_id.plausible_site)
- `cdn_activated` Boolean (related=website_id.cdn_activated)
- `cdn_url` Char (related=website_id.cdn_url)
- `cdn_filters` Text (related=website_id.cdn_filters)
- `auth_signup_uninvited` Selection (compute=_compute_auth_signup_uninvited)
- `favicon` Binary “Favicon” (related=website_id.favicon)
- `social_default_image` Binary “Default Social Share Image” (related=website_id.social_default_image)
- `group_multi_website` Boolean “Multi-website”
- `has_google_analytics` Boolean “Google Tag Manager/Google Analytics” (compute=_compute_has_google_analytics)
- `has_google_search_console` Boolean “Google Search Console” (compute=_compute_has_google_search_console)
- `has_default_share_image` Boolean “Use a image by default for sharing” (compute=_compute_has_default_share_image)
- `has_plausible_shared_key` Boolean “Plausible Analytics” (compute=_compute_has_plausible_shared_key)
- `module_website_livechat` Boolean
- `module_website_address_autocomplete` Boolean “Website Address Autocomplete”

Public methods: `action_open_blocked_third_party_domains`, `action_open_llms`, `action_open_robots`, `action_website_create_new`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.lang` (extends)


Public methods: `action_activate_langs`, `write`

Extension points: `_get_frontend`

## `res.partner` (extends)

Inherits: `website.published.multi.mixin`

- `visitor_ids` One2many → `website.visitor` “Visitors”

Public methods: `google_map_img`, `google_map_link`

## `res.users` (extends)

- `website_id` Many2one → `website` (store, related=partner_id.website_id)

Public methods: `authenticate`, `website_publish_button`

Extension points: `_check_disjoint_groups`, `_check_login`, `_get_email_domain`, `_get_login_domain`, `_get_login_order`, `_get_signup_invitation_scope`

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

Theme Attachment

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

Inherits: `website.page_options.mixin`

- `url` Char
- `view_id` Many2one → `theme.ir.ui.view` (required, index)
- `website_indexed` Boolean “Page Indexed”
- `is_published` Boolean
- `is_new_page_template` Boolean “New Page Template”
- `copy_ids` One2many → `website.page` (readonly)

## `theme.utils` (defines)

Theme Utils


Public methods: `disable_asset`, `disable_view`, `enable_asset`, `enable_view`, `set_page_option`

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

## `website` (extends)

Website

Inherits: `website.structured_data.mixin`

- `language_ids` Many2many → `res.lang` “Languages” (required)
- `language_count` Integer “Number of languages” (compute=_compute_language_count)
- `default_lang_id` Many2one → `res.lang` “Default Language” (required)
- `auto_redirect_lang` Boolean “Autoredirect Language”
- `cookies_bar` Boolean “Cookies Bar”
- `cookie_policy_id` Many2one → `website.page` “Cookie Policy Page”
- `configurator_done` Boolean
- `block_third_party_domains` Boolean “Block 3rd-party domains”
- `custom_blocked_third_party_domains` Text “User list of blocked 3rd-party domains”
- `blocked_third_party_domains` Text “List of blocked 3rd-party domains” (compute=_compute_blocked_third_party_domains)
- `logo` Binary “Website Logo”
- `social_default_image` Binary “Default Social Share Image”
- `has_social_default_image` Boolean (store, compute=_compute_has_social_default_image)
- `google_analytics_key` Char “Google Analytics Key”
- `google_search_console` Char
- `google_maps_api_key` Char “Google Maps API Key”
- `plausible_shared_key` Char
- `plausible_site` Char
- `cdn_activated` Boolean “Content Delivery Network (CDN)”
- `cdn_url` Char “CDN Base URL”
- `cdn_filters` Text “CDN Filters”
- `partner_id` Many2one “Public Partner” (related=user_id.partner_id)
- `menu_id` Many2one → `website.menu` “Main Menu” (compute=_compute_menu)
- `homepage_url` Char
- `custom_code_head` Html “Custom <head> code”
- `custom_code_footer` Html “Custom end of <body> code”
- `robots_txt` Html “Robots.txt”
- `llms_txt` Text “LLMs.txt”
- `header_search_type` Char “Header Search Scope” (required)
- `header_search_order_by` Char “Header Search Sort” (required)
- `header_search_limit` Integer “Header Search Suggestions”
- `favicon` Binary “Website Favicon”
- `theme_id` Many2one → `ir.module.module`
- `specific_user_account` Boolean “Specific User Account”
- `auth_signup_uninvited` Selection “Customer Account”

Public methods: `action_dashboard_redirect`, `button_go_website`, `check_existing_page`, `configurator_addons_apply`, `configurator_apply`, `configurator_get_footer_links`, `configurator_get_images`, `configurator_init`, `configurator_missing_industry`, `configurator_recommended_themes`, `configurator_set_menu_links`, `configurator_skip`, `copy_menu_hierarchy`, `create`, `create_and_redirect_configurator`, `get_cdn_url`, `get_client_action`, `get_client_action_url`, `get_cta_data`, `get_search_scopes`, `get_suggested_controllers`, `get_theme_configurator_snippets`, `get_unique_key`, `get_unique_path`, `get_website_page_ids`, `image_url`, `is_menu_cache_disabled`, `is_public_user`, `is_reachable`, `is_view_active`, `new_page`, `pager`, `rule_is_enumerable`, `search_pages`, `search_url_dependencies`, `set_header_search`, `unlink`, `viewref`, `website_domain`, `write`

Extension points: `_check_configurator_access`, `_check_domain`, `_check_homepage_url`, `_check_snippet_used`, `_check_user_can_modify`, `_get_blocked_iframe_containers_classes`, `_get_blocked_third_party_domains_list`, `_get_canonical_url`, `_get_configurator_theme_preview_url`, `_get_font_urls`, `_get_header_search_scope`, `_get_html_fields`, `_get_html_fields_blacklist`, `_get_icon_font_family`, `_get_plausible_script_url`, `_get_plausible_server`, `_get_plausible_share_url`, `_get_scss_exports`, `_get_search_scopes`, `_get_settings_to_copy_onto_new_default_website`, `_get_snippet_defaults`, `_get_snippet_view_key`, `_get_website_pages`, `_prepare_jsonld_vals`

## `website.configurator.feature` (defines)

Website Configurator Feature

- `sequence` Integer
- `name` Char
- `description` Char
- `icon` Char
- `icon_class` Char
- `iap_page_code` Char
- `website_config_preselection` Char
- `page_view_id` Many2one → `ir.ui.view`
- `module_id` Many2one → `ir.module.module`
- `feature_url` Char
- `menu_sequence` Integer
- `menu_company` Boolean

Extension points: `_check_module_xor_page_view`

## `website.controller.page` (defines)

Model Page

Inherits: `website.published.multi.mixin`, `website.searchable.mixin`

- `view_id` Many2one → `ir.ui.view` “Listing view” (required, index)
- `record_view_id` Many2one → `ir.ui.view` “Record view”
- `menu_ids` One2many → `website.menu`
- `website_id` Many2one (store, related=view_id.website_id)
- `name` Char “The name is used to generate the URL and is shown in the browser title bar” (required, store, compute=_compute_name)
- `name_slugified` Char “URL” (store, compute=_compute_name_slugified)
- `url_demo` Char “Demo URL” (compute=_compute_url_demo)
- `record_domain` Char “Domain”
- `default_layout` Selection

Public methods: `create`, `open_website_url`, `unlink`, `write`

Extension points: `_check_user_has_model_access`

## `website` (extends)


## `ir.model` (extends)

- `website_form_access` Boolean “Allowed to use in forms”
- `website_form_default_field_id` Many2one → `ir.model.fields`
- `website_form_label` Char “Label for form action”
- `website_form_key` Char

Public methods: `get_authorized_fields`, `get_compatible_form_models`

Extension points: `_get_form_writable_fields`

## `ir.model.fields` (extends)

- `website_form_blacklisted` Boolean “Blacklisted in web forms” (index)

Public methods: `formbuilder_whitelist`, `init`

Extension points: `_check_if_used_in_website_form`

## `website.menu` (defines)

Website Menu

- `name` Char “Menu” (required)
- `url` Char “Url” (compute=_compute_url)
- `manual_url` Char “Url defined by user”
- `page_id` Many2one → `website.page`
- `controller_page_id` Many2one → `website.controller.page`
- `new_window` Boolean “New Window”
- `sequence` Integer
- `website_id` Many2one → `website`
- `parent_id` Many2one → `website.menu` (index)
- `child_id` One2many → `website.menu` “Child Menus”
- `parent_path` Char (index)
- `is_visible` Boolean “Is Visible” (compute=_compute_visible)
- `group_ids` Many2many → `res.groups` “Visible Groups”
- `is_mega_menu` Boolean (compute=_compute_field_is_mega_menu)
- `mega_menu_content` Html
- `mega_menu_classes` Char

Public methods: `create`, `get_tree`, `save`, `unlink`, `write`

## `website.page` (defines)

Page

Inherits: `website.published.multi.mixin`, `website.searchable.mixin`, `website.page_options.mixin`, `website.trackable.mixin`

- `name` Char “Page Name” (store, compute=_compute_name)
- `url` Char “Page URL” (required)
- `view_id` Many2one → `ir.ui.view` “View” (required, index)
- `view_write_uid` Many2one → `res.users` (related=view_id.write_uid)
- `view_write_date` Datetime “Last Content Update on” (related=view_id.write_date)
- `website_indexed` Boolean “Is Indexed”
- `menu_ids` One2many → `website.menu`
- `is_in_menu` Boolean (compute=_compute_website_menu)
- `is_homepage` Boolean “Homepage” (compute=_compute_is_homepage)
- `is_visible` Boolean “Is Visible” (compute=_compute_visible)
- `is_new_page_template` Boolean “New Page Template”
- `parent_id` Many2one → `website.page` “Parent Page”
- `parent_ids` Many2many → `website.page` (compute=_compute_parent_ids)
- `website_id` Many2one (store, related=view_id.website_id)
- `arch` Text (related=view_id.arch)

Public methods: `action_page_debug_view`, `clone_page`, `copy_data`, `get_website_meta`, `open_website_url`, `unlink`, `write`

Extension points: `_get_cache_key`, `_get_most_specific_pages`, `_get_page_info`, `_get_response`, `_get_response_cached`, `_get_response_raw`, `_post_process_response_from_cache`

## `website.page.properties.base` (defines)

Page Properties Base

- `target_model_id` Reference (required)
- `website_id` Many2one → `website` (required)
- `menu_ids` One2many → `website.menu` (compute=_compute_menu_ids)
- `is_in_menu` Boolean (compute=_compute_is_in_menu)
- `url` Char (required)
- `is_homepage` Boolean “Homepage” (compute=_compute_is_homepage)
- `can_publish` Boolean (compute=_compute_can_publish)
- `is_published` Boolean (compute=_compute_is_published)
- `published_date` Datetime (compute=_compute_published_date)
- `publish_on` Datetime (compute=_compute_publish_on)

Public methods: `action_unschedule`, `write`

Extension points: `_get_ir_ui_view_unpublish_group`, `_get_menu_domain`

## `website.page.properties` (defines)

Page Property

Inherits: `website.page.properties.base`

- `target_model_id` Many2one → `website.page`
- `name` Char (related=target_model_id.name)
- `url` Char (related=target_model_id.url)
- `website_indexed` Boolean (related=target_model_id.website_indexed)
- `visibility` Selection (related=target_model_id.visibility)
- `visibility_password_display` Char (related=target_model_id.visibility_password_display)
- `group_ids` Many2many (related=target_model_id.group_ids)
- `is_new_page_template` Boolean (related=target_model_id.is_new_page_template)
- `has_parent_page` Boolean (compute=_compute_has_parent_page)
- `parent_id` Many2one (related=target_model_id.parent_id)
- `old_url` Char
- `redirect_old_url` Boolean
- `redirect_type` Selection (required)
- `url_in_website_default_lang` Char (compute=_compute_url_in_website_default_lang)

Public methods: `create`, `write`

## `website.route` (defines)

All Website Route

- `path` Char “Route”

Public methods: `name_search`

## `website.rewrite` (defines)

Website rewrite

- `name` Char “Name”
- `website_id` Many2one → `website` “Website” (index)
- `active` Boolean
- `url_from` Char “URL from” (required, index)
- `route_id` Many2one → `website.route`
- `url_to` Char “URL to”
- `redirect_type` Selection “Action” (required)
- `is_url_from_exist` Boolean (compute=_compute_is_url_from_exist)
- `sequence` Integer

Public methods: `create`, `get_import_templates`, `refresh_routes`, `unlink`, `write`

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
- `help` Text “Description”

Extension points: `_check_data_source_is_provided`, `_check_field_names`, `_check_limit`, `_get_field_name_and_type`, `_get_filter_meta_data`, `_get_hardcoded_sample`, `_get_website_currency`, `_prepare_sample`, `_prepare_sample_records`, `_prepare_values`

## `website.technical.page` (defines)

Website Technical Page

- `name` Char “Page Name”
- `website_url` Char “Website Page URL”

Public methods: `open_website_url`

Extension points: `_get_static_routes`

## `website.track` (defines)

Visited Page

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
- `is_connected` Boolean “Is connected?” (compute=_compute_time_statistics)

Public methods: `action_send_mail`

Extension points: `_check_for_message_composer`, `_get_access_token`, `_get_additional_track_query_parts`, `_get_visitor_statistics`, `_get_visitor_timezone`, `_prepare_message_composer_context`

## `base.language.install` (extends)

- `website_ids` Many2many → `website` “Websites to translate”

Public methods: `default_get`, `lang_install`

## `website.custom_blocked_third_party_domains` (defines)

User list of blocked 3rd-party domains

- `content` Text

Public methods: `action_save`

## `portal.wizard.user` (extends)


Extension points: `_get_similar_users_domain`, `_get_similar_users_fields`

## `website.llms` (defines)

LLMs.txt Editor

Inherits: `website.multi.mixin`

- `content` Text (related=website_id.llms_txt)

Public methods: `action_save`

## `website.robots` (defines)

Robots.txt Editor

- `content` Text

Public methods: `action_save`
