# Unit tests in 20.0

JavaScript unit tests use hoot (`@odoo/hoot`); QUnit is gone.

- A test file is named `*.test.js` and lives in `static/tests/`; the runner loads only that
  suffix, so `my_field_tests.js` is silently skipped. It is added to `web.assets_unit_tests`
  in the manifest (`'web.assets_unit_tests': ['my_module/static/tests/**/*']`); keep
  tours out of that bundle (`('remove', 'my_module/static/tests/tours/**/*')`).
- Run the suite in the browser at `/web/tests`, narrowed with the filter box or
  `?filter=<text>`, and with `?preset=mobile` for the mobile layout. On the server, the
  `WebSuite` of `web`'s `test_js.py` (tag `hoot`) runs, for each installed module, the tests
  of that module headless.
- `describe("MyField", () => { ... })` groups tests, `test("does this", async () => { ... })`
  is one test, and `expect(target).toHaveCount(1)`, `expect(value).toBe(...)` and
  `expect.step("x")` with `expect.verifySteps([...])` or `expect.waitForSteps([...])` are
  the assertions; `asyncStep` and `waitForSteps` of the web helpers no longer exist.
- Imports: `@odoo/hoot` (`describe`, `test`, `expect`, `beforeEach`, `afterEach`),
  `@odoo/hoot-dom` (DOM queries and user events), `@odoo/hoot-mock` (time, network, locale)
  and `@web/../tests/web_test_helpers` (models, mounting, RPC mocks). A deferred value is
  `Promise.withResolvers()`: `Deferred` was removed from hoot and from
  `@web/core/utils/concurrency`.

# Mock the server with test models, never with a database

A unit test never reaches a database: the mock server answers every RPC from the models
the test declares, which keeps the test fast and independent of installed modules.

- Declare a model as a class: `class LibraryBook extends models.Model { _name =
  "library.book"; name = fields.Char(); _records = [{ id: 1, name: "Dune" }]; }`, then
  `defineModels([LibraryBook])` at the top of the file. `_views` holds the archs by type.
  Models of other modules come with their helpers (`defineMailModels()` from
  `@mail/../tests/mail_test_helpers`).
- Mount a view with `await mountView({ type: "form", resModel: "library.book", resId: 1,
  arch })` (it takes no target argument), a component with
  `await mountWithCleanup(MyComponent, { props })`, and the whole client with
  `mountWebClient()`. The test app runs the plugins: get one with
  `getService(MyPlugin)`, a service not converted yet with `getService("name")`, and use
  `makeTestApp()` where older tests used `makeMockEnv()`, which no longer exists.
- Intercept a call with `onRpc("library.book", "action_lend", ({ args }) => ...)`, or a
  route with `onRpc("/my_module/data", async (request) => ...)`: return a value to answer
  it, nothing to let the mock server answer; record it with `expect.step`.
- `serverState` sets the user, company and language the client sees
  (`serverState.userId`, `serverState.lang`); `defineParams` sets session parameters.

# Interact through the test helpers and wait for the DOM

Owl renders on the next animation frame, so an assertion written right after an event
reads the old DOM. Use the helpers, which dispatch the full sequence of real events.

- `@odoo/hoot-dom` acts on selectors: `await click(".o_field_widget input")`,
  `await edit("Dune")` on the focused input, `await press("Enter")`, `check`, `select`,
  `hover`; `queryAll`, `queryOne` and `waitFor` read the DOM.
- After an action, `await animationFrame()` (from `@odoo/hoot-mock`) lets Owl render;
  `contains(".o_field_widget input").click()` from the web helpers waits for the element
  before acting, which suits elements that appear late.
- Time is mocked: `advanceTime(ms)`, `runAllTimers()` and `mockDate("2024-01-01 10:00:00")`
  replace real waiting.
- Assert on what the user sees: `expect(".o_field_widget input").toHaveValue("Dune")`,
  `toHaveCount`, `toHaveClass`, `toBeVisible`. Component internals change between
  versions; the DOM contract changes less.

# Undo every patch a test makes

A patch that survives its test changes every test after it, and the failure shows up in a
test that has nothing to do with it.

- Call `patch(target, { method() { ... } })` from `@web/core/utils/patch` inside the test:
  the test framework undoes every `patch` when the test ends. `patchWithCleanup` is a
  deprecated alias of it.
- Never assign to a prototype or to `browser` directly: only `patch` is undone.

# Register a tour in the `web_tour.tours` registry

A tour is an entry of `registry.category("web_tour.tours")`, whose `steps` is a function
returning the steps.

```js
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("my_module.lend_book", {
    url: "/odoo",
    steps: () => [
        { trigger: ".o_app[data-menu-xmlid='my_module.menu_root']", run: "click" },
        { trigger: ".o_list_button_add", run: "click" },
    ],
});
```

- The name is prefixed with the module (`my_module.lend_book`): tour names are global.
- The entry takes `steps` and an optional `url`, nothing else: the registry validates it
  strictly in debug mode, so a leftover `test` or `wait_for` from an older version is an
  error there.
- Shared steps come from `stepUtils` of `@web_tour/tour_utils` (`goToAppSteps`,
  `saveForm`, `discardForm`, `showAppsMenuItem`).

# Write each tour step as a trigger and an action

A step waits until its `trigger` matches a visible element, then runs its `run`. A tour
that acts on an element before it is ready fails at random, so every step targets the
element the user would look at.

- `trigger` is a hoot selector (`:contains(Dune)`, `:iframe`, `:not(:visible)` are
  allowed); to wait for two elements, chain two steps. `extra_trigger` and `in_modal` no
  longer exist: put the dialog in the selector (`.modal .o_field_widget`).
- `run` is a string action or a function: `"click"`, `"edit Dune"`, `"fill Dune"`,
  `"press Enter"`, `"select 2"`, `"check"`, or several joined with `&&`
  (`"edit Dune && press Enter"`); `run(helpers) { ... }` gets the same helpers.
- A step without `run` only waits for its trigger: it no longer clicks by default, so a
  step written for an older version that relied on the implicit click needs
  `run: "click"`.
- `content` is the tooltip text and `tooltipPosition` places it; both matter for
  onboarding tours only.
- `isActive: ["community"]` (or `"enterprise"`, `"mobile"`, `"desktop"`, `"auto"`,
  `"manual"`, `"robot"`) limits a step to that edition, layout or mode.

# Run tours from an `HttpCase`

A tour runs in a real browser against a real database, so it is the test for a whole
flow (open a menu, fill a form, save); a unit test is the test for one component.

- The tour file goes in the `web.assets_tests` bundle of the manifest
  (`'web.assets_tests': ['my_module/static/tests/tours/**/*']`), never in
  `web.assets_backend`: it would ship to every user.
- The Python test is an `HttpCase` tagged `@tagged('post_install', '-at_install')`:
  the tour needs every module installed and the assets built.
- Start it with `self.start_tour("/odoo", "my_module.my_tour", login="admin")`; the
  signature is `start_tour(url_path, tour_name, step_delay=None, **kwargs)`, and
  `step_delay` is for watching a tour locally, never for a committed test.
- Create the records the tour needs in the Python test, before `start_tour`, and check
  the result there afterwards: the tour proves the UI flow, the Python asserts prove the
  data.
