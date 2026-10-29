# View records

- A view is an `ir.ui.view` record: `name` (`library.book.view.form`), `model`,
  `arch` with `type="xml"`, and for an extension `inherit_id` (see
  [xml.md](xml.md#inherit-views-by-extension-with-the-position-that-matches-the-change)).
- The root tag of `arch` is the view type: `<form>`, `<list>`, `<kanban>`, `<card>`, `<search>`, `<calendar>`, `<graph>`,
  `<pivot>`, `<activity>` (from `mail`), `<hierarchy>` (from `web_hierarchy`); `qweb` is the type of
  `<template>` records.
- One view per type per model in the module that defines the model; other
  modules extend it. A second view of a type for a special screen is a
  `mode="primary"` view picked by its action or by a `<field>`'s
  `context="{'form_view_ref': 'library.library_book_view_form_simple'}"`
  (also `list_view_ref`, `kanban_view_ref`, `search_view_ref`).
- A view without `priority` gets `16`; the default view of a type for a model is
  the one with the lowest `priority`.
- Labels and strings in an arch are translated with the module: write them in
  English, as plain text, never as `_()`.

# Write dynamic modifiers in the syntax this version evaluates

`invisible`, `readonly`, `required` and, on list columns, `column_invisible`
take a Python expression evaluated in the client on the record's values. It
reads the record's fields, `id`, `parent` (the record that holds an x2many),
`context`, `uid`, `current_company_id`, `allowed_company_ids`,
`context_today()`, `today` and `now`. `attrs` and `states` are refused at
install with a `ValidationError`: translate each domain into an expression.

```xml
<field name="partner_id" readonly="state != 'draft'" required="kind == 'loan'"/>
<button name="action_confirm" type="object" string="Confirm" invisible="state != 'draft'"/>
<!-- in the list of an x2many -->
<field name="price" column_invisible="parent.kind == 'gift'"/>
```

The server adds, invisible and readonly, the fields that a modifier, a
`domain`, a `context` or a `decoration-*` reads and the view lacks: do not add
`invisible="1"` copies of them.

# Form views

- Layout: `<header>` (action buttons, then the status field with
  `widget="statusbar"`), `<sheet>`, then `<chatter/>` when the model inherits `mail.thread`.
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
  main button, `special="cancel"` (or `save`) in a dialog `<footer>`.
  `confirm-title`, `confirm-label` and `cancel-label` set the title and the
  buttons of the confirmation.
- Field attributes: `widget`, `options="{...}"` (per widget: `no_create`,
  `no_open` on relations), `placeholder`, `help`, `context`, `domain`, `nolabel`,
  `mode` (`list,kanban` on x2many), `force_save="1"` to send a readonly
  field's value on save (otherwise readonly values computed in the client are
  dropped).
- x2many fields embed their sub-views inline: `<field name="line_ids"><list
  editable="bottom">...</list></field>`; an inline view reads only the fields
  it declares.
- Root attributes `create="0"`, `edit="0"`, `delete="0"`, `duplicate="0"` hide the
  matching actions (not access control); `disable_autofocus="1"` stops focusing
  the first field.
- A wizard (`TransientModel`) form opened with `target="new"` ends with a
  `<footer>` holding its buttons: the confirm button `class="btn-primary"`, then
  `<button string="Cancel" special="cancel"/>`.

# List views

- Root `<list>`: `editable="top"` or `"bottom"` for inline edition,
  `multi_edit="1"` to edit several selected rows, `default_order="date desc, id"`,
  `limit` (page size), `groups_limit`, `default_group_by` (comma-separated for several levels),
  `create`/`edit`/`delete`/`import`/`export_xlsx` `="0"`, `sample="1"` to show
  sample data when empty, `expand="1"` to open groups.
  `open_form_view="1"` adds a button opening the form on each row of an
  editable list.
  `group_create`, `group_edit`, `group_delete` allow managing the groups.
- `decoration-<style>="<expression>"` colors a row (or one field): `bf`, `it`,
  `danger`, `info`, `muted`, `primary`, `success`, `warning`. Keep them few and
  meaningful: `decoration-muted="state == 'cancel'"`.
- Column fields: `optional="show"` or `"hide"` lets users toggle the column
  (mark optional every column that is not essential); `sum="Total"`, `avg`,
  `min`, `max` add a footer aggregate; `widget="handle"` on a `sequence` field
  makes rows draggable; `width` fixes a column; `column_invisible="True"`
  (or an expression on `parent.` and `context`) hides the whole column,
  `invisible` empties the cell per record.
- `<header>` with buttons acts on the selected records; `<button>` in a row acts
  on its record; `<control>` with `<create string="Add a line"
  context="{...}"/>` replaces the add-line links of an x2many list; `<groupby
  name="partner_id">` adds buttons to the group rows of a many2one.
- `<column string="Product">` with several `<field>`s shows them stacked
  under one header.

# Kanban views

The record template is `<t t-name="card">` inside `<templates>`: the whole card
opens the record, `<aside>` and `<footer>` place a side image and a bottom row,
and a `<t t-name="menu">` template fills the dropdown menu. A `kanban-box`
template is refused: write `card` and `menu`.

```xml
<kanban default_group_by="state" highlight_color="color">
    <templates>
        <t t-name="card">
            <field name="name" class="fw-bold"/>
            <field name="author_id"/>
            <footer>
                <field name="tag_ids" widget="many2many_tags"/>
            </footer>
        </t>
    </templates>
</kanban>
```

- Root attributes: `default_group_by`, `default_order`, `quick_create="0"` or
  `quick_create_view` (a small form), `on_create` (an action instead of the
  form), `group_create`/`group_delete`/`group_edit`, `records_draggable`,
  `groups_draggable`, `archivable`, `sample="1"`, `highlight_color="color"`
  (an integer color field), `can_open="0"` (the card does not open the record).
- `<progressbar field="state" colors='{"done": "success", "blocked": "danger"}'
  sum_field="amount"/>` shows a bar per column.
- Inside the template: `<field name="..."/>` renders the field with its widget;
  `record.<field>.value` (formatted) and `record.<field>.raw_value` read values in
  `t-if`/`t-esc`; `<a type="object" name="...">` and `<a type="open">` act on the
  record; `<widget name="...">` mounts a view widget.
- A `card` view (`<card>` root, `<templates><t t-name="card">`) is a card
  layout several views share: `<kanban card_id="%(library.library_book_view_card)d">`
  inlines it, and so does a calendar's `<popover card_id="...">`. Keep the
  template in the kanban unless two views use it.

# Search views

- `<field name="partner_id"/>` searches a field; `filter_domain="['|', ('name',
  'ilike', self), ('ref', 'ilike', self)]"` searches several, `operator`
  changes the comparison.
- `<filter name="available" string="Available" domain="[('state', '=',
  'available')]"/>`: `name` is required; filters in the same block are OR-ed;
  `<separator/>` starts a new block, AND-ed with the others.
- Date filters: `<filter name="published" date="published_on"/>` gives period
  options; `default_period` picks the initial one, and `start_month`, `end_month`,
  `start_year`, `end_year` bound the offered periods; `end_date` names a second
  date field so the filter matches records whose period overlaps the chosen one.
- Group by: `<filter name="group_author" context="{'group_by': 'author_id'}"/>`
  (`'published_on:month'` for a date interval), inside a bare `<group>` (`expand` and `string` are refused).
- Default filters come from the action context: `search_default_<filter name>`,
  `1` to activate it.
- `<searchpanel>` adds a side panel: `<field name="category_id" icon="fa-folder"
  enable_counters="1"/>` is a category (one value, `hierarchize` on parent
  fields); `select="multi"` makes it a filter (several values, `groupby`,
  `domain`). One searchpanel per view.
- `invisible="1"` hides a filter that only actions activate.

# Calendar, graph and pivot views

- Calendar: `<calendar date_start="start" date_stop="stop" color="user_id"
  mode="week">`; `all_day` names a boolean for all-day events, and a length
  comes from `date_stop` only (compute it from a duration);
  `mode` is `day`, `week`, `month` or `year`, `scales` limits the choice;
  `quick_create="0"` disables quick creation and
  `quick_create_view_id` picks the form it uses; `event_open_popup="1"` opens events in a dialog,
  `form_view_id` picks the form. A `<field
  name="user_id" filters="1" avatar_field="avatar_128"/>` adds a side filter;
  `write_model`/`write_field` save the user's filter choices.
  `create`, `edit`, `delete` `="0"` hide those actions; `aggregate="amount:sum"`
  totals a field per day; `multi_create_view` names the form that creates
  several events at once; `<popover>` with `<field>`s sets the event popover.
- Graph: `<graph type="bar" stacked="1">` (`bar`, `line`, `pie`), `order`
  (`asc`/`desc`), `cumulated="1"` on lines, `disable_linking="1"` to stop opening
  the records on click; `<field name="amount" type="measure"/>` sets the measure,
  every other field is a group-by in order (`interval="month"` on dates).
- Pivot: `<pivot display_quantity="1">`; `<field name="author_id" type="row"/>`,
  `type="col"`, `type="measure"`, and `interval` on dates;
  `disable_linking="1"` as in graph.
- Measures must be stored numeric fields; their aggregate comes from the field
  definition (`aggregator`).

# Activity, hierarchy and QWeb views

- Activity (`mail`): `<activity string="Books">` (`string` is required) with a
  `<templates><div t-name="activity-box">...</div></templates>` per record; it
  lists the activities of models with `mail.activity.mixin`.
- Hierarchy (`web_hierarchy`): `<hierarchy parent_field="parent_id"
  child_field="child_ids" avatar_field="image_128" draggable="1">` draws an
  org chart; `parent_field` is a many2one and `child_field` a one2many to
  the same model, and the node is a `<templates><t t-name="hierarchy-box">`
  template.
- QWeb (`type="qweb"`) views are templates, written with `<template id="...">`:
  reports, website and portal pages, mail layouts. They are not opened by
  actions; see [reports.md](reports.md#qweb-pdf-reports).

# Show and hide view parts by group

- `groups="base.group_no_one,library.group_librarian"` on any node shows it
  only to members of one of the groups; `!library.group_librarian` excludes
  them. The server removes the node from the arch for others.
- `groups` hides; it does not protect. A field restricted for security has
  `groups=` on its definition in Python, which also blocks RPC reads.
- A view record can be limited to groups with `group_ids` (not on an
  extension); prefer `groups` on the nodes.
