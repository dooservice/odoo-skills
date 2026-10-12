# website_sale — eCommerce

Depends on: website, sale, website_payment, website_mail, portal_rating, digest.

## `account.move` (extends)

- `website_id` Many2one → `website` “Website” (readonly, store, compute=_compute_website_id)

Public methods: `preview_invoice`

## `crm.team` (extends)

- `website_ids` One2many → `website` “Websites”
- `abandoned_carts_count` Integer “Number of Abandoned Carts” (readonly, compute=_compute_abandoned_carts)
- `abandoned_carts_amount` Integer “Amount of Abandoned Carts” (readonly, compute=_compute_abandoned_carts)

Public methods: `get_abandoned_carts`

## `digest.digest` (extends)

- `kpi_website_sale_total` Boolean “eCommerce Sales”
- `kpi_website_sale_total_value` Monetary (compute=_compute_kpi_website_sale_total_value)

## `ir.http` (extends)


## `payment.provider` (extends)


Extension points: `_get_compatible_providers`

## `product.attribute` (extends)

- `visibility` Selection

## `product.template.attribute.line` (extends)


Extension points: `_prepare_single_value_for_display`

## `product.image` (defines)

Product Image

Inherits: `image.mixin`

- `name` Char “Name” (required)
- `sequence` Integer
- `image_1920` Image
- `product_tmpl_id` Many2one → `product.template` (index)
- `product_variant_id` Many2one → `product.product` (index)
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

Extension points: `_check_website_pricelist`, `_check_websites_in_company`, `_get_partner_pricelist_multi_filter_hook`, `_get_partner_pricelist_multi_search_domain_hook`, `_get_website_pricelists_domain`

## `product.product` (extends)

- `website_id` Many2one (related=product_tmpl_id.website_id)
- `product_variant_image_ids` One2many → `product.image` “Extra Variant Images”
- `website_url` Char “Website URL” (compute=_compute_product_website_url)
- `base_unit_count` Float “Base Unit Count” (required)
- `base_unit_id` Many2one → `website.base.unit` “Custom Unit of Measure”
- `base_unit_price` Monetary “Price Per Unit” (compute=_compute_base_unit_price)
- `base_unit_name` Char (compute=_compute_base_unit_name)

Public methods: `open_website_url`, `website_publish_button`

Extension points: `_check_base_unit_count`, `_get_base_unit_price`, `_get_contextual_price_tax_selection`, `_get_images`, `_get_mail_message_access`, `_prepare_variant_values`

## `product.public.category` (defines)

Website Product Category

Inherits: `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `image.mixin`

- `name` Char (required)
- `parent_id` Many2one → `product.public.category` “Parent Category” (index)
- `parent_path` Char (index)
- `child_id` One2many → `product.public.category` “Children Categories”
- `parents_and_self` Many2many → `product.public.category` (compute=_compute_parents_and_self)
- `sequence` Integer (index)
- `website_description` Html “Category Description”
- `product_tmpl_ids` Many2many → `product.template`

Public methods: `check_parent_id`, `name_get`

## `product.ribbon` (defines)

Product ribbon

- `html` Html “Ribbon html” (required)
- `bg_color` Char “Ribbon background color”
- `text_color` Char “Ribbon text color”
- `html_class` Char “Ribbon class” (required)
- `product_tag_ids` One2many → `product.tag` “Product Tags”

Public methods: `name_get`

## `product.tag` (extends)

Inherits: `website.multi.mixin`

- `ribbon_id` Many2one → `product.ribbon` “Ribbon”

## `product.template` (extends)

Inherits: `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `rating.mixin`

- `website_description` Html “Description for the website”
- `alternative_product_ids` Many2many → `product.template` “Alternative Products”
- `accessory_product_ids` Many2many → `product.product` “Accessory Products”
- `website_size_x` Integer “Size X”
- `website_size_y` Integer “Size Y”
- `website_ribbon_id` Many2one → `product.ribbon` “Ribbon”
- `website_sequence` Integer “Website Sequence” (index)
- `public_categ_ids` Many2many → `product.public.category` “Website Product Category”
- `product_template_image_ids` One2many → `product.image` “Extra Product Media”
- `base_unit_count` Float “Base Unit Count” (required, store, compute=_compute_base_unit_count)
- `base_unit_id` Many2one → `website.base.unit` “Custom Unit of Measure” (store, compute=_compute_base_unit_id)
- `base_unit_price` Monetary “Price Per Unit” (compute=_compute_base_unit_price)
- `base_unit_name` Char (compute=_compute_base_unit_name)
- `compare_list_price` Float “Compare to Price”

