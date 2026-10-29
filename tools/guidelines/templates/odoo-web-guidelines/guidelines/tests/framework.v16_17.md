JavaScript unit tests use QUnit.

- Test files live in `static/tests/` (any name, by convention `*_tests.js`) and start with
  `/** @odoo-module **/`. They are added to `web.qunit_suite_tests` in the manifest
  (`'web.qunit_suite_tests': ['my_module/static/tests/**/*']`), and mobile-only tests to
  `web.qunit_mobile_suite_tests`.
- Run them in the browser at `/web/tests` (desktop) or `/web/tests/mobile`, narrowed with
  `?mod=my_module` or `?filter=<text>`. On the server, `test_js.py` of `web` runs the
  whole suite through `browser_js`.
- A suite is `QUnit.module("MyField", (hooks) => { hooks.beforeEach(...); })` and a test is
  `QUnit.test("does this", async (assert) => { ... })`, with `assert.containsOnce`,
  `assert.strictEqual`, `assert.verifySteps`.
- Imports of the helpers start with `@web/../tests/`: `@web/../tests/helpers/utils`
  (`getFixture`, `click`, `editInput`, `triggerEvent`, `nextTick`, `mount`,
  `patchWithCleanup`), `@web/../tests/views/helpers` (`makeView`, `setupViewRegistries`),
  `@web/../tests/helpers/mock_env` (`makeTestEnv`) and
  `@web/../tests/helpers/mock_services` (`makeFakeNotificationService`).
