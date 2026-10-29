# Analytic accounting: plans, accounts and distributions

Analytic accounting tracks costs and revenues by project, department or any other axis,
next to the financial accounts. Each axis is an analytic plan (`account.analytic.plan`)
holding analytic accounts (`account.analytic.account`). A journal item, sale line,
purchase line or expense carries an analytic distribution (`analytic_distribution`, a
JSON of analytic account ids and percentages); posting the journal item writes analytic
items (`account.analytic.line`) with the amounts. Distribution models
(`account.analytic.distribution.model`) fill the distribution by partner, product or
account. This recipe covers `analytic` with the Invoicing app (`account`), all in
Community; budgets (`account_budget`) and the Accounting app's analytic reports are
Enterprise and left out.

## Before you start

- Apps: `account` (it installs `analytic`).
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ Analytics):

```python
env['res.config.settings'].create({'group_analytic_accounting': True}).execute()
env.cr.commit()
```

- `group_analytic_accounting` adds the user group `analytic.group_analytic_accounting`
  and shows the analytic menus and columns. The Analytics block is visible only to users
  with "Show Full Accounting Features" (`account.group_account_user`); in Community an
  administrator gets that group from Settings ‣ Users ‣ the user, in developer mode.
- Ticking the box in the form also ticks `module_account_accountant` (an onchange), which
  installs the Enterprise Accounting app. In Community, untick it before saving; the
  script above does not run the onchange.
- Read first:

```python
print(env.user.has_group('analytic.group_analytic_accounting'))
print(env['account.analytic.plan'].search_read([], ['complete_name', 'parent_id', 'default_applicability']))
print(env['account.analytic.account'].search_read([], ['name', 'code', 'plan_id', 'company_id', 'active']))
print(env['account.analytic.distribution.model'].search_read([], ['partner_id', 'product_id', 'account_prefix', 'analytic_distribution']))
print(env['ir.config_parameter'].sudo().get_param('analytic.project_plan'))
```

  The `analytic.project_plan` parameter exists from 17.0; in 16.0 it reads `False`.

## The standard flow

The order of Odoo's analytic accounting documentation: plans, accounts, then the
distribution on documents, and the reports.

1. **Create the analytic plans.** Invoicing ‣ Configuration ‣ Analytic Accounting ‣
   Analytic Plans ‣ New. One plan per axis (`Departments`, `Projects`); a plan with a
   `parent_id` is a subplan of it.

   ```python
   plan = env['account.analytic.plan'].create({'name': 'Departments', 'default_applicability': 'optional'})
   env.cr.commit()
   ```

   Leaves a root plan. `default_applicability`: `optional` (the distribution may be
   left empty), `mandatory` (posting fails without 100% on this plan), `unavailable`
   (the plan is hidden on documents). From 17.0 it is company dependent.

   - From 17.0 each root plan is a column of the analytic items: the plan stored in
     the system parameter `analytic.project_plan` (the `Projects` plan the module
     creates) is `account_id`, every other root plan `x_plan<id>_id`.
   - 16.0 has no such columns: an analytic item has one `account_id` and its `plan_id`.

2. **Set where a plan is mandatory.** The plan form ‣ Applicability tab ‣ Add a line.

   ```python
   plan.write({'applicability_ids': [(0, 0, {
       'business_domain': 'bill', 'applicability': 'mandatory', 'account_prefix': '6',
   })]})
   env.cr.commit()
   ```

   Leaves vendor bill lines on accounts starting with `6` blocked at posting until they
   carry 100% on this plan. `business_domain`: `general` (Miscellaneous), `invoice`,
   `bill`; `sale`, `purchase` and `expense` come with `sale`, `purchase` and
   `hr_expense`. `account_prefix` (several prefixes separated by commas from 18.0) and
   `product_categ_id` narrow the rule; the most specific rule wins. From 18.0 a rule
   has a `company_id`.

3. **Create the analytic accounts.** Invoicing ‣ Configuration ‣ Analytic Accounting ‣
   Analytic Accounts ‣ New.

   ```python
   sales = env['account.analytic.account'].create({'name': 'Sales department', 'code': 'SAL', 'plan_id': plan.id})
   admin = env['account.analytic.account'].create({'name': 'Administration', 'code': 'ADM', 'plan_id': plan.id})
   env.cr.commit()
   ```

   Leaves two accounts in the plan. `company_id` empty shares the account with every
   company; `partner_id` is informative.

