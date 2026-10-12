# website_crm_iap_reveal — Lead Generation From Website Visits

Depends on: iap_crm, iap_mail, crm_iap_mine, website_crm.

## `crm.lead` (extends)

- `reveal_ip` Char “IP Address”
- `reveal_iap_credits` Integer “IAP Credits”
- `reveal_rule_id` Many2one → `crm.reveal.rule` “Lead Generation Rule”

## `crm.reveal.rule` (defines)

CRM Lead Generation Rule

- `name` Char “Rule Name” (required)
- `active` Boolean
- `country_ids` Many2many → `res.country` “Countries”
- `website_id` Many2one → `website`
- `state_ids` Many2many → `res.country.state` “States”
- `regex_url` Char “URL Expression”
- `sequence` Integer
- `industry_tag_ids` Many2many → `crm.iap.lead.industry` “Industries”
- `filter_on_size` Boolean “Filter on Size”
- `company_size_min` Integer “Company Size”
- `company_size_max` Integer
- `contact_filter_type` Selection “Filter On” (required)
- `preferred_role_id` Many2one → `crm.iap.lead.role` “Preferred Role”
- `other_role_ids` Many2many → `crm.iap.lead.role` “Other Roles”
- `seniority_id` Many2one → `crm.iap.lead.seniority` “Seniority”
- `extra_contacts` Integer “Number of Contacts”
- `lead_for` Selection “Data Tracking” (required)
- `lead_type` Selection “Type” (required)
- `suffix` Char “Suffix”
- `team_id` Many2one → `crm.team` “Sales Team”
- `tag_ids` Many2many → `crm.tag` “Tags”
- `user_id` Many2one → `res.users` “Salesperson”
- `priority` Selection “Priority”
- `lead_ids` One2many → `crm.lead` “Generated Lead / Opportunity”
- `lead_count` Integer “Number of Generated Leads” (compute=_compute_lead_count)
- `opportunity_count` Integer “Number of Generated Opportunity” (compute=_compute_lead_count)

Public methods: `action_get_lead_tree_view`, `action_get_opportunity_tree_view`

Extension points: `_check_regex_url`, `_create_lead_from_response`, `_get_active_rules`, `_get_reveal_views_to_process`, `_get_rules_payload`, `_prepare_iap_payload`

## `crm.reveal.view` (defines)

CRM Reveal View

- `reveal_ip` Char “IP Address”
- `reveal_rule_id` Many2one → `crm.reveal.rule` “Lead Generation Rule”
- `reveal_state` Selection “State” (index)
- `create_date` Datetime (index)

Extension points: `_create_reveal_view`

## `ir.http` (extends)
