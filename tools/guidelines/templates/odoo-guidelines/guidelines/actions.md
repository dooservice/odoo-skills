# Action records

Every action is a record of a model that extends `ir.actions.actions`, which holds
what all of them share:

- `name`: the title shown in the breadcrumb and the Action menu; a real display
  name, translated.
- `type`: the action model's name, set by the model itself; write it only in a dict
  returned from Python.
- `help`: HTML shown when the view is empty (`<p class="o_view_nocontent_smiling_face">`).
- `binding_model_id`, `binding_type`, `binding_view_types`: see
  [Bind actions to the Action and Print menus](#bind-actions-to-the-action-and-print-menus).$path
- Groups: $groups_field on `ir.actions.act_window`, `ir.actions.server` and
  `ir.actions.report` (`groups` in a `<menuitem>`) restricts who sees the action
  in menus and bindings. It is not access control: a user who knows the id can
  still run it, and the model's access rights decide what they see.

The action models of base are `ir.actions.act_window` (open views),
`ir.actions.act_window_close`, `ir.actions.act_url`, `ir.actions.client`,
`ir.actions.report`, `ir.actions.server` and `ir.actions.todo`; `ir.cron` is a server
action with a schedule.$history_model

# Window actions

- `res_model` is required; `view_mode` is a comma-separated list of view types,
  first one opened, default `$default_view_mode`; no duplicates, no spaces.
  $tree_mode
- `domain` (a string, evaluated in the client) restricts the records for good;
  `context` (a string, default `{}`) passes defaults and starts filters:
  `{'default_state': 'draft', 'search_default_my_books': 1}`. A filter the user
  can remove is a `search_default_<filter name>` key, never a `domain`.
- `target`: $targets
- `res_id` opens one record (form first in `view_mode`); `limit` is the page
  size of list views (default `80`); `search_view_id` picks the search view;
  `view_id` picks the first view of the first type.
- `usage` and `filter` are technical: leave them unset.$mobile$embedded$cache
- To pick a specific view per type, add `ir.actions.act_window.view` records
  (`sequence`, `view_mode`, `view_id`, `act_window_id`): they rank before
  `view_id` and the default views.

```xml
<record id="library_book_action" model="ir.actions.act_window">
    <field name="name">Books</field>
    <field name="res_model">library.book</field>
    <field name="view_mode">$list_tag,form</field>
    <field name="search_view_id" ref="library_book_view_search"/>
    <field name="context">{'search_default_available': 1}</field>
</record>

<record id="library_book_action_view_$list_tag" model="ir.actions.act_window.view">
    <field name="sequence">1</field>
    <field name="view_mode">$list_tag</field>
    <field name="view_id" ref="library_book_view_$list_tag"/>
    <field name="act_window_id" ref="library_book_action"/>
</record>
```

# Return actions from Python as dicts or by xml id

- A button `type="object"` method, a wizard and a server action return an action
  dict, or `False`/`None` to stay where the user is (a form reloads the record).
- Start from a data record when one exists:
  `action = self.env['ir.actions.act_window']._for_xml_id('library.library_book_action')`
  returns its dict (the model asserts the record's type; `ir.actions.actions` takes
  any type), then adjust `domain`, `context` or `res_id`. Never `env.ref(...).read()[0]`:
  it returns every field, including ones the client does not expect.
- An inline dict names `type`, `res_model` and `views` (a list of `(view_id, type)`
  pairs, `False` for the default view): `{'type': 'ir.actions.act_window',
  'res_model': 'library.book', 'views': [(False, 'form')], 'res_id': book.id,
  'target': 'new'}`. `view_mode` alone is not read by the client.
- Close a dialog with `{'type': 'ir.actions.act_window_close'}`; its optional
  `infos` key is passed to the caller's `on_close`, and `effect` shows the rainbow
  man (`{'fadeout': 'slow', 'message': ...}`).
- Open a URL with `ir.actions.act_url`: `{'type': 'ir.actions.act_url', 'url':
  '/library/book/1', 'target': 'new'}`; `target` is $url_targets. Prefer a relative
  URL; an external one must be one the user can trust.
- Run a JavaScript client action with `ir.actions.client`: `tag` is the key the
  component is registered under in `registry.category("actions")`, `params` its
  arguments, `target` $client_targets. The built-in `display_notification` tag shows
  a toast: `{'type': 'ir.actions.client', 'tag': 'display_notification', 'params':
  {'message': ..., 'type': 'success', 'sticky': False, 'next': next_action}}`.
- `ir.actions.report` prints: return `self.env.ref('library.action_report_book').report_action(self)`,
  never a hand-made dict.

# Bind actions to the Action and Print menus

- `binding_model_id` (an `ir.model`, `ref="model_library_book"`) adds the action to
  that model's Action menu, or Print menu when `binding_type` is `report` (the
  default on `ir.actions.report`; `action` on the others).
