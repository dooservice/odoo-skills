# delivery_mondialrelay — delivery_mondialrelay

Depends on: delivery.

## `delivery.carrier` (extends)

- `is_mondialrelay` Boolean (compute=_compute_is_mondialrelay)
- `mondialrelay_brand` Char “Brand Code”
- `mondialrelay_packagetype` Char

Public methods: `base_on_rule_get_tracking_link`, `fixed_get_tracking_link`

## `res.partner` (extends)

- `is_mondialrelay` Boolean (compute=_compute_is_mondialrelay)

## `sale.order` (extends)


Public methods: `action_confirm`

## `choose.delivery.carrier` (extends)

- `shipping_zip` Char (related=order_id.partner_shipping_id.zip)
- `shipping_country_code` Char (related=order_id.partner_shipping_id.country_id.code)
- `is_mondialrelay` Boolean (compute=_compute_is_mondialrelay)
- `mondialrelay_last_selected` Char “Last Relay Selected”
- `mondialrelay_last_selected_id` Char (compute=_compute_mr_last_selected_id)
- `mondialrelay_brand` Char (related=carrier_id.mondialrelay_brand)
- `mondialrelay_colLivMod` Char (related=carrier_id.mondialrelay_packagetype)
- `mondialrelay_allowed_countries` Char (compute=_compute_mr_allowed_countries)

Public methods: `button_confirm`
