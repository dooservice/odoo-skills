# account_test — Accounting Consistency Tests

Depends on: account.

## `accounting.assert.test` (defines)

Accounting Assert Test

- `name` Char “Test Name” (required)
- `desc` Text “Test Description”
- `code_exec` Text “Python code” (required)
- `active` Boolean
- `sequence` Integer

## `report.account_test.report_accounttest` (defines)

Account Test Report


Extension points: `_get_report_values`
