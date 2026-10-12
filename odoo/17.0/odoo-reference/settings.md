# Settings

Each field of `res.config.settings`, and where it keeps its value.

| Field | Label | Kept as | Addon |
|---|---|---|---|
| `account_cash_basis_base_account_id` | Base Tax Received Account | `company_id.account_cash_basis_base_account_id` | account |
| `account_check_printing_date_label` | Print Date Label | `company_id.account_check_printing_date_label` | account_check_printing |
| `account_check_printing_layout` | Check Layout | `company_id.account_check_printing_layout` | account_check_printing |
| `account_check_printing_margin_left` | Check Left Margin | `company_id.account_check_printing_margin_left` | account_check_printing |
| `account_check_printing_margin_right` | Check Right Margin | `company_id.account_check_printing_margin_right` | account_check_printing |
| `account_check_printing_margin_top` | Check Top Margin | `company_id.account_check_printing_margin_top` | account_check_printing |
| `account_check_printing_multi_stub` | Multi-Pages Check Stub | `company_id.account_check_printing_multi_stub` | account_check_printing |
| `account_default_credit_limit` | Default Credit Limit | computed by the screen | account |
| `account_default_pos_receivable_account_id` | Default Account Receivable (PoS) | `company_id.account_default_pos_receivable_account_id` | point_of_sale |
| `account_discount_expense_allocation_id` | Customer Invoices Discounts Account | `company_id.account_discount_expense_allocation_id` | account |
| `account_discount_income_allocation_id` | Vendor Bills Discounts Account | `company_id.account_discount_income_allocation_id` | account |
| `account_fiscal_country_id` | Fiscal Country Code | `company_id.account_fiscal_country_id` | account |
| `account_journal_early_pay_discount_gain_account_id` | Cash Discount Gain | `company_id.account_journal_early_pay_discount_gain_account_id` | account |
| `account_journal_early_pay_discount_loss_account_id` | Cash Discount Loss | `company_id.account_journal_early_pay_discount_loss_account_id` | account |
| `account_journal_payment_credit_account_id` | Outstanding Payments | `company_id.account_journal_payment_credit_account_id` | account |
| `account_journal_payment_debit_account_id` | Outstanding Receipts | `company_id.account_journal_payment_debit_account_id` | account |
| `account_journal_suspense_account_id` | Bank Suspense | `company_id.account_journal_suspense_account_id` | account |
| `account_on_checkout` | Customer Accounts | computed by the screen | website_sale |
| `account_peppol_contact_email` |  | `company_id.account_peppol_contact_email` | account_peppol |
| `account_peppol_eas` |  | `company_id.peppol_eas` | account_peppol |
| `account_peppol_edi_identification` |  | `account_peppol_edi_user.edi_identification` | account_peppol |
| `account_peppol_edi_mode` |  | computed by the screen | account_peppol |
| `account_peppol_edi_user` | EDI user | computed by the screen | account_peppol |
| `account_peppol_endpoint` |  | `company_id.peppol_endpoint` | account_peppol |
| `account_peppol_endpoint_warning` | Warning | computed by the screen | account_peppol |
| `account_peppol_migration_key` |  | `company_id.account_peppol_migration_key` | account_peppol |
| `account_peppol_mode_constraint` |  | computed by the screen | account_peppol |
| `account_peppol_phone_number` |  | `company_id.account_peppol_phone_number` | account_peppol |
| `account_peppol_proxy_state` |  | `company_id.account_peppol_proxy_state` | account_peppol |
| `account_peppol_purchase_journal_id` |  | `company_id.peppol_purchase_journal_id` | account_peppol |
| `account_peppol_verification_code` |  | `account_peppol_edi_user.peppol_verification_code` | account_peppol |
| `account_storno` | Storno accounting | `company_id.account_storno` | account |
| `account_use_credit_limit` | Sales Credit Limit | `company_id.account_use_credit_limit` | account |
| `active_user_count` | Number of Active Users | computed by the screen | base_setup |
| `add_to_cart_action` |  | `website_id.add_to_cart_action` | website_sale |
| `alias_domain_id` |  | `company_id.alias_domain_id` | mail |
| `allow_out_of_stock_order` | Continue selling when out-of-stock | computed by the screen | website_sale_stock |
| `analytic_plan_id` | Analytic Plan | parameter `analytic.analytic_plan_projects` | project |
| `annual_inventory_day` |  | `company_id.annual_inventory_day` | stock |
| `annual_inventory_month` |  | `company_id.annual_inventory_month` | stock |
| `attendance_barcode_source` |  | `company_id.attendance_barcode_source` | hr_attendance |
| `attendance_from_systray` |  | `company_id.attendance_from_systray` | hr_attendance |
| `attendance_kiosk_delay` |  | `company_id.attendance_kiosk_delay` | hr_attendance |
| `attendance_kiosk_mode` |  | `company_id.attendance_kiosk_mode` | hr_attendance |
| `attendance_kiosk_url` |  | `company_id.attendance_kiosk_url` | hr_attendance |
| `attendance_kiosk_use_pin` |  | `company_id.attendance_kiosk_use_pin` | hr_attendance |
| `auth_oauth_google_client_id` | Client ID | computed by the screen | auth_oauth |
| `auth_oauth_google_enabled` | Allow users to sign in with Google | computed by the screen | auth_oauth |
| `auth_signup_reset_password` | Enable password reset from Login page | parameter `auth_signup.reset_password` | auth_signup |
| `auth_signup_template_user_id` | Template user for new users created through signup | parameter `base.template_portal_user_id` | auth_signup |
| `auth_signup_uninvited` | Customer Account | parameter `auth_signup.invitation_scope` | auth_signup |
| `auth_signup_uninvited` |  | computed by the screen | website |
| `auth_totp_enforce` | Enforce two-factor authentication | computed by the screen | auth_totp_mail_enforce |
| `auth_totp_policy` | Two-factor authentication enforcing policy | parameter `auth_totp.policy` | auth_totp_mail_enforce |
| `authorize_capture_method` | Authorize.net: Payment Capture Method | computed by the screen | website_payment_authorize |
| `automatic_invoice` | Automatic Invoice | parameter `sale.automatic_invoice` | sale |
| `available_threshold` | Show Threshold | computed by the screen | website_sale_stock |
| `barcode_nomenclature_id` |  | `company_id.nomenclature_id` | event |
| `barcode_nomenclature_id` |  | `company_id.nomenclature_id` | point_of_sale |
| `cal_client_id` | Client_id | parameter `google_calendar_client_id` | google_calendar |
| `cal_client_secret` | Client_key | parameter `google_calendar_client_secret` | google_calendar |
| `cal_microsoft_client_id` | Microsoft Client_id | parameter `microsoft_calendar_client_id` | microsoft_calendar |
| `cal_microsoft_client_secret` | Microsoft Client_key | parameter `microsoft_calendar_client_secret` | microsoft_calendar |
| `cal_microsoft_sync_paused` | Microsoft Synchronization Paused | parameter `microsoft_calendar_sync_paused` | microsoft_calendar |
| `cal_sync_paused` | Google Synchronization Paused | parameter `google_calendar_sync_paused` | google_calendar |
| `cart_abandoned_delay` | Send After | `website_id.cart_abandoned_delay` | website_sale |
| `cart_recovery_mail_template` | Cart Recovery Email | `website_id.cart_recovery_mail_template_id` | website_sale |
| `cdn_activated` |  | `website_id.cdn_activated` | website |
| `cdn_filters` |  | `website_id.cdn_filters` | website |
| `cdn_url` |  | `website_id.cdn_url` | website |
| `channel_id` | Website Live Channel | `website_id.channel_id` | website_livechat |
| `chart_template` |  | computed by the screen | account |
| `check_account_audit_trail` | Audit Trail | `company_id.check_account_audit_trail` | account_audit_trail |
| `company_count` | Number of Companies | computed by the screen | base_setup |
| `company_country_code` | Company Country Code | `company_id.country_id.code` | base_setup |
| `company_currency_id` | Company Currency | `company_id.currency_id` | purchase |
| `company_expense_allowed_payment_method_line_ids` |  | `company_id.company_expense_allowed_payment_method_line_ids` | hr_expense |
| `company_id` | Company | computed by the screen | base_setup |
| `company_informations` |  | computed by the screen | base_setup |
| `company_lunch_minimum_threshold` | Maximum Allowed Overdraft | `company_id.lunch_minimum_threshold` | lunch |
| `company_lunch_notify_message` | Lunch notification message | `company_id.lunch_notify_message` | lunch |
| `company_name` | Company Name | `company_id.display_name` | base_setup |
| `company_so_template_id` | Default Template | `company_id.sale_order_template_id` | sale_management |
| `contract_expiration_notice_period` | Contract Expiry Notice Period | `company_id.contract_expiration_notice_period` | hr_contract |
| `country_code` |  | `company_id.account_fiscal_country_id.code` | account |
| `crm_auto_assignment_action` | Auto Assignment Action | computed by the screen | crm |
| `crm_auto_assignment_interval_number` | Repeat every | computed by the screen | crm |
| `crm_auto_assignment_interval_type` | Auto Assignment Interval Unit | computed by the screen | crm |
| `crm_auto_assignment_run_datetime` | Auto Assignment Next Execution Date | computed by the screen | crm |
| `crm_use_auto_assignment` | Rule-Based Assignment | parameter `crm.lead.auto.assignment` | crm |
| `currency_exchange_journal_id` | Currency Exchange Journal | `company_id.currency_exchange_journal_id` | account |
| `currency_id` | Currency | `company_id.currency_id` | account |
| `currency_id` |  | `company_id.currency_id` | lunch |
| `days_to_purchase` |  | `company_id.days_to_purchase` | purchase_stock |
| `default_invoice_policy` | Invoicing Policy | computed by the screen | sale |
| `default_picking_policy` |  | computed by the screen | sale_stock |
| `default_purchase_method` | Bill Control | computed by the screen | purchase |
| `delay_alert_contract` | Delay alert contract outdated | parameter `hr_fleet.delay_alert_contract` | fleet |
| `deposit_default_product_id` |  | `company_id.sale_down_payment_product_id` | sale |
| `digest_emails` | Digest Emails | parameter `digest.default_digest_emails` | digest |
| `digest_id` | Digest Email | parameter `digest.default_digest_id` | digest |
| `display_invoice_amount_total_words` | Total amount of invoice in letters | `company_id.display_invoice_amount_total_words` | account |
| `email_primary_color` |  | `company_id.email_primary_color` | mail |
| `email_secondary_color` |  | `company_id.email_secondary_color` | mail |
| `enabled_buy_now_button` | Buy Now | computed by the screen | website_sale |
| `enabled_extra_checkout_step` | Extra Step During Checkout | computed by the screen | website_sale |
| `events_app_name` | Events App Name | `website_id.events_app_name` | website_event_track |
| `expense_currency_exchange_account_id` | Loss Exchange Rate Account | `company_id.expense_currency_exchange_account_id` | account |
| `expense_journal_id` |  | `company_id.expense_journal_id` | hr_expense |
| `expense_product_id` |  | `company_id.expense_product_id` | hr_expense |
| `external_email_server_default` | Use Custom Email Servers | parameter `base_setup.default_external_email_server` | mail |
| `external_report_layout_id` |  | `company_id.external_report_layout_id` | base_setup |
| `fail_counter` | Fail Mail | computed by the screen | mail |
| `favicon` | Favicon | `website_id.favicon` | website |
| `first_provider_label` |  | computed by the screen | website_payment |
| `geoloc_provider_googlemap_key` | Google Map API Key | parameter `base_geolocalize.google_map_api_key` | base_geolocalize |
| `geoloc_provider_id` | API | parameter `base_geolocalize.geo_provider` | base_geolocalize |
| `geoloc_provider_techname` |  | `geoloc_provider_id.tech_name` | base_geolocalize |
| `google_analytics_key` | Google Analytics Key | `website_id.google_analytics_key` | website |
| `google_custom_search_key` | Google Custom Search API Key | parameter `google.custom_search.key` | product_images |
| `google_gmail_client_identifier` | Gmail Client Id | parameter `google_gmail_client_id` | google_gmail |
| `google_gmail_client_secret` | Gmail Client Secret | parameter `google_gmail_client_secret` | google_gmail |
| `google_maps_static_api_key` | Google Maps API key | parameter `google_maps.signed_static_api_key` | event |
| `google_maps_static_api_secret` | Google Maps API secret | parameter `google_maps.signed_static_api_secret` | event |
| `google_places_api_key` | Google Places API Key | `website_id.google_places_api_key` | website_sale_autocomplete |
| `google_pse_id` | The identifier of the Google Programmable Search Engine | parameter `google.pse.id` | product_images |
| `google_search_console` | Google Search Console | `website_id.google_search_console` | website |
| `google_translate_api_key` | Message Translation API Key | parameter `mail.google_translate_api_key` | mail |
| `group_analytic_accounting` | Analytic Accounting | group `analytic.group_analytic_accounting` | analytic |
| `group_applicant_cv_display` |  | group `hr_recruitment.group_applicant_cv_display` | hr_recruitment |
| `group_auto_done_setting` | Lock Confirmed Sales | group `sale.group_auto_done_setting` | sale |
| `group_cash_rounding` | Cash Rounding | group `account.group_cash_rounding` | account |
| `group_delivery_invoice_address` | Shipping Address | group `account.group_delivery_invoice_address` | website_sale |
| `group_discount_per_so_line` | Discounts | group `product.group_discount_per_so_line` | product |
| `group_expiry_date_on_delivery_slip` | Display Expiration Dates on Delivery Slips | group `product_expiry.group_expiry_date_on_delivery_slip` | product_expiry |
| `group_l10n_in_reseller` | Manage Reseller(E-Commerce) | group `l10n_in.group_l10n_in_reseller` | l10n_in |
| `group_lot_on_delivery_slip` | Display Lots & Serial Numbers on Delivery Slips | group `stock.group_lot_on_delivery_slip` | stock |
| `group_lot_on_invoice` | Display Lots & Serial Numbers on Invoices | group `stock_account.group_lot_on_invoice` | stock_account |
| `group_mass_mailing_campaign` | Mailing Campaigns | group `mass_mailing.group_mass_mailing_campaign` | mass_mailing |
| `group_mrp_byproducts` | By-Products | group `mrp.group_mrp_byproducts` | mrp |
| `group_mrp_reception_report` | Allocation Report for Manufacturing Orders | group `mrp.group_mrp_reception_report` | mrp |
| `group_mrp_routings` | MRP Work Orders | group `mrp.group_mrp_routings` | mrp |
| `group_mrp_workorder_dependencies` | Work Order Dependencies | group `mrp.group_mrp_workorder_dependencies` | mrp |
| `group_multi_currency` | Multi-Currencies | group `base.group_multi_currency` | base_setup |
| `group_multi_website` | Multi-website | group `website.group_multi_website` | website |
| `group_product_price_comparison` | Comparison Price | group `website_sale.group_product_price_comparison` | website_sale |
| `group_product_pricelist` | Pricelists | group `product.group_product_pricelist` | product |
| `group_product_pricelist` |  | computed by the screen | website_sale |
| `group_product_variant` | Variants | group `product.group_product_variant` | product |
| `group_proforma_sales` | Pro-Forma Invoice | group `sale.group_proforma_sales` | sale |
| `group_project_milestone` | Milestones | group `project.group_project_milestone` | project |
| `group_project_rating` | Customer Ratings | group `project.group_project_rating` | project |
| `group_project_recurring_tasks` | Recurring Tasks | group `project.group_project_recurring_tasks` | project |
| `group_project_stages` | Project Stages | group `project.group_project_stages` | project |
| `group_project_task_dependencies` | Task Dependencies | group `project.group_project_task_dependencies` | project |
| `group_sale_delivery_address` | Customer Addresses | group `account.group_delivery_invoice_address` | account |
| `group_sale_order_template` | Quotation Templates | group `sale_management.group_sale_order_template` | sale_management |
| `group_sale_pricelist` | Advanced Pricelists | group `product.group_sale_pricelist` | product |
| `group_send_reminder` | Receipt Reminder | group `purchase.group_send_reminder` | purchase |
| `group_show_purchase_receipts` | Purchase Receipt | group `account.group_purchase_receipts` | account |
| `group_show_sale_receipts` | Sale Receipt | group `account.group_sale_receipts` | account |
| `group_show_uom_price` | Base Unit Price | group `website_sale.group_show_uom_price` | website_sale |
| `group_stock_accounting_automatic` | Automatic Stock Accounting | group `stock_account.group_stock_accounting_automatic` | stock_account |
| `group_stock_adv_location` | Multi-Step Routes | group `stock.group_adv_location` | stock |
| `group_stock_lot_print_gs1` | Print GS1 Barcodes for Lots & Serial Numbers | group `stock.group_stock_lot_print_gs1` | stock |
| `group_stock_multi_locations` | Storage Locations | group `stock.group_stock_multi_locations` | stock |
| `group_stock_packaging` | Product Packagings | group `product.group_stock_packaging` | product |
| `group_stock_picking_wave` | Wave Transfers | group `stock.group_stock_picking_wave` | stock |
| `group_stock_production_lot` | Lots & Serial Numbers | group `stock.group_production_lot` | stock |
| `group_stock_reception_report` | Reception Report | group `stock.group_reception_report` | stock |
| `group_stock_sign_delivery` | Signature | group `stock.group_stock_sign_delivery` | stock |
| `group_stock_storage_categories` | Storage Categories | group `stock.group_stock_storage_categories` | stock |
| `group_stock_tracking_lot` | Packages | group `stock.group_tracking_lot` | stock |
| `group_stock_tracking_owner` | Consignment | group `stock.group_tracking_owner` | stock |
| `group_unlocked_by_default` | Unlock Manufacturing Orders | group `mrp.group_unlocked_by_default` | mrp |
| `group_uom` | Units of Measure | group `uom.group_uom` | product |
| `group_use_lead` | Leads | group `crm.group_use_lead` | crm |
| `group_use_recurring_revenues` | Recurring Revenues | group `crm.group_use_recurring_revenues` | crm |
| `group_warning_account` | Warnings in Invoices | group `account.group_warning_account` | account |
| `group_warning_purchase` | Purchase Warnings | group `purchase.group_warning_purchase` | purchase |
| `group_warning_sale` | Sale Order Warnings | group `sale.group_warning_sale` | sale |
| `group_warning_stock` | Warnings for Stock | group `stock.group_warning_stock` | stock |
| `has_accounting_entries` |  | computed by the screen | account |
| `has_chart_of_accounts` | Company has a chart of accounts | computed by the screen | account |
| `has_default_share_image` | Use a image by default for sharing | computed by the screen | website |
| `has_google_analytics` | Google Analytics | computed by the screen | website |
| `has_google_search_console` | Console Google Search | computed by the screen | website |
| `has_plausible_shared_key` | Plausible Analytics | computed by the screen | website |
| `hr_attendance_display_overtime` |  | `company_id.hr_attendance_display_overtime` | hr_attendance |
| `hr_attendance_overtime` | Count Extra Hours | computed by the screen | hr_attendance |
| `hr_employee_self_edit` | Employee Editing | parameter `hr.hr_employee_self_edit` | hr |
| `hr_expense_alias_domain_id` |  | computed by the screen | hr_expense |
| `hr_expense_alias_prefix` | Default Alias Name for Expenses | computed by the screen | hr_expense |
| `hr_expense_use_mailgateway` | Let your employees record expenses by email | parameter `hr_expense.use_mailgateway` | hr_expense |
| `hr_presence_control_email` | Based on number of emails sent | parameter `hr_presence.hr_presence_control_email` | hr |
| `hr_presence_control_email_amount` |  | `company_id.hr_presence_control_email_amount` | hr |
| `hr_presence_control_ip` | Based on IP Address | parameter `hr_presence.hr_presence_control_ip` | hr |
| `hr_presence_control_ip_list` |  | `company_id.hr_presence_control_ip_list` | hr |
| `hr_presence_control_login` | Based on user status in system | parameter `hr.hr_presence_control_login` | hr |
| `income_currency_exchange_account_id` | Gain Exchange Rate Account | `company_id.income_currency_exchange_account_id` | account |
| `incoterm_id` | Default incoterm | `company_id.incoterm_id` | account |
| `internal_project_id` | Internal Project | `company_id.internal_project_id` | project_timesheet_holidays |
| `invoice_is_download` | Download | `company_id.invoice_is_download` | account |
| `invoice_is_email` | Send Email | `company_id.invoice_is_email` | account |
| `invoice_is_snailmail` | Send by Post | `company_id.invoice_is_snailmail` | snailmail_account |
| `invoice_is_ubl_cii` | Peppol format | `company_id.invoice_is_ubl_cii` | account_edi_ubl_cii |
| `invoice_mail_template_id` | Invoice Email Template | parameter `sale.default_invoice_email_template` | sale |
| `invoice_policy` | Invoice Policy | computed by the screen | sale_timesheet |
| `invoice_terms` | Terms & Conditions | `company_id.invoice_terms` | account |
| `invoice_terms_html` | Terms & Conditions as a Web page | `company_id.invoice_terms_html` | account |
| `is_account_peppol_eligible` | PEPPOL eligible | computed by the screen | account |
| `is_account_peppol_participant` | Use PEPPOL | `company_id.is_account_peppol_participant` | account_peppol |
| `is_edi_proxy_active` |  | computed by the screen | l10n_it_edi |
| `is_encode_uom_days` |  | computed by the screen | hr_timesheet |
| `is_installed_sale` | Is the Sale Module Installed | computed by the screen | purchase_stock |
| `is_kiosk_mode` | Is Kiosk Mode | computed by the screen | point_of_sale |
| `is_membership_multi` | Multi Teams | parameter `sales_team.membership_multi` | crm |
| `is_root_company` |  | computed by the screen | base_setup |
| `is_stripe_supported_country` |  | `company_id.country_id.is_stripe_supported_country` | website_payment |
| `jitsi_server_domain` | Jitsi Server Domain | parameter `website_jitsi.jitsi_server_domain` | website_event_jitsi |
| `l10n_ar_tax_base_account_id` | Tax Base Account | `company_id.l10n_ar_tax_base_account_id` | l10n_ar_withholding |
| `l10n_eg_client_identifier` |  | `company_id.l10n_eg_client_identifier` | l10n_eg_edi_eta |
| `l10n_eg_client_secret` |  | `company_id.l10n_eg_client_secret` | l10n_eg_edi_eta |
| `l10n_eg_invoicing_threshold` |  | `company_id.l10n_eg_invoicing_threshold` | l10n_eg_edi_eta |
| `l10n_eg_production_env` |  | `company_id.l10n_eg_production_env` | l10n_eg_edi_eta |
| `l10n_es_edi_certificate_ids` |  | `company_id.l10n_es_edi_certificate_ids` | l10n_es_edi_sii |
| `l10n_es_edi_tax_agency` |  | `company_id.l10n_es_edi_tax_agency` | l10n_es_edi_sii |
| `l10n_es_edi_test_env` |  | `company_id.l10n_es_edi_test_env` | l10n_es_edi_sii |
| `l10n_es_edi_verifactu_certificate_ids` |  | `company_id.l10n_es_edi_verifactu_certificate_ids` | l10n_es_edi_verifactu |
| `l10n_es_edi_verifactu_required` |  | `company_id.l10n_es_edi_verifactu_required` | l10n_es_edi_verifactu |
| `l10n_es_edi_verifactu_special_vat_regime` |  | `company_id.l10n_es_edi_verifactu_special_vat_regime` | l10n_es_edi_verifactu |
| `l10n_es_edi_verifactu_test_environment` |  | `company_id.l10n_es_edi_verifactu_test_environment` | l10n_es_edi_verifactu |
| `l10n_es_tbai_tax_agency` |  | `company_id.l10n_es_tbai_tax_agency` | l10n_es_edi_tbai |
| `l10n_eu_oss_eu_country` | Is European country? | computed by the screen | l10n_eu_oss |
| `l10n_fr_pdp_annuaire_start_date` | Annuaire Start Date | `company_id.l10n_fr_pdp_annuaire_start_date` | l10n_fr_pdp |
| `l10n_fr_pdp_peppol_proxy_display_state` | Approved Platform Status | computed by the screen | l10n_fr_pdp |
| `l10n_fr_pdp_periodicity` | Flow 10 Report Periodicity | `company_id.l10n_fr_pdp_periodicity` | l10n_fr_pdp |
| `l10n_fr_pdp_pilot_phase` | Pilot Phase | computed by the screen | l10n_fr_pdp |
| `l10n_fr_pdp_registered` | Approved Platform Registered | `company_id.l10n_fr_pdp_registered` | l10n_fr_pdp |
| `l10n_fr_pdp_send_to_ppf` | Send to PPF | `company_id.l10n_fr_pdp_send_to_ppf` | l10n_fr_pdp |
| `l10n_fr_reference_leave_type` |  | `company_id.l10n_fr_reference_leave_type` | l10n_fr_hr_holidays |
| `l10n_hu_edi_is_active` |  | computed by the screen | l10n_hu_edi |
| `l10n_hu_edi_password` |  | `company_id.l10n_hu_edi_password` | l10n_hu_edi |
| `l10n_hu_edi_replacement_key` |  | `company_id.l10n_hu_edi_replacement_key` | l10n_hu_edi |
| `l10n_hu_edi_server_mode` |  | `company_id.l10n_hu_edi_server_mode` | l10n_hu_edi |
| `l10n_hu_edi_signature_key` |  | `company_id.l10n_hu_edi_signature_key` | l10n_hu_edi |
| `l10n_hu_edi_username` |  | `company_id.l10n_hu_edi_username` | l10n_hu_edi |
| `l10n_hu_tax_regime` |  | `company_id.l10n_hu_tax_regime` | l10n_hu_edi |
| `l10n_id_tax_address` | Tax Address | `company_id.partner_id.l10n_id_tax_address` | l10n_id_efaktur |
| `l10n_id_tax_name` | Tax Name | `company_id.partner_id.l10n_id_tax_address` | l10n_id_efaktur |
| `l10n_in_edi_ewaybill_password` | Indian EDI Stock password | `company_id.l10n_in_edi_ewaybill_password` | l10n_in_edi_ewaybill |
| `l10n_in_edi_ewaybill_username` | Indian EDI Stock username | `company_id.l10n_in_edi_ewaybill_username` | l10n_in_edi_ewaybill |
| `l10n_in_edi_password` | Indian EDI password | `company_id.l10n_in_edi_password` | l10n_in_edi |
| `l10n_in_edi_production_env` | Indian EDI Testing Environment | `company_id.l10n_in_edi_production_env` | l10n_in_edi |
| `l10n_in_edi_username` | Indian EDI username | `company_id.l10n_in_edi_username` | l10n_in_edi |
| `l10n_in_gsp` | GSP | computed by the screen | l10n_in |
| `l10n_in_withholding_account_id` |  | `company_id.l10n_in_withholding_account_id` | l10n_in_withholding |
| `l10n_in_withholding_journal_id` |  | `company_id.l10n_in_withholding_journal_id` | l10n_in_withholding |
| `l10n_it_edi_demo_mode` |  | computed by the screen | l10n_it_edi |
| `l10n_it_edi_proxy_current_state` |  | computed by the screen | l10n_it_edi |
| `l10n_it_edi_register` |  | computed by the screen | l10n_it_edi |
| `l10n_jo_edi_client_identifier` | JoFotara Client ID | `company_id.l10n_jo_edi_client_identifier` | l10n_jo_edi |
| `l10n_jo_edi_demo_mode` | JoFotara Demo Mode | `company_id.l10n_jo_edi_demo_mode` | l10n_jo_edi_extended |
| `l10n_jo_edi_secret_key` | JoFotara Secret Key | `company_id.l10n_jo_edi_secret_key` | l10n_jo_edi |
| `l10n_jo_edi_sequence_income_source` | JoFotara Sequence of Income Source | `company_id.l10n_jo_edi_sequence_income_source` | l10n_jo_edi |
| `l10n_jo_edi_taxpayer_type` | JoFotara Taxpayer Type | `company_id.l10n_jo_edi_taxpayer_type` | l10n_jo_edi |
| `l10n_ke_cu_proxy_address` |  | `company_id.l10n_ke_cu_proxy_address` | l10n_ke_edi_tremol |
| `l10n_my_accept_processing` |  | computed by the screen | l10n_my_edi |
| `l10n_my_edi_company_vat` |  | `company_id.vat` | l10n_my_edi |
| `l10n_my_edi_default_import_journal_id` |  | `company_id.l10n_my_edi_default_import_journal_id` | l10n_my_edi |
| `l10n_my_edi_mode` |  | `company_id.l10n_my_edi_mode` | l10n_my_edi |
| `l10n_my_edi_proxy_user_id` |  | `company_id.l10n_my_edi_proxy_user_id` | l10n_my_edi |
| `l10n_pl_reports_tax_office_id` |  | `company_id.l10n_pl_reports_tax_office_id` | l10n_pl |
| `l10n_ro_edi_access_expiry_date` |  | `company_id.l10n_ro_edi_access_expiry_date` | l10n_ro_efactura |
| `l10n_ro_edi_access_token` |  | `company_id.l10n_ro_edi_access_token` | l10n_ro_efactura |
| `l10n_ro_edi_anaf_imported_inv_journal_id` |  | `company_id.l10n_ro_edi_anaf_imported_inv_journal_id` | l10n_ro_efactura_synchronize |
| `l10n_ro_edi_callback_url` |  | `company_id.l10n_ro_edi_callback_url` | l10n_ro_efactura |
| `l10n_ro_edi_client_id` |  | `company_id.l10n_ro_edi_client_id` | l10n_ro_efactura |
| `l10n_ro_edi_client_secret` |  | `company_id.l10n_ro_edi_client_secret` | l10n_ro_efactura |
| `l10n_ro_edi_oauth_error` |  | `company_id.l10n_ro_edi_oauth_error` | l10n_ro_efactura |
| `l10n_ro_edi_refresh_expiry_date` |  | `company_id.l10n_ro_edi_refresh_expiry_date` | l10n_ro_efactura |
| `l10n_ro_edi_refresh_token` |  | `company_id.l10n_ro_edi_refresh_token` | l10n_ro_efactura |
| `l10n_ro_edi_test_env` |  | `company_id.l10n_ro_edi_test_env` | l10n_ro_efactura |
| `l10n_rs_edi_api_key` |  | `company_id.l10n_rs_edi_api_key` | l10n_rs_edi |
| `l10n_rs_edi_demo_env` |  | `company_id.l10n_rs_edi_demo_env` | l10n_rs_edi |
| `l10n_sa_api_mode` |  | `company_id.l10n_sa_api_mode` | l10n_sa_edi |
| `l10n_tr_nilvera_api_key` | Nilvera API key | `company_id.l10n_tr_nilvera_api_key` | l10n_tr_nilvera |
| `l10n_tr_nilvera_environment` | Nilvera Environment | `company_id.l10n_tr_nilvera_environment` | l10n_tr_nilvera |
| `l10n_tr_nilvera_purchase_journal_id` |  | `company_id.l10n_tr_nilvera_purchase_journal_id` | l10n_tr_nilvera |
| `l10n_vn_edi_default_symbol` | Default Symbol | computed by the screen | l10n_vn_edi_viettel |
| `l10n_vn_edi_password` |  | `company_id.l10n_vn_edi_password` | l10n_vn_edi_viettel |
| `l10n_vn_edi_username` |  | `company_id.l10n_vn_edi_username` | l10n_vn_edi_viettel |
| `language_count` | Number of Languages | computed by the screen | base_setup |
| `language_ids` |  | `website_id.language_ids` | website |
| `lc_journal_id` | Default Journal | `company_id.lc_journal_id` | stock_landed_costs |
| `ldaps` | LDAP Parameters | `company_id.ldaps` | auth_ldap |
| `lead_enrich_auto` | Enrich lead automatically | parameter `crm.iap.lead.enrich.setting` | crm |
| `lead_mining_in_pipeline` | Create a lead mining request directly from the opportunity pipeline. | parameter `crm.lead_mining_in_pipeline` | crm |
| `leave_timesheet_task_id` | Time Off Task | `company_id.leave_timesheet_task_id` | project_timesheet_holidays |
| `lock_confirmed_po` | Lock Confirmed Orders | computed by the screen | purchase |
| `manufacturing_lead` | Manufacturing Lead Time | `company_id.manufacturing_lead` | mrp |
| `mass_mailing_mail_server_id` | Mail Server | parameter `mass_mailing.mail_server_id` | mass_mailing |
| `mass_mailing_outgoing_mail_server` | Dedicated Server | parameter `mass_mailing.outgoing_mail_server` | mass_mailing |
| `mass_mailing_reports` | 24H Stat Mailing Reports | parameter `mass_mailing.mass_mailing_reports` | mass_mailing |
| `microsoft_outlook_client_identifier` | Outlook Client Id | parameter `microsoft_outlook_client_id` | microsoft_outlook |
| `microsoft_outlook_client_secret` | Outlook Client Secret | parameter `microsoft_outlook_client_secret` | microsoft_outlook |
| `minlength` | Minimum Password Length | parameter `auth_password_policy.minlength` | auth_password_policy |
| `module_account` | Invoicing | installs `account` | website_sale |
| `module_account_3way_match` | 3-way matching: purchases, receptions and bills | installs `account_3way_match` | purchase |
| `module_account_accountant` | Accounting | installs `account_accountant` | account |
| `module_account_avatax` | Account Avatax | installs `account_avatax` | account |
| `module_account_bank_statement_import_camt` | Import in CAMT.053 format | installs `account_bank_statement_import_camt` | account |
| `module_account_bank_statement_import_csv` | Import in .csv, .xls, and .xlsx format | installs `account_bank_statement_import_csv` | account |
| `module_account_bank_statement_import_ofx` | Import in .ofx format | installs `account_bank_statement_import_ofx` | account |
| `module_account_bank_statement_import_qif` | Import .qif files | installs `account_bank_statement_import_qif` | account |
| `module_account_batch_payment` | Use batch payments | installs `account_batch_payment` | account |
| `module_account_budget` | Budget Management | installs `account_budget` | account |
| `module_account_check_printing` | Allow check printing and deposits | installs `account_check_printing` | account |
| `module_account_inter_company_rules` | Manage Inter Company | installs `account_inter_company_rules` | base_setup |
| `module_account_intrastat` | Intrastat | installs `account_intrastat` | account |
| `module_account_invoice_extract` | Document Digitization | installs `account_invoice_extract` | account |
| `module_account_payment` | Invoice Online Payment | installs `account_payment` | account |
| `module_account_peppol` | PEPPOL Invoicing | installs `account_peppol` | account |
| `module_account_reports` | Dynamic Reports | installs `account_reports` | account |
| `module_account_sepa` | SEPA Credit Transfer (SCT) | installs `account_sepa` | account |
| `module_account_sepa_direct_debit` | Use SEPA Direct Debit | installs `account_sepa_direct_debit` | account |
| `module_account_taxcloud` | Account TaxCloud | installs `account_taxcloud` | account |
| `module_auth_ldap` | LDAP Authentication | installs `auth_ldap` | base_setup |
| `module_auth_oauth` | Use external authentication providers (OAuth) | installs `auth_oauth` | base_setup |
| `module_base_geolocalize` | GeoLocalize | installs `base_geolocalize` | base_setup |
| `module_base_import` | Allow users to import data from CSV/XLS/XLSX/ODS files | installs `base_import` | base_setup |
| `module_crm_iap_enrich` | Enrich your leads automatically with company data based on their email address. | installs `crm_iap_enrich` | crm |
| `module_crm_iap_mine` | Generate new leads based on their country, industries, size, etc. | installs `crm_iap_mine` | crm |
| `module_currency_rate_live` | Automatic Currency Rates | installs `currency_rate_live` | account |
| `module_delivery` | Delivery Methods | installs `delivery` | sale |
| `module_delivery` | Delivery Methods | installs `delivery` | stock |
| `module_delivery_bpost` | bpost Connector | installs `delivery_bpost` | sale |
| `module_delivery_bpost` | bpost Connector | installs `delivery_bpost` | stock |
| `module_delivery_dhl` | DHL Express Connector | installs `delivery_dhl` | sale |
| `module_delivery_dhl` | DHL Express Connector | installs `delivery_dhl` | stock |
| `module_delivery_easypost` | Easypost Connector | installs `delivery_easypost` | sale |
| `module_delivery_easypost` | Easypost Connector | installs `delivery_easypost` | stock |
| `module_delivery_fedex` | FedEx Connector | installs `delivery_fedex` | sale |
| `module_delivery_fedex` | FedEx Connector | installs `delivery_fedex` | stock |
| `module_delivery_mondialrelay` | Mondial Relay Connector | installs `delivery_mondialrelay` | website_sale |
| `module_delivery_sendcloud` | Sendcloud Connector | installs `delivery_sendcloud` | sale |
| `module_delivery_sendcloud` | Sendcloud Connector | installs `delivery_sendcloud` | stock |
| `module_delivery_shiprocket` | Shiprocket Connector | installs `delivery_shiprocket` | sale |
| `module_delivery_shiprocket` | Shiprocket Connector | installs `delivery_shiprocket` | stock |
| `module_delivery_ups` | UPS Connector | installs `delivery_ups` | sale |
| `module_delivery_ups` | UPS Connector | installs `delivery_ups` | stock |
| `module_delivery_usps` | USPS Connector | installs `delivery_usps` | sale |
| `module_delivery_usps` | USPS Connector | installs `delivery_usps` | stock |
| `module_event_booth` | Booth Management | installs `event_booth` | event |
| `module_event_sale` | Tickets | installs `event_sale` | event |
| `module_google_calendar` | Allow the users to synchronize their calendar  with Google Calendar | installs `google_calendar` | base_setup |
| `module_google_gmail` | Support Gmail Authentication | installs `google_gmail` | mail |
| `module_google_recaptcha` | reCAPTCHA | installs `google_recaptcha` | base_setup |
| `module_hr_attendance` | Based on attendances | installs `hr_attendance` | hr |
| `module_hr_expense_extract` | Send bills to OCR to generate expenses | installs `hr_expense_extract` | hr_expense |
| `module_hr_homeworking` | Remote Work | installs `hr_homeworking` | hr |
| `module_hr_payroll_expense` | Reimburse Expenses in Payslip | installs `hr_payroll_expense` | hr_expense |
| `module_hr_presence` | Advanced Presence Control | installs `hr_presence` | hr |
| `module_hr_recruitment_extract` | Send CV to OCR to fill applications | installs `hr_recruitment_extract` | hr_recruitment |
| `module_hr_recruitment_survey` | Interview Forms | installs `hr_recruitment_survey` | hr_recruitment |
| `module_hr_skills` | Skills Management | installs `hr_skills` | hr |
| `module_hr_timesheet` | Task Logs | installs `hr_timesheet` | project |
| `module_l10n_eu_oss` | EU Intra-community Distance Selling | installs `l10n_eu_oss` | account |
| `module_l10n_in_edi` | Indian Electronic Invoicing | installs `l10n_in_edi` | l10n_in |
| `module_l10n_in_edi_ewaybill` | Indian Electronic Waybill | installs `l10n_in_edi_ewaybill` | l10n_in |
| `module_l10n_mx_edi` | Mexican Electronic Invoicing | installs `l10n_mx_edi` | l10n_mx |
| `module_loyalty` | Promotions, Coupons, Gift Card & Loyalty Program | installs `loyalty` | product |
| `module_mail_plugin` | Allow integration with the mail plugins | installs `mail_plugin` | base_setup |
| `module_maintenance_worksheet` | Custom Maintenance Worksheets | installs `maintenance_worksheet` | maintenance |
| `module_marketing_automation` |  | installs `marketing_automation` | website |
| `module_mass_mailing_slides` | Mailing | installs `mass_mailing_slides` | website_slides |
| `module_microsoft_calendar` | Allow the users to synchronize their calendar with Outlook Calendar | installs `microsoft_calendar` | base_setup |
| `module_microsoft_outlook` | Support Outlook Authentication | installs `microsoft_outlook` | mail |
| `module_mrp_mps` | Master Production Schedule | installs `mrp_mps` | mrp |
| `module_mrp_plm` | Product Lifecycle Management (PLM) | installs `mrp_plm` | mrp |
| `module_mrp_subcontracting` | Subcontracting | installs `mrp_subcontracting` | mrp |
| `module_partner_autocomplete` | Partner Autocomplete | installs `partner_autocomplete` | base_setup |
| `module_pos_adyen` | Adyen Payment Terminal | installs `pos_adyen` | point_of_sale |
| `module_pos_mercury` | Vantiv Payment Terminal | installs `pos_mercury` | point_of_sale |
| `module_pos_paytm` | PayTM Payment Terminal | installs `pos_paytm` | point_of_sale |
| `module_pos_preparation_display` | Preparation Display | installs `pos_preparation_display` | point_of_sale |
| `module_pos_six` | Six Payment Terminal | installs `pos_six` | point_of_sale |
| `module_pos_stripe` | Stripe Payment Terminal | installs `pos_stripe` | point_of_sale |
| `module_product_email_template` | Specific Email | installs `product_email_template` | sale |
| `module_product_expiry` | Expiration Dates | installs `product_expiry` | stock |
| `module_product_images` | Get product pictures using barcode | installs `product_images` | base_setup |
| `module_product_margin` | Allow Product Margin | installs `product_margin` | account |
| `module_project_timesheet_holidays` | Time Off | installs `project_timesheet_holidays` | hr_timesheet |
| `module_purchase_product_matrix` | Purchase Grid Entry | installs `purchase_product_matrix` | purchase |
| `module_purchase_requisition` | Purchase Agreements | installs `purchase_requisition` | purchase |
| `module_quality_control` | Quality | installs `quality_control` | mrp |
| `module_quality_control` | Quality | installs `quality_control` | stock |
| `module_quality_control_worksheet` | Quality Worksheet | installs `quality_control_worksheet` | mrp |
| `module_quality_control_worksheet` | Quality Worksheet | installs `quality_control_worksheet` | stock |
| `module_sale_amazon` | Amazon Sync | installs `sale_amazon` | sale |
| `module_sale_loyalty` | Coupons & Loyalty | installs `sale_loyalty` | sale |
| `module_sale_margin` | Margins | installs `sale_margin` | sale |
| `module_sale_pdf_quote_builder` | PDF Quote builder | installs `sale_pdf_quote_builder` | sale |
| `module_sale_product_matrix` | Sales Grid Entry | installs `sale_product_matrix` | product |
| `module_snailmail_account` | Snailmail | installs `snailmail_account` | account |
| `module_stock_barcode` | Barcode Scanner | installs `stock_barcode` | stock |
| `module_stock_dropshipping` | Dropshipping | installs `stock_dropshipping` | purchase_stock |
| `module_stock_dropshipping` | Dropshipping | installs `stock_dropshipping` | stock |
| `module_stock_landed_costs` | Landed Costs | installs `stock_landed_costs` | stock_account |
| `module_stock_picking_batch` | Batch Transfers | installs `stock_picking_batch` | stock |
| `module_stock_sms` | SMS Confirmation | installs `stock_sms` | stock |
| `module_voip` | Asterisk (VoIP) | installs `voip` | base_setup |
| `module_web_unsplash` | Unsplash Image Library | installs `web_unsplash` | base_setup |
| `module_website_cf_turnstile` | Cloudflare Turnstile | installs `website_cf_turnstile` | base_setup |
| `module_website_crm_iap_reveal` | Create Leads/Opportunities from your website's traffic | installs `website_crm_iap_reveal` | crm |
| `module_website_event_exhibitor` | Advanced Sponsors | installs `website_event_exhibitor` | event |
| `module_website_event_meet` | Discussion Rooms | installs `website_event_meet` | event |
| `module_website_event_sale` | Online Ticketing | installs `website_event_sale` | event |
| `module_website_event_track` | Tracks and Agenda | installs `website_event_track` | event |
| `module_website_event_track_live` | Live Mode | installs `website_event_track_live` | event |
| `module_website_event_track_quiz` | Quiz on Tracks | installs `website_event_track_quiz` | event |
| `module_website_hr_recruitment` | Online Posting | installs `website_hr_recruitment` | hr_recruitment |
| `module_website_livechat` |  | installs `website_livechat` | website |
| `module_website_sale_autocomplete` | Address Autocomplete | installs `website_sale_autocomplete` | website_sale |
| `module_website_sale_comparison` | Product Comparison Tool | installs `website_sale_comparison` | website_sale |
| `module_website_sale_picking` | On Site Payments & Picking | installs `website_sale_picking` | website_sale |
| `module_website_sale_slides` | Sell on eCommerce | installs `website_sale_slides` | website_slides |
| `module_website_sale_wishlist` | Wishlists | installs `website_sale_wishlist` | website_sale |
| `module_website_slides_forum` | Forum | installs `website_slides_forum` | website_slides |
| `module_website_slides_survey` | Certifications | installs `website_slides_survey` | website_slides |
| `overtime_company_threshold` | Tolerance Time In Favor Of Company | computed by the screen | hr_attendance |
| `overtime_employee_threshold` | Tolerance Time In Favor Of Employee | computed by the screen | hr_attendance |
| `overtime_start_date` | Extra Hours Starting Date | computed by the screen | hr_attendance |
| `partner_autocomplete_insufficient_credit` | Insufficient credit | computed by the screen | partner_autocomplete |
| `pay_invoices_online` |  | parameter `account_payment.enable_portal_payment` | account_payment |
| `peppol_use_parent_company` |  | computed by the screen | account_peppol |
| `picking_site_ids` |  | `website_id.picking_site_ids` | website_sale_picking |
| `plausible_shared_key` | Plausible auth Key | `website_id.plausible_shared_key` | website |
| `plausible_site` | Plausible Site (e.g. domain.com) | `website_id.plausible_site` | website |
| `po_double_validation` | Levels of Approvals * | `company_id.po_double_validation` | purchase |
| `po_double_validation_amount` | Minimum Amount | `company_id.po_double_validation_amount` | purchase |
| `po_lead` |  | `company_id.po_lead` | purchase |
| `po_lock` | Purchase Order Modification * | `company_id.po_lock` | purchase |
| `po_order_approval` | Purchase Order Approval | computed by the screen | purchase |
| `point_of_sale_ticket_unique_code` |  | `company_id.point_of_sale_ticket_unique_code` | point_of_sale |
| `point_of_sale_use_ticket_qr_code` |  | `company_id.point_of_sale_use_ticket_qr_code` | point_of_sale |
| `portal_allow_api_keys` | Customer API Keys | computed by the screen | portal |
| `portal_confirmation_pay` |  | `company_id.portal_confirmation_pay` | sale |
| `portal_confirmation_sign` |  | `company_id.portal_confirmation_sign` | sale |
| `pos_advanced_employee_ids` |  | `pos_config_id.advanced_employee_ids` | pos_hr |
| `pos_adyen_ask_customer_for_tip` |  | computed by the screen | pos_adyen |
| `pos_allowed_pricelist_ids` |  | computed by the screen | point_of_sale |
| `pos_amount_authorized_diff` |  | `pos_config_id.amount_authorized_diff` | point_of_sale |
| `pos_auto_validate_terminal_payment` | Automatically validates orders paid with a payment terminal. | `pos_config_id.auto_validate_terminal_payment` | point_of_sale |
| `pos_available_pricelist_ids` | Available Pricelists | computed by the screen | point_of_sale |
| `pos_basic_employee_ids` |  | `pos_config_id.basic_employee_ids` | pos_hr |
| `pos_cash_control` |  | `pos_config_id.cash_control` | point_of_sale |
| `pos_cash_rounding` | Cash Rounding (PoS) | `pos_config_id.cash_rounding` | point_of_sale |
| `pos_company_has_template` |  | `pos_config_id.company_has_template` | point_of_sale |
| `pos_config_id` | Point of Sale | computed by the screen | point_of_sale |
| `pos_crm_team_id` | Sales Team (PoS) | `pos_config_id.crm_team_id` | pos_sale |
| `pos_default_bill_ids` |  | `pos_config_id.default_bill_ids` | point_of_sale |
| `pos_default_fiscal_position_id` | Default Fiscal Position | computed by the screen | point_of_sale |
| `pos_discount_pc` |  | `pos_config_id.discount_pc` | pos_discount |
| `pos_discount_product_id` |  | computed by the screen | pos_discount |
| `pos_down_payment_product_id` |  | `pos_config_id.down_payment_product_id` | pos_sale |
| `pos_epson_printer_ip` |  | computed by the screen | pos_epson_printer |
| `pos_fiscal_position_ids` | Fiscal Positions | computed by the screen | point_of_sale |
| `pos_floor_ids` |  | `pos_config_id.floor_ids` | pos_restaurant |
| `pos_gift_card_settings` |  | `pos_config_id.gift_card_settings` | pos_loyalty |
| `pos_has_active_session` |  | `pos_config_id.has_active_session` | point_of_sale |
| `pos_iface_available_categ_ids` | Available PoS Product Categories | computed by the screen | point_of_sale |
| `pos_iface_big_scrollbars` |  | `pos_config_id.iface_big_scrollbars` | point_of_sale |
| `pos_iface_cashdrawer` | Cashdrawer | computed by the screen | point_of_sale |
| `pos_iface_customer_facing_display_background_image_1920` |  | `pos_config_id.iface_customer_facing_display_background_image_1920` | point_of_sale |
| `pos_iface_customer_facing_display_local` |  | `pos_config_id.iface_customer_facing_display_local` | point_of_sale |
| `pos_iface_customer_facing_display_via_proxy` | Customer Facing Display | computed by the screen | point_of_sale |
| `pos_iface_electronic_scale` | Electronic Scale | computed by the screen | point_of_sale |
| `pos_iface_orderline_notes` |  | `pos_config_id.iface_orderline_notes` | pos_restaurant |
| `pos_iface_print_auto` |  | `pos_config_id.iface_print_auto` | point_of_sale |
| `pos_iface_print_skip_screen` |  | `pos_config_id.iface_print_skip_screen` | point_of_sale |
| `pos_iface_print_via_proxy` | Print via Proxy | computed by the screen | point_of_sale |
| `pos_iface_printbill` |  | computed by the screen | pos_restaurant |
| `pos_iface_scan_via_proxy` | Scan via Proxy | computed by the screen | point_of_sale |
| `pos_iface_splitbill` |  | computed by the screen | pos_restaurant |
| `pos_iface_start_categ_id` | Initial Category | computed by the screen | point_of_sale |
| `pos_iface_tax_included` |  | `pos_config_id.iface_tax_included` | point_of_sale |
| `pos_iface_tipproduct` |  | `pos_config_id.iface_tipproduct` | point_of_sale |
| `pos_invoice_journal_id` |  | `pos_config_id.invoice_journal_id` | point_of_sale |
| `pos_is_header_or_footer` |  | `pos_config_id.is_header_or_footer` | point_of_sale |
| `pos_is_margins_costs_accessible_to_every_user` |  | `pos_config_id.is_margins_costs_accessible_to_every_user` | point_of_sale |
| `pos_is_order_printer` |  | computed by the screen | point_of_sale |
| `pos_is_posbox` |  | `pos_config_id.is_posbox` | point_of_sale |
| `pos_is_spanish` | Consider the specific spanish legislation, such as the use of simplified invoices | `pos_config_id.is_spanish` | l10n_es_pos |
| `pos_journal_id` |  | `pos_config_id.journal_id` | point_of_sale |
| `pos_l10n_es_simplified_invoice_journal_id` |  | `pos_config_id.l10n_es_simplified_invoice_journal_id` | l10n_es_pos |
| `pos_l10n_es_simplified_invoice_limit` |  | `pos_config_id.l10n_es_simplified_invoice_limit` | l10n_es_pos |
| `pos_limit_categories` |  | `pos_config_id.limit_categories` | point_of_sale |
| `pos_manual_discount` |  | `pos_config_id.manual_discount` | point_of_sale |
| `pos_module_pos_discount` |  | `pos_config_id.module_pos_discount` | point_of_sale |
| `pos_module_pos_hr` |  | `pos_config_id.module_pos_hr` | point_of_sale |
| `pos_module_pos_restaurant` |  | `pos_config_id.module_pos_restaurant` | point_of_sale |
| `pos_module_pos_restaurant_appointment` |  | `pos_config_id.module_pos_restaurant_appointment` | pos_restaurant |
| `pos_only_round_cash_method` |  | `pos_config_id.only_round_cash_method` | point_of_sale |
| `pos_other_devices` |  | `pos_config_id.other_devices` | point_of_sale |
| `pos_payment_method_ids` |  | `pos_config_id.payment_method_ids` | point_of_sale |
| `pos_picking_policy` |  | `pos_config_id.picking_policy` | point_of_sale |
| `pos_picking_type_id` |  | `pos_config_id.picking_type_id` | point_of_sale |
| `pos_pricelist_id` | Default Pricelist | computed by the screen | point_of_sale |
| `pos_printer_ids` |  | `pos_config_id.printer_ids` | point_of_sale |
| `pos_proxy_ip` | IP Address | computed by the screen | point_of_sale |
| `pos_receipt_footer` | Receipt Footer | computed by the screen | point_of_sale |
| `pos_receipt_header` | Receipt Header | computed by the screen | point_of_sale |
| `pos_restrict_price_control` |  | `pos_config_id.restrict_price_control` | point_of_sale |
| `pos_rounding_method` |  | `pos_config_id.rounding_method` | point_of_sale |
| `pos_route_id` |  | `pos_config_id.route_id` | point_of_sale |
| `pos_selectable_categ_ids` |  | computed by the screen | point_of_sale |
| `pos_self_order_online_payment_method_id` |  | `pos_config_id.self_order_online_payment_method_id` | pos_online_payment_self_order |
| `pos_self_ordering_alternative_fp_id` |  | `pos_config_id.self_ordering_alternative_fp_id` | pos_self_order |
| `pos_self_ordering_available_language_ids` |  | `pos_config_id.self_ordering_available_language_ids` | pos_self_order |
| `pos_self_ordering_default_language_id` |  | `pos_config_id.self_ordering_default_language_id` | pos_self_order |
| `pos_self_ordering_default_user_id` |  | `pos_config_id.self_ordering_default_user_id` | pos_self_order |
| `pos_self_ordering_image_brand` |  | `pos_config_id.self_ordering_image_brand` | pos_self_order |
| `pos_self_ordering_image_brand_name` |  | `pos_config_id.self_ordering_image_brand_name` | pos_self_order |
| `pos_self_ordering_image_home_ids` |  | `pos_config_id.self_ordering_image_home_ids` | pos_self_order |
| `pos_self_ordering_mode` |  | `pos_config_id.self_ordering_mode` | pos_self_order |
| `pos_self_ordering_pay_after` |  | `pos_config_id.self_ordering_pay_after` | pos_self_order |
| `pos_self_ordering_service_mode` |  | `pos_config_id.self_ordering_service_mode` | pos_self_order |
| `pos_self_ordering_takeaway` |  | `pos_config_id.self_ordering_takeaway` | pos_self_order |
| `pos_sequence_id` |  | `pos_config_id.sequence_id` | point_of_sale |
| `pos_set_maximum_difference` |  | `pos_config_id.set_maximum_difference` | point_of_sale |
| `pos_set_tip_after_payment` |  | computed by the screen | pos_restaurant |
| `pos_ship_later` |  | `pos_config_id.ship_later` | point_of_sale |
| `pos_start_category` |  | `pos_config_id.start_category` | point_of_sale |
| `pos_tax_regime_selection` |  | `pos_config_id.tax_regime_selection` | point_of_sale |
| `pos_tip_product_id` | Tip Product | computed by the screen | point_of_sale |
| `pos_trusted_config_ids` |  | `pos_config_id.trusted_config_ids` | point_of_sale |
| `pos_use_pricelist` |  | `pos_config_id.use_pricelist` | point_of_sale |
| `pos_warehouse_id` | Warehouse (PoS) | `pos_config_id.warehouse_id` | point_of_sale |
| `predictive_lead_scoring_field_labels` |  | computed by the screen | crm |
| `predictive_lead_scoring_fields` | Lead Scoring Frequency Fields | computed by the screen | crm |
| `predictive_lead_scoring_fields_str` | Lead Scoring Frequency Fields in String | parameter `crm.pls_fields` | crm |
| `predictive_lead_scoring_start_date` | Lead Scoring Starting Date | computed by the screen | crm |
| `predictive_lead_scoring_start_date_str` | Lead Scoring Starting Date in String | parameter `crm.pls_start_date` | crm |
| `prepayment_percent` |  | `company_id.prepayment_percent` | sale |
| `preview_ready` | Display preview button | computed by the screen | account |
| `product_pricelist_setting` | Pricelists Method | parameter `product.product_pricelist_setting` | product |
| `product_volume_volume_in_cubic_feet` |  | parameter `product.volume_in_cubic_feet` | product |
| `product_weight_in_lbs` |  | parameter `product.weight_in_lbs` | product |
| `profiling_enabled_until` | Profiling enabled until | parameter `base.profiling_enabled_until` | base_setup |
| `project_time_mode_id` | Project Time Unit | `company_id.project_time_mode_id` | hr_timesheet |
| `providers_state` |  | computed by the screen | website_payment |
| `purchase_tax_id` | Default Purchase Tax | `company_id.account_purchase_tax_id` | account |
| `qr_code` | Display SEPA QR-code | `company_id.qr_code` | account |
| `quick_edit_mode` | Quick encoding | `company_id.quick_edit_mode` | account |
| `quotation_validity_days` |  | `company_id.quotation_validity_days` | sale |
| `recaptcha_min_score` | Minimum score | parameter `recaptcha_min_score` | google_recaptcha |
| `recaptcha_private_key` | Secret Key | parameter `recaptcha_private_key` | google_recaptcha |
| `recaptcha_public_key` | Site Key | parameter `recaptcha_public_key` | google_recaptcha |
| `reminder_allow` | Approver Reminder | computed by the screen | hr_timesheet |
| `reminder_user_allow` | Employee Reminder | computed by the screen | hr_timesheet |
| `report_footer` | Custom Report Footer | `company_id.report_footer` | base_setup |
| `resource_calendar_id` |  | `company_id.resource_calendar_id` | hr |
| `restrict_template_rendering` | Restrict Template Rendering | parameter `mail.restrict.template.rendering` | mail |
| `sale_footer` |  | `company_id.sale_footer` | sale_pdf_quote_builder |
| `sale_footer_name` |  | `company_id.sale_footer_name` | sale_pdf_quote_builder |
| `sale_header` |  | `company_id.sale_header` | sale_pdf_quote_builder |
| `sale_header_name` |  | `company_id.sale_header_name` | sale_pdf_quote_builder |
| `sale_tax_id` | Default Sale Tax | `company_id.account_sale_tax_id` | account |
| `sale_tax_id` | Default Sale Tax | `company_id.account_sale_tax_id` | point_of_sale |
| `salesperson_id` | Salesperson | `website_id.salesperson_id` | website_sale |
| `salesteam_id` | Sales Team | `website_id.salesteam_id` | website_sale |
| `security_lead` | Security Lead Time | `company_id.security_lead` | sale_stock |
| `send_abandoned_cart_email` | Abandoned Email | `website_id.send_abandoned_cart_email` | website_sale |
| `server_uri_google` | Server uri | computed by the screen | auth_oauth |
| `sfu_server_key` | SFU Server key | parameter `mail.sfu_server_key` | mail |
| `sfu_server_url` | SFU Server URL | parameter `mail.sfu_server_url` | mail |
| `shared_user_account` | Shared Customer Accounts | computed by the screen | website |
| `show_availability` | Show availability Qty | computed by the screen | website_sale_stock |
| `show_blacklist_buttons` | Blacklist Option when Unsubscribing | parameter `mass_mailing.show_blacklist_buttons` | mass_mailing |
| `show_effect` | Show Effect | parameter `base_setup.show_effect` | base_setup |
| `show_line_subtotals_tax_selection` |  | `website_id.show_line_subtotals_tax_selection` | website_sale |
| `sms_provider` |  | `company_id.sms_provider` | sms_twilio |
| `snailmail_color` | Print In Color | `company_id.snailmail_color` | snailmail |
| `snailmail_cover` | Add a Cover Page | `company_id.snailmail_cover` | snailmail |
| `snailmail_duplex` | Print Both sides | `company_id.snailmail_duplex` | snailmail |
| `social_default_image` | Default Social Share Image | `website_id.social_default_image` | website |
| `stock_move_email_validation` |  | `company_id.stock_move_email_validation` | stock |
| `stock_move_sms_validation` | SMS Validation with stock move | `company_id.stock_move_sms_validation` | stock_sms |
| `stock_sms_confirmation_template_id` |  | `company_id.stock_sms_confirmation_template_id` | stock_sms |
| `tax_calculation_rounding_method` | Tax calculation rounding method | `company_id.tax_calculation_rounding_method` | account |
| `tax_cash_basis_journal_id` | Tax Cash Basis Journal | `company_id.tax_cash_basis_journal_id` | account |
| `tax_exigibility` | Cash Basis | `company_id.tax_exigibility` | account |
| `tenor_api_key` | Klipy API key | parameter `discuss.klipy_api_key` | mail |
| `tenor_content_filter` | Klipy content filter | parameter `discuss.tenor_content_filter` | mail |
| `tenor_gif_limit` | Klipy GIF limits | parameter `discuss.tenor_gif_limit` | mail |
| `terms_type` |  | `company_id.terms_type` | account |
| `timesheet_encode_method` | Encoding Method | computed by the screen | hr_timesheet |
| `transfer_account_id` | Internal Transfer | `company_id.transfer_account_id` | account |
| `turnstile_secret_key` | CF Secret Key | parameter `cf.turnstile_secret_key` | website_cf_turnstile |
| `turnstile_site_key` | CF Site Key | parameter `cf.turnstile_site_key` | website_cf_turnstile |
| `twilio_account_sid` | Twilio Account SID | parameter `mail.twilio_account_sid` | mail |
| `twilio_account_token` | Twilio Account Auth Token | parameter `mail.twilio_account_token` | mail |
| `twitter_api_key` | API Key | `website_id.twitter_api_key` | website_twitter |
| `twitter_api_secret` | API secret | `website_id.twitter_api_secret` | website_twitter |
| `twitter_screen_name` | Favorites From | `website_id.twitter_screen_name` | website_twitter |
| `twitter_server_uri` | Twitter server uri | computed by the screen | website_twitter |
| `unsplash_access_key` | Access Key | parameter `unsplash.access_key` | web_unsplash |
| `unsplash_app_id` | Application ID | parameter `unsplash.app_id` | web_unsplash |
| `update_stock_quantities` |  | `company_id.point_of_sale_update_stock_quantities` | point_of_sale |
| `use_event_barcode` | Use Event Barcode | parameter `event.use_event_barcode` | event |
| `use_google_maps_static_api` | Google Maps static API | computed by the screen | event |
| `use_invoice_terms` | Default Terms & Conditions | parameter `account.use_invoice_terms` | account |
| `use_manufacturing_lead` | Default Manufacturing Lead Time | parameter `mrp.use_manufacturing_lead` | mrp |
| `use_po_lead` | Security Lead Time for Purchase | parameter `purchase.use_po_lead` | purchase |
| `use_security_lead` | Security Lead Time for Sales | parameter `sale_stock.use_security_lead` | sale_stock |
| `use_twilio_rtc_servers` | Use Twilio ICE servers | parameter `mail.use_twilio_rtc_servers` | mail |
| `user_default_rights` | Default Access Rights | parameter `base_setup.default_user_rights` | base_setup |
| `vat_check_vies` | Verify VAT Numbers | `company_id.vat_check_vies` | base_vat |
| `web_app_name` | Web App Name | parameter `web.web_app_name` | web |
| `website_company_id` | Website Company | `website_id.company_id` | website |
| `website_cookies_bar` |  | `website_id.cookies_bar` | website |
| `website_default_lang_code` | Default language code | `website_id.default_lang_id.code` | website |
| `website_default_lang_id` | Default language | `website_id.default_lang_id` | website |
| `website_domain` | Website Domain | `website_id.domain` | website |
| `website_homepage_url` |  | `website_id.homepage_url` | website |
| `website_id` | website | computed by the screen | website |
| `website_language_count` | Number of languages | `website_id.language_count` | website |
| `website_logo` |  | `website_id.logo` | website |
| `website_name` | Website Name | `website_id.name` | website |
| `website_sale_contact_us_button_url` | Button URL | `website_id.contact_us_button_url` | website_sale |
| `website_sale_enabled_portal_reorder_button` | Re-order From Portal | `website_id.enabled_portal_reorder_button` | website_sale |
| `website_sale_prevent_zero_price_sale` | Prevent Sale of Zero Priced Product | `website_id.prevent_zero_price_sale` | website_sale |
| `website_slide_google_app_key` |  | `website_id.website_slide_google_app_key` | website_slides |
| `website_warehouse_id` |  | `website_id.warehouse_id` | website_sale_stock |
| `work_permit_expiration_notice_period` | Work Permit Expiry Notice Period | `company_id.work_permit_expiration_notice_period` | hr_contract |