- `binding_view_types` (default `list,form`) limits the views showing it: `form`
  for a single-record action.$report_domain
- A bound window action receives `active_id`, `active_ids` and `active_model` in
  its context; read them from `self.env.context` in the wizard, not from the
  action's `context` field.
- Remove a binding by setting `binding_model_id` to `False` (`eval="False"`),
  not by deleting the action other code may call.

# Server actions

`ir.actions.server` runs on `model_id` (required) and does one thing, its `state`:
$server_states

$code_state
- `object_write` updates the records: $object_write
- `object_create` creates a record of `crud_model_id` named after `value`
  (`name_create`) and can link it back through `link_field_id`.$object_copy
- `multi` runs its children $children in sequence; the last action returned wins.$webhook
- Server actions show in the Action menu through `binding_model_id`; restrict them
  with $groups_field.

Prefer a `type="object"` button calling a model method over a `code` server
action: the method is versioned, tested, overridable and readable in a traceback,
while `code` lives in a database field. Keep `code` to one call:
`records.action_mark_available()`.$history

# Scheduled actions

An `ir.cron` delegates to its own server action (`ir_actions_server_id`): the record
sets the server action fields too.

```xml
<record id="ir_cron_library_book_remind" model="ir.cron">
    <field name="name">Library: send return reminders</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="state">code</field>
    <field name="code">model._cron_send_reminders()</field>
    <field name="interval_number">1</field>
    <field name="interval_type">days</field>$cron_fields
</record>
```

- The code calls one method of the model, `_cron_<what>`, which the cron and the
  tests both call. `model` is the empty recordset of `model_id`, run as `user_id`
  (default the creating user: `base.user_root` for a data file).
- `interval_type` is one of `minutes`, `hours`, `days`, `weeks`, `months` (the
  default); `nextcall` (default now) is the first run; `priority` (default `5`,
  lower first) orders crons due together.$cron_removed
- Make the method work in batches: $cron_progress
- Wake a cron before its next run with `self.env.ref('library.ir_cron_library_book_remind')._trigger()`
  (optionally `at=` a datetime) instead of a second cron or a short interval.$cron_failures
- Declare crons in a `noupdate="1"` file: an administrator changes their interval
  or deactivates them, and an update must not undo that.

# Menus

- Declare menus with `<menuitem>`, after the actions they open (the file order
  is the load order): `id` (required), `name` (default: the action's name),
  `parent` (or nest `<menuitem>` elements), `action`, `sequence` (default `10`,
  lower first), `groups` (comma-separated xml ids, `-` removes one) and `active`.
- Only a root menu takes `web_icon="library,static/description/icon.png"` (the
  module, then the path); a sub-menu ignores it.
- A menu shows only when the user belongs to its `groups` and can read its
  action's model; a menu without action shows only when it has a visible child.
- Structure an app as a root menu, sections without action, and entries that
  hold the actions.
- The groups of a menu ($groups_field on `ir.ui.menu`) hide it; they do not
  protect the model: access rights and record rules do.
- Change another module's menu with `<record id="other.menu_id" model="ir.ui.menu">`
  and only the fields you change, never by redeclaring the `<menuitem>`.

# Configuration wizards

`ir.actions.todo` queues an action (`action_id`, `sequence`, `state` `open` or
`done`) that the setup flow launches once after installation. Use it only for a
wizard that must run before the module is usable, and ship it with `state` `open`;
everything else is a menu entry or a button.
