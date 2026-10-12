# web — Web

Depends on: base.

## `base.document.layout` (defines)

Company Document Layout

- `company_id` Many2one → `res.company` (required)
- `logo` Binary (related=company_id.logo)
- `preview_logo` Binary “Preview logo” (related=logo)
- `report_header` Html (related=company_id.report_header)
- `report_footer` Html (related=company_id.report_footer)
- `company_details` Html (related=company_id.company_details)
- `is_company_details_empty` Boolean (compute=_compute_empty_company_details)
- `paperformat_id` Many2one (related=company_id.paperformat_id)
- `external_report_layout_id` Many2one (related=company_id.external_report_layout_id)
- `font` Selection (related=company_id.font)
- `primary_color` Char (related=company_id.primary_color)
- `secondary_color` Char (related=company_id.secondary_color)
- `custom_colors` Boolean (compute=_compute_custom_colors)
- `logo_primary_color` Char (compute=_compute_logo_colors)
- `logo_secondary_color` Char (compute=_compute_logo_colors)
- `layout_background` Selection (related=company_id.layout_background)
- `layout_background_image` Binary (related=company_id.layout_background_image)
- `report_layout_id` Many2one → `report.layout`
- `preview` Html (compute=_compute_preview)
- `partner_id` Many2one (readonly, related=company_id.partner_id)
- `phone` Char (readonly, related=company_id.phone)
- `email` Char (readonly, related=company_id.email)
- `website` Char (readonly, related=company_id.website)
- `vat` Char (readonly, related=company_id.vat)
- `name` Char (readonly, related=company_id.name)
- `country_id` Many2one (readonly, related=company_id.country_id)

Public methods: `document_layout_save`, `extract_image_primary_secondary_colors`

Extension points: `_get_asset_style`, `_get_css_for_preview`, `_get_preview_template`, `_get_render_information`

## `ir.http` (extends)


Public methods: `color_scheme`, `get_currencies`, `get_frontend_session_info`, `is_a_bot`, `lazy_session_info`, `session_info`, `webclient_rendering_context`

Extension points: `_post_logout`

## `ir.model` (extends)


Public methods: `display_name_for`, `get_available_models`

Extension points: `_get_definitions`

## `ir.qweb.field.image` (extends)


Public methods: `record_to_html`

Extension points: `_get_src_urls`

## `ir.qweb.field.image_url` (extends)


Extension points: `_get_src_urls`

## `ir.ui.menu` (extends)


Public methods: `load_web_menus`

## `ir.ui.view` (extends)


Public methods: `get_view_info`

Extension points: `_get_view_info`

## `base` (extends)


Public methods: `formatted_read_group`, `formatted_read_grouping_sets`, `onchange`, `onchange_batch`, `read_progress_bar`, `search_panel_select_multi_range`, `search_panel_select_range`, `web_name_search`, `web_override_translations`, `web_read`, `web_read_group`, `web_resequence`, `web_save`, `web_save_multi`, `web_search_read`

Extension points: `_get_read_group_order`

## `res.company` (extends)


Public methods: `create`, `write`

Extension points: `_get_asset_style_b64`

## `properties.base.definition` (extends)


Public methods: `get_properties_base_definition`

## `res.config.settings` (extends)

- `web_app_name` Char “Web App Name”

## `res.partner` (extends)


Extension points: `_get_vcard_file`

## `res.users` (extends)


Public methods: `name_search`

## `res.users.settings` (extends)

- `embedded_actions_config_ids` One2many → `res.users.settings.embedded.action`

Public methods: `get_embedded_actions_settings`, `set_embedded_actions_setting`

## `res.users.settings.embedded.action` (defines)

User Settings for Embedded Actions

- `user_setting_id` Many2one → `res.users.settings` (required)
- `action_id` Many2one → `ir.actions.act_window` (required)
- `res_model` Char (required)
- `res_id` Integer
- `embedded_actions_order` Char “List order of embedded action ids”
- `embedded_actions_visibility` Char “List visibility of embedded actions ids”
- `embedded_visibility` Boolean “Is top bar visible”

Extension points: `_check_embedded_actions_field_format`, `_check_embedded_actions_order`, `_check_embedded_actions_visibility`
