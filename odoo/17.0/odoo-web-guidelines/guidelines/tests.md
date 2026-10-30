Key names in 17.0:

- QUnit: `QUnit.module`, `QUnit.test`, files in `web.qunit_suite_tests`.
- Mock server: `serverData`, `makeView`, `setupViewRegistries`, `mockRPC`.
- Helpers: `click`, `editInput`, `triggerEvent`, `nextTick`, `patchWithCleanup`.
- Tours: `registry.category("web_tour.tours")`, `steps` as a function, `test: true`, jQuery `trigger`, `extra_trigger`.
- Python: `HttpCase`, `start_tour`.

Sections of this file:

- Unit tests in 17.0
- Mock the server with test models, never with a database
- Interact through the test helpers and wait for the DOM
- Undo every patch a test makes
- Register a tour in the `web_tour.tours` registry
- Write each tour step as a trigger and an action
- Run tours from an `HttpCase`

# Unit tests in 17.0

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

# Mock the server with test models, never with a database

A unit test never reaches a database: the mock server answers every RPC from the
`serverData` the test declares, which keeps the test fast and independent of installed
modules.

- Declare models in `serverData.models`: `{ "library.book": { fields: { name: { string:
  "Name", type: "char" } }, records: [{ id: 1, name: "Dune" }] } }`, and views in
  `serverData.views` keyed `"library.book,false,form"`.
- Mount a view with `makeView({ type: "form", resModel: "library.book", resId: 1,
  serverData, arch })`, after `setupViewRegistries()` in `beforeEach`.
- Intercept a call with `mockRPC(route, args, performRPC)`: return a value to answer it,
  return nothing to let the mock server answer, and call `assert.step(args.method)` to
  check that it happened.

# Interact through the test helpers and wait for the DOM

Owl renders on the next animation frame, so an assertion written right after an event
reads the old DOM. Use the helpers, which dispatch real events and wait for the render.

- `await click(target, ".o_field_widget input")`, `await editInput(target, "input", "Dune")`
  and `await triggerEvent(target, "input", "keydown", { key: "Enter" })` act and wait;
  `target` is `getFixture()`.
- After a change made outside a helper (a resolved promise, a patched service), add
  `await nextTick()` before asserting.
- Assert on what the user sees (`.o_field_widget`, text, classes), not on component
  internals: internals change between versions, the DOM contract changes less.

# Undo every patch a test makes

A patch that survives its test changes every test after it, and the failure shows up in a
test that has nothing to do with it.

- Patch through `patchWithCleanup(target, { method() { ... } })` (from
  `@web/../tests/helpers/utils`); it is undone when the test ends.
- Never call `patch` from `@web/core/utils/patch` in a test, nor assign to a prototype
  or to `browser` directly.

# Register a tour in the `web_tour.tours` registry

A tour is an entry of `registry.category("web_tour.tours")`, whose `steps` is a function
returning the steps; a plain array throws when the tour starts.

```js
/** @odoo-module **/
import { registry } from "@web/core/registry";

registry.category("web_tour.tours").add("my_module.lend_book", {
    test: true,
    url: "/web",
    steps: () => [
        { trigger: ".o_app[data-menu-xmlid='my_module.menu_root']" },
        { trigger: ".o_list_button_add" },
    ],
});
```

- The name is prefixed with the module (`my_module.lend_book`): tour names are global.
- `test: true` keeps the tour out of the onboarding tours a user can start; every test
  tour sets it.
- Shared steps come from `stepUtils` of `@web_tour/tour_service/tour_utils`
  (`goToAppSteps`, `saveForm`, `discardForm`, `showAppsMenuItem`).

# Write each tour step as a trigger and an action

A step waits until its `trigger` matches a visible element, then runs its `run`. A tour
that acts on an element before it is ready fails at random, so every step targets the
element the user would look at.

- `trigger` is a jQuery selector (`:contains("Dune")` is allowed); `extra_trigger` adds a
  second element that must be present, and `in_modal: true` restricts the search to the
  open dialog.
- `run` is a string action or a function: `"click"` (the default when `run` is absent,
  except on the last step), `"text Dune"` to type, `"drag_and_drop_native .o_target"`,
  or `run(actions) { ... }`.
- A step that only checks the page, without acting, says `run: () => {}`.
- `content` is the tooltip text; `position` places it. Both matter for onboarding tours
  only.
- `edition: "community"` or `mobile: true` limit a step to that edition or layout.

# Run tours from an `HttpCase`

A tour runs in a real browser against a real database, so it is the test for a whole
flow (open a menu, fill a form, save); a unit test is the test for one component.

- The tour file goes in the `web.assets_tests` bundle of the manifest
  (`'web.assets_tests': ['my_module/static/tests/tours/**/*']`), never in
  `web.assets_backend`: it would ship to every user.
- The Python test is an `HttpCase` tagged `@tagged('post_install', '-at_install')`:
  the tour needs every module installed and the assets built.
- Start it with `self.start_tour("/web", "my_module.my_tour", login="admin")`; the
  signature is `start_tour(url_path, tour_name, step_delay=None, **kwargs)`, and
  `step_delay` is for watching a tour locally, never for a committed test.
- Create the records the tour needs in the Python test, before `start_tour`, and check
  the result there afterwards: the tour proves the UI flow, the Python asserts prove the
  data.
