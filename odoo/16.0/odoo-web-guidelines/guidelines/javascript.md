Key names in 16.0:

- Header: `/** @odoo-module **/` on every file of `static/src` and `static/tests`.
- Patch: `patch(target, name, extension)` with `this._super(...arguments)`; `unpatch(target, name)`.
- Translation: `_t` at call time only, `_lt` at module level, values through `sprintf`.
- Owl 2 with static `props`; server calls through `useService("rpc")` and `useService("orm")`.
- Raw HTML: `escape` from `@web/core/utils/strings`, or `t-out`.
- Tests: QUnit in `web.qunit_suite_tests`.

Sections of this file:

- The web framework in 16.0
- Write each file as an ES module with absolute imports
- Organize files by feature, not by type
- Avoid getters
- Patch sparingly
- Patch the prototype with `patch` and call `super`
- Translate every user-facing string with `_t`

# The web framework in 16.0

- Every JavaScript file under `static/src` starts with `/** @odoo-module **/`;
  without it the file is not transpiled and its `import`s fail.
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`; see [owl.md](owl.md).
- Extend a field widget: `registry.category("fields").add("my_widget", MyField)` registers the component; see [views.md](views.md).
- Server calls: `useService("rpc")` for a route, `useService("orm")` for model methods; see [services.md](services.md).
- Extension points are registries: `registry.category("...")`; see
  [registries.md](registries.md).
- Override existing behaviour: `patch(Target.prototype, "my_module.Target", { setup() { this._super(...arguments); ... } })`.
- Raw HTML: never assign `innerHTML` from data; escape with `escape` from `@web/core/utils/strings` or render through `t-out`.
- Translated text: `_t` from `@web/core/l10n/translation`; at module level use `_lt`.
- Tests: QUnit, under `static/tests/`, added to `web.qunit_suite_tests`; run in the browser at `/web/tests`; see [tests.md](tests.md).
- Assets are declared in the manifest `assets` (`web.assets_backend`,
  `web.assets_frontend`, ...), never by an XML template in this version; see
  [assets.md](assets.md).
- Public pages: see [website.md](website.md); the Point of Sale: see
  [point_of_sale.md](point_of_sale.md).

# Write each file as an ES module with absolute imports

Every file under `static/src` and `static/tests` starts with `/** @odoo-module **/`:
without it the file is not transpiled, its `import`s stay as they are, and the bundle
fails to load with a syntax error in the browser. The header also takes
`alias=<name>` (a second, legacy name for the module) and `default=false`.

- A file of `my_module/static/src/a/b.js` is the module `@my_module/a/b`, and
  `my_module/static/tests/c.js` is `@my_module/../tests/c`. Import another addon's code
  by that name (`import { registry } from "@web/core/registry"`), never with a relative
  path that leaves your addon.
- Owl is `@odoo/owl`; third-party code shipped in `static/lib/` is imported
  as `@my_module/../lib/...` when it is a module, or loaded with `loadJS` when it is not.
- Export what other modules extend (components, descriptors, classes) by name; a
  default export cannot be patched or spread by name.
- Side effects at import time are limited to registry additions and patches: a module
  never calls the server or touches the DOM when it is loaded.

# Organize files by feature, not by type

Code is organized by feature, not by type. Instead of folders like `components/`,
`services/` or `hooks/`, each feature gets one folder holding all of its
files: `notification/` contains the notification component, its template
and its styles.

# Avoid getters

A getter hides the fact that a computation happens, and only saves a pair of
parentheses. Write a plain function instead: the call site then shows that code runs,
and it can take an argument the day the computation needs one.

# Patch sparingly

Outside Odoo's own code a `patch` is the normal way to change standard behaviour, but
it is the hardest code to maintain: reading the patched class no longer tells you what
runs, and the patch drifts from the code it targets at every upgrade. Patch the
smallest method that does the job, always call `super`, and prefer a registry entry,
a new component or a prop when the framework offers one.

# Patch the prototype with `patch` and call `super`

`patch(target, name, extension)` from `@web/core/utils/patch` changes `target` in
place; `name` identifies the patch (`"my_module.BookCard"`) and must be unique, and
`unpatch(target, name)` removes it. The patched method reaches the original with
`this._super(...arguments)`.

```js
patch(BookCard.prototype, "my_module.BookCard", {
    setup() {
        this._super(...arguments);
        this.notification = useService("notification");
    },
});
```

- Patch `MyClass.prototype` to change instance methods, and `MyClass` itself only to
  change its statics (`template`, `components`).
- A patched `setup` calls `this._super(...arguments)` first, then adds its hooks.
- Never replace a method without calling `super` unless the replacement is the point;
  another module's patch of the same method is then skipped silently.
- The patch is applied when its file loads: put it in the same bundle as the code it
  patches.

# Translate every user-facing string with `_t`

`_t("Book lent")` translates at call time, so it must run after the translations are
loaded: inside a function or a component, never at module level. A string defined at
module level (a label in a registry entry, a constant) uses `_lt("Book lent")`, which
translates when it is displayed. `_t` takes no values: format with `sprintf` from
`@web/core/utils/strings` (`sprintf(_t("Lent to %s"), name)`).

- The string passed to `_t` is a literal, so the translation export can find it:
  `_t("Lent")`, never `_t(label)` or `_t("Lent " + name)`.
- In templates, text nodes and the `title`, `placeholder`, `alt` and `aria-label`
  attributes are translated without `_t`.
