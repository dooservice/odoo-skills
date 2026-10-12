# pos_sms — POS - SMS

Depends on: point_of_sale, sms.

## `pos.config` (extends)

- `sms_receipt_template_id` Many2one → `sms.template` “Sms Receipt template”

## `pos.order` (extends)


Public methods: `action_sent_message_on_sms`

## `res.config.settings` (extends)

- `pos_sms_receipt_template_id` Many2one → `sms.template` (related=pos_config_id.sms_receipt_template_id)
