JavaScript unit tests use hoot (`@odoo/hoot`). A few old suites of Odoo itself still run
on QUnit at `/web/tests/legacy`; never write a new QUnit test.

- A test file is named `*.test.js` and lives in `static/tests/`; the runner loads only that
  suffix, so `my_field_tests.js` is silently skipped. It is added to `web.assets_unit_tests`
  in the manifest (`'web.assets_unit_tests': ['my_module/static/tests/**/*']`); keep
  tours out of that bundle (`('remove', 'my_module/static/tests/tours/**/*')`).
- Run the suite in the browser at `/web/tests`, narrowed with the filter box or
  `?filter=<text>`, and with `?preset=mobile` for the mobile layout. On the server,
  `test_unit_desktop` and `test_unit_mobile` of `web`'s `test_js.py` run it headless.
- `describe("MyField", () => { ... })` groups tests, `test("does this", async () => { ... })`
  is one test, and `expect(target).toHaveCount(1)`, `expect(value).toBe(...)` and
  `expect.step("x")` with `expect.verifySteps([...])` are the assertions.
- Imports: `@odoo/hoot` (`describe`, `test`, `expect`, `beforeEach`, `afterEach`),
  `@odoo/hoot-dom` (DOM queries and user events), `@odoo/hoot-mock` (time, network, locale)
  and `@web/../tests/web_test_helpers` (models, mounting, RPC mocks).
