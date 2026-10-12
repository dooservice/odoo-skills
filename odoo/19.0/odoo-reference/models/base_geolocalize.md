# base_geolocalize — Partners Geolocation

Depends on: base_setup.

## `base.geo_provider` (defines)

Geo Provider

- `tech_name` Char “Technical Name”
- `name` Char

## `base.geocoder` (defines)

Geo Coder


Public methods: `geo_find`, `geo_query_address`

Extension points: `_get_localisation`, `_get_provider`

## `res.config.settings` (extends)

- `geoloc_provider_id` Many2one → `base.geo_provider` “API”
- `geoloc_provider_techname` Char (readonly, related=geoloc_provider_id.tech_name)
- `geoloc_provider_googlemap_key` Char “Google Map API Key”

## `res.partner` (extends)

- `date_localization` Date “Geolocation Date”

Public methods: `geo_localize`, `write`
