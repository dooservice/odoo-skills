# Payment terms and fiscal positions

A payment term (`account.payment.term`) splits an invoice total into due dates. A fiscal
position (`account.fiscal.position`) swaps taxes and accounts for some customers or
vendors: exports, sales to businesses in another country, another state's rules. Which
positions a country needs is set by law: the country's localization decides this; see
its localization skill if installed. Both need `account` (Invoicing). Both are copied
onto documents when they are created: changing one changes future documents, not posted
ones. Changes to either need the user's yes; one already used on posted invoices is best
replaced by a new record and the old one archived.

## Before you start

- Apps: `account`.
- Settings: none to switch on. The company's early payment discount accounts
  (`account_journal_early_pay_discount_gain_account_id`, `..._loss_account_id`) for
  discounts.
- Read first:

```python
company = env.company
partner = env['res.partner'].search([('name', '=', '<partner name>')], limit=1)
terms = env['account.payment.term'].search([('company_id', 'in', [company.id, False])])
terms.read(['name', 'line_ids', 'company_id'])
terms.line_ids.read()
positions = env['account.fiscal.position'].search([('company_id', '=', company.id)])
positions.read(['name', 'auto_apply', 'country_id', 'country_group_id', 'state_ids', 'vat_required', 'sequence', 'tax_ids', 'account_ids'])
partner.with_company(company).read(['property_payment_term_id', 'property_supplier_payment_term_id', 'property_account_position_id'])
```

Standard terms to reuse first: `account.account_payment_term_immediate`,
`account.account_payment_term_30days`,
`account.account_payment_term_30_days_end_month_the_10`,
`account.account_payment_term_advance_60days`.

## The standard flow

Odoo's order: create the payment term and test it on its example; create the fiscal
position, map its taxes and accounts, say when it applies by itself; then set both on
the partners that need them.

1. **Create the payment term.** Invoicing ‣ Configuration ‣ Invoicing ‣ Payment Terms ‣ New. Name,
   the Due Terms lines, Show installment dates (`display_on_invoice`, Display terms on
   invoice in 16.0); the Example line
   shows the due dates. 30% now, the rest at 60 days, from 17.0 on:

   ```python
   term = env['account.payment.term'].create({
       'name': '30% now, 70% at 60 days',
       'line_ids': [
           (0, 0, {'value': 'percent', 'value_amount': 30, 'nb_days': 0}),
           (0, 0, {'value': 'percent', 'value_amount': 70, 'nb_days': 60}),
       ],
   })
   env.cr.commit()
   ```

   The same in 16.0, where the last line is the balance:

   ```python
   'line_ids': [
       (0, 0, {'value': 'percent', 'value_amount': 30, 'days': 0}),
       (0, 0, {'value': 'balance', 'days': 60}),
   ]
   ```

   Leaves a term offered on quotations, orders, invoices and bills. Lines are computed
   in the order of their due dates.

   - `delay_type` (17.0 on): `days_after` (invoice date), `days_after_end_of_month`,
     `days_after_end_of_next_month`, `days_end_of_month_on_the` with `days_next_month`
     (`'10'`: the 10th of the next month).
   - The text on the document is `note` (Description on the Invoice in 16.0, the
     Preview box from 17.0).

2. **Create the fiscal position.** Invoicing ‣ Configuration ‣ Accounting ‣ Fiscal Positions ‣ New.

   ```python
   position = env['account.fiscal.position'].create({
       'name': 'Business customers abroad', 'company_id': company.id, 'sequence': 10,
   })
   env.cr.commit()
   ```

   Leaves a position selectable by hand on documents (Other Info tab), mapping nothing
   yet. Legal notes for its documents go in `note`.

3. **Map its taxes.** Mapping only works with active taxes (`taxes-and-journals.md`).

   16.0 to 18.0, on the position's tax mapping lines (`account.fiscal.position.tax`):

   ```python
   position.write({'tax_ids': [(0, 0, {'tax_src_id': domestic_tax.id, 'tax_dest_id': export_tax.id})]})
   env.cr.commit()
   ```

   An empty `tax_dest_id` removes the tax.

   19.0 on, on the replacement tax: Invoicing ‣ Configuration ‣ Accounting ‣ Taxes ‣ the replacement
   tax ‣ Fiscal Positions and Replaces. `tax_ids` on the position is the list of taxes
   it uses, and each of them names the domestic taxes it replaces in
   `original_tax_ids` (the tax side of the same relation is `fiscal_position_ids`).

   ```python
   export_tax.write({'fiscal_position_ids': [(4, position.id)], 'original_tax_ids': [(4, domestic_tax.id)]})
   env.cr.commit()
   ```

   Leaves documents with the position using the replacement tax instead of the
   domestic one. To replace one tax with several, add one line per replacement (16.0
   to 18.0) or set the domestic tax in Replaces of each replacement (19.0 on).

   - 19.0: a tax not replaced stays on the document, except that a position with no
     `tax_ids` drops every tax limited to other positions.
   - 20.0: a tax limited to some fiscal positions is dropped on documents with another
     one.
   - In every version, prefer a 0% replacement tax (exports, sales to businesses
     abroad) to removing the tax: the tax report still sees the base.

4. **Map its accounts**, when sales or purchases under it go to other income or expense
   accounts. The position's Account Mapping tab: Account on Product, Account to Use
   Instead.

   ```python
   position.write({'account_ids': [(0, 0, {'account_src_id': income.id, 'account_dest_id': export_income.id})]})
   env.cr.commit()
   ```

   Leaves invoice lines with the position booked on `export_income` instead of the
   product's `income` account.

