# im_livechat — Live Chat

Depends on: mail, rating, digest, utm.

## `chatbot.message` (defines)

Chatbot Message

- `mail_message_id` Many2one → `mail.message` “Related Mail Message”
- `discuss_channel_id` Many2one → `discuss.channel` “Discussion Channel” (required, index)
- `script_step_id` Many2one → `chatbot.script.step` “Chatbot Step”
- `user_script_answer_id` Many2one → `chatbot.script.answer` “User's answer”
- `user_raw_script_answer_id` Integer
- `user_raw_answer` Html “User's raw answer”

## `chatbot.script` (defines)

Chatbot Script

Inherits: `image.mixin`, `utm.source.mixin`

- `title` Char “Title” (required)
- `active` Boolean
- `image_1920` Image (related=operator_partner_id.image_1920)
- `script_step_ids` One2many → `chatbot.script.step` “Script Steps”
- `operator_partner_id` Many2one → `res.partner` “Bot Operator” (required, index)
- `livechat_channel_count` Integer “Livechat Channel Count” (compute=_compute_livechat_channel_count)
- `first_step_warning` Selection (compute=_compute_first_step_warning)

Public methods: `action_view_livechat_channels`, `copy`, `copy_data`, `create`, `write`

Extension points: `_check_question_selection`, `_get_chatbot_language`, `_get_welcome_steps`, `_post_welcome_steps`

## `chatbot.script.answer` (defines)

Chatbot Script Answer

- `name` Char “Answer” (required)
- `sequence` Integer “Sequence”
- `redirect_link` Char “Redirect Link”
- `script_step_id` Many2one → `chatbot.script.step` “Script Step” (required, index)
- `chatbot_script_id` Many2one (related=script_step_id.chatbot_script_id)

## `chatbot.script.step` (defines)

Chatbot Script Step

- `name` Char “Name” (compute=_compute_name)
- `message` Html “Message”
- `sequence` Integer “Sequence”
- `chatbot_script_id` Many2one → `chatbot.script` “Chatbot” (required, index)
- `step_type` Selection (required)
- `answer_ids` One2many → `chatbot.script.answer` “Answers”
- `triggering_answer_ids` Many2many → `chatbot.script.answer` “Only If” (store, compute=_compute_triggering_answer_ids)
- `is_forward_operator` Boolean (compute=_compute_is_forward_operator)
- `is_forward_operator_child` Boolean (compute=_compute_is_forward_operator_child)
- `operator_expertise_ids` Many2many → `im_livechat.expertise` “Operator Expertise”

Public methods: `create`

Extension points: `_get_parent_step`

## `digest.digest` (extends)

- `kpi_livechat_rating` Boolean “% of Happiness”
- `kpi_livechat_rating_value` Float (compute=_compute_kpi_livechat_rating_value)
- `kpi_livechat_conversations` Boolean “Conversations handled”
- `kpi_livechat_conversations_value` Integer (compute=_compute_kpi_livechat_conversations_value)
- `kpi_livechat_response` Boolean “Time to answer (sec)”
- `kpi_livechat_response_value` Float (compute=_compute_kpi_livechat_response_value)

## `discuss.call.history` (extends)

- `livechat_participant_history_ids` Many2many → `im_livechat.channel.member.history`

## `discuss.channel` (extends)

Inherits: `rating.mixin`

