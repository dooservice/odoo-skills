# sms_twilio — Twilio SMS

Depends on: sms.

## `mail.notification` (extends)

- `failure_type` Selection

## `res.company` (extends)

- `sms_provider` Selection “SMS Provider”
- `sms_twilio_account_sid` Char “Account SID”
- `sms_twilio_auth_token` Char “Auth Token”
- `sms_twilio_number_ids` One2many → `sms.twilio.number`

Extension points: `_action_open_sms_twilio_account_manage`, `_get_sms_api_class`

## `res.config.settings` (extends)

- `sms_provider` Selection (required, related=company_id.sms_provider)

Public methods: `action_open_sms_twilio_account_manage`

## `sms.composer` (extends)


Extension points: `_prepare_mass_sms_values`

## `sms.sms` (extends)

- `sms_twilio_sid` Char (related=sms_tracker_id.sms_twilio_sid)
- `record_company_id` Many2one → `res.company`
- `failure_type` Selection

Public methods: `create`

Extension points: `_get_send_batch_size`, `_get_sms_company`

## `sms.tracker` (extends)

- `sms_twilio_sid` Char “Twilio SMS SID” (readonly)

## `sms.twilio.number` (defines)

Twilio Number

- `company_id` Many2one → `res.company` “Company” (required)
- `sequence` Integer
- `number` Char “Twilio Number” (required)
- `country_id` Many2one → `res.country` “Country” (required)
- `country_code` Char “Country Code” (related=country_id.code)

## `sms.twilio.account.manage` (defines)

SMS Twilio Connection Wizard

- `company_id` Many2one → `res.company` (required, readonly)
- `sms_provider` Selection (related=company_id.sms_provider)
- `sms_twilio_account_sid` Char (related=company_id.sms_twilio_account_sid)
- `sms_twilio_auth_token` Char (related=company_id.sms_twilio_auth_token)
- `sms_twilio_number_ids` One2many (related=company_id.sms_twilio_number_ids)
- `test_number` Char “Test Number”

Public methods: `action_reload_numbers`, `action_save`, `action_send_test`
