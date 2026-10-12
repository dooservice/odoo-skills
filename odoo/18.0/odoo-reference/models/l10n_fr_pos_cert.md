# l10n_fr_pos_cert — France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis)

Depends on: l10n_fr_account, point_of_sale.

## `account.sale.closing` (defines)

Sale Closing

- `name` Char (required)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `date_closing_stop` Datetime “Closing Date” (required, readonly)
- `date_closing_start` Datetime “Starting Date” (required, readonly)
- `frequency` Selection “Closing Type” (required, readonly)
- `total_interval` Monetary “Period Total” (required, readonly)
- `cumulative_total` Monetary “Cumulative Grand Total” (required, readonly)
- `sequence_number` Integer “Sequence #” (required, readonly)
- `last_order_id` Many2one → `pos.order` “Last Pos Order” (readonly)
- `last_order_hash` Char “Last Order entry's inalteralbility hash” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, store, related=company_id.currency_id)

Public methods: `write`

## `account.fiscal.position` (extends)


Public methods: `write`

## `pos.config` (extends)


Public methods: `open_ui`

## `pos.session` (extends)


Public methods: `open_frontend_cb`

Extension points: `_check_session_timing`

## `pos.order` (extends)

- `l10n_fr_hash` Char “Inalteralbility Hash” (readonly)
- `l10n_fr_secure_sequence_number` Integer “Inalteralbility No Gap Sequence #” (readonly)
- `l10n_fr_string_to_hash` Char (readonly, compute=_compute_string_to_hash)
- `previous_order_id` Many2one → `pos.order` “Previous Order” (readonly, store, compute=_compute_previous_order)
- `pos_version` Char (readonly)

Public methods: `create`, `write`

Extension points: `_get_new_hash`

## `pos.order.line` (extends)


Public methods: `write`

## `res.company` (extends)

- `l10n_fr_pos_cert_sequence_id` Many2one → `ir.sequence`

Public methods: `create`, `write`

Extension points: `_action_check_pos_hash_integrity`, `_check_pos_hash_integrity`

## `report.l10n_fr_pos_cert.report_pos_hash_integrity` (defines)

Get french pos hash integrity result as PDF.


Extension points: `_get_report_values`
