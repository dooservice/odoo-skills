# l10n_it_edi_doi — Italy - Declaration of Intent

Depends on: l10n_it_edi, sale.

## `account.chart.template` (extends)


Extension points: `_get_it_edi_doi_account_fiscal_position`, `_get_it_edi_doi_account_tax`, `_get_it_edi_doi_res_company`

## `account.fiscal.position` (extends)


## `account.move` (extends)

- `l10n_it_edi_doi_date` Date “Date on which Declaration of Intent is applied” (compute=_compute_l10n_it_edi_doi_date)
- `l10n_it_edi_doi_use` Boolean “Use Declaration of Intent” (compute=_compute_l10n_it_edi_doi_use)
- `l10n_it_edi_doi_id` Many2one → `l10n_it_edi_doi.declaration_of_intent` “Declaration of Intent” (store, compute=_compute_l10n_it_edi_doi_id)
- `l10n_it_edi_doi_amount` Monetary “Declaration of Intent Amount” (readonly, store, compute=_compute_l10n_it_edi_doi_amount)
- `l10n_it_edi_doi_warning` Text “Declaration of Intent Threshold Warning” (compute=_compute_l10n_it_edi_doi_warning)

Public methods: `action_open_declaration_of_intent`, `copy_data`

Extension points: `_check_l10n_it_edi_doi_id`

## `account.tax` (extends)


## `l10n_it_edi_doi.declaration_of_intent` (defines)

Declaration of Intent

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`

- `state` Selection “State” (required, readonly)
- `company_id` Many2one → `res.company` “Company” (required, index)
- `partner_id` Many2one → `res.partner` “Partner” (required, index)
- `currency_id` Many2one → `res.currency` “Currency” (required, readonly)
- `issue_date` Date “Date of Issue” (required)
- `start_date` Date “Start Date” (required)
- `end_date` Date “End Date” (required)
- `threshold` Monetary “Threshold” (required)
- `invoiced` Monetary “Invoiced” (readonly, store, compute=_compute_invoiced)
- `not_yet_invoiced` Monetary “Not Yet Invoiced” (readonly, store, compute=_compute_not_yet_invoiced)
- `remaining` Monetary “Remaining” (readonly, store, compute=_compute_remaining)
- `protocol_number_part1` Char “Protocol 1” (required)
- `protocol_number_part2` Char “Protocol 2” (required)
- `invoice_ids` One2many → `account.move` “Invoices / Refunds” (readonly)
- `sale_order_ids` One2many → `sale.order` “Sales Orders / Quotations” (readonly)

Public methods: `action_open_invoice_ids`, `action_open_sale_order_ids`, `action_reactivate`, `action_reset_to_draft`, `action_revoke`, `action_terminate`, `action_validate`

Extension points: `_get_validity_errors`, `_get_validity_warnings`

## `res.company` (extends)

- `l10n_it_edi_doi_tax_id` Many2one → `account.tax` “Declaration of Intent Tax”
- `l10n_it_edi_doi_fiscal_position_id` Many2one → `account.fiscal.position` “Declaration of Intent Fiscal Position”

## `res.partner` (extends)

- `l10n_it_edi_doi_ids` One2many → `l10n_it_edi_doi.declaration_of_intent` “Available Declarations of Intent of this partner”

Public methods: `l10n_it_edi_doi_action_open_declarations`

## `sale.order` (extends)

- `l10n_it_edi_doi_date` Date “Date on which Declaration of Intent is applied” (compute=_compute_l10n_it_edi_doi_date)
- `l10n_it_edi_doi_use` Boolean “Use Declaration of Intent” (compute=_compute_l10n_it_edi_doi_use)
- `l10n_it_edi_doi_id` Many2one → `l10n_it_edi_doi.declaration_of_intent` “Declaration of Intent” (store, compute=_compute_l10n_it_edi_doi_id)
- `l10n_it_edi_doi_not_yet_invoiced` Monetary “Declaration of Intent Amount Not Yet Invoiced” (readonly, store, compute=_compute_l10n_it_edi_doi_not_yet_invoiced)
- `l10n_it_edi_doi_warning` Text “Declaration of Intent Threshold Warning” (compute=_compute_l10n_it_edi_doi_warning)

Public methods: `action_confirm`, `action_open_declaration_of_intent`, `action_quotation_send`, `action_quotation_sent`, `copy_data`

Extension points: `_check_l10n_it_edi_doi_id`, `_prepare_invoice`

## `sale.order.line` (extends)

- `qty_invoiced_posted` Float “Invoiced Quantity (posted)” (store, compute=_compute_qty_invoiced_posted)