- `channel_type` Selection
- `duration` Float “Duration” (compute=_compute_duration)
- `livechat_lang_id` Many2one → `res.lang` “Language”
- `livechat_end_dt` Datetime “Session end date”
- `livechat_channel_id` Many2one → `im_livechat.channel`
- `livechat_operator_id` Many2one → `res.partner` “Operator”
- `livechat_channel_member_history_ids` One2many → `im_livechat.channel.member.history`
- `livechat_expertise_ids` Many2many → `im_livechat.expertise` (store)
- `livechat_agent_history_ids` One2many → `im_livechat.channel.member.history` “Agents (History)” (compute=_compute_livechat_agent_history_ids)
- `livechat_bot_history_ids` One2many → `im_livechat.channel.member.history` “Bots (History)” (compute=_compute_livechat_bot_history_ids)
- `livechat_customer_history_ids` One2many → `im_livechat.channel.member.history` “Customers (History)” (compute=_compute_livechat_customer_history_ids)
- `livechat_agent_partner_ids` Many2many → `res.partner` “Agents” (store, compute=_compute_livechat_agent_partner_ids)
- `livechat_bot_partner_ids` Many2many → `res.partner` “Bots” (store, compute=_compute_livechat_bot_partner_ids)
- `livechat_customer_partner_ids` Many2many → `res.partner` “Customers (Partners)” (store, compute=_compute_livechat_customer_partner_ids)
- `livechat_customer_guest_ids` Many2many → `mail.guest` “Customers (Guests)” (compute=_compute_livechat_customer_guest_ids)
- `livechat_agent_requesting_help_history` Many2one → `im_livechat.channel.member.history` “Help Requested (Agent)” (store, compute=_compute_livechat_agent_requesting_help_history)
- `livechat_agent_providing_help_history` Many2one → `im_livechat.channel.member.history` “Help Provided (Agent)” (store, compute=_compute_livechat_agent_providing_help_history)
- `livechat_note` Html “Live Chat Note”
- `livechat_status` Selection (store, compute=_compute_livechat_status)
- `livechat_outcome` Selection (store, compute=_compute_livechat_outcome)
- `livechat_conversation_tag_ids` Many2many → `im_livechat.conversation.tag` “Live Chat Conversation Tags”
- `livechat_start_hour` Float “Session Start Hour” (store, compute=_compute_livechat_start_hour)
- `livechat_week_day` Selection “Day of the Week” (store, compute=_compute_livechat_week_day)
- `livechat_matches_self_lang` Boolean (compute=_compute_livechat_matches_self_lang)
- `livechat_matches_self_expertise` Boolean (compute=_compute_livechat_matches_self_expertise)
- `chatbot_current_step_id` Many2one → `chatbot.script.step` “Chatbot Current Step”
- `chatbot_message_ids` One2many → `chatbot.message` “Chatbot Messages”
- `country_id` Many2one → `res.country` “Country”
- `livechat_failure` Selection “Live Chat Session Failure”
- `livechat_is_escalated` Boolean “Is session escalated” (store, compute=_compute_livechat_is_escalated)
- `rating_last_text` Selection (store)

Public methods: `execute_command_history`, `livechat_join_channel_needing_help`, `write`

Extension points: `_action_unfollow`, `_get_allowed_channel_member_create_params`, `_get_channel_history`, `_get_human_operator`, `_get_livechat_session_fields_to_store`, `_get_visitor_leave_message`, `_post_current_chatbot_step_message`

## `discuss.channel.member` (extends)

- `livechat_member_history_ids` One2many → `im_livechat.channel.member.history`
- `livechat_member_type` Selection (compute=_compute_livechat_member_type)
- `chatbot_script_id` Many2one → `chatbot.script` (compute=_compute_chatbot_script_id)
- `agent_expertise_ids` Many2many → `im_livechat.expertise` (compute=_compute_agent_expertise_ids)

Public methods: `create`

Extension points: `_create_or_update_history`, `_get_excluded_rtc_members_partner_ids`, `_get_html_link_title`, `_get_rtc_invite_members_domain`, `_get_store_guest_fields`, `_get_store_partner_fields`

## `discuss.channel.rtc.session` (extends)


Public methods: `create`

## `im_livechat.channel` (defines)

Livechat Channel

Inherits: `rating.parent.mixin`

- `name` Char “Channel Name” (required)
- `button_text` Char “Text of the Button”
- `default_message` Char “Welcome Message”
- `header_background_color` Char
- `title_color` Char
- `button_background_color` Char
- `button_text_color` Char
- `max_sessions_mode` Selection “Sessions per Operator”
- `max_sessions` Integer “Maximum Sessions”
- `block_assignment_during_call` Boolean “No Chats During Call”
- `review_link` Char “Review Link”
- `web_page` Char “Web Page” (readonly, compute=_compute_web_page_link)
- `are_you_inside` Boolean “Are you inside the matrix?” (readonly, compute=_are_you_inside)
- `available_operator_ids` Many2many → `res.users` (compute=_compute_available_operator_ids)
- `script_external` Html “Script (external)” (readonly, compute=_compute_script_external)
- `nbr_channel` Integer “Number of conversation” (readonly, compute=_compute_nbr_channel)
- `user_ids` Many2many → `res.users` “Agents”
- `channel_ids` One2many → `discuss.channel`
- `chatbot_script_count` Integer “Number of Chatbot” (compute=_compute_chatbot_script_count)
- `rule_ids` One2many → `im_livechat.channel.rule`
- `ongoing_session_count` Integer “Number of Ongoing Sessions” (compute=_compute_ongoing_sessions_count)
- `remaining_session_capacity` Integer “Remaining Session Capacity” (compute=_compute_remaining_session_capacity)

