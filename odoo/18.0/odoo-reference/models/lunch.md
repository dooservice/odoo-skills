# lunch — Lunch

Depends on: mail.

## `lunch.alert` (defines)

Lunch Alert

- `name` Char “Alert Name” (required)
- `message` Html “Message” (required)
- `mode` Selection “Display”
- `recipients` Selection “Recipients”
- `notification_time` Float “Notification Time”
- `notification_moment` Selection (required)
- `tz` Selection “Timezone” (required)
- `cron_id` Many2one → `ir.cron` (required, readonly)
- `until` Date “Show Until”
- `mon` Boolean
- `tue` Boolean
- `wed` Boolean
- `thu` Boolean
- `fri` Boolean
- `sat` Boolean
- `sun` Boolean
- `available_today` Boolean “Is Displayed Today” (compute=_compute_available_today)
- `active` Boolean “Active”
- `location_ids` Many2many → `lunch.location` “Location”

Public methods: `create`, `unlink`, `write`

## `lunch.cashmove` (defines)

Lunch Cashmove

- `currency_id` Many2one → `res.currency` (required)
- `user_id` Many2one → `res.users`
- `date` Date “Date” (required)
- `amount` Float “Amount” (required)
- `description` Text “Description”

Public methods: `get_wallet_balance`

## `lunch.location` (defines)

Lunch Locations

- `name` Char “Location Name” (required)
- `address` Text “Address”
- `company_id` Many2one → `res.company`

## `lunch.order` (defines)

Lunch Order

- `name` Char “Product Name” (readonly, related=product_id.name)
- `topping_ids_1` Many2many → `lunch.topping` “Extras 1”
- `topping_ids_2` Many2many → `lunch.topping` “Extras 2”
- `topping_ids_3` Many2many → `lunch.topping` “Extras 3”
- `product_id` Many2one → `lunch.product` “Product” (required)
- `category_id` Many2one “Product Category” (store, related=product_id.category_id)
- `date` Date “Order Date” (required)
- `supplier_id` Many2one “Vendor” (store, index, related=product_id.supplier_id)
- `available_today` Boolean (related=supplier_id.available_today)
- `available_on_date` Boolean (compute=_compute_available_on_date)
- `order_deadline_passed` Boolean (compute=_compute_order_deadline_passed)
- `user_id` Many2one → `res.users`
- `lunch_location_id` Many2one → `lunch.location`
- `note` Text “Notes”
- `price` Monetary “Total Price” (readonly, store, compute=_compute_total_price)
- `active` Boolean “Active”
- `state` Selection (readonly, index)
- `notified` Boolean
- `company_id` Many2one → `res.company`
- `currency_id` Many2one (store, related=company_id.currency_id)
- `quantity` Float “Quantity” (required)
- `display_toppings` Text “Extras” (store, compute=_compute_display_toppings)
- `product_description` Html “Description” (related=product_id.description)
- `topping_label_1` Char (related=product_id.supplier_id.topping_label_1)
- `topping_label_2` Char (related=product_id.supplier_id.topping_label_2)
- `topping_label_3` Char (related=product_id.supplier_id.topping_label_3)
- `topping_quantity_1` Selection (related=product_id.supplier_id.topping_quantity_1)
- `topping_quantity_2` Selection (related=product_id.supplier_id.topping_quantity_2)
- `topping_quantity_3` Selection (related=product_id.supplier_id.topping_quantity_3)
- `image_1920` Image (compute=_compute_product_images)
- `image_128` Image (compute=_compute_product_images)
- `available_toppings_1` Boolean (compute=_compute_available_toppings)
- `available_toppings_2` Boolean (compute=_compute_available_toppings)
- `available_toppings_3` Boolean (compute=_compute_available_toppings)
- `display_reorder_button` Boolean (compute=_compute_display_reorder_button)
- `display_add_button` Boolean (compute=_compute_display_add_button)

Public methods: `action_cancel`, `action_confirm`, `action_notify`, `action_order`, `action_reorder`, `action_reset`, `action_send`, `add_to_cart`, `create`, `init`, `update_quantity`, `write`

Extension points: `_check_topping_quantity`, `_check_wallet`, `_get_topping_ids`

## `lunch.product` (defines)

Lunch Product

Inherits: `image.mixin`

