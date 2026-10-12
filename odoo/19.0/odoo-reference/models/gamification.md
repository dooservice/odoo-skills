# gamification — Gamification

Depends on: mail.

## `gamification.badge` (defines)

Gamification Badge

Inherits: `mail.thread`, `image.mixin`

- `name` Char “Badge” (required)
- `active` Boolean “Active”
- `description` Html “Description”
- `level` Selection “Forum Badge Level”
- `rule_auth` Selection “Allowance to Grant” (required)
- `rule_auth_user_ids` Many2many → `res.users` “Authorized Users”
- `rule_auth_badge_ids` Many2many → `gamification.badge` “Required Badges”
- `rule_max` Boolean “Monthly Limited Sending”
- `rule_max_number` Integer “Limitation Number”
- `challenge_ids` One2many → `gamification.challenge` “Reward of Challenges”
- `goal_definition_ids` Many2many → `gamification.goal.definition` “Rewarded by”
- `owner_ids` One2many → `gamification.badge.user` “Owners”
- `granted_count` Integer “Total” (compute=_get_owners_info)
- `granted_users_count` Integer “Number of users” (compute=_get_owners_info)
- `unique_owner_ids` Many2many → `res.users` “Unique Owners” (compute=_get_owners_info)
- `stat_this_month` Integer “Monthly total” (compute=_get_badge_user_stats)
- `stat_my` Integer “My Total” (compute=_get_badge_user_stats)
- `stat_my_this_month` Integer “My Monthly Total” (compute=_get_badge_user_stats)
- `stat_my_monthly_sending` Integer “My Monthly Sending Total” (compute=_get_badge_user_stats)
- `remaining_sending` Integer “Remaining Sending Allowed” (compute=_remaining_sending_calc)

Public methods: `check_granting`

Extension points: `_get_badge_user_stats`, `_get_owners_info`

## `gamification.badge.user` (defines)

Gamification User Badge

Inherits: `mail.thread`

- `user_id` Many2one → `res.users` “User” (required, index)
- `user_partner_id` Many2one → `res.partner` (related=user_id.partner_id)
- `sender_id` Many2one → `res.users` “Sender”
- `badge_id` Many2one → `gamification.badge` “Badge” (required, index)
- `challenge_id` Many2one → `gamification.challenge` “Challenge”
- `comment` Text “Comment”
- `badge_name` Char “Badge Name” (related=badge_id.name)
- `level` Selection “Badge Level” (readonly, store, related=badge_id.level)

Public methods: `create`

## `gamification.challenge` (defines)

Gamification Challenge

Inherits: `mail.thread`

- `name` Char “Challenge Name” (required)
- `description` Text “Description”
- `state` Selection “State” (required)
- `manager_id` Many2one → `res.users` “Responsible”
- `user_ids` Many2many → `res.users` “Participants”
- `user_domain` Char “User domain”
- `user_count` Integer “# Users” (compute=_compute_user_count)
- `period` Selection “Periodicity” (required)
- `start_date` Date “Start Date”
- `end_date` Date “End Date”
- `invited_user_ids` Many2many → `res.users` “Suggest to users”
- `line_ids` One2many → `gamification.challenge.line` “Lines” (required)
- `reward_id` Many2one → `gamification.badge` “For Every Succeeding User”
- `reward_first_id` Many2one → `gamification.badge` “For 1st user”
- `reward_second_id` Many2one → `gamification.badge` “For 2nd user”
- `reward_third_id` Many2one → `gamification.badge` “For 3rd user”
- `reward_failure` Boolean “Reward Bests if not Succeeded?”
- `reward_realtime` Boolean “Reward as soon as every goal is reached”
- `visibility_mode` Selection “Display Mode” (required)
- `report_message_frequency` Selection “Report Frequency” (required)
- `report_message_group_id` Many2one → `discuss.channel` “Send a copy to”
- `report_template_id` Many2one → `mail.template` “Report Template” (required)
- `remind_update_delay` Integer “Non-updated manual goals will be reminded after”
- `last_report_date` Date “Last Report Date”
- `next_report_date` Date “Next Report Date” (store, compute=_get_next_report_date)
- `challenge_category` Selection “Appears in” (required)

Public methods: `accept_challenge`, `action_check`, `action_report_progress`, `action_start`, `action_view_users`, `create`, `default_get`, `discard_challenge`, `report_progress`, `write`

Extension points: `_check_challenge_reward`, `_get_challenger_users`, `_get_next_report_date`, `_get_report_template`, `_get_serialized_challenge_lines`, `_get_topN_users`

## `gamification.challenge.line` (defines)

Gamification generic goal for challenge

- `challenge_id` Many2one → `gamification.challenge` “Challenge” (required, index)
- `definition_id` Many2one → `gamification.goal.definition` “Goal Definition” (required)
- `sequence` Integer “Sequence”
- `target_goal` Float “Target Value to Reach” (required)
- `name` Char “Name” (related=definition_id.name)
- `condition` Selection “Condition” (readonly, related=definition_id.condition)
- `definition_suffix` Char “Unit” (readonly, related=definition_id.suffix)
- `definition_monetary` Boolean “Monetary” (readonly, related=definition_id.monetary)
- `definition_full_suffix` Char “Suffix” (readonly, related=definition_id.full_suffix)

## `gamification.goal` (defines)

