# l10n_my_edi_pos — Malaysia - E-invoicing (POS)

Depends on: l10n_my_edi, point_of_sale.

## `account.edi.xml.ubl_myinvois_my` (extends)


Extension points: `_get_address_node`, `_get_consolidated_invoice_node`, `_get_consolidated_invoice_party_node`

## `myinvois.document` (extends)

- `pos_order_ids` Many2many → `pos.order`
- `pos_config_id` Many2one → `pos.config` “PoS Config” (readonly)
- `linked_order_count` Integer (compute=_compute_linked_order_count)
- `pos_order_date_range` Char “Date Range” (store, compute=_compute_pos_order_date_range)

Public methods: `action_show_myinvois_documents`, `action_view_linked_orders`

Extension points: `_get_record_rounded_base_lines`

## `pos.order` (extends)

- `consolidated_invoice_ids` Many2many → `myinvois.document`
- `l10n_my_edi_state` Selection “MyInvois State” (store, compute=_compute_l10n_my_edi_state)

Public methods: `action_show_myinvois_documents`

Extension points: `_get_active_consolidated_invoice`

## `res.partner` (extends)


Extension points: `_get_frontend_writable_fields`

## `myinvois.consolidate.invoice.wizard` (extends)

- `consolidation_type` Selection

Extension points: `_get_myinvois_document_vals`
