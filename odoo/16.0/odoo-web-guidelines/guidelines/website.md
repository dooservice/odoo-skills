# Frontend code in 16.0

Public pages (website, portal, login, shop) are server-rendered QWeb; JavaScript only
adds behaviour to the HTML the server sent. That code goes in `web.assets_frontend`,
which every public page loads, and it must run for visitors who are not logged in.

Behaviour is written as a public widget: `publicWidget.Widget.extend({...})` from
`@web/legacy/js/public/public_widget`, registered in `publicWidget.registry`. It is the
legacy widget class, not Owl: no templates, no reactivity, `this._super` for overrides.

# Attach behaviour to a selector, never to the whole page

A public widget is started on every element that matches its `selector`, and only
there: code that queries `document` runs on pages that do not have the element and
breaks them.

```js
/** @odoo-module **/
import publicWidget from "@web/legacy/js/public/public_widget";

publicWidget.registry.BookList = publicWidget.Widget.extend({
    selector: ".o_my_module_book_list",
    events: {
        "click .o_my_module_lend": "_onLendClick",
    },
    async start() {
        await this._super(...arguments);
        this.counterEl = this.el.querySelector(".o_my_module_counter");
    },
    _onLendClick(ev) {
        this.counterEl.textContent = ...;
    },
});
```

- `selector` scopes the widget, `events` binds handlers on elements inside it, and
  `start` runs once the widget is attached; it returns a promise and calls `_super`.
- A route is called with `this._rpc({ route: "/my_module/books", params: { limit: 10 } })`.

# Release everything the code added when it stops

A widget is destroyed when the editor enters edit mode, when a part of the page is
re-rendered, and when it is restarted; anything it left behind (a listener on
`window`, an interval, an element appended to `body`) then runs twice or leaks.

- Bind handlers through `events`, which are unbound for you; a listener on `window` or
  `document` is added in `start` and removed in `destroy`.
- Clear intervals and timeouts in `destroy`, and remove elements the widget inserted
  outside its own element.
- `destroy` calls `this._super(...arguments)`.
- Code that must not run while the page is edited checks
  `this.options.editableMode`, which the website editor sets when it starts the
  widget, and returns early.

# Mount an Owl component in a page with `<owl-component>`

This version has no registry for Owl components on public pages: write the behaviour
as a public widget.

# Call the server from a public page through a controller

- Read and write data through a route of your module (`@http.route(..., type='json',
  auth='public', website=True)`) that checks what a visitor may see, and call it with
  `this._rpc({ route: "/my_module/books", params: { limit: 10 } })` from a public
  widget.
- Never call model methods from frontend code through `/web/dataset/call_kw` with a
  visitor's session: the public user has almost no access rights, and the route that
  works for you as an administrator fails for every visitor.
- A form that posts and reloads needs no JavaScript: a plain `<form method="post">` with
  `<input type="hidden" name="csrf_token" t-att-value="request.csrf_token()"/>`.

# Extend the portal with your own documents

The portal is `/my`: a home page of cards, one per kind of document, and a list and a
detail page per kind.

- A list page renders through `portal.portal_layout` and its table through
  `portal.portal_table`; the detail page uses `portal.portal_sidebar` and
  `portal.record_pager`. Inherit them instead of building a layout.
- The controller extends `CustomerPortal` (`odoo.addons.portal.controllers.portal`):
  `_prepare_portal_layout_values()` gives the values every `/my` page needs, and
  `_document_check_access(model_name, document_id, access_token)` returns the record in
  `sudo` only after checking the user's access or the token; never browse the record
  with `sudo()` yourself.
- A home card is a `portal.portal_docs_entry` call added to `portal.portal_my_home`,
  with `placeholder_count` naming a counter (`book_count`). The page asks
  `/my/counters` for the counters it shows, and the controller answers in
  `_prepare_home_portal_values(counters)`: compute a value only when its key is in
  `counters`, with `search_count`, and only if the user has read access.

# Add a building block (snippet)

- The block itself is a QWeb template whose id starts with `s_`
  (`<template id="s_book_list" name="Book List">`), with `data-snippet="s_book_list"`
  on its root and the `o_` classes of your module.
- It appears in the editor through `website.snippets`: inherit it and add
  `<t t-snippet="my_module.s_book_list" t-thumbnail="/my_module/static/src/img/s_book_list.svg"/>` in the right
  group.
- Options are declared in a template inheriting `website.snippet_options`: a
  `<div data-selector=".s_book_list">` holding `we-*` controls (`<we-select>`,
  `<we-checkbox>`, `<we-colorpicker>`) whose `data-select-class` or
  `data-select-data-attribute` change the block. JavaScript is needed only for an
  option that computes something: `options.registry.BookList = options.Class.extend({...})`
  from the editor's snippet options module, named in `data-js="BookList"`.
- Behaviour of the block on the published page is ordinary frontend code:
  a public widget whose `selector` is the block's class.
