# l10n_pe_pos — Peruvian - Point of Sale with Pe Doc

Depends on: l10n_pe, point_of_sale.

## `l10n_pe.res.city.district` (extends)

Inherits: `pos.load.mixin`

- `country_id` Many2one (related=city_id.country_id)
- `state_id` Many2one (related=city_id.state_id)

## `pos.config` (extends)


Public methods: `get_limited_partners_loading`

## `pos.session` (extends)


## `res.city` (extends)

Inherits: `pos.load.mixin`


## `res.partner` (extends)


## `pos.order.receipt` (extends)


Public methods: `order_receipt_generate_data`