- `name` Char “Product Name” (required)
- `category_id` Many2one → `lunch.product.category` (required)
- `description` Html “Description”
- `price` Float “Price” (required)
- `supplier_id` Many2one → `lunch.supplier` (required)
- `active` Boolean
- `company_id` Many2one → `res.company` (store, related=supplier_id.company_id)
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `new_until` Date “New Until”
- `is_new` Boolean (compute=_compute_is_new)
- `favorite_user_ids` Many2many → `res.users`
- `is_favorite` Boolean (compute=_compute_is_favorite)
- `last_order_date` Date (compute=_compute_last_order_date)
- `product_image` Image (compute=_compute_product_image)
- `is_available_at` Many2one → `lunch.location` (compute=_compute_is_available_at)

Public methods: `toggle_active`, `write`

## `lunch.product.category` (defines)

Lunch Product Category

Inherits: `image.mixin`

- `name` Char “Product Category” (required)
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `product_count` Integer (compute=_compute_product_count)
- `active` Boolean “Active”
- `image_1920` Image

Public methods: `toggle_active`

## `lunch.supplier` (defines)

Lunch Supplier

Inherits: `mail.thread`, `mail.activity.mixin`

- `partner_id` Many2one → `res.partner` “Vendor” (required)
- `name` Char “Name” (related=partner_id.name)
- `email` Char (related=partner_id.email)
- `email_formatted` Char (readonly, related=partner_id.email_formatted)
- `phone` Char (related=partner_id.phone)
- `street` Char (related=partner_id.street)
- `street2` Char (related=partner_id.street2)
- `zip_code` Char (related=partner_id.zip)
- `city` Char (related=partner_id.city)
- `state_id` Many2one → `res.country.state` (related=partner_id.state_id)
- `country_id` Many2one → `res.country` (related=partner_id.country_id)
- `company_id` Many2one → `res.company` (store, related=partner_id.company_id)
- `responsible_id` Many2one → `res.users` “Responsible”
- `send_by` Selection
- `automatic_email_time` Float “Order Time” (required)
- `cron_id` Many2one → `ir.cron` (required, readonly)
- `mon` Boolean
- `tue` Boolean
- `wed` Boolean
- `thu` Boolean
- `fri` Boolean
- `sat` Boolean
- `sun` Boolean
- `recurrency_end_date` Date “Until”
- `available_location_ids` Many2many → `lunch.location` “Location”
- `available_today` Boolean “This is True when if the supplier is available today” (compute=_compute_available_today)
- `order_deadline_passed` Boolean (compute=_compute_order_deadline_passed)
- `tz` Selection “Timezone” (required)
- `active` Boolean
- `moment` Selection (required)
- `delivery` Selection
- `topping_label_1` Char “Extra 1 Label” (required)
- `topping_label_2` Char “Extra 2 Label” (required)
- `topping_label_3` Char “Extra 3 Label” (required)
- `topping_ids_1` One2many → `lunch.topping`
- `topping_ids_2` One2many → `lunch.topping`
- `topping_ids_3` One2many → `lunch.topping`
- `topping_quantity_1` Selection (required)
- `topping_quantity_2` Selection (required)
- `topping_quantity_3` Selection (required)
- `show_order_button` Boolean (compute=_compute_buttons)
- `show_confirm_button` Boolean (compute=_compute_buttons)

Public methods: `action_confirm_orders`, `action_send_orders`, `create`, `toggle_active`, `unlink`, `write`

Extension points: `_get_current_orders`

## `lunch.topping` (defines)

Lunch Extras

- `name` Char “Name” (required)
- `company_id` Many2one → `res.company`
- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `price` Monetary “Price” (required)
- `supplier_id` Many2one → `lunch.supplier`
- `topping_category` Integer “Topping Category” (required)

## `res.company` (extends)

- `lunch_minimum_threshold` Float
- `lunch_notify_message` Html

## `res.config.settings` (extends)

- `currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `company_lunch_minimum_threshold` Float “Maximum Allowed Overdraft” (related=company_id.lunch_minimum_threshold)
- `company_lunch_notify_message` Html “Lunch notification message” (related=company_id.lunch_notify_message)

## `res.users` (extends)

- `last_lunch_location_id` Many2one → `lunch.location`
- `favorite_lunch_product_ids` Many2many → `lunch.product`

## `lunch.cashmove.report` (defines)

Cashmoves report

- `id` Integer “ID”
- `amount` Float “Amount”
- `date` Date “Date”
- `currency_id` Many2one → `res.currency` “Currency”
- `user_id` Many2one → `res.users` “User”
- `description` Text “Description”

Public methods: `init`
