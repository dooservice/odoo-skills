# website_event_track_quiz — Quizzes on Tracks

Depends on: website_profile, website_event_track.

## `event.event` (extends)


## `event.quiz` (defines)

Quiz

- `name` Char “Name” (required)
- `question_ids` One2many → `event.quiz.question` “Questions”
- `event_track_id` Many2one → `event.track` (readonly)
- `event_id` Many2one → `event.event` (readonly, store, related=event_track_id.event_id)
- `repeatable` Boolean “Unlimited Tries”

## `event.quiz.question` (defines)

Content Quiz Question

- `name` Char “Question” (required)
- `sequence` Integer “Sequence”
- `quiz_id` Many2one → `event.quiz` (required)
- `correct_answer_id` One2many → `event.quiz.answer` (compute=_compute_correct_answer_id)
- `awarded_points` Integer “Number of Points” (compute=_compute_awarded_points)
- `answer_ids` One2many → `event.quiz.answer` “Answer”

Extension points: `_check_answers_integrity`

## `event.quiz.answer` (defines)

Question's Answer

- `sequence` Integer “Sequence”
- `question_id` Many2one → `event.quiz.question` “Question” (required)
- `text_value` Char “Answer” (required)
- `is_correct` Boolean “Correct”
- `comment` Text “Extra Comment”
- `awarded_points` Integer “Points”

## `event.track` (extends)

- `quiz_id` Many2one → `event.quiz` “Quiz” (store, compute=_compute_quiz_id)
- `quiz_ids` One2many → `event.quiz` “Quizzes”
- `quiz_questions_count` Integer “# Quiz Questions” (compute=_compute_quiz_questions_count)
- `is_quiz_completed` Boolean “Is Quiz Done” (compute=_compute_quiz_data)
- `quiz_points` Integer “Quiz Points” (compute=_compute_quiz_data)

Public methods: `action_add_quiz`, `action_view_quiz`

## `event.track.visitor` (extends)

- `quiz_completed` Boolean “Completed”
- `quiz_points` Integer “Quiz Points”
