# The web framework in 17.0

- Every JavaScript file under `static/src` starts with `/** @odoo-module **/`;
  without it the file is not transpiled and its `import`s fail.
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. Owl 2: state with `useState`, lifecycle with `onWillStart`/`onMounted`/`onWillUnmount`.
- Extend a field widget: `registry.category("fields").add("my_widget", { component: MyField, supportedTypes: [...] })` registers a descriptor.
- Server calls: `useService("rpc")` for a route, `useService("orm")` for model methods.
- Override existing behaviour: `patch(Target.prototype, { setup() { super.setup(...arguments); ... } })`.
- Raw HTML: never assign `innerHTML` from data; escape with `escape` from `@web/core/utils/strings` or render through `t-out`.
- Tests: QUnit, under `static/tests/`, added to `web.qunit_suite_tests`; run in the browser at `/web/tests`.
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
