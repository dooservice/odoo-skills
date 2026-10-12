# website_sale — eCommerce

Depends on: website, sale, website_payment, website_mail, portal_rating, digest, delivery.

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


## `payment.token` (extends)


Extension points: `_get_available_tokens`

## `product.attribute` (extends)

- `visibility` Selection

## `product.document` (extends)

- `shown_on_product_page` Boolean “Publish on website”

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

Extension points: `_check_base_unit_count`, `_get_base_unit_price`, `_get_combination_info_variant`, `_get_images`, `_get_mail_message_access`, `_prepare_variant_values`

## `product.public.category` (defines)

Website Product Category

Inherits: `website.seo.metadata`, `website.multi.mixin`, `website.searchable.mixin`, `image.mixin`

- `name` Char (required)
- `sequence` Integer (index)
- `parent_id` Many2one → `product.public.category` “Parent Category” (index)
- `child_id` One2many → `product.public.category` “Children Categories”
- `parent_path` Char (index)
- `parents_and_self` Many2many → `product.public.category` (compute=_compute_parents_and_self)
- `product_tmpl_ids` Many2many → `product.template`
- `website_description` Html “Category Description”
- `website_footer` Html “Category Footer”

Public methods: `check_parent_id`

## `product.ribbon` (defines)

Product ribbon

- `name` Char “Ribbon Name” (required)
- `bg_color` Char “Background Color” (required)
- `text_color` Char “Text Color” (required)
- `position` Selection “Position” (required)

Extension points: `_get_position_class`

## `product.tag` (extends)

Inherits: `website.multi.mixin`

- `visible_on_ecommerce` Boolean “Visible on eCommerce”
- `image` Image “Image”

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
- `product_template_image_ids` One2many → `product.image` “Extra Product Media”
- `base_unit_count` Float “Base Unit Count” (required, store, compute=_compute_base_unit_count)
- `base_unit_id` Many2one → `website.base.unit` “Custom Unit of Measure” (store, compute=_compute_base_unit_id)
- `base_unit_price` Monetary “Price Per Unit” (compute=_compute_base_unit_price)
- `base_unit_name` Char (compute=_compute_base_unit_name)
- `compare_list_price` Monetary “Compare to Price”

Public methods: `create_product_variant`, `set_sequence_bottom`, `set_sequence_down`, `set_sequence_top`, `set_sequence_up`, `write`

Extension points: `_get_access_action`, `_get_additional_configurator_data`, `_get_additionnal_combination_info`, `_get_alternative_product_filter`, `_get_attrib_values_domain`, `_get_base_unit_price`, `_get_combination_info`, `_get_configurator_display_price`, `_get_contextual_pricelist`, `_get_google_analytics_data`, `_get_image_holder`, `_get_images`, `_get_mail_message_access`, `_get_possible_variants_sorted`, `_get_product_types_allow_zero_price`, `_get_sales_prices`, `_get_suitable_image_size`, `_get_website_accessory_product`, `_get_website_alternative_product`, `_prepare_variant_values`

## `product.template.attribute.line` (extends)


Extension points: `_prepare_single_value_for_display`

## `product.template.attribute.value` (extends)


Extension points: `_get_extra_price`

## `res.company` (extends)


Extension points: `_get_default_pricelist_vals`

## `res.config.settings` (extends)

- `group_delivery_invoice_address` Boolean “Shipping Address”
- `group_show_uom_price` Boolean “Base Unit Price”
- `group_product_price_comparison` Boolean “Comparison Price”
- `module_account` Boolean “Invoicing”
- `module_delivery_mondialrelay` Boolean “Mondial Relay Connector”
- `module_website_sale_autocomplete` Boolean “Address Autocomplete”
- `module_website_sale_comparison` Boolean “Product Comparison Tool”
- `module_website_sale_collect` Boolean “Click & Collect”
- `module_website_sale_wishlist` Boolean “Wishlists”
- `add_to_cart_action` Selection (related=website_id.add_to_cart_action)
- `cart_recovery_mail_template` Many2one (related=website_id.cart_recovery_mail_template_id)
- `cart_abandoned_delay` Float (related=website_id.cart_abandoned_delay)
- `send_abandoned_cart_email` Boolean “Abandoned Email” (related=website_id.send_abandoned_cart_email)
- `salesperson_id` Many2one (related=website_id.salesperson_id)
- `salesteam_id` Many2one (related=website_id.salesteam_id)
- `website_sale_prevent_zero_price_sale` Boolean “Prevent Sale of Zero Priced Product” (related=website_id.prevent_zero_price_sale)
- `website_sale_contact_us_button_url` Char “Button Url” (related=website_id.contact_us_button_url)
- `website_sale_enabled_portal_reorder_button` Boolean (related=website_id.enabled_portal_reorder_button)
- `show_line_subtotals_tax_selection` Selection (related=website_id.show_line_subtotals_tax_selection)
- `account_on_checkout` Selection “Customer Accounts” (required, compute=_compute_account_on_checkout)
- `ecommerce_access` Selection (related=website_id.ecommerce_access)
- `enabled_extra_checkout_step` Boolean “Extra Step During Checkout” (store, compute=_compute_checkout_process_steps)
- `enabled_buy_now_button` Boolean “Buy Now” (store, compute=_compute_checkout_process_steps)

Public methods: `action_open_abandoned_cart_mail_template`, `action_open_extra_info`, `action_open_sale_mail_templates`, `set_values`

## `res.partner` (extends)

- `last_website_so_id` Many2one → `sale.order` “Last Online Sales Order” (compute=_compute_last_website_so_id)

