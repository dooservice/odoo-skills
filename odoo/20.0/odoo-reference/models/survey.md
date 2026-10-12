# survey — Surveys

Depends on: auth_signup, http_routing, mail, web_tour, gamification, digest.

## `gamification.badge` (extends)

- `survey_ids` One2many → `survey.survey`
- `survey_id` Many2one → `survey.survey` (store, compute=_compute_survey_id)

## `gamification.challenge` (extends)

- `challenge_category` Selection

## `digest.digest` (extends)

- `kpi_nbr_of_answers` Boolean “Participants”
- `kpi_nbr_of_answers_value` Integer (compute=_compute_kpi_nbr_of_answers_value)
- `kpi_nbr_of_certified_participants` Boolean “Certified Participants”
- `kpi_nbr_of_certified_participants_value` Integer (compute=_compute_kpi_nbr_of_certified_participants_value)

Extension points: `_get_kpi_custom_settings`

## `ir.http` (extends)


Public methods: `get_nearest_lang`

Extension points: `_get_translation_frontend_modules_name`

## `res.lang` (extends)


Public methods: `write`

## `res.partner` (extends)

- `certifications_count` Integer “Certifications Count” (compute=_compute_certifications_count)
- `certifications_company_count` Integer “Company Certifications Count” (compute=_compute_certifications_company_count)

Public methods: `action_view_certifications`

## `survey.question` (defines)

Survey Question

- `title` Char “Title” (required)
- `description` Html “Description”
- `question_placeholder` Char “Placeholder” (store, compute=_compute_question_placeholder)
- `background_image` Image “Background Image” (store, compute=_compute_background_image)
- `background_image_url` Char “Background Url” (compute=_compute_background_image_url)
- `survey_id` Many2one → `survey.survey` “Survey”
- `scoring_type` Selection “Scoring Type” (readonly, related=survey_id.scoring_type)
- `sequence` Integer “Sequence”
- `session_available` Boolean “Live Session available” (readonly, related=survey_id.session_available)
- `survey_session_speed_rating` Boolean (related=survey_id.session_speed_rating)
- `survey_session_speed_rating_time_limit` Integer “General Time limit (seconds)” (related=survey_id.session_speed_rating_time_limit)
- `is_page` Boolean “Is a page?”
- `question_ids` One2many → `survey.question` “Questions” (compute=_compute_question_ids)
- `questions_selection` Selection (readonly, related=survey_id.questions_selection)
- `random_questions_count` Integer “# Questions Randomly Picked”
- `page_id` Many2one → `survey.question` “Page” (store, compute=_compute_page_id)
- `question_type` Selection “Question Type” (store, compute=_compute_question_type)
- `is_scored_question` Boolean “Scored” (store, compute=_compute_is_scored_question)
- `answer_numerical_box` Float “Correct numerical answer”
- `answer_date` Date “Correct date answer”
- `answer_datetime` Datetime “Correct datetime answer”
- `answer_score` Float “Score”
- `save_as_email` Boolean “Save as user email” (store, compute=_compute_save_as_email)
- `save_as_nickname` Boolean “Save as nickname” (store, compute=_compute_save_as_nickname)
- `suggested_answer_ids` One2many → `survey.question.answer` “Types of answers”
- `matrix_subtype` Selection “Matrix Type”
- `matrix_row_ids` One2many → `survey.question.answer` “Matrix Rows”
- `scale_min` Integer “Scale Minimum Value”
- `scale_max` Integer “Scale Maximum Value”
- `scale_min_label` Char “Scale Minimum Label”
- `scale_max_label` Char “Scale Maximum Label”
- `scale_min_label_placeholder` Char “Min Label Placeholder” (compute=_compute_scale_min_label_placeholder)
- `scale_max_label_placeholder` Char “Max Label Placeholder” (compute=_compute_scale_max_label_placeholder)
- `is_time_limited` Boolean “The question is limited in time”
- `is_time_customized` Boolean “Customized speed rewards”
- `time_limit` Integer “Time limit (seconds)”
- `comments_allowed` Boolean “Show Comments Field”
- `comments_message` Char “Comment Message”
- `comment_count_as_answer` Boolean “Comment is an answer”
- `validation_required` Boolean “Validate entry” (store, compute=_compute_validation_required)
- `validation_email` Boolean “Input must be an email”
- `validation_length_min` Integer “Minimum Text Length”
- `validation_length_max` Integer “Maximum Text Length”
- `validation_min_float_value` Float “Minimum value”
- `validation_max_float_value` Float “Maximum value”
- `validation_min_date` Date “Minimum Date”
- `validation_max_date` Date “Maximum Date”
- `validation_min_datetime` Datetime “Minimum Datetime”
- `validation_max_datetime` Datetime “Maximum Datetime”
- `validation_error_msg` Char “Validation Error”
- `constr_mandatory` Boolean “Mandatory Answer”
- `constr_error_msg` Char “Error message”
- `user_input_line_ids` One2many → `survey.user_input.line` “Answers”
- `triggering_question_ids` Many2many → `survey.question` “Triggering Questions” (compute=_compute_triggering_question_ids)
- `allowed_triggering_question_ids` Many2many → `survey.question` “Allowed Triggering Questions” (compute=_compute_allowed_triggering_question_ids)
- `is_placed_before_trigger` Boolean “Is misplaced?” (compute=_compute_allowed_triggering_question_ids)
- `triggering_answer_ids` Many2many → `survey.question.answer` “Triggering Answers” (store)

