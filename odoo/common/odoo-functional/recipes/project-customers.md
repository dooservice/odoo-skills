# Customer requests, text messages and ratings on projects

The customer's side of a project: a request sent from a website form becomes a task, the
customer gets a text message when the task reaches a stage, and an email asking for a
rating when it is done. The customer's answer lands on the task, and the team can reply
to it on the portal. Needs `project`; `website` for the request form (it installs
`website_form_project` in 16.0, 17.0 and `website_project` from 18.0), `sms` for text
messages (`project_sms`); ratings are part of `project` with `rating` and `portal_rating`.
Creating the project and sharing it on the portal is in `projects-and-timesheets.md`.
Text messages are sent through Odoo's IAP service and use prepaid credits; the helpdesk
app is Enterprise and left out.

## Before you start

- Apps: `project`; `website` for the request form; `sms` for text messages.
- Settings: `group_project_rating` (Project ‣ Configuration ‣ Settings ‣ Customer
  Ratings) in 16.0-18.0; from 19.0 there is no setting, ratings are switched on per
  stage. `group_project_stages` only to send text messages on project stages.
- Read first:

19.0+:

```python
print(env['project.project'].search_read([], ['name', 'partner_id', 'privacy_visibility']))
print(env['project.task.type'].search_read([('project_ids', '!=', False)],
      ['name', 'sms_template_id', 'rating_active', 'rating_status', 'rating_template_id']))
print(env['sms.template'].search_read([('model', '=', 'project.task')], ['name', 'body']))
```

16.0-18.0:

```python
print(env['project.project'].search_read([], ['name', 'partner_id', 'privacy_visibility', 'rating_active', 'rating_status']))
print(env['project.task.type'].search_read([('project_ids', '!=', False)], ['name', 'sms_template_id', 'rating_template_id']))
print(env['sms.template'].search_read([('model', '=', 'project.task')], ['name', 'body']))
```

`sms_template_id` and `sms.template` exist only with `sms` installed; drop them otherwise.

## The standard flow

1. **Put a request form on the website.** Website ‣ Go to Website ‣ Edit, drop a Form
   block on a page (for example Contact Us), and in its options set Action to "Create a
   Task" and Project to the project that receives requests. Save.

   The form creates the task as below. In 16.0 and 17.0 it fills the title, description
   and, for a signed-in visitor, the customer; from 18.0 it also matches the customer by
   the email typed (`email_from`), or keeps that email in `email_cc` with the name, phone
   and company typed when no contact has it.

   ```python
   task = env['project.task'].create({
       'name': '<request title>', 'project_id': project.id, 'partner_id': customer.id,
       'description': '<p><request text></p>',
   })
   env.cr.commit()
   ```

   Leaves the task in the project's first stage, unassigned.

2. **Text the customer when a task reaches a stage.** Create the message: Settings ‣
   Technical ‣ Phone / SMS ‣ SMS Templates (developer mode) ‣ New, Applies to Task. Then
   Project ‣ Configuration ‣ Task Stages (developer mode) ‣ the stage ‣ SMS Template.

   ```python
   sms_template = env['sms.template'].create({
       'name': '<template name>', 'model_id': env['ir.model']._get_id('project.task'),
       'body': 'Hello {{ object.partner_id.name }}, your request "{{ object.name }}" is in progress.',
   })
   in_progress = env['project.task.type'].browse(<stage id>)
   in_progress.sms_template_id = sms_template
   env.cr.commit()
   ```

   From then on, every task of a customer with a phone that enters this stage, or is
   created in it, sends the text message, logged in the task's chatter. Ask before
   setting it on a stage with tasks moving today: each move costs a credit.

3. **Ask for a rating when the work is done.** 16.0-18.0: turn on Customer Ratings in
   the settings, then on the project's Settings tab Customer Ratings (`rating_active`),
   "Rating when changing stage" (`rating_status`), and on the done stage the Rating Email
   Template. 19.0+: on the done stage (Task Stages ‣ the stage) "Send a customer rating
   request" (20.0: Ask for Ratings), "when reaching this stage" and the Rating Email
   Template.

   19.0+:

   ```python
   template = env.ref('project.rating_project_request_email_template')
   done = env['project.task.type'].browse(<stage id>)
   done.write({'rating_active': True, 'rating_status': 'stage', 'rating_template_id': template.id})
   env.cr.commit()
   ```

   16.0-18.0:

   ```python
   template = env.ref('project.rating_project_request_email_template')
   done = env['project.task.type'].browse(<stage id>)
   env['res.config.settings'].create({'group_project_rating': True}).execute()
   project.write({'rating_active': True, 'rating_status': 'stage'})
   done.rating_template_id = template
   env.cr.commit()
   ```

