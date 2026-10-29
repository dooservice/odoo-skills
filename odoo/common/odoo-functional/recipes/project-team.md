# To-dos, skills and time off in projects

How the people of a project organise their own work around it: private to-dos that can
become project tasks (To-do app, 17.0+), finding tasks by the skills of their assignees
(18.0+), and approved time off and public holidays written into timesheets on their own.
Needs `project`; `project_todo` installs with it from 17.0; `project_hr_skills` with
`hr_skills`; `project_timesheet_holidays` with `hr_timesheet` and `hr_holidays`. Creating
projects, tasks and timesheets is in `projects-and-timesheets.md`; employees and time off
requests are in `employees-and-expenses.md`. Planning is Enterprise and left out.

## Before you start

- Apps: `project` (To-do from 17.0); `hr_skills` for skills; `hr_timesheet` and
  `hr_holidays` for time off in timesheets.
- Settings: `internal_project_id` and `leave_timesheet_task_id` (Timesheets ‣
  Configuration ‣ Settings ‣ Time Off): the project and task that receive time off hours.
  Installing `hr_timesheet` creates an "Internal" project with a "Time Off" task for each
  company.
- Read first:

```python
print(env.company.internal_project_id.name, env.company.leave_timesheet_task_id.name)
print(env['project.task'].search_read([('project_id', '=', False), ('parent_id', '=', False)], ['name', 'user_ids', 'personal_stage_type_id'], limit=20))
print(env['hr.employee.skill'].search_read([], ['employee_id', 'skill_id', 'skill_level_id'], limit=20))
```

The skills line needs `hr_skills`. In 16.0-18.0 also read the time off types' own
project and task:

```python
print(env['hr.leave.type'].search_read([], ['name', 'company_id', 'timesheet_project_id', 'timesheet_task_id']))
```

## The standard flow

1. **Write a to-do (17.0+).** To-do ‣ New, type the note; the first line becomes its
   title. Assign other users in the form to share it with them.

   ```python
   todo = env['project.task'].with_user(user).create({
       'description': '<p>Call Example Shop about the delivery</p>', 'user_ids': [(6, 0, user.ids)],
   })
   env.cr.commit()
   print(todo.name, todo.personal_stage_type_id.name)
   ```

   A to-do is a task without project. It lands in the user's first personal stage (each
   user has their own, created on first use); dragging it moves `personal_stage_type_id`,
   and the check mark sets `state` to `1_done`.

2. **Turn a to-do into a project task.** Open the to-do ‣ gear menu ‣ Convert to Task,
   choose the Project (and assignees, tags), Convert to Task.

   ```python
   todo.write({'project_id': project.id})
   todo.action_convert_to_task()
   env.cr.commit()
   ```

   Leaves it a task of the project, in its first stage, with the project's company; it
   leaves the To-do app.

3. **Find tasks by skill (18.0+).** Project ‣ open the project (or My Tasks), search,
   choose Skills and type the skill. The skills come from the assignees' employee resume
   (Employees ‣ the employee ‣ Resume tab ‣ Skills).

   ```python
   tasks = env['project.task'].search([('project_id', '=', project.id),
                                       '|', ('user_ids', '=', False), ('user_skill_ids', 'ilike', '<skill>')])
   print(tasks.mapped(lambda t: (t.name, t.user_ids.mapped('name'))))
   ```

   The result also lists unassigned tasks, the ones to staff.

4. **Choose where time off is logged.** Timesheets ‣ Configuration ‣ Settings ‣ Time Off:
   Project and Task. 16.0-18.0 also on each time off type (Time Off ‣ Configuration ‣
   Time Off Types ‣ the type, Timesheet section) when the type belongs to one company.

   ```python
   settings = env['res.config.settings'].create({
       'internal_project_id': internal.id, 'leave_timesheet_task_id': timeoff_task.id,
   })
   settings.execute()
   env.cr.commit()
   ```

5. **Approve time off.** As in `employees-and-expenses.md`, steps 5 and 6. Approval
   writes one timesheet line per working day of the request, for the hours of the
   employee's working schedule, on that project and task.

   ```python
   print(leave.state, leave.timesheet_ids.mapped(lambda t: (t.date, t.unit_amount, t.task_id.name)))
   ```

   Refusing or cancelling the time off deletes those lines.

6. **Public holidays.** Time Off ‣ Configuration ‣ Public Holidays (20.0: Company
   Holidays) ‣ New: the holiday writes the same lines for every employee on that working
   schedule (all schedules when left empty).

   ```python
   holiday = env['resource.calendar.leaves'].create({
       'name': '<holiday>', 'company_id': env.company.id, 'calendar_id': False,
       'date_from': '<YYYY-MM-DD> 00:00:00', 'date_to': '<YYYY-MM-DD> 23:59:59',
   })
   env.cr.commit()
   print(len(holiday.timesheet_ids))
   ```

## Variations

- **To-do with a reminder (17.0+)**: the Activities menu (clock icon) ‣ Add To-Do
  (`mail.activity.todo.create`) creates a to-do and an activity on its due date.
- **Time off types that log nothing**: 16.0-18.0 clear the type's project and task (17.0,
  18.0: Generate Timesheet off on a company-less type); 19.0 types with Kind of Time Off
  "Worked Time" (`time_type = 'other'`) and 20.0 time types counted as working time log nothing.
- **Skills on employees**: adding the skills themselves is in `hr_skills` (Employees ‣
  the employee ‣ Resume).

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| To-do app (`project_todo`) | no | yes | yes | yes | yes |
| Skills search on tasks (`project_hr_skills`) | no | no | yes | yes | yes |
| Time off project/task per type | `timesheet_project_id`, `timesheet_task_id` | same + `timesheet_generate` | same | company settings only | same |
| Time off skipped for | types without project or task | `timesheet_generate` off | same | `time_type = 'other'` | `count_as = 'working_time'` |
| Public holidays menu | Public Holidays | same | same | same | Company Holidays |

## Verify

```python
print(todo.project_id.name, todo.stage_id.name)
print(env['account.analytic.line'].search_read([('holiday_id', '!=', False)], ['employee_id', 'date', 'unit_amount', 'task_id'], limit=10))
print(env['account.analytic.line'].search_count([('global_leave_id', '=', holiday.id)]))
```

## Pitfalls

- Time off timesheets cannot be edited or deleted, and nobody can log time on the time off
  task by hand: change the time off request in Time Off instead.
- A to-do is visible to its assignees only. Converting it to a task opens it to everyone
  who sees the project: check the note before converting.
- The skills search finds tasks through their assignees, not through the task: a task
  needing a skill nobody assigned has, appears only as unassigned.
