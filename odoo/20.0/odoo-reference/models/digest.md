# digest — KPI Digests

Depends on: mail, portal, resource.

## `digest.digest` (defines)

Digest

- `name` Char “Name” (required)
- `user_ids` Many2many → `res.users` “Recipients”
- `periodicity` Selection “Periodicity” (required)
- `next_run_date` Date “Next Mailing Date”
- `currency_id` Many2one “Currency” (related=company_id.currency_id)
- `company_id` Many2one → `res.company` “Company”
- `available_fields` Char (compute=_compute_available_fields)
- `is_subscribed` Boolean “Is user subscribed” (compute=_compute_is_subscribed)
- `state` Selection “Status” (readonly)
- `kpi_res_users_connected` Boolean “Connected Users”
- `kpi_res_users_connected_value` Integer (compute=_compute_kpi_res_users_connected_value)
- `kpi_mail_message_total` Boolean “Messages Sent”
- `kpi_mail_message_total_value` Integer (compute=_compute_kpi_mail_message_total_value)

Public methods: `action_activate`, `action_deactivate`, `action_launch_test_wizard`, `action_send`, `action_send_manual`, `action_set_periodicity`, `action_subscribe`, `action_unsubscribe`, `create`

Extension points: `_action_send`, `_action_send_to_user`, `_action_subscribe_users`, `_action_unsubscribe_users`, `_check_daily_logs`, `_get_all_kpi_fields`, `_get_company_field`, `_get_kpi_compute_parameters`, `_get_kpi_custom_settings`, `_get_margin_value`, `_get_next_periodicity`, `_get_next_run_date`, `_get_unsubscribe_token`

## `digest.tip` (defines)

Digest Tip

- `sequence` Integer “Sequence”
- `name` Char “Name”
- `user_ids` Many2many → `res.users` “Recipients”
- `tip_description` Html “Tip description”
- `group_id` Many2one → `res.groups` “Authorized Group”

## `res.config.settings` (extends)

- `digest_emails` Boolean “Digest Emails”
- `digest_id` Many2one → `digest.digest` “Digest Email”

## `res.users` (extends)

- `digest_ids` Many2many → `digest.digest` “Digests”

Public methods: `create`

## `digest.test` (defines)

Sample Digest Wizard

- `digest_id` Many2one → `digest.digest` “Digest” (required)
- `user_ids` Many2many → `res.users` “Recipients”

Public methods: `send_mail_test`
