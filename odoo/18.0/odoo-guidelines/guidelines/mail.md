# Add the chatter with `mail.thread`

A model that needs a discussion thread, followers or tracking inherits
`mail.thread`; one that needs scheduled activities also inherits
`mail.activity.mixin`, which does not bring `mail.thread` with it.

```python
class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
```

- The module depends on `mail`.
- The form view ends with `<chatter/>`, after `</sheet>`.
  `reload_on_post="True"`, `reload_on_follower`
  and `reload_on_attachment`
  reload the form after that event, when a computed field depends on it;
  `open_attachments="True"` opens the attachment box. `div.oe_chatter` is no
  longer rendered.
- `_mail_post_access = 'write'` (the default) lets only users who can write
  the record post on it; set it to `'read'` when readers must be able to
  comment. Reading messages always needs read access on the record.
- `_primary_email = 'email'` names the field that holds the record's own email
  address, used to suggest it as a recipient.
- Other mixins, inherited next to `mail.thread`: `mail.thread.blacklist`
  (records with an email address that mass mailings must respect),
  `mail.thread.cc` (keeps the Cc of incoming emails on the record),
  `mail.thread.main.attachment` (a main attachment, for documents received by
  email) and `mail.tracking.duration.mixin` (time spent in each value of a
  tracked many2one, such as a stage).
- `record.activity_schedule('library.mail_activity_return', user_id=...)`
  creates an activity from its type's external id (`date_deadline`, `summary`
  and `note` are optional); `activity_feedback([...])` marks the matching ones
  done and `activity_unlink([...])` removes them.

# Track field changes with `tracking=`

Declare `tracking=True` (or an integer, the order in the tracking message) on
each field whose changes must appear in the chatter; never write the change
message by hand.

- `tracking` is only accepted on models that inherit `mail.thread`; anywhere else
  it logs an "unknown parameter" warning and does nothing. `track_visibility`
  is not accepted in this version.
- Trackable types: `Char`, `Text`, `Integer`, `Float`, `Monetary`, `Date`,
  `Datetime`, `Boolean`, `Selection`, `Many2one`, `One2many` and
  `Many2many`; any other type raises `NotImplementedError` on its first change.
- To post a business event instead of a plain change log, override
  `_track_subtype(init_values)`: return
  `self.env.ref('library.mt_book_borrowed')` when `'state' in init_values`
  and the new state calls for it, else `super()`. `_track_template(changes)`
  returns `{field_name: (template, post_kwargs)}` to send a template on a change.
- `_creation_subtype()` returns the subtype posted when a record is created
  (default: none, and the creation is written as a plain log line).
- Context keys for imports and batch jobs: `tracking_disable=True` turns off
  tracking, logging and auto-subscription; `mail_notrack=True` only tracking;
  `mail_create_nolog=True` skips the "created" message;
  `mail_create_nosubscribe=True` keeps the creator from following.

# Post messages with `message_post`

Post on a record with `record.message_post(...)`, choosing the subtype from who
must be notified.

```python
book.message_post(
    body=self.env._("Returned by %s", partner.name),
    message_type='comment',
    subtype_xmlid='mail.mt_note',
)
```

- `subtype_xmlid='mail.mt_comment'` notifies the followers;
  `subtype_xmlid='mail.mt_note'` is an internal note that notifies only
  `partner_ids`. `message_type` is `'comment'` for something a person says and
  `'notification'` for a system event.
- A `str` body is escaped, so its tags show as text: pass HTML as
  `markupsafe.Markup` and insert values with `Markup('<p>%s</p>') % value`,
  which escapes the value. `body_is_html=True` exists for RPC clients only.
- Other arguments: `subject`, `partner_ids` (notified even if not followers),
  `author_id` (default: the current user's partner), `attachments` (a list of
  `(file_name, content)`), `attachment_ids` (existing attachments, which are
  moved onto the record) and `parent_id`.
