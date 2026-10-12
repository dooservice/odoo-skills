# partner_autocomplete — Partner Autocomplete

Depends on: iap_mail.

## `iap.autocomplete.api` (defines)

IAP Partner Autocomplete API


## `ir.http` (extends)


Public methods: `session_info`

## `res.company` (extends)

- `iap_enrich_auto_done` Boolean “Enrich Done”

Public methods: `create`, `iap_enrich_auto`

Extension points: `_get_view`

## `res.config.settings` (extends)

- `partner_autocomplete_insufficient_credit` Boolean “Insufficient credit” (compute=_compute_partner_autocomplete_insufficient_credit)

Public methods: `redirect_to_buy_autocomplete_credit`

## `res.partner` (extends)


Public methods: `action_enrich_partner`, `autocomplete_by_duns`, `autocomplete_by_field`, `autocomplete_by_name`, `autocomplete_by_vat`, `enrich_by_domain`, `enrich_by_duns`, `enrich_by_gst`, `enrich_by_vat`, `enrich_company_message_post`

Extension points: `_get_field_to_check`, `_get_partner_domain`, `_get_view`
