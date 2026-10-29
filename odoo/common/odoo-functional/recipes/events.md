# Events

An event (`event.event`) has dates, a venue, a seat limit, tickets
(`event.event.ticket`) and attendees (`event.registration`). Attendees register from the
back end, from a sales order (`event_sale`) or on the website (`website_event`,
`website_event_sale`). Mail schedulers (`event.mail`) send the confirmation, reminders and
follow-ups. Around it: booths rented to exhibitors (`event_booth`, `event_booth_sale`),
talks and agenda (`website_event_track`), sponsors (`website_event_exhibitor`), quizzes
(`website_event_track_quiz`), meeting rooms (`website_event_meet`, up to 18.0) and leads
from attendees (`event_crm`). Badge scanning with the Enterprise barcode app and the
Enterprise social and marketing automation apps are left out. Emailing attendees as a
campaign is in `email-and-sms-marketing.md`.

## Before you start

- Apps: `event`. Selling tickets: `event_sale` (16.0, 17.0 it also holds the ticket
  product; 18.0+ the product part is `event_product`, installed with it). Website:
  `website_event`; online ticket sales: `website_event_sale`.
- Settings (Events ‣ Configuration ‣ Settings), each installs a module:
  `module_event_sale` (Tickets), `module_website_event_sale` (Online Ticketing),
  `module_event_booth` (Booth Management), `module_website_event_track` (Schedule &
  Tracks), `module_website_event_track_live` (Live Broadcast),
  `module_website_event_track_quiz` (Quiz on Tracks), `module_website_event_exhibitor`
  (Online Exhibitors), `module_website_event_meet` (Community Chat Rooms, 16.0 to 18.0),
  `module_website_event_questions` (Questions, 16.0 only). 17.0+ also
  `use_event_barcode` (attendee barcodes) and `use_google_maps_static_api`. Ask before
  installing any.
- Groups: `event.group_event_registration_desk`, `event.group_event_user`,
  `event.group_event_manager`.
- Read first:

```python
print(env['ir.module.module'].search_read([('name', 'like', 'event'), ('state', '=', 'installed')], ['name']))
print(env['event.type'].search_read([], ['name']))
print(env['event.stage'].search_read([], ['name', 'sequence', 'pipe_end']))
for e in env['event.event'].search([], limit=20):
    print(e.name, e.date_begin, e.date_tz, e.stage_id.name, e.seats_limited, e.seats_max, e.seats_available)
```

## The standard flow

1. **Event template** (optional, for events that repeat). Events ‣ Configuration ‣ Event
   Templates ‣ New: default seat limit, tickets, mail schedule and questions.

   ```python
   etype = env['event.type'].create({
       'name': 'Workshop',
       'seats_limited': True, 'seats_max': 30,
       'event_type_ticket_ids': [(0, 0, {'name': 'Standard'})],
   })
   env.cr.commit()
   ```

   Leaves a template; picking it on an event copies its tickets, mails and questions.

2. **Create the event.** Events ‣ Events ‣ New: name, dates (in `date_tz`), venue
   (`address_id`), organizer, seat limit.

   ```python
   event = env['event.event'].create({
       'name': 'Example Conference',
       'event_type_id': etype.id,
       'date_begin': '2026-11-20 08:00:00',   # stored in UTC
       'date_end': '2026-11-20 17:00:00',
       'date_tz': env.user.tz or 'UTC',
       'address_id': env.company.partner_id.id,
       'seats_limited': True, 'seats_max': 100,
   })
   env.cr.commit()
   ```

   Leaves the event in the first stage (`event.event_stage_new`). Stages are only a
   kanban; the stage with `pipe_end` marks it finished.

3. **Tickets.** The event form, Tickets tab: one line per ticket, with its price and
   seat limit. With `event_sale` each ticket has a product (default
   `event_sale.product_product_event` up to 17.0, `event_product.product_product_event`
   from 18.0) whose taxes and accounts are used when it is sold.

   ```python
   event.write({'event_ticket_ids': [(0, 0, {'name': 'Standard', 'price': 50.0, 'seats_max': 80}),
                                     (0, 0, {'name': 'VIP', 'price': 120.0, 'seats_max': 20})]})
   env.cr.commit()
   ```

   A ticket product must be an event ticket: `detailed_type='event'` (16.0, 17.0),
   `type='service'` with `service_tracking='event'` (18.0+).

