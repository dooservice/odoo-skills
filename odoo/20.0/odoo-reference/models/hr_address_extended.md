# hr_address_extended — HR Address Extended

Depends on: hr, base_address_extended.

## `hr.employee` (extends)


## `hr.version` (extends)

- `private_city_id` Many2one → `res.city` “Private City ID” (store, compute=_compute_private_city_id)
- `private_country_enforce_cities` Boolean (readonly, related=private_country_id.enforce_cities)
