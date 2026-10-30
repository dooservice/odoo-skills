---
name: odoo-web-guidelines
description: >-
  Read before writing or reviewing any JavaScript, Owl template or SCSS of an
  Odoo 17.0 addon, even if you know Odoo: the web framework changes between
  versions. In 17.0: Owl 2; ES modules need `/** @odoo-module **/`; `patch(object, extension)` with `super`; `useService("rpc")` and `useService("orm")`; QUnit tests; tours in `registry.category("web_tour.tours")`. Covers modules, Owl, patching, registries,
  services, RPC and ORM calls, field widgets and js_class views, website and
  portal code, the Point of Sale, assets, SCSS, unit tests and tours under
  static/.
---

# Odoo 17.0 web guidelines

These rules apply to the web framework code an addon ships in `static/src/` and
`static/tests/`: JavaScript, Owl templates (XML) and SCSS. They do not apply to
`static/lib/` (vendored or library-style code), nor to images and
`static/description/`. They are house rules, not general web development advice.

One file per domain in `guidelines/`, one section per guideline; no rule outranks
another. Each file opens with the key names of 17.0 and the list of its sections:
read that, then only the sections that match the code you are touching.

| Task | Read |
| --- | --- |
| Any JavaScript: a module, imports, a patch, `_t`, where files go | [javascript.md](guidelines/javascript.md) |
| An Owl component: props, state, templates, hooks, refs | [owl.md](guidelines/owl.md) |
| A field widget, a `<widget>` or a `js_class` view | [views.md](guidelines/views.md) |
| The registry API and keys; fields, views, control panel, formatters, frontend registries | [registries.md](guidelines/registries.md) |
| Systray, user menu, client actions, command palette, debug menu, errors, effects | [registries_webclient.md](guidelines/registries_webclient.md) |
| Shared state or logic that any component uses (a service), plugins, RPC and ORM calls, actions, notifications, user, router, `env` | [services.md](guidelines/services.md) |
| Website, portal and public page code, snippets | [website.md](guidelines/website.md) |
| The Point of Sale | [point_of_sale.md](guidelines/point_of_sale.md) |
| Manifest `assets`, bundles, a "missing template" error, lazy loading | [assets.md](guidelines/assets.md) |
| SCSS and CSS | [scss.md](guidelines/scss.md) |
| JavaScript unit tests and tours | [tests.md](guidelines/tests.md) |

To add a guideline, follow [AUTHORING.md](AUTHORING.md).

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the 17.0 source.
