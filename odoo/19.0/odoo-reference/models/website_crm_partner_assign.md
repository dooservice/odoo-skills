# website_crm_partner_assign — Resellers

Depends on: base_geolocalize, crm, account, partnership, website_partner, website_google_map, portal.

## `crm.lead` (extends)

- `partner_latitude` Float “Geo Latitude”
- `partner_longitude` Float “Geo Longitude”
- `partner_assigned_id` Many2one → `res.partner`
- `partner_declined_ids` Many2many → `res.partner` “Partner not interested”
- `date_partner_assign` Date “Partner Assignment Date” (store, compute=_compute_date_partner_assign)

Public methods: `action_assign_partner`, `assign_geo_localize`, `assign_partner`, `assign_salesman_of_assigned_partner`, `create_opp_portal`, `partner_desinterested`, `partner_interested`, `search_geo_partner`, `update_contact_details_from_portal`, `update_lead_portal`, `update_stage_from_portal`, `write`

Extension points: `_get_access_action`, `_get_partner_email_update`, `_get_partner_phone_update`, `_prepare_customer_values`

## `res.partner` (extends)

- `partner_weight` Integer “Level Weight” (store, compute=_compute_partner_weight)
- `grade_sequence` Integer (readonly, store, related=grade_id.sequence)
- `activation` Many2one → `res.partner.activation`
- `date_partnership` Date “Partnership Date”
- `date_review` Date “Latest Review”
- `date_review_next` Date “Next Review”
- `assigned_partner_id` Many2one → `res.partner`
- `implemented_partner_ids` One2many → `res.partner` “Implementation References”
- `implemented_partner_count` Integer (store, compute=_compute_implemented_partner_count)

Public methods: `default_get`

Extension points: `_get_contact_opportunities_domain`

## `res.partner.activation` (defines)

Partner Activation

- `sequence` Integer “Sequence”
- `name` Char “Name” (required)
- `active` Boolean

## `res.partner.grade` (extends)

Inherits: `website.published.mixin`

- `partner_weight` Integer “Level Weight”

## `website` (extends)


Public methods: `get_suggested_controllers`

## `crm.partner.report.assign` (defines)

CRM Partnership Analysis

- `partner_id` Many2one → `res.partner` (readonly)
- `grade_id` Many2one → `res.partner.grade` (readonly)
- `activation` Many2one → `res.partner.activation` (index)
- `user_id` Many2one → `res.users` (readonly)
- `date_review` Date “Latest Partner Review”
- `date_partnership` Date “Partnership Date”
- `country_id` Many2one → `res.country` (readonly)
- `nbr_opportunities` Integer “# of Opportunity” (readonly)
- `turnover` Float “Turnover” (readonly)
- `date` Date “Invoice Account Date” (readonly)

## `crm.lead.forward.to.partner` (defines)

Lead forward to partner

- `forward_type` Selection
- `partner_id` Many2one → `res.partner`
- `assignation_lines` One2many → `crm.lead.assignation`
- `body` Html “Contents”

Public methods: `action_forward`, `default_get`, `get_lead_portal_url`

## `crm.lead.assignation` (defines)

Lead Assignation

- `forward_id` Many2one → `crm.lead.forward.to.partner`
- `lead_id` Many2one → `crm.lead`
- `lead_location` Char “Lead Location”
- `partner_assigned_id` Many2one → `res.partner`
- `partner_location` Char “Partner Location”
- `lead_link` Char “Link to Lead”
