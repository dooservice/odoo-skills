Key names in $version:

$essentials

Sections of this file:

$sections

# Frontend code in $version

Public pages (website, portal, login, shop) are server-rendered QWeb; JavaScript only
adds behaviour to the HTML the server sent. That code goes in `web.assets_frontend`,
which every public page loads, and it must run for visitors who are not logged in.

$frontend_model

# Attach behaviour to a selector, never to the whole page

$attach

# Release everything the code added when it stops

$cleanup

# Mount an Owl component in a page with `<owl-component>`

$owl_component

# Call the server from a public page through a controller

- Read and write data through a route of your module (`@http.route(..., type='$json_type',
  auth='public', website=True)`) that checks what a visitor may see, and call it with
  $rpc_frontend.
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
- $portal_counter

# Add a building block (snippet)

- The block itself is a QWeb template whose id starts with `s_`
  (`<template id="s_book_list" name="Book List">`), with `data-snippet="s_book_list"`
  on its root and the `o_` classes of your module.
- It appears in the editor through `website.snippets`: inherit it and add
  `<t t-snippet="my_module.s_book_list" $snippet_attr/>` in the right
  group.
- $snippet_options
- Behaviour of the block on the published page is ordinary frontend code:
  $snippet_js
