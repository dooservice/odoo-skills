# l10n_in_sale — Indian - Sale Report(GST)

Depends on: l10n_in, sale.

## `sale.order` (extends)

- `l10n_in_reseller_partner_id` Many2one → `res.partner` “Reseller”
- `l10n_in_gst_treatment` Selection “GST Treatment” (store, compute=_compute_l10n_in_gst_treatment)

Extension points: `_prepare_invoice`

## `sale.advance.payment.inv` (extends)


Extension points: `_prepare_invoice_values`
