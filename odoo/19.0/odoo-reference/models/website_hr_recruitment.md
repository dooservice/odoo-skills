# website_hr_recruitment — Online Jobs

Depends on: hr_recruitment, website_mail.

## `hr.applicant` (extends)


Public methods: `website_form_input_filter`

## `hr.department` (extends)

- `display_name` Char

## `hr.job` (extends)

Inherits: `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`

- `description` Html “Job Description”
- `website_published` Boolean
- `website_description` Html “Website description”
- `job_details` Html “Process Details”
- `published_date` Date (store, compute=_compute_published_date)
- `full_url` Char “job URL” (compute=_compute_full_url)

Public methods: `action_archive`, `get_backend_menu_id`, `set_open`

Extension points: `_get_default_job_details`, `_get_default_website_description`

## `hr.recruitment.source` (extends)

- `url` Char “Tracker URL” (compute=_compute_url)

## `website` (extends)


Public methods: `get_suggested_controllers`

## `website.page` (extends)
