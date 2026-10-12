# project — Project

Depends on: analytic, base_setup, mail, portal_rating, resource, web, web_tour, digest.

## `account.analytic.account` (extends)

Analytic Account

- `project_ids` One2many → `project.project` “Projects”
- `project_count` Integer “Project Count” (compute=_compute_project_count)

Public methods: `action_view_projects`

## `account.analytic.line` (extends)


## `digest.digest` (extends)

- `kpi_project_task_opened` Boolean “Open Tasks”
- `kpi_project_task_opened_value` Integer (compute=_compute_project_task_opened_value)

Extension points: `_get_kpi_custom_settings`

## `ir.ui.menu` (extends)


## `mail.activity` (extends)


## `mail.message` (extends)


## `project.collaborator` (defines)

Collaborators in project shared

- `project_id` Many2one → `project.project` (required, readonly)
- `partner_id` Many2one → `res.partner` (required, readonly, index)
- `partner_email` Char (related=partner_id.email)
- `access_mode` Selection “Access Mode” (required)

Public methods: `create`, `unlink`

## `project.milestone` (defines)

Project Milestone

Inherits: `mail.thread`

- `name` Char (required)
- `sequence` Integer “Sequence”
- `project_id` Many2one → `project.project` (required, index)
- `deadline` Date
- `is_reached` Boolean “Reached”
- `reached_date` Date (store, compute=_compute_reached_date)
- `task_ids` One2many → `project.task`
- `project_allow_milestones` Boolean (compute=_compute_project_allow_milestones)
- `is_deadline_exceeded` Boolean (compute=_compute_is_deadline_exceeded)
- `is_deadline_future` Boolean (compute=_compute_is_deadline_future)
- `task_count` Integer “# of Tasks” (compute=_compute_task_count)
- `done_task_count` Integer “# of Done Tasks” (compute=_compute_task_count)
- `can_be_marked_as_done` Boolean (compute=_compute_can_be_marked_as_done)

Public methods: `action_view_tasks`, `copy`

Extension points: `_get_data`, `_get_data_list`, `_get_default_project_id`, `_get_fields_to_export`

## `project.project` (defines)

Project

Inherits: `portal.mixin`, `mail.alias.mixin`, `rating.parent.mixin`, `mail.activity.mixin`, `mail.tracking.duration.mixin`, `analytic.plan.fields.mixin`

- `name` Char “Name” (required)
- `description` Html
- `active` Boolean
- `sequence` Integer
- `partner_id` Many2one → `res.partner` “Customer”
- `partner_phone` Char (related=partner_id.phone)
- `partner_email` Char (related=partner_id.email)
- `company_id` Many2one → `res.company` “Company” (store, compute=_compute_company_id)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, compute=_compute_currency_id)
- `analytic_account_balance` Monetary (related=account_id.balance)
- `account_id` Many2one → `account.analytic.account`
- `favorite_user_ids` Many2many → `res.users` “Members”
- `is_favorite` Boolean “Show Project on Dashboard” (compute=_compute_is_favorite)
- `label_tasks` Char “Use Tasks as”
- `tasks` One2many → `project.task` “Task Activities”
- `resource_calendar_id` Many2one → `resource.calendar` “Working Time” (compute=_compute_resource_calendar_id)
- `type_ids` Many2many → `project.task.type` “Tasks Stages”
- `task_count` Integer “Task Count” (compute=_compute_task_count)
- `open_task_count` Integer “Open Task Count” (compute=_compute_open_task_count)
- `task_ids` One2many → `project.task` “Tasks”
- `color` Integer “Color Index”
- `user_id` Many2one → `res.users` “Project Manager”
- `alias_id` Many2one
- `privacy_visibility` Selection “Visibility” (required)
- `allowed_internal_user_ids` Many2many → `res.users` “Team Members” (store, compute=_compute_allowed_internal_user_ids)
- `access_instruction_message` Char “Access Instruction Message” (compute=_compute_access_instruction_message)
- `date_start` Date “Start Date”
- `date` Date “Expiration Date” (index)
- `allow_task_dependencies` Boolean “Task Dependencies”
- `allow_milestones` Boolean “Milestones”
- `allow_recurring_tasks` Boolean “Recurring Tasks”
- `tag_ids` Many2many → `project.tags` “Tags”
- `task_properties_definition` PropertiesDefinition “Task Properties”
- `closed_task_count` Integer (compute=_compute_closed_task_count)
- `task_completion_percentage` Float (compute=_compute_task_completion_percentage)
- `collaborator_ids` One2many → `project.collaborator` “Collaborators”
- `collaborator_count` Integer “# Collaborators” (compute=_compute_collaborator_count)
- `stage_id` Many2one → `project.project.stage` “Stage” (index)
- `duration_tracking` Json
- `rotting_days` Integer
- `is_rotting` Boolean
- `date_last_stage_update` Datetime “Last Stage Update” (index)
- `update_ids` One2many → `project.update`
- `update_count` Integer (compute=_compute_total_update_ids)
- `last_update_id` Many2one → `project.update` “Last Update”
- `last_update_status` Selection (required, store, compute=_compute_last_update_status)
- `last_update_color` Integer (compute=_compute_last_update_color)
- `milestone_ids` One2many → `project.milestone`
- `milestone_count` Integer (compute=_compute_milestone_count)
- `milestone_count_reached` Integer (compute=_compute_milestone_reached_count)
- `is_milestone_exceeded` Boolean (compute=_compute_is_milestone_exceeded)
- `milestone_progress` Integer “Milestones Reached” (compute=_compute_milestone_reached_count)
- `next_milestone_id` Many2one → `project.milestone` (compute=_compute_next_milestone_id)
- `can_mark_milestone_as_done` Boolean (compute=_compute_next_milestone_id)
- `is_milestone_deadline_exceeded` Boolean (compute=_compute_next_milestone_id)
- `next_milestone_status` Char (compute=_compute_next_milestone_info)
- `is_template` Boolean
- `show_ratings` Boolean (compute=_compute_show_ratings)
- `google_map_iframe` Html (compute=_compute_google_map_iframe)

