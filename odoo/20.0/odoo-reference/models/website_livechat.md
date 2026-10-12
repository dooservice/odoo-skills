# website_livechat — Website Live Chat

Depends on: website, im_livechat.

## `chatbot.script` (extends)


Public methods: `action_test_script`

## `chatbot.script.step` (extends)


## `discuss.channel` (extends)

- `is_pending_chat_request` Boolean “When created from an operator, whether the channel is yet to be opened on the visitor side.”
- `livechat_visitor_id` Many2one → `website.visitor` “Visitor”

Public methods: `message_post`

Extension points: `_get_visitor_leave_message`

## `discuss.channel.member` (extends)


## `im_livechat.channel` (extends)


Public methods: `create`

Extension points: `_get_livechat_discuss_channel_vals`

## `ir.http` (extends)


Extension points: `_get_translation_frontend_modules_name`

## `res.config.settings` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Channel” (related=website_id.channel_id)

## `website` (extends)

- `channel_id` Many2one → `im_livechat.channel` “Website Live Chat Channel”

Extension points: `_get_livechat_channel_info`, `_get_settings_to_copy_onto_new_default_website`

## `website.page` (extends)


Extension points: `_post_process_response_from_cache`

## `website.visitor` (extends)

- `current_livechat_agent_ids` Many2many → `res.partner` “Speaking with” (compute=_compute_current_livechat_agent_ids)
- `discuss_channel_ids` One2many → `discuss.channel` “Visitor's livechat channels” (readonly)
- `session_count` Integer “# Sessions” (compute=_compute_session_count)

Public methods: `action_send_chat_request`
