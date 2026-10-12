# product_images — Product Images

Depends on: product.

## `ir.cron.trigger` (extends)


Extension points: `_check_image_cron_is_not_already_triggered`

## `product.product` (extends)

- `image_fetch_pending` Boolean

## `res.config.settings` (extends)

- `google_custom_search_key` Char “Google Custom Search API Key”
- `google_pse_id` Char “The identifier of the Google Programmable Search Engine”

## `product.fetch.image.wizard` (defines)

Fetch product images from Google Images based on the product's barcode number.

- `nb_products_selected` Integer “Number of selected products” (readonly)
- `products_to_process` Many2many → `product.product`
- `nb_products_to_process` Integer “Number of products to process” (readonly)
- `nb_products_unable_to_process` Integer “Number of product unprocessable” (readonly)

Public methods: `action_fetch_image`, `default_get`

Extension points: `_get_image_from_url`, `_get_products_to_process`