4. **Communication.** The event form, Communication tab: when to send which
   template. Event templates bring defaults.

   ```python
   event.write({'event_mail_ids': [(0, 0, {
       'interval_nbr': 1, 'interval_unit': 'days', 'interval_type': 'before_event',
       'template_ref': f"mail.template,{env.ref('event.event_reminder').id}",
   })]})
   env.cr.commit()
   ```

   `interval_type`: `after_sub`, `before_event`, `after_event`; 19.0+ also
   `after_event_start` and `before_event_end`. The scheduled action sends them.

5. **Register attendees.** Event form ‣ Attendees smart button ‣ New, or a sales order
   (step 6), or the website (step 7).

   ```python
   ticket = event.event_ticket_ids.filtered(lambda t: t.name == 'Standard')
   reg = env['event.registration'].create({
       'event_id': event.id, 'event_ticket_id': ticket.id,
       'partner_id': env['res.partner'].search([('email', '=', 'buyer@client.example')], limit=1).id,
   })
   env.cr.commit()
   ```

   Leaves the attendee `open` (Registered) from 17.0. 16.0: `open` (Confirmed) when the
   event has `auto_confirm` (default), else `draft` until `reg.action_confirm()`.

6. **Sell tickets on a sales order** (`event_sale`). Sales ‣ Orders ‣ Quotations ‣ New,
   a line with the ticket product; the configurator asks event and ticket. Confirming
   opens the attendee details wizard (`registration.editor`).

   ```python
   order = env['sale.order'].create({
       'partner_id': reg.partner_id.id,
       'order_line': [(0, 0, {'product_id': ticket.product_id.id, 'product_uom_qty': 2,
                               'event_id': event.id, 'event_ticket_id': ticket.id})],
   })
   order.action_confirm()
   regs = order.order_line.registration_ids
   print(regs.mapped('state'), regs.mapped('sale_status'))
   env.cr.commit()
   ```

   16.0 has no `sale_status`: print `regs.mapped('is_paid')` instead.

   Leaves one registration per unit. 17.0+: the wizard confirms paid ones (`open`,
   `sale_status` `sold`); through the ORM fill their name and email, then
   `regs.action_confirm()`. A free order registers at once. 16.0: paid registrations stay
   `draft` until the invoice is paid, unless the event has `auto_confirm`. Cancelling the
   order cancels them.

7. **Publish on the website** (`website_event`). The event form's Go to Website button,
   then the Published switch; `website_menu` adds the event's own menu (Introduction,
   Location, Register, and Talks, Exhibitors, Booths when installed).

   ```python
   event.write({'website_menu': True, 'is_published': True})
   env.cr.commit()
   print(event.website_url)
   ```

   Leaves the event listed on `/event`; visitors register (and pay with
   `website_event_sale`) from its page. 17.0+ `website_visibility` (`public`, `link`,
   `logged_users`) limits who finds it; 20.0 `publish_on` publishes it at a date.

8. **On the day.** Events ‣ Registration Desk (17.0+, group
   `event.group_event_registration_desk`) scans badges; or the Attendees list, Attended
   button.

   ```python
   reg.action_set_done()
   env.cr.commit()
   ```

   Leaves the attendee `done` (Attended). When it ends, the event's Mark as done
   (`event.action_set_done()`) moves it to the `pipe_end` stage.

## Variations

- **Registration questions.** Events ‣ Configuration ‣ Event Questions (19.0+), or the
  event's Questions tab: `event.question` with `question_type` `simple_choice` or
  `text_box`; 17.0+ also `name`, `email`, `phone`, `company_name`. `once_per_order` asks
  once per order instead of per attendee. 16.0 needs `website_event_questions`, 17.0 has
  them in `website_event`, 18.0+ in `event`.
