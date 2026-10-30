# Recruitment

A job position (`hr.job`) receives applications (`hr.applicant`) from the website, by
email or typed in by a recruiter. Each application moves through the recruitment stages
(`hr.recruitment.stage`): interviews are calendar meetings, an interview form is a survey
sent to the applicant, and the application ends hired (in a stage marked as hired, then
turned into an employee) or refused with a refuse reason. Needs `hr_recruitment`; the
optional parts are `hr_recruitment_skills` (skills of the applicant and match against the
job), `hr_recruitment_survey` (interview forms) and `website_hr_recruitment` (job pages
and the apply form). Employees themselves are in
[employees-and-expenses.md](employees-and-expenses.md). CV scanning (`hr_recruitment_extract`),
job board posting and SMS are Enterprise or paid services and left out. 18.0 adds a
candidate (`hr.candidate`) that holds the person and has one application per job; 19.0
removes it again: check `## Versions` before every step.

**At a glance**

- Apps: `hr_recruitment`; `hr_recruitment_skills`, `hr_recruitment_survey`,
  `website_hr_recruitment` when needed.
- Names that change by version: the person is `hr.candidate` in 18.0 only
  (`candidate_id`), on the application otherwise; application `name` required up to 17.0,
  removed 18.0+; recruiter `user_id` up to 19.0, `recruiter_id` (employees) 20.0; meeting
  button `action_makeMeeting` up to 17.0, `action_create_meeting` 18.0+; employee link
  `emp_id` up to 17.0, `employee_id` 18.0+; interview answer `response_id` 16.0,
  `response_ids` 17.0+; job URL `/jobs/detail/<job>` 16.0, `/jobs/<job>` 17.0+; job skills
  `skill_ids` 18.0, `job_skill_ids` 19.0+; talent pools 19.0+.
- Sections: Before you start; The standard flow (1 job position, 2 stages, 3 application,
  4 interview, 5 interview form (optional, `hr_recruitment_survey`), 6 move through the
  stages, 7 refuse, 8 hire, 9 create the employee); Variations; Versions; Verify;
  Pitfalls.

## Before you start

- Settings (Recruitment ‣ Configuration ‣ Settings): `module_website_hr_recruitment`
  (Online Posting), `module_hr_recruitment_survey` (Interview Forms). Access: Recruitment
  Officer (`hr_recruitment.group_hr_recruitment_user`) or Administrator; a user listed as
  interviewer on a job or application gets Interviewer
  (`hr_recruitment.group_hr_recruitment_interviewer`) and sees only those applications.
- Read first:

```python
print(env['hr.job'].search_read([], ['name', 'department_id', 'no_of_recruitment', 'interviewer_ids', 'company_id']))
print(env['hr.recruitment.stage'].search_read([], ['sequence', 'name', 'job_ids', 'fold', 'hired_stage', 'template_id'], order='sequence'))
print(env['hr.applicant.refuse.reason'].search_read([], ['name', 'template_id']))
print(env['hr.applicant'].read_group([], ['job_id'], ['job_id']))
print(env['ir.module.module'].search_read([('name', 'like', 'recruitment')], ['name', 'state']))
```

## The standard flow

1. **Job position.** Recruitment ‣ Applications ‣ By Job Positions ‣ New.

   ```python
   job = env['hr.job'].create({
       'name': '<job position>', 'department_id': department.id, 'no_of_recruitment': 1,
       'interviewer_ids': [(6, 0, interviewer_user.ids)], 'company_id': company.id,
       'recruiter_id': recruiter_employee.id,
   })
   env.cr.commit()
   ```

   This is 20.0, where the recruiter is an employee. In 16.0-19.0 the recruiter is a
   user: write `'user_id': recruiter_user.id` instead of `recruiter_id`.

   `no_of_recruitment` is the Target (number of new employees expected). The interviewers
   get the Interviewer group on save. The job's email alias (`alias_name`) turns every
   email it receives into an application for this job.

2. **Stages.** Recruitment ‣ Configuration ‣ Job Positions ‣ Stages. Odoo ships New (17.0+), Initial
   Qualification (20.0: Qualification), First Interview, Second Interview, Contract
   Proposal and Contract Signed; only Contract Signed has `hired_stage`.

   ```python
   env['hr.recruitment.stage'].create({
       'name': '<stage>', 'sequence': 25, 'job_ids': [(6, 0, job.ids)],   # empty job_ids: every job
       'template_id': False,                     # an hr.applicant mail template sent on entering the stage
   })
   ```

   A stage with `fold` is collapsed in the kanban; the first unfolded stage receives new
   applications. Moving an application into a `hired_stage` sets its hire date.

