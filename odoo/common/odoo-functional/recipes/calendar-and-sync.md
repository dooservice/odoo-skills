# Calendar and sync

The Calendar app holds meetings (`calendar.event`) with attendees (`calendar.attendee`),
reminders (`calendar.alarm`) and recurrence. Each user can synchronize their own
calendar with Google Calendar (`google_calendar`) or Outlook (`microsoft_calendar`), after
an administrator registers the database with Google or Microsoft once. Reminders can go
by notification, email, or SMS (`calendar_sms`). Appointment booking pages are
Enterprise and left out.

## Before you start

- Apps: `calendar`. Sync: `module_google_calendar`, `module_microsoft_calendar` in
  Settings ‣ General Settings, Integrations. Ask before installing.
- Settings: Google `cal_client_id`, `cal_client_secret`; Microsoft
  `cal_microsoft_client_id`, `cal_microsoft_client_secret`; 17.0+ also
  `cal_sync_paused`, `cal_microsoft_sync_paused`. Up to 16.0 they are in Settings ‣
  General Settings; from 17.0 in Calendar ‣ Configuration ‣ Settings. The client ID and
  secret come from the user's Google Cloud or Microsoft Entra account.
- Read first:

```python
icp = env['ir.config_parameter'].sudo()
print(bool(icp.get_param('google_calendar_client_id')), bool(icp.get_param('microsoft_calendar_client_id')))
print(env['calendar.alarm'].search_read([], ['name', 'alarm_type', 'duration', 'interval']))
print(env['calendar.event'].search_count([('start', '>=', '2026-01-01')]), 'events this year')
```

## The standard flow

1. **Reminders.** Calendar ‣ Configuration ‣ Reminders: type and delay.

   ```python
   alarm = env['calendar.alarm'].create({'name': 'Email, 1 day before', 'alarm_type': 'email',
                                         'duration': 1, 'interval': 'days'})
   env.cr.commit()
   ```

   `alarm_type`: `notification`, `email`; `sms` with `calendar_sms`. `interval`:
   `minutes`, `hours`, `days`.

2. **Create a meeting.** Calendar ‣ Calendar, drag on the grid or New: title, start and
   end, attendees, reminders, recurrence.

   ```python
   partner = env['res.partner'].search([('email', '=', 'customer.a@example.com')], limit=1)
   event = env['calendar.event'].create({
       'name': 'Product A demo',
       'start': '2026-11-20 14:00:00', 'stop': '2026-11-20 15:00:00',   # UTC
       'partner_ids': [(6, 0, (env.user.partner_id | partner).ids)],
       'alarm_ids': [(6, 0, alarm.ids)],
   })
   env.cr.commit()
   ```

   Leaves one attendee per partner in `needsAction`; the others receive an invitation
   email with accept and decline links. `allday=True` uses dates instead of hours.

3. **Repeat it** (optional). The event's Recurrent option: `recurrency=True` with
   `rrule_type` (`daily`, `weekly`, `monthly`, `yearly`), `interval`, `end_type`
   (`count`, `end_date`, `forever`) and `count` or `until`.

   ```python
   event.write({'recurrency': True, 'rrule_type': 'weekly', 'interval': 1, 'end_type': 'count', 'count': 4})
   env.cr.commit()
   ```

   Leaves four events of one `calendar.recurrence`; editing one asks whether to apply
   to this, following or all events.

4. **Answer.** An attendee accepts or declines from the email or the event.

   ```python
   event.attendee_ids.filtered(lambda a: a.partner_id == partner).do_accept()
   env.cr.commit()
   ```

   `state`: `needsAction`, `tentative`, `declined`, `accepted`.

5. **Register the database with Google** (once, administrator). In the Google Cloud
   console the user creates an OAuth client of type web application with the redirect
   URI `<web.base.url>/google_account/authentication` and enables the Calendar API; then
   enters the client ID and secret in the settings.

   ```python
   env['res.config.settings'].create({'cal_client_id': '<client id>', 'cal_client_secret': '<client secret>'}).execute()
   env.cr.commit()
   ```

   Microsoft is the same with an Entra app registration, the redirect URI
   `<web.base.url>/microsoft_account/authentication` and `cal_microsoft_client_id`,
   `cal_microsoft_client_secret`.

6. **Each user connects.** Calendar ‣ Calendar, the Google or Outlook button, then the
   provider's consent screen. Only the user can do this, in their own browser.

   Leaves the user's events synchronized both ways by a scheduled action; the user's
   preferences hold Stop or Pause synchronization.

## Variations

- **SMS reminders** (`calendar_sms`). A reminder with `alarm_type='sms'` texts the
  attendees with a mobile number; it uses SMS credits (`email-and-sms-marketing.md`).
- **Meetings from other documents.** The Meeting button of a lead, a contact or an
  activity of type Meeting opens the calendar with that record linked.
- **Video call.** The event's Odoo meeting link (`videocall_location`); with Google sync
  a Meet link is added by Google (20.0: `cal_google_disable_auto_videocall_link` turns
  that off).
- **Shared calendars** (20.0). Calendar ‣ Configuration ‣ Calendars: a
  `calendar.calendar` shared with users, and the privacy `members_only`.
- **Pause sync for everyone** (17.0+). `cal_sync_paused` or `cal_microsoft_sync_paused`
  stop the synchronization without disconnecting the users.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Sync credentials | General Settings | Calendar Settings | same | same | same |
| Pause sync settings | no | yes | yes | yes | yes |
| Calendar ‣ Configuration ‣ Settings | no | yes | yes | yes | yes |
| Shared calendars, `members_only` | no | no | no | no | yes |
| Google auto Meet link switch | no | no | no | no | yes |

## Verify

```python
event.invalidate_recordset()
print(event.start, event.stop, [(a.partner_id.name, a.state) for a in event.attendee_ids])
print(env['res.users'].search_count([('google_calendar_rtoken', '!=', False)]), 'users synced with Google')
```

## Pitfalls

- `start` and `stop` are stored in UTC; the user sees them in their timezone (`tz`).
  A user without timezone sees shifted hours in synced calendars.
- A database copy keeps the users' sync tokens unless it is neutralized (neutralizing
  clears them and stops the sync); otherwise the copy writes to the real calendars.
- Changing `web.base.url` breaks the redirect URI; register the new one with Google or
  Microsoft.
- Synced events are shared: deleting one in Odoo removes it from the user's Google or
  Outlook calendar too. Ask before bulk deletes.
