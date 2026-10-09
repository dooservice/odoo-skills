# The web framework in 18.0

- Files under `static/src` are ES modules; no `@odoo-module` header is needed.
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`.
- Extend a field widget: `registry.category("fields").add("my_widget", { component: MyField, supportedTypes: [...] })` registers a descriptor.
- Server calls: `import { rpc } from "@web/core/network/rpc"` for a route, `useService("orm")` for model methods.
- Override existing behaviour: `patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`.
- Raw HTML: never assign `innerHTML` from data; escape with `htmlEscape` and set content with `setElementContent` (`@web/core/utils/html`), or render through `t-out`.
- Tests: hoot (`@odoo/hoot`): `*.test.js` under `static/tests/`, added to `web.assets_unit_tests`; QUnit is only for legacy suites.
- Assets are declared in the manifest `assets` (`web.assets_backend`,
  `web.assets_frontend`, ...), never by an XML template in this version.

# Organize files by feature, not by type

Code is organized by feature, not by type. Instead of folders like `components/`,
`services/` or `hooks/`, each feature gets one folder holding all of its files:
`notification/` contains the notification component, its template and its styles.

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
