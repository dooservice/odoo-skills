# project_sms — Project - SMS

Depends on: project, sms.

## `project.project` (extends)


Public methods: `create`, `write`

## `project.project.stage` (extends)

- `sms_template_id` Many2one → `sms.template` “SMS Template”

## `project.task` (extends)


Public methods: `create`, `write`

## `project.task.type` (extends)

- `sms_template_id` Many2one → `sms.template` “SMS Template”
