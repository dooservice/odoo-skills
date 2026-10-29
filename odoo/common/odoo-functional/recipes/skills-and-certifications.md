# Skills, resumes and certifications

What each employee knows and has learned: skills rated on the levels of a skill type, a
resume of experience and education lines, and the courses and certifications that the
eLearning, Surveys and Events apps write into that resume by themselves. Needs `hr` and
`hr_skills`; `hr_skills_slides` (eLearning), `hr_skills_survey` (Surveys) and
`hr_skills_event` (Events, from 19.0) are bridges installed automatically with both apps.
Employees, departments and users are set up in
[employees-and-expenses.md](employees-and-expenses.md); skills on job positions and
applicants belong to [recruitment.md](recruitment.md). Appraisals are Enterprise and left
out.

## Before you start

- Apps: `hr_skills`. With eLearning (`website_slides`) installed, `hr_skills_slides`
  comes along; with Surveys (`survey`), `hr_skills_survey`; with Events (`event`, 19.0+),
  `hr_skills_event`.
- Settings: none. Employees ‣ Configuration ‣ Resume ‣ Line Types (19.0+: Sections) needs
  developer mode.
- Every automatic resume line goes to the employee whose user (20.0: user or work
  contact) is the partner who finished the course or the certification: link the users
  first.
- Read first:

```python
for st in env['hr.skill.type'].search([]):
    print(st.name, st.is_certification, st.skill_ids.mapped('name'), [(l.name, l.level_progress, l.default_level) for l in st.skill_level_ids])
print(env['hr.resume.line.type'].search_read([], ['name', 'sequence']))
employee = env['hr.employee'].search([('name', '=', '<employee>')])
print(employee.user_id.login, employee.employee_skill_ids.mapped('display_name'))
print(employee.resume_line_ids.read(['name', 'line_type_id', 'date_start', 'date_end']))
```

  The block is for 19.0 and 20.0; in 16.0-18.0 drop `st.is_certification` (no
  certification types).

## The standard flow

1. **Skill type, its skills and levels.** Employees ‣ Configuration ‣ Skill Types ‣ New.
   One type groups skills that share a scale (`Languages`: `English`, `Spanish`;
   levels `A1` to `C2`).

   ```python
   skill_type = env['hr.skill.type'].create({
       'name': '<type>',
       'skill_ids': [(0, 0, {'name': '<skill A>'}), (0, 0, {'name': '<skill B>'})],
       'skill_level_ids': [
           (0, 0, {'name': '<beginner>', 'level_progress': 25, 'default_level': True}),
           (0, 0, {'name': '<intermediate>', 'level_progress': 60}),
           (0, 0, {'name': '<expert>', 'level_progress': 100}),
       ],
   })
   ```

   `level_progress` (0 to 100) orders the levels and draws the bar; `default_level` is
   the level proposed when the skill is picked. From 19.0, tick Certification
   (`is_certification`) to make the type a certification type (step 3).

2. **Skills of an employee.** Employees ‣ the employee ‣ Resume tab ‣ Skills ‣ Pick a
   skill from the list.

   ```python
   skill = skill_type.skill_ids[0]
   level = skill_type.skill_level_ids.filtered(lambda l: l.level_progress == 60)
   employee.write({'employee_skill_ids': [(0, 0, {
       'skill_type_id': skill_type.id, 'skill_id': skill.id, 'skill_level_id': level.id,
   })]})
   ```

   One line per skill and employee. To change the level, edit the line in the form; up
   to 18.0 the change is written in place and logged in `hr.employee.skill.log` (the
   progress graph); from 19.0 the old line gets `valid_to` = yesterday and a new line
   starts today, so write through the employee:
   `employee.write({'employee_skill_ids': [(1, emp_skill.id, {'skill_level_id': new_level.id})]})`.

3. **Certification of an employee (19.0+).** Employees ‣ Learning ‣ Certifications ‣ New,
   or the Certifications section of the employee's Resume tab. A certification is a skill
   of a type with `is_certification`, valid between two dates.

   ```python
   cert_type = env['hr.skill.type'].create({
       'name': '<certification>', 'is_certification': True,
       'skill_ids': [(0, 0, {'name': '<certificate>'})],
       'skill_level_ids': [(0, 0, {'name': 'Certified', 'level_progress': 100, 'default_level': True})],
   })
   employee.write({'employee_skill_ids': [(0, 0, {
       'skill_type_id': cert_type.id, 'skill_id': cert_type.skill_ids.id,
       'skill_level_id': cert_type.skill_level_ids.id,
       'valid_from': '<YYYY-MM-DD>', 'valid_to': '<YYYY-MM-DD>',
   })]})
   ```

   When every period of a certificate has ended, the latest one stays listed as expired;
   the same certificate can be held again for another period. Up to 18.0 there are no certification skills: certifications are
   resume lines written by Surveys (step 6).

