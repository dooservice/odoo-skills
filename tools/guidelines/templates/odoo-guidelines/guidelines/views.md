# View records

- A view is an `ir.ui.view` record: `name` (`library.book.view.form`), `model`,
  `arch` with `type="xml"`, and for an extension `inherit_id` (see
  [xml.md](xml.md#inherit-views-by-extension-with-the-position-that-matches-the-change)).
- The root tag of `arch` is the view type: $view_types
- One view per type per model in the module that defines the model; other
  modules extend it. A second view of a type for a special screen is a
  `mode="primary"` view picked by its action or by a `<field>`'s
  `context="{'form_view_ref': 'library.library_book_view_form_simple'}"`
  (also `$list_tag_ref`, `kanban_view_ref`, `search_view_ref`).
- A view without `priority` gets `16`; the default view of a type for a model is
  the one with the lowest `priority`.
- Labels and strings in an arch are translated with the module: write them in
  English, as plain text, never as `_()`.

# Write dynamic modifiers in the syntax this version evaluates

$modifier_rule

```xml
$modifier_example
```

$modifier_fields

# Form views

- Layout: `<header>` (action buttons, then the status field with
  `widget="statusbar"`), `<sheet>`, then $chatter_tag.
- In the sheet: `<div class="oe_button_box" name="button_box">` for smart buttons
  (`type="object"` or `type="action"`, `class="oe_stat_button"`, an `icon`), a
  `widget="web_ribbon"` (`title`, `bg_color`) for archived or special states,
  `<div class="oe_title"><h1><field name="name"/></h1></div>`, then `<group>`s
  and a `<notebook>` of `<page name="..." string="...">` (give each page a `name`:
  extensions anchor on it).
- `<group>` makes a two-column grid of label and field: two nested `<group>`s
  side by side; `col` and `colspan` change the grid only when the default fails.
  Outside a group, a field needs a `<label for="field_name"/>` or `nolabel="1"`.
- The status field: `<field name="state" widget="statusbar"
  statusbar_visible="draft,confirmed,done"/>`; `options="{'clickable': '1'}"`
  lets users change the state by clicking, which skips the action methods: only
  on states without logic.
- Buttons: `type="object"` calls a public method of the model (not starting with
  `_`), `type="action"` opens `name="%(module.action_xml_id)d"`; `confirm="..."`
  asks first, `context="{...}"` passes values, `class="btn-primary"` on the one
  main button, `special="cancel"` (or `save`) in a dialog `<footer>`.$button_labels
- Field attributes: `widget`, `options="{...}"` (per widget: `no_create`,
  `no_open` on relations), `placeholder`, `help`, `context`, `domain`, `nolabel`,
  `mode` (`$list_tag,kanban` on x2many), `force_save="1"` to send a readonly
  field's value on save (otherwise readonly values computed in the client are
  dropped).
- x2many fields embed their sub-views inline: `<field name="line_ids"><$list_tag
  editable="bottom">...</$list_tag></field>`; an inline view reads only the fields
  it declares.
- Root attributes `create="0"`, `edit="0"`, `delete="0"`, `duplicate="0"` hide the
  matching actions (not access control); `disable_autofocus="1"` stops focusing
  the first field.
- A wizard (`TransientModel`) form opened with `target="new"` ends with a
  `<footer>` holding its buttons: the confirm button `class="btn-primary"`, then
  `<button string="Cancel" special="cancel"/>`.

# List views

- Root `<$list_tag>`: `editable="top"` or `"bottom"` for inline edition,
  `multi_edit="1"` to edit several selected rows, `default_order="date desc, id"`,
  `limit` (page size), `groups_limit`$list_group_by,
  `create`/`edit`/`delete`/`import`/`export_xlsx` `="0"`, `sample="1"` to show
  sample data when empty, `expand="1"` to open groups.$open_form_view$list_attributes_extra
- `decoration-<style>="<expression>"` colors a row (or one field): `bf`, `it`,
  `danger`, `info`, `muted`, `primary`, `success`, `warning`. Keep them few and
  meaningful: `decoration-muted="state == 'cancel'"`.
- Column fields: `optional="show"` or `"hide"` lets users toggle the column
  (mark optional every column that is not essential); `sum="Total"`, `avg`,
  `min`, `max` add a footer aggregate; `widget="handle"` on a `sequence` field
  makes rows draggable; `width` fixes a column; $column_invisible
- `<header>` with buttons acts on the selected records; `<button>` in a row acts
  on its record; `<control>` with `<create string="Add a line"
  context="{...}"/>` replaces the add-line links of an x2many list; `<groupby
  name="partner_id">` adds buttons to the group rows of a many2one.$list_column

# Kanban views

$kanban_template

```xml
$kanban_example
```

- Root attributes: `default_group_by`, `default_order`, `quick_create="0"` or
  `quick_create_view` (a small form), `on_create` (an action instead of the
  form), `group_create`/`group_delete`/`group_edit`, `records_draggable`,
  `groups_draggable`, `archivable`, `sample="1"`$kanban_attributes.
- `<progressbar field="state" colors='{"done": "success", "blocked": "danger"}'
  sum_field="amount"/>` shows a bar per column.
- Inside the template: `<field name="..."/>` renders the field with its widget;
  `record.<field>.value` (formatted) and `record.<field>.raw_value` read values in
  `t-if`/`t-esc`; `<a type="object" name="...">` and `<a type="open">` act on the
  record; `<widget name="...">` mounts a view widget.$kanban_card

# Search views

- `<field name="partner_id"/>` searches a field; `filter_domain="['|', ('name',
  'ilike', self), ('ref', 'ilike', self)]"` searches several, `operator`
  changes the comparison.
- `<filter name="available" string="Available" domain="[('state', '=',
  'available')]"/>`: $filter_name filters in the same block are OR-ed;
  `<separator/>` starts a new block, AND-ed with the others.
- Date filters: `<filter name="published" date="published_on"/>` gives period
  options; `default_period` picks the initial one$date_filter_extra.
- Group by: `<filter name="group_author" context="{'group_by': 'author_id'}"/>`
  (`'published_on:month'` for a date interval), inside $search_group.
- Default filters come from the action context: `search_default_<filter name>`,
  `1` to activate it.
- `<searchpanel>` adds a side panel: `<field name="category_id" icon="fa-folder"
  enable_counters="1"/>` is a category (one value, `hierarchize` on parent
  fields); `select="multi"` makes it a filter (several values, `groupby`,
  `domain`). One searchpanel per view.
- `invisible="1"` hides a filter that only actions activate.

# Calendar, graph and pivot views

- Calendar: `<calendar date_start="start" date_stop="stop" color="user_id"
  mode="week">`; `all_day` names a boolean for all-day events$calendar_delay;
  `mode` is `day`, `week`, `month` or `year`, `scales` limits the choice;
  $calendar_quick; `event_open_popup="1"` opens events in a dialog,
  `form_view_id` picks the form. A `<field
  name="user_id" filters="1" avatar_field="avatar_128"/>` adds a side filter;
  `write_model`/`write_field` save the user's filter choices.$calendar_extra
- Graph: `<graph type="bar" stacked="1">` (`bar`, `line`, `pie`), `order`
  (`asc`/`desc`), `cumulated="1"` on lines, `disable_linking="1"` to stop opening
  the records on click; `<field name="amount" type="measure"/>` sets the measure,
  every other field is a group-by in order (`interval="month"` on dates).
- Pivot: `<pivot display_quantity="1">`; `<field name="author_id" type="row"/>`,
  `type="col"`, `type="measure"`, and `interval` on dates;
  `disable_linking="1"` as in graph.
- Measures must be stored numeric fields; their aggregate comes from the field
  definition ($aggregator).

# Activity, hierarchy and QWeb views

- Activity (`mail`): `<activity string="Books">` (`string` is required) with a
  `<templates><div t-name="activity-box">...</div></templates>` per record; it
  lists the activities of models with `mail.activity.mixin`.
- $hierarchy
- QWeb (`type="qweb"`) views are templates, written with `<template id="...">`:
  reports, website and portal pages, mail layouts. They are not opened by
  actions; see [reports.md](reports.md#qweb-pdf-reports).

# Show and hide view parts by group

- `groups="base.group_no_one,library.group_librarian"` on any node shows it
  only to members of one of the groups; `!library.group_librarian` excludes
  them. The server removes the node from the arch for others.
- `groups` hides; it does not protect. A field restricted for security has
  `groups=` on its definition in Python, which also blocks RPC reads.
- A view record can be limited to groups with $view_groups (not on an
  extension); prefer `groups` on the nodes.
