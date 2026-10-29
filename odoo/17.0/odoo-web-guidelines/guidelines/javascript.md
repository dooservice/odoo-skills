# The web framework in 17.0

- Every JavaScript file under `static/src` starts with `/** @odoo-module **/`;
  without it the file is not transpiled and its `import`s fail.
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`; see [owl.md](owl.md).
- Extend a field widget: `registry.category("fields").add("my_widget", { component: MyField, supportedTypes: [...] })` registers a descriptor; see [views.md](views.md).
- Server calls: `useService("rpc")` for a route, `useService("orm")` for model methods; see [services.md](services.md).
- Extension points are registries: `registry.category("...")`; see
  [registries.md](registries.md).
- Override existing behaviour: `patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`.
- Raw HTML: never assign `innerHTML` from data; escape with `escape` from `@web/core/utils/strings` or render through `t-out`.
- Translated text: `_t` from `@web/core/l10n/translation`.
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

`patch(target, extension)` from `@web/core/utils/patch` changes `target` in place and
returns a function that removes the patch; there is no patch name in this version (a
string second argument throws). The patched method reaches the original with `super`.

```js
patch(BookCard.prototype, {
    setup() {
        super.setup(...arguments);
        this.notification = useService("notification");
    },
});
```

- Patch `MyClass.prototype` to change instance methods, and `MyClass` itself only to
  change its statics (`template`, `components`).
- A patched `setup` calls `super.setup(...arguments)` first, then adds its hooks.
- Never replace a method without calling `super` unless the replacement is the point;
  another module's patch of the same method is then skipped silently.
- The patch is applied when its file loads: put it in the same bundle as the code it
  patches.

# Translate every user-facing string with `_t`

`_t("Book lent")` may be called anywhere, at module level too: before the translations
are loaded it returns a lazy string that translates when displayed. Values are passed
after the string: `_t("Lent to %s", name)`. `_lt` is only an alias of `_t` kept for old
code.

- The string passed to `_t` is a literal, so the translation export can find it:
  `_t("Lent")`, never `_t(label)` or `_t("Lent " + name)`.
- In templates, text nodes and the `title`, `placeholder`, `alt` and `aria-label`
  attributes are translated without `_t`.