- `message_notify(partner_ids=[...], body=..., subject=...)` reaches those
  partners without posting in the thread; `_message_log(body=...)` writes a
  line in the chatter that notifies nobody and accepts no keyword beyond
  its own (`body`, `subject`, `author_id`, `partner_ids`, `attachment_ids`, ...).
- Several records with the same kind of log:
  `records._message_log_batch(bodies={record.id: body, ...})` writes them in
  one go instead of a `message_post` per record.

# Followers and subtypes

- `record.message_subscribe(partner_ids=[...], subtype_ids=[...])` and
  `message_unsubscribe(partner_ids=[...])`; without `subtype_ids` the follower
  gets the subtypes marked `default`.
- A `mail.message.subtype` record per business event (`mt_book_borrowed`):
  `res_model` set to the model, `default` for "followers get it unless they opt
  out", `internal=True` to hide it from portal followers. Return it from the
  tracking subtype hook so followers can subscribe to that event alone.
- A subtype on a parent model with `parent_id` (the child's subtype) and
  `relation_field` (the child's many2one to the parent) makes followers of a
  shelf follow the same event on its books.
- To propose the record's contact in the composer, override
  `_message_get_suggested_recipients()` (one record; it returns a list of
  dicts) and add it with `self._message_add_suggested_recipient(...)`.

# Send emails with `mail.template`

Emails written for a record come from a `mail.template` data record rendered
for that record; never assemble subject and body by string concatenation.

```xml
<record id="mail_template_book_due" model="mail.template">
    <field name="name">Library: book due</field>
    <field name="model_id" ref="model_library_book"/>
    <field name="subject">{{ object.name }} is due</field>
    <field name="email_from">{{ (object.company_id.email_formatted or user.email_formatted) }}</field>
    <field name="partner_to">{{ object.borrower_id.id }}</field>
    <field name="lang">{{ object.borrower_id.lang }}</field>
    <field name="body_html" type="html">
        <div>Please return <t t-out="object.name"/>.</div>
    </field>
    <field name="auto_delete" eval="True"/>
</record>
```

- Short fields (`subject`, `email_from`, `email_to`, `partner_to`, `lang`) use
  the inline syntax `{{ expression }}`, with an optional fallback text after `|||`
  (`{{ object.borrower_id.name ||| Reader }}`); `body_html` is QWeb
  (`t-out`, `t-if`), with `object` the record and `user` the sender.
- `report_template_ids` (`ir.actions.report` records) attaches their PDFs;
  `email_layout_xmlid` picks the notification layout around the body.
- `template.send_mail(record.id)` queues the email for the mail cron;
  `force_send=True` sends it during the request, which makes the user wait and
  fails the request when the server is down: use it only where the user expects
  the email at once.
  `template.send_mail_batch(records.ids)` renders and queues one email per
  record in one call.
- `record.message_post_with_source(template)` (a record or its external id)
  renders the template and posts it in the chatter;
  `message_post_with_template` no longer exists.
- Put templates in `data/mail_template_data.xml` with `noupdate="1"`: users
  edit them, and an update must not overwrite their edits.

# Receive emails through aliases

A model that creates records from incoming emails overrides `message_new`, and
the model that owns the address inherits `mail.alias.mixin`.

- `message_new(msg_dict, custom_values=None)` creates the record from the email:
  map `msg_dict` (`subject`, `email_from`, `body`, ...) into `custom_values` and
  call `super()`. `message_update(msg_dict, update_vals=None)` handles replies
  on an existing record.
- The owner (a team, a shelf) inherits `mail.alias.mixin` and overrides
  `_alias_get_creation_values()` to set `alias_model_id` (the model records are
  created in) and `alias_defaults` (their default values, such as the owner's
  id). The domain comes from a `mail.alias.domain` record
  (`res.company.alias_domain_id`); never hardcode it.
- Never trust `email_from` for access decisions: anyone can write any sender.
