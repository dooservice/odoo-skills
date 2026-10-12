# pos_cache — pos_cache

Depends on: point_of_sale.

## `pos.cache` (defines)

Point of Sale Cache

- `cache` Binary
- `product_domain` Text (required)
- `product_fields` Text (required)
- `config_id` Many2one → `pos.config` (required)
- `compute_user_id` Many2one → `res.users` (required)

Public methods: `cache2json`, `get_product_domain`, `get_product_fields`, `refresh_all_caches`, `refresh_cache`

## `pos.config` (extends)

- `cache_ids` One2many → `pos.cache`
- `oldest_cache_time` Datetime “Oldest cache time” (readonly, compute=_get_oldest_cache_time)
- `limit_products_per_request` Integer (compute=_compute_limit_products_per_request)

Public methods: `delete_cache`

Extension points: `_get_oldest_cache_time`

## `pos.session` (extends)


Public methods: `get_cached_products`, `get_products_from_cache`, `get_total_products_count`

Extension points: `_get_pos_ui_product_product`
