# Taxes and journals

Taxes (`account.tax`) decide how much is charged and where it is booked; journals
(`account.journal`) group entries and number invoices. The chart of accounts usually
installs the taxes, tax groups and journals: adjust what is there before creating
anything. Which taxes exist and how they are reported depend on the country: the
country's localization decides this; see its localization skill if installed. It needs
`account` (Invoicing); tax return reports and bank synchronization are Enterprise and
left out. Both taxes and journals are shared by every document that uses them. Count the
users before a change, and never change one with posted entries in place: create a new
one, point new documents to it, archive the old one. Every accounting change needs the
user's yes.

## Before you start

- Apps: `account`; `account_tax_python` only for taxes computed by code.
- Settings: `sale_tax_id`, `purchase_tax_id` (default taxes); `account_price_include`
  (18.0+); `tax_exigibility` (cash basis); `group_cash_rounding`.
- Read first:

```python
company = env.company
taxes = env['account.tax'].with_context(active_test=False).search([('company_id', '=', company.id)])
taxes.read(['name', 'type_tax_use', 'amount_type', 'amount', 'price_include', 'tax_group_id', 'active'])
env['account.journal'].search_read([('company_id', '=', company.id)], ['name', 'code', 'type', 'default_account_id', 'currency_id'])
tax = taxes.filtered(lambda t: t.name == '<tax name>')
env['account.move.line'].search_count(['|', ('tax_ids', 'in', tax.ids), ('tax_line_id', 'in', tax.ids), ('parent_state', '=', 'posted')])
```

## The standard flow

Odoo's order for taxes: the company-wide options, then activate the taxes the
localization already brought, then edit or create a tax and its distribution, then put
taxes on products. Journals come with the chart; extra ones are added from the
Configuration menu.

1. **Set the company-wide tax options.** Invoicing ‣ Configuration ‣ Settings ‣ Taxes:
   Default Taxes (put on new products), and from 18.0 whether prices are tax included
   by default.

   ```python
   sale = env['account.tax'].search([('company_id', '=', company.id), ('type_tax_use', '=', 'sale')], limit=1)
   purchase = env['account.tax'].search([('company_id', '=', company.id), ('type_tax_use', '=', 'purchase')], limit=1)
   env['res.config.settings'].with_company(company).create({'sale_tax_id': sale.id, 'purchase_tax_id': purchase.id}).execute()
   env.cr.commit()
   ```

   Leaves the company's `account_sale_tax_id` and `account_purchase_tax_id` set, used on
   new products.

2. **Activate the taxes the localization brought.** Invoicing ‣ Configuration ‣ Accounting ‣ Taxes,
   toggle Active. Localizations create most rates inactive; only the main one is
   active.

   ```python
   inactive = env['account.tax'].with_context(active_test=False).search([('company_id', '=', company.id), ('active', '=', False)])
   inactive.filtered(lambda t: t.name == '<tax name>').write({'active': True})
   env.cr.commit()
   ```

   Leaves the tax selectable on documents and products, and usable in fiscal positions
   (mapping only works with active taxes).

3. **Create a tax when none fits.** Invoicing ‣ Configuration ‣ Accounting ‣ Taxes ‣ a tax of the
   same kind ‣ Actions ‣ Duplicate, then edit. Copying keeps the distribution lines with
   their accounts and tax grids (`tag_ids`) the tax report needs.

   ```python
   source = env['account.tax'].search([('company_id', '=', company.id), ('type_tax_use', '=', 'sale'), ('amount', '=', 10)], limit=1)
   tax = source.copy({'name': 'Sales tax 10% (services)', 'tax_scope': 'service'})
   env.cr.commit()
   ```

   Leaves an active tax with the source's distribution.

   - `type_tax_use`: `sale`, `purchase`, or `none` (only used inside a group of taxes).
   - `amount_type`: `percent`, `fixed` (an amount per unit), `division` (percentage of
     the price tax included), `group` (sums `children_tax_ids`). The
     `account_tax_python` module adds `code`.
   - `tax_scope`: `service` or `consu` restricts the tax to that kind of product.
   - `include_base_amount` (Affect Base of Subsequent Taxes) makes the tax part of the
     base of the taxes after it (ordered by `sequence`, the drag handle in the list);
     `is_base_affected` says whether a tax accepts that.
   - Tax included in the price (B2C shops, retail):
     - 16.0, 17.0: `price_include=True` on the tax.
     - 18.0 on: `price_include` is computed. Set `price_include_override` to
       `tax_included` or `tax_excluded` on the tax, or the company default with the
       setting `account_price_include` (default `tax_excluded`).

