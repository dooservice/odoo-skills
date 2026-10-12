# project_todo — To-Do

Depends on: project.

## `mail.activity.type` (extends)

- `category` Selection

## `project.task` (extends)


Public methods: `action_convert_to_task`, `create`

## `mail.activity.todo.create` (defines)

Create activity and todo at the same time

- `summary` Char
- `date_deadline` Date “Due Date” (required, index)
- `user_id` Many2one → `res.users` (required, readonly)
- `note` Html

Public methods: `create_todo_activity`
