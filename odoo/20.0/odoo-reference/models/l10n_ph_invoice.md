# l10n_ph_invoice — Philippines - Discount Privileges on Invoice

Depends on: l10n_ph.

## `account.move` (extends)

- `l10n_ph_has_discount_privilege` Boolean (compute=_compute_l10n_ph_has_discount_privilege)

Public methods: `action_open_discount_privilege_wizard`

## `account.move.line` (extends)

Inherits: `l10n_ph.discount.privilege.line.mixin`

- `l10n_ph_original_tax_ids` Many2many

## `l10n_ph.discount.privilege` (defines)

Philippines Discount Privilege

- `name` Char “Discount Name” (required)
- `discount_type` Selection “Type” (required)
- `discount_amount` Float “Discount Amount” (required)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position”
- `account_id` Many2one → `account.account` “Account” (required)
- `applied_to_category_ids` Many2many → `product.category` “Applies To”
- `company_id` Many2one → `res.company` (required)
- `active` Boolean “Active”

Extension points: `_check_discount_amount`

## `l10n_ph.discount.privilege.line.mixin` (defines)

Philippine Discount Privilege Line Mixin

- `currency_id` Many2one → `res.currency` “Currency”
- `l10n_ph_discount_privilege_id` Many2one → `l10n_ph.discount.privilege` “Discount Privilege” (readonly)
- `l10n_ph_original_tax_ids` Many2many → `account.tax` “Original Taxes (pre-privilege)” (store)
- `l10n_ph_original_price_unit` Float “Original Price Unit (pre-privilege)” (store)
- `l10n_ph_original_discount` Float “Original Discount (pre-privilege)” (readonly)
- `l10n_ph_regular_discount_amount` Monetary “Regular Disc. Amount” (readonly, compute=_compute_l10n_ph_discount_amounts)
- `l10n_ph_special_discount_amount` Monetary “Special Disc. Amount” (readonly, compute=_compute_l10n_ph_discount_amounts)

## `account.chart.template` (extends)


Extension points: `_get_ph_discount_privileges`

## `l10n_ph.discount.privilege.wizard` (defines)

Discount Privilege Wizard

- `move_id` Many2one → `account.move`
- `company_id` Many2one → `res.company` (readonly, compute=_compute_l10n_ph_document_company_currency)
- `currency_id` Many2one → `res.currency` (readonly, compute=_compute_l10n_ph_document_company_currency)
- `privilege_id` Many2one → `l10n_ph.discount.privilege` “Privilege Applied”
- `apply_on` Selection “Apply On” (required)
- `product_ids` Many2many → `product.product` “Products”
- `category_ids` Many2many → `product.category` “Product Categories”
- `scope_category_ids` Many2many → `product.category` (compute=_compute_scope_category_ids)
- `available_product_ids` Many2many → `product.product` (compute=_compute_available_filters)
- `available_category_ids` Many2many → `product.category` (compute=_compute_available_filters)
- `line_ids` One2many → `l10n_ph.discount.privilege.wizard.line` “Lines”
- `has_applied_privileges` Boolean (compute=_compute_has_applied_privileges)

Public methods: `action_confirm`, `action_remove_all`, `create`

Extension points: `_check_can_modify`, `_check_document_fields`, `_check_scope_inputs`, `_get_document`, `_get_document_fields`, `_get_preview_privilege_for_line`

## `l10n_ph.discount.privilege.wizard.line` (defines)

Discount Privilege Wizard Line

- `wizard_id` Many2one → `l10n_ph.discount.privilege.wizard` (required)
- `invoice_line_id` Many2one → `account.move.line`
- `name` Text “Product” (compute=_compute_name)
- `category_id` Many2one → `product.category` “Product Category” (compute=_compute_category_id)
- `currency_id` Many2one (related=wizard_id.currency_id)
- `has_discount_privilege` Boolean (compute=_compute_preview_fields)
- `has_applied_discount_privilege` Boolean (compute=_compute_preview_fields)
- `remove_discount_privilege` Boolean “Remove Discount Privilege”
- `discount` Float “Discount Applied (%)” (compute=_compute_preview_fields)
- `discount_amount` Monetary “Discount Amount” (compute=_compute_preview_fields)

Public methods: `action_remove_line_discount`

Extension points: `_get_line_source`
