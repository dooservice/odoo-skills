# Challenges and badges

Recognition and targets for the team: badges one user grants another, and challenges
that give each participant goals measured from Odoo's own records (number of leads,
sum of sales) and reward the winners with badges. Needs `gamification` (installed with
`hr`, eLearning or Forum) and `hr_gamification`, which puts the menus in Employees and
the Badges tab on the employee. Users and employees are set up in
[users-and-access.md](users-and-access.md) and
[employees-and-expenses.md](employees-and-expenses.md). The same models drive karma and
ranks of eLearning and Forum, left out here.

## Before you start

- Apps: `gamification`, `hr_gamification` (both in every version 16.0-20.0).
- Access: Employees: Officer (`hr.group_hr_user`) manages challenges; goal definitions
  are under Settings ‣ Gamification Tools, in developer mode.
- Settings: none.
- Read first:

```python
print(env['gamification.badge'].search_read([], ['name', 'rule_auth', 'rule_max', 'rule_max_number', 'granted_count']))
print(env['gamification.challenge'].search_read([], ['name', 'state', 'period', 'challenge_category', 'user_count']))
print(env['gamification.goal.definition'].search_read([], ['name', 'computation_mode', 'model_id', 'domain', 'condition']))
```

## The standard flow

1. **Badge.** Employees ‣ Configuration ‣ Challenges ‣ Badges ‣ New: name, description,
   image, and who may grant it (Allowance to Grant, `rule_auth`).

   ```python
   badge = env['gamification.badge'].create({
       'name': '<badge>', 'description': '<what it recognises>',
       'rule_auth': 'everyone',           # 'users' (rule_auth_user_ids), 'having' (rule_auth_badge_ids), 'nobody' (challenges only)
       'rule_max': True, 'rule_max_number': 3,   # at most 3 grants per sender per month
   })
   ```

2. **Grant it to an employee.** Employees ‣ the employee ‣ Badges tab ‣ Grant a Badge:
   badge and comment. The employee needs a user.

   ```python
   wizard = env['gamification.badge.user.wizard'].with_user(sender_user).create({
       'employee_id': employee.id, 'badge_id': badge.id, 'comment': '<why>',
   })
   wizard.action_grant_badge()
   env.cr.commit()
   ```

   Creates a `gamification.badge.user` and mails the employee. Refused for oneself and
   when the sender is not allowed (`rule_auth`) or has reached the monthly limit.

3. **Goal definition.** Settings ‣ Gamification Tools ‣ Goal Definitions ‣ New (developer
   mode): what is counted, on which model, for which user.

   ```python
   definition = env['gamification.goal.definition'].create({
       'name': '<goal>', 'computation_mode': 'count',          # 'manually', 'count', 'sum', 'python'
       'model_id': env['ir.model']._get_id('<model>'),
       'domain': "[('user_id', '=', user.id)]",                 # 'user' is the participant
       'field_date_id': env['ir.model.fields']._get('<model>', 'create_date').id,
       'condition': 'higher', 'display_mode': 'progress',
   })
   ```

   `sum` also needs Field to Sum (`field_id`). `field_date_id` limits the count to the
   challenge period.

4. **Challenge.** Employees ‣ Configuration ‣ Challenges ‣ Challenges ‣ New:
   participants, periodicity, the goals with their target, and the rewards.

   ```python
   challenge = env['gamification.challenge'].create({
       'name': '<challenge>', 'manager_id': env.user.id,
       'user_domain': "[('employee_ids.department_id', '=', %d)]" % department.id,   # or 'user_ids': [(6, 0, users.ids)]
       'period': 'monthly',                     # 'once' with start_date/end_date, 'daily', 'weekly', 'yearly'
       'visibility_mode': 'ranking',            # 'personal'
       'report_message_frequency': 'weekly',
       'line_ids': [(0, 0, {'definition_id': definition.id, 'target_goal': 10})],
       'reward_id': badge.id,                   # every participant who reaches all goals
       'challenge_category': 'hr',
   })
   ```

   Leaves it `draft`. `reward_first_id`, `reward_second_id`, `reward_third_id` reward the
   top three at the end of each period.

5. **Start.** Start Challenge.

   ```python
   challenge.action_start()
   env.cr.commit()
   print(env['gamification.goal'].search_read([('challenge_id', '=', challenge.id)], ['user_id', 'target_goal', 'current', 'state']))
   ```

   Leaves the challenge `inprogress` and one goal per participant and line, `inprogress`.
   A daily scheduled action recomputes automatic goals, starts the next period and sends
   the reports; Refresh Challenge (`action_check`) does it now.

6. **Manual goals.** Participants of a `manually` goal update their current value:
   Employees ‣ Configuration ‣ Challenges ‣ Goals History ‣ the goal ‣ Current Value.

   ```python
   goal.write({'current': 7})
   ```

   At the next refresh (daily, or Refresh Challenge) a goal whose current value meets the
   target becomes `reached`; one still short after its end date becomes `failed`.

7. **Close.** Set the challenge to Done on the status bar, or let `end_date` pass
   (non-recurring challenges).

   ```python
   challenge.write({'state': 'done'})
   ```

   Grants the pending rewards (with Reward as soon as every goal is reached,
   `reward_realtime`, the badge was already given when the goals were reached).

## Variations

- Badge from a certification: a Surveys certification with Give Badge
  (`certification_give_badge`, `certification_badge_id`) grants the badge to whoever
  passes it; see [skills-and-certifications.md](skills-and-certifications.md) for the
  resume line it also writes.
- Challenges for other areas (`challenge_category='other'`) are listed under Settings ‣
  Gamification Tools ‣ Challenges, not in Employees.
- Suggest a challenge (`invited_user_ids`): users see it and join it themselves.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Grant wizard | employee required, refuses an employee without user | employee optional, user from employee | same | same | same |
| Wizard title | Reward Employee | same | same | Grant a badge | same |
| Badges tab on employee | yes | yes | yes | yes | yes |

## Verify

```python
print(env['gamification.badge.user'].search_read([('badge_id', '=', badge.id)], ['user_id', 'employee_id', 'sender_id', 'comment', 'create_date']))
print(challenge.state, [(g.user_id.name, g.current, g.target_goal, g.state) for g in env['gamification.goal'].search([('challenge_id', '=', challenge.id)])])
```

## Pitfalls

- "You can not send a badge to yourself": grant as another user (`with_user`), not as
  the user who receives it.
- No goals after Start: `user_domain` matches no active internal user, or the employees
  have no user. Check `challenge.user_ids`.
- An automatic goal stays at 0: the definition's domain does not use `user` the way the
  model links records to people (`user_id`, `partner_id`), or `field_date_id` excludes
  the records. Test the domain on the model first.
- "You can not reset a challenge with unfinished goals": close or cancel the goals in
  progress before setting the challenge back to Draft.
- Report emails to everyone every day: `report_message_frequency` is per challenge; set
  `never` or a longer period.
