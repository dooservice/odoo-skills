# project_hr_skills — Project - Skills

Depends on: project, hr_skills.

## `project.task` (extends)

- `user_skill_ids` One2many → `hr.employee.skill` (related=user_ids.employee_skill_ids)

## `report.project.task.user` (extends)

- `user_skill_ids` One2many → `hr.employee.skill` “Skills” (related=user_ids.employee_skill_ids)
