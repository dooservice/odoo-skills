# event — Events Organization

Depends on: barcodes, base_setup, mail, phone_validation, portal, utm.

## `event.event` (defines)

Event

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Event” (required)
- `note` Html “Note” (store, compute=_compute_note)
- `description` Html “Description”
- `active` Boolean
- `user_id` Many2one → `res.users` “Responsible”
- `use_barcode` Boolean (compute=_compute_use_barcode)
- `company_id` Many2one → `res.company` “Company”
- `organizer_id` Many2one → `res.partner` “Organizer”
- `event_type_id` Many2one → `event.type` “Template”
- `event_mail_ids` One2many → `event.mail` “Mail Schedule” (store, compute=_compute_event_mail_ids)
- `tag_ids` Many2many → `event.tag` “Tags” (store, compute=_compute_tag_ids)
- `registration_properties_definition` PropertiesDefinition “Registration Properties”
- `kanban_state` Selection (store, compute=_compute_kanban_state)
- `stage_id` Many2one → `event.stage`
- `seats_max` Integer “Maximum Attendees” (store, compute=_compute_seats_max)
- `seats_limited` Boolean “Limit Attendees” (required, store, compute=_compute_seats_limited)
- `seats_reserved` Integer “Number of Registrations” (readonly, compute=_compute_seats)
- `seats_available` Integer “Available Seats” (readonly, compute=_compute_seats)
- `seats_used` Integer “Number of Attendees” (readonly, compute=_compute_seats)
- `seats_taken` Integer “Number of Taken Seats” (readonly, compute=_compute_seats)
- `registration_ids` One2many → `event.registration` “Attendees”
- `is_multi_slots` Boolean “Is Multi Slots”
- `event_slot_ids` One2many → `event.slot`
- `event_slot_count` Integer “Slots Count” (compute=_compute_event_slot_count)
- `event_ticket_ids` One2many → `event.event.ticket` “Event Ticket” (store, compute=_compute_event_ticket_ids)
- `event_registrations_started` Boolean “Registrations started” (compute=_compute_event_registrations_started)
- `event_registrations_open` Boolean “Registration open” (compute=_compute_event_registrations_open)
- `event_registrations_sold_out` Boolean “Sold Out” (compute=_compute_event_registrations_sold_out)
- `start_sale_datetime` Datetime “Start sale date” (compute=_compute_start_sale_date)
- `date_tz` Selection “Display Timezone” (required, store, compute=_compute_date_tz)
- `date_begin` Datetime “Start Date” (required)
- `date_end` Datetime “End Date” (required)
- `is_ongoing` Boolean “Is Ongoing” (compute=_compute_is_ongoing)
- `is_one_day` Boolean (compute=_compute_field_is_one_day)
- `is_finished` Boolean (compute=_compute_is_finished)
- `address_id` Many2one → `res.partner` “Venue”
- `address_search` Many2one → `res.partner` “Address” (compute=_compute_address_search)
- `address_inline` Char “Venue (formatted for one line uses)” (compute=_compute_address_inline)
- `country_id` Many2one → `res.country` (store, related=address_id.country_id)
- `event_url` Char “Online Event URL” (store, compute=_compute_event_url)
- `event_share_url` Char “Event Share URL” (compute=_compute_event_share_url)
- `lang` Selection “Language”
- `badge_format` Selection “Badge Dimension” (required)
- `badge_image` Image “Badge Background”
- `ticket_instructions` Html “Ticket Instructions” (store, compute=_compute_ticket_instructions)
- `question_ids` Many2many → `event.question` “Questions” (store, compute=_compute_question_ids)
- `general_question_ids` Many2many → `event.question` “General Questions”
- `specific_question_ids` Many2many → `event.question` “Specific Questions”

Public methods: `action_open_slot_calendar`, `action_set_done`, `copy_data`, `default_get`, `get_kiosk_url`