Public methods: `copy`, `create`, `default_get`, `validate_question`

Extension points: `_check_question_type_for_pages`, `_get_correct_answers`, `_get_stats_data`, `_get_stats_data_answers`, `_get_stats_data_scale`, `_get_stats_graph_data_matrix`, `_get_stats_summary_data`, `_get_stats_summary_data_choice`, `_get_stats_summary_data_numerical`, `_get_stats_summary_data_scored`, `_prepare_statistics`

## `survey.question.answer` (defines)

Survey Label

- `question_id` Many2one → `survey.question` “Question”
- `matrix_question_id` Many2one → `survey.question` “Question (as matrix row)”
- `question_type` Selection (related=question_id.question_type)
- `sequence` Integer “Label Sequence order”
- `scoring_type` Selection (related=question_id.scoring_type)
- `value` Char “Suggested value”
- `value_image` Image “Image”
- `value_image_filename` Char “Image Filename”
- `value_label` Char “Value Label” (compute=_compute_value_label)
- `is_correct` Boolean “Correct”
- `answer_score` Float “Score”

Extension points: `_check_question_not_empty`, `_get_answer_matching_domain`

## `survey.survey` (defines)

Survey

Inherits: `mail.thread`, `mail.activity.mixin`

- `survey_type` Selection “Survey Type” (required)
- `lang_ids` Many2many → `res.lang` “Languages”
- `allowed_survey_types` Json “Allowed survey types” (compute=_compute_allowed_survey_types)
- `title` Char “Survey Title” (required)
- `color` Integer “Color Index”
- `description` Html “Description”
- `description_done` Html “End Message”
- `background_image` Image “Background Image”
- `background_image_url` Char “Background Url” (compute=_compute_background_image_url)
- `background_image_filename` Char “Background Filename”
- `active` Boolean “Active”
- `user_id` Many2one → `res.users` “Responsible”
- `restrict_user_ids` Many2many → `res.users` “Restricted to”
- `question_and_page_ids` One2many → `survey.question` “Sections and Questions”
- `page_ids` One2many → `survey.question` “Pages” (compute=_compute_page_and_question_ids)
- `question_ids` One2many → `survey.question` “Questions” (compute=_compute_page_and_question_ids)
- `question_count` Integer “# Questions” (compute=_compute_page_and_question_ids)
- `questions_layout` Selection “Pagination” (required)
- `questions_selection` Selection “Question Selection” (required)
- `progression_mode` Selection “Display Progress as”
- `user_input_ids` One2many → `survey.user_input` “User responses” (readonly)
- `access_mode` Selection “Access Mode” (required)
- `access_token` Char “Access Token”
- `users_login_required` Boolean “Require Login”
- `users_can_go_back` Boolean “Users can go back”
- `users_can_signup` Boolean “Users can signup” (compute=_compute_users_can_signup)
- `answer_count` Integer “Registered” (compute=_compute_survey_statistic)
- `answer_done_count` Integer “Attempts” (compute=_compute_survey_statistic)
- `answer_score_avg` Float “Avg Score (%)” (compute=_compute_survey_statistic)
- `answer_duration_avg` Float “Average Duration” (compute=_compute_answer_duration_avg)
- `success_count` Integer “Success” (compute=_compute_survey_statistic)
- `success_ratio` Integer “Success Ratio (%)” (compute=_compute_survey_statistic)
- `scoring_type` Selection “Scoring” (required, store, compute=_compute_scoring_type)
- `scoring_success_min` Float “Required Score (%)”
- `scoring_max_obtainable` Float “Maximum obtainable score” (compute=_compute_scoring_max_obtainable)
- `is_attempts_limited` Boolean “Limited number of attempts” (store, compute=_compute_is_attempts_limited)
- `attempts_limit` Integer “Number of attempts”
- `is_time_limited` Boolean “The survey is limited in time”
- `time_limit` Float “Time limit (minutes)”
- `certification` Boolean “Is a Certification” (store, compute=_compute_certification)
- `certification_mail_template_id` Many2one → `mail.template`
- `certification_report_layout` Selection “Certification template”
- `certification_give_badge` Boolean “Give Badge” (store, compute=_compute_certification_give_badge)
- `certification_badge_id` Many2one → `gamification.badge`
- `certification_badge_id_dummy` Many2one “Certification Badge ” (related=certification_badge_id)
- `session_available` Boolean “Live session available” (compute=_compute_session_available)
- `session_state` Selection “Session State”
- `session_code` Char “Session Code” (store, compute=_compute_session_code)
- `session_link` Char “Session Link” (compute=_compute_session_link)
- `session_question_id` Many2one → `survey.question` “Current Question”
- `session_question_can_answer` Boolean “Can Answer Current Question”
- `session_start_time` Datetime “Current Session Start Time”
- `session_question_start_time` Datetime “Current Question Start Time”
- `session_answer_count` Integer “Answers Count” (compute=_compute_session_answer_count)
- `session_question_answer_count` Integer “Question Answers Count” (compute=_compute_session_question_answer_count)
- `session_show_leaderboard` Boolean “Show Session Leaderboard” (compute=_compute_session_show_leaderboard)
- `session_speed_rating` Boolean “Reward quick answers”
- `session_speed_rating_time_limit` Integer “Time limit (seconds)”
- `has_conditional_questions` Boolean “Contains conditional questions” (compute=_compute_has_conditional_questions)

