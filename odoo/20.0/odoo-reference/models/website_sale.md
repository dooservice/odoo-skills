# website_sale — eCommerce

Depends on: website, sale, website_payment, website_mail, portal_rating, digest, delivery, html_builder.

## `account.move` (extends)

- `website_id` Many2one → `website` (readonly)

Public methods: `preview_invoice`

## `crm.team` (extends)

- `website_ids` One2many → `website` “Websites”
- `abandoned_carts_amount` Integer “Amount of Abandoned Carts” (compute=_compute_abandoned_carts)
- `abandoned_carts_count` Integer “Number of Abandoned Carts” (compute=_compute_abandoned_carts)

Public methods: `get_abandoned_carts`

## `delivery.carrier` (extends)

Inherits: `website.published.multi.mixin`

- `website_description` Text “Description for Online Quotations” (related=product_id.description_sale)
- `enable_delivery_estimate` Boolean “Estimated Delivery”
- `delivery_estimate_lead_days` Integer
- `delivery_estimate_range_days` Integer
- `delivery_calendar_id` Many2one → `resource.calendar`

Public methods: `write`

Extension points: `_get_delivery_estimate_supported_types`, `_get_estimate_delivery_days`

## `digest.digest` (extends)

- `kpi_website_sale_total` Boolean “eCommerce Sales”
- `kpi_website_sale_total_value` Monetary (compute=_compute_kpi_website_sale_total_value)

Extension points: `_get_kpi_custom_settings`

## `ir.http` (extends)


## `ir.module.module` (extends)


## `payment.transaction` (extends)


Extension points: `_get_status_message`

## `product.attribute` (extends)

- `category_id` Many2one → `product.attribute.category` “Category” (index)
- `visibility` Selection
- `preview_variants` Selection “On Product Cards”
- `is_thumbnail_visible` Boolean “Show Thumbnails”
- `external_identifier` Char “External Identifier”

## `product.attribute.category` (defines)

Product Attribute Category

- `name` Char “Category Name” (required)
- `sequence` Integer “Sequence” (index)
- `attribute_ids` One2many → `product.attribute` “Related Attributes”

## `product.combo` (extends)


Extension points: `_get_max_quantity`

## `product.document` (extends)

- `attached_on_sale` Selection

## `product.feed` (defines)

Product Feed

Inherits: `mail.thread`

- `name` Char (required)
- `website_id` Many2one → `website` (required, index)
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

Extension points: `_check_product_limit`, `_get_feed_product_domain`, `_get_feed_products`, `_prepare_gmc_additional_info`, `_prepare_gmc_identifier`, `_prepare_gmc_image_links`, `_prepare_gmc_items`, `_prepare_gmc_price_info`, `_prepare_gmc_stock_info`, `_prepare_gmc_weight_info`

## `product.image` (defines)

Product Image

Inherits: `image.mixin`

- `name` Char “Name” (required)
- `sequence` Integer
- `image_1920` Image
- `product_tmpl_id` Many2one → `product.template` “Product Template” (index)
- `video_url` Char “Video URL”
- `can_image_1024_be_zoomed` Boolean “Can Image 1024 be zoomed” (store, compute=_compute_can_image_1024_be_zoomed)
- `attribute_value_ids` Many2many → `product.template.attribute.value`
- `has_attribute_value` Boolean (store, compute=_compute_has_attribute_value)
- `type` Selection

Public methods: `create`, `unlink`, `write`

Extension points: `_check_valid_video_url`

## `product.pricelist` (extends)

- `website_id` Many2one → `website` “Website”
- `code` Char “Access Code”
- `selectable` Boolean
- `tax_display` Selection “eCommerce Price Display”

Public methods: `create`

Extension points: `_check_websites_in_company`, `_get_partner_pricelist_multi_filter_hook`, `_get_partner_pricelist_multi_search_domain_hook`, `_get_website_pricelists_domain`

## `product.pricelist.item` (extends)


## `product.product` (extends)

Inherits: `website.structured_data.mixin`, `website.trackable.mixin`

- `variant_ribbon_id` Many2one → `product.ribbon` “Variant Ribbon”
- `website_id` Many2one (related=product_tmpl_id.website_id)
- `product_template_image_ids` One2many (related=product_tmpl_id.product_template_image_ids)
- `variant_image_ids` Many2many → `product.image` “Variant Extra Images” (store, compute=_compute_variant_image_ids)
- `website_url` Char “Website URL” (compute=_compute_product_website_url)