4. **Set the distribution accounts.** The tax form ‣ Distribution for Invoices and
   Distribution for Refunds. Each has a base line and a tax line. Created from nothing
   they have no account, and the tax amount then lands on the product's income or
   expense account. Set the account of the `tax` lines.

   ```python
   lines = tax.invoice_repartition_line_ids | tax.refund_repartition_line_ids
   lines.filtered(lambda l: l.repartition_type == 'tax').write({'account_id': account.id})
   env.cr.commit()
   ```

   Leaves the tax amount booked on `account`.

   - 16.0: lines link to the tax with `invoice_tax_id` / `refund_tax_id`. From 17.0 on
     with `tax_id` and `document_type` (`invoice` or `refund`), all in
     `repartition_line_ids`.
   - `factor_percent` splits the tax: 100 and -100 on two tax lines is a reverse charge.
   - Finding the account: `('company_id', '=', company.id)` in 16.0 and 17.0;
     `('company_ids', 'in', company.id)` from 18.0 on, where accounts can be shared.

5. **Put the taxes on products.** Invoicing ‣ Customers ‣ Products ‣ the product ‣
   Customer Taxes and Vendor Taxes.

   ```python
   product = env['product.template'].search([('name', '=', '<product name>')], limit=1)
   product.with_company(company).write({'taxes_id': [(6, 0, tax.ids)]})
   env.cr.commit()
   ```

   Leaves the tax applied when the product is added to a quotation, order, invoice or
   bill. Vendor taxes are `supplier_taxes_id`.

6. **Add a journal.** Invoicing ‣ Configuration ‣ Accounting ‣ Journals ‣ New; for a bank, the bank
   card on the Invoicing dashboard creates the journal and its account.

   ```python
   env['account.journal'].create({
       'name': 'Second bank', 'code': 'BNK2', 'type': 'bank',
       'bank_acc_number': '<account number>', 'company_id': company.id,   # 'bank_account_number' in 20.0
   })
   env.cr.commit()
   ```

   Leaves a journal with its own default account and numbering.

   - `type`: `sale`, `purchase`, `cash`, `bank`, `general`; `credit` (credit card) from
     18.0.
   - `code` is the prefix of entry numbers; at most 5 characters up to 19.0, where a
     longer one is cut to 5 without a warning.
   - Bank account: `bank_acc_number` creates the `res.partner.bank` up to 19.0. In 20.0
     the field is `bank_account_number` (with `bank_bic`): `res.bank` is gone and the
     bank name and BIC live on `res.partner.bank`.
   - `currency_id` only for a bank or cash journal in another currency.
   - `default_account_id` is the income, expense, bank or cash account;
     `suspense_account_id` holds bank lines not yet reconciled.

7. **Set the invoice numbering.** Invoices and entries take their number from the
   journal, not from `ir.sequence`. The first number is `CODE/YYYY/00001`, with an `R`
   in front for refunds when the journal has `refund_sequence`. Odoo then follows the
   format of the previous name: yearly, monthly (`INV/2026/05/0001`) or fixed. To change
   the format, the user edits the number of the first invoice of a sequence period
   while creating it; on a journal already in use, Odoo's way is to open the last
   posted invoice, Reset to Draft, and edit its number, which only the user does, with
   the accountant's yes. Odoo then applies the detected format to the next invoices.

   Leaves the journal numbering in the new format from that invoice on.

## Variations

