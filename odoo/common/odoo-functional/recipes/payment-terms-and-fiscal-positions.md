# Payment terms and fiscal positions

A payment term (`account.payment.term`) splits an invoice total into due dates. A fiscal
position (`account.fiscal.position`) swaps taxes and accounts for some customers or
vendors: exports, sales to businesses in another country, another state's rules. Which
positions a country needs is set by law: the country's localization decides this; see
its localization skill if installed. Both are copied onto invoices
when they are created: changing one changes future documents, not posted ones. Changes
to either need the user's yes; one already used on posted invoices is best replaced by
a new record and the old one archived.

## Read first

```python
company = env.company
terms = env['account.payment.term'].search([('company_id', 'in', [company.id, False])])
terms.read(['name', 'line_ids', 'company_id'])
terms.line_ids.read()
positions = env['account.fiscal.position'].search([('company_id', '=', company.id)])
positions.read(['name', 'auto_apply', 'country_id', 'country_group_id', 'state_ids', 'vat_required', 'sequence', 'tax_ids', 'account_ids'])
partner.with_company(company).read(['property_payment_term_id', 'property_supplier_payment_term_id', 'property_account_position_id'])
```

## A payment term

30% now, the rest at 60 days, from 17.0 on:

```python
env['account.payment.term'].create({
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

| line field | 16.0 | 17.0 to 20.0 |
|---|---|---|
| `value` | `balance`, `percent`, `fixed` | `percent`, `fixed` |
| days | `days`, `months` | `nb_days` |
| end of month | `end_month`, `days_after` | `delay_type`, `days_next_month` |
| rule | exactly one `balance` line | percent lines sum to 100 |

`delay_type` (17.0 on): `days_after` (invoice date), `days_after_end_of_month`,
`days_after_end_of_next_month`, `days_end_of_month_on_the` with `days_next_month`
(`'10'`: the 10th of the next month).

Standard terms to reuse first: `account.account_payment_term_immediate`,
`account.account_payment_term_30days`, `account.account_payment_term_30_days_end_month_the_10`,
`account.account_payment_term_advance_60days`.

## Early payment discount

"2% if paid within 10 days, net 30", from 17.0 on (16.0 below):

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

## Fiscal positions

```python
group = env['res.country.group'].search([('name', '=', '<country group name>')], limit=1)
position = env['account.fiscal.position'].create({
    'name': 'Business customers abroad', 'company_id': company.id,
    'auto_apply': True, 'country_group_id': group.id, 'vat_required': True,
    'sequence': 10,
})
env.cr.commit()
```

- `auto_apply` picks it for a partner (the delivery address when there is one) that
  matches `country_id` or `country_group_id`, `state_ids`, `zip_from`/`zip_to` and, with
  `vat_required`, has a VAT number. Up to 18.0 the most specific match wins, then
  `sequence`; from 19.0 the first match by `sequence` wins, so give the narrower position
  the lower sequence. A partner without a country gets no automatic position at all.
- Country groups: `env['res.country.group'].search([]).mapped('name')`; a group's
  countries are in `country_ids`.
- A position set on the partner (`property_account_position_id`, per company) wins over
  auto-detection. Test with
  `env['account.fiscal.position'].with_company(company)._get_fiscal_position(partner)`.
- Account mapping, all versions: `account_ids` with `account_src_id` (the product's
  account) and `account_dest_id` (the one to use instead).

## Tax mapping

16.0 to 18.0: lines of `account.fiscal.position.tax`.

```python
position.write({'tax_ids': [(0, 0, {'tax_src_id': domestic_tax.id, 'tax_dest_id': export_tax.id})]})
env.cr.commit()
```

An empty `tax_dest_id` removes the tax.

19.0 on: the mapping lives on the replacement tax. `tax_ids` on the position is the
list of taxes it uses, and each of them names the domestic taxes it replaces in
`original_tax_ids` (the tax side of the same relation is `fiscal_position_ids`).

```python
export_tax.write({'fiscal_position_ids': [(4, position.id)], 'original_tax_ids': [(4, domestic_tax.id)]})
env.cr.commit()
```

- 19.0: a tax not replaced stays on the document, except that a position with no
  `tax_ids` drops every tax limited to other positions.
- 20.0: a tax limited to some fiscal positions is dropped on documents with another one.
- In every version, prefer a 0% replacement tax (exports, sales to businesses abroad) to
  removing the tax:
  the tax report still sees the base.

## Assigning to partners

```python
partner.with_company(company).write({
    'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
    'property_supplier_payment_term_id': env.ref('account.account_payment_term_immediate').id,
    'property_account_position_id': position.id,
})
env.cr.commit()
```

These are per company. Open documents keep what they had; a draft invoice takes the new
values only when its partner is set again.