Public methods: `action_unschedule`, `create`, `open_website_url`, `website_publish_button`, `write`

Extension points: `_get_all_extra_images_to_display`, `_get_available_uoms`, `_get_combination_info_variant`, `_get_extra_image_1920_urls`, `_get_free_qty`, `_get_image_1024_url`, `_get_image_1920_url`, `_get_images`, `_get_main_uom`, `_get_max_quantity`, `_prepare_categories_for_display`, `_prepare_jsonld_vals`

## `product.public.category` (defines)

Website Product Category

Inherits: `website.seo.metadata`, `website.published.multi.mixin`, `website.located.mixin`, `website.searchable.mixin`, `image.mixin`

- `name` Char (required)
- `cover_image` Image “Cover Image”
- `is_published` Boolean (compute=_compute_is_published)
- `not_in_shop` Boolean “Not in Shop” (store, compute=_compute_not_in_shop)
- `sequence` Integer (index)
- `parent_id` Many2one → `product.public.category` “Parent” (index)
- `child_id` One2many → `product.public.category` “Children Categories”
- `parent_path` Char (index)
- `parents_and_self` Many2many → `product.public.category` (compute=_compute_parents_and_self)
- `product_tmpl_ids` Many2many → `product.template`
- `has_published_products` Boolean (compute=_compute_has_published_products)
- `website_description` Html “Description”
- `website_footer` Html “Category Footer”

Public methods: `get_available_snippet_categories`

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

## `product.stock.notification` (defines)

Product Stock Notification

- `product_id` Many2one → `product.product` (required)
- `partner_id` Many2one → `res.partner` (required)
- `website_id` Many2one → `website` (required)

## `product.tag` (extends)

Inherits: `website.multi.mixin`


## `product.template` (extends)

Inherits: `rating.mixin`, `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`

- `website_description` Html “Description for the website”
- `description_ecommerce` Html “eCommerce Description”
- `dropzone_above_price` Html “Drop Zone Above Price”
- `dropzone_above_specification` Html “Drop Zone Above Specification”
- `alternative_product_ids` Many2many → `product.template` “Alternative Products”
- `accessory_product_ids` Many2many → `product.product` “Accessory Products”
- `suggest_optional_products` Boolean “Suggest Optional Products” (store, compute=_compute_suggest_optional_products)
- `suggest_accessory_products` Boolean “Suggest Accessory Products” (store, compute=_compute_suggest_accessory_products)
- `suggest_alternative_products` Boolean “Suggest Alternative Products” (store, compute=_compute_suggest_alternative_products)
- `suggested_products_last_update` Datetime “Last update of suggested products”
- `website_size_x` Integer “Size X”
- `website_size_y` Integer “Size Y”
- `website_ribbon_id` Many2one → `product.ribbon` “Ribbon”
- `minimum_quantity` Integer “Minimum Quantity”
- `website_sequence` Integer “Website Sequence” (index)
- `public_categ_ids` Many2many → `product.public.category` “Website Product Category”
- `is_published` Boolean (store, compute=_compute_is_published)
- `publish_date` Datetime “Publish Date” (required, store, compute=_compute_publish_date)
- `product_template_image_ids` One2many → `product.image` “Extra Product Media”
- `compare_list_price` Monetary “Compare to Price”
- `variants_default_code` Char (store, compute=_compute_variants_default_code)
- `description` Html
- `description_sale` Text
- `allow_out_of_stock_order` Boolean “Sell when Out-of-Stock”
- `available_threshold` Float “Show Threshold”
- `show_availability` Boolean “Show availability Qty”
- `out_of_stock_message` Html “Out-of-Stock Message”

Public methods: `action_update_suggested_products`, `copy`, `create`, `create_product_variant`, `get_attribute_value_mapping`, `set_sequence_bottom`, `set_sequence_down`, `set_sequence_top`, `set_sequence_up`, `write`