Public methods: `write`

## `sale.order` (extends)

- `website_id` Many2one → `website` (readonly)
- `cart_recovery_email_sent` Boolean “Cart recovery email already sent”
- `shop_warning` Char “Warning”
- `website_order_line` One2many → `sale.order.line` “Order Lines displayed on Website” (compute=_compute_website_order_line)
- `amount_delivery` Monetary “Delivery Amount” (compute=_compute_amount_delivery)
- `cart_quantity` Integer “Cart Quantity” (compute=_compute_cart_info)
- `only_services` Boolean “Only Services” (compute=_compute_cart_info)
- `is_abandoned_cart` Boolean “Abandoned Cart” (compute=_compute_abandoned_cart)

Public methods: `action_preview_sale_order`, `action_recovery_email_send`, `create`

Extension points: `_check_cart_is_ready_to_be_paid`, `_get_amount_total_excluding_delivery`, `_get_cart_recovery_template`, `_get_delivery_methods`, `_get_lang`, `_get_non_delivery_lines`, `_get_note_url`, `_get_preferred_delivery_method`, `_get_shop_warning`, `_get_zero_priced_lines`, `_prepare_order_line_update_values`, `_prepare_order_line_values`

## `sale.order.line` (extends)

- `name_short` Char (compute=_compute_name_short)
- `shop_warning` Char “Warning”

Public methods: `get_description_following_lines`

Extension points: `_get_cart_display_price`, `_get_displayed_quantity`, `_get_displayed_unit_price`, `_get_order_date`, `_get_shop_warning`

## `website` (extends)

- `enabled_portal_reorder_button` Boolean “Re-order From Portal”
- `salesperson_id` Many2one → `res.users` “Salesperson”
- `salesteam_id` Many2one → `crm.team` “Sales Team”
- `show_line_subtotals_tax_selection` Selection “Line Subtotals Tax Display” (required)
- `add_to_cart_action` Selection
- `auth_signup_uninvited` Selection
- `account_on_checkout` Selection “Customer Accounts”
- `cart_recovery_mail_template_id` Many2one → `mail.template` “Cart Recovery Email”
- `contact_us_button_url` Char “Contact Us Button URL”
- `cart_abandoned_delay` Float “Abandoned Delay”
- `send_abandoned_cart_email` Boolean “Send email to customers who abandoned their cart.”
- `shop_ppg` Integer “Number of products in the grid on the shop”
- `shop_ppr` Integer “Number of grid columns on the shop”
- `shop_gap` Char “Grid-gap on the shop”
- `shop_default_sort` Selection (required)
- `shop_extra_field_ids` One2many → `website.sale.extra.field` “E-Commerce Extra Fields”
- `product_page_image_layout` Selection (required)
- `product_page_image_width` Selection (required)
- `product_page_image_spacing` Selection (required)
- `ecommerce_access` Selection (required)
- `product_page_grid_columns` Integer
- `prevent_zero_price_sale` Boolean “Hide 'Add To Cart' when price = 0”
- `prevent_zero_price_sale_text` Char “Text to show instead of price”
- `fiscal_position_id` Many2one → `account.fiscal.position` (compute=_compute_fiscal_position_id)
- `pricelist_id` Many2one → `product.pricelist` “Default Pricelist if any” (compute=_compute_pricelist_id)
- `currency_id` Many2one → `res.currency` “Default Currency” (compute=_compute_currency_id)
- `pricelist_ids` One2many → `product.pricelist` “Price list available for this Ecommerce/Website” (compute=_compute_pricelist_ids)
- `all_pricelist_ids` One2many → `product.pricelist` “All pricelists”

Public methods: `action_dashboard_redirect`, `get_pricelist_available`, `get_suggested_controllers`, `has_ecommerce_access`, `is_pricelist_available`, `sale_get_order`, `sale_product_domain`, `sale_reset`

Extension points: `_get_cached_pricelist_id`, `_get_checkout_step_list`, `_get_checkout_steps`, `_get_current_fiscal_position`, `_get_current_pricelist`, `_get_geoip_country_code`, `_get_pl_partner_order`, `_get_product_page_grid_image_spacing_classes`, `_get_product_page_proportions`, `_get_product_sort_mapping`, `_prepare_sale_order_values`

## `website.base.unit` (defines)

Unit of Measure for price per unit on eCommerce products.

- `name` Char (required)

## `website.menu` (extends)


## `website.sale.extra.field` (defines)

E-Commerce Extra Info Shown on product page

- `website_id` Many2one → `website`
- `sequence` Integer
- `field_id` Many2one → `ir.model.fields` (required)
- `label` Char (related=field_id.field_description)
- `name` Char (related=field_id.name)

## `website.snippet.filter` (extends)

- `product_cross_selling` Boolean “About cross selling products”

Extension points: `_get_hardcoded_sample`, `_get_products`, `_get_products_accessories`, `_get_products_alternative_products`, `_get_products_latest_sold`, `_get_products_latest_viewed`, `_get_products_recently_sold_with`, `_get_website_currency`, `_prepare_values`

## `website.track` (extends)

- `product_id` Many2one → `product.product` (readonly)

## `website.visitor` (extends)

- `visitor_product_count` Integer “Product Views” (compute=_compute_product_statistics)
- `product_ids` Many2many → `product.product` “Visited Products” (compute=_compute_product_statistics)
- `product_count` Integer “Products Views” (compute=_compute_product_statistics)

## `sale.report` (extends)

- `website_id` Many2one → `website` (readonly)
- `is_abandoned_cart` Boolean “Abandoned Cart” (readonly)
