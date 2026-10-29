# Action records

Every action is a record of a model that extends `ir.actions.actions`, which holds
what all of them share:

- `name`: the title shown in the breadcrumb and the Action menu; a real display
  name, translated.
- `type`: the action model's name, set by the model itself; write it only in a dict
  returned from Python.
- `help`: HTML shown when the view is empty (`<p class="o_view_nocontent_smiling_face">`).
- `binding_model_id`, `binding_type`, `binding_view_types`: see
  [Bind actions to the Action and Print menus](#bind-actions-to-the-action-and-print-menus).
- `path`: the readable URL segment (`/odoo/<path>`), unique across all
  actions, lowercase letters, digits, `_` and `-`, starting with a letter; not
  `new` nor starting with `m-` or `action-`. Set it on the actions of menus.
- Groups: `groups_id` on `ir.actions.act_window`, `ir.actions.server` and
  `ir.actions.report` (`groups` in a `<menuitem>`) restricts who sees the action
  in menus and bindings. It is not access control: a user who knows the id can
  still run it, and the model's access rights decide what they see.

The action models of base are `ir.actions.act_window` (open views),
`ir.actions.act_window_close`, `ir.actions.act_url`, `ir.actions.client`,
`ir.actions.report`, `ir.actions.server` and `ir.actions.todo`; `ir.cron` is a server
action with a schedule.

# Window actions

- `res_model` is required; `view_mode` is a comma-separated list of view types,
  first one opened, default `list,form`; no duplicates, no spaces.
  The list view type is `list`; `tree` is not a view type any more and
  breaks the action in the client.
- `domain` (a string, evaluated in the client) restricts the records for good;
  `context` (a string, default `{}`) passes defaults and starts filters:
  `{'default_state': 'draft', 'search_default_my_books': 1}`. A filter the user
  can remove is a `search_default_<filter name>` key, never a `domain`.
- `target`: `current` (default, in the main area), `new` (a dialog), `fullscreen`,
  `main` (replaces the breadcrumb) or `inline` (legacy settings form).
- `res_id` opens one record (form first in `view_mode`); `limit` is the page
  size of list views (default `80`); `search_view_id` picks the search view;
  `view_id` picks the first view of the first type.
- `usage` and `filter` are technical: leave them unset.
- `mobile_view_mode` (default `kanban`) is the multi-record view opened
  first on a phone when `view_mode` has it.
- Embedded actions (`ir.embedded.actions`, shown as `embedded_action_ids`)
  are the tabs above a view that open a related action (`parent_action_id`,
  `action_id` or `python_method`, `parent_res_model`, `domain`, `context`).
- To pick a specific view per type, add `ir.actions.act_window.view` records
  (`sequence`, `view_mode`, `view_id`, `act_window_id`): they rank before
  `view_id` and the default views.

```xml
<record id="library_book_action" model="ir.actions.act_window">
    <field name="name">Books</field>
    <field name="res_model">library.book</field>
    <field name="view_mode">list,form</field>
    <field name="search_view_id" ref="library_book_view_search"/>
    <field name="context">{'search_default_available': 1}</field>
</record>

<record id="library_book_action_view_list" model="ir.actions.act_window.view">
    <field name="sequence">1</field>
    <field name="view_mode">list</field>
    <field name="view_id" ref="library_book_view_list"/>
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
  '/library/book/1', 'target': 'new'}`; `target` is `new` (default, a new tab), `self`, or `download`. Prefer a relative
  URL; an external one must be one the user can trust.
- Run a JavaScript client action with `ir.actions.client`: `tag` is the key the
  component is registered under in `registry.category("actions")`, `params` its
  arguments, `target` `current`, `new`, `fullscreen` or `main`. The built-in `display_notification` tag shows
  a toast: `{'type': 'ir.actions.client', 'tag': 'display_notification', 'params':
  {'message': ..., 'type': 'success', 'sticky': False, 'next': next_action}}`.
- `ir.actions.report` prints: return `self.env.ref('library.action_report_book').report_action(self)`,
  never a hand-made dict.

# Bind actions to the Action and Print menus

- `binding_model_id` (an `ir.model`, `ref="model_library_book"`) adds the action to
  that model's Action menu, or Print menu when `binding_type` is `report` (the
  default on `ir.actions.report`; `action` on the others).
