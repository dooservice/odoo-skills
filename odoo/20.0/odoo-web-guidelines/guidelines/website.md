# Frontend code in 20.0

Public pages (website, portal, login, shop) are server-rendered QWeb; JavaScript only
adds behaviour to the HTML the server sent. That code goes in `web.assets_frontend`,
which every public page loads, and it must run for visitors who are not logged in.

Behaviour is written as an interaction: a class extending `Interaction` from
`@web/public/interaction`, registered in `registry.category("public.interactions")`.
Public widgets no longer exist: code written with `publicWidget` must be ported to an
interaction.

# Attach behaviour to a selector, never to the whole page

An interaction is started on every element that matches its `selector`, and only there:
code that queries `document` runs on pages that do not have the element and breaks them.

```js
import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";
import { rpc } from "@web/core/network/rpc";

export class BookList extends Interaction {
    static selector = ".o_my_module_book_list";
    dynamicContent = {
        ".o_my_module_lend": { "t-on-click": this.onLendClick },
        ".o_my_module_counter": { "t-out": () => this.count },
        _root: { "t-att-class": () => ({ o_my_module_empty: !this.count }) },
    };

    setup() {
        this.count = 0;
    }

    async willStart() {
        this.count = await this.waitFor(rpc("/my_module/book_count"));
    }

    onLendClick() {
        this.count--;
    }
}

registry.category("public.interactions").add("my_module.book_list", BookList);
```

- `static selector` scopes it; `static selectorHas` and `static selectorNotHas` start it
  only when the element contains, or does not contain, a match.
- `dynamicContent` maps selectors inside the element (and `_root`, `_body`, `_window`,
  `_document`) to `t-on-<event>`, `t-att-<attribute>`, `t-att-class`, `t-att-style` and
  `t-out`. It is not Owl: after a handler runs, the interaction re-applies the values,
  and after changing state elsewhere (a timer, a promise) call `this.updateContent()`.
- The lifecycle is `setup()`, `async willStart()`, `start()`, `destroy()`; never
  override the constructor. Handlers are bound to the interaction, and services are in
  `this.services`.

# Release everything the code added when it stops

An interaction is destroyed when the editor enters edit mode, when a part of the page is
re-rendered, and when it is restarted; anything it left behind then runs twice or
leaks. Use the helpers that undo themselves:

- `this.addListener(target, "scroll", handler)` for a listener outside the
  `dynamicContent` selectors, `this.insert(el)` for an element added to the page,
  `this.mountComponent(el, Component, props)` for an Owl component; all are removed on
  destroy.
- `this.waitFor(promise)` around every awaited call, and `this.protectSyncAfterAsync(fn)`
  for code that runs after one: they stop the code when the interaction was destroyed
  while waiting.
- `this.waitForTimeout(fn, delay)` and `this.waitForAnimationFrame(fn)` instead of
  `setTimeout` and `requestAnimationFrame`; `this.debounced(fn, delay)` and
  `this.throttled(fn)` for handlers.
- `this.registerCleanup(fn)` for anything else. `destroy()` is for the rare case left.

# Mount an Owl component in a page with `<owl-component>`

An Owl component in a QWeb page is declared in the HTML and mounted by an
interaction:

```xml
<owl-component name="my_module.book_card" t-att-props="json.dumps({'bookId': book.id})"/>
```

```js
registry.category("public_components").add("my_module.book_card", BookCard);
```

- The `name` attribute is the registry key; `props` is JSON, so pass ids and plain
  values, never records.
- Each component is its own small Owl application: it does not share state with
  another `<owl-component>` of the page. Use one when a block is truly interactive (a
  configurator, a live search); simple behaviour stays an interaction.

# Call the server from a public page through a controller

- Read and write data through a route of your module (`@http.route(..., type='jsonrpc',
  auth='public', website=True)`) that checks what a visitor may see, and call it with
  `rpc("/my_module/books", { limit: 10 })` (`rpc` from `@web/core/network/rpc`).
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
- A home card is a `portal.entry` record (data file): `name`, `url`, `category`,
  `sequence`, and `placeholder_count` naming a counter (`book_count`). The page asks
  `/my/counters` for the counters it shows, and the controller answers in
  `_prepare_portal_counter_values(counter)`, returning the model, the domain and the
  access to check (`"library.book", domain, "read"`) for its own counter and
  `super()` for the others; the count itself is done for you.

# Add a building block (snippet)

- The block itself is a QWeb template whose id starts with `s_`
  (`<template id="s_book_list" name="Book List">`), with `data-snippet="s_book_list"`
  on its root and the `o_` classes of your module.
- It appears in the editor through `website.snippets`: inherit it and add
  `<t t-snippet="my_module.s_book_list" group="content"/>` in the right
  group.
- Options are part of the website builder: their template is added to
  `website.BuilderOptions` (an extension with an `xpath` after the
  `snippet_specific_options` node, `<MyOption template="my_module.MyOption"
  selector=".s_book_list"/>`), with builder controls (`BuilderSelect`,
  `BuilderCheckbox`) and `classAction` or `dataAttributeAction`. Options that compute
  something add a `Plugin` with `builder_actions`, registered in
  `registry.category("website-plugins")`.
- Behaviour of the block on the published page is ordinary frontend code:
  an interaction whose `selector` is the block's class; code that must also run while
  editing is a separate entry of `registry.category("public.interactions.edit")`, in a
  `*.edit.js` file.
