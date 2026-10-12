# mass_mailing_sale — Mass mailing on sale orders

Depends on: sale, mass_mailing.

## `mailing.mailing` (extends)

- `sale_quotation_count` Integer “Quotation Count” (compute=_compute_sale_quotation_count)
- `sale_invoiced_amount` Monetary “Invoiced Amount” (compute=_compute_sale_invoiced_amount)
- `currency_id` Many2one → `res.currency` (compute=_compute_currency_id)

Public methods: `action_redirect_to_invoiced`, `action_redirect_to_quotations`

Extension points: `_prepare_statistics_email_values`

## `sale.order` (extends)


## `utm.campaign` (extends)

- `ab_testing_winner_selection` Selection
