# Employees, time off and expenses

Employees (`hr.employee`) belong to a department and report to a manager; linked to a
user, they request time off and log expenses themselves. Time off is taken from
allocations of a time off type and approved by the manager or a time off officer.
Expenses are logged against an expense category (a product) and, once approved, posted
to accounting as a bill to reimburse the employee or as a payment the company already
made. Needs `hr`, `hr_holidays` and `hr_expense`; payroll and the expense card are
Enterprise and left out. `hr_expense` and `hr_holidays` changed shape between versions:
check `## Versions` before every step.

## Before you start

- Apps: `hr`, `hr_holidays`, `hr_expense` (with `account`).
- Settings: none required. The approvers come from the employee: `leave_manager_id` and
  `expense_manager_id` (users).
- Read first:

```python
print(env['hr.employee'].search_read([], ['name', 'user_id', 'department_id', 'parent_id', 'leave_manager_id', 'company_id']))
print(env['hr.department'].search_read([], ['name', 'manager_id', 'parent_id']))
if 'hr.leave.type' in env:                                                   # 16.0-19.0
    types = env['hr.leave.type'].search([])
else:                                                                        # 20.0
    types = env['hr.work.entry.type'].search([('time_off_selectable', '=', True), ('count_as', '=', 'absence'),
                                              ('country_id', 'in', [False, env.company.country_id.id])])
print(types.read(['name', 'requires_allocation', 'leave_validation_type', 'allocation_validation_type']))
print(env['product.product'].search_read([('can_be_expensed', '=', True)], ['name', 'default_code', 'standard_price']))
```

## The standard flow

1. **Department.** Employees ‣ Departments ‣ New.

   ```python
   department = env['hr.department'].create({'name': '<department>', 'manager_id': manager.id, 'company_id': company.id})
   ```

2. **Employee and their user.** Employees ‣ New; Manager and Department on the Work
   Information tab, the user under Related User (HR Settings tab; Settings from 18.0).

   ```python
   employee = env['hr.employee'].create({
       'name': '<full name>', 'work_email': '<work email>', 'department_id': department.id,
       'parent_id': manager.id, 'user_id': user.id, 'expense_manager_id': manager.user_id.id,
       'company_id': company.id,
   })
   env.cr.commit()
   ```

   The manager's user becomes the time off approver (`leave_manager_id`) and, up to
   19.0, the expense approver; in 20.0 set `expense_manager_id` as above. The coach
   defaults to the manager. The user sees the employee as `user.employee_id`.

3. **Time off type.** Time Off ‣ Configuration ‣ Time Off Types (20.0: Time Types).

   ```python
   leave_type = env['hr.leave.type'].create({                 # 16.0-19.0
       'name': '<type>', 'requires_allocation': 'yes',          # 19.0: True
       'leave_validation_type': 'manager',
       'allocation_validation_type': 'officer',                 # 18.0+: 'hr'
       'request_unit': 'day',
   })
   leave_type = env['hr.work.entry.type'].create({             # 20.0
       'name': '<type>', 'code': '<CODE>', 'count_as': 'absence', 'requires_allocation': True,
       'leave_validation_type': 'manager', 'allocation_validation_type': 'hr',
       'request_unit': 'day', 'unit_of_measure': 'day',
   })
   type_field = 'holiday_status_id' if 'hr.leave.type' in env else 'work_entry_type_id'
   ```

4. **Allocation.** Time Off ‣ Management ‣ Allocations ‣ New (16.0: Approvals ‣
   Allocations), then Validate/Approve.

   ```python
   allocation = env['hr.leave.allocation'].create({
       type_field: leave_type.id, 'employee_id': employee.id, 'number_of_days': 5, 'date_from': '<YYYY-MM-DD>',
   })
   allocation.action_approve()          # 16.0: action_confirm() if draft, then action_validate(); 17.0: action_validate()
   env.cr.commit()
   ```

   Created `confirm` (16.0: `draft`), leaves it `validate`.

5. **Request.** Time Off ‣ New (or My Time ‣ My Time Off), by the employee.

   ```python
   leave = env['hr.leave'].with_user(user).create({
       type_field: leave_type.id, 'employee_id': employee.id,
       'request_date_from': '<YYYY-MM-DD>', 'request_date_to': '<YYYY-MM-DD>',
       # 16.0 also: 'date_from': '<YYYY-MM-DD> 08:00:00', 'date_to': '<YYYY-MM-DD> 17:00:00'
   })
   ```

   Leaves it `confirm` (To Approve); `no_validation` types are approved at once. In
   16.0 the request dates alone give a one-day leave: set `date_from` and `date_to` too
   and check `number_of_days`.

6. **Approval.** Time Off ‣ Management ‣ Time Off (16.0: Approvals ‣ Time Off) ‣ Approve.

   ```python
   leave.with_user(manager_user).action_approve()
   env.cr.commit()
   print(leave.state, leave_type.with_context(employee_id=employee.id).virtual_remaining_leaves)
   ```

   Leaves it `validate` and the days come off the allocation. With
   `leave_validation_type='both'`, the first approval leaves `validate1` and a time off
   officer runs `action_validate()` (20.0: `action_approve()` again).

7. **Expense category.** Expenses ‣ Configuration ‣ Expense Categories (20.0: Expense
   Products) ‣ New.

   ```python
   category = env['product.product'].create({'name': '<category>', 'can_be_expensed': True, 'type': 'service', 'standard_price': 0.0})
   ```

   `standard_price` 0 lets the employee enter the amount; a value fixes the unit cost.
   The expense account is the product's (or its category's) expense account; the taxes
   are its vendor taxes, which the localization decides: see its localization skill if
   installed.

