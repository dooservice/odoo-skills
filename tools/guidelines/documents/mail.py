"""`odoo-guidelines/guidelines/mail.md`: chatter, tracking, messages, followers, templates and aliases."""

from __future__ import annotations

from ..document import Document
from ..version import OdooVersion
from .mail_messages import MailMessages


class Mail(Document):
    path = "odoo-guidelines/guidelines/mail.md"

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            **super().values(version),
            **MailMessages().values(version),
            "chatter": version.pick(
                v16_17="""\
- The form view ends with the chatter, after `</sheet>`:
  `<div class="oe_chatter"><field name="message_follower_ids"/><field name="activity_ids"/><field name="message_ids"/></div>`
  (without `activity_ids` when the model has no activities). `<chatter/>` does
  not exist in this version.""",
                v18_=f"""\
- The form view ends with `<chatter/>`, after `</sheet>`.
  {self.chatter_options(version)}
  reload the form after that event, when a computed field depends on it;
  `open_attachments="True"` opens the attachment box. `div.oe_chatter` is no
  longer rendered.""",
            ),
            "customer_attribute": version.pick(
                v16_18="",
                v19_="\n- `_mail_thread_customer = True` makes the customer a follower once a message\n"
                "  is sent to them.",
            ),
            "extra_mixins": version.pick(
                v16=",\n  `mail.thread.cc` (keeps the Cc of incoming emails on the record)",
                v17_19=",\n  `mail.thread.cc` (keeps the Cc of incoming emails on the record),\n"
                "  `mail.thread.main.attachment` (a main attachment, for documents received by\n"
                "  email) and `mail.tracking.duration.mixin` (time spent in each value of a\n"
                "  tracked many2one, such as a stage)",
                v20=",\n  `mail.thread.main.attachment` (a main attachment, for documents\n"
                "  received by email) and `mail.tracking.duration.mixin` (time spent in each\n"
                "  value of a tracked many2one, such as a stage). `mail.thread.cc` no longer\n"
                "  exists: Cc handling is part of `mail.thread`",
            ),
            "tracked_types": version.pick(
                v16="Trackable types: `Char`, `Text`, `Integer`, `Float`, `Monetary`, `Date`,\n"
                "  `Datetime`, `Boolean`, `Selection` and `Many2one`. `tracking` on a\n"
                "  `One2many` or `Many2many` is silently ignored.",
                v17_18="Trackable types: `Char`, `Text`, `Integer`, `Float`, `Monetary`, `Date`,\n"
                "  `Datetime`, `Boolean`, `Selection`, `Many2one`, `One2many` and\n"
                "  `Many2many`; any other type raises `NotImplementedError` on its first change.",
                v19_="Trackable types: `Char`, `Text`, `Integer`, `Float`, `Monetary`, `Date`,\n"
                "  `Datetime`, `Boolean`, `Selection`, `Many2one`, `One2many`, `Many2many` and\n"
                "  properties; any other type raises `NotImplementedError` on its first change.",
            ),
            "track_subtype": version.pick(
                v16_19="To post a business event instead of a plain change log, override\n"
                "  `_track_subtype(init_values)`: return\n"
                "  `self.env.ref('library.mt_book_borrowed')` when `'state' in init_values`\n"
                "  and the new state calls for it, else `super()`. `_track_template(changes)`\n"
                "  returns `{field_name: (template, post_kwargs)}` to send a template on a change.",
                v20="To post a business event instead of a plain change log, override\n"
                "  `_track_log_get_default_subtype(track_init_values)`: return\n"
                "  `self.env.ref('library.mt_book_borrowed')` when `'state' in track_init_values`\n"
                "  and the new state calls for it, else `super()`.\n"
                "  `_track_template_parameters(tracked_fields)` returns\n"
                "  `{field_name: (template, post_kwargs)}` to send a template on a change.\n"
                "  `_track_subtype` and `_track_template` no longer exist: overrides of them\n"
                "  are silently never called.",
            ),
        }

    @staticmethod
    def chatter_options(version: OdooVersion) -> str:
        return version.pick(
            v16_17="",
            v18="`reload_on_post=\"True\"`, `reload_on_follower`\n  and `reload_on_attachment`",
            v19_="`reload_on_post=\"True\"`, `reload_on_follower`,\n"
            "  `reload_on_attachment` and `reload_on_activity`",
        )
