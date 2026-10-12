# website_hr_recruitment — Online Jobs

Depends on: hr_recruitment, website_mail.

## `hr.department` (extends)


Public methods: `name_get`

## `hr.job` (extends)

Inherits: `website.seo.metadata`, `website.published.multi.mixin`

- `website_published` Boolean
- `website_description` Html “Website description”
- `job_details` Html “Process Details”

Public methods: `get_backend_menu_id`, `set_open`, `toggle_active`

Extension points: `_get_default_job_details`, `_get_default_website_description`

## `hr.recruitment.source` (extends)

- `url` Char “Url Parameters” (compute=_compute_url)

## `hr.applicant` (extends)


Public methods: `website_form_input_filter`

## `website` (extends)


Public methods: `get_suggested_controllers`
