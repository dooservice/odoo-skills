# Dashboards and data cleaning

Two ways to see figures at a glance and one to keep old data in check. The Dashboards
app shows spreadsheet dashboards (`spreadsheet.dashboard`) that the apps ship (sales,
invoicing, inventory, live chat and others) grouped in sections
(`spreadsheet.dashboard.group`); My Dashboard (`board`) collects the user's own saved
reports. Data Cleaning (`data_recycle`) finds records matching a rule (for example
leads lost two years ago) and archives or deletes them after review. 16.0 also has the
Notes app (`note`). Editing spreadsheets, creating new dashboards and the
deduplication rules of Data Cleaning are Enterprise and left out.

**At a glance**

- Apps: `spreadsheet_dashboard` with its `spreadsheet_dashboard_<app>` bridges; `board`,
  `data_recycle`; `note` (16.0).
- Names that change by version: dashboard `is_published` (18.0+); dashboard companies
  `company_id` (18.0), `company_ids` (19.0+); Undiscard a recycle line (20.0); Notes app
  `note` (16.0), To-do `project_todo` (17.0+).
- Sections: Before you start; The standard flow (Dashboards: 1 open a dashboard, 2 decide
  who sees which dashboard, 3 my dashboard; Data cleaning: 1 create a rule, 2 review);
  Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `spreadsheet_dashboard` (Dashboards) is installed with the apps; each app's
  dashboard comes with a `spreadsheet_dashboard_<app>` bridge. `board` and
  `data_recycle` from Apps. Ask before installing.
- Groups: dashboards are visible to the groups in their `group_ids`; Data Cleaning
  needs administrator rights.
- Read first:

```python
for g in env['spreadsheet.dashboard.group'].search([]):
    print(g.name, [(d.name, d.group_ids.mapped('full_name')) for d in g.dashboard_ids])
print(env['data_recycle.model'].search_read([], ['name', 'res_model_name', 'recycle_mode', 'recycle_action', 'records_to_recycle_count']))
```

## The standard flow

### Dashboards

1. **Open a dashboard.** Dashboards ‣ Dashboards, then a dashboard in the side panel;
   filters at the top narrow the period and other values. Data comes live from the
   records the user may read.

2. **Decide who sees which dashboard.** Dashboards ‣ Configuration ‣ Dashboards: each
   line's groups, section and sequence.

   ```python
   dash = env['spreadsheet.dashboard'].search([('name', '=', 'Sales')], limit=1)
   dash.write({'group_ids': [(6, 0, [env.ref('sales_team.group_sale_manager').id])]})
   env.cr.commit()
   ```

   Leaves the dashboard visible only to sales administrators. 18.0+ a dashboard also
   has `is_published` (unpublished ones are hidden) and companies (`company_id` in
   18.0, `company_ids` from 19.0).

3. **My Dashboard** (`board`). In any list, graph or pivot view: Favorites (the search
   panel's toggle) ‣ Add to my dashboard. Dashboards ‣ My Dashboard shows the saved
   views side by side; each user has their own.

### Data cleaning

1. **Create a rule.** Data Cleaning ‣ Configuration ‣ Rules ‣ Recycle Records ‣ New:
   model, filter, age, action, manual or automatic.

   ```python
   rule = env['data_recycle.model'].create({
       'name': 'Lost leads older than 2 years',
       'res_model_id': env['ir.model']._get_id('crm.lead'),
       'domain': "[('active', '=', False), ('probability', '=', 0)]",
       'include_archived': True,
       'time_field_id': env['ir.model.fields']._get('crm.lead', 'write_date').id,
       'time_field_delta': 2, 'time_field_delta_unit': 'years',
       'recycle_action': 'unlink',
       'recycle_mode': 'manual',
   })
   rule.action_recycle_records()
   env.cr.commit()
   ```

   Leaves candidate lines (`data_recycle.record`) for the matching records.
   `recycle_action`: `archive` or `unlink`. `recycle_mode`: `manual` (someone validates)
   or `automatic` (the daily scheduled action `data_recycle.ir_cron_clean_records`
   applies it). `notify_user_ids` with `notify_frequency` remind reviewers.

2. **Review.** Data Cleaning ‣ Recycle Records: Validate applies the action, Discard
   keeps the record and stops proposing it (20.0: Undiscard reverses that).

   ```python
   lines = env['data_recycle.record'].search([('recycle_model_id', '=', rule.id)])
   print(len(lines), lines[:5].mapped('name'))
   # lines.action_validate()   # only after the user approved the list
   ```

## Variations

- **Archive instead of delete.** `recycle_action='archive'` keeps the records out of
  sight and reversible; prefer it unless the user wants the data gone.
- **Notes** (16.0, `note`). Notes app: personal notes (`note.note`, `memo`) with the
  user's own stages and tags (Notes ‣ Configuration). From 17.0 the To-do app
  (`project_todo`) replaces it.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Dashboard `is_published` | no | no | yes | yes | yes |
| Dashboard companies | no | no | `company_id` | `company_ids` | `company_ids` |
| Favorite dashboards | no | no | no | yes | yes |
| Sections and share links menus | no | no | no | no | yes |
| Undiscard a recycle line | no | no | no | no | yes |
| Notes app | `note` | To-do | To-do | To-do | To-do |

## Verify

```python
print(dash.name, dash.group_ids.mapped('full_name'))
print(rule.records_to_recycle_count, rule.recycle_mode, rule.recycle_action)
```

## Pitfalls

- A rule with `recycle_action='unlink'` and `recycle_mode='automatic'` deletes records
  every day without review; never set both without the user's explicit yes.
- Deleting records that other documents reference fails or cascades; archive first.
- A dashboard shows only what the viewer may read; two users can see different totals
  on the same dashboard.
