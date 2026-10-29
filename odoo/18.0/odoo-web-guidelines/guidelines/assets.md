# Assets

- Every resource a page needs ships in the codebase: copy images, fonts and libraries
  into the addon instead of linking them by URL.
- Third-party libraries go in `static/lib/`, unminified, so they can be read and diffed.

# Declare static files in the manifest `assets`

Every JavaScript, SCSS and Owl XML file of `static/src` reaches the browser through a
bundle, and bundles are declared in the `assets` key of `__manifest__.py`:

```python
'assets': {
    'web.assets_backend': [
        'my_module/static/src/**/*',
    ],
    'web.assets_unit_tests': [
        'my_module/static/tests/**/*',
    ],
},
```

- A file that no bundle lists is never loaded, and nothing warns about it.
- Globs are recursive (`**`) and sorted, so `my_module/static/src/**/*` takes the whole
  tree; list a file on its own only when it must load before the others.
- Never add a file with an XML `<template inherit_id="web.assets_backend">`: bundles
  are not QWeb templates in this version, and the inheritance does nothing.
- `ir.asset` records add to a bundle at runtime (`bundle`, `directive`, `path`,
  `target`, `sequence`); those with a `sequence` below 16 come before the manifests, the
  others after. Use them only for content a user configures, never for a module's own
  files.

# Put each file in the bundle of the page that runs it

| Code | Bundle |
| --- | --- |
| Backend web client: fields, views, actions, systray | `web.assets_backend` (the page loads it through `web.assets_web`) |
| Website, portal, login and other public pages | `web.assets_frontend` |
| QWeb reports (PDF and HTML) | `web.report_assets_common` |
| SCSS variables that other files read | `web._assets_primary_variables` |
| Point of Sale | `point_of_sale._assets_pos` |
| Tours | `web.assets_tests` |
| Unit tests | `web.assets_unit_tests` |
| Backend code loaded on first use, like the graph and pivot views | `web.assets_backend_lazy` |

Code in the wrong bundle fails in one of two ways: it is missing where it is needed, or
it ships to pages that never use it and breaks them with imports they cannot resolve.
A module that both extends the backend and serves public pages lists its frontend files
under `web.assets_frontend` and its backend files under `web.assets_backend`, from two
folders.

# Use a directive to place a file relative to another

A plain path appends the file to the bundle. A tuple changes where it goes:

- `('prepend', 'my_module/static/src/early.js')` puts it at the start of the bundle.
- `('before', 'web/static/src/core/target.scss', 'my_module/static/src/vars.scss')` and
  `('after', target, path)` place it next to a file already in the bundle; the target
  must be there, or the bundle fails to build.
- `('replace', target, path)` swaps a file of another module for yours.
- `('remove', 'other_module/static/src/thing.js')` takes a file out.
- `('include', 'my_module.assets_shared')` copies a whole bundle in, which is how a
  module shares files between two bundles without listing them twice.

`replace` and `remove` change another module's files behind its back; reach for them
only when a `patch` or a registry entry cannot do the job.

# Keep an Owl template in the same bundle as its component

The XML files of a bundle are compiled into that bundle and registered when it loads,
through `registerTemplate` and `registerTemplateExtension` of `@web/core/templates`. A
component whose template sits in another bundle fails at render with a missing
template, so ship the `.xml` next to the `.js` that uses it and let the same glob take
both.

The template's `t-name` is `my_module.ComponentName`, and an extension of another
template sets `t-inherit="web.Original"` and `t-inherit-mode="extension"`; the parent
must be in the same bundle or one loaded before it.

# Load heavy code lazily

A large library or a rarely opened screen should not slow every page load. Put it in
its own bundle, declared in the manifest like any other
(`'my_module.assets_heavy': ['my_module/static/src/heavy/**/*']`), and load it when it is
needed:

- `await loadBundle("my_module.assets_heavy")` (from `@web/core/assets`) loads it, once;
  later calls return at once. It takes the bundle name only.
- To show a component of that bundle, register it in its bundle with
  `registry.category("lazy_components").add("my_module.Chart", Chart)` and render
  `<LazyComponent bundle="'my_module.assets_heavy'" Component="'my_module.Chart'"/>`
  (`LazyComponent` from `@web/core/assets`).
- A third-party script or stylesheet of `static/lib/` that is not in a bundle loads
  with `loadJS(url)` or `loadCSS(url)` from `@web/core/assets`.

# Debug a bundle with `?debug=assets`

In normal mode a bundle is one minified file per type, served under
``/web/assets/<version>/<bundle>.min.js``. With `?debug=assets` each file is served on its own, unminified, with
source maps, so a stack trace names the real file and line. A bundle is rebuilt when one
of its files changes, so after editing a file a reload is enough; after changing the
manifest `assets`, restart the server: the list of files is cached per process.
