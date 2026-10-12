# mail_plugin — Mail Plugin

Depends on: web, contacts, iap.

## `ir.http` (extends)


## `res.partner` (extends)

- `iap_enrich_info` Text “IAP Enrich Info” (compute=_compute_partner_iap_info)
- `iap_search_domain` Char “Search Domain / Email” (compute=_compute_partner_iap_info)

Public methods: `create`, `write`

## `res.partner.iap` (defines)

Partner IAP

- `partner_id` Many2one → `res.partner` “Partner” (required)
- `iap_search_domain` Char “Search Domain / Email”
- `iap_enrich_info` Text “IAP Enrich Info” (readonly)