Gamification Goal

- `definition_id` Many2one → `gamification.goal.definition` “Goal Definition” (required)
- `user_id` Many2one → `res.users` “User” (required, index)
- `user_partner_id` Many2one → `res.partner` (related=user_id.partner_id)
- `line_id` Many2one → `gamification.challenge.line` “Challenge Line”
- `challenge_id` Many2one (readonly, store, index, related=line_id.challenge_id)
- `start_date` Date “Start Date”
- `end_date` Date “End Date”
- `target_goal` Float “To Reach” (required)
- `current` Float “Current Value” (required)
- `completeness` Float “Completeness” (compute=_get_completion)
- `state` Selection “State” (required)
- `to_update` Boolean “To update”
- `closed` Boolean “Closed goal”
- `computation_mode` Selection (related=definition_id.computation_mode)
- `color` Integer “Color Index” (compute=_compute_color)
- `remind_update_delay` Integer “Remind delay”
- `last_update` Date “Last Update”
- `definition_description` Text “Definition Description” (readonly, related=definition_id.description)
- `definition_condition` Selection “Definition Condition” (readonly, related=definition_id.condition)
- `definition_suffix` Char “Suffix” (readonly, related=definition_id.full_suffix)
- `definition_display` Selection “Display Mode” (readonly, related=definition_id.display_mode)

Public methods: `action_cancel`, `action_fail`, `action_reach`, `action_start`, `create`, `get_action`, `update_goal`, `write`

Extension points: `_check_remind_delay`, `_get_completion`, `_get_write_values`

## `gamification.goal.definition` (defines)

Gamification Goal Definition

- `name` Char “Goal Definition” (required)
- `description` Text “Goal Description”
- `monetary` Boolean “Monetary Value”
- `suffix` Char “Suffix”
- `full_suffix` Char “Full Suffix” (compute=_compute_full_suffix)
- `computation_mode` Selection “Computation Mode” (required)
- `display_mode` Selection “Displayed as” (required)
- `model_id` Many2one → `ir.model` “Model”
- `model_inherited_ids` Many2many → `ir.model` (related=model_id.inherited_model_ids)
- `field_id` Many2one → `ir.model.fields` “Field to Sum”
- `field_date_id` Many2one → `ir.model.fields` “Date Field”
- `domain` Char “Filter Domain” (required)
- `batch_mode` Boolean “Batch Mode”
- `batch_distinctive_field` Many2one → `ir.model.fields` “Distinctive field for batch user”
- `batch_user_expression` Char “Evaluated expression for batch mode”
- `compute_code` Text “Python Code”
- `condition` Selection “Goal Performance” (required)
- `action_id` Many2one → `ir.actions.act_window` “Action”
- `res_id_field` Char “ID Field of user”

Public methods: `create`, `write`

Extension points: `_check_domain_validity`, `_check_model_validity`

## `gamification.karma.rank` (defines)

Rank based on karma

Inherits: `image.mixin`

- `name` Text “Rank Name” (required)
- `description` Html “Description”
- `description_motivational` Html “Motivational”
- `karma_min` Integer “Required Karma” (required)
- `user_ids` One2many → `res.users` “Users”
- `rank_users_count` Integer “# Users” (compute=_compute_rank_users_count)

Public methods: `create`, `write`

## `gamification.karma.tracking` (defines)

Track Karma Changes

- `user_id` Many2one → `res.users` (required, index)
- `old_value` Integer “Old Karma Value” (readonly)
- `new_value` Integer “New Karma Value” (required)
- `gain` Integer “Gain” (compute=_compute_gain)
- `consolidated` Boolean “Consolidated”
- `tracking_date` Datetime (readonly, index)
- `reason` Text “Description”
- `origin_ref` Reference “Source”
- `origin_ref_model_name` Selection “Source Type” (store, compute=_compute_origin_ref_model_name)

Public methods: `create`

Extension points: `_get_origin_selection_values`

## `res.users` (extends)

- `karma` Integer “Karma” (store, compute=_compute_karma)
- `karma_tracking_ids` One2many → `gamification.karma.tracking` “Karma Changes”
- `badge_ids` One2many → `gamification.badge.user` “Badges”
- `gold_badge` Integer “Gold badges count” (compute=_get_user_badge_level)
- `silver_badge` Integer “Silver badges count” (compute=_get_user_badge_level)
- `bronze_badge` Integer “Bronze badges count” (compute=_get_user_badge_level)
- `rank_id` Many2one → `gamification.karma.rank`
- `next_rank_id` Many2one → `gamification.karma.rank`

Public methods: `action_karma_report`, `create`, `get_gamification_redirection_data`, `write`

Extension points: `_get_karma_position`, `_get_next_rank`, `_get_tracking_karma_gain_position`, `_get_user_badge_level`, `_get_user_ids_ranked_by_karma`

## `gamification.badge.user.wizard` (defines)

Gamification User Badge Wizard

- `user_id` Many2one → `res.users` “User” (required)
- `badge_id` Many2one → `gamification.badge` “Badge” (required)
- `comment` Text “Comment”

Public methods: `action_grant_badge`

## `gamification.goal.wizard` (defines)

Gamification Goal Wizard

- `goal_id` Many2one → `gamification.goal` “Goal” (required)
- `current` Float “Current”

Public methods: `action_update_current`
