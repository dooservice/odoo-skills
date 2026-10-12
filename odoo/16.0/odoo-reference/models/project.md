# project — Project

Depends on: analytic, base_setup, mail, portal, rating, resource, web, web_tour, digest.

## `account.analytic.account` (extends)

Analytic Account

- `project_ids` One2many → `project.project` “Projects”
- `project_count` Integer “Project Count” (compute=_compute_project_count)

Public methods: `action_view_projects`

Extension points: `_check_company_id`

## `res.company` (extends)

- `analytic_plan_id` Many2one → `account.analytic.plan` “Default Plan” (compute=_compute_analytic_plan_id)

Public methods: `write`

## `digest.digest` (extends)

- `kpi_project_task_opened` Boolean “Open Tasks”
- `kpi_project_task_opened_value` Integer (compute=_compute_project_task_opened_value)

## `ir.ui.menu` (extends)


## `mail.message` (extends)


Public methods: `init`

## `project.task.type` (defines)

Task Stage

- `active` Boolean “Active”
- `name` Char “Name” (required)
- `description` Text
- `sequence` Integer
- `project_ids` Many2many → `project.project` “Projects”
- `legend_blocked` Char “Red Kanban Label” (required)
- `legend_done` Char “Green Kanban Label” (required)
- `legend_normal` Char “Grey Kanban Label” (required)
- `mail_template_id` Many2one → `mail.template` “Email Template”
- `fold` Boolean “Folded in Kanban”
- `rating_template_id` Many2one → `mail.template` “Rating Email Template”
- `auto_validation_kanban_state` Boolean “Automatic Kanban Status”
- `disabled_rating_warning` Text (compute=_compute_disabled_rating_warning)
- `user_id` Many2one → `res.users` (index)

Public methods: `remove_personal_stage`, `toggle_active`, `unlink_wizard`, `write`

Extension points: `_check_personal_stage_not_linked_to_projects`, `_get_default_project_ids`

## `project.project` (defines)

Project

Inherits: `portal.mixin`, `mail.alias.mixin`, `mail.thread`, `mail.activity.mixin`, `rating.parent.mixin`

- `name` Char “Name” (required)
- `description` Html
- `active` Boolean
- `sequence` Integer
- `partner_id` Many2one → `res.partner` “Customer”
- `partner_email` Char “Email” (store, compute=_compute_partner_email)
- `partner_phone` Char “Phone” (store, compute=_compute_partner_phone)
- `commercial_partner_id` Many2one (related=partner_id.commercial_partner_id)
- `company_id` Many2one → `res.company` “Company” (required)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, related=company_id.currency_id)
- `analytic_account_id` Many2one → `account.analytic.account` “Analytic Account”
- `analytic_account_balance` Monetary (related=analytic_account_id.balance)
- `favorite_user_ids` Many2many → `res.users` “Members”
- `is_favorite` Boolean “Show Project on Dashboard” (compute=_compute_is_favorite)
- `label_tasks` Char “Use Tasks as”
- `tasks` One2many → `project.task` “Task Activities”
- `resource_calendar_id` Many2one → `resource.calendar` “Working Time” (related=company_id.resource_calendar_id)
- `type_ids` Many2many → `project.task.type` “Tasks Stages”
- `task_count` Integer “Task Count” (compute=_compute_task_count)
- `task_count_with_subtasks` Integer (compute=_compute_task_count)
- `task_ids` One2many → `project.task` “Tasks”
- `color` Integer “Color Index”
- `user_id` Many2one → `res.users` “Project Manager”
- `alias_enabled` Boolean “Use Email Alias” (compute=_compute_alias_enabled)
- `alias_id` Many2one → `mail.alias` “Alias” (required)
- `alias_value` Char “Alias email” (compute=_compute_alias_value)
- `privacy_visibility` Selection “Visibility” (required)
- `privacy_visibility_warning` Char “Privacy Visibility Warning” (compute=_compute_privacy_visibility_warning)
- `access_instruction_message` Char “Access Instruction Message” (compute=_compute_access_instruction_message)
- `doc_count` Integer “Number of documents attached” (compute=_compute_attached_docs_count)
- `date_start` Date “Start Date”
- `date` Date “Expiration Date” (index)
- `allow_subtasks` Boolean “Sub-tasks”
- `allow_recurring_tasks` Boolean “Recurring Tasks”
- `allow_task_dependencies` Boolean “Task Dependencies”
- `allow_milestones` Boolean “Milestones”
- `tag_ids` Many2many → `project.tags` “Tags”
- `task_properties_definition` PropertiesDefinition “Task Properties”
- `collaborator_ids` One2many → `project.collaborator` “Collaborators”
- `collaborator_count` Integer “# Collaborators” (compute=_compute_collaborator_count)
- `rating_request_deadline` Datetime (store, compute=_compute_rating_request_deadline)
- `rating_active` Boolean “Customer Ratings”
- `allow_rating` Boolean “Allow Customer Ratings” (compute=_compute_allow_rating)
- `rating_status` Selection (required)
- `rating_status_period` Selection (required)
- `stage_id` Many2one → `project.project.stage` “Stage” (index)
- `update_ids` One2many → `project.update`
- `last_update_id` Many2one → `project.update` “Last Update”
- `last_update_status` Selection (required, store, compute=_compute_last_update_status)
- `last_update_color` Integer (compute=_compute_last_update_color)
- `milestone_ids` One2many → `project.milestone`
- `milestone_count` Integer (compute=_compute_milestone_count)
- `milestone_count_reached` Integer (compute=_compute_milestone_reached_count)
- `is_milestone_exceeded` Boolean (compute=_compute_is_milestone_exceeded)

