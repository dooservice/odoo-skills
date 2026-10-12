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

Public methods: `action_open_base_document_layout`, `document_layout_save`, `extract_image_primary_secondary_colors`

Extension points: `_get_asset_style`, `_get_css_for_preview`

## `ir.http` (extends)


Public methods: `get_currencies`, `get_frontend_session_info`, `is_a_bot`, `session_info`, `webclient_rendering_context`

## `ir.model` (extends)


Public methods: `display_name_for`, `get_available_models`

Extension points: `_check_model_access`

## `ir.qweb.field.image` (extends)

Qweb Field Image


Public methods: `record_to_html`

Extension points: `_get_src_urls`

## `ir.qweb.field.image_url` (extends)

Qweb Field Image


Extension points: `_get_src_urls`

## `ir.ui.menu` (extends)


Public methods: `load_web_menus`

## `ir.actions.act_window.view` (extends)

- `view_mode` Selection

## `base` (extends)


Public methods: `qweb_render_view`, `read_progress_bar`, `search_panel_select_multi_range`, `search_panel_select_range`, `web_read_group`, `web_search_read`

Extension points: `_get_view`

## `res.company` (extends)


Public methods: `create`, `write`

Extension points: `_get_asset_style_b64`
