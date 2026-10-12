# website_livechat — Website Live Chat

Depends on: website, im_livechat.

## `chatbot.script` (extends)


Public methods: `action_test_script`

## `chatbot.script.step` (extends)


## `discuss.channel` (extends)

- `is_pending_chat_request` Boolean “When created from an operator, whether the channel is yet to be opened on the visitor side.”
- `livechat_visitor_id` Many2one → `website.visitor` “Visitor”

Public methods: `channel_pin`, `message_post`

Extension points: `_get_livechat_session_fields_to_store`, `_get_visitor_history`, `_get_visitor_leave_message`

## `im_livechat.channel` (extends)


Public methods: `create`

Extension points: `_get_livechat_discuss_channel_vals`

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `res.config.settings` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Channel” (related=website_id.channel_id)

## `website` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Chat Channel”

Extension points: `_get_livechat_channel_info`

## `website.page` (extends)


Extension points: `_post_process_response_from_cache`

## `website.visitor` (extends)

- `livechat_operator_id` Many2one → `res.partner` “Speaking with” (store, compute=_compute_livechat_operator_id)
- `livechat_operator_name` Char “Operator Name” (related=livechat_operator_id.name)
- `discuss_channel_ids` One2many → `discuss.channel` “Visitor's livechat channels” (readonly)
- `session_count` Integer “# Sessions” (compute=_compute_session_count)

Public methods: `action_send_chat_request`

Extension points: `_get_visitor_history`