Public methods: `get_google_analytics_data`, `set_sequence_bottom`, `set_sequence_down`, `set_sequence_top`, `set_sequence_up`

Extension points: `_get_alternative_product_filter`, `_get_base_unit_price`, `_get_combination_info`, `_get_contextual_pricelist`, `_get_current_company_fallback`, `_get_image_holder`, `_get_images`, `_get_mail_message_access`, `_get_possible_variants_sorted`, `_get_product_types_allow_zero_price`, `_get_sales_prices`, `_get_suitable_image_size`, `_get_website_accessory_product`, `_get_website_alternative_product`, `_get_website_ribbon`, `_prepare_variant_values`

## `res.company` (extends)

- `website_sale_onboarding_payment_provider_state` Selection “State of the website sale onboarding payment provider step”

Public methods: `action_open_website_sale_onboarding_payment_provider`

## `res.config.settings` (extends)

- `salesperson_id` Many2one → `res.users` “Salesperson” (related=website_id.salesperson_id)
- `salesteam_id` Many2one → `crm.team` “Sales Team” (related=website_id.salesteam_id)
- `module_website_sale_delivery` Boolean (store, compute=_compute_module_delivery)
- `sale_delivery_settings` Selection “Shipping Management”
- `group_delivery_invoice_address` Boolean “Shipping Address”
- `group_show_uom_price` Boolean “Base Unit Price”
- `group_product_price_comparison` Boolean “Comparison Price”
- `module_website_sale_digital` Boolean “Digital Content”
- `module_website_sale_wishlist` Boolean “Wishlists”
- `module_website_sale_comparison` Boolean “Product Comparison Tool”
- `module_website_sale_autocomplete` Boolean “Address Autocomplete”
- `module_account` Boolean “Invoicing”
- `module_website_sale_picking` Boolean “On Site Payments & Picking”
- `cart_recovery_mail_template` Many2one → `mail.template` “Cart Recovery Email” (related=website_id.cart_recovery_mail_template_id)
- `cart_abandoned_delay` Float “Send After” (related=website_id.cart_abandoned_delay)
- `send_abandoned_cart_email` Boolean “Abandoned Email” (related=website_id.send_abandoned_cart_email)
- `add_to_cart_action` Selection (related=website_id.add_to_cart_action)
- `terms_url` Char “URL” (compute=_compute_terms_url)
- `module_delivery` Boolean (store, compute=_compute_module_delivery)
- `module_delivery_mondialrelay` Boolean “Mondial Relay Connector”
- `group_product_pricelist` Boolean (store, compute=_compute_group_product_pricelist)
- `enabled_extra_checkout_step` Boolean “Extra Step During Checkout” (store, compute=_compute_checkout_process_steps)
- `enabled_buy_now_button` Boolean “Buy Now” (store, compute=_compute_checkout_process_steps)
- `account_on_checkout` Selection “Customer Accounts” (required, compute=_compute_account_on_checkout)
- `website_sale_prevent_zero_price_sale` Boolean “Prevent Sale of Zero Priced Product” (related=website_id.prevent_zero_price_sale)
- `website_sale_contact_us_button_url` Char “Button URL” (related=website_id.contact_us_button_url)
- `website_sale_enabled_portal_reorder_button` Boolean “Re-order From Portal” (related=website_id.enabled_portal_reorder_button)

Public methods: `action_open_abandoned_cart_mail_template`, `action_open_extra_info`, `action_open_sale_mail_templates`, `action_update_terms`, `get_values`, `set_values`

## `res.country` (extends)


Public methods: `get_website_sale_countries`, `get_website_sale_states`

## `res.partner` (extends)

- `last_website_so_id` Many2one → `sale.order` “Last Online Sales Order” (compute=_compute_last_website_so_id)

Public methods: `write`

## `sale.order` (extends)

- `website_order_line` One2many → `sale.order.line` “Order Lines displayed on Website” (compute=_compute_website_order_line)
- `cart_quantity` Integer “Cart Quantity” (compute=_compute_cart_info)
- `only_services` Boolean “Only Services” (compute=_compute_cart_info)
- `is_abandoned_cart` Boolean “Abandoned Cart” (compute=_compute_abandoned_cart)
- `cart_recovery_email_sent` Boolean “Cart recovery email already sent”
- `website_id` Many2one → `website` “Website” (readonly)
- `shop_warning` Char “Warning”

