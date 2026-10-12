# crm_iap_mine — Lead Generation

Depends on: iap_crm, iap_mail.

## `crm.iap.lead.helpers` (defines)

Helper methods for crm_iap_mine modules


Public methods: `lead_vals_from_response`

## `crm.iap.lead.industry` (defines)

CRM IAP Lead Industry

- `name` Char “Industry” (required)
- `reveal_ids` Char (required)
- `color` Integer “Color Index”
- `sequence` Integer “Sequence”

## `crm.iap.lead.mining.request` (defines)

CRM Lead Mining Request

- `name` Char “Request Number” (required, readonly)
- `state` Selection “Status” (required)
- `lead_number` Integer “Number of Leads” (required)
- `search_type` Selection “Target” (required)
- `error_type` Selection “Error Type” (readonly)
- `lead_type` Selection “Type” (required)
- `display_lead_label` Char (compute=_compute_display_lead_label)
- `team_id` Many2one → `crm.team` “Sales Team” (store, compute=_compute_team_id)
- `user_id` Many2one → `res.users` “Salesperson”
- `tag_ids` Many2many → `crm.tag` “Tags”
- `lead_ids` One2many → `crm.lead` “Generated Lead / Opportunity”
- `lead_count` Integer “Number of Generated Leads” (compute=_compute_lead_count)
- `filter_on_size` Boolean “Filter on Size”
- `company_size_min` Integer “Size”
- `company_size_max` Integer
- `country_ids` Many2many → `res.country` “Countries”
- `state_ids` Many2many → `res.country.state` “States”
- `available_state_ids` One2many → `res.country.state` (compute=_compute_available_state_ids)
- `industry_ids` Many2many → `crm.iap.lead.industry` “Industries”
- `contact_number` Integer “Number of Contacts”
- `contact_filter_type` Selection “Filter on”
- `preferred_role_id` Many2one → `crm.iap.lead.role` “Preferred Role”
- `role_ids` Many2many → `crm.iap.lead.role` “Other Roles”
- `seniority_id` Many2one → `crm.iap.lead.seniority` “Seniority”
- `lead_credits` Char (readonly, compute=_compute_tooltip)
- `lead_contacts_credits` Char (readonly, compute=_compute_tooltip)
- `lead_total_credits` Char (readonly, compute=_compute_tooltip)

Public methods: `action_buy_credits`, `action_draft`, `action_get_lead_action`, `action_get_opportunity_action`, `action_submit`, `get_empty_list_help`

Extension points: `_create_leads_from_response`, `_prepare_iap_payload`

## `crm.iap.lead.role` (defines)

People Role

- `name` Char “Role Name” (required)
- `reveal_id` Char (required)
- `color` Integer “Color Index”

Public methods: `name_get`

## `crm.iap.lead.seniority` (defines)

People Seniority

- `name` Char “Name” (required)
- `reveal_id` Char (required)

Public methods: `name_get`

## `crm.lead` (extends)

- `lead_mining_request_id` Many2one → `crm.iap.lead.mining.request` “Lead Mining Request”
