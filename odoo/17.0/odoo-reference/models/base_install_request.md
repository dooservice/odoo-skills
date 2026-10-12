# base_install_request — Base - Module Install Request

Depends on: mail.

## `ir.module.module` (extends)


Public methods: `action_open_install_request`

## `base.module.install.request` (defines)

Module Activation Request

- `module_id` Many2one → `ir.module.module` “Module” (required, readonly)
- `user_id` Many2one → `res.users` (required)
- `user_ids` Many2many → `res.users` “Send to:” (compute=_compute_user_ids)
- `body_html` Html “Body”

Public methods: `action_send_request`

## `base.module.install.review` (defines)

Module Activation Review

- `module_id` Many2one → `ir.module.module` “Module” (required, readonly)
- `module_ids` Many2many → `ir.module.module` “Depending Apps” (compute=_compute_modules_description)
- `modules_description` Html (compute=_compute_modules_description)

Public methods: `action_install_module`

Extension points: `_get_depending_apps`
