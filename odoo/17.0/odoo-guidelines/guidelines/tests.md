# Tests

- Use `TransactionCase` (or `HttpCase` for web); start new business tests from
  `odoo.addons.base.tests.common.BaseCommon` (independent non-admin user and
  company, mail side effects disabled), or
  `TransactionCaseWithUserDemo`/`HttpCaseWithUserDemo` when demo data is
  needed (it is not guaranteed present). Assert behavior, not implementation.
- Tests are tagged `standard` and **`at_install`** by default in 17.0: they run
  before the other modules are installed. Business tests should run on a fully
  loaded registry: decorate them `@tagged('post_install', '-at_install')`. An
  `HttpCase` (tours) must be `post_install`.
- Set exactly one of `at_install`/`post_install`: the check is only a log
  warning, and *both* tags make the class run twice while *neither* makes it
  never run. Tests run only for installed modules.
- Silent skips: a test file must be named `test_*.py` **and** imported from
  `tests/__init__.py`; the test class must be *defined* in that file (a class
  merely imported into it is skipped); and inherited `test_*` methods are not
  collected: a subclass runs nothing of its parent's unless it
  defines its own.
- `assertQueryCount` only when strictly necessary, and never inside a business
  test: it breaks on any unrelated ORM change. Keep it to dedicated
  performance tests, paired with `@warmup` (and `@users`); only *exceeding*
  the budget fails; a lower count merely logs, so keep budgets exact.
- Wrap expected-error and warning logs in `mute_logger(...)` so the expected
  ERROR or WARNING never reaches the log.
- Tours: the last step must leave the client in a stable state (no pending
  edits or in-flight requests), or the teardown races the browser.
- Run them with `odoo-bin -u <module> --test-enable --stop-after-init`; one class
  or method with
  `odoo-bin --test-tags /<module>:<Class>.<method> --stop-after-init`.
