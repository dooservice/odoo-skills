# Views, actions and data records

- Record format: put `id` before `model`; inside a `field`, `name` first, then
  the value (tag body or `eval`), then other attributes by importance. Group
  records by model.
- Prefer the syntactic-sugar tags `<menuitem>` and `<template>` over raw
  `<record>`. Trap: an `active` attribute on `<template>` is applied at
  record creation and module *install/re-install* (`-i`) only; a module
  **update** (`-u`) updates the arch but never changes `active`, so it can't
  deactivate an already-installed record.
- `<report>` and `<act_window>` still load in this version but later versions
  drop them: write `<record model="ir.actions.report">` and
  `<record model="ir.actions.act_window">`.
- `<data noupdate="1">` only for non-updatable data; if the whole file is
  noupdate, set `noupdate="1"` on `<odoo>` and drop `<data>`.
- The list view is `<tree>` and its view_mode is `tree`.
- Dynamic visibility and editability: `attrs="{'invisible': [('state', '!=', 'draft')]}"`
  and `states="draft"` on buttons. Keep the domain short; a field used in
  `attrs` must be in the view (add it `invisible="1"` when needed).
- The chatter of a form inheriting `mail.thread` goes last:
  `<div class="oe_chatter"><field name="message_follower_ids"/>
  <field name="activity_ids"/><field name="message_ids"/></div>`.
- XML id patterns: view `<model>_view_<type>` (`form`/`tree`/`kanban`/`search`),
  action `<model>_action[_<detail>]`, window-action view
  `<model>_action_view_<type>`, menu `<model>_menu[_<do_stuff>]`, group
  `<module>_group_<name>`, rule `<model>_rule_<group>`. The record `name` mirrors
  the id with dots instead of underscores; actions get a real display name.
- CSS classes in views and templates: prefix with `o_<module>` (`o_` alone is
  reserved for the web client), never style through ids, and keep names flat
  (`o_element_entry`) rather than mirroring the DOM nesting.