4. **Resume lines.** Resume tab ‣ Resume ‣ Add (19.0+: the section's add button). Up to
   18.0 a new employee already has one Experience line (company and job title) created
   with the employee.

   ```python
   env['hr.resume.line'].create({
       'employee_id': employee.id, 'name': '<school or company>',
       'line_type_id': env.ref('hr_skills.resume_type_education').id,
       'date_start': '<YYYY-MM-DD>', 'date_end': '<YYYY-MM-DD>', 'description': '<text>',
   })
   ```

   Types shipped: `hr_skills.resume_type_experience`, `hr_skills.resume_type_education`;
   `Training` comes from `hr_skills_slides` up to 18.0
   and from `hr_skills` from 19.0 (`hr_skills.resume_type_training`, a course type:
   `is_course`).

5. **A course finished in eLearning.** The employee's user completes an eLearning course
   (all its required content). Nothing to do by hand: `hr_skills_slides` adds a Training
   line named after the course and posts "The employee has completed the course" on the
   employee.

   ```python
   lines = employee.resume_line_ids.filtered(lambda l: l.line_type_id == env.ref('hr_skills.resume_type_training'))
   print(lines.read(['name', 'date_start', 'channel_id', 'course_type']))
   ```

   The block is for 19.0 and 20.0. In 16.0-18.0 the type is
   `hr_skills_slides.resume_type_training` and the field is `display_type`, not
   `course_type`. Up to 18.0 the line has `display_type='course'`; from 19.0 `course_type='elearning'`.
   From 19.0, Employees ‣ Learning ‣ Courses ‣ eLearning opens the courses meant for
   training and Learning ‣ Training Attendances lists who followed what.

6. **A certification passed in Surveys.** The employee's user passes a survey with
   Is a Certification (`certification`) and a score at least the Required Score
   (`scoring_success_min`). `hr_skills_survey` adds a Certification line
   (`hr_skills_survey.resume_type_certification`) with `survey_id`.

   ```python
   survey = env['survey.survey'].search([('title', '=', '<certification survey>')])
   survey.certification_validity_months = 12
   print(env['hr.resume.line'].search_read([('employee_id', '=', employee.id), ('survey_id', '=', survey.id)],
                                          ['name', 'date_start', 'date_end', 'expiration_status']))
   ```

   The block is for 18.0-20.0 (`0` months means it never expires). In 17.0 skip the
   validity line; in 16.0 also leave `expiration_status` out of the read.
   From 18.0 `date_end` is the pass date plus the validity months and passing again
   updates the same line; `expiration_status` (17.0+) is `valid`, `expiring` or
   `expired`. In 17.0 and 18.0, Employees ‣ Reporting ‣ Certifications lists them.

## Variations

- Onsite training (19.0+, `hr_skills_event`): Employees ‣ Learning ‣ Courses ‣ Onsite
  lists the events; on the Resume tab, add a Training line with Course Type `onsite` and
  the event (`event_id`). An event created from that field registers the employee as an
  attendee.
- External training (19.0+): a Training line with Course Type `external`, its URL
  (`external_url`) and the certificate file (`certificate_file`).
- Skills inventory: Employees ‣ Reporting ‣ Skills (19.0: Reporting ‣ Skills ‣ Skills
  Inventory; 20.0: Reporting ‣ Skills Inventory) and, per department, the department's
  Skills report from its kanban card.
- Certifications a job requires (19.0+): the job position's skills (`job_skill_ids`)
  with a certification type; the daily scheduled action "Skills: Add an activity to
  employees with missing or expiring certifications" reminds the employee's manager.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Skill level change | edited in place, logged | same | same | old line closed (`valid_to`), new line | same |
| Certification skills (`is_certification`) | no | no | no | yes, Learning ‣ Certifications | same |
| Resume line kind | `display_type` (`classic`, `course`, `certification`) | same | same | `course_type` (`external`, `elearning`, `onsite`) on course types | same |
| Training line type | `hr_skills_slides.resume_type_training` | same | same | `hr_skills.resume_type_training` | same |
| Survey certification validity | none | none, `expiration_status` | `certification_validity_months` | same | same |
| Certifications list | none | Reporting ‣ Certifications (survey lines) | same | Learning ‣ Certifications, Reporting ‣ Skills ‣ Certifications (certification skills) | Learning ‣ Certifications |
| Experience line on new employee | yes | yes | yes | no | no |
| Onsite courses (`hr_skills_event`) | no | no | no | yes | yes |
| Survey line matched by | user's partner | same | same | same | user's partner or work contact |

## Verify

19.0, 20.0:

```python
print([(s.display_name, s.valid_from, s.valid_to) for s in employee.current_employee_skill_ids])
print([(c.display_name, c.valid_from, c.valid_to) for c in employee.certification_ids])
for line in employee.resume_line_ids.sorted('date_start'):
    print(line.line_type_id.name, line.name, line.date_start, line.date_end)
```

16.0-18.0:

```python
print([(s.skill_id.name, s.skill_level_id.name, s.level_progress) for s in employee.employee_skill_ids])
for line in employee.resume_line_ids.sorted('date_start'):
    print(line.line_type_id.name, line.name, line.date_start, line.date_end)
```

## Pitfalls

- No resume line after a finished course or a passed certification: the participant's
  partner is not the employee's user (20.0: nor work contact). Link the user to the
  employee; past completions are not replayed, add the line by hand.
- 19.0+: writing `hr.employee.skill` directly (`emp_skill.write(...)`) bypasses the
  history and can raise "The following skills can't be created as they overlap". Change
  skills through the employee's `employee_skill_ids` commands, as above.
- 19.0+: removing a skill older than one day only closes it (`valid_to` = yesterday);
  it disappears from the current skills but stays in the history and the reports.
- Deleting a skill type deletes its skills, levels and every employee's skill on it
  (`ondelete='cascade'`). From 18.0, archive the type instead (`active`).
- Up to 17.0 a survey certification has no end date: the line never expires. Set
  `date_end` on the line when the certificate is time-limited.
