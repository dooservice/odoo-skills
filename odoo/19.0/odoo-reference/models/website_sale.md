# website_sale — eCommerce

Depends on: website, sale, website_payment, website_mail, portal_rating, digest, delivery, html_builder.

## `account.move` (extends)

- `website_id` Many2one → `website` “Website” (readonly, store, compute=_compute_website_id)

Public methods: `preview_invoice`

## `crm.team` (extends)

- `website_ids` One2many → `website` “Websites”
- `abandoned_carts_amount` Integer “Amount of Abandoned Carts” (compute=_compute_abandoned_carts)
- `abandoned_carts_count` Integer “Number of Abandoned Carts” (compute=_compute_abandoned_carts)

Public methods: `get_abandoned_carts`

## `delivery.carrier` (extends)

Inherits: `website.published.multi.mixin`

- `website_description` Text “Description for Online Quotations” (related=product_id.description_sale)

## `digest.digest` (extends)

- `kpi_website_sale_total` Boolean “eCommerce Sales”
- `kpi_website_sale_total_value` Monetary (compute=_compute_kpi_website_sale_total_value)

## `ir.http` (extends)


Public methods: `get_frontend_session_info`

## `ir.module.module` (extends)


## `payment.token` (extends)


Extension points: `_get_available_tokens`

## `product.attribute` (extends)

- `visibility` Selection
- `preview_variants` Selection “On Product Cards”
- `is_thumbnail_visible` Boolean “Show Thumbnails”

## `product.document` (extends)

- `shown_on_product_page` Boolean “Publish on website”

## `product.feed` (defines)

Product Feed

Inherits: `mail.thread`

- `name` Char (required)
- `website_id` Many2one → `website` (required)
- `pricelist_id` Many2one → `product.pricelist`
- `lang_id` Many2one → `res.lang` “Language” (required, store, compute=_compute_lang_id)
- `website_lang_ids` Many2many (related=website_id.language_ids)
- `product_category_ids` Many2many → `product.public.category` “Categories”
- `target` Selection (required)
- `access_token` Char (required, readonly)
- `url` Char (compute=_compute_url)
- `last_notification_date` Date
- `feed_cache` Binary (readonly, store, compute=_compute_feed_cache)
- `cache_expiry` Datetime (required, readonly)

Public methods: `action_invalidate_cache`

Extension points: `_check_product_limit`, `_get_feed_product_domain`, `_get_feed_products`, `_prepare_gmc_additional_info`, `_prepare_gmc_identifier`, `_prepare_gmc_image_links`, `_prepare_gmc_items`, `_prepare_gmc_price_info`, `_prepare_gmc_stock_info`

## `product.image` (defines)

Product Image

Inherits: `image.mixin`

- `name` Char “Name” (required)
- `sequence` Integer
- `image_1920` Image
- `product_tmpl_id` Many2one → `product.template` “Product Template” (index)
- `product_variant_id` Many2one → `product.product` “Product Variant” (index)
- `video_url` Char “Video URL”
- `embed_code` Html (compute=_compute_embed_code)
- `can_image_1024_be_zoomed` Boolean “Can Image 1024 be zoomed” (store, compute=_compute_can_image_1024_be_zoomed)

Public methods: `create`

Extension points: `_check_valid_video_url`

## `product.pricelist` (extends)

- `website_id` Many2one → `website` “Website”
- `code` Char “E-commerce Promotional Code”
- `selectable` Boolean

Public methods: `create`, `unlink`, `write`

Extension points: `_check_websites_in_company`, `_get_partner_pricelist_multi_filter_hook`, `_get_partner_pricelist_multi_search_domain_hook`, `_get_website_pricelists_domain`

## `product.pricelist.item` (extends)


## `product.product` (extends)

- `variant_ribbon_id` Many2one → `product.ribbon` “Variant Ribbon”
- `website_id` Many2one (related=product_tmpl_id.website_id)
- `product_variant_image_ids` One2many → `product.image` “Extra Variant Images”
- `base_unit_count` Float “Base Unit Count” (required)
- `base_unit_id` Many2one → `website.base.unit` “Custom Unit of Measure”
- `base_unit_price` Monetary “Price Per Unit” (compute=_compute_base_unit_price)
- `base_unit_name` Char (compute=_compute_base_unit_name)
- `website_url` Char “Website URL” (compute=_compute_product_website_url)

Public methods: `open_website_url`, `website_publish_button`, `write`

