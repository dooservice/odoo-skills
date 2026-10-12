# hr_skills — Skills Management

Depends on: hr.

## `hr.employee` (extends)

- `resume_line_ids` One2many → `hr.resume.line` “Resume lines”
- `employee_skill_ids` One2many → `hr.employee.skill` “Skills”
- `current_employee_skill_ids` One2many → `hr.employee.skill` (compute=_compute_current_employee_skill_ids)
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)
- `certification_ids` One2many → `hr.employee.skill` (compute=_compute_certification_ids)
- `display_certification_page` Boolean (compute=_compute_display_certification_page)

Public methods: `create`, `get_internal_resume_lines`, `load_demo_data`, `write`

## `hr.employee.public` (extends)

- `resume_line_ids` One2many → `hr.resume.line` “Resume lines”
- `employee_skill_ids` One2many → `hr.employee.skill` “Skills”
- `current_employee_skill_ids` One2many → `hr.employee.skill` (related=employee_id.current_employee_skill_ids)
- `certification_ids` One2many → `hr.employee.skill` (related=employee_id.certification_ids)
- `display_certification_page` Boolean (related=employee_id.display_certification_page)

## `hr.employee.skill` (defines)

Skill level for employee

Inherits: `hr.individual.skill.mixin`

- `employee_id` Many2one → `hr.employee` (required, index)
- `company_id` Many2one (related=employee_id.company_id)

Public methods: `action_hr_employee_skill_certification`, `action_save`, `get_current_skills_by_employee`, `open_hr_employee_skill_modal`

## `hr.individual.skill.mixin` (defines)

Skill level

- `skill_id` Many2one → `hr.skill` (required, store, compute=_compute_skill_id)
- `skill_level_id` Many2one → `hr.skill.level` (required, store, index, compute=_compute_skill_level_id)
- `skill_type_id` Many2one → `hr.skill.type` (required, index)
- `level_progress` Integer (related=skill_level_id.level_progress)
- `color` Integer (related=skill_type_id.color)
- `valid_from` Date “Validity Start”
- `valid_to` Date “Validity Stop”
- `levels_count` Integer (related=skill_type_id.levels_count)
- `certification_skill_type_count` Integer (compute=_compute_certification_skill_type_count)
- `is_certification` Boolean (related=skill_type_id.is_certification)
- `display_warning_message` Boolean
- `certificate_file` Binary “Certificate”

Extension points: `_check_date`, `_check_not_overlapping_regular_skill`, `_check_skill_level`, `_check_skill_type`, `_create_individual_skills`, `_get_overlapping_individual_skill`, `_get_passive_fields`, `_get_transformed_commands`

## `hr.job` (extends)

- `job_skill_ids` One2many → `hr.job.skill` “Skills”
- `current_job_skill_ids` One2many → `hr.job.skill` (compute=_compute_current_job_skill_ids)
- `skill_ids` Many2many → `hr.skill` (store, compute=_compute_skill_ids)

Public methods: `create`, `write`

## `hr.job.skill` (defines)

Skill for job position

Inherits: `hr.individual.skill.mixin`

- `job_id` Many2one → `hr.job` (required, index)

## `hr.resume.line` (defines)

Resume line of an employee

- `employee_id` Many2one → `hr.employee` “Employee” (required, index)
- `avatar_128` Image (related=employee_id.avatar_128)
- `company_id` Many2one (related=employee_id.company_id)
- `department_id` Many2one (related=employee_id.department_id)
- `name` Char (required)
- `date_start` Date (required)
- `date_end` Date
- `duration` Integer “Duration”
- `description` Html “Description”
- `line_type_id` Many2one → `hr.resume.line.type` “Type” (index)
- `is_course` Boolean (related=line_type_id.is_course)
- `course_type` Selection “Course Type” (required)
- `color` Char (compute=_compute_color)
- `external_url` Char “External URL” (store, compute=_compute_external_url)
- `certificate_file` Binary “Certificate”
- `resume_line_properties` Properties “Properties”

## `hr.resume.line.type` (defines)

Type of a resume line

- `name` Char (required)
- `sequence` Integer “Sequence”
- `is_course` Boolean “Course”
- `resume_line_type_properties_definition` PropertiesDefinition “Sections Properties”

## `hr.skill` (defines)

Skill

- `name` Char (required)
- `sequence` Integer
- `skill_type_id` Many2one → `hr.skill.type` (required, index)
- `color` Integer (related=skill_type_id.color)

## `hr.skill.level` (defines)

Skill Level

- `skill_type_id` Many2one → `hr.skill.type`
- `name` Char (required)
- `level_progress` Integer “Progress”
- `default_level` Boolean
- `technical_is_new_default` Boolean (compute=_compute_technical_is_new_default)

Public methods: `create`, `write`

## `hr.skill.type` (defines)

Skill Type

- `active` Boolean “Active”
- `sequence` Integer “Sequence”
- `name` Char (required)
- `skill_ids` One2many → `hr.skill` “Skills”
- `skill_level_ids` One2many → `hr.skill.level` “Levels”
- `color` Integer “Color”
- `levels_count` Integer (store, compute=_compute_levels_count)
- `is_certification` Boolean “Certification”

Public methods: `copy_data`

Extension points: `_check_no_null_skill_or_skill_level`, `_get_default_color`

## `resource.resource` (extends)

- `employee_skill_ids` One2many (related=employee_id.employee_skill_ids)

## `report.hr_skills.report_employee_cv` (defines)

Employee Resume


Extension points: `_get_report_values`

## `hr.employee.skill.history.report` (defines)

Employee Skills Report

- `employee_id` Many2one → `hr.employee` (readonly)
- `date` Date
- `skill_id` Many2one → `hr.skill` (readonly)
- `skill_type_id` Many2one → `hr.skill.type` (readonly)
- `level_progress` Float (readonly)

Public methods: `init`

## `hr.employee.skill.report` (defines)

Employee Skills Report

Inherits: `hr.manager.department.report`

- `company_id` Many2one → `res.company` (readonly)
- `department_id` Many2one → `hr.department` (readonly)
- `job_id` Many2one → `hr.job` (readonly)
- `skill_id` Many2one → `hr.skill` (readonly)
- `skill_type_id` Many2one → `hr.skill.type` (readonly)
- `skill_level` Char (readonly)
- `level_progress` Float (readonly)
- `active` Boolean (related=employee_id.active)

Public methods: `formatted_read_grouping_sets`, `init`

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
