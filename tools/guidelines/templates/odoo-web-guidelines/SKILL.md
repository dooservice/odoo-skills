---
name: odoo-web-guidelines
description: >-
  Read before writing or reviewing any JavaScript, Owl template or SCSS of an
  Odoo $version addon, even if you know Odoo: the web framework changes between
  versions. In $version: $names Covers modules, Owl, patching, registries,
  services, RPC and ORM calls, field widgets and js_class views, website and
  portal code, the Point of Sale, assets, SCSS, unit tests and tours under
  static/.
---

# Odoo $version web guidelines

These rules apply to the web framework code an addon ships in `static/src/` and
`static/tests/`: JavaScript, Owl templates (XML) and SCSS. They do not apply to
`static/lib/`, which holds vendored or library-style code, nor to the images and
`static/description/` an addon ships alongside. They are house rules, not general web
development advice.

Guidelines are grouped by domain, one file per domain in `guidelines/`, one section per
guideline. No rule outranks another. Read the sections that match the code you are
touching instead of loading whole files.

| Guideline | Read it when |
| --- | --- |
| [The web framework in $version](guidelines/javascript.md#the-web-framework-in-${major}0) | writing any JavaScript; see the other files for each domain |
| [Organize files by feature](guidelines/javascript.md#organize-files-by-feature-not-by-type) | creating a file, or deciding where new code lives |
| [Avoid getters](guidelines/javascript.md#avoid-getters) | adding a computed value to a class or a component |
| [Patch sparingly](guidelines/javascript.md#patch-sparingly) | extending or overriding behaviour that already exists |
| [Write each file as an ES module](guidelines/javascript.md#write-each-file-as-an-es-module-with-absolute-imports) | creating a JS file, writing imports, or the `@odoo-module` header |
| [Patch with `patch` and call `super`](guidelines/javascript.md#patch-the-prototype-with-patch-and-call-super) | writing a `patch` |
| [Translate with `_t`](guidelines/javascript.md#translate-every-user-facing-string-with-_t) | adding user-facing text in JavaScript |
| [Owl in $version](guidelines/owl.md#owl-in-${major}0) | writing or changing an Owl component |
| [Declare every prop](guidelines/owl.md#declare-every-prop-the-component-takes) | adding or changing a component's props |
| [Keep component state reactive](guidelines/owl.md#keep-component-state-reactive) | adding state, signals or derived values to a component |
| [Name templates and keep them in XML](guidelines/owl.md#name-templates-modulecomponent-and-keep-them-in-xml-files) | writing an Owl template |
| [Extend a template with `t-inherit`](guidelines/owl.md#extend-a-template-with-t-inherit-never-by-copying-it) | changing another module's Owl template |
| [Load data in `onWillStart`](guidelines/owl.md#load-data-in-onwillstart-not-in-setup) | loading data or using lifecycle hooks and effects |
| [Reach the DOM through a ref](guidelines/owl.md#reach-the-dom-through-a-ref-and-listen-outside-it-through-a-hook) | touching DOM elements or adding global listeners |
| [Pass shared values through props or the environment](guidelines/owl.md#pass-shared-values-through-props-or-the-environment) | passing data between components |
| [Registries in $version](guidelines/registries.md#registries-in-${major}0) | adding to any `registry.category(...)` |
| [Prefix every registry key](guidelines/registries.md#prefix-every-registry-key-with-the-module) | choosing a registry key, widget name or client action tag |
| [Systray, user menu and main components](guidelines/registries.md#systray-user-menu-and-main-components) | adding a navbar item, user menu entry or root component |
| [Client actions and action handlers](guidelines/registries.md#client-actions-and-action-handlers) | writing an `ir.actions.client` tag, an action type or a report handler |
| [Command palette](guidelines/registries.md#command-palette) | adding commands to the command palette |
| [Debug menu](guidelines/registries.md#debug-menu) | adding a debug menu item |
| [Error handling](guidelines/registries.md#error-handling) | showing a custom server error or catching client errors |
| [Effects, dialogs and lazy components](guidelines/registries.md#effects-dialogs-and-lazy-components) | adding an effect or lazily loaded component |
| [Fields, views and view widgets registries](guidelines/registries.md#fields-views-and-view-widgets) | registering a field, view, widget or form compiler |
| [Control panel menus](guidelines/registries.md#control-panel-menus) | adding to the gear or favorites menu |
| [Formatters, parsers and the sample server](guidelines/registries.md#formatters-parsers-and-the-sample-server) | formatting or parsing values, or sample data |
| [Frontend registries](guidelines/registries.md#frontend-registries) | code in `web.assets_frontend` |
| [Registries of this version only](guidelines/registries.md#registries-of-this-version-only) | using a registry not listed above |
| [Services in $version](guidelines/services.md#services-in-${major}0) | using any service or plugin |
| [Get a service through its hook](guidelines/services.md#get-a-service-through-its-hook-never-through-a-global) | calling `useService`, `usePlugin` or `env.services` |
| [Keep shared logic out of components](guidelines/services.md#keep-shared-logic-and-shared-state-out-of-components) | writing a service or plugin |
| [Call model methods with `orm`](guidelines/services.md#call-model-methods-with-the-orm-service) | calling a model method from JavaScript |
| [Call a route with `rpc`](guidelines/services.md#call-a-route-with-rpc) | calling a controller route from JavaScript |
| [Open actions with `action`](guidelines/services.md#open-actions-with-the-action-service) | opening an action or switching views |
| [Notify and ask](guidelines/services.md#notify-with-notification-ask-with-dialog) | showing a notification, dialog or confirmation |
| [Read the user and the companies](guidelines/services.md#read-the-user-and-the-companies) | reading the user, groups or companies |
| [Change the URL through the router](guidelines/services.md#change-the-url-through-the-router) | reading or changing the URL |
| [Read shared context from `env`](guidelines/services.md#read-shared-context-from-env-never-write-to-it) | using `env` |
| [Views on the client side in $version](guidelines/views.md#views-on-the-client-side-in-${major}0) | choosing between a field widget, view widget, js_class or patch |
| [Write a field widget](guidelines/views.md#write-a-field-widget-as-a-component-plus-a-registry-entry) | writing a field widget |
| [Read options in `extractProps`](guidelines/views.md#read-arch-attributes-and-options-in-extractprops) | passing arch attributes or options to a widget |
| [Prefix a widget key with a view type](guidelines/views.md#prefix-a-widget-key-with-a-view-type-to-change-it-in-one-view-only) | making a widget differ in one view type |
| [Extend a view with `js_class`](guidelines/views.md#extend-a-view-with-js_class-never-by-patching-it-for-one-model) | customizing a view's controller, renderer or model |
| [Add a `<widget>`](guidelines/views.md#add-a-widget-to-a-view-through-view_widgets) | writing a `<widget name=...>` |
| [Frontend code in $version](guidelines/website.md#frontend-code-in-${major}0) | writing JS for website, portal or public pages |
| [Attach behaviour to a selector](guidelines/website.md#attach-behaviour-to-a-selector-never-to-the-whole-page) | writing a public widget or interaction |
| [Release everything when it stops](guidelines/website.md#release-everything-the-code-added-when-it-stops) | adding listeners, timers or elements from frontend code |
| [Mount an Owl component in a page](guidelines/website.md#mount-an-owl-component-in-a-page-with-owl-component) | putting an Owl component in a QWeb page |
| [Call the server from a public page](guidelines/website.md#call-the-server-from-a-public-page-through-a-controller) | fetching data from a public page |
| [Extend the portal](guidelines/website.md#extend-the-portal-with-your-own-documents) | adding documents or cards to `/my` |
| [Add a building block](guidelines/website.md#add-a-building-block-snippet) | writing a website snippet or its options |
| [The Point of Sale in $version](guidelines/point_of_sale.md#the-point-of-sale-in-${major}0) | any code in the Point of Sale |
| [Load a field into the Point of Sale](guidelines/point_of_sale.md#load-a-field-into-the-point-of-sale-from-python) | making a field or model available in the POS |
| [Extend POS models and screens](guidelines/point_of_sale.md#extend-point-of-sale-models-and-screens-without-replacing-them) | changing POS orders, lines, store or screens |
| [Add a button to the product screen](guidelines/point_of_sale.md#add-a-button-to-the-product-screen-through-its-extension-point) | adding a POS control button |
| [Keep the POS working offline](guidelines/point_of_sale.md#keep-the-point-of-sale-working-offline) | calling the server from the POS |
| [Test the POS with tours](guidelines/point_of_sale.md#test-the-point-of-sale-with-tours) | writing POS tours |
| [Unit tests in $version](guidelines/tests.md#unit-tests-in-${major}0) | writing JavaScript unit tests |
| [Mock the server with test models](guidelines/tests.md#mock-the-server-with-test-models-never-with-a-database) | declaring test models or mocking RPCs |
| [Interact through the test helpers](guidelines/tests.md#interact-through-the-test-helpers-and-wait-for-the-dom) | clicking, typing or waiting in a JS test |
| [Undo every patch a test makes](guidelines/tests.md#undo-every-patch-a-test-makes) | patching in a test |
| [Register a tour](guidelines/tests.md#register-a-tour-in-the-web_tourtours-registry) | writing a tour |
| [Write each tour step](guidelines/tests.md#write-each-tour-step-as-a-trigger-and-an-action) | writing tour steps |
| [Run tours from an `HttpCase`](guidelines/tests.md#run-tours-from-an-httpcase) | starting a tour from Python |
| [SCSS and CSS](guidelines/scss.md#scss-and-css) | touching `*.scss` |
| [Assets](guidelines/assets.md#assets) | adding an image, font, or library |
| [Declare static files in the manifest](guidelines/assets.md#declare-static-files-in-the-manifest-assets) | editing the manifest `assets` |
| [Put each file in the right bundle](guidelines/assets.md#put-each-file-in-the-bundle-of-the-page-that-runs-it) | choosing a bundle |
| [Use a directive to place a file](guidelines/assets.md#use-a-directive-to-place-a-file-relative-to-another) | using prepend/before/after/replace/remove/include |
| [Keep an Owl template in the same bundle](guidelines/assets.md#keep-an-owl-template-in-the-same-bundle-as-its-component) | a "missing template" error, or moving XML files |
| [Load heavy code lazily](guidelines/assets.md#load-heavy-code-lazily) | adding a large library or rarely used screen |
| [Debug a bundle with `?debug=assets`](guidelines/assets.md#debug-a-bundle-with-debugassets) | debugging asset loading |

To add a guideline, follow [AUTHORING.md](AUTHORING.md).

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the $version source.
