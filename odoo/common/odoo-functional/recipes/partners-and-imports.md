# Partners and imports

Customers, vendors, employees' addresses and the contacts inside a company are all
`res.partner`. A company record holds the commercial data (VAT, payment terms,
pricelist, fiscal position); the people and addresses under it point to it with
`parent_id` and share that data. Bulk loads go through `load()` with external ids, so a
second run updates instead of creating duplicates. This recipe needs only `contacts`
(the app) on top of `base`; what a country adds to a partner belongs to its
localization skill.

## Before you start

- Apps: `contacts` for the menus (the model is in `base`); `account` for payment terms
  and fiscal positions; `product` for pricelists; `base_vat` (16.0 to 19.0) for VAT
  checks.
- Settings: none for contacts. Pricelists on partners need `group_product_pricelist`
  (`pricelists.md`); `vat_check_vies` (VIES check) is a company setting.
- Read first:

```python
partner = env['res.partner'].search([('vat', '=', '<vat number>'), ('parent_id', '=', False)])
print(partner.read(['name', 'is_company', 'parent_id', 'type', 'country_id', 'vat', 'user_id', 'lang', 'active']))
print(partner.child_ids.mapped('name'), partner.commercial_partner_id.name)
print(env['ir.model.data'].search([('model', '=', 'res.partner'), ('res_id', '=', partner.id)]).mapped('complete_name'))
```

Contacts under a company get the company's VAT, so a search by VAT alone also returns
them: filter on `parent_id`.

## The standard flow

The order of Odoo's Contacts documentation: the company, the people and addresses under
it, its sales and purchase data; then bulk loads and merging duplicates.

1. **Create the tags you will use.** Contacts ‣ Configuration ‣ Contact Tags.

   ```python
   distributor = env['res.partner.category'].create({'name': 'Distributor'})
   env.cr.commit()
   ```

   Leaves a tag (`res.partner.category`, Many2many `category_id` on the partner).

2. **Create the company.** Contacts ‣ Contacts ‣ New, with Company selected (16.0 to
   19.0; in 20.0 the VAT makes it a company).

   ```python
   acme = env['res.partner'].create({
       'name': 'Acme Industrial', 'is_company': True,
       'country_id': env.ref('base.<country code>').id, 'vat': '<vat number>',
       'category_id': [(4, distributor.id)],
       'user_id': salesperson.id,
   })
   env.cr.commit()
   ```

   Leaves an active company contact, its own commercial partner.

   - `base.<country code>` is the lowercase ISO code
     (`env['res.country'].search([('name', 'ilike', ...)]).code`). A VAT number must be
     a real, valid one for that country; never invent one.
   - 16.0 to 19.0: `is_company` is a plain boolean, with `company_type` (`person`,
     `company`) as its form widget. 20.0: `is_company` is computed (a contact without
     parent and with a VAT is a company) and `company_type` is gone: writing
     `is_company` has no effect, the VAT decides.
   - VAT is checked against the country by `base_vat` (16.0 to 19.0, only when
     installed; without it any text is accepted) or by `base` itself (20.0). Set
     `country_id` before or with `vat`. `vat_check_vies` (company setting, `base_vat` up
     to 19.0, `account` in 20.0) adds an online check against the VIES service. The
     country's localization decides the VAT format and other partner fields; see its
     localization skill if installed.
   - Salesperson: `user_id`. 16.0 and 17.0 also have a default sales team `team_id` on
     the partner; 18.0 removed it.

3. **Add its people and addresses.** The company form, Contacts & Addresses tab
   (Contacts in 19.0+).

   ```python
   env['res.partner'].create({'name': 'Laura Grey', 'parent_id': acme.id, 'type': 'contact', 'email': 'laura@acme.example'})
   env['res.partner'].create({'name': 'North warehouse', 'parent_id': acme.id, 'type': 'delivery', 'city': '<city>'})
   env.cr.commit()
   ```

   Leaves child contacts whose `commercial_partner_id` is the company.

   - `type`: `contact`, `invoice`, `delivery`, `other`; 16.0 also has `private`.
   - Commercial fields (VAT, payment terms, pricelist, fiscal position) are synced from
     the company to its children: set them on the company, not on each contact.

4. **Set payment terms, pricelist and fiscal position.** The company form, Sales &
   Purchase tab. These are company-dependent: each company sees its own value, so write
   them per company.

   ```python
   acme.with_company(company).write({
       'property_payment_term_id': env.ref('account.account_payment_term_30days').id,
       'property_supplier_payment_term_id': env.ref('account.account_payment_term_30days').id,
       'property_product_pricelist': pricelist.id,
       'property_account_position_id': fiscal_position.id,
   })
   env.cr.commit()
   ```

   Leaves the values that new quotations, orders and invoices of that company take.

   - 16.0 and 17.0 store these values in `ir.property`; 18.0+ in a JSON column on the
     partner. Through the ORM the code is the same; a SQL query is not.
   - `property_product_pricelist` is computed (by country when empty) with an inverse;
     from 18.0 the stored value is `specific_property_product_pricelist`. Write the
     first. From 19.0 it reads empty while pricelists are off in Settings
     (`pricelists.md`).