Extension points: `_check_base_unit_count`, `_get_base_unit_price`, `_get_combination_info_variant`, `_get_extra_image_1920_urls`, `_get_image_1920_url`, `_get_images`, `_prepare_variant_values`

## `product.public.category` (defines)

Website Product Category

Inherits: `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `image.mixin`

- `name` Char (required)
- `cover_image` Image “Cover Image”
- `sequence` Integer (index)
- `parent_id` Many2one → `product.public.category` “Parent” (index)
- `child_id` One2many → `product.public.category` “Children Categories”
- `parent_path` Char (index)
- `parents_and_self` Many2many → `product.public.category` (compute=_compute_parents_and_self)
- `product_tmpl_ids` Many2many → `product.template`
- `has_published_products` Boolean (compute=_compute_has_published_products)
- `website_description` Html “Description”
- `website_footer` Html “Category Footer”
- `show_category_title` Boolean “Show Category Title”
- `show_category_description` Boolean “Show Category Description”
- `align_category_content` Boolean “Align Category Content”

Public methods: `check_parent_id`, `get_available_snippet_categories`

Extension points: `_get_available_category_domain`

## `product.ribbon` (defines)

Product ribbon

- `name` Char “Ribbon Name” (required)
- `sequence` Integer
- `bg_color` Char “Background Color” (required)
- `text_color` Char “Text Color” (required)
- `position` Selection “Position” (required)
- `style` Selection “Style” (required)
- `assign` Selection “Assign” (required)
- `new_period` Integer

Extension points: `_check_assign`, `_get_css_classes`

## `product.tag` (extends)

Inherits: `website.multi.mixin`


## `product.template` (extends)

Inherits: `rating.mixin`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`

- `website_description` Html “Description for the website”
- `description_ecommerce` Html “eCommerce Description”
- `alternative_product_ids` Many2many → `product.template` “Alternative Products”
- `accessory_product_ids` Many2many → `product.product` “Accessory Products”
- `website_size_x` Integer “Size X”
- `website_size_y` Integer “Size Y”
- `website_ribbon_id` Many2one → `product.ribbon` “Ribbon”
- `website_sequence` Integer “Website Sequence” (index)
- `public_categ_ids` Many2many → `product.public.category` “Website Product Category”
- `publish_date` Datetime “Publish Date” (required, store, compute=_compute_publish_date)
- `product_template_image_ids` One2many → `product.image` “Extra Product Media”
- `base_unit_count` Float “Base Unit Count” (required, store, compute=_compute_base_unit_count)
- `base_unit_id` Many2one → `website.base.unit` “Custom Unit of Measure” (store, compute=_compute_base_unit_id)
- `base_unit_price` Monetary “Price Per Unit” (compute=_compute_base_unit_price)
- `base_unit_name` Char (compute=_compute_base_unit_name)
- `compare_list_price` Monetary “Compare to Price”
- `variants_default_code` Char (store, compute=_compute_variants_default_code)
- `description` Html
- `description_sale` Text

Public methods: `create_product_variant`, `set_sequence_bottom`, `set_sequence_down`, `set_sequence_top`, `set_sequence_up`, `write`

Extension points: `_get_access_action`, `_get_additionnal_combination_info`, `_get_alternative_product_filter`, `_get_attribute_value_domain`, `_get_base_unit_price`, `_get_combination_info`, `_get_configurator_display_price`, `_get_contextual_pricelist`, `_get_google_analytics_data`, `_get_image_holder`, `_get_images`, `_get_possible_variants_sorted`, `_get_previewed_attribute_values`, `_get_product_types_allow_zero_price`, `_get_product_url`, `_get_ribbon`, `_get_sales_prices`, `_get_suitable_image_size`, `_get_website_accessory_product`, `_get_website_alternative_product`, `_get_website_sale_search_fields`, `_prepare_variant_values`

## `product.template.attribute.line` (extends)


Extension points: `_prepare_single_value_for_display`, `_prepare_single_value_including_multi_type_for_display`

## `product.template.attribute.value` (extends)


Extension points: `_get_extra_price`

## `res.company` (extends)


Extension points: `_get_default_pricelist_vals`

## `res.config.settings` (extends)

