# Go-live: loading a new company's data

Loading a new company on day one, in Odoo's order: configuration, master data, then the
opening entries from the old system (open invoices and bills, stock count, trial balance,
bank). Agree on the go-live date (ideally the start of a fiscal year): before it is
opening entries, from it is Odoo. Opening entries need the accountant's figures and the
user's yes before posting. Bank synchronization is Enterprise.

## Before you start

- Apps: `account`, plus `stock`, `sale`, `purchase` as used, installed first (they add
  settings, journals, sequences).
- Settings: Journal Entries and Chart of Accounts menus need the user group
  `account.group_account_readonly` ("Show Accounting Features - Readonly").
- Read first:

```python
company = env.company
print(company.name, company.country_id.code, company.currency_id.name, company.account_opening_date, company.account_opening_move_id.name)
print(env['ir.module.module'].search([('state', '=', 'installed'), ('application', '=', True)]).mapped('name'))
print(env['account.journal'].search_read([('company_id', '=', company.id)], ['code', 'type']))
for model in ('res.users', 'res.partner', 'product.product', 'account.move', 'stock.quant'):
    print(model, env[model].search_count([]))
```

If entries or stock are already posted, this is not day one: ask what was loaded.

## The standard flow

1. **Company, settings, users.** Settings ‣ Users & Companies ‣ Companies / Users;
   Invoicing ‣ Configuration ‣ Settings: `companies.md`, `users-and-access.md`,
   `currencies-and-rates.md`, `languages-and-translations.md`, `reports-and-layout.md`.
2. **Accounting master data.** Invoicing ‣ Configuration ‣ Accounting ‣ Chart of Accounts:
   rename or recode standard accounts, never delete them; then journals, fiscal positions,
   taxes, payment terms (`taxes-and-journals.md`, `payment-terms-and-fiscal-positions.md`).
   The chart is the localization's; see its localization skill if installed.
3. **Product categories, products, then contacts:** `products-and-categories.md`,
   `pricelists.md`, `purchase.md`, `partners-and-imports.md`.
4. **Open invoices and bills.** Invoicing ‣ Customers ‣ Invoices and Invoicing ‣ Vendors ‣
   Bills, Import: per open document its number and date, one line with the amount due, no
   taxes, on a clearing account (type current asset) instead of income or expense.

   ```python
   ar_clearing, ap_clearing = env['account.account'].create([
       {'code': '<account code>', 'name': 'Receivable clearing', 'account_type': 'asset_current'},
       {'code': '<account code>', 'name': 'Payable clearing', 'account_type': 'asset_current'},
   ])
   invoice = env['account.move'].create({
       'move_type': 'out_invoice', 'partner_id': partner.id, 'name': '<old number>',
       'invoice_date': '<original date>', 'invoice_date_due': '<original due date>',
       'invoice_line_ids': [(0, 0, {'name': 'Open balance of <old number>', 'account_id': ar_clearing.id,
                                    'quantity': 1, 'price_unit': 1200.0, 'tax_ids': [(6, 0, [])]})],
   })
   invoice.action_post()
   env.cr.commit()
   ```

   Leaves it `posted`, `not_paid`, on the partner's receivable. Bills: `in_invoice`, vendor
   number in `ref`, `ap_clearing`. Totals must equal the old receivables and payables.
5. **Opening inventory.** Costs (`standard_price`) first. Stock count menu (per version
   below), Apply, reason "Opening inventory". Lots, locations: `inventory.md`.

   ```python
   warehouse = env['stock.warehouse'].search([('company_id', '=', company.id)], limit=1)
   quants = env['stock.quant']
   for product, quantity in {env['product.product'].search([('default_code', '=', '<reference>')], limit=1): 40}.items():
       quants |= env['stock.quant'].with_context(inventory_mode=True).create({
           'product_id': product.id, 'location_id': warehouse.lot_stock_id.id, 'inventory_quantity': quantity})
   quants.with_context(inventory_name='Opening inventory').action_apply_inventory()
   env.cr.commit()
   ```

   Leaves `done` moves "Opening inventory". Quantity × cost must equal the old stock
   accounts; with automated valuation the count posts it too: agree who carries it.