Extension points: `_create_extra_variant_images`, `_get_access_action`, `_get_additional_combination_info`, `_get_additional_configurator_data`, `_get_alternative_product_filter`, `_get_attribute_value_domain`, `_get_attribute_values_from_search_term`, `_get_available_uoms`, `_get_breadcrumb_items`, `_get_combination_info`, `_get_configurator_display_price`, `_get_contextual_pricelist`, `_get_dynamic_attribute_images`, `_get_first_available_combination`, `_get_google_analytics_data`, `_get_google_analytics_list_data_batch`, `_get_image_holder`, `_get_images`, `_get_jsonld_dict`, `_get_main_uom`, `_get_possible_variants_sorted`, `_get_previewed_attribute_values`, `_get_price_before_discount`, `_get_product_page_documents`, `_get_product_types_allow_zero_price`, `_get_product_url`, `_get_products_by_categories`, `_get_products_by_sales`, `_get_ribbon`, `_get_sales_prices`, `_get_suggested_alternatives`, `_get_suggested_optionals_and_accessories`, `_get_suitable_image_size`, `_get_website_accessory_product`, `_get_website_alternative_product`, `_get_website_sale_search_fields`, `_prepare_jsonld_vals`

## `product.template.attribute.line` (extends)


Extension points: `_prepare_categories_for_display`, `_prepare_single_value_for_display`

## `product.template.attribute.value` (extends)


Extension points: `_get_extra_price`

## `product.wishlist` (defines)

Product Wishlist

- `partner_id` Many2one → `res.partner` “Owner”
- `product_id` Many2one → `product.product` “Product” (required)
- `currency_id` Many2one → `res.currency` (readonly, related=website_id.currency_id)
- `pricelist_id` Many2one → `product.pricelist` “Pricelist”
- `price` Monetary “Price”
- `website_id` Many2one → `website` (required, index)
- `active` Boolean (required)

Public methods: `current`

Extension points: `_check_wishlist_from_session`

## `res.company` (extends)

- `free_order_label` Char “Free Order Label”

Extension points: `_get_default_pricelist_vals`

## `res.config.settings` (extends)

- `group_product_price_comparison` Boolean “Comparison Price”
- `group_gmc_feed` Boolean “Google Merchant Center”
- `group_automate_suggested_products` Boolean “Automate suggested products”
- `group_unpublish_out_of_stock` Boolean “Unpublish Out-of-Stock Products”
- `module_website_sale_collect` Boolean “Click & Collect”
- `cart_recovery_mail_template` Many2one (related=website_id.cart_recovery_mail_template_id)
- `cart_abandoned_delay` Float (related=website_id.cart_abandoned_delay)
- `send_abandoned_cart_followup` Boolean (related=website_id.send_abandoned_cart_followup)
- `salesperson_id` Many2one (related=website_id.salesperson_id)
- `salesteam_id` Many2one (related=website_id.salesteam_id)
- `prevent_sale` Boolean (related=website_id.prevent_sale)
- `prevent_sale_for` Selection (related=website_id.prevent_sale_for)
- `prevent_sale_for_categories` Many2many (related=website_id.prevent_sale_for_categories)
- `contact_us_link_url` Char (related=website_id.contact_us_link_url)
- `show_line_subtotals_tax_selection` Selection (related=website_id.show_line_subtotals_tax_selection)
- `confirmation_email_template_id` Many2one (related=website_id.confirmation_email_template_id)
- `send_order_rating_emails` Boolean (related=website_id.send_order_rating_emails)
- `rating_email_delay` Integer (related=website_id.rating_email_delay)
- `rating_email_template_id` Many2one (related=website_id.rating_email_template_id)
- `restricted_uom_ids` Many2many (related=website_id.restricted_uom_ids)
- `journal_id` Many2one (related=website_id.journal_id)
- `website_show_reference_price` Boolean (related=website_id.show_product_reference_price)
- `account_on_checkout` Selection “Customer Accounts” (required, compute=_compute_account_on_checkout)
- `ecommerce_access` Selection (related=website_id.ecommerce_access)
- `default_allow_out_of_stock_order` Boolean “Continue selling when out-of-stock”
- `default_available_threshold` Float “Show Threshold”
- `default_show_availability` Boolean “Show availability Qty”