- `group_show_uom_price` Boolean “Base Unit Price”
- `group_product_price_comparison` Boolean “Comparison Price”
- `group_gmc_feed` Boolean “Google Merchant Center” (related=website_id.enabled_gmc_src)
- `module_website_sale_autocomplete` Boolean “Address Autocomplete”
- `module_website_sale_collect` Boolean “Click & Collect”
- `add_to_cart_action` Selection (related=website_id.add_to_cart_action)
- `cart_recovery_mail_template` Many2one (related=website_id.cart_recovery_mail_template_id)
- `cart_abandoned_delay` Float (related=website_id.cart_abandoned_delay)
- `send_abandoned_cart_email` Boolean “Abandoned Email” (related=website_id.send_abandoned_cart_email)
- `salesperson_id` Many2one (related=website_id.salesperson_id)
- `salesteam_id` Many2one (related=website_id.salesteam_id)
- `website_sale_prevent_zero_price_sale` Boolean “Prevent Sale of Zero Priced Product” (related=website_id.prevent_zero_price_sale)
- `website_sale_contact_us_button_url` Char “Button Url” (related=website_id.contact_us_button_url)
- `show_line_subtotals_tax_selection` Selection (related=website_id.show_line_subtotals_tax_selection)
- `confirmation_email_template_id` Many2one (related=website_id.confirmation_email_template_id)
- `account_on_checkout` Selection “Customer Accounts” (required, compute=_compute_account_on_checkout)
- `ecommerce_access` Selection (related=website_id.ecommerce_access)

Public methods: `action_open_abandoned_cart_mail_template`, `action_open_extra_info`, `action_open_product_feeds`, `action_open_sale_mail_templates`, `action_view_delivery_provider_modules`, `set_values`

## `res.partner` (extends)


Public methods: `write`

Extension points: `_get_current_partner`, `_get_frontend_writable_fields`, `_get_order_fiscal_position_recompute_domain`

## `sale.order` (extends)

- `website_id` Many2one → `website` (readonly)
- `cart_recovery_email_sent` Boolean “Cart recovery email already sent”
- `shop_warning` Char “Warning”
- `website_order_line` One2many → `sale.order.line` “Order Lines displayed on Website” (compute=_compute_website_order_line)
- `amount_delivery` Monetary “Delivery Amount” (compute=_compute_amount_delivery)
- `cart_quantity` Integer “Cart Quantity” (compute=_compute_cart_info)
- `only_services` Boolean “Only Services” (compute=_compute_cart_info)
- `is_abandoned_cart` Boolean “Abandoned Cart” (compute=_compute_abandoned_cart)

Public methods: `action_confirm`, `action_preview_sale_order`, `action_recovery_email_send`, `create`

Extension points: `_check_cart_is_ready_to_be_paid`, `_check_combo_quantities`, `_create_new_cart_line`, `_get_amount_total_excluding_delivery`, `_get_cart_recovery_template`, `_get_confirmation_template`, `_get_delivery_methods`, `_get_lang`, `_get_non_delivery_lines`, `_get_note_url`, `_get_preferred_delivery_method`, `_get_shop_warning`, `_get_zero_priced_lines`, `_prepare_order_line_update_values`, `_prepare_order_line_values`

## `sale.order.line` (extends)

- `name_short` Char (compute=_compute_name_short)
- `shop_warning` Char “Warning”

Public methods: `get_description_following_lines`

Extension points: `_check_validity`, `_get_cart_display_price`, `_get_combination_name`, `_get_displayed_quantity`, `_get_displayed_unit_price`, `_get_line_header`, `_get_order_date`, `_get_selected_combo_items`, `_get_shop_warning`

## `theme.utils` (extends)


Public methods: `enable_view`

## `website` (extends)

