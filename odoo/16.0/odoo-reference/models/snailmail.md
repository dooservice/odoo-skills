# snailmail — Snail Mail

Depends on: iap_mail, mail.

## `ir.actions.report` (extends)


Public methods: `get_paperformat`, `retrieve_attachment`

## `mail.message` (extends)

- `snailmail_error` Boolean “Snailmail message in error” (compute=_compute_snailmail_error)
- `letter_ids` One2many → `snailmail.letter`
- `message_type` Selection

Public methods: `cancel_letter`, `send_letter`

## `mail.notification` (extends)

- `notification_type` Selection
- `letter_id` Many2one → `snailmail.letter` “Snailmail Letter”
- `failure_type` Selection

## `mail.thread` (extends)


Public methods: `notify_cancel_by_type`

## `res.company` (extends)

- `snailmail_color` Boolean “Color”
- `snailmail_cover` Boolean “Add a Cover Page”
- `snailmail_duplex` Boolean “Both sides”

## `res.config.settings` (extends)

- `snailmail_color` Boolean “Print In Color” (related=company_id.snailmail_color)
- `snailmail_cover` Boolean “Add a Cover Page” (related=company_id.snailmail_cover)
- `snailmail_duplex` Boolean “Print Both sides” (related=company_id.snailmail_duplex)

## `res.partner` (extends)


Public methods: `write`

Extension points: `_get_address_format`, `_get_country_name`

## `snailmail.letter` (defines)

Snailmail Letter

- `user_id` Many2one → `res.users`
- `model` Char “Model” (required)
- `res_id` Integer “Document ID” (required)
- `partner_id` Many2one → `res.partner` “Recipient” (required)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `report_template` Many2one → `ir.actions.report`
- `attachment_id` Many2one → `ir.attachment` “Attachment”
- `attachment_datas` Binary “Document” (related=attachment_id.datas)
- `attachment_fname` Char “Attachment Filename” (related=attachment_id.name)
- `color` Boolean “Color”
- `cover` Boolean “Cover Page”
- `duplex` Boolean “Both side”
- `state` Selection (required, readonly)
- `error_code` Selection “Error”
- `info_msg` Html “Information”
- `display_name` Char “Display Name” (compute=_compute_display_name)
- `reference` Char “Related Record” (readonly, compute=_compute_reference)
- `message_id` Many2one → `mail.message` “Snailmail Status Message”
- `notification_ids` One2many → `mail.notification`
- `street` Char “Street”
- `street2` Char “Street2”
- `zip` Char “Zip”
- `city` Char “City”
- `state_id` Many2one → `res.country.state` “State”
- `country_id` Many2one → `res.country` “Country”

Public methods: `cancel`, `create`, `onchange`, `snailmail_print`, `write`

Extension points: `_get_error_message`, `_get_failure_type`

## `snailmail.confirm` (defines)

Snailmail Confirm

- `model_name` Char

Public methods: `action_cancel`, `action_confirm`, `action_open`, `show_warning`

## `snailmail.letter.format.error` (defines)

Format Error Sending a Snailmail Letter

- `message_id` Many2one → `mail.message`
- `snailmail_cover` Boolean “Add a Cover Page”

Public methods: `cancel_letter_action`, `update_resend_action`

## `snailmail.letter.missing.required.fields` (defines)

Update address of partner

- `partner_id` Many2one → `res.partner`
- `letter_id` Many2one → `snailmail.letter`
- `street` Char “Street”
- `street2` Char “Street2”
- `zip` Char “Zip”
- `city` Char “City”
- `state_id` Many2one → `res.country.state` “State”
- `country_id` Many2one → `res.country` “Country”

Public methods: `default_get`, `update_address_cancel`, `update_address_save`