- `binding_view_types` (default `list,form`) limits the views showing it: `form`
  for a single-record action.
- On `ir.actions.report`, `domain` shows the Print entry only on records
  matching it.
- A bound window action receives `active_id`, `active_ids` and `active_model` in
  its context; read them from `self.env.context` in the wizard, not from the
  action's `context` field.
- Remove a binding by setting `binding_model_id` to `False` (`eval="False"`),
  not by deleting the action other code may call.

# Server actions

`ir.actions.server` runs on `model_id` (required) and does one thing, its `state`:
`object_write` (the default), `object_create`, `code`, `webhook` or `multi`;
`mail` adds `next_activity`, `mail_post`, `followers` and `remove_followers`,
`sms` adds `sms`.

- `code` runs Python (`code`, editable by `base.group_system` only) with
  `env`, `model` (empty recordset of `model_id`), `record` and `records` (from
  `active_id`/`active_ids`), `log(message, level)`, `_logger`, `UserError`,
  `Command`, `time`, `datetime`, `dateutil`, `timezone` (pytz), `float_compare`,
  `b64encode`, `b64decode`, `uid` and `user`. Assign `action = {...}` to return
  an action. No `import`: `safe_eval` refuses it.
- `object_write` updates the records: `update_path` names the field (`partner_id.name` follows relations),
  `value` with `evaluation_type` `value` or `equation` (a Python expression),
  `update_m2m_operation` (`add`, `remove`, `set`, `clear`) for many2many, and
  `update_boolean_value` for booleans. One field per action: chain several
  with `multi`.
- `object_create` creates a record of `crud_model_id` named after `value`
  (`name_create`) and can link it back through `link_field_id`.
- `multi` runs its children (`child_ids`, a many2many) in sequence; the last action returned wins.
- `webhook` POSTs `_model`, `_id` and the `webhook_field_ids` of the active
  record as JSON to `webhook_url`.
- Server actions show in the Action menu through `binding_model_id`; restrict them
  with `groups_id`.

Prefer a `type="object"` button calling a model method over a `code` server
action: the method is versioned, tested, overridable and readable in a traceback,
while `code` lives in a database field. Keep `code` to one call:
`records.action_mark_available()`.

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
    <field name="interval_type">days</field>
</record>
```

- The code calls one method of the model, `_cron_<what>`, which the cron and the
  tests both call. `model` is the empty recordset of `model_id`, run as `user_id`
  (default the creating user: `base.user_root` for a data file).
- `interval_type` is one of `minutes`, `hours`, `days`, `weeks`, `months` (the
  default); `nextcall` (default now) is the first run; `priority` (default `5`,
  lower first) orders crons due together.
- A cron runs until deactivated; it has no `numbercall` or `doall`.
- Make the method work in batches: process a limited batch, report it with
  `self.env['ir.cron']._notify_progress(done=..., remaining=...)`: the cron
  reruns itself while `remaining` is not zero and a run that reports progress
  does not count as a failure.
- Wake a cron before its next run with `self.env.ref('library.ir_cron_library_book_remind')._trigger()`
  (optionally `at=` a datetime) instead of a second cron or a short interval.
- A failing run rolls back; after 5 consecutive failures spanning at least
  7 days the cron deactivates itself (`failure_count`, `first_failure_date`).
  Log and skip a bad record rather than raise on it.
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
- The groups of a menu (`groups_id` on `ir.ui.menu`) hide it; they do not
  protect the model: access rights and record rules do.
- Change another module's menu with `<record id="other.menu_id" model="ir.ui.menu">`
  and only the fields you change, never by redeclaring the `<menuitem>`.

# Configuration wizards

`ir.actions.todo` queues an action (`action_id`, `sequence`, `state` `open` or
`done`) that the setup flow launches once after installation. Use it only for a
wizard that must run before the module is usable, and ship it with `state` `open`;
everything else is a menu entry or a button.