Public methods: `action_open_product_feeds`, `action_open_sale_mail_templates`, `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `wishlist_ids` One2many → `product.wishlist` “Wishlist”

Public methods: `write`

Extension points: `_get_current_partner`, `_get_frontend_writable_fields`, `_get_order_fiscal_position_recompute_domain`

## `res.users` (extends)


Extension points: `_check_credentials`

## `sale.order` (extends)

Inherits: `website.checkout.alert.mixin`

- `website_id` Many2one → `website` “eCommerce Website” (readonly)
- `assigned_website_id` Many2one → `website` “Website” (store, compute=_compute_assigned_website_id)
- `cart_recovery_email_sent` Boolean “Cart recovery email already sent”
- `website_order_line` One2many → `sale.order.line` “Order Lines displayed on Website” (compute=_compute_website_order_line)
- `amount_delivery` Monetary “Delivery Amount” (compute=_compute_amount_delivery)
- `cart_quantity` Integer “Cart Quantity” (compute=_compute_cart_info)
- `only_services` Boolean “Only Services” (compute=_compute_cart_info)
- `is_abandoned_cart` Boolean “Abandoned Cart” (compute=_compute_abandoned_cart)
- `is_rating_email_sent` Boolean “Rating email already sent”

Public methods: `action_confirm`, `action_preview_sale_order`, `action_recovery_email_send`, `create`, `get_base_url`, `retrieve_ecommerce_dashboard`

Extension points: `_check_combo_quantities`, `_create_new_cart_line`, `_get_amount_total_excluding_delivery`, `_get_cart_and_free_qty`, `_get_cart_lines_tracking_info`, `_get_cart_qty`, `_get_cart_recovery_template`, `_get_checkout_delivery_address`, `_get_common_product_lines`, `_get_confirmation_template`, `_get_delivery_methods`, `_get_free_qty`, `_get_lang`, `_get_non_delivery_lines`, `_get_note_url`, `_get_order_line_tracking_data`, `_get_order_tracking_info`, `_get_order_tracking_items`, `_get_order_tracking_lines`, `_get_preferred_delivery_method`, `_get_prevented_sale_lines`, `_get_purchase_tracking_info`, `_get_remaining_minimum_qty`, `_get_update_prices_lines`, `_prepare_invoice`, `_prepare_order_line_update_values`, `_prepare_order_line_values`

## `sale.order.line` (extends)

Inherits: `website.checkout.alert.mixin`

- `name_short` Char (compute=_compute_name_short)
- `is_donation` Boolean (compute=_compute_is_donation)

Public methods: `get_description_following_lines`

Extension points: `_check_availability`, `_check_minimum_qty`, `_check_validity`, `_get_cart_display_price`, `_get_combination_name`, `_get_displayed_quantity`, `_get_displayed_unit_price`, `_get_line_header`, `_get_max_available_qty`, `_get_max_line_qty`, `_get_minimum_line_quantity`, `_get_minimum_qty_reached_message`, `_get_order_date`, `_get_selected_combo_items`, `_get_shop_warning_minimum_qty`, `_get_shop_warning_stock`

## `theme.utils` (extends)


Public methods: `enable_view`

## `website` (extends)

- `salesperson_id` Many2one → `res.users` “Salesperson”
- `salesteam_id` Many2one → `crm.team` “Sales Team”
- `show_line_subtotals_tax_selection` Selection “Display Product Prices” (required, store, compute=_compute_show_line_subtotals_tax_selection)
- `auth_signup_uninvited` Selection
- `account_on_checkout` Selection “Customer Accounts”
- `cart_recovery_mail_template_id` Many2one → `mail.template` “Cart Recovery Email”
- `contact_us_link_url` Char “Link URL”
- `cart_abandoned_delay` Float “Abandoned Delay”
- `send_abandoned_cart_followup` Boolean “Send Follow-up”
- `send_abandoned_cart_email_activation_time` Datetime “Time when the 'Send abandoned cart' feature was activated for emails followup.” (store, compute=_compute_send_abandoned_cart_email_activation_time)
- `send_order_rating_emails` Boolean “Request ratings”
- `rating_email_delay` Integer “Days After Order to Send Rating Email”
- `rating_email_template_id` Many2one → `mail.template`
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
- `wishlist_opt_products_design_classes` Char “Wishlist Page Design Class”
- `wishlist_grid_columns` Integer “Wishlist Grid Columns”
- `wishlist_mobile_columns` Integer “Wishlist Mobile Columns”
- `wishlist_gap` Char “Wishlist Grid Gap”
- `prevent_sale` Boolean “Hide Add To Cart”
- `prevent_sale_for` Selection “Prevent Sale For”
- `prevent_sale_for_categories` Many2many → `product.public.category` “Categories”
- `pricelist_ids` One2many → `product.pricelist` “Price list available for this Ecommerce/Website” (compute=_compute_pricelist_ids)
- `confirmation_email_template_id` Many2one → `mail.template`
- `restricted_uom_ids` Many2many → `uom.uom` “Restrict Packagings”
- `journal_id` Many2one → `account.journal` “Default Website Journal”
- `show_product_reference_price` Boolean “Product Reference Price”
- `extra_step_category_ids` Many2many → `product.public.category` “Extra Step Categories”
- `show_category_title` Boolean “Show Category Title”
- `show_category_description` Boolean “Show Category Description”
- `align_category_content` Boolean “Align Category Content”
- `pricelist_id` Many2one → `product.pricelist` (compute=_compute_pricelist_id)
- `currency_id` Many2one → `res.currency` “Default Currency” (compute=_compute_currency_id)
- `tax_display` Selection (compute=_compute_tax_display)

Public methods: `action_dashboard_redirect`, `configurator_addons_apply`, `configurator_apply`, `create`, `get_configurator_product_page_styles`, `get_configurator_shop_page_styles`, `get_cta_data`, `get_pricelist_available`, `get_suggested_controllers`, `has_ecommerce_access`, `is_pricelist_available`, `sale_product_domain`, `sale_reset`, `write`

Extension points: `_create_cart`, `_create_checkout_steps`, `_get_allowed_checkout_steps_domain`, `_get_and_cache_current_cart`, `_get_and_cache_current_fiscal_position`, `_get_and_cache_current_pricelist`, `_get_basic_feed_product_domain`, `_get_breadcrumb_checkout_steps_domain`, `_get_checkout_breadcrumb_steps`, `_get_checkout_step`, `_get_checkout_step_id`, `_get_checkout_step_values`, `_get_contact_us_url`, `_get_geoip_country_code`, `_get_next_breadcrumb_step`, `_get_next_breadcrumb_step_href`, `_get_pl_partner_order`, `_get_previous_breadcrumb_step`, `_get_product_available_qty`, `_get_product_image_ratio_classes`, `_get_product_image_ratio_height`, `_get_product_page_container`, `_get_product_page_grid_image_rounded_classes`, `_get_product_page_grid_image_spacing_classes`, `_get_product_page_proportions`, `_get_product_sort_mapping`, `_get_search_scopes`, `_get_settings_to_copy_onto_new_default_website`, `_get_snippet_defaults`, `_prepare_sale_order_values`

## `website.checkout.alert.mixin` (defines)

Website Checkout Alert Mixin

- `alerts` Json

Extension points: `_get_alerts`, `_get_max_alert_level`

## `website.checkout.step` (defines)

Website Checkout Step

Inherits: `website.published.multi.mixin`

- `name` Char (required)
- `sequence` Integer
- `step_href` Char “Href” (required)
- `main_button_label` Char
- `back_button_label` Char
- `website_id` Many2one → `website`
- `show_in_breadcrumb` Boolean

Public methods: `validate_checkout_progress`

Extension points: `_check_shop_address_completion`, `_check_shop_cart_completion`, `_check_shop_checkout_completion`, `_check_shop_payment_completion`, `_get_next_steps`, `_get_previous_steps`, `_get_step_by_href`

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

## `withdrawal.request` (defines)

Withdrawal Request

- `email` Char “Your Email” (required)
- `order_reference` Char (store, related=order_id.name)
- `order_id` Many2one → `sale.order` “Order” (required, index)
- `recipient_emails` Char “Recipient Emails”
- `log_message` Text “Message”

Public methods: `create`, `website_form_input_filter`

## `sale.report` (extends)

- `website_id` Many2one → `website` (readonly)
- `is_abandoned_cart` Boolean “Abandoned Cart” (readonly)
- `public_categ_ids` Many2many “eCommerce Categories” (related=product_tmpl_id.public_categ_ids)
