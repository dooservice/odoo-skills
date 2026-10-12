# l10n_pe_pos — Peruvian - Point of Sale with Pe Doc

Depends on: l10n_pe, point_of_sale.

## `l10n_pe.res.city.district` (extends)

- `country_id` Many2one (related=city_id.country_id)
- `state_id` Many2one (related=city_id.state_id)

## `pos.session` (extends)


Extension points: `_get_pos_ui_l10n_latam_identification_type`, `_get_pos_ui_l10n_pe_res_city_district`, `_get_pos_ui_res_city`

## `res.partner` (extends)
