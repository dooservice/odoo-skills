# base_setup — Initial Setup Tools

Depends on: base, web.

## `ir.http` (extends)


Public methods: `session_info`

## `kpi.provider` (defines)

KPI Provider


Public methods: `get_kpi_summary`

## `res.config.settings` (extends)

- `company_id` Many2one → `res.company` “Company” (required)
- `is_root_company` Boolean (compute=_compute_is_root_company)
- `user_default_rights` Boolean “Default Access Rights”
- `module_base_import` Boolean “Allow users to import data from CSV/XLS/XLSX/ODS files”
- `module_google_calendar` Boolean “Allow the users to synchronize their calendar  with Google Calendar”
- `module_microsoft_calendar` Boolean “Allow the users to synchronize their calendar with Outlook Calendar”
- `module_mail_plugin` Boolean “Allow integration with the mail plugins”
- `module_auth_oauth` Boolean “Use external authentication providers (OAuth)”
- `module_auth_ldap` Boolean “LDAP Authentication”
- `module_account_inter_company_rules` Boolean “Manage Inter Company”
- `module_voip` Boolean “VoIP”
- `module_web_unsplash` Boolean “Unsplash Image Library”
- `module_sms` Boolean “SMS”
- `module_partner_autocomplete` Boolean “Partner Autocomplete”
- `module_base_geolocalize` Boolean “GeoLocalize”
- `module_google_recaptcha` Boolean “reCAPTCHA”
- `module_website_cf_turnstile` Boolean “Cloudflare Turnstile”
- `report_footer` Html “Custom Report Footer” (related=company_id.report_footer)
- `group_multi_currency` Boolean “Multi-Currencies”
- `external_report_layout_id` Many2one (related=company_id.external_report_layout_id)
- `show_effect` Boolean “Show Effect”
- `company_count` Integer “Number of Companies” (compute=_compute_company_count)
- `active_user_count` Integer “Number of Active Users” (compute=_compute_active_user_count)
- `language_count` Integer “Number of Languages” (compute=_compute_language_count)
- `company_name` Char “Company Name” (related=company_id.display_name)
- `company_informations` Text (compute=_compute_company_informations)
- `company_country_code` Char “Company Country Code” (readonly, related=company_id.country_id.code)
- `profiling_enabled_until` Datetime “Profiling enabled until”
- `module_product_images` Boolean “Get product pictures using barcode”

Public methods: `edit_external_header`, `open_company`, `open_default_user`

Extension points: `_prepare_report_view_action`

## `res.users` (extends)


Public methods: `web_create_users`