Public methods: `action_join`, `action_quit`, `action_view_chatbot_scripts`, `action_view_rating`, `get_livechat_info`, `web_read`

Extension points: `_check_review_link`, `_get_agent_member_vals`, `_get_available_operators_by_livechat_channel`, `_get_channel_infos`, `_get_channel_name`, `_get_less_active_operator`, `_get_livechat_discuss_channel_vals`, `_get_ongoing_session_count_by_agent_livechat_channel`, `_get_operator`, `_get_operator_info`

## `im_livechat.channel.rule` (defines)

Livechat Channel Rules

- `regex_url` Char “URL Regex”
- `action` Selection “Live Chat Button” (required)
- `auto_popup_timer` Integer “Time to Open”
- `chatbot_script_id` Many2one → `chatbot.script` “Chatbot”
- `chatbot_enabled_condition` Selection “Enable ChatBot” (required)
- `channel_id` Many2one → `im_livechat.channel`
- `country_ids` Many2many → `res.country`
- `sequence` Integer “Matching order”

Public methods: `match_rule`

Extension points: `_check_regex_url`

## `im_livechat.channel.member.history` (defines)

Keep the channel member history

- `member_id` Many2one → `discuss.channel.member`
- `livechat_member_type` Selection (store, compute=_compute_member_fields)
- `channel_id` Many2one → `discuss.channel` (store, index, compute=_compute_member_fields)
- `guest_id` Many2one → `mail.guest` (store, compute=_compute_member_fields)
- `partner_id` Many2one → `res.partner` (store, compute=_compute_member_fields)
- `chatbot_script_id` Many2one → `chatbot.script` (store, compute=_compute_member_fields)
- `agent_expertise_ids` Many2many → `im_livechat.expertise` (store, compute=_compute_member_fields)
- `conversation_tag_ids` Many2many → `im_livechat.conversation.tag` (related=channel_id.livechat_conversation_tag_ids)
- `avatar_128` Binary (compute=_compute_avatar_128)
- `session_country_id` Many2one → `res.country` (related=channel_id.country_id)
- `session_livechat_channel_id` Many2one → `im_livechat.channel` (related=channel_id.livechat_channel_id)
- `session_outcome` Selection (related=channel_id.livechat_outcome)
- `session_start_hour` Float (related=channel_id.livechat_start_hour)
- `session_week_day` Selection (related=channel_id.livechat_week_day)
- `session_duration_hour` Float “Session Duration” (store, compute=_compute_session_duration_hour)
- `rating_id` Many2one → `rating.rating` (store, compute=_compute_rating_id)
- `rating` Float (related=rating_id.rating)
- `rating_text` Selection “Rating text” (related=rating_id.rating_text)
- `call_history_ids` Many2many → `discuss.call.history`
- `has_call` Float (store, compute=_compute_has_call)
- `call_count` Float “# of Sessions with Calls” (related=has_call)
- `call_percentage` Float “Session with Calls (%)” (related=has_call)
- `call_duration_hour` Float “Call Duration” (store, compute=_compute_call_duration_hour)
- `message_count` Integer “# of Messages per Session”
- `help_status` Selection (store, compute=_compute_help_status)
- `response_time_hour` Float “Response Time”

Public methods: `action_open_discuss_channel_view`

## `im_livechat.conversation.tag` (defines)

Live Chat Conversation Tags

- `name` Char “Name” (required)
- `color` Integer “Color”
- `conversation_ids` Many2many → `discuss.channel` “Discuss Channels”

Extension points: `_get_default_color`

## `im_livechat.expertise` (defines)

Live Chat Expertise

- `name` Char “Name” (required)
- `user_ids` Many2many → `res.users` “Operators” (compute=_compute_user_ids)

Extension points: `_get_users_by_expertise`

## `ir.qweb` (extends)


Extension points: `_get_bundles_to_pregenarate`

## `ir.websocket` (extends)


## `mail.message` (extends)


Extension points: `_get_store_partner_name_fields`

