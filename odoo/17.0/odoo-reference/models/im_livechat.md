# im_livechat — Live Chat

Depends on: mail, rating, digest, utm.

## `chatbot.message` (defines)

Chatbot Message

- `mail_message_id` Many2one → `mail.message` “Related Mail Message” (required)
- `discuss_channel_id` Many2one → `discuss.channel` “Discussion Channel” (required)
- `script_step_id` Many2one → `chatbot.script.step` “Chatbot Step” (required)
- `user_script_answer_id` Many2one → `chatbot.script.answer` “User's answer”
- `user_raw_answer` Html “User's raw answer”

## `chatbot.script` (defines)

Chatbot Script

Inherits: `image.mixin`, `utm.source.mixin`

- `title` Char “Title” (required)
- `active` Boolean
- `image_1920` Image (related=operator_partner_id.image_1920)
- `script_step_ids` One2many → `chatbot.script.step` “Script Steps”
- `operator_partner_id` Many2one → `res.partner` “Bot Operator” (required)
- `livechat_channel_count` Integer “Livechat Channel Count” (compute=_compute_livechat_channel_count)
- `first_step_warning` Selection (compute=_compute_first_step_warning)

Public methods: `action_view_livechat_channels`, `copy`, `create`, `write`

Extension points: `_get_welcome_steps`, `_post_welcome_steps`

## `chatbot.script.answer` (defines)

Chatbot Script Answer

- `name` Char “Answer” (required)
- `sequence` Integer “Sequence”
- `redirect_link` Char “Redirect Link”
- `script_step_id` Many2one → `chatbot.script.step` “Script Step” (required)
- `chatbot_script_id` Many2one (related=script_step_id.chatbot_script_id)

## `chatbot.script.step` (defines)

Chatbot Script Step

- `message` Text “Message”
- `sequence` Integer “Sequence”
- `chatbot_script_id` Many2one → `chatbot.script` “Chatbot” (required)
- `step_type` Selection (required)
- `answer_ids` One2many → `chatbot.script.answer` “Answers”
- `triggering_answer_ids` Many2many → `chatbot.script.answer` “Only If” (store, compute=_compute_triggering_answer_ids)
- `is_forward_operator_child` Boolean (compute=_compute_is_forward_operator_child)

Public methods: `create`

Extension points: `_get_parent_step`

## `digest.digest` (extends)

- `kpi_livechat_rating` Boolean “% of Happiness”
- `kpi_livechat_rating_value` Float (compute=_compute_kpi_livechat_rating_value)
- `kpi_livechat_conversations` Boolean “Conversations handled”
- `kpi_livechat_conversations_value` Integer (compute=_compute_kpi_livechat_conversations_value)
- `kpi_livechat_response` Boolean “Time to answer (sec)”
- `kpi_livechat_response_value` Float (compute=_compute_kpi_livechat_response_value)

## `discuss.channel` (extends)

Inherits: `rating.mixin`

- `anonymous_name` Char “Anonymous Name”
- `channel_type` Selection
- `duration` Float “Duration” (compute=_compute_duration)
- `livechat_active` Boolean “Is livechat ongoing?”
- `livechat_channel_id` Many2one → `im_livechat.channel`
- `livechat_operator_id` Many2one → `res.partner` “Operator”
- `chatbot_current_step_id` Many2one → `chatbot.script.step` “Chatbot Current Step”
- `chatbot_message_ids` One2many → `chatbot.message` “Chatbot Messages”
- `country_id` Many2one → `res.country` “Country”

Public methods: `execute_command_history`

Extension points: `_get_channel_history`, `_get_visitor_leave_message`

## `discuss.channel.member` (extends)


Extension points: `_get_partner_data`

## `im_livechat.channel` (defines)

Livechat Channel

Inherits: `rating.parent.mixin`

- `name` Char “Channel Name” (required)
- `button_text` Char “Text of the Button”
- `default_message` Char “Welcome Message”
- `input_placeholder` Char “Chat Input Placeholder”
- `header_background_color` Char
- `title_color` Char
- `button_background_color` Char
- `button_text_color` Char
- `web_page` Char “Web Page” (readonly, compute=_compute_web_page_link)
- `are_you_inside` Boolean “Are you inside the matrix?” (readonly, compute=_are_you_inside)
- `available_operator_ids` Many2many → `res.users` (compute=_compute_available_operator_ids)
- `script_external` Html “Script (external)” (readonly, compute=_compute_script_external)
- `nbr_channel` Integer “Number of conversation” (readonly, compute=_compute_nbr_channel)
- `image_128` Image “Image”
- `user_ids` Many2many → `res.users` “Operators”
- `channel_ids` One2many → `discuss.channel`
- `chatbot_script_count` Integer “Number of Chatbot” (compute=_compute_chatbot_script_count)
- `rule_ids` One2many → `im_livechat.channel.rule`

