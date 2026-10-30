Key names in 19.0: `TransactionCase`, `HttpCase`; default tag `at_install`, so business tests take `@tagged('post_install', '-at_install')`; `Form.from_action(self.env, action)`; `from odoo.tests import freeze_time`; `--test-tags`, `--test-file <path>`.

Sections of this file:

- [Tests](#tests)
- [Pick the test class by what the test needs](#pick-the-test-class-by-what-the-test-needs)
- [Tag every test class with the moment it runs](#tag-every-test-class-with-the-moment-it-runs)
- [Make sure the runner collects every test](#make-sure-the-runner-collects-every-test)
- [Build shared data in setUpClass](#build-shared-data-in-setupclass)
- [Drive form behavior through Form](#drive-form-behavior-through-form)
- [Count queries only in dedicated performance tests](#count-queries-only-in-dedicated-performance-tests)
- [Freeze the date a test depends on](#freeze-the-date-a-test-depends-on)
- [Test routes and tours with HttpCase](#test-routes-and-tours-with-httpcase)
- [Other test decorators](#other-test-decorators)
- [Select tests with test tags](#select-tests-with-test-tags)

# Tests

Conventions for everything under `tests/`.

- One `test_<feature>.py` per feature, imported from `tests/__init__.py`; classes
  named `Test<Feature>`, methods `test_<behavior>`, one behavior per method.
- Assert behavior (field values, raised exceptions, returned actions), not
  implementation (which method was called, how many times).
- `assertRaises` wraps only the one call expected to raise:
  `with self.assertRaises(UserError): book.action_lend()`.
- Wrap expected ERROR and WARNING logs in
  `mute_logger('odoo.addons.library.models.library_book')` (from `odoo.tools`), so the
  log of a passing run shows none.
- Create every record a test reads: demo data is not guaranteed (a new database has none
  unless created with `--with-demo`).
  `TransactionCaseWithUserDemo`/`HttpCaseWithUserDemo` (from
  `odoo.addons.base.tests.common`) give the demo user and create it when it is missing.
- In a `TransactionCase`, `self.env` is the superuser: access rights and record rules are bypassed. Test
  them through `record.with_user(user)` or `@users`, with users created by
  `new_test_user(self.env, login='librarian', groups='library.group_librarian')`.
- Never commit or roll back the test cursor: it raises `AssertionError`. Undo part of a
  test with a savepoint (`with self.env.cr.savepoint():`).
- Check several records and fields with
  `assertRecordValues(books, [{'name': 'A'}, {'name': 'B'}])` rather than one
  `assertEqual` per field: one failure shows every difference.

# Pick the test class by what the test needs

Derive every test class from one of these, imported from `odoo.tests`. A class derived
from `unittest.TestCase` has no test tags, and the runner skips it without a word.

- `TransactionCase`: the default. `setUpClass` runs once, each test runs in a
  savepoint rolled back after it.
- `HttpCase`: a `TransactionCase` with a test HTTP server and a headless Chrome,
  for routes, controllers and tours.
- `SingleTransactionCase`: all tests of the class share one transaction, rolled back
  after the last one, so each test sees what the previous ones wrote and the
  result depends on their order. Keep it for read-only checks of a costly setup.
- `BaseCase`: the base of the classes above, with Odoo's assertions and no cursor of
  its own. Derive from it directly only for tests that never touch the database.
- `TestCase` (`odoo.tests.case`): Odoo's rewrite of `unittest.TestCase` under
  `BaseCase`. Never derive from it directly: it carries no test tags.

# Tag every test class with the moment it runs

Decorate each class with `@tagged(...)`; it adds tags to the defaults, and a tag
prefixed with `-` removes one.

- Tests are tagged `standard` and `at_install` by default: they run before the
  modules that depend on theirs are loaded. Business tests need the full registry:
  decorate them `@tagged('post_install', '-at_install')`.
- Set exactly one of `at_install`/`post_install`. Both tags run the class twice; neither
  never runs it, and the only signal is a log warning.
- `at_install` tests run right after their module is installed or updated, before the
  modules that depend on it are loaded, so they need `-i` or `-u` of that module.
  `post_install` tests run once the whole registry is loaded, for the modules just
  installed or updated, or for every installed module when there was no `-i`/`-u`.
- `@tagged('-standard', 'library_slow')` keeps a slow or external test out of the
  default run (`--test-enable` selects `standard`); it runs only when
  `--test-tags library_slow` asks for it.
- The module's technical name is a tag of each of its tests: `--test-tags /library`
  selects them.

# Make sure the runner collects every test

A test that is not collected reports nothing: it does not fail, it is just not there.

- The file is named `test_*.py` and imported from `tests/__init__.py`; any other file
  under `tests/` is never loaded.
- The class must be defined in the file: a class imported into it is not
  collected. Inherited `test_*` methods are not collected either: a subclass runs
  only the tests it defines, unless it sets `allow_inherited_tests_method = True`.
- Only methods whose name starts with `test` run; a helper named `test_...` runs as a
  test.

# Build shared data in setUpClass

Create the data every test of a class reads once, in `setUpClass`, on `cls.env`:

```python
@tagged('post_install', '-at_install')
class TestLibraryLending(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.env = cls.env(context=dict(cls.env.context, tracking_disable=True))
        cls.member = cls.env['res.partner'].create({'name': 'Member'})
        cls.book = cls.env['library.book'].create({'name': 'Book'})

    def test_lend(self):
        self.book.action_lend(self.member)
        self.assertEqual(self.book.state, 'lent')
```

- Call `super().setUpClass()` first: it opens the cursor and creates `cls.env`.
- Each test of a `TransactionCase` runs in a savepoint rolled back after it: a test may
  change `cls.book`, the next one sees it as `setUpClass` left it.
- Rebind `cls.env` before creating records, never after: a record keeps the
  environment it was created with.
- Use `setUp` only for what must be fresh per test (a patch, a mock), and undo it with
  `self.addCleanup(...)` or `self.startPatcher(...)` rather than in `tearDown`.
- `BaseCommon` (from `odoo.addons.base.tests.common`) is a ready `TransactionCase`:
  mail tracking and notifications off in the `cls.env` context, the main company's currency
  set to USD, and `cls.partner`, `cls.company`, `cls.currency` and
  `cls.group_user`. Override `setup_independent_user()` or
  `setup_independent_company()` to run the class as its own user or company, and
  `default_env_context()` to turn mail tracking back on.

# Drive form behavior through Form

To test what a user does in a form (onchanges, defaults, required and readonly
fields), go through `Form`, not `create`/`write`, which run no onchange.

```python
with Form(self.env['library.book']) as form:
    form.name = 'Book'
    form.author_id = self.author
    with form.copy_ids.new() as copy:
        copy.barcode = 'B-1'
book = form.record
```

- Import it with `from odoo.tests import Form`; `odoo.tests.common.Form` is
  deprecated. `Form(record, view=...)` loads the record's default form view, or the
  given one; leaving the `with` block calls `save()`.
- Setting a field runs its onchanges as the client would. Writing a field that the view
  makes readonly or invisible raises `AssertionError`, and so does `save()` with an empty
  required field: the test follows the view, so put the field in the view or pass
  another view.
- A one2many line is an `O2MForm`: `form.copy_ids.new()` adds one,
  `form.copy_ids.edit(index)` changes one, `form.copy_ids.remove(index)` drops one. A
  many2many changes with `form.tag_ids.add(tag)` and `form.tag_ids.remove(id=tag.id)`.
- `Form.from_action(self.env, action)` opens the form that a window action returned
  by a button describes, to go on as the user would.

# Count queries only in dedicated performance tests

`assertQueryCount` breaks on any unrelated change of the ORM or of another module, so
it never goes in a business test.

```python
@users('__system__', 'librarian')
@warmup
def test_lend_queries(self):
    with self.assertQueryCount(__system__=4, librarian=5):
        self.book.with_user(self.env.user).action_lend(self.member)
```

- `@users(...)` runs the method once per login, as a subtest, with `self.env` switched
  to that user; the users must exist when the method starts.
- `@warmup` runs the method twice, the first time to fill the caches, and rolls the
  first run back; `self.warm` is `False` during the warm-up.
- Only exceeding the budget fails; a lower count is only logged, so lower the budget
  whenever the log shows it.

# Freeze the date a test depends on

A test whose result depends on today's date fails on the day the date crosses a
boundary (month end, leap day, year end). Freeze it.

Use `from odoo.tests import freeze_time`, then `@freeze_time('2024-01-31')` on a test
method, or `with freeze_time('2024-01-31'):` around the code that reads the date. On a
`TransactionCase` class it freezes `setUpClass` and every test of the class.

# Test routes and tours with HttpCase

- `self.url_open('/library/books')` sends a request to the test server;
  `self.authenticate('librarian', 'librarian')` logs the test session in first.
  `self.make_jsonrpc_request('/library/lend', {'book_id': book.id})` calls a JSON-RPC
  route and returns its `result`.
- `self.start_tour('/odoo', 'library_lend_tour', login='librarian')` runs a tour
  registered in JavaScript with `registry.category("web_tour.tours").add('library_lend_tour', {steps: () => [...]})`,
  in an asset bundle the page loads. `self.browser_js(url, code, login=...)` runs
  arbitrary JavaScript in the headless browser.
- An `HttpCase` stays `post_install`: the browser needs the assets of every module.
- A tour step that unloads the page sets `expectUnloadPage: true`, and the last step
  leaves the client stable (no pending edit, no request in flight), or the teardown
  races the browser.

# Other test decorators

- `@no_retry` on a class or method: never rerun it after a failure. Failed tests are
  rerun only when the `ODOO_TEST_FAILURE_RETRIES` environment variable is set; mark a
  test whose rerun cannot pass, such as one with side effects outside the transaction.
- `@standalone('library')` on a module-level function `def test_reinstall(env):`
  registers a script that installs, updates or uninstalls modules, which a test case
  may not do. It is not collected as a test: it runs only through
  `python3 -m odoo.tests.test_module_operations -d <db> standalone library` (a module
  name or a tag).
- `@test_xsd(path='library/data/book.xsd')` (or `url=...`) on a method that returns
  XML documents validates each of them against that XSD schema.

# Select tests with test tags

A test-tags spec is a comma-separated list of filters
`[-][tag][/module][:class][.method]`:

- `--test-tags /library` runs the `standard` tests of `library`;
  `/library:TestLibraryLending.test_lend` one method; `library_slow` every test with
  that tag; `-/library:TestLibraryLending` excludes a class.
- A filter without a tag implies `standard`; `*` matches every tag.
- A path ending in `.py` selects the tests of one file:
  `/library/tests/test_lending.py`, or an absolute path; `--test-file <path>` adds
  such a filter to the spec.
- `--test-tags` enables tests by itself; `--test-enable` alone means `+standard`.
- Run them with
  `odoo-bin -c odoo.conf -d test_library -u library --test-tags /library --stop-after-init`;
  use `-i library` on a new database to also test the install. See
  [Run odoo-bin with explicit options](command_line.md#run-odoo-bin-with-explicit-options).