Public methods: `action_create_from_template`, `action_create_template_from_project`, `action_get_list_view`, `action_open_project_form`, `action_open_share_project_wizard`, `action_project_task_burndown_chart_report`, `action_project_time_by_stage_report`, `action_toggle_project_template_mode`, `action_undo_convert_to_template`, `action_view_all_rating`, `action_view_tasks`, `action_view_tasks_analysis`, `check_features_enabled`, `copy`, `copy_data`, `create`, `create_template_from_project_undo_callback`, `get_last_update_or_default`, `get_portal_url`, `get_template_tasks`, `map_tasks`, `message_subscribe`, `message_unsubscribe`, `project_update_all_action`, `template_to_project_confirmation_callback`, `toggle_favorite`, `unlink`, `write`

Extension points: `_check_account_id`, `_check_project_group_at_removal`, `_check_project_group_with_field`, `_check_project_sharing_access`, `_create_analytic_account`, `_get_account_node_context`, `_get_default_task_stage`, `_get_hide_partner`, `_get_new_collaborators`, `_get_plan_domain`, `_get_project_features_mapping`, `_get_projects_to_make_billable_domain`, `_get_rotting_depends_fields`, `_get_rotting_domain`, `_get_share_url`, `_get_template_default_context_whitelist`, `_get_template_field_blacklist`, `_get_template_from_project_undo_callbacks`, `_get_template_to_project_confirmation_callbacks`, `_get_template_to_project_warnings`, `_get_values_analytic_account_batch`

## `project.project.stage` (defines)

Project Stage

- `active` Boolean
- `sequence` Integer
- `name` Char “Stage Name” (required)
- `mail_template_id` Many2one → `mail.template` “Email Template”
- `fold` Boolean “Folded”
- `company_id` Many2one → `res.company` “Company”
- `rotting_threshold_days` Integer “Days to rot”

Public methods: `action_unarchive`, `unlink_wizard`, `write`

## `project.role` (defines)

Project Role

- `active` Boolean
- `name` Char (required)
- `color` Integer
- `sequence` Integer
- `user_ids` Many2many → `res.users` “Team Members”

Extension points: `_get_default_color`

## `project.tags` (defines)

Project Tag

- `name` Char “Name” (required)
- `color` Integer “Color”
- `project_ids` Many2many → `project.project` “Projects”
- `task_ids` Many2many → `project.task` “Tasks”

Public methods: `arrange_tag_list_by_id`, `formatted_read_group`, `name_create`, `name_search`, `search_read`

Extension points: `_get_default_color`, `_get_project_tags_domain`

## `project.task` (defines)

Task

Inherits: `portal.mixin`, `mail.activity.mixin`, `rating.mixin`, `mail.tracking.duration.mixin`, `html.field.history.mixin`

