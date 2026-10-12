# Settings

Each field of `res.config.settings`, and where it keeps its value.

| Field | Label | Kept as | Addon |
|---|---|---|---|
| `absence_management` |  | `company_id.absence_management` | hr_attendance |
| `account_cash_basis_base_account_active` | Base Tax Received Account Active | `account_cash_basis_base_account_id.active` | account |
| `account_cash_basis_base_account_id` | Base Tax Received Account | `company_id.account_cash_basis_base_account_id` | account |
| `account_check_printing_date_label` | Print Date Label | `company_id.account_check_printing_date_label` | account_check_printing |
| `account_check_printing_layout` | Check Layout | `company_id.account_check_printing_layout` | account_check_printing |
| `account_check_printing_margin_left` | Check Left Margin | `company_id.account_check_printing_margin_left` | account_check_printing |
| `account_check_printing_margin_right` | Check Right Margin | `company_id.account_check_printing_margin_right` | account_check_printing |
| `account_check_printing_margin_top` | Check Top Margin | `company_id.account_check_printing_margin_top` | account_check_printing |
| `account_check_printing_multi_stub` | Multi-Pages Check Stub | `company_id.account_check_printing_multi_stub` | account_check_printing |
| `account_default_credit_limit` | Default Credit Limit | `company_id.account_credit_limit` | account |
| `account_discount_expense_allocation_active` | Customer Invoices Discounts Account Active | `account_discount_expense_allocation_id.active` | account |
| `account_discount_expense_allocation_id` | Customer Invoices Discounts Account | `company_id.account_discount_expense_allocation_id` | account |
| `account_discount_income_allocation_active` | Vendor Bills Discounts Account Active | `account_discount_income_allocation_id.active` | account |
| `account_discount_income_allocation_id` | Vendor Bills Discounts Account | `company_id.account_discount_income_allocation_id` | account |
| `account_fiscal_country_id` | Fiscal Country Code | `company_id.account_fiscal_country_id` | account |
| `account_interco_clearing_journal_id` |  | `company_id.account_interco_clearing_journal_id` | account_payment_interco |
| `account_interco_payable_id` |  | `company_id.account_interco_payable_id` | account_payment_interco |
| `account_interco_receivable_id` |  | `company_id.account_interco_receivable_id` | account_payment_interco |
| `account_is_token_out_of_sync` |  | `account_peppol_edi_user.is_token_out_of_sync` | account_peppol |
| `account_journal_early_pay_discount_gain_account_active` | Early Discount Gain Account Active | `account_journal_early_pay_discount_gain_account_id.active` | account |
| `account_journal_early_pay_discount_gain_account_id` | Early Discount Gain | `company_id.account_journal_early_pay_discount_gain_account_id` | account |
| `account_journal_early_pay_discount_loss_account_active` | Early Discount Loss Account Active | `account_journal_early_pay_discount_loss_account_id.active` | account |
| `account_journal_early_pay_discount_loss_account_id` | Early Discount Loss | `company_id.account_journal_early_pay_discount_loss_account_id` | account |
| `account_journal_suspense_account_active` | Bank Suspense Account Active | `account_journal_suspense_account_id.active` | account |
| `account_journal_suspense_account_id` | Bank Suspense | `company_id.account_journal_suspense_account_id` | account |
| `account_on_checkout` | Customer Accounts | computed by the screen | website_sale |
| `account_peppol_contact_email` |  | computed by the screen | account_peppol |
| `account_peppol_edi_identification` |  | `account_peppol_edi_user.edi_identification` | account_peppol |
| `account_peppol_edi_mode` |  | `account_peppol_edi_user.edi_mode` | account_peppol |
| `account_peppol_edi_user` |  | `company_id.account_peppol_edi_user` | account_peppol |
| `account_peppol_migration_key` |  | `company_id.account_peppol_migration_key` | account_peppol |
| `account_peppol_phone_number` |  | `company_id.account_peppol_phone_number` | account_peppol |
| `account_peppol_proxy_state` |  | `company_id.account_peppol_proxy_state` | account_peppol |
| `account_peppol_purchase_journal_id` |  | `company_id.peppol_purchase_journal_id` | account_peppol |
| `account_price_include` | Default Sales Price Include | `company_id.account_price_include` | account |
| `account_storno` | Storno accounting | `company_id.account_storno` | account |
| `account_use_credit_limit` | Sales Credit Limit | `company_id.account_use_credit_limit` | account |
| `active_user_count` | Number of Active Users | computed by the screen | base_setup |
| `alias_domain_id` |  | `company_id.alias_domain_id` | mail |
| `allow_spontaneous_returns` |  | `company_id.allow_spontaneous_returns` | sale_stock |
| `annual_inventory_day` |  | `company_id.annual_inventory_day` | stock |
| `annual_inventory_month` |  | `company_id.annual_inventory_month` | stock |
| `attendance_barcode_source` |  | `company_id.attendance_barcode_source` | hr_attendance |
| `attendance_based` | Default Tracking | `company_id.attendance_based` | hr_attendance |
| `attendance_break_management` |  | `company_id.attendance_break_management` | hr_attendance |
| `attendance_capture_check_in` |  | `company_id.attendance_capture_check_in` | hr_attendance |
| `attendance_device_tracking` |  | `company_id.attendance_device_tracking` | hr_attendance |
| `attendance_from_systray` |  | `company_id.attendance_from_systray` | hr_attendance |
| `attendance_kiosk_delay` |  | `company_id.attendance_kiosk_delay` | hr_attendance |
| `attendance_kiosk_mode` |  | `company_id.attendance_kiosk_mode` | hr_attendance |
| `attendance_kiosk_url` |  | `company_id.attendance_kiosk_url` | hr_attendance |
| `attendance_kiosk_use_pin` |  | `company_id.attendance_kiosk_use_pin` | hr_attendance |
| `attendance_validation` |  | `company_id.attendance_validation` | hr_attendance |
| `attendance_validation_tolerance` |  | `company_id.attendance_validation_tolerance` | hr_attendance |
| `attendance_work_entry_type_id` |  | `company_id.attendance_work_entry_type_id` | hr_attendance |
| `auth_oauth_google_client_id` | Client ID | computed by the screen | auth_oauth |
| `auth_oauth_google_enabled` | Allow users to sign in with Google | computed by the screen | auth_oauth |
| `auth_signup_reset_password` | Enable password reset from Login page | parameter `auth_signup.reset_password` | auth_signup |
| `auth_signup_template_user_id` | Template user for new users created through signup | parameter `base.template_portal_user_id` | auth_signup |
| `auth_signup_uninvited` | Customer Account | parameter `auth_signup.invitation_scope` | auth_signup |
| `auth_signup_uninvited` |  | computed by the screen | website |
| `auth_totp_enforce` | Enforce two-factor authentication | computed by the screen | auth_totp_mail |
| `auth_totp_policy` | Two-factor authentication enforcing policy | parameter `auth_totp.policy` | auth_totp_mail |
| `auto_check_out` |  | `company_id.auto_check_out` | hr_attendance |
| `auto_check_out_mode` |  | `company_id.auto_check_out_mode` | hr_attendance |
| `auto_check_out_specific_time` |  | `company_id.auto_check_out_specific_time` | hr_attendance |
| `auto_check_out_tolerance` |  | `company_id.auto_check_out_tolerance` | hr_attendance |
| `autopost_bills` |  | `company_id.autopost_bills` | account |
| `barcode_nomenclature_id` |  | `company_id.nomenclature_id` | event |
| `barcode_nomenclature_id` |  | `company_id.nomenclature_id` | point_of_sale |
| `barcode_separator` | Separator | parameter `stock.barcode_separator` | stock |
| `cal_client_id` | Client_id | parameter `google_calendar_client_id` | google_calendar |
| `cal_client_secret` | Client_key | parameter `google_calendar_client_secret` | google_calendar |
| `cal_google_disable_auto_videocall_link` | Disable videocall generation | parameter `google_calendar.disable_auto_videocall_link` | google_calendar |
| `cal_microsoft_client_id` | Microsoft Client_id | parameter `microsoft_calendar_client_id` | microsoft_calendar |
| `cal_microsoft_client_secret` | Microsoft Client_key | parameter `microsoft_calendar_client_secret` | microsoft_calendar |
| `cal_microsoft_sync_paused` | Microsoft Synchronization Paused | parameter `microsoft_calendar_sync_paused` | microsoft_calendar |
| `cal_sync_paused` | Google Synchronization Paused | parameter `google_calendar_sync_paused` | google_calendar |
| `cart_abandoned_delay` |  | `website_id.cart_abandoned_delay` | website_sale |
| `cart_recovery_mail_template` |  | `website_id.cart_recovery_mail_template_id` | website_sale |
| `cash_rounding_loss_account_id` |  | `company_id.cash_rounding_loss_account_id` | account |
| `cash_rounding_profit_account_id` |  | `company_id.cash_rounding_profit_account_id` | account |
| `cdn_activated` |  | `website_id.cdn_activated` | website |
| `cdn_filters` |  | `website_id.cdn_filters` | website |
| `cdn_url` |  | `website_id.cdn_url` | website |
| `channel_id` | Website Live Channel | `website_id.channel_id` | website_livechat |
| `chart_template` |  | computed by the screen | account |
| `cloud_storage_azure_account_name` | Azure Account Name | parameter `cloud_storage_azure_account_name` | cloud_storage_azure |
| `cloud_storage_azure_client_id` | Azure Client ID | parameter `cloud_storage_azure_client_id` | cloud_storage_azure |
| `cloud_storage_azure_client_secret` | Azure Client Secret | parameter `cloud_storage_azure_client_secret` | cloud_storage_azure |
| `cloud_storage_azure_container_name` | Azure Container Name | parameter `cloud_storage_azure_container_name` | cloud_storage_azure |
| `cloud_storage_azure_invalidate_user_delegation_key` | Invalidate Cached Azure User Delegation Key | computed by the screen | cloud_storage_azure |
| `cloud_storage_azure_tenant_id` | Azure Tenant ID | parameter `cloud_storage_azure_tenant_id` | cloud_storage_azure |
| `cloud_storage_google_account_info` | Google Service Account Info | parameter `cloud_storage_google_account_info` | cloud_storage_google |
| `cloud_storage_google_bucket_name` | Google Bucket Name | parameter `cloud_storage_google_bucket_name` | cloud_storage_google |
| `cloud_storage_google_service_account_key` | Google Service Account Key | computed by the screen | cloud_storage_google |
| `cloud_storage_migration_all_model_ids` | All Attachments | computed by the screen | cloud_storage_migration |
| `cloud_storage_migration_all_models` |  | parameter `cloud_storage_migration_all_models` | cloud_storage_migration |
| `cloud_storage_migration_message_model_ids` | Message Attachments | computed by the screen | cloud_storage_migration |
| `cloud_storage_migration_message_models` |  | parameter `cloud_storage_migration_message_models` | cloud_storage_migration |
| `cloud_storage_migration_progress` | Migration Progress | computed by the screen | cloud_storage_migration |
| `cloud_storage_min_file_size` | Minimum File Size (bytes) | parameter `cloud_storage_min_file_size` | cloud_storage |
| `cloud_storage_min_file_size_mb` | Minimum File Size (MB) | computed by the screen | cloud_storage |
| `cloud_storage_provider` | Cloud Storage Provider for new attachments | parameter `cloud_storage_provider` | cloud_storage |
| `cloud_storage_provider` |  | computed by the screen | cloud_storage_azure |
| `cloud_storage_provider` |  | computed by the screen | cloud_storage_google |
| `cloud_storage_upload_record_attachments` | Upload Record Attachments | parameter `cloud_storage_upload_record_attachments` | cloud_storage |
| `company_count` | Number of Companies | computed by the screen | base_setup |
| `company_country_code` | Company Country Code | `company_id.country_id.code` | base_setup |
| `company_country_group_codes` |  | `company_id.country_id.country_group_codes` | base_setup |
| `company_currency_id` | Company Currency | `company_id.currency_id` | purchase |
| `company_expense_allowed_payment_method_line_ids` |  | `company_id.company_expense_allowed_payment_method_line_ids` | hr_expense |
| `company_id` | Company | computed by the screen | base_setup |
| `company_informations` |  | computed by the screen | base_setup |
| `company_lunch_minimum_threshold` | Maximum Allowed Overdraft | `company_id.lunch_minimum_threshold` | lunch |
| `company_lunch_notify_message` | Lunch notification message | `company_id.lunch_notify_message` | lunch |
| `company_name` | Company Name | `company_id.display_name` | base_setup |
| `company_tz` | Company Timezone | `company_id.tz` | hr |
| `confirmation_email_template_id` |  | `website_id.confirmation_email_template_id` | website_sale |
| `contact_us_link_url` |  | `website_id.contact_us_link_url` | website_sale |
| `contract_expiration_notice_period` | Contract Expiry Notice Period | `company_id.contract_expiration_notice_period` | hr |
| `cookie_policy_id` | Cookie Policy Page | `website_id.cookie_policy_id` | website |
| `country_code` |  | `company_id.account_fiscal_country_id.code` | account |
| `crm_auto_assignment_action` | Auto Assignment Action | computed by the screen | crm |
| `crm_auto_assignment_interval_number` | Repeat every | computed by the screen | crm |
| `crm_auto_assignment_interval_type` | Auto Assignment Interval Unit | computed by the screen | crm |
| `crm_auto_assignment_run_datetime` | Auto Assignment Next Execution Date | computed by the screen | crm |
| `crm_use_auto_assignment` | Rule-Based Assignment | parameter `crm.lead.auto.assignment` | crm |
| `currency_exchange_journal_id` | Currency Exchange Journal | `company_id.currency_exchange_journal_id` | account |
| `currency_id` | Currency | `company_id.currency_id` | account |
| `currency_id` |  | `company_id.currency_id` | lunch |
| `custom_address_placeholder` |  | `pos_config_id.company_id.receipt_address` | point_of_sale |
| `custom_email_placeholder` |  | `pos_config_id.company_id.email` | point_of_sale |
| `custom_phone_placeholder` | phone placeholder | `pos_config_id.company_id.phone` | point_of_sale |
| `custom_website_placeholder` |  | `pos_config_id.company_id.website` | point_of_sale |
| `days_to_purchase` |  | `company_id.days_to_purchase` | purchase_stock |
| `default_allow_out_of_stock_order` | Continue selling when out-of-stock | computed by the screen | website_sale |
| `default_available_threshold` | Show Threshold | computed by the screen | website_sale |
| `default_show_availability` | Show availability Qty | computed by the screen | website_sale |
| `delay_alert_contract` | Delay alert contract outdated | parameter `hr_fleet.delay_alert_contract` | fleet |
| `digest_emails` | Digest Emails | parameter `digest.default_digest_emails` | digest |
| `digest_id` | Digest Email | parameter `digest.default_digest_id` | digest |
| `display_account_storno` |  | `company_id.display_account_storno` | account |
| `display_invoice_amount_total_words` | Total amount of invoice in words | `company_id.display_invoice_amount_total_words` | account |
| `display_invoice_tax_company_currency` | Taxes in company currency | `company_id.display_invoice_tax_company_currency` | account |
| `display_product_images_on_so` |  | `company_id.display_product_images_on_so` | sale |
| `document_sequence_editable` | Document's sequence editable | `company_id.document_sequence_editable` | account |
| `downpayment_account_active` | Down payment Account Active | `downpayment_account_id.active` | sale |
| `downpayment_account_id` |  | `company_id.downpayment_account_id` | sale |
| `ecommerce_access` |  | `website_id.ecommerce_access` | website_sale |
| `email_primary_color` |  | `company_id.email_primary_color` | mail |
| `email_secondary_color` |  | `company_id.email_secondary_color` | mail |
| `enable_recaptcha` | Enable reCAPTCHA | parameter `enable_recaptcha` | google_recaptcha |
| `events_app_name` | Events App Name | `website_id.events_app_name` | website_event_track |
| `expense_account_active` | Expense Account Active | `expense_account_id.active` | account |
| `expense_account_id` |  | `company_id.expense_account_id` | account |
| `expense_currency_exchange_account_active` | Loss Exchange Rate Account Active | `expense_currency_exchange_account_id.active` | account |
| `expense_currency_exchange_account_id` | Loss Exchange Rate Account | `company_id.expense_currency_exchange_account_id` | account |
| `expense_journal_id` |  | `company_id.expense_journal_id` | hr_expense |
| `external_code` | External Code | `company_id.external_code` | hr_work_entry |
| `external_email_server_default` | Use Custom Email Servers | parameter `base_setup.default_external_email_server` | mail |
| `external_report_layout_id` |  | `company_id.external_report_layout_id` | base_setup |
| `fail_counter` | Fail Mail | computed by the screen | mail |
| `favicon` | Favicon | `website_id.favicon` | website |
| `force_restrictive_audit_trail` | Forced Audit Trail | `company_id.force_restrictive_audit_trail` | account |
| `gelato_api_key` |  | `company_id.gelato_api_key` | sale_gelato |
| `gelato_webhook_secret` |  | `company_id.gelato_webhook_secret` | sale_gelato |
| `geoloc_provider_googlemap_key` | Google Map API Key | parameter `base_geolocalize.google_map_api_key` | base_geolocalize |
| `geoloc_provider_id` | API | parameter `base_geolocalize.geo_provider` | base_geolocalize |
| `geoloc_provider_techname` |  | `geoloc_provider_id.tech_name` | base_geolocalize |
| `google_analytics_key` | Google Analytics Key | `website_id.google_analytics_key` | website |
| `google_gmail_client_identifier` | Gmail Client Id | parameter `google_gmail_client_id` | google_gmail |
| `google_gmail_client_secret` | Gmail Client Secret | parameter `google_gmail_client_secret` | google_gmail |
| `google_maps_static_api_key` | Google Maps API key | parameter `google_maps.signed_static_api_key` | event |
| `google_maps_static_api_secret` | Google Maps API secret | parameter `google_maps.signed_static_api_secret` | event |
| `google_places_api_key` | Google Places API Key | parameter `google_address_autocomplete.google_places_api_key` | google_address_autocomplete |
| `google_search_console` | Google Search Console Key | `website_id.google_search_console` | website |
| `google_translate_api_key` | Message Translation API Key | parameter `mail.google_translate_api_key` | mail |
| `group_analytic_accounting` | Analytic Accounting | group `analytic.group_analytic_accounting` | analytic |
| `group_auto_done_setting` | Lock Confirmed Sales | group `sale.group_auto_done_setting` | sale |
| `group_automate_suggested_products` | Automate suggested products | group `website_sale.group_automate_suggested_products` | website_sale |
| `group_cash_rounding` | Total Rounding | group `account.group_cash_rounding` | account |
| `group_discount_per_so_line` | Discounts | group `sale.group_discount_per_so_line` | sale |
| `group_expiry_date_on_delivery_slip` | Display Expiration Dates on Delivery Slips | group `product_expiry.group_expiry_date_on_delivery_slip` | product_expiry |
| `group_gmc_feed` | Google Merchant Center | group `website_sale.group_product_feed` | website_sale |
| `group_l10n_in_reseller` | Manage Reseller(E-Commerce) | group `l10n_in.group_l10n_in_reseller` | l10n_in |
| `group_lot_on_delivery_slip` | Display Lots & Serial Numbers on Delivery Slips | group `stock.group_lot_on_delivery_slip` | stock |
| `group_lot_on_invoice` | Display Lots & Serial Numbers on Invoices | group `stock_account.group_lot_on_invoice` | stock_account |
| `group_mass_mailing_campaign` | Mailing Campaigns | group `mass_mailing.group_mass_mailing_campaign` | mass_mailing |
| `group_mrp_byproducts` | By-Products | group `mrp.group_mrp_byproducts` | mrp |
| `group_mrp_routings` | MRP Work Orders | group `mrp.group_mrp_routings` | mrp |
| `group_multi_currency` | Multi-Currencies | group `base.group_multi_currency` | base_setup |
| `group_multi_website` | Multi-website | group `website.group_multi_website` | website |
| `group_pos_preset` | Presets | group `point_of_sale.group_pos_preset` | point_of_sale |
| `group_product_price_comparison` | Comparison Price | group `website_sale.group_product_price_comparison` | website_sale |
| `group_product_pricelist` | Pricelists | group `product.group_product_pricelist` | product |
| `group_product_variant` | Variants | group `product.group_product_variant` | product |
| `group_proforma_sales` | Pro Forma Invoice | group `sale.group_proforma_sales` | sale |
| `group_project_stages` | Project Stages | group `project.group_project_stages` | project |
| `group_sale_delivery_address` | Customer Addresses | group `account.group_delivery_invoice_address` | account |
| `group_send_reminder` | Receipt Reminder | group `purchase.group_send_reminder` | purchase |
| `group_services_and_material` | Services & Materials | group `sale.group_services_and_material` | sale |
| `group_show_uom_price` | Base Unit Price | group `product.group_show_uom_price` | product |
| `group_stock_adv_location` | Multi-Step Routes | group `stock.group_adv_location` | stock |
| `group_stock_lot_print_gs1` | Print GS1 Barcodes for Lots & Serial Numbers | group `stock.group_stock_lot_print_gs1` | stock |
| `group_stock_multi_locations` | Storage Locations | group `stock.group_stock_multi_locations` | stock |
| `group_stock_picking_batch` | Batch, Wave & Cluster Transfers | group `stock.group_stock_picking_batch` | stock |
| `group_stock_production_lot` | Lots & Serial Numbers | group `stock.group_production_lot` | stock |
| `group_stock_sign_delivery` | Signature | group `stock.group_stock_sign_delivery` | stock |
| `group_stock_tracking_lot` | Packages | group `stock.group_tracking_lot` | stock |
| `group_stock_tracking_owner` | Consignment | group `stock.group_tracking_owner` | stock |
| `group_unlocked_by_default` | Unlock Manufacturing Orders | group `mrp.group_unlocked_by_default` | mrp |
| `group_unpublish_out_of_stock` | Unpublish Out-of-Stock Products | group `website_sale.group_unpublish_out_of_stock` | website_sale |
| `group_uom` | Units of Measure & Packagings | group `uom.group_uom` | product |
| `group_use_lead` | Leads | group `crm.group_use_lead` | crm |
| `group_use_recurring_revenues` | Recurring Revenues | group `crm.group_use_recurring_revenues` | crm |
| `group_warning_purchase` | Purchase Warnings | group `purchase.group_warning_purchase` | purchase |
| `group_warning_sale` | Sale Order Warnings | group `sale.group_warning_sale` | sale |
| `group_warning_stock` | Warnings for Stock | group `stock.group_warning_stock` | stock |
| `has_accounting_entries` |  | computed by the screen | account |
| `has_chart_of_accounts` | Company has a chart of accounts | computed by the screen | account |
| `has_cookie_policy` |  | computed by the screen | website |
| `has_default_share_image` | Use a image by default for sharing | computed by the screen | website |
| `has_google_analytics` | Google Tag Manager/Google Analytics | computed by the screen | website |
| `has_google_search_console` | Google Search Console | computed by the screen | website |
| `has_plausible_shared_key` | Plausible Analytics | computed by the screen | website |
| `has_position_column` |  | `company_id.has_position_column` | l10n_din5008 |
| `horizon_days` |  | `company_id.horizon_days` | stock |
| `hr_expense_alias_domain_id` |  | computed by the screen | hr_expense |
| `hr_expense_alias_prefix` | Default Alias Name for Expenses | computed by the screen | hr_expense |
| `hr_expense_use_mailgateway` | Let your employees record expenses by email | parameter `hr_expense.use_mailgateway` | hr_expense |
| `hr_presence_control_attendance` |  | `company_id.hr_presence_control_attendance` | hr |
| `hr_presence_control_email` |  | `company_id.hr_presence_control_email` | hr |
| `hr_presence_control_email_amount` |  | `company_id.hr_presence_control_email_amount` | hr |
| `hr_presence_control_ip` |  | `company_id.hr_presence_control_ip` | hr |
| `hr_presence_control_ip_list` |  | `company_id.hr_presence_control_ip_list` | hr |
| `hr_presence_control_login` |  | `company_id.hr_presence_control_login` | hr |
| `income_account_active` | Income Account Active | `income_account_id.active` | account |
| `income_account_id` |  | `company_id.income_account_id` | account |
| `income_currency_exchange_account_active` | Gain Exchange Rate Account Active | `income_currency_exchange_account_id.active` | account |
| `income_currency_exchange_account_id` | Gain Exchange Rate Account | `company_id.income_currency_exchange_account_id` | account |
| `incoterm_id` | Default incoterm | `company_id.incoterm_id` | account |
| `installed_provider_id` | Installed Provider | computed by the screen | payment |
| `internal_project_id` | Internal Project | `company_id.internal_project_id` | project_timesheet_holidays |
| `invoice_mail_template_id` | Email Template | parameter `sale.default_invoice_email_template` | sale |
| `invoice_policy` | Invoice Policy | computed by the screen | sale_timesheet |
| `invoice_terms` | Terms & Conditions | `company_id.invoice_terms` | account |
| `invoice_terms_html` | Terms & Conditions as a Web page | `company_id.invoice_terms_html` | account |
| `is_account_peppol_eligible` | PEPPOL eligible | computed by the screen | account |
| `is_encode_uom_days` |  | computed by the screen | hr_timesheet |
| `is_installed_sale` | Is the Sale Module Installed | computed by the screen | purchase_stock |
| `is_membership_multi` | Multi Teams | parameter `sales_team.membership_multi` | crm |
| `is_newsletter_enabled` |  | computed by the screen | website_sale_mass_mailing |
| `is_root_company` |  | computed by the screen | base_setup |
| `journal_id` |  | `website_id.journal_id` | website_sale |
| `l10n_ar_arca_activity_id` |  | `company_id.l10n_ar_arca_activity_id` | l10n_ar |
| `l10n_ar_website_sale_show_both_prices` |  | `website_id.l10n_ar_website_sale_show_both_prices` | l10n_ar_website_sale |
| `l10n_cn_output_vat_offset_account_id` |  | `company_id.l10n_cn_output_vat_offset_account_id` | l10n_cn |
| `l10n_cn_output_vat_offset_journal_id` |  | `company_id.l10n_cn_output_vat_offset_journal_id` | l10n_cn |
| `l10n_cn_vat_differential_taxation` |  | `company_id.l10n_cn_vat_differential_taxation` | l10n_cn |
| `l10n_dk_nemhandel_proxy_state` |  | `company_id.l10n_dk_nemhandel_proxy_state` | l10n_dk |
| `l10n_eg_client_identifier` |  | `company_id.l10n_eg_client_identifier` | l10n_eg_edi_eta |
| `l10n_eg_client_secret` |  | `company_id.l10n_eg_client_secret` | l10n_eg_edi_eta |
| `l10n_eg_edi_api_mode` |  | `company_id.l10n_eg_edi_api_mode` | l10n_eg_edi_eta |
| `l10n_es_edi_verifactu_certificate_ids` |  | `company_id.l10n_es_edi_verifactu_certificate_ids` | l10n_es_edi_verifactu |
| `l10n_es_edi_verifactu_required` |  | `company_id.l10n_es_edi_verifactu_required` | l10n_es_edi_verifactu |
| `l10n_es_edi_verifactu_test_environment` |  | `company_id.l10n_es_edi_verifactu_test_environment` | l10n_es_edi_verifactu |
| `l10n_es_sii_certificate_ids` |  | `company_id.l10n_es_sii_certificate_ids` | l10n_es_edi_sii |
| `l10n_es_sii_tax_agency` |  | `company_id.l10n_es_sii_tax_agency` | l10n_es_edi_sii |
| `l10n_es_sii_test_env` |  | `company_id.l10n_es_sii_test_env` | l10n_es_edi_sii |
| `l10n_es_simplified_invoice_limit` |  | `company_id.l10n_es_simplified_invoice_limit` | l10n_es |
| `l10n_es_special_vat_regime` |  | `company_id.l10n_es_special_vat_regime` | l10n_es |
| `l10n_es_tbai_certificate_ids` |  | `company_id.l10n_es_tbai_certificate_ids` | l10n_es_edi_tbai |
| `l10n_es_tbai_tax_agency` |  | `company_id.l10n_es_tbai_tax_agency` | l10n_es_edi_tbai |
| `l10n_es_tbai_test_env` |  | `company_id.l10n_es_tbai_test_env` | l10n_es_edi_tbai |
| `l10n_eu_oss_eu_country` | Is European country? | computed by the screen | l10n_eu_oss |
| `l10n_fr_pdp_annuaire_start_date` | Annuaire Start Date | `company_id.l10n_fr_pdp_annuaire_start_date` | l10n_fr_pdp |
| `l10n_fr_pdp_periodicity` | Flow 10 Report Periodicity | `company_id.l10n_fr_pdp_periodicity` | l10n_fr_pdp |
| `l10n_fr_pdp_pilot_phase` | Pilot Phase | computed by the screen | l10n_fr_pdp |
| `l10n_fr_pdp_registered` | Approved Platform Registered | `company_id.l10n_fr_pdp_registered` | l10n_fr_pdp |
| `l10n_fr_pdp_send_to_ppf` | Send to PPF | `company_id.l10n_fr_pdp_send_to_ppf` | l10n_fr_pdp |
| `l10n_fr_reference_work_entry_type` |  | `company_id.l10n_fr_reference_work_entry_type` | l10n_fr_hr_holidays |
| `l10n_gcc_country_is_gcc` |  | `company_id.l10n_gcc_country_is_gcc` | l10n_gcc_invoice |
| `l10n_gcc_dual_language_invoice` |  | `company_id.l10n_gcc_dual_language_invoice` | l10n_gcc_invoice |
| `l10n_gcc_dual_language_receipt` |  | `pos_config_id.l10n_gcc_dual_language_receipt` | l10n_gcc_pos |
| `l10n_gr_edi_aade_id` |  | `company_id.l10n_gr_edi_aade_id` | l10n_gr_edi |
| `l10n_gr_edi_aade_key` |  | `company_id.l10n_gr_edi_aade_key` | l10n_gr_edi |
| `l10n_gr_edi_branch_number` |  | `company_id.l10n_gr_edi_branch_number` | l10n_gr_edi |
| `l10n_gr_edi_test_env` |  | `company_id.l10n_gr_edi_test_env` | l10n_gr_edi |
| `l10n_hr_mer_company_bu` |  | `company_id.partner_id.l10n_hr_business_unit_code` | l10n_hr_edi |
| `l10n_hr_mer_company_ident` |  | `company_id.l10n_hr_mer_company_ident` | l10n_hr_edi |
| `l10n_hr_mer_connection_mode` |  | `company_id.l10n_hr_mer_connection_mode` | l10n_hr_edi |
| `l10n_hr_mer_connection_state` |  | `company_id.l10n_hr_mer_connection_state` | l10n_hr_edi |
| `l10n_hr_mer_password` |  | `company_id.l10n_hr_mer_password` | l10n_hr_edi |
| `l10n_hr_mer_purchase_journal_id` |  | `company_id.l10n_hr_mer_purchase_journal_id` | l10n_hr_edi |
| `l10n_hr_mer_software_ident` |  | `company_id.l10n_hr_mer_software_ident` | l10n_hr_edi |
| `l10n_hr_mer_username` |  | `company_id.l10n_hr_mer_username` | l10n_hr_edi |
| `l10n_hu_edi_is_active` |  | computed by the screen | l10n_hu_edi |
| `l10n_hu_edi_password` |  | `company_id.l10n_hu_edi_password` | l10n_hu_edi |
| `l10n_hu_edi_replacement_key` |  | `company_id.l10n_hu_edi_replacement_key` | l10n_hu_edi |
| `l10n_hu_edi_server_mode` |  | `company_id.l10n_hu_edi_server_mode` | l10n_hu_edi |
| `l10n_hu_edi_signature_key` |  | `company_id.l10n_hu_edi_signature_key` | l10n_hu_edi |
| `l10n_hu_edi_username` |  | `company_id.l10n_hu_edi_username` | l10n_hu_edi |
| `l10n_hu_tax_regime` |  | `company_id.l10n_hu_tax_regime` | l10n_hu_edi |
| `l10n_in_composition_tax_rate` |  | `company_id.l10n_in_composition_tax_rate` | l10n_in |
| `l10n_in_disable_b2c_hsn_reporting` |  | `company_id.l10n_in_disable_b2c_hsn_reporting` | l10n_in |
| `l10n_in_edi_feature` |  | `company_id.l10n_in_edi_feature` | l10n_in_edi |
| `l10n_in_edi_password` | Indian EDI password | `company_id.l10n_in_edi_password` | l10n_in_edi |
| `l10n_in_edi_production_env` | Indian Production Environment | `company_id.l10n_in_edi_production_env` | l10n_in |
| `l10n_in_edi_username` | Indian EDI username | `company_id.l10n_in_edi_username` | l10n_in_edi |
| `l10n_in_enet_vendor_batch_payment_feature` | ENet Vendor Batch Payment | computed by the screen | l10n_in |
| `l10n_in_ewaybill_feature` |  | `company_id.l10n_in_ewaybill_feature` | l10n_in_ewaybill |
| `l10n_in_ewaybill_password` | Indian Ewaybill password | `company_id.l10n_in_ewaybill_password` | l10n_in_ewaybill |
| `l10n_in_ewaybill_username` | Indian Ewaybill username | `company_id.l10n_in_ewaybill_username` | l10n_in_ewaybill |
| `l10n_in_fetch_vendor_edi_feature` | Fetch Vendor E-Invoiced Document | computed by the screen | l10n_in |
| `l10n_in_gsp` | GSP | computed by the screen | l10n_in |
| `l10n_in_gst_efiling_feature` | GST Reports & E-Filing | computed by the screen | l10n_in |
| `l10n_in_gst_registration_type` |  | `company_id.l10n_in_gst_registration_type` | l10n_in |
| `l10n_in_gstin` | GST Number | `company_id.vat` | l10n_in |
| `l10n_in_gstin_status_feature` |  | `company_id.l10n_in_gstin_status_feature` | l10n_in |
| `l10n_in_hsn_code_digit` |  | `company_id.l10n_in_hsn_code_digit` | l10n_in |
| `l10n_in_tan` |  | `company_id.l10n_in_tan` | l10n_in |
| `l10n_in_tcs_feature` |  | `company_id.l10n_in_tcs_feature` | l10n_in |
| `l10n_in_tds_feature` |  | `company_id.l10n_in_tds_feature` | l10n_in |
| `l10n_in_upi_id` |  | `company_id.l10n_in_upi_id` | l10n_in |
| `l10n_in_withholding_journal_id` |  | `company_id.l10n_in_withholding_journal_id` | l10n_in |
| `l10n_it_edi_purchase_journal_id` |  | `company_id.l10n_it_edi_purchase_journal_id` | l10n_it_edi |
| `l10n_it_edi_register` |  | computed by the screen | l10n_it_edi |
| `l10n_it_edi_show_purchase_journal_id` |  | computed by the screen | l10n_it_edi |
| `l10n_jo_edi_client_identifier` | JoFotara Client ID | `company_id.l10n_jo_edi_client_identifier` | l10n_jo_edi |
| `l10n_jo_edi_demo_mode` | JoFotara Demo Mode | `company_id.l10n_jo_edi_demo_mode` | l10n_jo_edi |
| `l10n_jo_edi_pos_enabled` |  | `company_id.l10n_jo_edi_pos_enabled` | l10n_jo_edi_pos |
| `l10n_jo_edi_pos_testing_mode` |  | `company_id.l10n_jo_edi_pos_testing_mode` | l10n_jo_edi_pos |
| `l10n_jo_edi_secret_key` | JoFotara Secret Key | `company_id.l10n_jo_edi_secret_key` | l10n_jo_edi |
| `l10n_jo_edi_sequence_income_source` | JoFotara Sequence of Income Source | `company_id.l10n_jo_edi_sequence_income_source` | l10n_jo_edi |
| `l10n_jo_edi_taxpayer_type` | JoFotara Taxpayer Type | `company_id.l10n_jo_edi_taxpayer_type` | l10n_jo_edi |
| `l10n_ke_cu_proxy_address` |  | `company_id.l10n_ke_cu_proxy_address` | l10n_ke_edi_tremol |
| `l10n_mx_account_income_return_discount_id` | Income Returns and Discounts Account | `company_id.l10n_mx_income_return_discount_account_id` | l10n_mx |
| `l10n_my_accept_processing` |  | computed by the screen | l10n_my_edi |
| `l10n_my_edi_company_vat` |  | `company_id.vat` | l10n_my_edi |
| `l10n_my_edi_default_import_journal_id` |  | `company_id.l10n_my_edi_default_import_journal_id` | l10n_my_edi |
| `l10n_my_edi_identification_number` |  | `company_id.l10n_my_identification_number` | l10n_my_edi |
| `l10n_my_edi_is_branch` |  | `company_id.l10n_my_edi_is_branch` | l10n_my_edi |
| `l10n_my_edi_is_sole_proprietor` |  | `company_id.l10n_my_edi_is_sole_proprietor` | l10n_my_edi |
| `l10n_my_edi_mode` |  | `company_id.l10n_my_edi_mode` | l10n_my_edi |
| `l10n_my_edi_parent_mode` | Parent MyInvois mode | `company_id.parent_id.l10n_my_edi_mode` | l10n_my_edi |
| `l10n_my_edi_proxy_user_id` |  | `company_id.l10n_my_edi_proxy_user_id` | l10n_my_edi |
| `l10n_my_edi_show_sole_proprietor` |  | computed by the screen | l10n_my_edi |
| `l10n_pk_edi_company_email` | Authorized Email | `company_id.email` | l10n_pk_edi |
| `l10n_pk_edi_enable` |  | `company_id.l10n_pk_edi_enable` | l10n_pk_edi |
| `l10n_pk_edi_production_auth_token` |  | `company_id.l10n_pk_edi_production_auth_token` | l10n_pk_edi |
| `l10n_pk_edi_test_auth_token` |  | `company_id.l10n_pk_edi_test_auth_token` | l10n_pk_edi |
| `l10n_pk_edi_test_vat` |  | `company_id.l10n_pk_edi_test_vat` | l10n_pk_edi |
| `l10n_pk_edi_whitelisted` |  | `company_id.l10n_pk_edi_whitelisted` | l10n_pk_edi |
| `l10n_pk_iap_server_ip` |  | `company_id.l10n_pk_iap_server_ip` | l10n_pk |
| `l10n_pl_edi_access_token` | KSeF Access Token | `company_id.l10n_pl_edi_access_token` | l10n_pl_edi |
| `l10n_pl_edi_certificate` |  | computed by the screen | l10n_pl_edi |
| `l10n_pl_edi_register` | Allow KSeF integration | `company_id.l10n_pl_edi_register` | l10n_pl_edi |
| `l10n_pl_reports_tax_office_id` |  | `company_id.l10n_pl_reports_tax_office_id` | l10n_pl |
| `l10n_ro_edi_access_expiry_date` |  | `company_id.l10n_ro_edi_access_expiry_date` | l10n_ro_edi |
| `l10n_ro_edi_access_token` |  | `company_id.l10n_ro_edi_access_token` | l10n_ro_edi |
| `l10n_ro_edi_anaf_imported_inv_journal_id` |  | `company_id.l10n_ro_edi_anaf_imported_inv_journal_id` | l10n_ro_edi |
| `l10n_ro_edi_callback_url` |  | `company_id.l10n_ro_edi_callback_url` | l10n_ro_edi |
| `l10n_ro_edi_client_id` |  | `company_id.l10n_ro_edi_client_id` | l10n_ro_edi |
| `l10n_ro_edi_client_secret` |  | `company_id.l10n_ro_edi_client_secret` | l10n_ro_edi |
| `l10n_ro_edi_refresh_expiry_date` |  | `company_id.l10n_ro_edi_refresh_expiry_date` | l10n_ro_edi |
| `l10n_ro_edi_refresh_token` |  | `company_id.l10n_ro_edi_refresh_token` | l10n_ro_edi |
| `l10n_ro_edi_test_env` |  | `company_id.l10n_ro_edi_test_env` | l10n_ro_edi |
| `l10n_rs_edi_api_key` |  | `company_id.l10n_rs_edi_api_key` | l10n_rs_edi |
| `l10n_rs_edi_demo_env` |  | `company_id.l10n_rs_edi_demo_env` | l10n_rs_edi |
| `l10n_sa_api_mode` |  | `company_id.l10n_sa_api_mode` | l10n_sa_edi |
| `l10n_tw_edi_ecpay_hashIV` |  | `company_id.l10n_tw_edi_ecpay_hashIV` | l10n_tw_edi_ecpay |
| `l10n_tw_edi_ecpay_hashkey` |  | `company_id.l10n_tw_edi_ecpay_hashkey` | l10n_tw_edi_ecpay |
| `l10n_tw_edi_ecpay_merchant_id` |  | `company_id.l10n_tw_edi_ecpay_merchant_id` | l10n_tw_edi_ecpay |
| `l10n_tw_edi_ecpay_staging_mode` |  | `company_id.l10n_tw_edi_ecpay_staging_mode` | l10n_tw_edi_ecpay |
| `l10n_vn_edi_default_symbol_id` | Default Symbol | `company_id.l10n_vn_edi_symbol_id` | l10n_vn_edi_viettel |
| `l10n_vn_edi_password` |  | `company_id.l10n_vn_edi_password` | l10n_vn_edi_viettel |
| `l10n_vn_edi_pos_default_symbol` | Default PoS Symbol | `company_id.l10n_vn_pos_default_symbol` | l10n_vn_edi_viettel_pos |
| `l10n_vn_edi_send_transfer_note` |  | `company_id.l10n_vn_edi_send_transfer_note` | l10n_vn_edi_viettel_stock |
| `l10n_vn_edi_stock_default_sinvoice_symbol_id` |  | `company_id.l10n_vn_edi_stock_default_sinvoice_symbol_id` | l10n_vn_edi_viettel_stock |
| `l10n_vn_edi_username` |  | `company_id.l10n_vn_edi_username` | l10n_vn_edi_viettel |
| `language_count` | Number of Languages | computed by the screen | base_setup |
| `language_ids` |  | `website_id.language_ids` | website |
| `lc_journal_id` | Default Journal | `company_id.lc_journal_id` | stock_landed_costs |
| `ldaps` | LDAP Parameters | `company_id.ldaps` | auth_ldap |
| `lead_enrich_auto` | Enrich lead automatically | parameter `crm.iap.lead.enrich.setting` | crm |
| `lead_mining_in_pipeline` | Create a lead mining request directly from the opportunity pipeline. | parameter `crm.lead_mining_in_pipeline` | crm |
| `leave_timesheet_task_id` | Time Off Task | `company_id.leave_timesheet_task_id` | project_timesheet_holidays |
| `link_qr_code` | Display Link QR-code | `company_id.link_qr_code` | account |
| `lock_confirmed_po` | Lock Confirmed Orders | computed by the screen | purchase |
| `mass_mailing_mail_server_id` | Mail Server | parameter `mass_mailing.mail_server_id` | mass_mailing |
| `mass_mailing_outgoing_mail_server` | Dedicated Server | parameter `mass_mailing.outgoing_mail_server` | mass_mailing |
| `mass_mailing_reports` | 24H Stat Mailing Reports | parameter `mass_mailing.mass_mailing_reports` | mass_mailing |
| `mass_mailing_split_contact_name` | Split First and Last Name | computed by the screen | mass_mailing |
| `microsoft_outlook_client_identifier` | Outlook Client Id | parameter `microsoft_outlook_client_id` | microsoft_outlook |
| `microsoft_outlook_client_secret` | Outlook Client Secret | parameter `microsoft_outlook_client_secret` | microsoft_outlook |
| `minlength` | Minimum Password Length | parameter `auth_password_policy.minlength` | auth_password_policy |
| `module_account_3way_match` | 3-way matching: purchases, receptions and bills | installs `account_3way_match` | purchase |
| `module_account_accountant` | Accounting | installs `account_accountant` | account |
| `module_account_avatax` | AvaTax | installs `account_avatax` | account |
| `module_account_bank_statement_extract` | Bank Statement Digitization | installs `account_bank_statement_extract` | account |
| `module_account_bank_statement_import_qif` | Import .qif files | installs `account_bank_statement_import_qif` | account |
| `module_account_batch_payment` | Use batch payments | installs `account_batch_payment` | account |
| `module_account_budget` | Budget Management | installs `account_budget` | account |
| `module_account_check_printing` | Allow check printing and deposits | installs `account_check_printing` | account |
| `module_account_extract` | Document Digitization | installs `account_extract` | account |
| `module_account_inter_company_rules` | Manage Inter Company | installs `account_inter_company_rules` | base_setup |
| `module_account_intrastat` | Intrastat | installs `account_intrastat` | account |
| `module_account_invoice_extract` | Invoice Digitization | installs `account_invoice_extract` | account |
| `module_account_iso20022` | SEPA Credit Transfer / ISO20022 | installs `account_iso20022` | account |
| `module_account_loan_extract` | Loans Digitization | installs `account_loan_extract` | account |
| `module_account_payment` | Invoice Online Payment | installs `account_payment` | account |
| `module_account_peppol` | PEPPOL Invoicing | installs `account_peppol` | account |
| `module_account_sepa_direct_debit` | Use SEPA Direct Debit | installs `account_sepa_direct_debit` | account |
| `module_auth_ldap` | LDAP Authentication | installs `auth_ldap` | base_setup |
| `module_auth_oauth` | Use external authentication providers (OAuth) | installs `auth_oauth` | base_setup |
| `module_base_geolocalize` | GeoLocalize | installs `base_geolocalize` | base_setup |
| `module_base_import` | Allow users to import data from CSV/XLS/XLSX/ODS files | installs `base_import` | base_setup |
| `module_crm_iap_enrich` | Enrich your leads automatically with company data based on their email address. | installs `crm_iap_enrich` | crm |
| `module_crm_iap_mine` | Generate new leads based on their country, industries, size, etc. | installs `crm_iap_mine` | crm |
| `module_currency_rate_live` | Automatic Currency Rates | installs `currency_rate_live` | account |
| `module_delivery` | Delivery Methods | installs `delivery` | sale |
| `module_delivery` | Delivery Methods | installs `delivery` | stock |
| `module_event_booth` | Booth Management | installs `event_booth` | event |
| `module_event_sale` | Tickets with Sale | installs `event_sale` | event |
| `module_google_address_autocomplete` | Google Address Autocomplete | installs `google_address_autocomplete` | base_setup |
| `module_google_calendar` | Allow the users to synchronize their calendar  with Google Calendar | installs `google_calendar` | base_setup |
| `module_google_gmail` | Support Gmail Authentication | installs `google_gmail` | mail |
| `module_google_recaptcha` | reCAPTCHA | installs `google_recaptcha` | base_setup |
| `module_hr_expense_extract` | Send bills to OCR to generate expenses | installs `hr_expense_extract` | hr_expense |
| `module_hr_expense_stripe` | Link your stripe issuing account to manage company credit cards for your employees through Odoo | installs `hr_expense_stripe` | hr_expense |
| `module_hr_payroll_expense` | Reimburse Expenses in Payslip | installs `hr_payroll_expense` | hr_expense |
| `module_hr_presence` | Advanced Presence Control | installs `hr_presence` | hr |
| `module_hr_recruitment_extract` | Send CV to OCR to fill applications | installs `hr_recruitment_extract` | hr_recruitment |
| `module_hr_recruitment_survey` | Interview Forms | installs `hr_recruitment_survey` | hr_recruitment |
| `module_hr_skills` | Skills Management | installs `hr_skills` | hr |
| `module_hr_timesheet` | Task Logs | installs `hr_timesheet` | project |
| `module_l10n_at_pos` | Austria Fiscalization | installs `l10n_at_pos` | point_of_sale |
| `module_l10n_ca_payment_cpa005` | Canadian CPA005 Payments (EFT/PAD) | installs `l10n_ca_payment_cpa005` | l10n_ca |
| `module_l10n_es_edi_sii` | SII | installs `l10n_es_edi_sii` | l10n_es |
| `module_l10n_es_edi_tbai` | TicketBai | installs `l10n_es_edi_tbai` | l10n_es |
| `module_l10n_es_edi_verifactu` | Veri*Factu | installs `l10n_es_edi_verifactu` | l10n_es |
| `module_l10n_eu_account_vies` | VAT number validation with VIES | installs `l10n_eu_account_vies` | account |
| `module_l10n_in_boe` | Bill of Entry | installs `l10n_in_boe` | l10n_in |
| `module_l10n_in_edi` | Indian Electronic Invoicing | installs `l10n_in_edi` | l10n_in |
| `module_l10n_in_ewaybill` | Indian Electronic Waybill | installs `l10n_in_ewaybill` | l10n_in |
| `module_l10n_in_reports` | GST E-Filing & Matching | installs `l10n_in_reports` | l10n_in |
| `module_l10n_ph_invoice` | Discount Privileges on Invoices | installs `l10n_ph_invoice` | l10n_ph |
| `module_l10n_ph_sale` | Discount Privileges on Sale Orders | installs `l10n_ph_sale` | l10n_ph |
| `module_l10n_us_direct_deposit` | U.S. Direct Deposit (via Wise) | installs `l10n_us_direct_deposit` | l10n_us_account |
| `module_loyalty` | Promotions, Coupons, Gift Card & Loyalty Program | installs `loyalty` | product |
| `module_maintenance_worksheet` | Custom Maintenance Worksheets | installs `maintenance_worksheet` | maintenance |
| `module_mass_mailing_slides` | Mailing | installs `mass_mailing_slides` | website_slides |
| `module_microsoft_calendar` | Allow the users to synchronize their calendar with Outlook Calendar | installs `microsoft_calendar` | base_setup |
| `module_microsoft_outlook` | Support Outlook Authentication | installs `microsoft_outlook` | mail |
| `module_mrp_mps` | Master Production Schedule | installs `mrp_mps` | mrp |
| `module_mrp_plm` | Product Lifecycle Management (PLM) | installs `mrp_plm` | mrp |
| `module_mrp_subcontracting` | Subcontracting | installs `mrp_subcontracting` | mrp |
| `module_partner_autocomplete` | Partner Autocomplete | installs `partner_autocomplete` | base_setup |
| `module_partnership` | Membership / Partnership | installs `partnership` | crm |
| `module_pos_adyen` | Adyen Payment Terminal | installs `pos_adyen` | point_of_sale |
| `module_pos_dpopay` | DPO Pay Payment Terminal | installs `pos_dpopay` | point_of_sale |
| `module_pos_event` | Tickets with PoS | installs `pos_event` | event |
| `module_pos_mercado_pago` | Mercado Pago Payment Terminal | installs `pos_mercado_pago` | point_of_sale |
| `module_pos_pine_labs` | Pine Labs Payment Terminal | installs `pos_pine_labs` | point_of_sale |
| `module_pos_pricer` | Pricer electronic price tags | installs `pos_pricer` | point_of_sale |
| `module_pos_qfpay` | QFPay Payment Terminal | installs `pos_qfpay` | point_of_sale |
| `module_pos_razorpay` | Razorpay Payment Terminal | installs `pos_razorpay` | point_of_sale |
| `module_pos_stripe` | Stripe Payment Terminal | installs `pos_stripe` | point_of_sale |
| `module_pos_viva_com` | Viva.com Payment Terminal | installs `pos_viva_com` | point_of_sale |
| `module_product_barcodelookup` | Barcode Database | installs `product_barcodelookup` | product |
| `module_product_email_template` | Specific Email | installs `product_email_template` | sale |
| `module_product_expiry` | Expiration Dates | installs `product_expiry` | stock |
| `module_product_margin` | Allow Product Margin | installs `product_margin` | account |
| `module_project_timesheet_holidays` | Time Off | installs `project_timesheet_holidays` | hr_timesheet |
| `module_purchase_alternative` | Purchase Alternative | installs `purchase_alternative` | purchase |
| `module_purchase_product_matrix` | Purchase Grid Entry | installs `purchase_product_matrix` | purchase |
| `module_purchase_requisition` | Purchase Agreements | installs `purchase_requisition` | purchase |
| `module_quality_control` | Quality | installs `quality_control` | mrp |
| `module_quality_control` | Quality | installs `quality_control` | stock |
| `module_quality_control_worksheet` | Quality Worksheet | installs `quality_control_worksheet` | mrp |
| `module_quality_control_worksheet` | Quality Worksheet | installs `quality_control_worksheet` | stock |
| `module_sale_amazon` | Amazon Sync | installs `sale_amazon` | sale |
| `module_sale_commission` | Commissions | installs `sale_commission` | sale |
| `module_sale_gelato` | Gelato | installs `sale_gelato` | sale |
| `module_sale_loyalty` | Coupons & Loyalty | installs `sale_loyalty` | sale |
| `module_sale_pdf_quote_builder` | PDF Quote builder | installs `sale_pdf_quote_builder` | sale |
| `module_sale_product_matrix` | Sales Grid Entry | installs `sale_product_matrix` | sale |
| `module_sale_shopee` | Shopee Sync | installs `sale_shopee` | sale |
| `module_sms` | SMS | installs `sms` | base_setup |
| `module_snailmail_account` | Snailmail | installs `snailmail_account` | account |
| `module_stock_barcode` | Barcode Scanner | installs `stock_barcode` | stock |
| `module_stock_barcode_barcodelookup` | Stock Barcode Database | installs `stock_barcode_barcodelookup` | stock |
| `module_stock_dropshipping` | Dropshipping | installs `stock_dropshipping` | purchase_stock |
| `module_stock_dropshipping` | Dropshipping | installs `stock_dropshipping` | stock |
| `module_stock_fleet` | Transport Management | installs `stock_fleet` | stock |
| `module_stock_landed_costs` | Landed Costs | installs `stock_landed_costs` | stock_account |
| `module_stock_sms` | SMS Confirmation | installs `stock_sms` | stock |
| `module_voip` | Phone | installs `voip` | base_setup |
| `module_web_unsplash` | Unsplash Image Library | installs `web_unsplash` | base_setup |
| `module_website_address_autocomplete` | Website Address Autocomplete | installs `website_address_autocomplete` | website |
| `module_website_cf_turnstile` | Cloudflare Turnstile | installs `website_cf_turnstile` | base_setup |
| `module_website_crm_iap_reveal` | Create Leads/Opportunities from your website's traffic | installs `website_crm_iap_reveal` | crm |
| `module_website_event_exhibitor` | Advanced Sponsors | installs `website_event_exhibitor` | event |
| `module_website_event_sale` | Online Ticketing | installs `website_event_sale` | event |
| `module_website_event_track` | Tracks and Agenda | installs `website_event_track` | event |
| `module_website_event_track_live` | Live Mode | installs `website_event_track_live` | event |
| `module_website_event_track_quiz` | Quiz on Tracks | installs `website_event_track_quiz` | event |
| `module_website_hr_recruitment` | Online Posting | installs `website_hr_recruitment` | hr_recruitment |
| `module_website_livechat` |  | installs `website_livechat` | website |
| `module_website_partnership` | Partners Website Page | installs `website_partnership` | crm |
| `module_website_sale_collect` | Click & Collect | installs `website_sale_collect` | website_sale |
| `module_website_sale_slides` | Sell on eCommerce | installs `website_sale_slides` | website_slides |
| `module_website_slides_forum` | Forum | installs `website_slides_forum` | website_slides |
| `module_website_slides_survey` | Certifications | installs `website_slides_survey` | website_slides |
| `nemhandel_contact_email` |  | `company_id.nemhandel_contact_email` | l10n_dk |
| `nemhandel_edi_identification` | Nemhandel identification | `nemhandel_edi_user.edi_identification` | l10n_dk |
| `nemhandel_edi_mode` | Nemhandel EDI operating mode | `nemhandel_edi_user.edi_mode` | l10n_dk |
| `nemhandel_edi_user` |  | `company_id.nemhandel_edi_user` | l10n_dk |
| `nemhandel_identifier_type` |  | `company_id.nemhandel_identifier_type` | l10n_dk |
| `nemhandel_identifier_value` |  | `company_id.nemhandel_identifier_value` | l10n_dk |
| `nemhandel_phone_number` |  | `company_id.nemhandel_phone_number` | l10n_dk |
| `nemhandel_purchase_journal_id` |  | `company_id.nemhandel_purchase_journal_id` | l10n_dk |
| `newsletter_id` |  | `website_id.newsletter_id` | website_sale_mass_mailing |
| `onboarding_payment_module` |  | `company_id.onboarding_payment_module` | payment |
| `partner_autocomplete_insufficient_credit` | Insufficient credit | computed by the screen | partner_autocomplete |
| `partnership_label` |  | `company_id.partnership_label` | partnership |
| `pay_invoices_online` |  | parameter `account_payment.enable_portal_payment` | account_payment |
| `peppol_external_provider` |  | `company_id.peppol_external_provider` | account_peppol |
| `peppol_parent_company_name` |  | computed by the screen | account_peppol |
| `peppol_participation_role` |  | computed by the screen | account_peppol |
| `peppol_purchase_journal_required` |  | computed by the screen | account_peppol |
| `peppol_use_parent_company` |  | computed by the screen | account_peppol |
| `picking_policy` |  | `company_id.picking_policy` | stock |
| `plausible_shared_key` | Plausible auth Key | `website_id.plausible_shared_key` | website |
| `plausible_site` | Plausible Site (e.g. domain.com) | `website_id.plausible_site` | website |
| `po_double_validation` | Levels of Approvals * | `company_id.po_double_validation` | purchase |
| `po_double_validation_amount` | Minimum Amount | `company_id.po_double_validation_amount` | purchase |
| `po_lock` | Purchase Order Modification * | `company_id.po_lock` | purchase |
| `po_order_approval` | Purchase Order Approval | computed by the screen | purchase |
| `point_of_sale_ticket_portal_url_display_mode` |  | `company_id.point_of_sale_ticket_portal_url_display_mode` | point_of_sale |
| `point_of_sale_ticket_unique_code` |  | `company_id.point_of_sale_ticket_unique_code` | point_of_sale |
| `point_of_sale_use_ticket_qr_code` |  | `company_id.point_of_sale_use_ticket_qr_code` | point_of_sale |
| `portal_allow_api_keys` | Customer API Keys | parameter `portal.allow_api_keys` | portal |
| `portal_confirmation_pay` |  | `company_id.portal_confirmation_pay` | sale |
| `portal_confirmation_sign` |  | `company_id.portal_confirmation_sign` | sale |
| `pos_adyen_ask_customer_for_tip` |  | computed by the screen | pos_adyen |
| `pos_allowed_pricelist_ids` |  | computed by the screen | point_of_sale |
| `pos_amount_authorized_diff` |  | `pos_config_id.amount_authorized_diff` | point_of_sale |
| `pos_auto_validate_electronic_payment` | Automatically validates orders paid with an electronic payment (terminals, qr codes, ...). | `pos_config_id.auto_validate_electronic_payment` | point_of_sale |
| `pos_available_preset_ids` |  | `pos_config_id.available_preset_ids` | point_of_sale |
| `pos_available_pricelist_ids` | Available Pricelists | computed by the screen | point_of_sale |
| `pos_basic_receipt` |  | `pos_config_id.basic_receipt` | point_of_sale |
| `pos_cash_control` |  | `pos_config_id.cash_control` | point_of_sale |
| `pos_cash_rounding` | Total Rounding (PoS) | `pos_config_id.cash_rounding` | point_of_sale |
| `pos_cashier_employee_ids` |  | `pos_config_id.cashier_employee_ids` | pos_hr |
| `pos_closing_journal_id` |  | `pos_config_id.closing_journal_id` | point_of_sale |
| `pos_company_has_template` |  | `pos_config_id.company_has_template` | point_of_sale |
| `pos_config_id` | Point of Sale | computed by the screen | point_of_sale |
| `pos_crm_team_id` | Sales Team (PoS) | `pos_config_id.crm_team_id` | pos_sale |
| `pos_custom_email` | email placeholder | `pos_config_id.custom_email` | point_of_sale |
| `pos_custom_logo` |  | `pos_config_id.custom_logo` | point_of_sale |
| `pos_custom_logo_name` |  | `pos_config_id.custom_logo_name` | point_of_sale |
| `pos_custom_phone` |  | `pos_config_id.custom_phone` | point_of_sale |
| `pos_custom_receipt_address` |  | `pos_config_id.custom_receipt_address` | point_of_sale |
| `pos_custom_website` |  | `pos_config_id.custom_website` | point_of_sale |
| `pos_customer_display_bg_img` |  | `pos_config_id.customer_display_bg_img` | point_of_sale |
| `pos_customer_display_bg_img_name` |  | `pos_config_id.customer_display_bg_img_name` | point_of_sale |
| `pos_default_bill_ids` |  | `pos_config_id.default_bill_ids` | point_of_sale |
| `pos_default_fiscal_position_id` | Default Fiscal Position | computed by the screen | point_of_sale |
| `pos_default_partner_id` |  | `pos_config_id.default_partner_id` | point_of_sale |
| `pos_default_preset_id` |  | `pos_config_id.default_preset_id` | point_of_sale |
| `pos_default_product_id` |  | `pos_config_id.default_product_id` | pos_sale |
| `pos_default_screen` |  | `pos_config_id.default_screen` | pos_restaurant |
| `pos_discount_pc` |  | `pos_config_id.discount_pc` | pos_discount |
| `pos_discount_product_id` |  | computed by the screen | pos_discount |
| `pos_down_payment_product_id` |  | `pos_config_id.down_payment_product_id` | pos_sale |
| `pos_fallback_nomenclature_id` |  | `pos_config_id.fallback_nomenclature_id` | point_of_sale |
| `pos_fast_payment_method_ids` |  | `pos_config_id.fast_payment_method_ids` | point_of_sale |
| `pos_fiscal_position_ids` | Fiscal Positions | computed by the screen | point_of_sale |
| `pos_floor_ids` |  | `pos_config_id.floor_ids` | pos_restaurant |
| `pos_has_active_session` |  | `pos_config_id.has_active_session` | point_of_sale |
| `pos_iface_available_categ_ids` | Available PoS Product Categories | computed by the screen | point_of_sale |
| `pos_iface_big_scrollbars` |  | `pos_config_id.iface_big_scrollbars` | point_of_sale |
| `pos_iface_group_by_categ` |  | `pos_config_id.iface_group_by_categ` | point_of_sale |
| `pos_iface_print_auto` |  | `pos_config_id.iface_print_auto` | point_of_sale |
| `pos_iface_printbill` |  | `pos_config_id.iface_printbill` | point_of_sale |
| `pos_iface_tax_included` |  | `pos_config_id.iface_tax_included` | point_of_sale |
| `pos_iface_tipproduct` |  | `pos_config_id.iface_tipproduct` | point_of_sale |
| `pos_is_margins_costs_accessible_to_every_user` |  | `pos_config_id.is_margins_costs_accessible_to_every_user` | point_of_sale |
| `pos_journal_id` |  | `pos_config_id.journal_id` | point_of_sale |
| `pos_l10n_eg_edi_pos_client_id` |  | `pos_config_id.l10n_eg_edi_pos_client_id` | l10n_eg_edi_pos |
| `pos_l10n_eg_edi_pos_client_secret` |  | `pos_config_id.l10n_eg_edi_pos_client_secret` | l10n_eg_edi_pos |
| `pos_l10n_eg_edi_pos_enable` |  | `pos_config_id.l10n_eg_edi_pos_enable` | l10n_eg_edi_pos |
| `pos_l10n_eg_edi_pos_preprod` |  | `pos_config_id.l10n_eg_edi_pos_preprod` | l10n_eg_edi_pos |
| `pos_l10n_eg_edi_pos_serial_number` |  | `pos_config_id.l10n_eg_edi_pos_serial_number` | l10n_eg_edi_pos |
| `pos_l10n_es_simplified_invoice_journal_id` |  | `pos_config_id.l10n_es_simplified_invoice_journal_id` | l10n_es_pos |
| `pos_l10n_pk_edi_pos_charge_service_fee` |  | `pos_config_id.l10n_pk_edi_pos_charge_service_fee` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_enabled` |  | `pos_config_id.l10n_pk_edi_pos_enabled` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_identifier` |  | `pos_config_id.l10n_pk_edi_pos_identifier` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_sandbox` |  | `pos_config_id.l10n_pk_edi_pos_sandbox` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_service_fee_product_id` |  | `pos_config_id.l10n_pk_edi_pos_service_fee_product_id` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_test_identifier` |  | `pos_config_id.l10n_pk_edi_pos_test_identifier` | l10n_pk_edi_pos |
| `pos_l10n_pk_edi_pos_token` |  | `pos_config_id.l10n_pk_edi_pos_token` | l10n_pk_edi_pos |
| `pos_l10n_vn_auto_send_to_sinvoice` |  | `pos_config_id.l10n_vn_auto_send_to_sinvoice` | l10n_vn_edi_viettel_pos |
| `pos_l10n_vn_pos_symbol` |  | `pos_config_id.l10n_vn_pos_symbol` | l10n_vn_edi_viettel_pos |
| `pos_limit_categories` |  | `pos_config_id.limit_categories` | point_of_sale |
| `pos_manager_employee_ids` |  | `pos_config_id.manager_employee_ids` | pos_hr |
| `pos_manual_discount` |  | `pos_config_id.manual_discount` | point_of_sale |
| `pos_module_pos_appointment` |  | `pos_config_id.module_pos_appointment` | point_of_sale |
| `pos_module_pos_avatax` |  | `pos_config_id.module_pos_avatax` | point_of_sale |
| `pos_module_pos_discount` |  | `pos_config_id.module_pos_discount` | point_of_sale |
| `pos_module_pos_hr` |  | `pos_config_id.module_pos_hr` | point_of_sale |
| `pos_module_pos_restaurant` |  | `pos_config_id.module_pos_restaurant` | point_of_sale |
| `pos_module_pos_sms` |  | `pos_config_id.module_pos_sms` | point_of_sale |
| `pos_note_ids` |  | `pos_config_id.note_ids` | point_of_sale |
| `pos_only_round_cash_method` |  | `pos_config_id.only_round_cash_method` | point_of_sale |
| `pos_other_devices` |  | `pos_config_id.other_devices` | point_of_sale |
| `pos_payment_method_ids` |  | `pos_config_id.payment_method_ids` | point_of_sale |
| `pos_picking_policy` |  | `pos_config_id.picking_policy` | pos_stock |
| `pos_picking_type_id` |  | `pos_config_id.picking_type_id` | pos_stock |
| `pos_preparation_devices` |  | `pos_config_id.preparation_devices` | point_of_sale |
| `pos_preparation_printer_ids` |  | `pos_config_id.preparation_printer_ids` | point_of_sale |
| `pos_pricelist_id` | Default Pricelist | computed by the screen | point_of_sale |
| `pos_receipt_footer` | Receipt Footer | computed by the screen | point_of_sale |
| `pos_receipt_header` | Receipt Header | computed by the screen | point_of_sale |
| `pos_receipt_printer_ids` |  | `pos_config_id.receipt_printer_ids` | point_of_sale |
| `pos_restrict_price_control` |  | `pos_config_id.restrict_price_control` | point_of_sale |
| `pos_restrictive_employee_ids` |  | `pos_config_id.restrictive_employee_ids` | pos_hr |
| `pos_rounding_method` |  | `pos_config_id.rounding_method` | point_of_sale |
| `pos_route_id` |  | `pos_config_id.route_id` | pos_stock |
| `pos_selectable_categ_ids` |  | computed by the screen | point_of_sale |
| `pos_self_order_online_payment_method_id` |  | `pos_config_id.self_order_online_payment_method_id` | pos_online_payment_self_order |
| `pos_self_ordering_available_language_ids` |  | `pos_config_id.self_ordering_available_language_ids` | pos_self_order |
| `pos_self_ordering_default_language_id` |  | `pos_config_id.self_ordering_default_language_id` | pos_self_order |
| `pos_self_ordering_default_user_id` |  | `pos_config_id.self_ordering_default_user_id` | pos_self_order |
| `pos_self_ordering_image_background_ids` |  | `pos_config_id.self_ordering_image_background_ids` | pos_self_order |
| `pos_self_ordering_image_brand` |  | `pos_config_id.self_ordering_image_brand` | pos_self_order |
| `pos_self_ordering_image_brand_name` |  | `pos_config_id.self_ordering_image_brand_name` | pos_self_order |
| `pos_self_ordering_image_home_ids` |  | `pos_config_id.self_ordering_image_home_ids` | pos_self_order |
| `pos_self_ordering_mode` |  | `pos_config_id.self_ordering_mode` | pos_self_order |
| `pos_self_ordering_pay_after` |  | `pos_config_id.self_ordering_pay_after` | pos_self_order |
| `pos_self_ordering_primary_color` |  | `pos_config_id.self_ordering_primary_color` | pos_self_order |
| `pos_self_ordering_service_mode` |  | `pos_config_id.self_ordering_service_mode` | pos_self_order |
| `pos_session_closing_daily_hour` |  | `pos_config_id.session_closing_daily_hour` | point_of_sale |
| `pos_session_closing_mode` |  | `pos_config_id.session_closing_mode` | point_of_sale |
| `pos_set_maximum_difference` |  | `pos_config_id.set_maximum_difference` | point_of_sale |
| `pos_set_tip_after_payment` |  | `pos_config_id.set_tip_after_payment` | point_of_sale |
| `pos_ship_later` |  | `pos_config_id.ship_later` | pos_stock |
| `pos_show_category_images` |  | `pos_config_id.show_category_images` | point_of_sale |
| `pos_show_product_images` |  | `pos_config_id.show_product_images` | point_of_sale |
| `pos_sms_receipt_template_id` |  | `pos_config_id.sms_receipt_template_id` | pos_sms |
| `pos_supervised_employee_ids` |  | `pos_config_id.supervised_employee_ids` | pos_hr |
| `pos_tax_regime_selection` |  | `pos_config_id.tax_regime_selection` | point_of_sale |
| `pos_tip_percentage_1` |  | `pos_config_id.tip_percentage_1` | point_of_sale |
| `pos_tip_percentage_2` |  | `pos_config_id.tip_percentage_2` | point_of_sale |
| `pos_tip_percentage_3` |  | `pos_config_id.tip_percentage_3` | point_of_sale |
| `pos_tip_product_id` |  | `pos_config_id.tip_product_id` | point_of_sale |
| `pos_trusted_config_ids` |  | `pos_config_id.trusted_config_ids` | point_of_sale |
| `pos_use_closing_entry_by_product` |  | `pos_config_id.use_closing_entry_by_product` | point_of_sale |
| `pos_use_course_allocation` |  | `pos_config_id.use_course_allocation` | pos_restaurant |
| `pos_use_custom_receipt_info` |  | `pos_config_id.use_custom_receipt_info` | point_of_sale |
| `pos_use_download_invoice` |  | `pos_config_id.use_download_invoice` | point_of_sale |
| `pos_use_fast_payment` |  | `pos_config_id.use_fast_payment` | point_of_sale |
| `pos_use_header_or_footer` |  | `pos_config_id.use_header_or_footer` | point_of_sale |
| `pos_use_presets` |  | `pos_config_id.use_presets` | point_of_sale |
| `pos_use_pricelist` |  | `pos_config_id.use_pricelist` | point_of_sale |
| `pos_use_show_items_on_course_ticket` |  | `pos_config_id.use_show_items_on_course_ticket` | pos_restaurant |
| `pos_warehouse_id` | Warehouse (PoS) | `pos_config_id.warehouse_id` | pos_stock |
| `predictive_lead_scoring_field_labels` |  | computed by the screen | crm |
| `predictive_lead_scoring_fields` | Lead Scoring Frequency Fields | computed by the screen | crm |
| `predictive_lead_scoring_fields_str` | Lead Scoring Frequency Fields in String | parameter `crm.pls_fields` | crm |
| `predictive_lead_scoring_start_date` | Lead Scoring Starting Date | computed by the screen | crm |
| `predictive_lead_scoring_start_date_str` | Lead Scoring Starting Date in String | parameter `crm.pls_start_date` | crm |
| `prepayment_percent` |  | `company_id.prepayment_percent` | sale |
| `prevent_sale` |  | `website_id.prevent_sale` | website_sale |
| `prevent_sale_for` |  | `website_id.prevent_sale_for` | website_sale |
| `prevent_sale_for_categories` |  | `website_id.prevent_sale_for_categories` | website_sale |
| `preview_ready` | Display preview button | computed by the screen | account |
| `product_volume_volume_in_cubic_feet` |  | parameter `product.volume_in_cubic_feet` | product |
| `product_weight_in_lbs` |  | parameter `product.weight_in_lbs` | product |
| `profiling_enabled_until` | Profiling enabled until | parameter `base.profiling_enabled_until` | base_setup |
| `project_time_mode_id` | Project Time Unit | `company_id.project_time_mode_id` | hr_timesheet |
| `purchase_tax_id` | Default Purchase Tax | `company_id.account_purchase_tax_id` | account |
| `qr_code` | Display SEPA QR-code | `company_id.qr_code` | account |
| `quick_edit_mode` |  | `company_id.quick_edit_mode` | account |
| `quick_edit_mode_enabled` | Quick encoding | `company_id.quick_edit_mode_enabled` | account |
| `quotation_validity_days` |  | `company_id.quotation_validity_days` | sale |
| `rating_email_delay` |  | `website_id.rating_email_delay` | website_sale |
| `rating_email_template_id` |  | `website_id.rating_email_template_id` | website_sale |
| `recaptcha_min_score` | Minimum score | parameter `recaptcha_min_score` | google_recaptcha |
| `recaptcha_private_key` | Secret Key | parameter `recaptcha_private_key` | google_recaptcha |
| `recaptcha_public_key` | Site Key | parameter `recaptcha_public_key` | google_recaptcha |
| `reminder_allow` | Approver Reminder | computed by the screen | hr_timesheet |
| `reminder_user_allow` | Employee Reminder | computed by the screen | hr_timesheet |
| `replenish_on_order` | Replenish on Order (MTO) | computed by the screen | stock |
| `report_footer` | Custom Report Footer | `company_id.report_footer` | base_setup |
| `resource_calendar_id` |  | `company_id.resource_calendar_id` | hr |
| `restrict_template_rendering` | Restrict Template Rendering | parameter `mail.restrict.template.rendering` | mail |
| `restricted_uom_ids` |  | `website_id.restricted_uom_ids` | website_sale |
| `restrictive_audit_trail` | Restricted Audit Trail | `company_id.restrictive_audit_trail` | account |
| `return_validity_days` |  | `company_id.return_validity_days` | sale_stock |
| `routing_endpoint` | Routing Endpoint | `company_id.partner_id.routing_endpoint` | account_peppol |
| `routing_scheme` | Routing Scheme | `company_id.partner_id.routing_scheme` | account_peppol |
| `sale_automatic_invoice` |  | `company_id.sale_automatic_invoice` | sale |
| `sale_invoice_policy` |  | `company_id.sale_invoice_policy` | sale |
| `sale_order_mandatory_product` | Mandatory Product | parameter `sale.mandatory_product` | sale |
| `sale_tax_id` | Default Sale Tax | `company_id.account_sale_tax_id` | account |
| `sale_tax_id` | Default Sale Tax | `company_id.account_sale_tax_id` | point_of_sale |
| `salesperson_id` |  | `website_id.salesperson_id` | website_sale |
| `salesteam_id` |  | `website_id.salesteam_id` | website_sale |
| `security_lead` | Security Lead Time | `company_id.security_lead` | sale_stock |
| `send_abandoned_cart_followup` |  | `website_id.send_abandoned_cart_followup` | website_sale |
| `send_order_rating_emails` |  | `website_id.send_order_rating_emails` | website_sale |
| `server_uri_google` | Server uri | computed by the screen | auth_oauth |
| `set_to_review_documents` | Review data | `company_id.set_to_review_documents` | account |
| `sfu_client_source` | SFU Client Bundle | computed by the screen | mail |
| `sfu_server_key` | SFU Server key | parameter `mail.sfu_server_key` | mail |
| `sfu_server_url` | SFU Server URL | parameter `mail.sfu_server_url` | mail |
| `shared_user_account` | Shared Customer Accounts | computed by the screen | website |
| `show_blacklist_buttons` | Blacklist Option when Unsubscribing | parameter `mass_mailing.show_blacklist_buttons` | mass_mailing |
| `show_effect` | Show Effect | parameter `base_setup.show_effect` | base_setup |
| `show_line_subtotals_tax_selection` |  | `website_id.show_line_subtotals_tax_selection` | website_sale |
| `show_sale_receipts` | Sale Receipt | parameter `account.show_sale_receipts` | account |
| `show_sol_numbers` | Line Numbers | `company_id.show_sol_numbers` | sale |
| `simplified_invoice_journal_id` |  | `website_id.simplified_invoice_journal_id` | l10n_es_website_sale |
| `single_check_in` |  | `company_id.single_check_in` | hr_attendance |
| `sms_provider` |  | `company_id.sms_provider` | sms_twilio |
| `snailmail_color` | Print In Color | `company_id.snailmail_color` | snailmail |
| `snailmail_cover` | Add a Cover Page | `company_id.snailmail_cover` | snailmail |
| `snailmail_duplex` | Print Both sides | `company_id.snailmail_duplex` | snailmail |
| `social_default_image` | Default Social Share Image | `website_id.social_default_image` | website |
| `stock_confirmation_type` | Stock Text Validation type | `company_id.stock_confirmation_type` | stock |
| `stock_move_email_validation` |  | `company_id.stock_move_email_validation` | stock |
| `stock_sms_confirmation_template_id` |  | `company_id.stock_sms_confirmation_template_id` | stock_sms |
| `stock_text_confirmation` | Stock Text Validation with stock move | `company_id.stock_text_confirmation` | stock |
| `tax_calculation_rounding_method` | Tax calculation rounding method | `company_id.tax_calculation_rounding_method` | account |
| `tax_cash_basis_journal_id` | Tax Cash Basis Journal | `company_id.tax_cash_basis_journal_id` | account |
| `tax_exigibility` | Cash Basis | `company_id.tax_exigibility` | account |
| `tenor_api_key` | Klipy API key | parameter `discuss.klipy_api_key` | mail |
| `terms_type` |  | `company_id.terms_type` | account |
| `timesheet_encode_method` | Encoding Method | computed by the screen | hr_timesheet |
| `transfer_account_active` | Internal Transfer Account Active | `transfer_account_id.active` | account |
| `transfer_account_id` | Internal Transfer | `company_id.transfer_account_id` | account |
| `turnstile_secret_key` | CF Secret Key | parameter `cf.turnstile_secret_key` | website_cf_turnstile |
| `turnstile_site_key` | CF Site Key | parameter `cf.turnstile_site_key` | website_cf_turnstile |
| `twilio_account_sid` | Account SID | parameter `mail.twilio_account_sid` | mail |
| `twilio_account_token` | Account Auth Token | parameter `mail.twilio_account_token` | mail |
| `unsplash_access_key` | Access Key | parameter `unsplash.access_key` | web_unsplash |
| `unsplash_app_id` | Application ID | parameter `unsplash.app_id` | web_unsplash |
| `update_stock_quantities` |  | `company_id.point_of_sale_update_stock_quantities` | pos_stock |
| `use_call_server` | Use Call Server | parameter `mail.use_call_server` | mail |
| `use_custom_sfu_client` | Use Custom SFU Bundle | computed by the screen | mail |
| `use_event_barcode` | Use Event Barcode | parameter `event.use_event_barcode` | event |
| `use_google_maps_static_api` | Google Maps static API | computed by the screen | event |
| `use_google_translate_api` | Use Google Translate API | parameter `mail.use_google_translate_api` | mail |
| `use_invoice_terms` | Default Terms & Conditions | parameter `account.use_invoice_terms` | account |
| `use_kiosk_mode` | Is Kiosk Mode | computed by the screen | point_of_sale |
| `use_root_proxy_user` |  | computed by the screen | l10n_it_edi |
| `use_security_lead` | Security Lead Time for Sales | parameter `sale_stock.use_security_lead` | sale_stock |
| `use_sfu_server` | Use SFU server | parameter `mail.use_sfu_server` | mail |
| `use_tenor_api` | Use Klipy API | parameter `discuss.use_klipy_api` | mail |
| `use_twilio_rtc_servers` | Use Twilio ICE servers | parameter `mail.use_twilio_rtc_servers` | mail |
| `vat_check_vies` | Verify VAT Numbers | `company_id.vat_check_vies` | account |
| `vat_disabled` | Not Subject to VAT | `company_id.vat_disabled` | account |
| `vat_disabled_available` | Not Subject to VAT Available | `company_id.vat_disabled_available` | account |
| `web_app_name` | Web App Name | parameter `web.web_app_name` | web |
| `website_block_third_party_domains` | Block 3rd-party domains | `website_id.block_third_party_domains` | website |
| `website_company_id` | Website Company | `website_id.company_id` | website |
| `website_cookies_bar` |  | `website_id.cookies_bar` | website |
| `website_default_lang_code` | Default language code | `website_id.default_lang_id.code` | website |
| `website_default_lang_id` | Default language | `website_id.default_lang_id` | website |
| `website_domain` | Website Domain | `website_id.domain` | website |
| `website_google_places_api_key` | Website's Google Places API Key | `website_id.google_places_api_key` | website_address_autocomplete |
| `website_homepage_url` |  | `website_id.homepage_url` | website |
| `website_id` | website | computed by the screen | website |
| `website_language_count` | Number of languages | `website_id.language_count` | website |
| `website_logo` |  | `website_id.logo` | website |
| `website_name` | Website Name | `website_id.name` | website |
| `website_show_reference_price` |  | `website_id.show_product_reference_price` | website_sale |
| `website_slide_google_app_key` |  | `website_id.website_slide_google_app_key` | website_slides |
| `website_warehouse_id` |  | `website_id.warehouse_id` | website_sale_stock |
| `withholding_tax_base_account_id` |  | `company_id.withholding_tax_base_account_id` | l10n_account_withholding_tax |
| `work_permit_expiration_notice_period` | Work Permit Expiry Notice Period | `company_id.work_permit_expiration_notice_period` | hr |
