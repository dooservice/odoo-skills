# survey — XML ids

## ir.actions.act_window

- `survey.action_survey_form`
- `survey.action_survey_user_input`
- `survey.survey_user_input_line_action`
- `survey.action_survey_question_form`
- `survey.survey_question_answer_action`
- `survey.res_partner_action_certifications`

## ir.actions.report

- `survey.certification_report`

## ir.actions.server

- `survey.action_survey_print`

## ir.module.category

- `base.module_category_marketing_surveys`

## ir.rule

- `survey.survey_survey_rule_survey_manager`
- `survey.survey_survey_rule_survey_user`
- `survey.survey_question_rule_survey_manager`
- `survey.survey_question_rule_survey_user`
- `survey.survey_question_answer_rule_survey_manager`
- `survey.survey_question_answer_rule_survey_user`
- `survey.survey_user_input_rule_survey_manager`
- `survey.survey_user_input_line_rule_survey_manager`
- `survey.survey_user_input_rule_survey_user`
- `survey.survey_user_input_line_rule_survey_user`
- `survey.survey_invite_survey_user`
- `survey.survey_invite_survey_manager`

## ir.ui.menu

- `survey.menu_surveys` — Surveys
- `survey.survey_menu_questions` — Questions & Answers
- `survey.menu_survey_form` — Surveys
- `survey.menu_survey_type_form1` — Participations
- `survey.menu_survey_question_form1` — Questions
- `survey.menu_survey_label_form1` — Suggested Values
- `survey.menu_survey_response_line_form` — Detailed Answers

## ir.ui.view

- `survey.certification_report_view_general`
- `survey.certification_report_view`
- `survey.survey_survey_view_form` — on survey.survey
- `survey.survey_survey_view_tree` — on survey.survey
- `survey.survey_survey_view_kanban` — on survey.survey
- `survey.survey_survey_view_activity` — on survey.survey
- `survey.survey_survey_view_search` — on survey.survey
- `survey.survey_survey_view_graph` — on survey.survey
- `survey.survey_survey_view_pivot` — on survey.survey
- `survey.survey_user_input_view_search` — on survey.user_input
- `survey.survey_user_input_view_form` — on survey.user_input
- `survey.survey_user_input_view_tree` — on survey.user_input
- `survey.survey_user_input_viuew_kanban` — on survey.user_input
- `survey.survey_user_input_line_view_form` — on survey.user_input.line
- `survey.survey_response_line_view_tree` — on survey.user_input.line
- `survey.survey_user_input_line_view_search` — on survey.user_input.line
- `survey.survey_question_form` — on survey.question
- `survey.survey_question_tree` — on survey.question
- `survey.survey_question_search` — on survey.question
- `survey.survey_question_answer_view_tree` — on survey.question.answer
- `survey.survey_question_answer_view_form` — on survey.question.answer
- `survey.survey_question_answer_view_search` — on survey.question.answer
- `survey.layout` — inherits web.frontend_layout
- `survey.survey_page_fill`
- `survey.survey_fill_header`
- `survey.survey_fill_form`
- `survey.survey_fill_form_start`
- `survey.survey_fill_form_in_progress`
- `survey.survey_fill_form_done`
- `survey.question_container`
- `survey.question_text_box`
- `survey.question_char_box`
- `survey.question_numerical_box`
- `survey.question_scale`
- `survey.question_date`
- `survey.question_datetime`
- `survey.question_suggested_value_image`
- `survey.question_simple_choice`
- `survey.question_multiple_choice`
- `survey.question_matrix`
- `survey.survey_selection_key`
- `survey.survey_progression`
- `survey.survey_403_page`
- `survey.survey_void_content`
- `survey.survey_auth_required`
- `survey.survey_closed_expired`
- `survey.survey_access_error`
- `survey.survey_button_form_view`
- `survey.survey_button_retake`
- `survey.survey_session_code`
- `survey.survey_navigation`
- `survey.survey_page_print`
- `survey.certification_preview`
- `survey.survey_page_statistics`
- `survey.survey_page_statistics_header`
- `survey.survey_page_statistics_inner`
- `survey.survey_page_statistics_question`
- `survey.survey_results_filters`
- `survey.question_result_text`
- `survey.question_result_number_or_date_or_datetime`
- `survey.question_result_choice`
- `survey.question_result_matrix`
- `survey.question_result_comments`
- `survey.question_table_pagination`
- `survey.survey_remove_unnecessary_decimals`
- `survey.user_input_session` — inherits web.frontend_layout
- `survey.user_input_session_open`
- `survey.user_input_session_manage`
- `survey.user_input_session_manage_content`
- `survey.user_input_session_leaderboard`
- `survey.gamification_badge_form_view_simplified` — on gamification.badge
- `survey.survey_invite_view_form` — on survey.invite
- `survey.res_partner_view_form` — on res.partner inherits base.view_partner_form

## mail.message.subtype

- `survey.mt_survey_user_input_completed`
- `survey.mt_survey_survey_user_input_completed`

## mail.template

- `survey.mail_template_user_input_invite`
- `survey.mail_template_certification`

## report.paperformat

- `survey.paperformat_survey_certification`

## res.groups

- `survey.group_survey_user`
- `survey.group_survey_manager`

## res.users

- `base.default_user`

## web_tour.tour

- `survey.survey_tour`
