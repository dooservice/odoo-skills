# l10n_es_pos — Spain - Point of Sale

Depends on: point_of_sale, l10n_es.

## `account.move` (extends)


## `pos.config` (extends)

- `is_spanish` Boolean “Company located in Spain” (compute=_compute_is_spanish)
- `l10n_es_simplified_invoice_limit` Float “Simplified Invoice limit amount”
- `l10n_es_simplified_invoice_journal_id` Many2one → `account.journal`
- `simplified_partner_id` Many2one → `res.partner` “Simplified invoice partner” (compute=_compute_simplified_partner_id)

Public methods: `get_limited_partners_loading`, `setup_defaults`

## `pos.order` (extends)

- `is_l10n_es_simplified_invoice` Boolean “Simplified invoice”
- `l10n_es_simplified_invoice_number` Char “Simplified invoice number” (compute=_compute_l10n_es_simplified_invoice_number)

Extension points: `_prepare_invoice_vals`

## `pos.session` (extends)


## `res.config.settings` (extends)

- `pos_is_spanish` Boolean “Consider the specific spanish legislation, such as the use of simplified invoices” (related=pos_config_id.is_spanish)
- `pos_l10n_es_simplified_invoice_limit` Float (related=pos_config_id.l10n_es_simplified_invoice_limit)
- `pos_l10n_es_simplified_invoice_journal_id` Many2one (related=pos_config_id.l10n_es_simplified_invoice_journal_id)