- `active` Boolean
- `name` Char “Title” (required)
- `description` Html “Description”
- `priority` Selection “Priority” (index)
- `sequence` Integer “Sequence”
- `stage_id` Many2one → `project.task.type` “Stage” (store, index, compute=_compute_stage_id)
- `tag_ids` Many2many → `project.tags` “Tags”
- `state` Selection “State” (required, store, index, compute=_compute_state)
- `is_closed` Boolean “Closed state” (compute=_compute_is_closed)
- `create_date` Datetime “Created On” (readonly, index)
- `write_date` Datetime “Last Updated On” (readonly)
- `date_end` Datetime “Ending Date” (index)
- `date_assign` Datetime “Assigning Date” (readonly)
- `date_deadline` Datetime “Deadline” (index)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly, index)
- `project_id` Many2one → `project.project` “Project” (store, index, compute=_compute_project_id)
- `display_in_project` Boolean (store, compute=_compute_display_in_project)
- `task_properties` Properties “Properties”
- `allocated_hours` Float “Allocated Time”
- `subtask_allocated_hours` Float “Sub-tasks Allocated Time” (compute=_compute_subtask_allocated_hours)
- `role_ids` Many2many → `project.role` “Project Roles”
- `user_ids` Many2many → `res.users` “Assignees”
- `portal_user_names` Char (compute=_compute_portal_user_names)
- `personal_stage_type_ids` Many2many → `project.task.type` “Personal Stages”
- `personal_stage_id` Many2one → `project.task.stage.personal` “Personal Stage State” (compute=_compute_personal_stage_id)
- `personal_stage_type_id` Many2one → `project.task.type` “Personal Stage” (related=personal_stage_id.stage_id)
- `partner_id` Many2one → `res.partner` “Customer” (store, compute=_compute_partner_id)
- `partner_phone` Char “Contact Number” (store, compute=_compute_partner_phone)
- `email_from` Char “Email From”
- `company_id` Many2one → `res.company` “Company” (store, compute=_compute_company_id)
- `color` Integer “Color Index”
- `rating_active` Boolean “Stage Rating Status” (related=stage_id.rating_active)
- `attachment_ids` One2many → `ir.attachment` “Attachments” (compute=_compute_attachment_ids)
- `displayed_image_id` Many2one → `ir.attachment` “Cover Image”
- `parent_id` Many2one → `project.task` “Parent Task” (index)
- `child_ids` One2many → `project.task` “Sub-tasks”
- `subtask_count` Integer “Sub-task Count” (compute=_compute_subtask_count)
- `closed_subtask_count` Integer “Closed Sub-tasks Count” (compute=_compute_subtask_count)
- `project_privacy_visibility` Selection “Project Visibility” (related=project_id.privacy_visibility)
- `subtask_completion_percentage` Float (compute=_compute_subtask_completion_percentage)
- `working_hours_open` Float “Working Hours to Assign” (store, compute=_compute_elapsed)
- `working_hours_close` Float “Working Hours to Close” (store, compute=_compute_elapsed)
- `working_days_open` Float “Working Days to Assign” (store, compute=_compute_elapsed)
- `working_days_close` Float “Working Days to Close” (store, compute=_compute_elapsed)
- `allow_milestones` Boolean (related=project_id.allow_milestones)
- `milestone_id` Many2one → `project.milestone` (store, compute=_compute_milestone_id)
- `has_late_and_unreached_milestone` Boolean (compute=_compute_has_late_and_unreached_milestone)
- `allow_task_dependencies` Boolean (compute=_compute_allow_task_dependencies)
- `depend_on_ids` Many2many → `project.task` “Blocked By”
- `depend_on_count` Integer “Depending on Tasks” (compute=_compute_depend_on_count)
- `closed_depend_on_count` Integer “Closed Depending on Tasks” (compute=_compute_depend_on_count)
- `dependent_ids` Many2many → `project.task` “Block”
- `dependent_tasks_count` Integer “Dependent Tasks” (compute=_compute_dependent_tasks_count)
- `display_parent_task_button` Boolean (compute=_compute_display_parent_task_button)
- `display_follow_button` Boolean (compute=_compute_display_follow_button)
- `project_sharing_portal_user_ids` Many2many → `res.users` “Assignable Portal Users” (compute=_compute_project_sharing_portal_user_ids)
- `allow_recurring_tasks` Boolean (compute=_compute_allow_recurring_tasks)
- `recurring_task` Boolean “Recurrent”
- `recurring_count` Integer “Tasks in Recurrence” (compute=_compute_recurring_count)
- `recurrence_id` Many2one → `project.task.recurrence`
- `repeat_interval` Integer “Repeat Every” (compute=_compute_repeat)
- `repeat_unit` Selection (compute=_compute_repeat)
- `repeat_type` Selection “Until” (compute=_compute_repeat)
- `repeat_until` Date “End Date” (compute=_compute_repeat)
- `display_name` Char
- `link_preview_name` Char (compute=_compute_link_preview_name)
- `is_template` Boolean
- `has_project_template` Boolean “Has Project Template” (related=project_id.is_template)
- `has_template_ancestor` Boolean (store, compute=_compute_has_template_ancestor)

