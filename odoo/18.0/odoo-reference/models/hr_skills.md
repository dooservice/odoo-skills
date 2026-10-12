# hr_skills — Skills Management

Depends on: hr.

## `hr.employee` (extends)

- `resume_line_ids` One2many → `hr.resume.line` “Resume lines”
- `employee_skill_ids` One2many → `hr.employee.skill` “Skills”
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)

Public methods: `create`, `write`

## `hr.employee.public` (extends)

- `resume_line_ids` One2many → `hr.resume.line` “Resume lines”
- `employee_skill_ids` One2many → `hr.employee.skill` “Skills”

## `hr.employee.skill` (defines)

Skill level for an employee

- `employee_id` Many2one → `hr.employee` (required)
- `skill_id` Many2one → `hr.skill` (required, store, compute=_compute_skill_id)
- `skill_level_id` Many2one → `hr.skill.level` (required, store, compute=_compute_skill_level_id)
- `skill_type_id` Many2one → `hr.skill.type` (required)
- `level_progress` Integer (related=skill_level_id.level_progress)
- `color` Integer (related=skill_type_id.color)

Public methods: `create`, `write`

Extension points: `_check_skill_level`, `_check_skill_type`, `_create_logs`

## `hr.employee.skill.log` (defines)

Skills History

- `employee_id` Many2one → `hr.employee` (required)
- `department_id` Many2one → `hr.department`
- `skill_id` Many2one → `hr.skill` (required, store, compute=_compute_skill_id)
- `skill_level_id` Many2one → `hr.skill.level` (required, store, compute=_compute_skill_level_id)
- `skill_type_id` Many2one → `hr.skill.type` (required)
- `level_progress` Integer (store, related=skill_level_id.level_progress)
- `date` Date

## `hr.resume.line` (defines)

Resume line of an employee

- `employee_id` Many2one → `hr.employee` (required, index)
- `name` Char (required)
- `date_start` Date (required)
- `date_end` Date
- `description` Html “Description”
- `line_type_id` Many2one → `hr.resume.line.type` “Type”
- `display_type` Selection “Display Type”

## `hr.resume.line.type` (defines)

Type of a resume line

- `name` Char (required)
- `sequence` Integer “Sequence”

## `hr.skill` (defines)

Skill

- `name` Char (required)
- `sequence` Integer
- `skill_type_id` Many2one → `hr.skill.type` (required)
- `color` Integer (related=skill_type_id.color)

## `hr.skill.level` (defines)

Skill Level

- `skill_type_id` Many2one → `hr.skill.type`
- `name` Char (required)
- `level_progress` Integer “Progress”
- `default_level` Boolean

Public methods: `create`, `write`

## `hr.skill.type` (defines)

Skill Type

- `active` Boolean “Active”
- `name` Char (required)
- `skill_ids` One2many → `hr.skill` “Skills”
- `skill_level_ids` One2many → `hr.skill.level` “Levels”
- `color` Integer “Color”

Public methods: `copy_data`

Extension points: `_get_default_color`

## `res.users` (extends)

- `resume_line_ids` One2many (related=employee_id.resume_line_ids)
- `employee_skill_ids` One2many (related=employee_id.employee_skill_ids)

Public methods: `SELF_READABLE_FIELDS`, `SELF_WRITEABLE_FIELDS`

## `resource.resource` (extends)

- `employee_skill_ids` One2many (related=employee_id.employee_skill_ids)

## `report.hr_skills.report_employee_cv` (defines)

Employee Resume


Extension points: `_get_report_values`

## `hr.employee.skill.report` (defines)

Employee Skills Report

Inherits: `hr.manager.department.report`

- `id` Id
- `display_name` Char (related=employee_id.name)
- `company_id` Many2one → `res.company` (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `skill_id` Many2one → `hr.skill` (readonly)
- `skill_type_id` Many2one → `hr.skill.type` (readonly)
- `skill_level` Char (readonly)
- `level_progress` Float (readonly)
- `active` Boolean (related=employee_id.active)

Public methods: `init`

## `hr.employee.cv.wizard` (defines)

Print Resume

- `employee_ids` Many2many → `hr.employee`
- `color_primary` Char “Primary Color” (required)
- `color_secondary` Char “Secondary Color” (required)
- `show_skills` Boolean “Skills”
- `show_contact` Boolean “Contact Information”
- `show_others` Boolean “Others”
- `can_show_others` Boolean (compute=_compute_can_show_others)
- `can_show_skills` Boolean (compute=_compute_can_show_others)

Public methods: `action_validate`
