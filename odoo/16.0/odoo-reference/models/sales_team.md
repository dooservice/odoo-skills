# sales_team — Sales Teams

Depends on: base, mail.

## `crm.tag` (defines)

CRM Tag

- `name` Char “Tag Name” (required)
- `color` Integer “Color”

Extension points: `_get_default_color`

## `crm.team` (defines)

Sales Team

Inherits: `mail.thread`

- `name` Char “Sales Team” (required)
- `sequence` Integer “Sequence”
- `active` Boolean
- `company_id` Many2one → `res.company` “Company” (index)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, related=company_id.currency_id)
- `user_id` Many2one → `res.users` “Team Leader”
- `is_membership_multi` Boolean “Multiple Memberships Allowed” (compute=_compute_is_membership_multi)
- `member_ids` Many2many → `res.users` “Salespersons” (compute=_compute_member_ids)
- `member_company_ids` Many2many → `res.company` (compute=_compute_member_company_ids)
- `member_warning` Text “Membership Issue Warning” (compute=_compute_member_warning)
- `crm_team_member_ids` One2many → `crm.team.member` “Sales Team Members”
- `crm_team_member_all_ids` One2many → `crm.team.member` “Sales Team Members (incl. inactive)”
- `color` Integer “Color Index”
- `favorite_user_ids` Many2many → `res.users` “Favorite Members”
- `is_favorite` Boolean “Show on dashboard” (compute=_compute_is_favorite)
- `dashboard_button_name` Char “Dashboard Button” (compute=_compute_dashboard_button_name)
- `dashboard_graph_data` Text (compute=_compute_dashboard_graph)

Public methods: `action_primary_channel_button`, `create`, `write`

Extension points: `_get_dashboard_graph_data`, `_get_default_favorite_user_ids`, `_get_default_team_id`

## `crm.team.member` (defines)

Sales Team Member

Inherits: `mail.thread`

- `crm_team_id` Many2one → `crm.team` “Sales Team” (required, index)
- `user_id` Many2one → `res.users` “Salesperson” (required, index)
- `user_in_teams_ids` Many2many → `res.users` (compute=_compute_user_in_teams_ids)
- `user_company_ids` Many2many → `res.company` (compute=_compute_user_company_ids)
- `active` Boolean “Active”
- `is_membership_multi` Boolean “Multiple Memberships Allowed” (compute=_compute_is_membership_multi)
- `member_warning` Text (compute=_compute_member_warning)
- `image_1920` Image “Image” (related=user_id.image_1920)
- `image_128` Image “Image (128)” (related=user_id.image_128)
- `name` Char “Name” (related=user_id.display_name)
- `email` Char “Email” (related=user_id.email)
- `phone` Char “Phone” (related=user_id.phone)
- `mobile` Char “Mobile” (related=user_id.mobile)
- `company_id` Many2one → `res.company` “Company” (related=user_id.company_id)

Public methods: `create`, `write`

## `res.partner` (extends)

- `team_id` Many2one → `crm.team`

## `res.users` (extends)

- `crm_team_ids` Many2many → `crm.team` “Sales Teams” (readonly, compute=_compute_crm_team_ids)
- `crm_team_member_ids` One2many → `crm.team.member` “Sales Team Members”
- `sale_team_id` Many2one → `crm.team` “User Sales Team” (readonly, store, compute=_compute_sale_team_id)
