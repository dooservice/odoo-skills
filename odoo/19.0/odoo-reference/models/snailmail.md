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

- `snailmail_color` Boolean
- `snailmail_cover` Boolean “Add a Cover Page”
- `snailmail_duplex` Boolean “Both sides”

## `res.config.settings` (extends)

- `snailmail_color` Boolean “Print In Color” (related=company_id.snailmail_color)
- `snailmail_cover` Boolean “Add a Cover Page” (related=company_id.snailmail_cover)
- `snailmail_duplex` Boolean “Print Both sides” (related=company_id.snailmail_duplex)
- `snailmail_cover_readonly` Boolean (compute=_compute_cover_readonly)

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
- `reference` Char “Related Record” (readonly, compute=_compute_reference)
- `message_id` Many2one → `mail.message` “Snailmail Status Message”
- `notification_ids` One2many → `mail.notification`
- `street` Char “Street”
- `street2` Char “Street2”
- `zip` Char “Zip”
- `city` Char “City”
- `state_id` Many2one → `res.country.state` “State”
- `country_id` Many2one → `res.country` “Country”

Public methods: `cancel`, `create`, `snailmail_print`, `write`

Extension points: `_get_cover_address_split`, `_get_error_message`, `_get_failure_type`
