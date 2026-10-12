# Companies, currencies and the chart of accounts

Read first: `env['res.company'].search_read([], ['name', 'currency_id', 'country_id'])`.

## A company

```python
company = env['res.company'].create({
    'name': 'Acme Services',
    'country_id': env.ref('base.es').id,
    'currency_id': env.ref('base.EUR').id,
})
env.user.write({'company_ids': [(4, company.id)]})
env.cr.commit()
```

- Odoo turns multi-company on by itself once there are two companies.
- Give each user the companies they work in (`company_ids`) and their default one
  (`company_id`); a user only sees records of companies they have.
- Currency: activate it first (`env.ref('base.USD').active = True`), and the setting
  `group_multi_currency` when documents use more than one.

## Chart of accounts

Install the country's localization (`l10n_<country>`, see `odoo-reference/addons.md`),
then load its chart for the company, before any entry is posted:

- 17.0 and later: `env['account.chart.template'].try_loading('<code>', company, install_demo=False)`, the
  code being the template's, as listed by `env['account.chart.template']._get_chart_template_mapping()`.
- 16.0: the template is a record: `env.ref('l10n_<country>.<template>').try_loading(company, install_demo=False)`.

A company with posted entries keeps its chart: say so and stop.
