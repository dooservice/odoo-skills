---
name: odoo-web-guidelines
description: >-
  House rules for the web framework code of Odoo 20.0 addons: the JavaScript,
  Owl templates and SCSS in static/src/ and static/tests/. Use when writing,
  reviewing, or moving files under static/ in an Odoo addon.
---

# Odoo 20.0 web guidelines

These rules apply to the web framework code an addon ships in `static/src/` and
`static/tests/`: JavaScript, Owl templates (XML) and SCSS. They do not apply to
`static/lib/`, which holds vendored code, nor to `static/description/`.

Guidelines are grouped by domain, one file per domain in `guidelines/`, one section per
guideline. Read the sections that match the code you are touching.

| Guideline | Read it when |
| --- | --- |
| [The web framework in 20.0](guidelines/javascript.md#the-web-framework-in-200) | writing any JavaScript: modules, services, registries, patches, tests |
| [Organize files by feature](guidelines/javascript.md#organize-files-by-feature-not-by-type) | creating a file, or deciding where new code lives |
| [Avoid getters](guidelines/javascript.md#avoid-getters) | adding a computed value to a class or a component |
| [Patch sparingly](guidelines/javascript.md#patch-sparingly) | extending or overriding behaviour that already exists |
| [SCSS and CSS](guidelines/scss.md#scss-and-css) | touching `*.scss` |
| [Assets](guidelines/assets.md#assets) | adding an image, font, or library |

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the 20.0 source.