Public methods: `action_archive`, `action_end_session`, `action_open_session_manager`, `action_print_survey`, `action_result_survey`, `action_send_survey`, `action_start_session`, `action_start_survey`, `action_survey_preview_certification_template`, `action_survey_user_input`, `action_survey_user_input_certified`, `action_survey_user_input_completed`, `action_test_survey`, `action_unarchive`, `check_validity`, `copy`, `create`, `default_get`, `get_print_url`, `get_start_short_url`, `get_start_url`, `write`

Extension points: `_check_answer_creation`, `_check_scoring_after_page_availability`, `_check_survey_responsible_access`, `_create_answer`, `_create_certification_badge_trigger`, `_get_conditional_maps`, `_get_default_access_token`, `_get_next_page_or_question`, `_get_number_of_attempts_lefts`, `_get_pages_and_questions_to_show`, `_get_pages_or_questions`, `_get_session_most_voted_answers`, `_get_session_next_question`, `_get_supported_lang_codes`, `_get_survey_questions`, `_prepare_challenge_category`, `_prepare_leaderboard_values`, `_prepare_statistics`, `_prepare_user_input_predefined_questions`

## `survey.user_input` (defines)

Survey User Input

Inherits: `mail.thread`, `mail.activity.mixin`

- `survey_id` Many2one → `survey.survey` “Survey” (required, readonly, index)
- `scoring_type` Selection “Scoring” (related=survey_id.scoring_type)
- `start_datetime` Datetime “Start date and time” (readonly)
- `end_datetime` Datetime “End date and time” (readonly)
- `deadline` Datetime “Deadline”
- `lang_id` Many2one → `res.lang` “Language”
- `state` Selection “Status” (readonly)
- `test_entry` Boolean (readonly)
- `last_displayed_page_id` Many2one → `survey.question` “Last displayed question/page”
- `is_attempts_limited` Boolean “Limited number of attempts” (related=survey_id.is_attempts_limited)
- `attempts_limit` Integer “Number of attempts” (related=survey_id.attempts_limit)
- `attempts_count` Integer “Attempts Count” (compute=_compute_attempts_info)
- `attempts_number` Integer “Attempt n°” (compute=_compute_attempts_info)
- `survey_time_limit_reached` Boolean “Survey Time Limit Reached” (compute=_compute_survey_time_limit_reached)
- `access_token` Char “Identification token” (required, readonly)
- `invite_token` Char “Invite token” (readonly)
- `partner_id` Many2one → `res.partner` “Contact” (readonly)
- `create_uid` Many2one → `res.users` “Created by” (index)
- `email` Char “Email” (readonly)
- `nickname` Char “Nickname”
- `user_input_line_ids` One2many → `survey.user_input.line` “Answers”
- `predefined_question_ids` Many2many → `survey.question` “Predefined Questions” (readonly)
- `scoring_percentage` Float “Score (%)” (store, compute=_compute_scoring_values)
- `scoring_total` Float “Total Score” (store, compute=_compute_scoring_values)
- `scoring_success` Boolean “Quiz Passed” (store, compute=_compute_scoring_success)
- `survey_first_submitted` Boolean “Survey First Submitted”
- `is_session_answer` Boolean “Is in a Session”
- `question_time_limit_reached` Boolean “Question Time Limit Reached” (compute=_compute_question_time_limit_reached)