8. **Log and submit.** Expenses ‣ My Expenses ‣ New, Paid By (`payment_mode`):
   `own_account` (employee, to reimburse) or `company_account`.

   ```python
   expense = env['hr.expense'].create({
       'name': '<description>', 'employee_id': employee.id, 'product_id': category.id,
       'total_amount_currency': <amount>, 'payment_mode': 'own_account',   # 16.0: 'total_amount'
   })
   expense.action_submit()                                                   # 19.0+
   sheet = env['hr.expense.sheet'].create({                                  # 16.0-18.0: a report
       'name': '<report>', 'employee_id': employee.id, 'expense_line_ids': [(6, 0, expense.ids)],
   })
   sheet.action_submit_sheet()
   ```

   Up to 18.0 an expense is submitted inside a report (Create Report, Submit to
   Manager), which leaves `submit`; from 19.0 the expense itself is `submitted`.

9. **Approval.** Expenses ‣ Expense Reports (19.0+: My Expenses ‣ Expenses to Process) ‣
   Approve, by the expense approver: `sheet.approve_expense_sheets()` (16.0),
   `sheet.action_approve_expense_sheets()` (17.0, 18.0), `expense.action_approve()`
   (19.0+). Leaves `approve` / `approved`. From 19.0 an expense of an employee without
   approver is approved on submit. 18.0 and 20.0 create the journal entries in draft at
   approval; 18.0 refuses to approve a company-paid expense until an outstanding account
   is set (Settings `expense_outstanding_account_id`, chosen with the accountant).

10. **Post.** Post Journal Entries, by a user with Accounting: Accountant or Adviser and
    Expenses: Manager. 20.0 has no such button: confirm the draft receipt or payment in
    Accounting.

    ```python
    sheet.action_sheet_move_create()        # 16.0, 17.0; 18.0: sheet.action_sheet_move_post()
    action = expense.action_post()          # 19.0: company-paid posts here; employee-paid returns a wizard
    env['hr.expense.post.wizard'].with_context(action['context']).create({}).action_post_entry()
    expense.account_move_id.action_post()   # 20.0 employee-paid; company-paid: account_move_id.origin_payment_id.action_post()
    env.cr.commit()
    ```

    Employee-paid: a vendor bill to the employee (`in_invoice` up to 18.0, `in_receipt`
    from 19.0), expense debited and payable credited, waiting for reimbursement.
    Company-paid: a payment entry in the bank journal against the outstanding payments
    account, already `paid`/`done`.

11. **Reimburse.** Register Payment on the report (16.0-18.0, `sheet.action_register_payment()`)
    or the expense (19.0+, `expense.action_pay()`): the usual payment wizard. Leaves the
    report `done` / the expense `paid`.

## Variations

- Many employees at once: 16.0, 17.0 `holiday_type` on the allocation (`company`,
  `department`, `category`); from 18.0 New Group Allocation, the wizard
  `hr.leave.allocation.generate.multi.wizard`.
- Accrual allocations, earned over time by a scheduled action: an `hr.leave.accrual.plan`
  in `accrual_plan_id` (16.0-19.0 also `allocation_type='accrual'`).
- Expenses sent by email to the expenses alias; receipt scanning is Enterprise.
- Re-invoicing to a customer (`sale_expense`): the category's `expense_policy` (`cost`,
  `sales_price`) and the sales order on the expense.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Time off type | `hr.leave.type` | same | same | same, `requires_allocation` boolean | `hr.work.entry.type` (`work_entry_type_id`) |
| Allocation approval | `draft` → `action_confirm`, `action_validate` | `action_validate` | `action_approve` | same | same |
| Expense amount | `total_amount` | `total_amount_currency` | same | same | same |
| Submit / approve | report `hr.expense.sheet` | same | same | on the expense | same |
| Employee-paid entry | `in_invoice` on post | same | same | `in_receipt` on post | `in_receipt` created draft on approval |
| Employee's partner | private address `address_home_id` (required to post) | `work_contact_id` | same | same | same |
| Expense approver from manager | yes | yes | yes | yes | no: set `expense_manager_id` |
| Entries created | at post | at post | draft at approval | at post | draft at approval |

## Verify

```python
print(employee.user_id.login, employee.leave_manager_id.name, employee.expense_manager_id.name)
print(leave.state, leave_type.with_context(employee_id=employee.id).virtual_remaining_leaves)
moves = expense.sheet_id.account_move_ids if 'sheet_id' in expense._fields else expense.account_move_id   # 16.0: sheet_id.account_move_id
for move in moves:
    print(move.name, move.move_type, move.state, [(l.account_id.code, l.debit, l.credit) for l in move.line_ids])
```

## Pitfalls

- 16.0: posting an employee-paid report fails until the employee has a private address
  (`address_home_id`). Create it with the user's yes; it holds personal data.
- A new category takes the company's default purchase taxes; with them, part of the
  amount goes to a tax account. Check `supplier_taxes_id` with the accountant.
- The shell runs as superuser: requests and approvals made there skip the checks of who
  may approve. Act `with_user()` as the employee and the approver, as above.
- 20.0: time types include working-time entries and other countries' types; filter by
  `time_off_selectable`, `count_as` and `country_id` as in the read-first snippet.
- Approved time off and posted expenses are history: refuse or reset them with Odoo's
  Refuse and Reset buttons, never by writing `state`.