Public methods: `action_get_list_view`, `action_profitability_items`, `action_project_task_burndown_chart_report`, `action_project_timesheets`, `action_view_all_rating`, `action_view_tasks`, `action_view_tasks_analysis`, `copy`, `create`, `get_last_update_or_default`, `get_milestones`, `get_panel_data`, `map_tasks`, `message_subscribe`, `name_create`, `project_update_all_action`, `toggle_favorite`, `unlink`, `write`

Extension points: `_check_project_sharing_access`, `_create_analytic_account`, `_create_analytic_account_from_values`, `_get_already_included_profitability_invoice_line_ids`, `_get_default_favorite_user_ids`, `_get_milestones`, `_get_profitability_aal_domain`, `_get_profitability_items`, `_get_profitability_labels`, `_get_profitability_sequence_per_invoice_type`, `_get_stat_buttons`, `_get_user_values`

## `project.task` (defines)

Task

Inherits: `portal.mixin`, `mail.thread.cc`, `mail.activity.mixin`, `rating.mixin`

- `active` Boolean
- `name` Char “Title” (required)
- `description` Html “Description”
- `priority` Selection “Priority” (index)
- `sequence` Integer “Sequence”
- `stage_id` Many2one → `project.task.type` “Stage” (store, index, compute=_compute_stage_id)
- `tag_ids` Many2many → `project.tags` “Tags”
- `kanban_state` Selection “Status” (required, store, compute=_compute_kanban_state)
- `kanban_state_label` Char “Kanban State Label” (compute=_compute_kanban_state_label)
- `create_date` Datetime “Created On” (readonly)
- `write_date` Datetime “Last Updated On” (readonly)
- `date_end` Datetime “Ending Date” (index)
- `date_assign` Datetime “Assigning Date” (readonly)
- `date_deadline` Date “Deadline” (index)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly, index)
- `project_id` Many2one → `project.project` “Project” (store, index, compute=_compute_project_id)
- `task_properties` Properties “Properties”
- `display_project_id` Many2one → `project.project` (index)
- `planned_hours` Float “Initially Planned Hours”
- `subtask_planned_hours` Float “Sub-tasks Planned Hours” (compute=_compute_subtask_planned_hours)
- `user_ids` Many2many → `res.users` “Assignees”
- `portal_user_names` Char (compute=_compute_portal_user_names)
- `personal_stage_type_ids` Many2many → `project.task.type` “Personal Stage”
- `personal_stage_id` Many2one → `project.task.stage.personal` “Personal Stage State” (compute=_compute_personal_stage_id)
- `personal_stage_type_id` Many2one → `project.task.type` “Personal User Stage” (compute=_compute_personal_stage_type_id)
- `partner_id` Many2one → `res.partner` “Customer” (store, compute=_compute_partner_id)
- `partner_is_company` Boolean (readonly, related=partner_id.is_company)
- `commercial_partner_id` Many2one (related=partner_id.commercial_partner_id)
- `partner_email` Char “Email” (store, compute=_compute_partner_email)
- `partner_phone` Char “Phone” (store, compute=_compute_partner_phone)
- `partner_city` Char (related=partner_id.city)
- `email_cc` Char
- `manager_id` Many2one → `res.users` “Project Manager” (readonly, related=project_id.user_id)
- `company_id` Many2one → `res.company` “Company” (required, store, compute=_compute_company_id)
- `color` Integer “Color Index”
- `project_color` Integer “Project Color” (related=project_id.color)
- `rating_active` Boolean “Project Rating Status” (related=project_id.rating_active)
- `attachment_ids` One2many → `ir.attachment` “Main Attachments” (compute=_compute_attachment_ids)
- `displayed_image_id` Many2one → `ir.attachment` “Cover Image”
- `legend_blocked` Char “Kanban Blocked Explanation” (readonly, related=stage_id.legend_blocked)
- `legend_done` Char “Kanban Valid Explanation” (readonly, related=stage_id.legend_done)
- `legend_normal` Char “Kanban Ongoing Explanation” (readonly, related=stage_id.legend_normal)
- `is_closed` Boolean “Closing Stage” (store, index, related=stage_id.fold)
- `parent_id` Many2one → `project.task` “Parent Task” (index)
- `ancestor_id` Many2one → `project.task` “Ancestor Task” (store, compute=_compute_ancestor_id)
- `child_ids` One2many → `project.task` “Sub-tasks”
- `child_text` Char (compute=_compute_child_text)
- `allow_subtasks` Boolean “Allow Sub-tasks” (readonly, related=project_id.allow_subtasks)
- `subtask_count` Integer “Sub-task Count” (compute=_compute_subtask_count)
- `email_from` Char “Email From” (store, compute=_compute_email_from)
- `project_privacy_visibility` Selection “Project Visibility” (related=project_id.privacy_visibility)
- `working_hours_open` Float “Working Hours to Assign” (store, compute=_compute_elapsed)
- `working_hours_close` Float “Working Hours to Close” (store, compute=_compute_elapsed)
- `working_days_open` Float “Working Days to Assign” (store, compute=_compute_elapsed)
- `working_days_close` Float “Working Days to Close” (store, compute=_compute_elapsed)
- `website_message_ids` One2many
- `is_private` Boolean (compute=_compute_is_private)
- `allow_milestones` Boolean (related=project_id.allow_milestones)
- `milestone_id` Many2one → `project.milestone` (store, compute=_compute_milestone_id)
- `has_late_and_unreached_milestone` Boolean (compute=_compute_has_late_and_unreached_milestone)
- `allow_task_dependencies` Boolean (related=project_id.allow_task_dependencies)
- `depend_on_ids` Many2many → `project.task` “Blocked By”
- `dependent_ids` Many2many → `project.task` “Block”
- `dependent_tasks_count` Integer “Dependent Tasks” (compute=_compute_dependent_tasks_count)
- `is_blocked` Boolean (store, compute=_compute_is_blocked)
- `display_parent_task_button` Boolean (compute=_compute_display_parent_task_button)
- `allow_recurring_tasks` Boolean (related=project_id.allow_recurring_tasks)
- `recurring_task` Boolean “Recurrent”
- `recurring_count` Integer “Tasks in Recurrence” (compute=_compute_recurring_count)
- `recurrence_id` Many2one → `project.task.recurrence`
- `recurrence_update` Selection
- `recurrence_message` Char “Next Recurrencies” (compute=_compute_recurrence_message)
- `repeat_interval` Integer “Repeat Every” (compute=_compute_repeat)
- `repeat_unit` Selection (compute=_compute_repeat)
- `repeat_type` Selection “Until” (compute=_compute_repeat)
- `repeat_until` Date “End Date” (compute=_compute_repeat)
- `repeat_number` Integer “Repetitions” (compute=_compute_repeat)
- `repeat_on_month` Selection (compute=_compute_repeat)
- `repeat_on_year` Selection (compute=_compute_repeat)
- `mon` Boolean “Mon” (compute=_compute_repeat)
- `tue` Boolean “Tue” (compute=_compute_repeat)
- `wed` Boolean “Wed” (compute=_compute_repeat)
- `thu` Boolean “Thu” (compute=_compute_repeat)
- `fri` Boolean “Fri” (compute=_compute_repeat)
- `sat` Boolean “Sat” (compute=_compute_repeat)
- `sun` Boolean “Sun” (compute=_compute_repeat)
- `repeat_day` Selection (compute=_compute_repeat)
- `repeat_week` Selection (compute=_compute_repeat)
- `repeat_weekday` Selection “Day Of The Week” (compute=_compute_repeat)
- `repeat_month` Selection (compute=_compute_repeat)
- `repeat_show_dow` Boolean (compute=_compute_repeat_visibility)
- `repeat_show_day` Boolean (compute=_compute_repeat_visibility)
- `repeat_show_week` Boolean (compute=_compute_repeat_visibility)
- `repeat_show_month` Boolean (compute=_compute_repeat_visibility)
- `analytic_account_id` Many2one → `account.analytic.account` (store, compute=_compute_analytic_account_id)
- `is_analytic_account_id_changed` Boolean “Is Analytic Account Manually Changed” (store, compute=_compute_is_analytic_account_id_changed)
- `project_analytic_account_id` Many2one → `account.analytic.account` “Project Analytic Account” (related=project_id.analytic_account_id)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITABLE_FIELDS`, `action_assign_to_me`, `action_continue_recurrence`, `action_dependent_tasks`, `action_open_parent_task`, `action_open_ratings`, `action_open_task`, `action_project_sharing_open_subtasks`, `action_project_sharing_open_task`, `action_project_sharing_view_parent_task`, `action_recurring_tasks`, `action_stop_recurrence`, `action_unassign_me`, `copy`, `copy_data`, `create`, `default_get`, `email_split`, `fields_get`, `filtered_domain`, `get_empty_list_help`, `get_unusual_days`, `mapped`, `message_new`, `message_subscribe`, `message_update`, `rating_apply`, `read`, `read_group`, `stage_find`, `update_date_end`, `write`

Extension points: `_check_no_cyclic_dependencies`, `_check_parent_id`, `_get_all_subtasks`, `_get_attachments_search_domain`, `_get_default_partner_id`, `_get_default_personal_stage_create_vals`, `_get_default_stage_id`, `_get_depends_tracked_fields`, `_get_portal_sudo_context`, `_get_portal_sudo_vals`, `_get_recurrence_fields`, `_get_recurrence_start_date`, `_get_subtask_ids_per_task_id`, `_get_subtasks_recursively`, `_get_task_analytic_account_id`, `_get_view`, `_get_view_cache_key`, `_get_weekdays`

## `project.tags` (defines)

Project Tags

- `name` Char “Name” (required)
- `color` Integer “Color”
- `project_ids` Many2many → `project.project` “Projects”
- `task_ids` Many2many → `project.task` “Tasks”

Public methods: `arrange_tag_list_by_id`, `read_group`, `search_read`

Extension points: `_get_default_color`, `_get_project_tags_domain`

## `project.collaborator` (defines)

Collaborators in project shared

- `project_id` Many2one → `project.project` (required, readonly)
- `partner_id` Many2one → `res.partner` (required, readonly)
- `partner_email` Char (related=partner_id.email)

Public methods: `create`, `name_get`, `unlink`

## `project.milestone` (defines)

Project Milestone

Inherits: `mail.thread`

- `name` Char (required)
- `project_id` Many2one → `project.project` (required)
- `deadline` Date
- `is_reached` Boolean “Reached”
- `reached_date` Date (store, compute=_compute_reached_date)
- `task_ids` One2many → `project.task`
- `is_deadline_exceeded` Boolean (compute=_compute_is_deadline_exceeded)
- `is_deadline_future` Boolean (compute=_compute_is_deadline_future)
- `task_count` Integer “# of Tasks” (compute=_compute_task_count)
- `can_be_marked_as_done` Boolean (compute=_compute_can_be_marked_as_done)

Public methods: `action_view_tasks`, `copy`, `toggle_is_reached`

Extension points: `_get_data`, `_get_data_list`, `_get_default_project_id`, `_get_fields_to_export`

## `project.project.stage` (defines)

Project Stage

- `active` Boolean
- `sequence` Integer
- `name` Char (required)
- `mail_template_id` Many2one → `mail.template` “Email Template”
- `fold` Boolean “Folded in Kanban”

## `project.task.recurrence` (defines)

Task Recurrence

- `task_ids` One2many → `project.task`
- `next_recurrence_date` Date
- `recurrence_left` Integer “Number of Tasks Left to Create”
- `repeat_interval` Integer “Repeat Every”
- `repeat_unit` Selection
- `repeat_type` Selection “Until”
- `repeat_until` Date “End Date”
- `repeat_number` Integer “Repetitions”
- `repeat_on_month` Selection
- `repeat_on_year` Selection
- `mon` Boolean “Mon”
- `tue` Boolean “Tue”
- `wed` Boolean “Wed”
- `thu` Boolean “Thu”
- `fri` Boolean “Fri”
- `sat` Boolean “Sat”
- `sun` Boolean “Sun”
- `repeat_day` Selection
- `repeat_week` Selection
- `repeat_weekday` Selection “Day Of The Week”
- `repeat_month` Selection

Public methods: `create`, `write`

Extension points: `_check_recurrence_days`, `_check_repeat_interval`, `_check_repeat_number`, `_check_repeat_until_date`, `_check_repeat_until_month`, `_create_next_task`, `_create_subtasks`, `_get_next_recurring_dates`, `_get_recurring_fields`, `_get_weekdays`

## `project.task.stage.personal` (defines)

Personal Task Stage

- `task_id` Many2one → `project.task` (required, index)
- `user_id` Many2one → `res.users` (required, index)
- `stage_id` Many2one → `project.task.type`

## `project.update` (defines)

Project Update

Inherits: `mail.thread.cc`, `mail.activity.mixin`

- `name` Char “Title” (required)
- `status` Selection (required)
- `color` Integer (compute=_compute_color)
- `progress` Integer
- `progress_percentage` Float (compute=_compute_progress_percentage)
- `user_id` Many2one → `res.users` “Author” (required)
- `description` Html
- `date` Date
- `project_id` Many2one → `project.project` (required)
- `name_cropped` Char (compute=_compute_name_cropped)

Public methods: `create`, `default_get`, `unlink`

Extension points: `_get_last_updated_milestone`, `_get_milestone_values`, `_get_template_values`

## `res.config.settings` (extends)

- `module_project_forecast` Boolean “Planning”
- `module_hr_timesheet` Boolean “Task Logs”
- `group_subtask_project` Boolean “Sub-tasks”
- `group_project_rating` Boolean “Customer Ratings”
- `group_project_stages` Boolean “Project Stages”
- `group_project_recurring_tasks` Boolean “Recurring Tasks”
- `group_project_task_dependencies` Boolean “Task Dependencies”
- `group_project_milestone` Boolean “Milestones”
- `analytic_plan_id` Many2one → `account.analytic.plan` “Default Plan” (related=company_id.analytic_plan_id)

Public methods: `set_values`

Extension points: `_get_basic_project_domain`

## `res.partner` (extends)

- `task_ids` One2many → `project.task` “Tasks”
- `task_count` Integer “# Tasks” (compute=_compute_task_count)

Extension points: `_create_portal_users`

## `project.task.type` (extends)


## `project.project` (extends)


## `project.task` (extends)


## `report.project.task.user` (defines)

Tasks Analysis

- `name` Char “Task” (readonly)
- `user_ids` Many2many → `res.users` “Assignees” (readonly)
- `create_date` Datetime “Create Date” (readonly)
- `date_assign` Datetime “Assignment Date” (readonly)
- `date_end` Datetime “Ending Date” (readonly)
- `date_deadline` Date “Deadline” (readonly)
- `date_last_stage_update` Datetime “Last Stage Update” (readonly)
- `project_id` Many2one → `project.project` “Project” (readonly)
- `working_days_close` Float “Working Days to Close” (readonly)
- `working_days_open` Float “Working Days to Assign” (readonly)
- `delay_endings_days` Float “Days to Deadline” (readonly)
- `nbr` Integer “# of Tasks” (readonly)
- `working_hours_open` Float “Working Hours to Assign” (readonly)
- `working_hours_close` Float “Working Hours to Close” (readonly)
- `rating_last_value` Float “Rating Value (/5)” (readonly)
- `rating_avg` Float “Average Rating” (readonly)
- `priority` Selection “Priority” (readonly)
- `state` Selection “Kanban State” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `stage_id` Many2one → `project.task.type` “Stage” (readonly)
- `is_closed` Boolean “Closing Stage” (readonly)
- `task_id` Many2one → `project.task` “Tasks” (readonly)
- `active` Boolean (readonly)
- `tag_ids` Many2many → `project.tags` “Tags” (readonly)
- `parent_id` Many2one → `project.task` “Parent Task” (readonly)
- `ancestor_id` Many2one → `project.task` “Ancestor Task” (readonly)
- `rating_last_text` Selection “Rating Last Text” (compute=_compute_rating_last_text)
- `personal_stage_type_ids` Many2many → `project.task.type` “Personal Stage” (readonly)
- `milestone_id` Many2one → `project.milestone` (readonly)
- `milestone_reached` Boolean “Is Milestone Reached” (readonly)
- `milestone_deadline` Date “Milestone Deadline” (readonly)

Public methods: `init`

## `project.task.burndown.chart.report` (defines)

Burndown Chart

- `planned_hours` Float “Allocated Hours” (readonly)
- `date` Datetime “Date” (readonly)
- `date_assign` Datetime “Assignment Date” (readonly)
- `date_deadline` Date “Deadline” (readonly)
- `display_project_id` Many2one → `project.project` (readonly)
- `is_closed` Boolean “Closing Stage” (readonly)
- `milestone_id` Many2one → `project.milestone` (readonly)
- `partner_id` Many2one → `res.partner` “Customer” (readonly)
- `project_id` Many2one → `project.project` (readonly)
- `stage_id` Many2one → `project.task.type` (readonly)
- `user_ids` Many2many → `res.users` “Assignees” (readonly)
- `has_late_and_unreached_milestone` Boolean (readonly)

Extension points: `_get_group_by_SQL`

## `project.share.wizard` (defines)

Project Sharing

Inherits: `portal.share`

- `access_mode` Selection
- `display_access_mode` Boolean

Public methods: `action_send_mail`, `default_get`

## `project.task.type.delete.wizard` (defines)

Project Stage Delete Wizard

- `project_ids` Many2many → `project.project` “Projects”
- `stage_ids` Many2many → `project.task.type` “Stages To Delete”
- `tasks_count` Integer “Number of Tasks” (compute=_compute_tasks_count)
- `stages_active` Boolean (compute=_compute_stages_active)

Public methods: `action_archive`, `action_confirm`, `action_unarchive_task`, `action_unlink`

Extension points: `_get_action`
