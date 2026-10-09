# Tests

- Use `TransactionCase` (or `HttpCase` for web); start new business tests from
  `odoo.addons.base.tests.common.BaseCommon` (independent non-admin user and
  company, mail side effects disabled), or
  `TransactionCaseWithUserDemo`/`HttpCaseWithUserDemo` when demo data is
  needed (it is not guaranteed present). Assert behavior, not implementation.
- Tests are tagged `standard` and `post_install` by default (fully-loaded
  registry); set exactly one of `at_install`/`post_install`. Opt into
  `@tagged('at_install', '-post_install')` only when the test must run before
  other modules load, with a comment justifying it; an `HttpCase` must stay
  `post_install`.
- Silent skips: a test file must be named `test_*.py` **and** imported from
  `tests/__init__.py`; the test class must be *defined* in that file (a class
  merely imported into it is skipped); and inherited `test_*` methods are not
  collected: a subclass runs nothing of its parent's unless it
  sets `allow_inherited_tests_method = True`.
- `assertQueryCount` only in dedicated performance tests, never inside a
  business test: it breaks on any unrelated ORM change.
- Wrap expected-error and warning logs in `mute_logger(...)` so the expected
  ERROR or WARNING never reaches the log.
- Tours: a step that triggers a page unload must set `expectUnloadPage: true`,
  and the last step must leave the client in a stable state (no pending edits
  or in-flight requests).
- Run them with `odoo-bin -u <module> --test-enable --stop-after-init`; one class
  or method with
  `odoo-bin --test-tags /<module>:<Class>.<method> --stop-after-init`.
