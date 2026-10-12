# partnership — Partnership / Membership

Depends on: crm, sale.

## `product.pricelist` (extends)

- `partners_count` Integer (compute=_compute_partners_count)
- `partners_label` Char (related=company_id.partnership_label)

## `product.template` (extends)

- `service_tracking` Selection
- `grade_id` Many2one → `res.partner.grade` “Assigned Level”

Extension points: `_get_saleable_tracking_types`

## `res.company` (extends)

- `partnership_label` Char

## `res.config.settings` (extends)

- `partnership_label` Char (required, related=company_id.partnership_label)

## `res.partner` (extends)

- `grade_id` Many2one → `res.partner.grade`

Public methods: `write`

## `res.partner.grade` (defines)

Partner Grade

- `sequence` Integer
- `active` Boolean
- `name` Char “Level Name”
- `company_id` Many2one → `res.company`
- `default_pricelist_id` Many2one → `product.pricelist`
- `partners_count` Integer (compute=_compute_partners_count)
- `partners_label` Char (related=company_id.partnership_label)

## `sale.order` (extends)

- `assigned_grade_id` Many2one → `res.partner.grade` (compute=_compute_partnership)

Public methods: `action_confirm`
