# Views, actions and data records

- Record format: put `id` before `model`; inside a `field`, `name` first, then
  the value (tag body or `eval`), then other attributes by importance. Group
  records by model.
- Prefer the syntactic-sugar tags `<menuitem>` and `<template>` over raw
  `<record>`. Trap: an `active` attribute on `<template>` is applied at record
  creation and module *install* only; a module **update** never changes `active`.
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
  action `<model>_action[_<detail>]`, menu `<model>_menu[_<do_stuff>]`, group
  `<module>_group_<name>`, rule `<model>_rule_<group>`. The record `name` mirrors
  the id with dots instead of underscores; actions get a real display name.
- CSS classes in views and templates: prefix with `o_<module>` (`o_` alone is
  reserved for the web client), never style through ids.
- Inheriting a view: see
  [Anchor view inheritance on names, never on position](#anchor-view-inheritance-on-names-never-on-position).

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
