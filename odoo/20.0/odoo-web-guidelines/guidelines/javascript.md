Key names in 20.0:

- Owl 3: `useProps`, `proxy`, `signal`, `computed`; shared logic in a `Plugin` reached with `usePlugin`, registered with `services.add`.
- Header: none needed; `/** @odoo-module ignore **/` keeps a file out of the transpiler.
- Patch: `patch(target, extension)` with `super`; it returns the function that removes it.
- Translation: `_t` anywhere, `_t("Lent to %(name)s", { name })`; `_lt` no longer exists.
- Server calls: `rpc` from `@web/core/network/rpc`, `usePlugin(ORM)` for model methods.
- Raw HTML: `htmlEscape`, `htmlJoin`/`htmlSprintf` and `setElementContent`, or `t-out`.
- Tests: hoot, `*.test.js` in `web.assets_unit_tests`.

Sections of this file:

- The web framework in 20.0
- Write each file as an ES module with absolute imports
- Organize files by feature, not by type
- Avoid getters
- Patch sparingly
- Patch the prototype with `patch` and call `super`
- Translate every user-facing string with `_t`

# The web framework in 20.0

- Files under `static/src` are ES modules; no `@odoo-module` header is needed.
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and `props = useProps({...})`. Owl 3: state with `proxy`, `signal` and `computed`; lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`; see [owl.md](owl.md).
- Extend a field widget: `registry.category("fields").add("my_widget", { component: MyField, supportedTypes: [...] })` registers a descriptor; see [views.md](views.md).
- Server calls: `import { rpc } from "@web/core/network/rpc"` for a route, `usePlugin(ORM)` (`ORM` from `@web/core/orm_plugin`) for model methods; see [services.md](services.md).
- Shared logic is a plugin, not a service: `class MyPlugin extends Plugin`, with `Plugin`,
  `usePlugin` and `useListener` from `@odoo/owl`, registered with `services.add(MyPlugin)` from
  `@web/core/services`; components and other plugins get it with `usePlugin(MyPlugin)`. The bus,
  the ORM, actions, dialogs and notifications are plugins (`GlobalBusPlugin`, `ORM`,
  `ActionPlugin`, `DialogPlugin`, `NotificationPlugin`). `registry.category("services")` and
  `useService` still work through a temporary bridge started after the plugins: keep them for
  code not moved yet, never for new code.
- Extension points are registries: `registry.category("...")`; see
  [registries.md](registries.md).
- Override existing behaviour: `patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`.
- Raw HTML: never assign `innerHTML` from data; escape with `htmlEscape`, build with `htmlJoin`/`htmlSprintf`, and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`.
- Translated text: `_t` from `@web/core/l10n/translation`.
- Tests: hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`; see [tests.md](tests.md).
- Assets are declared in the manifest `assets` (`web.assets_backend`,
  `web.assets_frontend`, ...), never by an XML template in this version; see
  [assets.md](assets.md).
- Public pages: see [website.md](website.md); the Point of Sale: see
  [point_of_sale.md](point_of_sale.md).

# Write each file as an ES module with absolute imports

Files under `static/src` and `static/tests` are always transpiled as ES modules; the
`/** @odoo-module **/` header is no longer needed there, and Odoo removed it from its
own files. It is still needed for a module outside those folders, and
`/** @odoo-module ignore **/` keeps a file of `static/src` out of the transpiler (a
script meant to run as it is).

- A file of `my_module/static/src/a/b.js` is the module `@my_module/a/b`, and
  `my_module/static/tests/c.js` is `@my_module/../tests/c`. Import another addon's code
  by that name (`import { registry } from "@web/core/registry"`), never with a relative
  path that leaves your addon.
- Owl is `@odoo/owl`, and the test framework `@odoo/hoot`, `@odoo/hoot-dom` and `@odoo/hoot-mock`; third-party code shipped in `static/lib/` is imported
  as `@my_module/../lib/...` when it is a module, or loaded with `loadJS` when it is not.
- Export what other modules extend (components, descriptors, classes) by name; a
  default export cannot be patched or spread by name.
- Side effects at import time are limited to registry additions and patches: a module
  never calls the server or touches the DOM when it is loaded.

# Organize files by feature, not by type

Code is organized by feature, not by type. Instead of folders like `components/`,
`plugins/`, `services/` or `hooks/`, each feature gets one folder holding all of its
files: `notification/` contains the notification component, its plugin, its template
and its styles.

# Avoid getters

A getter hides the fact that a computation happens, and only saves a pair of
parentheses. Write a plain function instead: the call site then shows that code runs,
and it can take an argument the day the computation needs one.

When the value is derived state, an Owl `computed` is the better answer: unlike a
getter, it recomputes only when what it reads changes.

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
after the string: `_t("Lent to %s", name)`, or `_t("Lent to %(name)s", { name })`
for several. `_lt` no longer exists.

- The string passed to `_t` is a literal, so the translation export can find it:
  `_t("Lent")`, never `_t(label)` or `_t("Lent " + name)`.
- In templates, text nodes and the `title`, `placeholder`, `alt` and `aria-label`
  attributes are translated without `_t`.