3. **Application.** Recruitment ‣ Applications ‣ By Job Positions, open the job, New
   (18.0: pick or create the candidate first, Applications ‣ Candidates).

   19.0, 20.0:

   ```python
   applicant = env['hr.applicant'].create({
       'job_id': job.id, 'partner_name': '<applicant name>', 'email_from': '<email>',
       'interviewer_ids': [(6, 0, interviewer_user.ids)],
   })
   env.cr.commit()
   print(applicant.stage_id.name, applicant.application_status)
   ```

   18.0, the person is a candidate:

   ```python
   candidate = env['hr.candidate'].create({'partner_name': '<applicant name>', 'email_from': '<email>'})
   applicant = env['hr.applicant'].create({
       'job_id': job.id, 'candidate_id': candidate.id,
       'interviewer_ids': [(6, 0, interviewer_user.ids)],
   })
   env.cr.commit()
   print(applicant.stage_id.name, applicant.application_status)
   ```

   16.0, 17.0: as in 19.0, plus the required subject
   `'name': '<applicant name> - <job position>'`.

   Leaves it in the first stage of the job, `application_status` `ongoing`. Recruiter,
   department and company come from the job.

4. **Interview.** On the application, the Meeting smart button (calendar) ‣ New.

   ```python
   event = env['calendar.event'].create({
       'name': '<applicant name> - First Interview', 'applicant_id': applicant.id,
       'start': '<YYYY-MM-DD HH:MM:SS>', 'stop': '<YYYY-MM-DD HH:MM:SS>',
       'partner_ids': [(6, 0, (applicant.partner_id | interviewer_user.partner_id).ids)],
   })
   ```

   The button (`action_makeMeeting` in 16.0, 17.0; `action_create_meeting` from 18.0)
   creates the applicant's contact if missing and invites it, the department manager and
   the recruiter. The meeting appears on the application (`meeting_ids`); in 18.0 also on
   the candidate. Invitations need an outgoing mail server.

5. **Interview form (optional, `hr_recruitment_survey`).** On the job, Interview Form
   (`survey_id`), or Create to start a new one; then on the application, Send Interview.

   ```python
   survey = env['survey.survey'].create({'title': 'Interview Form: <job position>', 'survey_type': 'recruitment'})
   env['survey.question'].create({'survey_id': survey.id, 'title': '<question>', 'question_type': 'text_box'})
   job.survey_id = survey
   action = applicant.action_send_survey()
   env[action['res_model']].with_context(action['context']).create({}).action_invite()
   env.cr.commit()
   ```

   This is 18.0-20.0. In 16.0, 17.0 the survey has no `recruitment` type: leave
   `survey_type` out. The form needs at least one question. It creates the applicant's answer
   (`response_id` in 16.0, `response_ids` from 17.0) and posts the invitation in the
   chatter. See Results / Print Interview prints the answer once done.

6. **Move through the stages.** Drag the card in the kanban, or click the stage in the
   status bar.

   ```python
   applicant.stage_id = env.ref('hr_recruitment.stage_job2')        # First Interview
   applicant.write({'salary_expected': 0.0, 'salary_proposed': 0.0, 'availability': '<YYYY-MM-DD>'})
   ```

   The stage's mail template, when set, is sent on entering it. Use the kanban state
   (`kanban_state`: `normal`, `done`, `blocked`; 19.0+ also `waiting`) to say the
   applicant is ready for the next stage or blocked.

7. **Refuse.** Refuse on the application: a refuse reason, and Send Email to notify the
   applicant with the reason's template.

   ```python
   reason = env['hr.applicant.refuse.reason'].search([('name', '=', 'Does not fit the job requirements')], limit=1)
   env['applicant.get.refuse.reason'].create({
       'refuse_reason_id': reason.id, 'applicant_ids': [(6, 0, other_applicant.ids)], 'send_mail': False,
   }).action_refuse_reason_apply()
   ```

   Leaves it archived with `refuse_reason_id` set, `application_status` `refused`. From
   18.0 the wizard can also refuse the duplicates (same email or phone). Restore puts it
   back in the first stage (`reset_applicant`).

8. **Hire.** Move the application to Contract Signed.

   ```python
   hired_stage = env['hr.recruitment.stage'].search(
       [('hired_stage', '=', True), '|', ('job_ids', '=', False), ('job_ids', 'in', job.ids)], limit=1)
   applicant.stage_id = hired_stage
   env.cr.commit()
   print(applicant.date_closed, applicant.application_status)
   ```

   Sets `date_closed` (Hire Date) and `application_status` `hired`; the job counts it in
   `no_of_hired_employee`.

