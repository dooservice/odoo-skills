# Partners and imports

Customers, vendors, employees' addresses and the contacts inside a company are all
`res.partner`. A company record holds the commercial data (VAT, payment terms,
pricelist); the people and addresses under it point to it with `parent_id` and share
that data. Bulk loads go through `load()` with external ids, so a second run updates
instead of creating duplicates.

```python
partner = env['res.partner'].search([('vat', '=', 'ESA12345674')])
print(partner.read(['name', 'is_company', 'parent_id', 'type', 'country_id', 'vat', 'user_id', 'lang', 'active']))
print(partner.child_ids.mapped('name'), partner.commercial_partner_id.name)
print(env['ir.model.data'].search([('model', '=', 'res.partner'), ('res_id', '=', partner.id)]).mapped('complete_name'))
```

## Companies and people

```python
acme = env['res.partner'].create({
    'name': 'Acme Industrial SA de CV', 'is_company': True,
    'country_id': env.ref('base.mx').id, 'vat': 'AIN010101AB1',
    'category_id': [(4, env['res.partner.category'].create({'name': 'Distributor'}).id)],
    'user_id': salesperson.id,
})
env['res.partner'].create({'name': 'Laura Gómez', 'parent_id': acme.id, 'type': 'contact', 'email': 'laura@acme.example'})
env['res.partner'].create({'name': 'Monterrey warehouse', 'parent_id': acme.id, 'type': 'delivery', 'city': 'Monterrey'})
env.cr.commit()
```

- `type`: `contact`, `invoice`, `delivery`, `other`; 16.0 also has `private`.
- Commercial fields (VAT, payment terms, pricelist, fiscal position) are synced from the
  company to its children: set them on the company, not on each contact.
- 16.0 to 19.0: `is_company` is a plain boolean, with `company_type` (`person`,
  `company`) as its form widget. 20.0: `is_company` is computed (a contact without parent
  and with a VAT is a company) and `company_type` is gone.
- VAT is checked against the country by `base_vat` (16.0 to 19.0) or by `base` itself
  (20.0). Set `country_id` before or with `vat`. `vat_check_vies` (company setting)
  adds the EU VIES check.
- Tags: `res.partner.category`, Many2many `category_id`. Salesperson: `user_id`. 16.0
  and 17.0 also have a default sales team `team_id` on the partner; 18.0 removed it.

## Payment terms, pricelist, fiscal position

These are company-dependent: each company sees its own value. Write them per company.

```python
acme.with_company(company).write({
    'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
    'property_supplier_payment_term_id': env.ref('account.account_payment_term_30days').id,
    'property_product_pricelist': pricelist.id,
    'property_account_position_id': fiscal_position.id,
})
env.cr.commit()
```

- 16.0 and 17.0 store these values in `ir.property`; 18.0+ in a JSON column on the
  partner. Through the ORM the code is the same; a SQL query is not.
- `property_product_pricelist` is computed (by country when empty) with an inverse; from
  18.0 the stored value is `specific_property_product_pricelist`. Write the first.

## Bulk loads that do not duplicate

`Model.load(fields, rows)` is what the import screen calls. Give every row an external
id in the `id` column: a bare name like `cust_0001` becomes `__import__.cust_0001`, and
loading the same id again updates that record. Never use a real module as prefix: a
module update would delete the record.

```python
fields = ['id', 'name', 'is_company', 'country_id/id', 'vat', 'category_id/id', 'parent_id/id', 'email']
rows = [
    ['cust_0001', 'Brasserie Lefèvre SPRL', '1', 'base.be', 'BE0477472701', '', '', 'info@lefevre.example'],
    ['cust_0001_c1', 'Marc Lefèvre', '0', 'base.be', '', '', 'cust_0001', 'marc@lefevre.example'],
]
result = env['res.partner'].load(fields, rows)
print(result['ids'], result['messages'])
```

- `field/id` takes an external id, `field` alone a display name (ambiguous names fail);
  Many2many takes several ids separated by commas.
- `load` does not raise: check `messages`. On any error `ids` is `False` and nothing
  from that call is kept. Commit only when there are no errors.
- Run a sample of 5 to 10 rows first, read them back, then the whole file. The full load
  needs the user's yes, with the row count.
- Records created without external ids (by hand or by `create`) get one when exported
  with "import-compatible" (`__export__.res_partner_42_...`); export, edit, re-import.
- Before loading, search for existing records by VAT or email and map them to the file's
  ids, or the load creates duplicates.

## Merging duplicates

The wizard `base.partner.merge.automatic.wizard` (in `base`, all versions) moves every
reference to a destination contact and deletes the others.

```python
wizard = env['base.partner.merge.automatic.wizard'].create({
    'partner_ids': [(6, 0, (keep | dup).ids)], 'dst_partner_id': keep.id,
})
wizard.action_merge()
env.cr.commit()
```

- At most 3 contacts per merge, none parent of another, at most one user among them.
- Different emails need an administrator.
- Merging cannot be undone and deletes records: the user confirms each group. Archiving
  the duplicate (`active=False`) is the safe alternative.
