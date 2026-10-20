# Tests

- Use `TransactionCase` (or `HttpCase` for web); start new business tests from
  `odoo.addons.base.tests.common.BaseCommon` (independent non-admin user and
  company, mail side effects disabled), or
  `TransactionCaseWithUserDemo`/`HttpCaseWithUserDemo` when demo data is
  needed (it is not guaranteed present). Assert behavior, not implementation.
$tags
- Silent skips: a test file must be named `test_*.py` **and** imported from
  `tests/__init__.py`; the test class must be *defined* in that file (a class
  merely imported into it is skipped); and inherited `test_*` methods are not
  collected: a subclass runs nothing of its parent's unless it$inherited
- `assertQueryCount` only in dedicated performance tests, never inside a
  business test: it breaks on any unrelated ORM change.
- Wrap expected-error and warning logs in `mute_logger(...)` so the expected
  ERROR or WARNING never reaches the log.
$tour
- Run them with `odoo-bin -u <module> --test-enable --stop-after-init`; one class
  or method with
  `odoo-bin --test-tags /<module>:<Class>.<method> --stop-after-init`.