4. **Add distribution models.** Invoicing ‣ Configuration ‣ Analytic Accounting ‣
   Analytic Distribution Models ‣ New. A model fills the distribution of new lines that
   match its conditions.

   ```python
   env['account.analytic.distribution.model'].create({
       'partner_id': partner.id,
       'account_prefix': '6',
       'analytic_distribution': {str(sales.id): 60, str(admin.id): 40},
   })
   env.cr.commit()
   ```

   Leaves a model that splits this vendor's expenses 60/40. Conditions: `partner_id`,
   `partner_category_id`, `product_id`, `product_categ_id`, `account_prefix`,
   `company_id`; empty conditions match everything. From 18.0 `sequence` orders models
   and several models can apply on different plans.

5. **Distribute a document's lines.** The invoice, bill or journal entry ‣ the line's
   Analytic Distribution column (Analytic in 16.0); sales orders, purchase orders and
   expenses carry the same column and pass it on to the invoice.

   ```python
   from odoo import fields
   bill = env['account.move'].create({
       'move_type': 'in_invoice', 'partner_id': partner.id, 'invoice_date': fields.Date.today(),
       'invoice_line_ids': [(0, 0, {
           'name': 'Office rent', 'quantity': 1, 'price_unit': 1000,
           'analytic_distribution': {str(admin.id): 100},
       })],
   })
   bill.action_post()
   env.cr.commit()
   ```

   Leaves the bill posted and one analytic item of -1000 on `Administration`. Posting
   checks the mandatory plans; a missing distribution raises "One or more lines require
   a 100% analytic distribution". Posting is an accounting change: only with the user's
   yes.

6. **Read the results.** Invoicing ‣ Accounting ‣ Analytic Items (menu by version in
   `## Versions`), grouped by analytic account; from 17.0 also Invoicing ‣ Reporting ‣
   Management ‣ Analytic Report (Analytic Reporting in 17.0), a pivot of journal items
   by analytic account. The analytic account form's smart buttons show its items.

## Variations

- **Several plans on one line** (17.0+): one key joins an account of each plan,
  `{"<sales_id>,<project_id>": 100}`; the analytic item gets both columns. Two keys of
  different plans, `{"<sales_id>": 100, "<project_id>": 100}`, give two items, one per
  plan. In 16.0 only the second form exists.
- **Split one line**: `{"<sales_id>": 60, "<admin_id>": 40}` writes two items with 60%
  and 40% of the amount. A plan with less than 100% leaves the rest unallocated.
- **Correct an analytic item** (18.0+): edit the item's account or amount in Analytic
  Items; the journal item's distribution follows. Up to 17.0 change the journal item's
  distribution instead (reset the entry to draft first, with the user's yes).
- **Manual analytic items**: Analytic Items ‣ New, for costs that are not in the
  accounts (`category` `other`).
- **Manufacturing**: `mrp_account` puts a distribution on manufacturing orders and
  work centers (`inventory-valuation.md`).

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Item columns | `account_id`, `plan_id` | `account_id` (project plan), `x_plan<id>_id` per root plan | same | same | same |
| Several plans in one key | no | `"id1,id2"` | same | same | same |
| `default_applicability` | per plan | company dependent | same | same | same |
| Applicability `company_id` | no | no | yes | yes | yes |
| Distribution model `sequence` | no | no | yes | yes | yes |
| Edit items syncs the journal item | no | no | yes | yes | yes |
| Menu: analytic items | Invoicing ‣ Accounting ‣ Management ‣ Analytic Items | same | Invoicing ‣ Accounting ‣ Analytic Items | Invoicing ‣ Accounting ‣ Transactions ‣ Analytic Items | same |
| Menu: analytic report | none | Invoicing ‣ Reporting ‣ Management ‣ Analytic Reporting | Invoicing ‣ Reporting ‣ Management ‣ Analytic Report | same | same |

The same in every version: Invoicing ‣ Configuration ‣ Analytic Accounting ‣ Analytic
Plans, Analytic Accounts and Analytic Distribution Models.

## Verify

```python
print(env['account.analytic.line'].search_read([('move_line_id.move_id', '=', bill.id)], ['account_id', 'amount', 'date']))
print(env['account.analytic.account'].browse(admin.id).read(['balance', 'debit', 'credit']))
```

Each distributed line has its analytic items, the amounts follow the percentages, and
the account balances match.

## Pitfalls

- An analytic account with analytic items cannot change company: decide `company_id`
  when creating it, and leave accounts shared by several companies without one.
- Making a plan mandatory blocks posting of every matching line without distribution,
  including imports and automatic entries: add the rule after the documents in progress
  are distributed, and tell the user.
- Distribution models apply only to new lines; existing documents keep their
  distribution.
- Archiving an analytic account keeps its items; deleting it is refused once items
  exist.
- Changing the project plan parameter (`analytic.project_plan`) moves columns: never do
  it on a database with analytic items.
