# base_address_extended — Extended Addresses

Depends on: web.

## `res.city` (defines)

City

- `name` Char “Name” (required)
- `zipcode` Char “Zip”
- `country_id` Many2one → `res.country` “Country” (required, index)
- `country_code` Char (related=country_id.code)
- `state_id` Many2one → `res.country.state` “State”

## `res.country` (extends)

- `enforce_cities` Boolean “Enforce Cities”

## `res.partner` (extends)

- `street_name` Char “Street Name” (store, compute=_compute_street_data)
- `street_number` Char “House” (store, compute=_compute_street_data)
- `street_number2` Char “Door” (store, compute=_compute_street_data)
- `city_id` Many2one → `res.city` “City ID”
- `country_enforce_cities` Boolean (related=country_id.enforce_cities)

Extension points: `_get_res_city_by_name`, `_get_street_split`