- **Cash basis.** Tax due when the invoice is paid, not when it is issued. Whether the
  law asks for it depends on the country: the country's localization decides this; see
  its localization skill if installed. Invoicing ‣ Configuration ‣ Settings ‣ Taxes ‣
  Cash Basis and its journal, then the tax form ‣ Advanced Options ‣ Tax Exigibility
  Based on Payment and the Cash Basis Transition Account.

  ```python
  env['res.config.settings'].create({'tax_exigibility': True, 'tax_cash_basis_journal_id': journal.id}).execute()
  tax.write({'tax_exigibility': 'on_payment', 'cash_basis_transition_account_id': transition.id})
  env.cr.commit()
  ```

  The transition account holds the tax until payment. Do not use a receivable or
  payable account (the form does not offer them, but a script is not stopped), and pick
  one that allows reconciliation (`reconcile`; 19.0 refuses one that does not).
- **Tax groups.** `account.tax.group` puts taxes together in the invoice totals
  ("Tax 10%", "Withholding 5%"); Invoicing ‣ Configuration ‣ Accounting ‣ Tax Groups in developer
  mode.
  - 16.0: no `company_id`; tax closing accounts are `property_tax_payable_account_id`,
    `property_tax_receivable_account_id`, `property_advance_tax_payment_account_id`.
  - 17.0 to 19.0: `company_id` is required; the accounts are `tax_payable_account_id`,
    `tax_receivable_account_id`, `advance_tax_payment_account_id`.
  - 20.0: the group keeps `company_id` but no longer carries those accounts in
    Community.
- **Renumbering posted entries.** The user runs Resequence (`account.resequence.wizard`,
  developer mode, the journal's invoices ‣ Actions ‣ Resequence) after confirming it is
  legal in that country. It refuses entries before a lock date, duplicates and numbers
  outside their period.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Taxes | Invoicing ‣ Configuration ‣ Accounting ‣ Taxes | same | same | same | same |
| Tax groups (developer mode) | Invoicing ‣ Configuration ‣ Accounting ‣ Tax Groups | same | same | same | same |
| Journals | Invoicing ‣ Configuration ‣ Accounting ‣ Journals | same | same | same | same |
| Products | Invoicing ‣ Customers ‣ Products | same | same | same | same |
| Tax included | `price_include` | `price_include` | `price_include_override`, setting `account_price_include` | same as 18.0 | same as 18.0 |
| Distribution lines | `invoice_tax_id` / `refund_tax_id` | `tax_id` + `document_type` | same as 17.0 | same as 17.0 | same as 17.0 |
| Tax group company and accounts | no company; `property_tax_*` | `company_id`; `tax_*_account_id` | same as 17.0 | same as 17.0 | `company_id`, no accounts |
| Journal types | no `credit` | no `credit` | `credit` added | same as 18.0 | same as 18.0 |
| Journal bank account | `bank_acc_number` | same | same | same | `bank_account_number`, `bank_bic` |
| Transition account must allow reconciliation | no | no | no | yes | no |

The menu root is Invoicing in Community and Accounting with the Enterprise accounting
app; Odoo's documentation writes Accounting.

## Verify

```python
tax.invalidate_recordset()
print(tax.read(['name', 'active', 'amount', 'type_tax_use', 'tax_group_id']))
print([(l.repartition_type, l.factor_percent, l.account_id.code) for l in tax.invoice_repartition_line_ids | tax.refund_repartition_line_ids])
print(tax.compute_all(100.0)['total_included'])
print(env['account.journal'].search_read([('company_id', '=', company.id)], ['code', 'type']))
```

Then create a draft invoice with the product and read its tax lines.

## Pitfalls

- **A tax with posted entries changed in place.** It rewrites history for reports:
  create a new tax and archive the old one.
- **Distribution without account.** A tax created from nothing books its amount on the
  income or expense account: copy a tax, or set the accounts (step 4).
- **A journal code longer than 5.** Up to 19.0 it is cut to 5 without a warning.
- **Names written on posted entries.** Never write `name` on posted entries from a
  script: use the reset-to-draft way or Resequence, done by the user.
- **Taxes of another company.** Taxes belong to one company: a document of company A
  cannot use those of company B.