## `rating.rating` (extends)


Public methods: `action_open_rated_object`

## `res.groups` (extends)


Public methods: `write`

## `res.partner` (extends)

- `user_livechat_username` Char (compute=_compute_user_livechat_username)
- `chatbot_script_ids` One2many → `chatbot.script`
- `livechat_channel_count` Integer (compute=_compute_livechat_channel_count)

Public methods: `action_view_livechat_sessions`

Extension points: `_get_store_livechat_username_fields`

## `res.users` (extends)

- `livechat_channel_ids` Many2many → `im_livechat.channel`
- `livechat_username` Char “Livechat Username” (compute=_compute_livechat_username)
- `livechat_lang_ids` Many2many → `res.lang` “Livechat Languages” (compute=_compute_livechat_lang_ids)
- `livechat_expertise_ids` Many2many → `im_livechat.expertise` “Live Chat Expertise” (compute=_compute_livechat_expertise_ids)
- `livechat_ongoing_session_count` Integer “Number of Ongoing sessions” (compute=_compute_livechat_ongoing_session_count)
- `livechat_is_in_call` Boolean (compute=_compute_livechat_is_in_call)
- `has_access_livechat` Boolean “Has access to Livechat” (readonly, compute=_compute_has_access_livechat)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`, `write`

## `res.users.settings` (extends)

- `livechat_username` Char “Livechat Username”
- `livechat_lang_ids` Many2many → `res.lang` “Livechat languages”
- `livechat_expertise_ids` Many2many → `im_livechat.expertise` “Live Chat Expertise”

## `im_livechat.report.channel` (defines)

Livechat Support Channel Report

- `uuid` Char “UUID” (readonly)
- `channel_id` Many2one → `discuss.channel` (readonly)
- `channel_name` Char “Channel Name” (readonly)
- `livechat_channel_id` Many2one → `im_livechat.channel` (readonly)
- `start_date` Datetime “Start Date of session” (readonly)
- `start_hour` Char “Start Hour of session” (readonly)
- `start_date_minutes` Char “Start Date of session, truncated to minutes” (readonly)
- `day_number` Selection “Day of the Week” (readonly)
- `time_to_answer` Float “Response Time” (readonly)
- `start_date_hour` Char “Hour of start Date of session” (readonly)
- `duration` Float “Duration (min)” (readonly)
- `nbr_message` Integer “Messages per Session” (readonly)
- `country_id` Many2one → `res.country` (readonly)
- `lang_id` Many2one → `res.lang` “Language” (readonly, related=channel_id.livechat_lang_id)
- `rating` Integer “Rating” (readonly)
- `rating_text` Char “Satisfaction Rate” (readonly)
- `partner_id` Many2one → `res.partner` (readonly)
- `handled_by_bot` Integer “Handled by Bot” (readonly)
- `handled_by_agent` Integer “Handled by Agent” (readonly)
- `visitor_partner_id` Many2one → `res.partner` “Customer” (readonly)
- `call_duration_hour` Float “Call Duration” (readonly)
- `has_call` Float “Whether the session had a call” (readonly)
- `number_of_calls` Float “# of Sessions with calls” (readonly, related=has_call)
- `percentage_of_calls` Float “Session with Calls (%)” (readonly, related=has_call)
- `session_outcome` Selection “Session Outcome” (readonly)
- `chatbot_script_id` Many2one → `chatbot.script` (readonly)
- `chatbot_answers_path` Char “Chatbot Answers” (readonly)
- `chatbot_answers_path_str` Char “Chatbot Answers (String)” (readonly)
- `session_expertises` Char “Expertises used in this session (String)” (readonly)
- `session_expertise_ids` Many2many → `im_livechat.expertise` “Expertises used in this session” (readonly, related=channel_id.livechat_expertise_ids)
- `conversation_tag_ids` Many2many → `im_livechat.conversation.tag` “Tags used in this conversation” (readonly, related=channel_id.livechat_conversation_tag_ids)
- `agent_requesting_help_history` Many2one → `im_livechat.channel.member.history` (readonly, related=channel_id.livechat_agent_requesting_help_history)
- `agent_providing_help_history` Many2one → `im_livechat.channel.member.history` (readonly, related=channel_id.livechat_agent_providing_help_history)

Public methods: `action_open_discuss_channel_view`, `formatted_read_group`
