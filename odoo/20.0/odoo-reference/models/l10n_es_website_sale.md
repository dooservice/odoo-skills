# l10n_es_website_sale — Spain - ECommerce

Depends on: l10n_es, website_sale.

## `account.chart.template` (extends)


Extension points: `_get_simplified_journal`

## `res.config.settings` (extends)

- `simplified_invoice_journal_id` Many2one (related=website_id.simplified_invoice_journal_id)

## `res.partner` (extends)


Extension points: `_get_mandatory_billing_address_fields`

## `sale.order` (extends)


## `website` (extends)

- `simplified_invoice_journal_id` Many2one → `account.journal` “Simplified Invoice Journal” (store, compute=_compute_simplified_invoice_journal_id)
