# onboarding — Onboarding Toolbox

Depends on: web.

## `onboarding.onboarding` (defines)

Onboarding

- `name` Char “Name of the onboarding”
- `route_name` Char “One word name” (required)
- `step_ids` Many2many → `onboarding.onboarding.step` “Onboarding steps”
- `text_completed` Char “Message at completion”
- `is_per_company` Boolean “Should be done per company?” (readonly, compute=_compute_is_per_company)
- `panel_close_action_name` Char “Closing action”
- `current_progress_id` Many2one → `onboarding.progress` (compute=_compute_current_progress)
- `current_onboarding_state` Selection “Completion State” (readonly, compute=_compute_current_progress)
- `is_onboarding_closed` Boolean “Was panel closed?” (compute=_compute_current_progress)
- `progress_ids` One2many → `onboarding.progress` “Onboarding Progress Records” (readonly)
- `sequence` Integer

Public methods: `action_close`, `action_close_panel`, `action_refresh_progress_ids`, `action_toggle_visibility`, `write`

Extension points: `_create_progress`, `_prepare_rendering_values`

## `onboarding.onboarding.step` (defines)

Onboarding Step

- `onboarding_ids` Many2many → `onboarding.onboarding` “Onboardings”
- `title` Char “Title”
- `description` Char “Description”
- `button_text` Char “Button text” (required)
- `done_icon` Char “Font Awesome Icon when completed”
- `done_text` Char “Text to show when step is completed”
- `step_image` Binary “Step Image”
- `step_image_filename` Char “Step Image Filename”
- `step_image_alt` Char “Alt Text for the Step Image”
- `panel_step_open_action_name` Char “Opening action”
- `current_progress_step_id` Many2one → `onboarding.progress.step` “Step Progress” (compute=_compute_current_progress)
- `current_step_state` Selection “Completion State” (compute=_compute_current_progress)
- `progress_ids` One2many → `onboarding.progress.step` “Onboarding Progress Step Records” (readonly)
- `is_per_company` Boolean “Is per company”
- `sequence` Integer

Public methods: `action_set_just_done`, `action_validate_step`, `check_step_on_onboarding_has_action`, `write`

Extension points: `_create_progress_steps`, `_get_placeholder_filename`

## `onboarding.progress` (defines)

Onboarding Progress Tracker

- `onboarding_state` Selection “Onboarding progress” (store, compute=_compute_onboarding_state)
- `is_onboarding_closed` Boolean “Was panel closed?”
- `company_id` Many2one → `res.company`
- `onboarding_id` Many2one → `onboarding.onboarding` (required)
- `progress_step_ids` Many2many → `onboarding.progress.step` “Progress Steps Trackers”

Public methods: `action_close`, `action_toggle_visibility`, `init`

Extension points: `_get_and_update_onboarding_state`

## `onboarding.progress.step` (defines)

Onboarding Progress Step Tracker

- `progress_ids` Many2many → `onboarding.progress` “Related Onboarding Progress Tracker”
- `step_state` Selection “Onboarding Step Progress”
- `step_id` Many2one → `onboarding.onboarding.step` “Onboarding Step” (required)
- `company_id` Many2one → `res.company`

Public methods: `action_consolidate_just_done`, `action_set_just_done`, `init`