5. **Apply it automatically.** The position form ‣ Detect Automatically, with its
   conditions.

   ```python
   group = env['res.country.group'].search([('name', '=', '<country group name>')], limit=1)
   position.write({'auto_apply': True, 'country_group_id': group.id, 'vat_required': True})
   env.cr.commit()
   ```

   Leaves the position chosen on new documents for partners that match.

   - `auto_apply` picks it for a partner (the delivery address when there is one) that
     matches `country_id` or `country_group_id`, `state_ids`, `zip_from`/`zip_to` and,
     with `vat_required`, has a VAT number. Up to 18.0 the most specific match wins,
     then `sequence`; from 19.0 the first match by `sequence` wins, so give the narrower
     position the lower sequence. A partner without a country gets no automatic
     position at all.
   - Country groups: Contacts ‣ Configuration ‣ Localization ‣ Country Group;
     `env['res.country.group'].search([]).mapped('name')`, a group's countries in
     `country_ids`.

6. **Set them on partners.** Contacts (or Invoicing ‣ Customers ‣ Customers) ‣ the
   partner ‣ Sales & Purchase tab: Payment Terms, Vendor Payment Terms, Fiscal Position.

   ```python
   partner.with_company(company).write({
       'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
       'property_supplier_payment_term_id': env.ref('account.account_payment_term_immediate').id,
       'property_account_position_id': position.id,
   })
   env.cr.commit()
   ```

   Leaves the partner's new documents with those terms and that position. These are
   per company. A position set on the partner wins over automatic detection. Open
   documents keep what they had; a draft invoice takes the new values only when its
   partner is set again.

## Variations

- **Early payment discount.** "2% if paid within 10 days, net 30": the term form ‣
  Early Discount. From 17.0 on:

  ```python
  env['account.payment.term'].create({
      'name': '2/10 Net 30',
      'line_ids': [(0, 0, {'value': 'percent', 'value_amount': 100, 'nb_days': 30})],
      'early_discount': True, 'discount_percentage': 2, 'discount_days': 10,
      'early_pay_discount_computation': 'included',
  })
  env.cr.commit()
  ```

  - 17.0 on: the discount is on the term (`early_discount`, `discount_percentage`,
    `discount_days`, `early_pay_discount_computation`) and needs a single 100% line.
  - 16.0: `discount_percentage` and `discount_days` are on the line, and
    `early_pay_discount_computation` is a company setting.
  - `early_pay_discount_computation`: `included` (tax reduced only when paid early),
    `excluded` (tax never reduced), `mixed` (tax reduced on the invoice already).
  - The company needs `account_journal_early_pay_discount_gain_account_id` and
    `..._loss_account_id`; the chart usually sets them.
- **A position chosen by hand.** Without Detect Automatically, the user picks it on the
  document (Other Info tab) before adding lines.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Payment terms | Invoicing ‣ Configuration ‣ Invoicing ‣ Payment Terms | same | same | same | same |
| Fiscal positions | Invoicing ‣ Configuration ‣ Accounting ‣ Fiscal Positions | same | same | same | same |
| Country groups | Contacts ‣ Configuration ‣ Localization ‣ Country Group | same | same | same | same |
| Term line `value` | `balance`, `percent`, `fixed` | `percent`, `fixed` | same as 17.0 | same as 17.0 | same as 17.0 |
| Term line days | `days`, `months` | `nb_days` | same as 17.0 | same as 17.0 | same as 17.0 |
| Term line end of month | `end_month`, `days_after` | `delay_type`, `days_next_month` | same as 17.0 | same as 17.0 | same as 17.0 |
| Term line rule | exactly one `balance` line | percent lines sum to 100 | same as 17.0 | same as 17.0 | same as 17.0 |
| Early discount | on the line; computation per company | on the term | same as 17.0 | same as 17.0 | same as 17.0 |
| Tax mapping | lines on the position | same | same | on the replacement tax | same as 19.0 |
| Automatic choice | most specific match, then `sequence` | same | same | first match by `sequence` | same as 19.0 |
| Domestic position | none | none | none | company's `domestic_fiscal_position_id` | same as 19.0 |

From 19.0 the company's domestic position is the first by `sequence` for the company's
country (or a country group with it); taxes without positions, or with that one, are
the domestic taxes, and the Replaces field is not shown for it. Account mapping
(`account_ids` with `account_src_id`, `account_dest_id`) is the same in every version.

## Verify

```python
import datetime
print(term._compute_terms(datetime.date.today(), company.currency_id, company, 0.0, 0.0, 1.0, 1000.0, 1000.0) if hasattr(term, '_compute_terms') else term.compute(1000.0))
print(env['account.fiscal.position'].with_company(company)._get_fiscal_position(partner).name)
print(position.map_tax(domestic_tax).mapped('name'))
```

Then create a draft invoice for the partner and read its due dates, taxes and accounts.

## Pitfalls

- **A term or position used on posted invoices changed in place.** Posted invoices keep
  what they had, but reports and follow-ups read the record: create a new one and
  archive the old.
- **Two automatic positions that both match.** From 19.0 the lower `sequence` wins;
  give the narrower position the lower sequence.
- **A partner without a country.** It gets no automatic position at all.
- **Removing a tax instead of a 0% tax.** The tax report loses the base: map to a 0%
  tax.
- **Mapping to an inactive tax.** Tax mapping only works with active taxes.
