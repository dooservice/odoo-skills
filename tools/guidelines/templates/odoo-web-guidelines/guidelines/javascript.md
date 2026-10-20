# The web framework in $version

$header
- Components are Owl classes with a static `template` (an XML file next to them,
  `t-name="<module>.<Component>"`) and static `props`. $owl.
- Extend a field widget: $field.
- Server calls: $rpc.
- Override existing behaviour: $patch.
- Raw HTML: never assign `innerHTML` from data; $html.
- Tests: $tests.
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