4. **Finish the task.** Move it to the done stage in the kanban. The customer of the task
   (or of the project) receives the rating email, unless the customer is the user moving
   the task.

   ```python
   task.write({'stage_id': done.id})
   env.cr.commit()
   rating = task.rating_ids.filtered(lambda r: not r.consumed)[:1]
   print(rating.partner_id.name, rating.access_token)
   ```

   Leaves a `rating.rating` waiting for the answer. This sends a real email: run it on a
   test customer.

5. **The customer rates.** The email links to `/rate/<token>/<5|3|1>` (satisfied, okay,
   dissatisfied) and a page to add a comment. The rating and comment are posted on the
   task's chatter.

   ```python
   task.rating_apply(5, token=rating.access_token, feedback='<comment>')
   env.cr.commit()
   ```

   Leaves the rating `consumed` with its value. With Automatic Kanban Status on the stage
   (`auto_validation_kanban_state` in 16.0, `auto_validation_state` from 17.0), a good
   rating sets the task to approved (16.0: green) and an okay or bad one to changes
   requested (16.0: blocked).

6. **Read and answer ratings.** Project ‣ Reporting ‣ Customer Ratings, open a rating and
   write in Comment (`publisher_comment`). The answer shows under the rating in the
   task's chatter on the customer portal.

   ```python
   rating.publisher_comment = '<answer>'
   env.cr.commit()
   print(rating.publisher_id.name, rating.publisher_datetime)
   ```

## Variations

- **Periodic ratings**: `rating_status = 'periodic'` with `rating_status_period`
  (`daily` to `yearly`), on the project up to 18.0 and on the stage from 19.0: a scheduled
  action sends the request while the task stays in that stage.
- **One-off text message**: select tasks in the list, Action ‣ Send SMS Text Message (18.0+:
  Send SMS), and write or pick a template.
- **Project stages**: with `group_project_stages`, Project ‣ Configuration ‣ Project
  Stages ‣ SMS Template texts the project's customer when the project reaches the stage.
- **Customer conversations on the portal (20.0, `portal_discuss`)**: invite a portal user
  to a Discuss channel (Discuss ‣ the channel ‣ Invite); they read and answer it from the
  Discuss card of their portal, `/my/conversations`.

  ```python
  channel._add_members(users=portal_user)
  env.cr.commit()
  ```

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Website form module | `website_form_project` | same | `website_project` | same | same |
| Form fields | title, email, description | title, description | adds customer name, phone, company | same | same |
| Ratings switched on by | setting + project `rating_active` | same | same | stage `rating_active` | same, labelled Ask for Ratings |
| Rating mode and frequency | on the project | same | same | on the stage | same |
| Automatic status field | `auto_validation_kanban_state` | `auto_validation_state` | same | same | same |
| Customer Ratings menu | needs the rating setting | same | same | always | always |
| Portal conversations | no | no | no | no | `portal_discuss` |

## Verify

```python
task.invalidate_recordset()
print(task.stage_id.name, task.partner_id.name, task.partner_id.phone)
print(env['sms.sms'].search_read([('partner_id', '=', task.partner_id.id)], ['number', 'state', 'body'], limit=5))
print(env['rating.rating'].search_read([('res_model', '=', 'project.task'), ('res_id', '=', task.id)],
                                       ['rating', 'feedback', 'consumed', 'publisher_comment']))
```

## Pitfalls

- No text message is sent for a task without customer or a customer without phone, and
  none without IAP credits: the chatter shows the failure. Check the customer's phone and
  the credits before blaming the template.
- No rating email goes to a task without customer (the project's customer is used as a
  fallback) or when the person moving the task is the customer.
- Up to 18.0 the stage's Rating Email Template does nothing until the project has Customer
  Ratings on; from 19.0 the stage needs "Send a customer rating request".
- A stage shared by several projects texts and rates the customers of all of them. Use a
  stage of its own for the projects that should notify.
- The website form creates tasks for anyone who submits it: limit the fields to what the
  team needs and watch the project for spam.
