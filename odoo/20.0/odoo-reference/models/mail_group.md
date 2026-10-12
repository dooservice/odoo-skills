# mail_group — Mail Group

Depends on: mail, portal.

## `mail.group` (defines)

Mail Group

Inherits: `mail.alias.mixin`

- `active` Boolean “Active”
- `name` Char “Name” (required)
- `description` Text “Description”
- `image_128` Image “Image”
- `is_closed` Boolean “Is Closed”
- `mail_group_message_ids` One2many → `mail.group.message` “Pending Messages”
- `mail_group_message_last_month_count` Integer “Messages Per Month” (compute=_compute_mail_group_message_last_month_count)
- `mail_group_message_count` Integer “Messages Count” (compute=_compute_mail_group_message_count)
- `mail_group_message_moderation_count` Integer “Pending Messages Count” (compute=_compute_mail_group_message_moderation_count)
- `is_member` Boolean “Is Member” (compute=_compute_is_member)
- `member_ids` One2many → `mail.group.member` “Members”
- `member_partner_ids` Many2many → `res.partner` “Partners Member” (compute=_compute_member_partner_ids)
- `member_count` Integer “Members Count” (compute=_compute_member_count)
- `is_moderator` Boolean “Moderator” (compute=_compute_is_moderator)
- `moderation` Boolean “Moderate”
- `moderation_rule_count` Integer “Moderated emails count” (compute=_compute_moderation_rule_count)
- `moderation_rule_ids` One2many → `mail.group.moderation` “Moderated Emails”
- `moderator_ids` Many2many → `res.users` “Moderators”
- `moderation_notify` Boolean “Automatic notification”
- `moderation_notify_msg` Html “Notification message”
- `moderation_guidelines` Boolean “Send guidelines to new members”
- `moderation_guidelines_msg` Html “Guidelines”
- `access_mode` Selection “Privacy” (required)
- `access_group_id` Many2one → `res.groups` “Authorized Group”
- `can_manage_group` Boolean “Can Manage” (compute=_compute_can_manage_group)

Public methods: `action_close`, `action_join`, `action_leave`, `action_open`, `action_send_guidelines`, `default_get`, `message_new`, `message_post`, `message_update`

Extension points: `_check_access_mode`, `_check_moderation_guidelines`, `_check_moderation_notify`, `_check_moderator_email`, `_check_moderator_existence`, `_get_email_unsubscribe_url`

## `mail.group.member` (defines)

Mailing List Member

- `email` Char “Email” (store, compute=_compute_email)
- `email_normalized` Char “Normalized Email” (store, index, compute=_compute_email_normalized)
- `mail_group_id` Many2one → `mail.group` “Group” (required, index)
- `partner_id` Many2one → `res.partner`

## `mail.group.message` (defines)

Mailing List Message

- `attachment_ids` Many2many (related=mail_message_id.attachment_ids)
- `author_id` Many2one (related=mail_message_id.author_id)
- `email_from` Char (related=mail_message_id.email_from)
- `email_from_normalized` Char “Normalized From” (store, compute=_compute_email_from_normalized)
- `body` Html (related=mail_message_id.body)
- `subject` Char (related=mail_message_id.subject)
- `mail_group_id` Many2one → `mail.group` “Group” (required, index)
- `mail_message_id` Many2one → `mail.message` (required, index)
- `group_message_parent_id` Many2one → `mail.group.message` “Parent” (store, index)
- `group_message_child_ids` One2many → `mail.group.message` “Children”
- `author_moderation` Selection “Author Moderation Status” (compute=_compute_author_moderation)
- `is_group_moderated` Boolean “Is Group Moderated” (related=mail_group_id.moderation)
- `moderation_status` Selection “Status” (required, index)
- `moderator_id` Many2one → `res.users` “Moderated By”
- `create_date` Datetime “Posted”

Public methods: `action_moderate_accept`, `action_moderate_allow`, `action_moderate_ban`, `action_moderate_ban_with_comment`, `action_moderate_reject`, `action_moderate_reject_with_comment`, `copy_data`, `create`

Extension points: `_create_moderation_rule`, `_get_pending_same_author_same_group`

## `mail.group.moderation` (defines)

Mailing List black/white list

- `email` Char “Email” (required)
- `status` Selection “Status” (required)
- `mail_group_id` Many2one → `mail.group` “Group” (required, index)

Public methods: `create`, `write`

## `mail.group.message.reject` (defines)

Reject Group Message

- `subject` Char “Subject” (store, compute=_compute_subject)
- `body` Html “Contents”
- `email_from_normalized` Char “Email From” (related=mail_group_message_id.email_from_normalized)
- `mail_group_message_id` Many2one → `mail.group.message` “Message” (required, readonly)
- `action` Selection “Action” (required)
- `send_email` Boolean “Send Email” (compute=_compute_send_email)

Public methods: `action_send_mail`