Extension points: `_check_closing_date`, `_check_event_url`, `_check_slots_dates`, `_get_date_range_str`, `_get_default_stage_id`, `_get_external_description`, `_get_external_description_url_encoded`, `_get_ics_file`, `_get_seats_availability`, `_get_tickets_access_hash`

## `event.mail` (defines)

Event Automated Mailing

- `event_id` Many2one → `event.event` “Event” (required, index)
- `sequence` Integer “Display order”
- `interval_nbr` Integer “Interval”
- `interval_unit` Selection “Unit” (required)
- `interval_type` Selection “Trigger ” (required)
- `scheduled_date` Datetime “Schedule Date” (store, compute=_compute_scheduled_date)
- `error_datetime` Datetime “Last Error”
- `last_registration_id` Many2one → `event.registration`
- `mail_registration_ids` One2many → `event.mail.registration`
- `mail_slot_ids` One2many → `event.mail.slot`
- `mail_done` Boolean “Sent” (readonly)
- `mail_state` Selection “Global communication Status” (compute=_compute_mail_state)
- `mail_count_done` Integer “# Sent” (readonly)
- `notification_type` Selection “Send” (compute=_compute_notification_type)
- `template_ref` Reference “Template” (required)

Public methods: `execute`, `run`, `schedule_communications`

Extension points: `_create_missing_mail_registrations`, `_prepare_event_mail_values`

## `event.mail.registration` (defines)

Registration Mail Scheduler

- `scheduler_id` Many2one → `event.mail` (required, index)
- `registration_id` Many2one → `event.registration` (required, index)
- `scheduled_date` Datetime “Scheduled Time” (store, compute=_compute_scheduled_date)
- `mail_sent` Boolean “Mail Sent”

Public methods: `execute`

Extension points: `_get_skip_domain`

## `event.mail.slot` (defines)

Slot Mail Scheduler

- `event_slot_id` Many2one → `event.slot` (required)
- `scheduled_date` Datetime “Schedule Date” (store, compute=_compute_scheduled_date)
- `scheduler_id` Many2one → `event.mail` (required, index)
- `last_registration_id` Many2one → `event.registration`
- `mail_count_done` Integer “# Sent” (readonly)
- `mail_done` Boolean “Sent” (readonly)

## `event.question` (defines)

Event Question

- `title` Char (required)
- `question_type` Selection “Question Type” (required)
- `active` Boolean “Active”
- `event_type_ids` Many2many → `event.type` “Event Types”
- `event_ids` Many2many → `event.event` “Events”
- `event_count` Integer “# Events” (compute=_compute_event_count)
- `is_default` Boolean “Default question”
- `is_reusable` Boolean “Is Reusable” (store, compute=_compute_is_reusable)
- `answer_ids` One2many → `event.question.answer`
- `sequence` Integer
- `once_per_order` Boolean “Ask once per order”
- `is_mandatory_answer` Boolean “Mandatory Answer”

Public methods: `action_event_view`, `action_view_question_answers`, `write`

## `event.question.answer` (defines)

Event Question Answer

- `name` Char “Answer” (required)
- `question_id` Many2one → `event.question` (required, index)
- `sequence` Integer

## `event.registration` (defines)

Event Registration

Inherits: `mail.thread`, `mail.activity.mixin`