9. **Create the employee.** Create Employee on the hired application (18.0: on the
   application or the candidate). Then complete the employee as in
   [employees-and-expenses.md](employees-and-expenses.md).

   17.0-20.0:

   ```python
   action = applicant.create_employee_from_applicant()
   employee = env['hr.employee'].browse(action['res_id'])
   env.cr.commit()
   print(employee.name, employee.job_id.name, employee.department_id.name)
   ```

   16.0, the button returns an unsaved form with defaults:

   ```python
   action = applicant.create_employee_from_applicant()
   employee = env['hr.employee'].with_context(action['context']).create({})
   env.cr.commit()
   print(employee.name, employee.job_id.name, employee.department_id.name)
   ```

   Creates the applicant's contact if missing and an employee with the job, department,
   private address and, from 19.0, the application's attachments. The application links
   to it (`emp_id` in 16.0, 17.0; `employee_id` from 18.0). In 16.0 the button only opens
   a prefilled employee form: save it.

## Variations

- Applications by email: each job has an alias (`alias_name`); a received email creates
  an application in the job's first stage with the email's attachments.
- Online job page (`website_hr_recruitment`): on the job, Go to Website and publish it
  (`website_published`), or Website ‣ Content ‣ Jobs. The page is `/jobs/<job>` (16.0:
  `/jobs/detail/<job>`), the apply form `/jobs/apply/<job>`; a submission creates the
  application in the first unfolded stage (18.0: and its candidate, reused when email
  and phone both match). `website_description` is the page's text, `job_details` (Process Details) the
  extra text of the apply page. 20.0 can schedule the publication (`publish_on`). Archiving a
  job unpublishes it (19.0+). Recruitment ‣ Configuration ‣ UTMs ‣ Sources gives one
  tracked link per source (`hr.recruitment.source.url`).
- Skills (`hr_recruitment_skills`): the applicant's Skills tab (`applicant_skill_ids`;
  18.0: `candidate_skill_ids` on the candidate), with the skill types of
  Recruitment ‣ Configuration ‣ Employees ‣ Skill Types (16.0: Employees ‣ Configuration
  ‣ Skill Types). From 18.0 the job lists its expected skills (18.0 `skill_ids`; 19.0+
  `job_skill_ids` with levels, and an `expected_degree`), and Search Matching
  Applicants (18.0: Candidates) on the job lists the best matches with their score.
  Skill types and levels are described in
  [skills-and-certifications.md](skills-and-certifications.md).
- Talent pools (19.0+): Applications ‣ By Talent Pools; Add to Pool on an application
  copies it into a pool (`hr.talent.pool`, wizard `talent.pool.add.applicants`), and Add
  to Job (`job.add.applicants`) applies a pooled talent to other jobs.
- Activity plans (18.0+): Recruitment ‣ Configuration ‣ Activities ‣ Activity Plans,
  launched from the application's chatter to schedule the usual follow-ups at once.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| The person | on the application | same | `hr.candidate`, one application per job (`candidate_id` required) | on the application again | same |
| Application subject `name` | required | required | removed | removed | removed |
| Recruiter | `user_id` (users) | same | same | same | `recruiter_id` (employees) |
| Meeting button | `action_makeMeeting` | same | `action_create_meeting` | same | same |
| Refused application | archived, status `refused` | same, `archived` status added | same, refuse duplicates | same | archived through `action_archive` |
| Create Employee | opens an unsaved form | creates the employee | creates it from the candidate | creates it, copies attachments | same |
| Employee link | `emp_id` | `emp_id` | `employee_id` (candidate) | `employee_id` | same |
| Interview form answer | `response_id` | `response_ids` | same, survey type `recruitment` | same | same |
| Job page URL | `/jobs/detail/<job>` | `/jobs/<job>` | same | same | same, scheduled publication |
| Job expected skills | none | none | `skill_ids` | `job_skill_ids` with levels | same |
| Talent pools | none | none | none | yes | yes |

## Verify

```python
for app in env['hr.applicant'].with_context(active_test=False).search([('job_id', '=', job.id)]):
    print(app.partner_name, app.stage_id.name, app.application_status, app.refuse_reason_id.name,
          app.date_closed, app.employee_id.name, len(app.meeting_ids))
print(job.no_of_recruitment, job.no_of_hired_employee)
```

This is 18.0-20.0. In 16.0, 17.0 the employee is `app.emp_id`.

## Pitfalls

- Refused applications are archived: search them with `active_test=False`, or they look
  deleted. Restore them with Restore (`action_unarchive` / `reset_applicant`), never by
  clearing `refuse_reason_id` alone.
- Only one stage per job should have `hired_stage`; an application that leaves it loses
  its hire date. A shared stage with empty `job_ids` applies to every job.
- 18.0: two applications of the same person share one candidate; editing the name or
  email on one changes all of them, and the employee is created from the candidate.
- Send Interview and Refuse with Send Email fail without an applicant email or without
  the sender's email; mail goes out only with an outgoing mail server.
- The shell runs as superuser: an interviewer acting in the interface sees only the
  applications of jobs where they are interviewer. Check access `with_user()`.
- Creating an employee from an application creates a contact and copies private data;
  do it with the user's yes.
