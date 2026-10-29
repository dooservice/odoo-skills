# Live chat

A live chat channel (`im_livechat.channel`) puts a chat button on the website. Visitors
write; available operators (the channel's users) answer from Discuss. Channel rules
(`im_livechat.channel.rule`) decide on which pages and countries the button shows, and
whether a chatbot (`chatbot.script`) answers first. Canned responses speed up typing;
visitors rate the conversation at the end. With CRM, an operator or the chatbot turns a
conversation into a lead (`crm_livechat`, `website_crm_livechat`). Helpdesk tickets from
chat are Enterprise and left out.

## Before you start

- Apps: `im_livechat` (Live Chat); `website_livechat` installs with `website`;
  `crm_livechat` and `website_crm_livechat` with `crm`.
- Settings: per website, Website ‣ Configuration ‣ Settings, Live Chat: `channel_id`
  (pass `website_id`). Without website, the channel's Widget tab gives a script to paste
  on another site.
- Read first:

```python
for ch in env['im_livechat.channel'].search([]):
    print(ch.name, ch.user_ids.mapped('name'), [(r.regex_url, r.action, r.chatbot_script_id.title) for r in ch.rule_ids])
print(env['website'].search_read([], ['name', 'channel_id']))
```

## The standard flow

1. **Create the channel.** Live Chat ‣ Channels ‣ New (20.0 also Live Chat ‣
   Configuration ‣ Live Chat Channels): name, operators, the button's text and colors,
   the welcome message.

   ```python
   channel = env['im_livechat.channel'].create({
       'name': 'Example Shop support',
       'user_ids': [(6, 0, env['res.users'].search([('login', 'in', ['agent.a@example.com'])]).ids)],
       'button_text': 'Questions? Chat with us.',
       'default_message': 'Hello, how can we help?',
   })
   env.cr.commit()
   ```

   Leaves the channel with its operators. An operator joins or leaves from the channel's
   kanban card (`action_join`, `action_quit`, for the current user).

2. **Rules.** The channel's Channel Rules tab: URL pattern, action, countries, chatbot.

   ```python
   channel.write({'rule_ids': [(0, 0, {'regex_url': '/shop', 'action': 'auto_popup', 'auto_popup_timer': 10}),
                               (0, 0, {'regex_url': '/', 'action': 'display_button'})]})
   env.cr.commit()
   ```

   `action`: `display_button`, `display_button_and_text`, `auto_popup`, `hide_button`.
   The first rule (by `sequence`) whose `regex_url` matches the page and whose
   `country_ids` (empty: all) match the visitor applies.

3. **Put it on the website.** Website ‣ Configuration ‣ Settings, Live Chat, the channel.

   ```python
   website = env['website'].search([('name', '=', '<website name>')])
   env['res.config.settings'].create({'website_id': website.id, 'channel_id': channel.id}).execute()
   env.cr.commit()
   ```

   Leaves the button on that website's pages, shown when an operator is available (or a
   chatbot is set).

4. **Answer.** Operators answer in Discuss, Livechat section. Typing `:` (up to 18.0) or
   `::` (19.0+) followed by a shortcut inserts a canned response (Live Chat ‣
   Configuration ‣ Canned Responses).

5. **Review.** Live Chat ‣ Report ‣ Sessions History, Session Statistics, Operator
   Analysis, Customer Ratings (up to 18.0); Live Chat ‣ Sessions and Live Chat ‣
   Reporting (19.0+).

   20.0, 19.0, 18.0, 17.0:

   ```python
   print(env['discuss.channel'].search_count([('livechat_channel_id', '=', channel.id)]), 'sessions')
   ```

   16.0: the model is `mail.channel`, same field.

## Variations

- **Chatbot.** Live Chat ‣ Configuration ‣ Chatbots ‣ New: steps (`script_step_ids`)
  with `step_type` `text`, `question_selection` (with answers), `question_email`,
  `question_phone`, `free_input_single`, `free_input_multi`, `forward_operator`, and
  `create_lead` with `crm_livechat`. A step shows only after the answers in its
  `triggering_answer_ids`. Set the chatbot on a rule (`chatbot_script_id`); up to 18.0
  `chatbot_only_if_no_operator`, 19.0+ `chatbot_enabled_condition` (`always`,
  `only_if_no_operator`, `only_if_operator`).
- **Lead from a conversation** (`crm_livechat`). The operator types `/lead` with a title
  in the conversation; the lead keeps the transcript. With `website_crm_livechat`, the
  visitor's pages and the lead are linked.
- **Visitors** (`website_livechat`). Live Chat ‣ Visitors lists who is on the website now;
  an operator can start a chat with one.
- **Session limits** (19.0+). `max_sessions_mode` and `max_sessions` cap the conversations
  per operator; Configuration ‣ Expertise routes visitors to operators by skill.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Session model | `mail.channel` | `discuss.channel` | same | same | same |
| Canned responses | `mail.shortcode`, `:` | same | `mail.canned.response`, `:` | same, `::` | same, `::` |
| Reporting menu | Report | Report | Report | Sessions, Reporting | Sessions, Reporting |
| Chatbot condition | `chatbot_only_if_no_operator` | same | same | `chatbot_enabled_condition` | same |
| `max_sessions`, Expertise | no | no | no | yes | yes |

## Verify

```python
print(channel.user_ids.mapped('name'), channel.rule_ids.mapped('action'), website.channel_id.name)
```

Then ask the user to open the website in a private window with an operator online and
send a message.

## Pitfalls

- No operator online and no chatbot: the button hides. Operators must be logged in and
  have joined the channel.
- A `regex_url` is a regular expression on the path; `/` matches every page, so order
  the more specific rules first.
- Chat transcripts hold personal data; ask before exporting or deleting them.
