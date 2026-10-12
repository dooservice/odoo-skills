# Taxes and journals

Accounting configuration is shared by every document that uses it. Before changing a
tax or journal in use, say how many documents use it, and never change one with posted
entries: create a new one and archive the old.

## A tax

```python
env['account.tax'].create({
    'name': 'VAT 21%',
    'amount': 21,
    'amount_type': 'percent',
    'type_tax_use': 'sale',
    'company_id': company.id,
})
```

- The chart of accounts usually brings the country's taxes: look before creating one,
  `env['account.tax'].search_read([('company_id', '=', company.id)], ['name', 'amount', 'type_tax_use'])`.
- Repartition lines (which account each part goes to) are created with defaults; check
  them against the chart before using the tax.
- Prices with tax included: `price_include` up to 17.0, `price_include_override` from 18.0
  on; check `odoo-reference/models/account.md`.

## A journal

```python
env['account.journal'].create({'name': 'Bank BBVA', 'code': 'BBVA', 'type': 'bank', 'company_id': company.id})
```

`type` is `sale`, `purchase`, `bank`, `cash` or `general`. Invoice numbers come from the
journal and its documents, not from `ir.sequence`: renumbering is the Resequence wizard
in the panel, done by the user.