- Views by type: see [View records](views.md#view-records); actions, crons and
  menus: see [Action records](actions.md#action-records).
- Inheriting a view: see
  [Anchor view inheritance on names, never on position](#anchor-view-inheritance-on-names-never-on-position).

# Field values in data records

- `<field name="x">text</field>` sets a literal (a `Char`, `Text`, `Selection`
  key, or a number the field converts).
- `ref="module.xml_id"` sets a many2one; the module prefix is optional for the
  module's own records. A record must be loaded before another refers to it:
  order the manifest's `data` list and the records in a file accordingly.
- `eval="..."` is a Python expression, for booleans (`eval="True"`), numbers,
  dates and x2many commands: `eval="[Command.set([ref('base.group_user')])]"`,
  `eval="[Command.link(ref('library_tag_novel'))]"`. Available names: `ref`,
  `Command`, `time`, `datetime`, `DateTime`, `timedelta`, `relativedelta`,
  `version`, `pytz`, and `obj` (browse of the record's model).
- `search="[('code', '=', 'X')]"` sets the first match (all matches on a
  many2many); `use="code"` takes another field than `id`. Prefer `ref`: a search
  depends on data the module does not control.
- `type="xml"` and `type="html"` keep the body as markup: `arch`, `body_html`.
  In them, `%(module.xml_id)d` is replaced by the record's database id (`%%`
  for a literal `%`): `<button name="%(library_book_action)d" type="action"/>`.
- `type="base64"` stores the body, or with `file=` the file, base64-encoded.
- `type="int"`, `type="float"`, `type="list"` and `type="tuple"`
  convert the body; `file="module/path"` reads the value from a file.
- `context="{...}"` on a `<record>` passes a context to its `create`/`write`.

# Load only what an update can redo

A data file is reloaded on every module update: each `<record>` is written
again with the values in the file, and changes an administrator made to those
fields are lost. Put in `noupdate="1"` every record users are expected to edit
(sequences, crons, mail templates, default stages, record rules a site adapts);
keep views, actions and menus updatable so fixes reach existing databases.

- `noupdate` records are created at install; an update creates them again only
  when missing, and `forcecreate="0"` on the `<record>` stops even that (and
  skips the record instead of failing when a `ref` does not resolve). Changing a
  `noupdate` record later needs a migration script or a `<function>`.
- `<function model="library.book" name="_init_shelves"/>` calls a model method
  at load (`eval="[...]"` or `<value>` children are its arguments). It runs on
  every update unless it sits in `noupdate` data: make the method idempotent.
- `<delete model="library.tag" id="library_tag_old"/>` removes a record (or
  `search="[...]"` removes the matches); a missing id is logged, not an error.
  Use it for a `noupdate` record the module no longer ships: an updatable record
  of the module that is gone from its files is deleted at the end of the update
  anyway, while a `noupdate` one stays in every existing database.
- Edit another module's record only when that is the purpose:
  `<record id="other_module.xml_id" model="...">` with only the fields you
  change. When that record is updatable, the other module's next update
  writes its own values back.

# Inherit views by extension, with the position that matches the change

- An extension view sets `inherit_id` and changes the parent in place for every
  user of the parent; `mode="primary"` (with `inherit_id`) builds a new view from
  the parent instead, used only where it is referenced (an action's view, a
  `context` key such as `form_view_ref`, another view's `inherit_id`).
- `priority` (default `16`, lower first) orders the extensions of a view and
  picks the default view of a type for a model; leave it at the default unless
  two extensions must apply in a set order, or a view must win as the default.
- `position` is `inside` (default, appended as last children), `after`,
  `before`, `replace`, `attributes` or `move`.
  - `replace` with an empty body removes the node; prefer `invisible="1"` (or
    `position="attributes"`) on a field other extensions may anchor to: a
    removed node breaks their inheritance.
  - In a `replace` body, `$0` stands for the replaced node, to wrap it.
  - `position="move"` on a child element moves an existing node:
    `<xpath expr="//field[@name='tag_ids']" position="after"><field name="author_id" position="move"/></xpath>`.
  - `position="attributes"` with `<attribute name="string">Title</attribute>`
    replaces a value; an empty body removes the attribute; `add`/`remove`
    edit a list attribute (`separator`, default `,`).
- One extension per parent view and per module; group the changes in one arch
  rather than one view per change.

# Anchor view inheritance on names, never on position

Anchor a view inheritance on a **stable, identifying attribute** (an
element's `name`), never on document position.

```xml
<!-- good: the shorthand form, which matches a field by name alone -->
<field name="partner_id" position="after">
    <field name="delivery_instructions"/>
</field>

<!-- good: xpath when the shorthand can't express the match -->
<xpath expr="//page[@name='other_information']//field[@name='user_id']" position="attributes">
    <attribute name="readonly">1</attribute>
</xpath>

<!-- bad: breaks as soon as the parent view inserts or reorders anything -->
<xpath expr="//group[2]/field[3]" position="after">
    <field name="delivery_instructions"/>
</xpath>
```

Shorthand matching is asymmetric: a `field` element matches the first field
with the same `name`, in document order at **any** depth (use xpath when the
name recurs in an embedded subview), other locator attributes ignored. Any
**other** tag matches the first node with the same tag carrying all the
locator's attributes with equal values (`position` excepted); extra attributes
on the target are fine.

## Why

- The parent view belongs to another module that changes it freely; a
  positional match silently lands the change on the wrong element or raises
  at install on every parent reorganization.
- The shorthand form reads as "this element, changed", and fails loudly if
  the anchor disappears.

## Record conventions

- An inheriting view reuses the **same xml id** as the original record; its
  `name` carries an `.inherit.<details>` suffix.
- A new **primary** view (a variant, not an extension) sets `mode="primary"`
  and needs no inherit suffix.
- Don't re-add fields the parent view already renders.