Public methods: `OPEN_STATES`, `TASK_PORTAL_READABLE_FIELDS`, `TASK_PORTAL_WRITABLE_FIELDS`, `action_archive`, `action_convert_to_subtask`, `action_convert_to_template`, `action_create_from_template`, `action_dependent_tasks`, `action_open_parent_task`, `action_open_ratings`, `action_open_share_task_wizard`, `action_open_subtasks`, `action_open_task`, `action_project_sharing_open_blocking`, `action_project_sharing_open_subtasks`, `action_project_sharing_open_task`, `action_project_sharing_recurring_tasks`, `action_project_sharing_toggle_assign`, `action_project_sharing_view_parent_task`, `action_recurring_tasks`, `action_redirect_to_project_task_form`, `action_undo_convert_to_template`, `action_unlink_recurrence`, `copy`, `copy_data`, `create`, `default_get`, `fields_get`, `get_empty_list_help`, `get_import_templates`, `get_mention_suggestions`, `get_portal_url`, `get_unusual_days`, `is_blocked_by_dependences`, `message_new`, `message_subscribe`, `message_update`, `plan_task_in_calendar`, `project_sharing_toggle_is_follower`, `rating_apply`, `unlink`, `update_date_end`, `write`

Extension points: `_check_no_cyclic_dependencies`, `_check_parent_id`, `_create_task_mapping`, `_get_access_action`, `_get_all_subtasks`, `_get_allowed_access_params`, `_get_attachments_search_domain`, `_get_cannot_start_with_patterns`, `_get_customer_portal_message_types`, `_get_default_partner_id`, `_get_default_personal_stage_create_vals`, `_get_default_stage_id`, `_get_group_pattern`, `_get_groups`, `_get_groups_patterns`, `_get_projects_to_make_billable_domain`, `_get_recurrence_fields`, `_get_rotting_depends_fields`, `_get_rotting_domain`, `_get_share_message_domain`, `_get_share_url`, `_get_subtask_ids_per_task_id`, `_get_subtasks_recursively`, `_get_template_default_context_whitelist`, `_get_template_field_blacklist`, `_get_thread_with_access`, `_get_versioned_fields`, `_get_view_cache_key`, `_prepare_pattern_groups`

## `project.task.recurrence` (defines)

Task Recurrence

- `task_ids` One2many → `project.task`
- `repeat_interval` Integer “Repeat Every”
- `repeat_unit` Selection
- `repeat_type` Selection “Until”
- `repeat_until` Date “End Date”

Extension points: `_check_repeat_interval`, `_check_repeat_until_date`, `_create_next_occurrences`, `_create_next_occurrences_values`, `_get_last_task_id_per_recurrence_id`, `_get_recurrence_delta`, `_get_recurring_fields_to_copy`, `_get_recurring_fields_to_postpone`

## `project.task.stage.personal` (defines)

Personal Task Stage

- `task_id` Many2one → `project.task` (required, index)
- `user_id` Many2one → `res.users` (required, index)
- `stage_id` Many2one → `project.task.type`

## `project.task.type` (defines)

Task Stage

- `active` Boolean “Active”
- `name` Char “Stage Name” (required)
- `sequence` Integer
- `project_ids` Many2many → `project.project` “Projects”
- `mail_template_id` Many2one → `mail.template` “Email Template”
- `fold` Boolean “Folded”
- `rating_template_id` Many2one → `mail.template` “Rating Email Template”
- `auto_validation_state` Boolean “Automatic Kanban Status”
- `rotting_threshold_days` Integer “Days to rot”
- `user_id` Many2one → `res.users` (store, index, compute=_compute_user_id)
- `rating_request_deadline` Datetime (store, compute=_compute_rating_request_deadline)
- `rating_active` Boolean “Ask for Ratings”
- `rating_status` Selection “Customer Ratings Status” (required)
- `rating_status_period` Selection “Rating Frequency” (required)

