# l10n_ar_website_sale — Argentinean eCommerce

Depends on: website_sale, l10n_ar.

## `product.template` (extends)


Extension points: `_get_additional_combination_info`, `_get_sales_prices`

## `res.config.settings` (extends)

- `l10n_ar_website_sale_show_both_prices` Boolean (related=website_id.l10n_ar_website_sale_show_both_prices)

## `website` (extends)

- `l10n_ar_website_sale_show_both_prices` Boolean “Display Price without National Taxes” (store, compute=_compute_l10n_ar_website_sale_show_both_prices)
