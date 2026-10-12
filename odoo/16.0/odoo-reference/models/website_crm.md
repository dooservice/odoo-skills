# website_crm — Contact Form

Depends on: website, crm.

## `crm.lead` (extends)

- `visitor_ids` Many2many → `website.visitor` “Web Visitors”
- `visitor_page_count` Integer “# Page Views” (compute=_compute_visitor_page_count)

Public methods: `action_redirect_to_page_views`, `website_form_input_filter`

## `website` (extends)

- `crm_default_team_id` Many2one → `crm.team` “Default Sales Teams”
- `crm_default_user_id` Many2one → `res.users` “Default Salesperson”

Extension points: `_get_crm_default_team_domain`

## `website.visitor` (extends)

- `lead_ids` Many2many → `crm.lead` “Leads”
- `lead_count` Integer “# Leads” (compute=_compute_lead_count)

Extension points: `_check_for_message_composer`, `_prepare_message_composer_context`