Public methods: `action_unarchive`, `unlink_wizard`, `write`

Extension points: `_check_personal_stage_not_linked_to_projects`, `_get_default_project_ids`, `_prepare_personal_stages_deletion`

## `project.update` (defines)

Project Update

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Title” (required)
- `status` Selection (required)
- `color` Integer (compute=_compute_color)
- `progress` Integer
- `progress_percentage` Float (compute=_compute_progress_percentage)
- `user_id` Many2one → `res.users` “Author” (required)
- `description` Html
- `date` Date
- `project_id` Many2one → `project.project` (required, index)
- `name_cropped` Char (compute=_compute_name_cropped)
- `task_count` Integer “Task Count” (readonly)
- `closed_task_count` Integer “Closed Task Count” (readonly)
- `closed_task_percentage` Integer “Closed Task Percentage” (compute=_compute_closed_task_percentage)
- `label_tasks` Char (related=project_id.label_tasks)

Public methods: `create`, `default_get`, `unlink`

Extension points: `_get_milestone_values`, `_get_template_values`

## `res.config.settings` (extends)

- `module_hr_timesheet` Boolean “Task Logs”
- `group_project_stages` Boolean “Project Stages”

Public methods: `set_values`

## `res.groups` (extends)


Extension points: `_get_light_group_xmlids`

## `res.partner` (extends)

- `project_ids` One2many → `project.project` “Projects”
- `task_ids` One2many → `project.task` “Tasks”
- `task_count` Integer “# Tasks” (compute=_compute_task_count)

Public methods: `action_view_tasks`

Extension points: `_create_portal_users`

## `res.users` (extends)

- `favorite_project_ids` Many2many → `project.project` “Favorite Projects”
- `project_role_ids` Many2many → `project.role` “Project Roles”
- `followed_project_ids` Many2many → `project.project`

Public methods: `create`

## `res.users.settings` (extends)


Public methods: `get_embedded_actions_settings`

## `report.project.task.user` (defines)

Tasks Analysis

- `name` Char “Task Title” (readonly)
- `user_ids` Many2many → `res.users` “Assignees” (readonly)
- `create_date` Datetime “Create Date” (readonly)
- `date_assign` Datetime “Assignment Date” (readonly)
- `date_end` Datetime “Ending Date” (readonly)
- `date_deadline` Datetime “Deadline” (readonly)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly)
- `display_in_project` Boolean
- `project_id` Many2one → `project.project` “Project” (readonly)
- `working_days_close` Float “Working Days to Close” (readonly)
- `working_days_open` Float “Working Days to Assign” (readonly)
- `delay_endings_days` Float “Days to Deadline” (readonly)
- `nbr` Integer “# of Tasks” (readonly)
- `working_hours_open` Float “Working Hours to Assign” (readonly)
- `working_hours_close` Float “Working Hours to Close” (readonly)
- `rating_last_value` Float “Last Rating (1-5)” (readonly)
- `rating_avg` Float “Average Rating (1-5)” (readonly)
- `priority` Selection “Priority” (readonly)
- `state` Selection “State” (readonly)
- `is_closed` Boolean “Closed state” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `stage_id` Many2one → `project.task.type` “Stage” (readonly)
- `task_id` Many2one → `project.task` “Task” (readonly)
- `tag_ids` Many2many → `project.tags` “Tags” (readonly)
- `parent_id` Many2one → `project.task` “Parent Task” (readonly)
- `personal_stage_type_ids` Many2many → `project.task.type` “Personal Stage” (readonly)
- `milestone_id` Many2one → `project.milestone` (readonly)
- `message_is_follower` Boolean (related=task_id.message_is_follower)
- `dependent_ids` Many2many → `project.task` “Block” (readonly)
- `description` Text (readonly)
- `is_template` Boolean (readonly)
- `has_template_ancestor` Boolean (readonly)
- `has_project_template` Boolean (readonly)

Public methods: `init`

## `project.task.burndown.chart.report` (defines)

Burndown Chart

