# partner_autocomplete — Partner Autocomplete

Depends on: iap_mail.

## `iap.autocomplete.api` (defines)

IAP Partner Autocomplete API


## `ir.http` (extends)


Public methods: `session_info`

## `res.company` (extends)

- `partner_gid` Integer “Company database ID” (store, related=partner_id.partner_gid)
- `iap_enrich_auto_done` Boolean “Enrich Done”

Public methods: `create`, `iap_enrich_auto`

Extension points: `_get_company_domain`, `_get_view`

## `res.config.settings` (extends)

- `partner_autocomplete_insufficient_credit` Boolean “Insufficient credit” (compute=_compute_partner_autocomplete_insufficient_credit)

Public methods: `redirect_to_buy_autocomplete_credit`

## `res.partner` (extends)

- `partner_gid` Integer “Company database ID”
- `additional_info` Char “Additional info”

Public methods: `autocomplete`, `autocomplete_by_name`, `autocomplete_by_vat`, `check_gst_in`, `enrich_by_domain`, `enrich_by_duns`, `enrich_by_gst`, `enrich_company`, `enrich_company_message_post`, `iap_partner_autocomplete_add_tags`, `read_by_vat`

Extension points: `_get_view`

## `res.partner.autocomplete.sync` (defines)

Partner Autocomplete Sync

- `partner_id` Many2one → `res.partner` “Partner”
- `synched` Boolean “Is synched”

Public methods: `add_to_queue`, `start_sync`