- `event_id` Many2one → `event.event` “Event” (required, index)
- `is_multi_slots` Boolean “Is Event Multi Slots” (related=event_id.is_multi_slots)
- `event_slot_id` Many2one → `event.slot` “Slot”
- `event_ticket_id` Many2one → `event.event.ticket` “Ticket Type”
- `active` Boolean
- `barcode` Char “Barcode” (readonly)
- `utm_campaign_id` Many2one → `utm.campaign` (index)
- `utm_source_id` Many2one → `utm.source` (index)
- `utm_medium_id` Many2one → `utm.medium` (index)
- `partner_id` Many2one → `res.partner` “Booked by”
- `name` Char “Attendee Name” (store, compute=_compute_name)
- `email` Char “Email” (store, compute=_compute_email)
- `phone` Char “Phone” (store, compute=_compute_phone)
- `company_name` Char “Company Name” (store, compute=_compute_company_name)
- `date_closed` Datetime “Attended Date” (store, compute=_compute_date_closed)
- `event_begin_date` Datetime “Event Start Date” (compute=_compute_event_begin_date)
- `event_end_date` Datetime “Event End Date” (compute=_compute_event_end_date)
- `event_date_range` Char “Date Range” (compute=_compute_date_range)
- `event_organizer_id` Many2one “Event Organizer” (readonly, related=event_id.organizer_id)
- `event_user_id` Many2one “Event Responsible” (readonly, related=event_id.user_id)
- `company_id` Many2one → `res.company` “Company” (store, related=event_id.company_id)
- `state` Selection “Status” (readonly)
- `registration_answer_ids` One2many → `event.registration.answer` “Attendee Answers”
- `registration_answer_choice_ids` One2many → `event.registration.answer` “Attendee Selection Answers”
- `mail_registration_ids` One2many → `event.mail.registration` “Scheduler Emails” (readonly)
- `registration_properties` Properties “Properties”

Public methods: `action_cancel`, `action_confirm`, `action_send_badge_email`, `action_set_done`, `action_set_draft`, `create`, `default_get`, `register_attendee`, `write`

Extension points: `_check_event_slot`, `_check_event_ticket`, `_check_seats_availability`, `_get_random_barcode`, `_get_registration_summary`

## `event.registration.answer` (defines)

Event Registration Answer

- `question_id` Many2one → `event.question` (required)
- `registration_id` Many2one → `event.registration` (required, index)
- `partner_id` Many2one → `res.partner` (related=registration_id.partner_id)
- `event_id` Many2one → `event.event` (related=registration_id.event_id)
- `question_type` Selection (related=question_id.question_type)
- `value_answer_id` Many2one → `event.question.answer` “Suggested answer”
- `value_text_box` Text “Text answer”

## `event.slot` (defines)

Event Slot

- `event_id` Many2one → `event.event` (required, index)
- `color` Integer “Color”
- `date` Date “Date” (required)
- `date_tz` Selection (related=event_id.date_tz)
- `start_hour` Float “Starting Hour” (required)
- `end_hour` Float “Ending Hour” (required)
- `start_datetime` Datetime “Start Datetime” (store, compute=_compute_datetimes)
- `end_datetime` Datetime “End Datetime” (store, compute=_compute_datetimes)
- `is_sold_out` Boolean “Sold Out” (compute=_compute_is_sold_out)
- `registration_ids` One2many → `event.registration` “Attendees”
- `seats_available` Integer “Available Seats” (readonly, compute=_compute_seats)
- `seats_reserved` Integer “Number of Registrations” (readonly, compute=_compute_seats)
- `seats_taken` Integer “Number of Taken Seats” (readonly, compute=_compute_seats)
- `seats_used` Integer “Number of Attendees” (readonly, compute=_compute_seats)

Extension points: `_check_hours`, `_check_time_range`

## `event.stage` (defines)

Event Stage

- `name` Char “Stage Name” (required)
- `description` Text “Stage description”
- `sequence` Integer “Sequence”
- `fold` Boolean “Folded in Kanban”
- `pipe_end` Boolean “End Stage”

## `event.tag.category` (defines)

Event Tag Category

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `tag_ids` One2many → `event.tag` “Tags”

## `event.tag` (defines)

Event Tag

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `category_id` Many2one → `event.tag.category` “Category” (required, index)
- `category_sequence` Integer “Category Sequence” (store, related=category_id.sequence)
- `color` Integer “Color Index”

## `event.event.ticket` (defines)

Event Ticket

Inherits: `event.type.ticket`

