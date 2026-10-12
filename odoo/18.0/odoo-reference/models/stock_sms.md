# stock_sms — Stock - SMS

Depends on: stock, sms.

## `res.company` (extends)

- `stock_move_sms_validation` Boolean “SMS Confirmation”
- `stock_sms_confirmation_template_id` Many2one → `sms.template` “SMS Template”
- `has_received_warning_stock_sms` Boolean

## `res.config.settings` (extends)

- `stock_move_sms_validation` Boolean “SMS Validation with stock move” (related=company_id.stock_move_sms_validation)
- `stock_sms_confirmation_template_id` Many2one (related=company_id.stock_sms_confirmation_template_id)

## `stock.picking` (extends)


Extension points: `_action_generate_warn_sms_wizard`, `_check_warn_sms`

## `confirm.stock.sms` (defines)

Confirm Stock SMS

- `pick_ids` Many2many → `stock.picking`

Public methods: `dont_send_sms`, `send_sms`