Public methods: `action_print_answers`, `action_redirect_to_attempts`, `action_resend`, `create`, `get_print_url`, `get_start_url`

Extension points: `_get_conditional_values`, `_get_inactive_conditional_questions`, `_get_line_answer_values`, `_get_line_comment_values`, `_get_next_post_submit_page_or_question`, `_get_post_submit_questions`, `_get_print_questions`, `_get_selected_suggested_answers`, `_prepare_statistics`

## `survey.user_input.line` (defines)

Survey User Input Line

- `user_input_id` Many2one → `survey.user_input` “User Input” (required, index)
- `survey_id` Many2one “Survey” (store, related=user_input_id.survey_id)
- `question_id` Many2one → `survey.question` “Question” (required, index)
- `page_id` Many2one “Section” (related=question_id.page_id)
- `question_sequence` Integer “Sequence” (store, related=question_id.sequence)
- `lang_id` Many2one → `res.lang` (related=user_input_id.lang_id)
- `skipped` Boolean “Skipped”
- `answer_type` Selection “Answer Type”
- `value_char_box` Char “Text answer”
- `value_numerical_box` Float “Numerical answer”
- `value_scale` Integer “Scale value”
- `value_date` Date “Date answer”
- `value_datetime` Datetime “Datetime answer”
- `value_text_box` Text “Free Text answer”
- `suggested_answer_id` Many2one → `survey.question.answer` “Suggested answer”
- `matrix_row_id` Many2one → `survey.question.answer` “Row answer”
- `answer_score` Float “Score” (store, compute=_compute_answer_score)
- `answer_is_correct` Boolean “Correct” (store, compute=_compute_answer_score)

Extension points: `_check_answer_type_skipped`, `_get_answer_matching_domain`, `_get_answer_value`

## `survey.survey` (extends)


Public methods: `action_load_sample_custom`, `action_load_survey_template_sample`, `action_show_sample`, `get_survey_templates_data`

Extension points: `_get_survey_template_values`, `_prepare_assessment_template_values`, `_prepare_live_session_template_values`, `_prepare_survey_template_values`

## `survey.invite` (defines)

Survey Invitation Wizard

Inherits: `mail.composer.mixin`

- `attachment_ids` Many2many → `ir.attachment` “Attachments” (store, compute=_compute_attachment_ids)
- `author_id` Many2one → `res.partner` (index)
- `partner_ids` Many2many → `res.partner` “Recipients”
- `existing_partner_ids` Many2many → `res.partner` (readonly, compute=_compute_existing_partner_ids)
- `emails` Text “Additional emails”
- `existing_emails` Text “Existing emails” (readonly, compute=_compute_existing_emails)
- `existing_mode` Selection “Handle existing” (required)
- `existing_text` Text “Resend Comment” (compute=_compute_existing_text)
- `mail_server_id` Many2one → `ir.mail_server`
- `survey_id` Many2one → `survey.survey` “Survey” (required)
- `survey_start_url` Char “Survey URL” (compute=_compute_survey_start_url)
- `survey_access_mode` Selection (readonly, related=survey_id.access_mode)
- `survey_users_login_required` Boolean (readonly, related=survey_id.users_login_required)
- `survey_users_can_signup` Boolean (related=survey_id.users_can_signup)
- `deadline` Datetime “Answer deadline”
- `send_email` Boolean (compute=_compute_send_email)
- `scheduled_date` Datetime “Scheduled Date”

Public methods: `action_invite`, `create`

Extension points: `_check_deadline_after_schedule`, `_get_answers_values`, `_get_default_author`, `_get_done_partners_emails`, `_prepare_answers`