- `event_type_id` Many2one
- `event_id` Many2one → `event.event` “Event” (required, index)
- `company_id` Many2one → `res.company` (related=event_id.company_id)
- `start_sale_datetime` Datetime “Registration Start”
- `end_sale_datetime` Datetime “Registration End”
- `is_launched` Boolean “Are sales launched” (compute=_compute_is_launched)
- `is_expired` Boolean “Is Expired” (compute=_compute_is_expired)
- `sale_available` Boolean “Is Available” (compute=_compute_sale_available)
- `registration_ids` One2many → `event.registration` “Registrations”
- `seats_reserved` Integer “Reserved Seats” (compute=_compute_seats)
- `seats_available` Integer “Available Seats” (compute=_compute_seats)
- `seats_used` Integer “Used Seats” (compute=_compute_seats)
- `seats_taken` Integer “Taken Seats” (compute=_compute_seats)
- `limit_max_per_order` Integer “Limit per Order”
- `is_sold_out` Boolean “Sold Out” (compute=_compute_is_sold_out)
- `color` Char “Color”

Public methods: `default_get`

Extension points: `_get_current_limit_per_order`, `_get_ticket_multiline_description`

## `event.type` (defines)

Event Template

- `name` Char “Event Template” (required)
- `note` Html “Note”
- `sequence` Integer
- `event_type_ticket_ids` One2many → `event.type.ticket` “Tickets”
- `tag_ids` Many2many → `event.tag` “Tags”
- `has_seats_limitation` Boolean “Limited Seats”
- `seats_max` Integer “Maximum Registrations” (store, compute=_compute_seats_max)
- `default_timezone` Selection “Timezone”
- `event_type_mail_ids` One2many → `event.type.mail` “Mail Schedule”
- `ticket_instructions` Html “Ticket Instructions”
- `question_ids` Many2many → `event.question` “Questions”

## `event.type.mail` (defines)

Mail Scheduling on Event Category

- `event_type_id` Many2one → `event.type` “Event Type” (required)
- `interval_nbr` Integer “Interval”
- `interval_unit` Selection “Unit” (required)
- `interval_type` Selection “Trigger” (required)
- `notification_type` Selection “Send” (compute=_compute_notification_type)
- `template_ref` Reference “Template” (required)

Extension points: `_prepare_event_mail_values`

## `event.type.ticket` (defines)

Event Template Ticket

- `sequence` Integer “Sequence”
- `name` Char “Name” (required)
- `description` Text “Description”
- `event_type_id` Many2one → `event.type` “Event Category” (required)
- `seats_limited` Boolean “Limit Attendees” (readonly, store, compute=_compute_seats_limited)
- `seats_max` Integer “Maximum Attendees”

Extension points: `_get_event_ticket_fields_whitelist`

## `mail.template` (extends)


Public methods: `unlink`

## `res.config.settings` (extends)

- `google_maps_static_api_key` Char “Google Maps API key” (store, compute=_compute_maps_static_api_key)
- `google_maps_static_api_secret` Char “Google Maps API secret” (store, compute=_compute_maps_static_api_secret)
- `module_event_sale` Boolean “Tickets with Sale”
- `module_pos_event` Boolean “Tickets with PoS”
- `module_website_event_track` Boolean “Tracks and Agenda”
- `module_website_event_track_live` Boolean “Live Mode”
- `module_website_event_track_quiz` Boolean “Quiz on Tracks”
- `module_website_event_exhibitor` Boolean “Advanced Sponsors”
- `use_event_barcode` Boolean “Use Event Barcode”
- `barcode_nomenclature_id` Many2one → `barcode.nomenclature` (related=company_id.nomenclature_id)
- `module_website_event_sale` Boolean “Online Ticketing”
- `module_event_booth` Boolean “Booth Management”
- `use_google_maps_static_api` Boolean “Google Maps static API”

Public methods: `create`, `write`

Extension points: `_check_google_maps_static_api_secret`

## `res.partner` (extends)

- `event_count` Integer “# Events” (compute=_compute_event_count)
- `static_map_url` Char (compute=_compute_static_map_url)
- `static_map_url_is_valid` Boolean (compute=_compute_static_map_url_is_valid)

Public methods: `action_event_view`
