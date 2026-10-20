# Taxes and journals

Taxes (`account.tax`) decide how much is charged and where it is booked; journals
(`account.journal`) group entries and number invoices. The chart of accounts usually
installs the taxes, tax groups and journals: adjust what is there before creating
anything. Which taxes exist and how they are reported depend on the country: the
country's localization decides this; see its localization skill if installed. Both are shared by every document that uses them. Count the users
before a change, and never change one with posted entries in place: create a new one,
point new documents to it, archive the old one. Every accounting change needs the
user's yes.

## Read first

```python
company = env.company
taxes = env['account.tax'].with_context(active_test=False).search([('company_id', '=', company.id)])
taxes.read(['name', 'type_tax_use', 'amount_type', 'amount', 'price_include', 'tax_group_id', 'active'])
env['account.journal'].search_read([('company_id', '=', company.id)], ['name', 'code', 'type', 'default_account_id', 'currency_id'])
tax = taxes.filtered(lambda t: t.name == '<tax name>')
env['account.move.line'].search_count(['|', ('tax_ids', 'in', tax.ids), ('tax_line_id', 'in', tax.ids), ('parent_state', '=', 'posted')])
```

## A tax

Copy a tax of the same kind rather than creating one from nothing: the copy keeps the
repartition lines with their accounts and tax grids (`tag_ids`) the tax report needs.

```python
source = env['account.tax'].search([('company_id', '=', company.id), ('type_tax_use', '=', 'sale'), ('amount', '=', 10)], limit=1)
tax = source.copy({'name': 'Sales tax 10% (services)', 'tax_scope': 'service'})
env.cr.commit()
```

- `type_tax_use`: `sale`, `purchase`, or `none` (only used inside a group of taxes).
- `amount_type`: `percent`, `fixed` (an amount per unit), `division` (percentage of the
  price tax included), `group` (sums `children_tax_ids`). The `account_tax_python`
  module adds `code`.
- `tax_scope`: `service` or `consu` restricts the tax to that kind of product.
- `include_base_amount` makes the tax part of the base of the taxes after it (ordered
  by `sequence`); `is_base_affected` says whether a tax accepts that.
- Tax included in the price (B2C shops, retail):
  - 16.0, 17.0: `price_include=True` on the tax.
  - 18.0 on: `price_include` is computed. Set `price_include_override` to
    `tax_included` or `tax_excluded` on the tax, or the company default with the
    setting `account_price_include` (default `tax_excluded`).

## Repartition lines

Each tax has a base line and a tax line for invoices, and the same for refunds. Created
from nothing they have no account, and the tax amount then lands on the product's
income or expense account. Set the account of the `tax` lines.

```python
lines = tax.invoice_repartition_line_ids | tax.refund_repartition_line_ids
lines.filtered(lambda l: l.repartition_type == 'tax').write({'account_id': account.id})
env.cr.commit()
```

- 16.0: lines link to the tax with `invoice_tax_id` / `refund_tax_id`. From 17.0 on
  with `tax_id` and `document_type` (`invoice` or `refund`), all in `repartition_line_ids`.
- `factor_percent` splits the tax: 100 and -100 on two tax lines is a reverse charge.
- Finding the account: `('company_id', '=', company.id)` in 16.0 and 17.0;
  `('company_ids', 'in', company.id)` from 18.0 on, where accounts can be shared.

## Tax groups

`account.tax.group` puts taxes together in the invoice totals ("Tax 10%", "Withholding 5%").

- 16.0: no `company_id`; tax closing accounts are `property_tax_payable_account_id`,
  `property_tax_receivable_account_id`, `property_advance_tax_payment_account_id`.
- 17.0 to 19.0: `company_id` is required; the accounts are `tax_payable_account_id`,
  `tax_receivable_account_id`, `advance_tax_payment_account_id`.
- 20.0: the group keeps `company_id` but no longer carries those accounts in Community.

## Cash basis

Tax due when the invoice is paid, not when it is issued. Whether the law asks for it
depends on the country: the country's localization decides this; see its localization
skill if installed. Turn on the setting, then mark the tax.

```python
env['res.config.settings'].create({'tax_exigibility': True, 'tax_cash_basis_journal_id': journal.id}).execute()
tax.write({'tax_exigibility': 'on_payment', 'cash_basis_transition_account_id': transition.id})
env.cr.commit()
```

The transition account holds the tax until payment. Do not use a receivable or payable
account (the form does not offer them, but a script is not stopped), and pick one that
allows reconciliation (`reconcile`; 19.0 refuses one that does not).

## Journals

```python
env['account.journal'].create({
    'name': 'Second bank', 'code': 'BNK2', 'type': 'bank',
    'bank_acc_number': '<account number>', 'company_id': company.id,   # 'bank_account_number' in 20.0
})
env.cr.commit()
```

- `type`: `sale`, `purchase`, `cash`, `bank`, `general`; `credit` (credit card) from 18.0.
- `code` is the prefix of entry numbers; at most 5 characters up to 19.0, where a longer
  one is cut to 5 without a warning.
- Bank account: `bank_acc_number` creates the `res.partner.bank` up to 19.0. In 20.0
  the field is `bank_account_number` (with `bank_bic`): `res.bank` is gone and the bank
  name and BIC live on `res.partner.bank`.
- `currency_id` only for a bank or cash journal in another currency.
- `default_account_id` is the income, expense, bank or cash account; `suspense_account_id`
  holds bank lines not yet reconciled.

## Invoice numbering

Invoices and entries take their number from the journal, not from `ir.sequence`. The
first number is `CODE/YYYY/00001`, with an `R` in front for refunds when the journal has
`refund_sequence`. Odoo then follows the format of the previous name: yearly, monthly
(`INV/2026/05/0001`) or fixed. To change the format, the user renames the first entry of
the journal or period in the form view. To renumber posted entries, the user runs
Resequence (`account.resequence.wizard`) after confirming it is legal in that country.
Never write `name` on posted entries from a script.