Public methods: `action_confirm`, `action_preview_sale_order`, `action_recovery_email_send`, `create`

Extension points: `_get_cart_recovery_template`, `_get_lang`, `_get_note_url`, `_get_shop_warning`, `_get_website_sale_extra_values`, `_prepare_order_line_update_values`, `_prepare_order_line_values`

## `sale.order.line` (extends)

- `linked_line_id` Many2one → `sale.order.line` “Linked Order Line” (index)
- `option_line_ids` One2many → `sale.order.line` “Options Linked”
- `name_short` Char (compute=_compute_name_short)
- `shop_warning` Char “Warning”

Public methods: `get_description_following_lines`

Extension points: `_get_order_date`, `_get_sale_order_line_multiline_description_sale`, `_get_shop_warning`

## `website` (extends)

- `salesperson_id` Many2one → `res.users` “Salesperson”
- `salesteam_id` Many2one → `crm.team` “Sales Team”
- `pricelist_id` Many2one → `product.pricelist` “Default Pricelist” (compute=_compute_pricelist_id)
- `currency_id` Many2one “Default Currency” (related=pricelist_id.currency_id)
- `pricelist_ids` One2many → `product.pricelist` “Price list available for this Ecommerce/Website” (compute=_compute_pricelist_ids)
- `all_pricelist_ids` One2many → `product.pricelist` “All pricelists”
- `cart_recovery_mail_template_id` Many2one → `mail.template` “Cart Recovery Email”
- `cart_abandoned_delay` Float “Abandoned Delay”
- `send_abandoned_cart_email` Boolean “Send email to customers who abandoned their cart.”
- `shop_ppg` Integer “Number of products in the grid on the shop”
- `shop_ppr` Integer “Number of grid columns on the shop”
- `shop_default_sort` Selection (required)
- `shop_extra_field_ids` One2many → `website.sale.extra.field` “E-Commerce Extra Fields”
- `add_to_cart_action` Selection
- `auth_signup_uninvited` Selection
- `account_on_checkout` Selection “Customer Accounts”
- `product_page_image_layout` Selection (required)
- `product_page_grid_columns` Integer
- `product_page_image_width` Selection (required)
- `product_page_image_spacing` Selection (required)
- `prevent_zero_price_sale` Boolean “Hide 'Add To Cart' when price = 0”
- `prevent_zero_price_sale_text` Char “Text to show instead of price”
- `contact_us_button_url` Char “Contact Us Button URL”
- `enabled_portal_reorder_button` Boolean “Re-order From Portal”

Public methods: `action_dashboard_redirect`, `get_current_pricelist`, `get_pricelist_available`, `get_suggested_controllers`, `is_pricelist_available`, `sale_get_order`, `sale_get_payment_term`, `sale_product_domain`, `sale_reset`

Extension points: `_get_cached_pricelist_id`, `_get_current_fiscal_position_id`, `_get_current_pricelist_id`, `_get_geoip_country_code`, `_get_pl_partner_order`, `_get_product_page_grid_image_classes`, `_get_product_page_proportions`, `_get_product_sort_mapping`, `_prepare_sale_order_values`

## `website.sale.extra.field` (defines)

E-Commerce Extra Info Shown on product page

- `website_id` Many2one → `website`
- `sequence` Integer
- `field_id` Many2one → `ir.model.fields` (required)
- `label` Char (related=field_id.field_description)
- `name` Char (related=field_id.name)

## `website.base.unit` (defines)

Unit of Measure for price per unit on eCommerce products.

- `name` Char (required)

## `website.snippet.filter` (extends)

- `product_cross_selling` Boolean “About cross selling products”

Extension points: `_get_hardcoded_sample`, `_get_products`, `_get_products_accessories`, `_get_products_alternative_products`, `_get_products_latest_sold`, `_get_products_latest_viewed`, `_get_products_recently_sold_with`, `_get_website_currency`

## `website.track` (extends)

- `product_id` Many2one → `product.product` (readonly)

## `website.visitor` (extends)

- `visitor_product_count` Integer “Product Views” (compute=_compute_product_statistics)
- `product_ids` Many2many → `product.product` “Visited Products” (compute=_compute_product_statistics)
- `product_count` Integer “Products Views” (compute=_compute_product_statistics)

## `sale.report` (extends)

- `website_id` Many2one → `website` (readonly)

## `mail.compose.message` (extends)


Extension points: `_action_send_mail`
