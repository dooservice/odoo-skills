# website_livechat — Website Live Chat

Depends on: website, im_livechat.

## `chatbot.script` (extends)


Public methods: `action_test_script`

## `chatbot.script.step` (extends)


## `discuss.channel` (extends)

- `livechat_visitor_id` Many2one → `website.visitor` “Visitor”

Public methods: `channel_pin`, `message_post`

Extension points: `_get_visitor_history`, `_get_visitor_history_data`, `_get_visitor_leave_message`

## `im_livechat.channel` (extends)

Inherits: `website.published.mixin`

- `website_description` Html “Website description”

## `im_livechat.channel` (extends)


Extension points: `_get_livechat_discuss_channel_vals`

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `res.config.settings` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Channel” (related=website_id.channel_id)

## `website` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Chat Channel”

Public methods: `get_suggested_controllers`

Extension points: `_get_livechat_channel_info`, `_get_livechat_request_session`

## `website.visitor` (extends)

- `livechat_operator_id` Many2one → `res.partner` “Speaking with” (store, compute=_compute_livechat_operator_id)
- `livechat_operator_name` Char “Operator Name” (related=livechat_operator_id.name)
- `discuss_channel_ids` One2many → `discuss.channel` “Visitor's livechat channels” (readonly)
- `session_count` Integer “# Sessions” (compute=_compute_session_count)

Public methods: `action_send_chat_request`