6. **Opening trial balance.** Journal Entries (per version below), Import: one miscellaneous
   entry the day before go-live, receivables and payables on the clearing accounts.

   ```python
   import datetime
   company.account_opening_date = datetime.date(2026, 1, 1)    # the go-live date
   company_field = 'company_ids' if 'company_ids' in env['account.account']._fields else 'company_id'
   def account(code):
       return env['account.account'].search([('code', '=', code), (company_field, 'in', company.ids)], limit=1)
   misc = env['account.journal'].search([('company_id', '=', company.id), ('type', '=', 'general')], limit=1)
   opening = env['account.move'].create({
       'move_type': 'entry', 'journal_id': misc.id, 'ref': 'Opening balance',
       'date': company.account_opening_date - datetime.timedelta(days=1),
       'line_ids': [
           (0, 0, {'account_id': account('<account code>').id, 'name': 'Bank', 'debit': 5000.0}),
           (0, 0, {'account_id': ar_clearing.id, 'name': 'Receivables', 'debit': 1200.0}),
           (0, 0, {'account_id': ap_clearing.id, 'name': 'Payables', 'credit': 700.0}),
           (0, 0, {'account_id': account('<account code>').id, 'name': 'Capital', 'credit': 5500.0}),
       ],
   })
   opening.action_post()
   company.account_opening_move_id = opening
   env.cr.commit()
   ```

   Leaves one `posted`, balanced entry: the Chart of Accounts' opening balances.
7. **Opening bank statements**, starting balance before the first transaction:
   `bank-and-reconciliation.md`.
8. **Final validation.** Clearing accounts at zero, then retired (Pitfalls: not Off-Balance).

   ```python
   for clearing in ar_clearing | ap_clearing:
       print(clearing.code, sum(env['account.move.line'].search([('account_id', '=', clearing.id), ('parent_state', '=', 'posted')]).mapped('balance')))
   (ar_clearing | ap_clearing).write({'deprecated': True} if 'deprecated' in ar_clearing._fields else {'active': False})
   env.cr.commit()
   ```

9. **Numbering and lock:** `sequences.md`, then lock before go-live (`closing-the-period.md`).

## Variations

- **Old numbers in another format**: later invoices of that year would follow it; use a
  separate journal (`taxes-and-journals.md`).
- **No documents**: one opening-entry line per open item on the receivable or payable
  account with `partner_id`, `date_maturity`, old number in `name`. No portal or reminders.
- **Opening Debit / Credit columns** of the Chart of Accounts (16.0 to 18.0 docs): a draft
  opening entry the day before `account_opening_date`; an "Automatic Balancing Line" means
  the figures do not add up: ask, do not post.
- **Invoice numbers continue**: name the journal's first draft invoice, then post.

  ```python
  first_invoice.name = 'INV/2026/01500'
  first_invoice.action_post()
  env.cr.commit()
  ```

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Journal Entries | Invoicing ‣ Accounting ‣ Journals ‣ Journal Entries | same | Invoicing ‣ Accounting ‣ Journal Entries | Invoicing ‣ Accounting ‣ Transactions ‣ Journal Entries | same |
| Stock count | Inventory ‣ Operations ‣ Inventory Adjustments | Inventory ‣ Operations ‣ Adjustments ‣ Physical Inventory | same | same | same |
| `account_opening_date` default | 1 January | 1 January | 1 January | empty | today |
| Accounts by company | `company_id` | `company_id` | `company_ids` | `company_ids` | `company_ids` |
| Stock product | `detailed_type='product'` | same | `is_storable=True` | same | same |
| Retire an account | `deprecated` | `deprecated` | `deprecated` | `active` | `active` |

## Verify

```python
lines = env['account.move.line'].search([('company_id', '=', company.id), ('parent_state', '=', 'posted'),
                                         ('date', '<', company.account_opening_date)])
balances = {}
for line in lines:
    balances[line.account_id.code] = balances.get(line.account_id.code, 0) + line.balance
print(sorted(balances.items()))
print(partner.credit, vendor.debit, product.qty_available)
```

Compare with the old trial balance, open items per partner (`credit` owed by a customer,
`debit` owed to a vendor) and the count; then post a test invoice and payment.

## Pitfalls

- The 19.0+ docs end by turning clearing accounts Off-Balance Sheet; with entries, every
  version refuses it on save ("all the accounts of the journal entry must be of this
  type"). Retire them instead.
- One receivable total without partner cannot be matched with payments: one item each.
- Foreign-currency items need `currency_id` and `amount_currency` on the line.
- Opening invoices outside e-invoicing: the country's localization decides this; see its
  localization skill if installed.
