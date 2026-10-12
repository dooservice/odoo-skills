# website_event_questions — Questions on Events

Depends on: website_event.

## `event.type` (extends)

- `question_ids` One2many → `event.question` “Questions”

## `event.event` (extends)

- `question_ids` One2many → `event.question` (store, compute=_compute_question_ids)
- `general_question_ids` One2many → `event.question`
- `specific_question_ids` One2many → `event.question`

## `event.question` (defines)

Event Question

- `title` Char (required)
- `question_type` Selection “Question Type” (required)
- `event_type_id` Many2one → `event.type`
- `event_id` Many2one → `event.event`
- `answer_ids` One2many → `event.question.answer`
- `sequence` Integer
- `once_per_order` Boolean “Ask once per order”
- `is_mandatory_answer` Boolean “Mandatory Answer”

Public methods: `action_view_question_answers`, `write`

## `event.question.answer` (defines)

Event Question Answer

- `name` Char “Answer” (required)
- `question_id` Many2one → `event.question` (required)
- `sequence` Integer

## `event.registration` (extends)

- `registration_answer_ids` One2many → `event.registration.answer` “Attendee Answers”

## `event.registration.answer` (defines)

Event Registration Answer

- `question_id` Many2one → `event.question` (required)
- `registration_id` Many2one → `event.registration` (required)
- `partner_id` Many2one → `res.partner` (related=registration_id.partner_id)
- `event_id` Many2one → `event.event` (related=registration_id.event_id)
- `question_type` Selection (related=question_id.question_type)
- `value_answer_id` Many2one → `event.question.answer` “Suggested answer”
- `value_text_box` Text “Text answer”

Public methods: `name_get`