5. **Test the bulk load.** Contacts ‣ Contacts, then Favorites ‣ Import records (16.0) or
   the Actions (gear) menu ‣ Import records (17.0+), and Test. `Model.load(fields, rows)`
   is what the import screen calls; Test runs it and rolls it back.

   ```python
   fields = ['id', 'name', 'is_company', 'country_id/id', 'vat', 'category_id/id', 'parent_id/id', 'email']
   rows = [
       ['cust_0001', 'Harbor Foods', '1', 'base.<country code>', '<vat number>', '', '', 'info@harbor.example'],
       ['cust_0001_c1', 'Mark Harbor', '0', 'base.<country code>', '', '', 'cust_0001', 'mark@harbor.example'],
   ]
   class DryRun(Exception):
       pass
   try:
       with env.cr.savepoint():
           result = env['res.partner'].load(fields, rows)
           print(result['ids'], result['messages'])
           raise DryRun
   except DryRun:
       pass
   ```

   Leaves nothing: it only reports what the import would do.

   - Give every row an external id in the `id` column: a bare name like `cust_0001`
     becomes `__import__.cust_0001`, and loading the same id again updates that record.
     Never use a real module as prefix: a module update would delete the record.
   - `field/id` takes an external id, `field` alone a display name (ambiguous names
     fail); Many2many takes several ids separated by commas.
   - Before loading, search for existing records by VAT or email and map them to the
     file's ids, or the load creates duplicates.

6. **Import.** The same screen, Import.

   ```python
   result = env['res.partner'].load(fields, rows)
   print(result['ids'], result['messages'])
   if not result['messages']:
       env.cr.commit()
   ```

   Leaves one partner per row, each with an `__import__` external id.

   - `load` does not raise: check `messages`. On any error `ids` is `False` and nothing
     from that call is kept. Commit only when there are no errors.
   - Run a sample of 5 to 10 rows first, read them back, then the whole file. The full
     load needs the user's yes, with the row count.

7. **Merge duplicates.** Contacts ‣ Contacts, list view, select the duplicates, Actions ‣
   Merge. The wizard `base.partner.merge.automatic.wizard` (in `base`, all versions)
   moves every reference to a destination contact and deletes the others.

   ```python
   wizard = env['base.partner.merge.automatic.wizard'].create({
       'partner_ids': [(6, 0, (keep | dup).ids)], 'dst_partner_id': keep.id,
   })
   wizard.action_merge()
   env.cr.commit()
   ```

   Leaves `keep` with the references of the others, which no longer exist.

   - At most 3 contacts per merge, none parent of another; from 17.0 at most one user
     among them.
   - Different emails need an administrator.
   - Merging cannot be undone and deletes records: the user confirms each group.

## Variations

- **Update records that were not imported.** Records created without external ids (by
  hand or by `create`) get one when exported with "import-compatible"
  (`__export__.res_partner_42_...`): export, edit, re-import.
- **Archive instead of merge.** Archiving the duplicate (`active=False`) is the safe
  alternative: nothing is deleted and it can be undone.
- **Vendors.** The same form, reached from Purchase ‣ Orders ‣ Vendors; vendor payment
  terms are `property_supplier_payment_term_id`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Company or person | `is_company` (`company_type` widget) | same | same | same | computed from parent and VAT; no `company_type` |
| VAT check | `base_vat` when installed | same | same | same | `base` |
| `vat_check_vies` from | `base_vat` | same | same | same | `account` |
| `type` values | `contact`, `invoice`, `delivery`, `other`, `private` | no `private` | same | same | same |
| Default sales team on partner | `team_id` | `team_id` | gone | gone | gone |
| Company-dependent values | `ir.property` | `ir.property` | JSON column | JSON column | JSON column |
| Pricelist stored in | `property_product_pricelist` | same | `specific_property_product_pricelist` | same, empty while pricelists are off | same |
| Merge: at most one user | no | yes | yes | yes | yes |
| Form tab for people and addresses | Contacts & Addresses | same | same | Contacts | Contacts |
| Import records | Favorites ‣ Import records | Actions (gear) ‣ Import records | same | same | same |
| Menu: bank accounts | Contacts ‣ Configuration ‣ Bank Accounts ‣ Bank Accounts | same | same | same | Contacts ‣ Configuration ‣ Bank Accounts |

The same in every version: Contacts ‣ Contacts, Contacts ‣ Configuration ‣ Contact Tags,
Sales ‣ Orders ‣ Customers, Purchase ‣ Orders ‣ Vendors, Invoicing ‣ Customers ‣
Customers.

## Verify

```python
acme.invalidate_recordset()
print(acme.read(['name', 'is_company', 'vat', 'category_id', 'user_id']))
print([(c.name, c.type, c.commercial_partner_id.name, c.vat) for c in acme.child_ids])
print(acme.with_company(company).property_payment_term_id.name, acme.with_company(company).property_product_pricelist.name)
print(env['ir.model.data'].search([('module', '=', '__import__'), ('model', '=', 'res.partner')]).mapped('name'))
```

Children show the company as commercial partner and its VAT; the per-company values read
back for that company; each imported row has its `__import__` id.

## Pitfalls

- A search by VAT returns the company and all its contacts: add
  `('parent_id', '=', False)`.
- Commercial fields written on a child are overwritten from the company: write them on
  the company.
- Values written without `with_company()` only apply to the current company.
- Loading without an `id` column creates new records on every run: always give external
  ids.
- An external id under a real module's name (`sale.cust_0001`) is deleted by the next
  update of that module.
- In 20.0, writing `is_company=True` on a contact without VAT does nothing.
- Merging is final; when in doubt, archive.