- **Multi-slot events** (19.0+). `is_multi_slots=True` and slots (`event.slot`: `date`,
  `start_hour`, `end_hour`); each registration takes an `event_slot_id`.
- **Booths** (`event_booth`). Events ‣ Configuration ‣ Booth Categories, then the event's
  Booths smart button: `event.booth` with `booth_category_id`, `state` `available` or
  `unavailable`. With `event_booth_sale` the category has a product (booth product:
  `detailed_type='event_booth'` up to 17.0, `service_tracking='event_booth'` 18.0+) and
  a price; `website_event_booth_sale` lets exhibitors book and pay online, and
  `website_event_booth_exhibitor` turns a booked booth into a sponsor when the category
  has `use_sponsor`.
- **Talks and agenda** (`website_event_track`). Events ‣ Tracks: `event.track` with
  speaker (`partner_id`), `date`, `duration`, `location_id`, `stage_id`, published on
  the agenda. `website_track_proposal` opens the Talk Proposals form on the website.
  Configuration has Track Stages, Track Locations, Track Tags. `website_event_track_live`
  adds `youtube_video_url` for streaming and replay.
- **Quizzes** (`website_event_track_quiz`). Events ‣ Configuration ‣ Quizzes: an
  `event.quiz` on a track, with questions and answers (`is_correct`, `awarded_points`);
  attendees earn points on the website.
- **Sponsors and exhibitors** (`website_event_exhibitor`). Events ‣ Configuration ‣
  Sponsor Levels, then the event's Sponsors: `event.sponsor` with `partner_id`,
  `sponsor_type_id`, `exhibitor_type` (`sponsor`, `exhibitor`, `online`), opening hours.
- **Meeting rooms** (16.0 to 18.0, `website_event_meet`). The event's Rooms:
  `event.meeting.room` with topic, capacity, audience; video rooms use Jitsi
  (`website_jitsi`, `website_event_jitsi`). `meeting_room_allow_creation` on the event
  template lets attendees open rooms. Not in 19.0+.
- **Leads from attendees** (`event_crm`). Events ‣ Configuration ‣ Lead Generation:
  `event.lead.rule` with `lead_creation_basis` (`attendee` or `order`),
  `lead_creation_trigger` (`create`, `confirm`, `done`), events or templates,
  `event_registration_filter` (a domain), team, salesperson, tags. `event_crm_sale`
  groups attendees of one sales order into one lead.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| New registration | `open` if `auto_confirm`, else `draft` | `open` | `open` | `open` | `open` |
| Ticket product | `detailed_type='event'` | same | `service_tracking='event'`, module `event_product` | same | same |
| Questions | `website_event_questions` | `website_event` | `event` | `event`, own menu | same |
| Registration Desk, `use_event_barcode` | no | yes | yes | yes | yes |
| `website_visibility` | no | yes | yes | yes | yes |
| Meeting rooms, Jitsi | yes | yes | yes | no | no |
| Multi-slot events | no | no | no | yes | yes |
| `after_event_start`, `before_event_end` | no | no | no | yes | yes |
| Stage Cancelled | yes | yes | yes | no | no |
| `publish_on` | no | no | no | no | yes |

## Verify

```python
event.invalidate_recordset()
print(event.stage_id.name, event.seats_limited, event.seats_max, event.seats_available)
print(env['event.registration'].read_group([('event_id', '=', event.id)], ['state'], ['state']))
print(event.event_mail_ids.mapped(lambda m: (m.interval_type, m.scheduled_date, m.mail_done)))
```

Then ask the user to open the event page in a private window and register.

## Pitfalls

- Dates are stored in UTC and shown in `date_tz`: write them converted, or the event
  moves by the timezone offset.
- A sold-out event or ticket raises on registration; raise `seats_max` or untick
  `seats_limited`, never delete attendees to make room.
- Confirming a sales order with an event product and no event on the line raises (17.0+):
  set `event_id` and `event_ticket_id` on each line.
- Mail schedulers run from a scheduled action; when mail fails the attendees get nothing
  (19.0+ the scheduler shows `error_datetime`). Fix outgoing mail first:
  `mail-servers.md`.
- Publishing an event makes its date, venue and prices public: ask.
