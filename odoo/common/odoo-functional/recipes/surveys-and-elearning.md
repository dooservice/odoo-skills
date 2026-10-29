# Surveys and eLearning

A survey (`survey.survey`) is a set of questions, grouped in sections, answered online
by invited or anonymous participants; each participation is a `survey.user_input`.
Surveys also score quizzes, issue certifications and run live sessions in a room. A
course (`slide.channel`, app eLearning, module `website_slides`) is a published series of
contents (`slide.slide`: documents, videos, articles, quizzes) that members follow on the
website, earning points (karma). Courses can be sold (`website_sale_slides`), end with a
certification survey (`website_slides_survey`) and have a forum (`website_slides_forum`).
Survey questions in recruitment and appraisals belong to those apps' recipes.

## Before you start

- Apps: `survey`; `website_slides` (it installs `website`). Bridges, each a setting:
  `module_website_sale_slides` (Sell on eCommerce), `module_website_slides_survey`
  (Certifications), `module_website_slides_forum` (Forum), `module_mass_mailing_slides`
  (Mailing), in eLearning ‣ Configuration ‣ Settings. 19.0+ `survey_crm` installs itself
  with `crm`. Ask before installing any.
- Read first:

```python
print(env['survey.survey'].search_read([], ['title', 'access_mode', 'scoring_type', 'certification', 'active']))
print(env['slide.channel'].search_read([], ['name', 'channel_type', 'enroll', 'visibility', 'is_published', 'members_count']))
```

## The standard flow

### A survey

1. **Create the survey.** Surveys ‣ Surveys ‣ New: title, then Add a section and Add a
   question in the Questions tab.

   ```python
   survey = env['survey.survey'].create({
       'title': 'Customer satisfaction',
       'access_mode': 'public',
       'questions_layout': 'page_per_section',
       'question_and_page_ids': [
           (0, 0, {'title': 'Your experience', 'is_page': True}),
           (0, 0, {'title': 'How satisfied are you?', 'question_type': 'simple_choice',
                   'constr_mandatory': True,
                   'suggested_answer_ids': [(0, 0, {'value': 'Very satisfied'}),
                                            (0, 0, {'value': 'Not satisfied'})]}),
           (0, 0, {'title': 'Comments', 'question_type': 'text_box'}),
       ],
   })
   env.cr.commit()
   ```

   Leaves an active survey. `question_type`: `simple_choice`, `multiple_choice`,
   `text_box`, `char_box`, `numerical_box`, `date`, `datetime`, `matrix`; 18.0+ also
   `scale`. `access_mode`: `public` (anyone with the link) or `token` (invited only).
   17.0+ `survey_type` (`survey`, `live_session`, `assessment`, `custom`, default
   `custom`) only presets the options.

2. **Test it.** The Test button answers as the current user without counting.

3. **Share or invite.** Share button: the link, or emails to contacts with a deadline.

   ```python
   partners = env['res.partner'].search([('email', 'in', ['customer.a@example.com'])])
   env['survey.invite'].create({'survey_id': survey.id, 'partner_ids': [(6, 0, partners.ids)]}).action_invite()
   env.cr.commit()
   ```

   Leaves one participation per contact in `new`, with a personal link, and the email
   sent.

4. **Read the answers.** The survey's Participations smart button (Participants from
   19.0) and See results; Surveys ‣ Participations lists them all.

   ```python
   print(env['survey.user_input'].read_group([('survey_id', '=', survey.id)], ['state'], ['state']))
   ```

   `state`: `new`, `in_progress`, `done`.

### A course

1. **Create the course.** eLearning ‣ Courses ‣ Courses ‣ New: name, type, who can
   enroll, who sees it.

   ```python
   course = env['slide.channel'].create({
       'name': 'Product A basics',
       'channel_type': 'training',
       'enroll': 'public',
       'visibility': 'public',
   })
   env.cr.commit()
   ```

   `channel_type`: `training` (in order, progress tracked) or `documentation`.
   `enroll`: `public`, `invite`; `payment` with `website_sale_slides`. `visibility`:
   `public`, `members`; 17.0+ `connected`; 19.0+ `link`.

