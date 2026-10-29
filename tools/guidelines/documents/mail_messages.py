"""The messages, templates and aliases of `mail.md`, whose methods changed in 17.0 and 19.0."""

from __future__ import annotations

from ..version import OdooVersion


class MailMessages:
    """Body escaping, logging calls, recipients, template fields and alias domains per version."""

    def values(self, version: OdooVersion) -> dict[str, str]:
        return {
            "markup_example": f'{version.translate}("Returned by %s", partner.name)',
            "body_escaping": version.pick(
                v16="`body` is HTML: a `str` is sanitized, not escaped. Escape user-provided\n"
                "  values with `markupsafe.escape` before inserting them in HTML.",
                v17_="A `str` body is escaped, so its tags show as text: pass HTML as\n"
                "  `markupsafe.Markup` and insert values with `Markup('<p>%s</p>') % value`,\n"
                "  which escapes the value. `body_is_html=True` exists for RPC clients only.",
            ),
            "notify_and_log": version.pick(
                v16="`message_notify(partner_ids=[...], body=..., subject=...)` reaches those\n"
                "  partners without posting in the thread; `_message_log(body=...)` writes a\n"
                "  line in the chatter that notifies nobody.",
                v17_19="`message_notify(partner_ids=[...], body=..., subject=...)` reaches those\n"
                "  partners without posting in the thread; `_message_log(body=...)` writes a\n"
                "  line in the chatter that notifies nobody and accepts no keyword beyond\n"
                "  its own (`body`, `subject`, `author_id`, `partner_ids`, `attachment_ids`, ...).",
                v20="`message_notify(partner_ids=[...], body=..., subject=...)` reaches those\n"
                "  partners without posting in the thread; `_message_log(body=...)` writes a\n"
                "  line in the chatter that notifies nobody.",
            ),
            "suggested_recipients": version.pick(
                v16_17="To propose the record's contact in the composer, override\n"
                "  `_message_get_suggested_recipients()` and add it with\n"
                "  `record._message_add_suggested_recipient(result, partner=..., reason=...)`.",
                v18="To propose the record's contact in the composer, override\n"
                "  `_message_get_suggested_recipients()` (one record; it returns a list of\n"
                "  dicts) and add it with `self._message_add_suggested_recipient(...)`.",
                v19_="To propose the record's contact in the composer, override\n"
                "  `_message_add_suggested_recipients()`: call `super()` and add partners to\n"
                "  `result[record.id]['partners']`. Do not override\n"
                "  `_message_get_suggested_recipients`, which only wraps it.",
            ),
            "inline_default": version.pick(
                v16_17="",
                v18_=", with an optional fallback text after `|||`\n"
                "  (`{{ object.borrower_id.name ||| Reader }}`)",
            ),
            "report_field": version.pick(
                v16="`report_template` (one `ir.actions.report`) attaches its PDF, named by\n"
                "  `report_name`.",
                v17_="`report_template_ids` (`ir.actions.report` records) attaches their PDFs;\n"
                "  `email_layout_xmlid` picks the notification layout around the body.",
            ),
            "send_batch": version.pick(
                v16="",
                v17_="\n  `template.send_mail_batch(records.ids)` renders and queues one email per\n"
                "  record in one call.",
            ),
            "post_with_template": version.pick(
                v16="`record.message_post_with_template(template.id)` renders the template and\n"
                "  posts it in the chatter, notifying the recipients.",
                v17_="`record.message_post_with_source(template)` (a record or its external id)\n"
                "  renders the template and posts it in the chatter;\n"
                "  `message_post_with_template` no longer exists.",
            ),
            "alias_domain": version.pick(
                v16=" The domain of every alias is the system parameter\n"
                "  `mail.catchall.domain`.",
                v17_=" The domain comes from a `mail.alias.domain` record\n"
                "  (`res.company.alias_domain_id`); never hardcode it.",
            ),
        }
