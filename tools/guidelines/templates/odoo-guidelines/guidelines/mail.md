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
$chatter
- `_mail_post_access = 'write'` (the default) lets only users who can write
  the record post on it; set it to `'read'` when readers must be able to
  comment. Reading messages always needs read access on the record.
- `_primary_email = 'email'` names the field that holds the record's own email
  address, used to suggest it as a recipient.$customer_attribute
- Other mixins, inherited next to `mail.thread`: `mail.thread.blacklist`
  (records with an email address that mass mailings must respect)$extra_mixins.
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
- $tracked_types
- $track_subtype
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
    body=$markup_example,
    message_type='comment',
    subtype_xmlid='mail.mt_note',
)
```

- `subtype_xmlid='mail.mt_comment'` notifies the followers;
  `subtype_xmlid='mail.mt_note'` is an internal note that notifies only
  `partner_ids`. `message_type` is `'comment'` for something a person says and
  `'notification'` for a system event.
- $body_escaping
- Other arguments: `subject`, `partner_ids` (notified even if not followers),
  `author_id` (default: the current user's partner), `attachments` (a list of
  `(file_name, content)`), `attachment_ids` (existing attachments, which are
  moved onto the record) and `parent_id`.
- $notify_and_log
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
- $suggested_recipients

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
  the inline syntax `{{ expression }}`$inline_default; `body_html` is QWeb
  (`t-out`, `t-if`), with `object` the record and `user` the sender.
- $report_field
- `template.send_mail(record.id)` queues the email for the mail cron;
  `force_send=True` sends it during the request, which makes the user wait and
  fails the request when the server is down: use it only where the user expects
  the email at once.$send_batch
- $post_with_template
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
  id).$alias_domain
- Never trust `email_from` for access decisions: anyone can write any sender.