Public methods: `action_join`, `action_quit`, `action_view_chatbot_scripts`, `action_view_rating`, `get_livechat_info`

Extension points: `_get_channel_infos`, `_get_less_active_operator`, `_get_livechat_discuss_channel_vals`, `_get_operator`

## `im_livechat.channel.rule` (defines)

Livechat Channel Rules

- `regex_url` Char “URL Regex”
- `action` Selection “Live Chat Button” (required)
- `auto_popup_timer` Integer “Open automatically timer”
- `chatbot_script_id` Many2one → `chatbot.script` “Chatbot”
- `chatbot_only_if_no_operator` Boolean “Enabled only if no operator”
- `channel_id` Many2one → `im_livechat.channel`
- `country_ids` Many2many → `res.country`
- `sequence` Integer “Matching order”

Public methods: `match_rule`

## `ir.qweb` (extends)


Extension points: `_get_bundles_to_pregenarate`

## `mail.message` (extends)

- `parent_author_name` Char (compute=_compute_parent_author_name)
- `parent_body` Html (compute=_compute_parent_body)

## `rating.rating` (extends)


Public methods: `action_open_rated_object`

## `res.partner` (extends)

- `user_livechat_username` Char (compute=_compute_user_livechat_username)

Public methods: `search_for_channel_invite`

## `res.users` (extends)

- `livechat_username` Char “Livechat Username” (compute=_compute_livechat_username)
- `livechat_lang_ids` Many2many → `res.lang` “Livechat Languages” (compute=_compute_livechat_lang_ids)
- `has_access_livechat` Boolean “Has access to Livechat” (readonly, compute=_compute_has_access_livechat)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`

## `res.users.settings` (extends)

- `livechat_username` Char “Livechat Username”
- `livechat_lang_ids` Many2many → `res.lang` “Livechat languages”
- `is_discuss_sidebar_category_livechat_open` Boolean “Is category livechat open”

## `im_livechat.report.channel` (defines)

Livechat Support Channel Report

- `uuid` Char “UUID” (readonly)
- `channel_id` Many2one → `discuss.channel` (readonly)
- `channel_name` Char “Channel Name” (readonly)
- `technical_name` Char “Code” (readonly)
- `livechat_channel_id` Many2one → `im_livechat.channel` (readonly)
- `start_date` Datetime “Start Date of session” (readonly)
- `start_hour` Char “Start Hour of session” (readonly)
- `day_number` Char “Day Number” (readonly)
- `time_to_answer` Float “Time to answer (sec)” (readonly)
- `start_date_hour` Char “Hour of start Date of session” (readonly)
- `duration` Float “Average duration” (readonly)
- `nbr_speaker` Integer “# of speakers” (readonly)
- `nbr_message` Integer “Average message” (readonly)
- `is_without_answer` Integer “Session(s) without answer” (readonly)
- `days_of_activity` Integer “Days of activity” (readonly)
- `is_anonymous` Integer “Is visitor anonymous” (readonly)
- `country_id` Many2one → `res.country` (readonly)
- `is_happy` Integer “Visitor is Happy” (readonly)
- `rating` Integer “Rating” (readonly)
- `rating_text` Char “Satisfaction Rate” (readonly)
- `is_unrated` Integer “Session not rated” (readonly)
- `partner_id` Many2one → `res.partner` (readonly)

Public methods: `init`

## `im_livechat.report.operator` (defines)

Livechat Support Operator Report

- `partner_id` Many2one → `res.partner` (readonly)
- `livechat_channel_id` Many2one → `im_livechat.channel` (readonly)
- `nbr_channel` Integer “# of Sessions” (readonly)
- `channel_id` Many2one → `discuss.channel` (readonly)
- `start_date` Datetime “Start Date of session” (readonly)
- `time_to_answer` Float “Time to answer” (readonly)
- `duration` Float “Average duration” (readonly)
- `rating` Float “Average rating” (readonly)

Public methods: `init`
