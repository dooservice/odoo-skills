# onboarding — Onboarding toolbox

Depends on: base.

## `onboarding.onboarding` (defines)

Onboarding

- `name` Char “Name of the onboarding”
- `route_name` Char “One word name” (required)
- `step_ids` One2many → `onboarding.onboarding.step`
- `is_per_company` Boolean “Should be done per company?”
- `panel_background_color` Selection “Panel's Background color”
- `panel_background_image` Binary “Panel's background image”
- `panel_close_action_name` Char “Closing action”
- `current_progress_id` Many2one → `onboarding.progress` (compute=_compute_current_progress)
- `current_onboarding_state` Selection “Completion State” (readonly, compute=_compute_current_progress)
- `is_onboarding_closed` Boolean “Was panel closed?” (compute=_compute_current_progress)
- `progress_ids` One2many → `onboarding.progress` “Onboarding Progress Records” (readonly)
- `sequence` Integer

Public methods: `action_close`, `action_toggle_visibility`, `write`

Extension points: `_create_progress`, `_prepare_rendering_values`

## `onboarding.progress` (defines)

Onboarding Progress Tracker

- `onboarding_state` Selection “Onboarding progress” (store, compute=_compute_onboarding_state)
- `is_onboarding_closed` Boolean “Was panel closed?”
- `company_id` Many2one → `res.company`
- `onboarding_id` Many2one → `onboarding.onboarding` (required)
- `progress_step_ids` One2many → `onboarding.progress.step`

Public methods: `action_close`, `action_toggle_visibility`

Extension points: `_get_and_update_onboarding_state`

## `onboarding.progress.step` (defines)

Onboarding Progress Step Tracker

- `progress_id` Many2one → `onboarding.progress` (required)
- `step_state` Selection “Onboarding Step Progress”
- `onboarding_id` Many2one “Onboarding” (related=progress_id.onboarding_id)
- `step_id` Many2one → `onboarding.onboarding.step` “Onboarding Step” (required)

Public methods: `action_consolidate_just_done`, `action_set_just_done`

## `onboarding.onboarding.step` (defines)

Onboarding Step

- `onboarding_id` Many2one → `onboarding.onboarding` “Onboarding” (required, readonly)
- `title` Char “Title”
- `description` Char “Description”
- `button_text` Char “Button text” (required)
- `done_icon` Char “Font Awesome Icon when completed”
- `done_text` Char “Text to show when step is completed”
- `panel_step_open_action_name` Char “Opening action” (required)
- `current_progress_step_id` Many2one → `onboarding.progress.step` “Step Progress” (compute=_compute_current_progress)
- `current_step_state` Selection “Completion State” (compute=_compute_current_progress)
- `progress_ids` One2many → `onboarding.progress.step` “Onboarding Progress Step Records” (readonly)
- `sequence` Integer

Public methods: `action_set_just_done`

Extension points: `_create_progress_steps`
