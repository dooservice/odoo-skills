# Accounting controls: audit trail, consistency tests, tax grids

Three controls an accountant or auditor uses on the books. The audit trail logs every
change to journal entries, accounts, taxes and partners and forbids deleting posted
entries (`account_audit_trail` in 17.0; in `account` from 18.0). Accounting tests
(`account_test`) run consistency checks written as small queries and print the result.
Updating tax grids (`account_update_tax_tags`) rewrites the tax report grids on journal
items already posted, after the tax report changed. All in Community. Whether an audit
trail is mandatory and how long logs are kept is decided by the country's law and
localization (some force it on): it is not covered here, so check it with the user. The
lock dates and closing are in `closing-the-period.md`.

**At a glance**

- Apps: `account`; `account_audit_trail` (17.0); `account_test`, `account_update_tax_tags`.
- Names that change by version: audit trail absent (16.0), `account_audit_trail` with
  `check_account_audit_trail` (17.0), in `account` with `check_account_audit_trail`
  (18.0), `restrictive_audit_trail` and `force_restrictive_audit_trail` (19.0+); audit
  trail menu under Invoicing ‣ Reporting ‣ Management (17.0, 18.0), Invoicing ‣ Review ‣
  Logs (19.0), Invoicing ‣ Review ‣ Control (20.0).
- Sections: Before you start; The standard flow (1 turn on the audit trail, 2 read the
  trail, 3 run the accounting tests, 4 update tax grids); Variations; Versions; Verify;
  Pitfalls.

## Before you start

- Apps: `account`; `account_audit_trail` (17.0), `account_test` and
  `account_update_tax_tags` from Apps. Installing needs the user's yes.
- Settings (Invoicing ‣ Configuration ‣ Settings ‣ Audit Trail, 17.0, 18.0;
  Reporting ‣ Restrictive Audit Trail, 20.0):

```python
env['res.config.settings'].create({'restrictive_audit_trail': True}).execute()
env.cr.commit()
```

  This is 19.0 and 20.0; in 19.0 Community the setting is hidden (its block needs the
  Enterprise reports), so it is set this way. In 17.0 and 18.0 the field is
  `check_account_audit_trail`. 16.0 has no audit trail.
- Read first:

```python
print(env.company.read(['restrictive_audit_trail', 'force_restrictive_audit_trail']))
print(env['ir.module.module'].search_read([('name', 'in', ['account_test', 'account_update_tax_tags'])], ['name', 'state']))
```

  This is 19.0 and 20.0; in 17.0 and 18.0 read `check_account_audit_trail`.

## The standard flow

1. **Turn on the audit trail.** The setting above, per company.

   Leaves the company protected: a journal entry that was ever posted cannot be deleted
   ("To keep the audit trail, you can not delete journal entries once they have been
   posted"); cancel it instead. Changes to posted entries, accounts, taxes, partners and
   the company are logged. `force_restrictive_audit_trail` (19.0+) is set by
   localizations that make it compulsory, and then the setting cannot be turned off.

2. **Read the trail.** Invoicing ‣ Reporting ‣ Management ‣ Audit Trail (17.0, 18.0),
   Invoicing ‣ Review ‣ Logs ‣ Audit Trail (19.0), Invoicing ‣ Review ‣ Control ‣ Audit
   Trail (20.0). Filters by Journal Entry, Account, Taxes, Partners, Company; group by
   date or record.

   ```python
   logs = env['mail.message'].search_read([
       ('message_type', '=', 'notification'),
       ('model', 'in', ('account.move', 'account.account', 'account.tax', 'res.partner', 'res.company')),
   ], ['date', 'model', 'res_id', 'author_id', 'tracking_value_ids'], limit=20, order='date desc')
   print(logs)
   ```

   Each line is a change with its author, date and old and new values.

3. **Run the accounting tests.** Invoicing ‣ Reporting ‣ Accounting Tests (developer
   mode); select tests ‣ Print ‣ Accounting Tests. The module ships tests such as "Test
   1: General balance" and "Test 3: Movement lines"; add your own with New: `name`,
   `desc`, `code_exec` (Python that fills `result` from queries).

   ```python
   tests = env['accounting.assert.test'].search([])
   pdf, _ = env['ir.actions.report']._render_qweb_pdf('account_test.account_assert_test_report', tests.ids)
   ```

   Leaves a PDF listing, per test, the records that break it; an empty test passed.

4. **Update tax grids after a tax report change.** Invoicing ‣ Configuration ‣ Settings
   (developer mode) ‣ Update tax tags on existing Journal Entries
   (`account.update.tax.tags.wizard`): Starting from (`date_from`, defaulting to the day
   after the tax lock date), then Update.

   ```python
   wizard = env['account.update.tax.tags.wizard'].create({'date_from': '2026-01-01'})
   wizard.update_amls_tax_tags()
   env.cr.commit()
   ```

   Leaves the journal items from that date with the grids of the taxes' current
   distribution lines. It changes posted entries: only with the accountant's yes, and
   never before the tax lock date (the wizard warns).

## Variations

- **Deleting a protected entry anyway**: impossible from the interface; the shell's
  `with_context(force_delete=True)` deletes it and only writes the entry's details to
  the server log. Do not
  use it without a written instruction from the accountant.
- **A test of your own**: `code_exec` runs as Python with `cr` and must set `result`
  (a list or a dictionary of the failing rows). Keep it read-only.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Audit trail | no | `account_audit_trail`, `check_account_audit_trail` | in `account`, `check_account_audit_trail` | `restrictive_audit_trail`, `force_restrictive_audit_trail` | same |
| Setting visible in Community | no | Audit Trail block | same | no (Enterprise reports block) | Reporting block |
| Menu: audit trail | none | Invoicing ‣ Reporting ‣ Management ‣ Audit Trail | same | Invoicing ‣ Review ‣ Logs ‣ Audit Trail | Invoicing ‣ Review ‣ Control ‣ Audit Trail |

The same in every version: Invoicing ‣ Reporting ‣ Accounting Tests (developer mode);
the Update tax tags button in Invoicing ‣ Configuration ‣ Settings (developer mode).

## Verify

```python
move = env['account.move'].search([('company_id', '=', env.company.id), ('posted_before', '=', True), ('state', '!=', 'posted')], limit=1)
try:
    with env.cr.savepoint():
        move.unlink()
except Exception as error:
    print('protected:', error)
```

The unlink of an entry that was posted once (now draft or cancelled) fails with the
audit trail message; the savepoint undoes nothing else. For the tax grids, the journal items
after `date_from` show the new grids (`tax_tag_ids`).

## Pitfalls

- Turning the audit trail on does not log the past: decide it before go-live.
- With the audit trail on, wrong entries are cancelled or reversed, never deleted:
  explain it to users who used to delete drafts that had been posted once.
- Updating tax grids rewrites already declared periods if `date_from` is too early:
  start after the last filed tax return.
- Accounting tests run Python written by a user: only administrators should edit them.