2. **Add contents.** The course's Content tab: Add Section, Add Content.

   ```python
   section = env['slide.slide'].create({'channel_id': course.id, 'name': 'Getting started', 'is_category': True})
   env['slide.slide'].create([
       {'channel_id': course.id, 'name': 'Overview', 'slide_category': 'article',
        'html_content': '<p>What Product A does.</p>', 'is_published': True, 'is_preview': True},
       {'channel_id': course.id, 'name': 'Check', 'slide_category': 'quiz', 'is_published': True,
        'question_ids': [(0, 0, {'question': 'Is Product A waterproof?', 'answer_ids': [
            (0, 0, {'text_value': 'Yes', 'is_correct': True}), (0, 0, {'text_value': 'No'})]})]},
   ])
   env.cr.commit()
   ```

   `slide_category`: `document` (PDF in `binary_content` or a Google Drive link),
   `infographic`, `video` (`url`), `article` (`html_content`), `quiz`; `certification`
   with `website_slides_survey`. `is_preview` shows it to visitors who have not
   enrolled.

3. **Publish.** The course form's Go to Website, Published switch.

   ```python
   course.write({'is_published': True})
   env.cr.commit()
   print(course.website_url)
   ```

4. **Enroll attendees.** Visitors join on the website (`enroll='public'`); for others,
   the course's Add Attendees (17.0+) or Invite button.

   ```python
   course._action_add_members(partners)
   env.cr.commit()
   ```

   Leaves a `slide.channel.partner` per attendee; 17.0+ `member_status` `joined`, then
   `ongoing` and `completed` as they progress (`invited` for invitations).

## Variations

- **Scored quiz.** `scoring_type` `scoring_with_answers` (shows the right answers at the
  end), `scoring_without_answers`; 17.0+ `scoring_with_answers_after_page`. Mark
  correct answers (`is_correct`, `answer_score`) and set `scoring_success_min` (%).
- **Certification.** `certification=True` on a scored survey: a PDF certificate on
  success, `certification_mail_template_id` to send it, `certification_give_badge` for
  a badge. With `website_slides_survey`, a course content of category `certification`
  points to it (`survey_id`).
- **Attempts and time.** `is_attempts_limited` with `attempts_limit` (needs `token` or
  login), `is_time_limited` with `time_limit` (minutes).
- **Live session.** `survey_type='live_session'` (17.0+) or the Create Live Session
  button: the host shows one question at a time to a room joining with a short code;
  `action_start_session`, `action_end_session`.
- **Leads from answers** (19.0+, `survey_crm`). Tick Lead creation (`generate_lead`) on
  suggested answers; a participant who chooses one creates a lead for the survey's
  `team_id`.
- **Sell a course** (`website_sale_slides`). `enroll='payment'` and a product of type
  course (`detailed_type='course'` up to 17.0, `service_tracking='course'` 18.0+).
  Paying the order on the website enrolls the buyer.
- **Course forum** (`website_slides_forum`). `forum_id` on the course; the forum is
  configured as in `website-content.md`.
- **Prerequisites** (17.0+). `prerequisite_channel_ids`: courses to complete first.
- **Mail attendees** (`mass_mailing_slides`). The course's Contact Attendees button:
  `email-and-sms-marketing.md`.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| `survey_type` | no | yes | yes | yes | yes |
| `scale` question | no | no | yes | yes | yes |
| `scoring_with_answers_after_page` | no | yes | yes | yes | yes |
| Participations menu name | Participations | same | same | Participants | same |
| `survey_crm` | no | no | no | yes | yes |
| Course `visibility` | `public`, `members` | adds `connected` | same | adds `link` | same |
| `member_status`, Add Attendees | no | yes | yes | yes | yes |
| Course product | `detailed_type='course'` | same | `service_tracking='course'` | same | same |

## Verify

```python
print(survey.answer_count, survey.access_mode)
print(course.is_published, course.total_slides, course.members_count, course.website_url)
```

Then ask the user to open the survey link and the course page in a private window.

## Pitfalls

- A `public` survey can be answered by anyone with the link, many times: use `token`
  and invitations when answers must be one per person.
- Changing questions after people answered breaks the results of those questions;
  copy the survey instead.
- A course with `enroll='invite'` and `visibility='public'` is listed but cannot be
  joined: say so to the user.
- Course videos and documents from external links depend on that service's sharing
  settings; a private Drive file shows an error to attendees.