- `allocated_hours` Float “Allocated Time” (readonly)
- `date` Datetime “Date” (readonly)
- `date_assign` Datetime “Assignment Date” (readonly)
- `date_deadline` Date “Deadline” (readonly)
- `date_last_stage_update` Date “Last Stage Update” (readonly)
- `state` Selection “State” (readonly)
- `is_open` Boolean “Open” (readonly)
- `is_done` Boolean “Done” (readonly)
- `is_canceled` Boolean “Cancelled” (readonly)
- `milestone_id` Many2one → `project.milestone` (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `project_id` Many2one → `project.project` (readonly)
- `stage_id` Many2one → `project.task.type` (readonly)
- `tag_ids` Many2many → `project.tags` “Tags” (readonly)
- `user_ids` Many2many → `res.users` “Assignees” (readonly)

Public methods: `task_specific_fields`

## `project.task.stage.report` (defines)

Task time spent per stage

- `name` Char “Task Title” (readonly)
- `user_ids` Many2many → `res.users` “Assignees” (readonly, related=task_id.user_ids)
- `tag_ids` Many2many → `project.tags` “Tags” (readonly, related=task_id.tag_ids)
- `milestone_id` Many2one → `project.milestone` (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `create_date` Datetime “Create Date” (readonly)
- `date_deadline` Datetime “Deadline” (readonly)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly)
- `is_closed` Boolean “Closed state” (readonly)
- `priority` Selection “Priority” (readonly)
- `task_id` Many2one → `project.task` “Task” (readonly)
- `project_id` Many2one → `project.project` “Project” (readonly)
- `stage_id` Many2one → `project.task.type` “Stage” (readonly)
- `sequence` Integer “Sequence” (readonly)
- `time_spent` Float “Time Spent” (readonly)
- `task_properties` Properties “Properties”

Public methods: `init`

## `portal.share` (extends)


Public methods: `action_send_mail`

## `project.project.stage.delete.wizard` (defines)

Project Stage Delete Wizard

- `stage_ids` Many2many → `project.project.stage` “Stages To Delete”
- `projects_count` Integer “Number of Projects” (compute=_compute_projects_count)
- `stages_active` Boolean (compute=_compute_stages_active)

Public methods: `action_archive`, `action_unarchive_project`, `action_unlink`

Extension points: `_get_action`

## `project.share.collaborator.wizard` (defines)

Project Sharing Collaborator Wizard

- `parent_wizard_id` Many2one → `project.share.wizard`
- `partner_id` Many2one → `res.partner` “Collaborator” (required)
- `access_mode` Selection “Access” (required)
- `send_invitation` Boolean “Send Invitation” (store, compute=_compute_send_invitation)

## `project.share.wizard` (defines)

Project Sharing

Inherits: `portal.share`

- `share_link` Char “Share Link”
- `collaborator_ids` One2many → `project.share.collaborator.wizard` “Collaborators”
- `existing_partner_ids` Many2many → `res.partner` (compute=_compute_existing_partner_ids)

Public methods: `action_send_mail`, `action_share_record`, `create`, `default_get`

## `task.share.wizard` (defines)

Task Sharing

Inherits: `portal.share`

- `task_id` Many2one → `project.task`
- `project_privacy_visibility` Selection (related=task_id.project_privacy_visibility)

## `project.task.type.delete.wizard` (defines)

Project Task Stage Delete Wizard

- `project_ids` Many2many → `project.project` “Projects”
- `stage_ids` Many2many → `project.task.type` “Stages To Delete”
- `tasks_count` Integer “Number of Tasks” (compute=_compute_tasks_count)
- `stages_active` Boolean (compute=_compute_stages_active)

Public methods: `action_archive`, `action_confirm`, `action_unarchive_task`, `action_unlink`

Extension points: `_get_action`

## `project.template.create.wizard` (defines)

Project Template create Wizard

- `name` Char “Name” (required)
- `date_start` Date “Start Date”
- `date` Date “Expiration Date”
- `alias_name` Char “Alias Name”
- `alias_domain_id` Many2one → `mail.alias.domain` “Alias Domain”
- `template_id` Many2one → `project.project`
- `template_has_dates` Boolean (compute=_compute_template_has_dates)
- `role_to_users_ids` One2many → `project.template.role.to.users.map`

Public methods: `action_open_template_view`, `create_project_from_template`

Extension points: `_create_project_from_template`, `_get_template_whitelist_fields`

## `project.template.role.to.users.map` (defines)

Project role to users mapping

- `wizard_id` Many2one → `project.template.create.wizard`
- `role_id` Many2one → `project.role` “Project Role” (required)
- `user_ids` Many2many → `res.users` “Assignees”
- `role_user_ids` Many2many (related=role_id.user_ids)