- `salesperson_id` Many2one → `res.users` “Salesperson”
- `salesteam_id` Many2one → `crm.team` “Sales Team”
- `show_line_subtotals_tax_selection` Selection “Line Subtotals Tax Display” (store, compute=_compute_show_line_subtotals_tax_selection)
- `add_to_cart_action` Selection
- `auth_signup_uninvited` Selection
- `account_on_checkout` Selection “Customer Accounts”
- `cart_recovery_mail_template_id` Many2one → `mail.template` “Cart Recovery Email”
- `contact_us_button_url` Char “Contact Us Button URL”
- `cart_abandoned_delay` Float “Abandoned Delay”
- `send_abandoned_cart_email` Boolean “Send email to customers who abandoned their cart.”
- `send_abandoned_cart_email_activation_time` Datetime “Time when the 'Send abandoned cart email' feature was activated.” (store, compute=_compute_send_abandoned_cart_email_activation_time)
- `shop_page_container` Selection
- `shop_ppg` Integer “Number of products in the grid on the shop”
- `shop_ppr` Integer “Number of grid columns on the shop”
- `shop_gap` Char “Grid-gap on the shop”
- `shop_opt_products_design_classes` Char “Shop Design Class”
- `shop_default_sort` Selection (required)
- `shop_extra_field_ids` One2many → `website.sale.extra.field` “E-Commerce Extra Fields”
- `product_page_container` Selection
- `product_page_cols_order` Selection “Product Page main columns order”
- `product_page_image_layout` Selection (required)
- `product_page_image_width` Selection (required)
- `product_page_image_spacing` Selection (required)
- `product_page_image_roundness` Selection (required)
- `product_page_image_ratio` Selection (required)
- `product_page_image_ratio_mobile` Selection (required)
- `ecommerce_access` Selection (required)
- `product_page_grid_columns` Integer
- `prevent_zero_price_sale` Boolean “Hide 'Add To Cart' when price = 0”
- `enabled_gmc_src` Boolean “Google Merchant Center”
- `currency_id` Many2one → `res.currency` “Default Currency” (compute=_compute_currency_id)
- `pricelist_ids` One2many → `product.pricelist` “Price list available for this Ecommerce/Website” (compute=_compute_pricelist_ids)
- `confirmation_email_template_id` Many2one → `mail.template`

Public methods: `action_dashboard_redirect`, `configurator_addons_apply`, `configurator_apply`, `create`, `get_configurator_product_page_styles`, `get_configurator_shop_page_styles`, `get_pricelist_available`, `get_suggested_controllers`, `has_ecommerce_access`, `is_pricelist_available`, `sale_product_domain`, `sale_reset`

Extension points: `_create_cart`, `_create_checkout_steps`, `_get_allowed_steps_domain`, `_get_and_cache_current_cart`, `_get_and_cache_current_fiscal_position`, `_get_and_cache_current_pricelist`, `_get_basic_feed_product_domain`, `_get_canonical_url`, `_get_checkout_step`, `_get_checkout_step_values`, `_get_checkout_steps`, `_get_geoip_country_code`, `_get_pl_partner_order`, `_get_product_image_ratio`, `_get_product_image_ratio_height`, `_get_product_page_container`, `_get_product_page_grid_image_rounded_classes`, `_get_product_page_grid_image_spacing_classes`, `_get_product_page_proportions`, `_get_product_sort_mapping`, `_get_snippet_defaults`, `_prepare_sale_order_values`

## `website.base.unit` (defines)

Unit of Measure for price per unit on eCommerce products.

- `name` Char (required)

## `website.checkout.step` (defines)

Website Checkout Step

Inherits: `website.published.multi.mixin`

- `name` Char (required)
- `sequence` Integer
- `step_href` Char “Href” (required)
- `main_button_label` Char
- `back_button_label` Char
- `website_id` Many2one → `website`

Extension points: `_get_next_checkout_step`, `_get_previous_checkout_step`

## `website.menu` (extends)


## `website.page` (extends)


Extension points: `_post_process_response_from_cache`

## `website.sale.extra.field` (defines)

E-Commerce Extra Info Shown on product page

- `website_id` Many2one → `website`
- `sequence` Integer
- `field_id` Many2one → `ir.model.fields` (required)
- `label` Char (related=field_id.field_description)
- `name` Char (related=field_id.name)

## `website.snippet.filter` (extends)

- `product_cross_selling` Boolean “About cross selling products”

Public methods: `default_get`

Extension points: `_get_hardcoded_sample`, `_get_products`, `_get_products_accessories`, `_get_products_alternative_products`, `_get_products_latest_sold`, `_get_products_latest_viewed`, `_get_products_recently_sold_with`, `_get_website_currency`, `_prepare_category_list_data`, `_prepare_values`

## `website.track` (extends)

- `product_id` Many2one → `product.product` (readonly)

## `website.visitor` (extends)

- `visitor_product_count` Integer “Product Views” (compute=_compute_product_statistics)
- `product_ids` Many2many → `product.product` “Visited Products” (compute=_compute_product_statistics)
- `product_count` Integer “Products Views” (compute=_compute_product_statistics)

## `sale.report` (extends)

- `website_id` Many2one → `website` (readonly)
- `is_abandoned_cart` Boolean “Abandoned Cart” (readonly)
- `public_categ_ids` Many2many “eCommerce Categories” (related=product_tmpl_id.public_categ_ids)
