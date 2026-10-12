# event_crm — Event CRM

Depends on: event, crm.

## `crm.lead` (extends)

- `event_lead_rule_id` Many2one → `event.lead.rule` “Registration Rule”
- `event_id` Many2one → `event.event` “Source Event”
- `registration_ids` Many2many → `event.registration` “Source Registrations”
- `registration_count` Integer “# Registrations” (compute=_compute_registration_count)

## `event.event` (extends)

- `lead_ids` One2many → `crm.lead` “Leads”
- `lead_count` Integer “# Leads” (compute=_compute_lead_count)

Public methods: `action_generate_leads`, `action_view_leads`

## `event.lead.request` (defines)

Event Lead Request

- `event_id` Many2one → `event.event` “Event” (required)
- `event_lead_rule_ids` Many2many → `event.lead.rule` “Lead Rules”
- `processed_registration_id` Integer “Processed Registration”

## `event.lead.rule` (defines)

Event Lead Rules

- `name` Char “Rule Name” (required)
- `active` Boolean “Active”
- `lead_ids` One2many → `crm.lead` “Created Leads”
- `lead_creation_basis` Selection “Create” (required)
- `lead_creation_trigger` Selection “When” (required)
- `event_type_ids` Many2many → `event.type` “Event Templates”
- `event_id` Many2one → `event.event` “Event”
- `company_id` Many2one → `res.company` “Company”
- `event_registration_filter` Text “Registrations Domain”
- `lead_type` Selection “Lead Type” (required)
- `lead_sales_team_id` Many2one → `crm.team` “Sales Team”
- `lead_user_id` Many2one → `res.users` “Salesperson”
- `lead_tag_ids` Many2many → `crm.tag` “Tags”

Public methods: `action_execute_rule`

## `event.question.answer` (extends)


Public methods: `action_add_rule_button`

## `event.registration` (extends)

- `lead_ids` Many2many → `crm.lead` “Leads” (readonly)
- `lead_count` Integer “# Leads” (compute=_compute_lead_count)

Public methods: `action_view_leads`, `create`, `write`

Extension points: `_get_lead_contact_fields`, `_get_lead_contact_values`, `_get_lead_description`, `_get_lead_description_fields`, `_get_lead_description_registration`, `_get_lead_grouping`, `_get_lead_tracked_values`, `_get_lead_values`
