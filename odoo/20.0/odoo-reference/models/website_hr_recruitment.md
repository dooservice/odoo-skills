# website_hr_recruitment — Online Jobs

Depends on: hr_recruitment, website_mail.

## `hr.applicant` (extends)


Public methods: `website_form_input_filter`

## `hr.department` (extends)

- `display_name` Char

## `hr.job` (extends)

Inherits: `website.seo.metadata`, `website.published.multi.mixin`, `website.searchable.mixin`, `website.structured_data.mixin`

- `description` Html “Job Description”
- `website_published` Boolean
- `website_description` Html “Website description”
- `website_rating` Html “Website rating”
- `job_details` Html “Process Details”
- `full_url` Char “job URL” (compute=_compute_full_url)

Public methods: `action_archive`, `get_backend_menu_id`

Extension points: `_get_breadcrumb_items`, `_get_default_job_details`, `_get_default_website_description`, `_get_default_website_rating`, `_get_jsonld_dict`, `_prepare_jsonld_vals`

## `hr.recruitment.source` (extends)

- `url` Char “Tracker URL” (compute=_compute_url)

## `website` (extends)


Public methods: `get_suggested_controllers`

Extension points: `_get_search_scopes`

## `website.page` (extends)


## `website.published.multi.mixin` (extends)


Public methods: `open_website_url`
