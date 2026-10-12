# account — Invoicing

Depends on: base_setup, onboarding, product, analytic, portal, digest.

## `account.chart.template` (extends)


Extension points: `_get_demo_account`, `_get_demo_data`, `_get_demo_data_attachment`, `_get_demo_data_bank`, `_get_demo_data_journal`, `_get_demo_data_mail_activity`, `_get_demo_data_mail_message`, `_get_demo_data_move`, `_get_demo_data_partner`, `_get_demo_data_product`, `_get_demo_data_products`, `_get_demo_data_reconcile_model`, `_get_demo_data_statement`, `_get_demo_data_transactions`, `_get_demo_data_user`, `_get_demo_exception_product_template_xml_ids`, `_get_demo_exception_product_variant_xml_ids`, `_post_load_demo_data`

## `account.account` (defines)

Account

Inherits: `mail.thread`, `mail.activity.mixin`

- `name` Char “Account Name” (required)
- `description` Text
- `currency_id` Many2one → `res.currency` “Account Currency”
- `company_currency_id` Many2one → `res.currency` (compute=_compute_company_currency_id)
- `company_fiscal_country_code` Char (compute=_compute_company_fiscal_country_code)
- `code` Char “Code” (compute=_compute_code)
- `code_store` Char (company_dependent)
- `placeholder_code` Char “Display code” (compute=_compute_placeholder_code)
- `active` Boolean
- `used` Boolean (compute=_compute_used)
- `account_type` Selection “Type” (required, store, index, compute=_compute_account_type)
- `include_initial_balance` Boolean “Bring Accounts Balance Forward” (compute=_compute_include_initial_balance)
- `internal_group` Selection “Internal Group” (compute=_compute_internal_group)
- `reconcile` Boolean “Allow Reconciliation” (store, compute=_compute_reconcile)
- `tax_ids` Many2many → `account.tax` “Default Taxes”
- `note` Text “Internal Notes”
- `company_ids` Many2many → `res.company` “Companies” (required)
- `code_mapping_ids` One2many → `account.code.mapping`
- `tag_ids` Many2many → `account.account.tag` “Tags” (store, compute=_compute_account_tags)
- `group_id` Many2one → `account.group` (compute=_compute_account_group)
- `root_id` Many2one → `account.root` (compute=_compute_account_root)
- `opening_debit` Monetary “Opening Debit” (compute=_compute_opening_debit_credit)
- `opening_credit` Monetary “Opening Credit” (compute=_compute_opening_debit_credit)
- `opening_balance` Monetary “Opening Balance” (compute=_compute_opening_debit_credit)
- `current_balance` Float (compute=_compute_current_balance)
- `related_taxes_amount` Integer (compute=_compute_related_taxes_amount)
- `non_trade` Boolean
- `display_mapping_tab` Boolean

Public methods: `action_open_related_taxes`, `action_unmerge`, `copy_data`, `copy_translations`, `create`, `default_get`, `get_import_templates`, `load`, `name_create`, `name_search`, `write`

Extension points: `_action_unmerge`, `_action_unmerge_get_user_confirmation`, `_check_account_code`, `_check_account_is_bank_journal_bank_account`, `_check_account_type_sales_purchase_journal`, `_check_action_unmerge_possible`, `_check_company_consistency`, `_check_journal_consistency`, `_check_reconcile`, `_get_closest_parent_account`, `_get_internal_group`, `_get_most_frequent_account_for_partner`, `_get_most_frequent_accounts_for_partner`, `_get_name_search_account_types`, `_get_used_account_ids`

## `account.group` (defines)

Account Group

- `parent_id` Many2one → `account.group` (readonly, index)
- `name` Char (required)
- `code_prefix_start` Char (store, compute=_compute_code_prefix_start)
- `code_prefix_end` Char (store, compute=_compute_code_prefix_end)
- `company_id` Many2one → `res.company` (required, readonly)

Public methods: `create`, `unlink`, `write`

Extension points: `_check_parent_not_circular`

## `account.account.tag` (defines)

Account Tag

- `name` Char “Tag Name” (required)
- `applicability` Selection (required)
- `color` Integer “Color Index”
- `active` Boolean
- `country_id` Many2one → `res.country` “Country”
- `report_expression_id` Many2one → `account.report.expression` (compute=_compute_report_expression_id)
- `balance_negate` Boolean (compute=_compute_report_expression_id)

Public methods: `create`

Extension points: `_get_related_tax_report_expressions`, `_get_tax_tags`, `_get_tax_tags_domain`

## `account.analytic.account` (extends)

- `invoice_count` Integer “Invoice Count” (compute=_compute_invoice_count)
- `vendor_bill_count` Integer “Vendor Bill Count” (compute=_compute_vendor_bill_count)

Public methods: `action_view_invoice`, `action_view_vendor_bill`

## `account.analytic.distribution.model` (extends)

- `account_prefix` Char “Accounts Prefix”
- `product_id` Many2one → `product.product` “Product”
- `product_categ_id` Many2one → `product.category` “Product Category”
- `prefix_placeholder` Char (compute=_compute_prefix_placeholder)

Extension points: `_create_domain`, `_get_applicable_models`, `_get_default_search_domain_vals`

## `account.analytic.line` (extends)

Analytic Line

- `product_id` Many2one → `product.product` “Product”
- `product_category` Many2one (related=product_id.categ_id)
- `general_account_id` Many2one → `account.account` “Financial Account” (store, compute=_compute_general_account_id)
- `journal_id` Many2one → `account.journal` “Financial Journal” (readonly, store, related=move_line_id.journal_id)
- `partner_id` Many2one (store, compute=_compute_partner_id)
- `move_line_id` Many2one → `account.move.line` “Journal Item” (index)
- `code` Char
- `ref` Char “Ref.”
- `category` Selection
- `analytic_profitability` Selection “Profitability” (compute=_compute_analytic_profitability)

Public methods: `create`, `on_change_unit_amount`, `unlink`, `view_header_get`, `write`

Extension points: `_check_general_account_id`

## `account.analytic.applicability` (extends)

Analytic Plan's Applicabilities

- `business_domain` Selection
- `account_prefix` Char “Financial Accounts Prefixes”
- `product_categ_id` Many2one → `product.category` “Product Category”
- `display_account_prefix` Boolean (compute=_compute_display_account_prefix)
- `account_prefix_placeholder` Char (compute=_compute_prefix_placeholder)

Extension points: `_get_score`

## `account.bank.statement` (defines)

Bank Statement

- `name` Char “Reference” (store, compute=_compute_name)
- `reference` Char “External Reference”
- `date` Date (store, index, compute=_compute_date)
- `first_line_index` Char → `account.bank.statement.line` (store, compute=_compute_first_line_index)
- `balance_start` Monetary “Starting Balance” (store, compute=_compute_balance_start)
- `balance_end` Monetary “Computed Balance” (store, compute=_compute_balance_end)
- `balance_end_real` Monetary “Ending Balance” (store, compute=_compute_balance_end_real)
- `company_id` Many2one → `res.company` (store, related=journal_id.company_id)
- `currency_id` Many2one → `res.currency` (store, compute=_compute_currency_id)
- `journal_id` Many2one → `account.journal` (store, compute=_compute_journal_id)
- `line_ids` One2many → `account.bank.statement.line` “Statement lines”
- `is_complete` Boolean (store, compute=_compute_is_complete)
- `is_valid` Boolean (compute=_compute_is_valid)
- `journal_has_invalid_statements` Boolean (related=journal_id.has_invalid_statements)
- `problem_description` Text (compute=_compute_problem_description)
- `attachment_ids` Many2many → `ir.attachment` “Attachments”

Public methods: `create`, `default_get`, `write`

Extension points: `_check_attachments`, `_get_invalid_statement_ids`, `_get_statement_validity`

## `account.bank.statement.line` (defines)

Bank Statement Line

- `move_id` Many2one → `account.move` “Journal Entry” (required, readonly, index)
- `journal_id` Many2one → `account.journal` (required, store, related=move_id.journal_id)
- `company_id` Many2one → `res.company` (required, store, related=move_id.company_id)
- `statement_id` Many2one → `account.bank.statement` “Statement” (index)
- `payment_ids` Many2many → `account.payment` “Auto-generated Payments”
- `sequence` Integer
- `partner_id` Many2one → `res.partner` “Partner”
- `account_number` Char “Bank Account Number”
- `partner_name` Char
- `transaction_type` Char
- `payment_ref` Char “Label”
- `currency_id` Many2one → `res.currency` “Journal Currency” (store, compute=_compute_currency_id)
- `amount` Monetary
- `running_balance` Monetary (compute=_compute_running_balance)
- `foreign_currency_id` Many2one → `res.currency` “Foreign Currency”
- `amount_currency` Monetary “Amount in Currency” (store, compute=_compute_amount_currency)
- `amount_residual` Float “Residual Amount” (store, compute=_compute_is_reconciled)
- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `internal_index` Char “Internal Reference” (store, compute=_compute_internal_index)
- `is_reconciled` Boolean “Is Reconciled” (store, compute=_compute_is_reconciled)
- `statement_complete` Boolean (related=statement_id.is_complete)
- `statement_valid` Boolean (related=statement_id.is_valid)
- `statement_balance_end_real` Monetary (related=statement_id.balance_end_real)
- `statement_name` Char “Statement Name” (related=statement_id.name)
- `transaction_details` Json (readonly)

Public methods: `action_undo_reconciliation`, `create`, `default_get`, `formatted_read_group`, `new`, `unlink`, `write`

Extension points: `_check_allow_unlink`, `_check_amounts_currencies`, `_get_accounting_amounts_and_currencies`, `_get_default_amls_matching_domain`, `_get_default_journal`, `_get_default_statement`, `_prepare_counterpart_amounts_using_st_line_rate`, `_prepare_move_line_default_vals`

## `account.move` (extends)

- `statement_line_ids` One2many → `account.bank.statement.line` “Statements”

## `account.cash.rounding` (defines)

Account Cash Rounding

- `name` Char “Name” (required)
- `rounding` Float “Rounding Precision” (required)
- `strategy` Selection “Rounding Strategy” (required)
- `profit_account_id` Many2one → `account.account` “Profit Account” (company_dependent)
- `loss_account_id` Many2one → `account.account` “Loss Account” (company_dependent)
- `rounding_method` Selection “Rounding Method” (required)

Public methods: `compute_difference`, `round`, `validate_rounding`

## `account.code.mapping` (defines)

Mapping of account codes per company

- `account_id` Many2one → `account.account` “Account” (compute=_compute_account_id)
- `company_id` Many2one → `res.company` “Company” (compute=_compute_company_id)
- `code` Char “Code” (compute=_compute_code)

Public methods: `create`

## `account.document.import.mixin` (defines)

Business document import mixin


Extension points: `_create_records_from_attachments`, `_get_edi_decoder`, `_get_import_file_type`, `_get_similarity_score`, `_get_xml_tree`

## `account.full.reconcile` (defines)

Full Reconcile

- `partial_reconcile_ids` One2many → `account.partial.reconcile` “Reconciliation Parts”
- `reconciled_line_ids` One2many → `account.move.line` “Matched Journal Items”

Public methods: `create`, `unlink`

## `account.incoterms` (defines)

Incoterms

- `name` Char “Name” (required)
- `code` Char “Code” (required)
- `active` Boolean “Active”

## `account.journal.group` (defines)

Account Journal Group

- `name` Char “Ledger group” (required)
- `company_id` Many2one → `res.company`
- `excluded_journal_ids` Many2many → `account.journal` “Excluded Journals”
- `sequence` Integer

## `account.journal` (defines)

Journal

Inherits: `portal.mixin`, `mail.alias.mixin.optional`, `mail.thread`, `mail.activity.mixin`

- `name` Char “Journal Name” (required)
- `name_placeholder` Char (compute=_compute_name_placeholder)
- `code` Char “Sequence Prefix” (required, store, compute=_compute_code)
- `active` Boolean
- `type` Selection (required)
- `is_self_billing` Boolean “Self Billing”
- `default_account_type` Char “Default Account Type” (compute=_compute_default_account_type)
- `default_account_id` Many2one → `account.account` “Default Account”
- `suspense_account_id` Many2one → `account.account` “Suspense Account” (store, compute=_compute_suspense_account_id)
- `non_deductible_account_id` Many2one → `account.account` “Private Share Account” (store)
- `restrict_mode_hash_table` Boolean “Secure Posted Entries with Hash”
- `sequence` Integer
- `invoice_reference_type` Selection “Communication Type” (required)
- `invoice_reference_model` Selection “Communication Standard” (required)
- `currency_id` Many2one → `res.currency` “Currency”
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `country_code` Char (readonly, related=company_id.account_fiscal_country_id.code)
- `account_fiscal_country_group_codes` Json (related=company_id.account_fiscal_country_group_codes)
- `refund_sequence` Boolean “Dedicated Credit Note Sequence” (store, compute=_compute_refund_sequence)
- `payment_sequence` Boolean “Dedicated Payment Sequence” (store, compute=_compute_payment_sequence)
- `invoice_template_pdf_report_id` Many2one → `ir.actions.report` “Invoice report”
- `available_invoice_template_pdf_report_ids` One2many → `ir.actions.report` (compute=_compute_available_invoice_template_pdf_report_ids)
- `display_invoice_template_pdf_report_id` Boolean
- `sequence_override_regex` Text
- `inbound_payment_method_line_ids` One2many → `account.payment.method.line` “Inbound Payment Methods” (store, compute=_compute_inbound_payment_method_line_ids)
- `outbound_payment_method_line_ids` One2many → `account.payment.method.line` “Outbound Payment Methods” (store, compute=_compute_outbound_payment_method_line_ids)
- `profit_account_id` Many2one → `account.account` “Profit Account”
- `loss_account_id` Many2one → `account.account` “Loss Account”
- `company_partner_id` Many2one → `res.partner` “Account Holder” (readonly, related=company_id.partner_id)
- `bank_account_id` Many2one → `res.partner.bank` “Bank Account”
- `bank_statements_source` Selection “Bank Feeds”
- `bank_acc_number` Char (related=bank_account_id.acc_number)
- `bank_id` Many2one → `res.bank` (related=bank_account_id.bank_id)
- `alias_name` Char
- `journal_group_ids` Many2many → `account.journal.group` “Ledger Group”
- `available_payment_method_ids` Many2many → `account.payment.method` (compute=_compute_available_payment_method_ids)
- `selected_payment_method_codes` Char (compute=_compute_selected_payment_method_codes)
- `accounting_date` Date (compute=_compute_accounting_date)
- `display_alias_fields` Boolean (compute=_compute_display_alias_fields)
- `has_invalid_statements` Boolean (compute=_compute_has_invalid_statements)
- `show_fetch_in_einvoices_button` Boolean “Show E-Invoice Buttons” (compute=_compute_show_fetch_in_einvoices_button)
- `show_refresh_out_einvoices_status_button` Boolean “Show E-Invoice Status Buttons” (compute=_compute_show_refresh_out_einvoices_status_button)
- `incoming_einvoice_notification_email` Char “Send Copy To”

Public methods: `action_configure_bank_journal`, `button_fetch_in_einvoices`, `button_refresh_out_einvoices_status`, `button_unsubscribe_from_invoice_notifications`, `copy_data`, `create`, `create_document_from_attachment`, `set_bank_account`, `unlink`, `write`

Extension points: `_check_auto_post_draft_entries`, `_check_bank_account`, `_check_company_consistency`, `_check_incoming_einvoice_notification_email`, `_check_payment_method_line_ids_multiplicity`, `_check_type_default_account_id_type`, `_create_default_account`, `_create_document_from_attachment`, `_get_available_payment_method_lines`, `_get_bank_statements_available_sources`, `_get_default_account_domain`, `_get_journal_bank_account_balance`, `_get_journal_inbound_outstanding_payment_accounts`, `_get_journal_notification_unsubscribe_scope`, `_get_journal_outbound_outstanding_payment_accounts`, `_get_journals_payment_method_information`, `_get_next_journal_default_code`, `_prepare_credit_account_vals`, `_prepare_liquidity_account_vals`

## `account.journal` (extends)

- `kanban_dashboard` Text (compute=_kanban_dashboard)
- `kanban_dashboard_graph` Text (compute=_kanban_dashboard_graph)
- `json_activity_data` Text (compute=_get_json_activity_data)
- `show_on_dashboard` Boolean “Show journal on dashboard”
- `color` Integer “Color Index”
- `current_statement_balance` Monetary (compute=_compute_current_statement_balance)
- `has_statement_lines` Boolean (compute=_compute_current_statement_balance)
- `entries_count` Integer (compute=_compute_entries_count)
- `has_posted_entries` Boolean (compute=_compute_has_entries)
- `has_entries` Boolean (compute=_compute_has_entries)
- `has_sequence_holes` Boolean (compute=_compute_has_sequence_holes)
- `has_unhashed_entries` Boolean “Unhashed Entries” (compute=_compute_has_unhashed_entries)
- `last_statement_id` Many2one → `account.bank.statement` (compute=_compute_last_bank_statement)

Public methods: `action_create_new`, `action_create_vendor_bill`, `action_post_all_entries`, `create_bank_statement`, `create_customer_payment`, `create_supplier_payment`, `is_sample_action_available`, `open_action`, `open_action_with_context`, `open_bank_difference_action`, `open_invalid_statements_action`, `open_payments_action`, `show_sequence_holes`, `show_unhashed_entries`, `to_check_ids`

Extension points: `_get_bank_cash_graph_data`, `_get_direct_bank_payments`, `_get_draft_sales_purchases_query`, `_get_journal_dashboard_bank_running_balance`, `_get_journal_dashboard_data_batched`, `_get_journal_dashboard_outstanding_payments`, `_get_json_activity_data`, `_get_move_action_context`, `_get_moves_to_hash`, `_get_open_sale_purchase_query`, `_get_sale_purchase_graph_data`, `_get_to_check_payment_query`, `_get_to_pay_select`

## `account.lock_exception` (defines)

Account Lock Exception

- `active` Boolean “Active”
- `state` Selection “State” (compute=_compute_state)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `user_id` Many2one → `res.users` “User”
- `reason` Char “Reason”
- `end_datetime` Datetime “End Date”
- `lock_date_field` Selection “Lock Date Field” (required)
- `lock_date` Date “Changed Lock Date”
- `company_lock_date` Date “Original Lock Date”
- `fiscalyear_lock_date` Date “Global Lock Date” (compute=_compute_lock_dates)
- `tax_lock_date` Date “Tax Return Lock Date” (compute=_compute_lock_dates)
- `sale_lock_date` Date “Sales Lock Date” (compute=_compute_lock_dates)
- `purchase_lock_date` Date “Purchase Lock Date” (compute=_compute_lock_dates)

Public methods: `action_revoke`, `action_show_audit_trail_during_exception`, `copy`, `create`

Extension points: `_get_active_exceptions_domain`, `_get_audit_trail_during_exception_domain`

## `account.move` (defines)

Journal Entry

Inherits: `portal.mixin`, `mail.thread.main.attachment`, `mail.activity.mixin`, `sequence.mixin`, `product.catalog.mixin`, `account.document.import.mixin`

- `name` Char “Number” (store, compute=_compute_name)
- `name_placeholder` Char (compute=_compute_name_placeholder)
- `ref` Char “Reference”
- `date` Date “Date” (required, store, index, compute=_compute_date)
- `state` Selection “Status” (required, readonly)
- `move_type` Selection “Type” (required, readonly, index)
- `is_storno` Boolean (compute=_compute_is_storno)
- `journal_id` Many2one → `account.journal` “Journal” (required, store, compute=_compute_journal_id)
- `journal_group_id` Many2one → `account.journal.group` “Ledger”
- `company_id` Many2one → `res.company` “Company” (store, index, compute=_compute_company_id)
- `line_ids` One2many → `account.move.line` “Journal Items”
- `journal_line_ids` One2many → `account.move.line` “Journal Items (DEPRECATED)”
- `exchange_diff_partial_ids` One2many → `account.partial.reconcile` “Related reconciliation”
- `origin_payment_id` Many2one → `account.payment` “Payment”
- `matched_payment_ids` Many2many → `account.payment` “Matched Payments”
- `reconciled_payment_ids` Many2many → `account.payment` “Reconciled Payments” (compute=_compute_reconciled_payment_ids)
- `payment_count` Integer (compute=_compute_payment_count)
- `statement_line_id` Many2one → `account.bank.statement.line` “Statement Line”
- `statement_id` Many2one (related=statement_line_id.statement_id)
- `adjusting_entry_origin_move_ids` Many2many → `account.move` “Adjusting Entry Origin Moves”
- `adjusting_entry_origin_label` Char (compute=_compute_adjusting_entry_origin_label)
- `adjusting_entry_origin_moves_count` Integer “Adjusting Entry Origin Moves Count” (compute=_compute_adjusting_entry_origin_moves_count)
- `adjusting_entries_move_ids` Many2many → `account.move` “Created Adjusting Entries”
- `adjusting_entries_count` Integer “Adjusting Entries Count” (compute=_compute_adjusting_entries_count)
- `tax_cash_basis_rec_id` Many2one → `account.partial.reconcile` “Tax Cash Basis Entry of”
- `tax_cash_basis_origin_move_id` Many2one → `account.move` “Cash Basis Origin” (readonly)
- `tax_cash_basis_created_move_ids` One2many → `account.move` “Cash Basis Entries”
- `always_tax_exigible` Boolean (store, compute=_compute_always_tax_exigible)
- `auto_post` Selection “Auto-post” (required)
- `auto_post_until` Date “Auto-post until” (store, compute=_compute_auto_post_until)
- `auto_post_origin_id` Many2one → `account.move` “First recurring entry” (readonly)
- `hide_post_button` Boolean (readonly, compute=_compute_hide_post_button)
- `checked` Boolean “Reviewed” (store, compute=_compute_checked)
- `posted_before` Boolean
- `suitable_journal_ids` Many2many → `account.journal` (compute=_compute_suitable_journal_ids)
- `highest_name` Char (compute=_compute_highest_name)
- `made_sequence_gap` Boolean
- `show_name_warning` Boolean
- `type_name` Char “Type Name” (compute=_compute_type_name)
- `country_code` Char (readonly, related=company_id.account_fiscal_country_id.code)
- `account_fiscal_country_group_codes` Json (related=company_id.account_fiscal_country_group_codes)
- `company_price_include` Selection (readonly, related=company_id.account_price_include)
- `attachment_ids` One2many → `ir.attachment` “Attachments”
- `audit_trail_message_ids` One2many → `mail.message` “Audit Trail Messages”
- `no_followup` Boolean “No Follow-Up” (compute=_compute_no_followup)
- `restrict_mode_hash_table` Boolean (related=journal_id.restrict_mode_hash_table)
- `secure_sequence_number` Integer “Inalterability No Gap Sequence #” (readonly, index)
- `inalterable_hash` Char “Inalterability Hash” (readonly)
- `secured` Boolean (compute=_compute_secured)
- `invoice_line_ids` One2many → `account.move.line` “Invoice lines”
- `invoice_date` Date “Invoice/Bill Date” (index)
- `invoice_date_due` Date “Due Date” (store, index, compute=_compute_invoice_date_due)
- `delivery_date` Date “Delivery Date” (store, compute=_compute_delivery_date)
- `show_delivery_date` Boolean (compute=_compute_show_delivery_date)
- `taxable_supply_date` Date “Taxable Supply Date” (store, compute=_compute_taxable_supply_date)
- `show_taxable_supply_date` Boolean (compute=_compute_show_taxable_supply_date)
- `taxable_supply_date_placeholder` Char (compute=_compute_taxable_supply_date_placeholder)
- `invoice_payment_term_id` Many2one → `account.payment.term` “Payment Terms” (store, compute=_compute_invoice_payment_term_id)
- `needed_terms` Binary (compute=_compute_needed_terms)
- `needed_terms_dirty` Boolean (compute=_compute_needed_terms)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `show_journal` Boolean (compute=_compute_show_journal)
- `partner_id` Many2one → `res.partner` “Partner” (index)
- `commercial_partner_id` Many2one → `res.partner` “Commercial Entity” (readonly, store, compute=_compute_commercial_partner_id)
- `partner_shipping_id` Many2one → `res.partner` “Delivery Address” (store, compute=_compute_partner_shipping_id)
- `partner_bank_id` Many2one → `res.partner.bank` “Recipient Bank” (store, compute=_compute_partner_bank_id)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (store, compute=_compute_fiscal_position_id)
- `payment_reference` Char “Payment Reference” (store, compute=_compute_payment_reference)
- `sanitize_payment_reference` Char “Label sanitize” (compute=_compute_sanitize_payment_reference)
- `display_qr_code` Boolean “Display QR-code” (compute=_compute_display_qr_code)
- `display_link_qr_code` Boolean “Display Link QR-code” (compute=_compute_display_link_qr_code)
- `qr_code_method` Selection “Payment QR-code”
- `invoice_outstanding_credits_debits_widget` Binary (compute=_compute_payments_widget_to_reconcile_info)
- `invoice_has_outstanding` Boolean (compute=_compute_invoice_has_outstanding)
- `invoice_payments_widget` Binary (compute=_compute_payments_widget_reconciled_info)
- `preferred_payment_method_line_id` Many2one → `account.payment.method.line` “Preferred Payment Method Line” (store, compute=_compute_preferred_payment_method_line_id)
- `company_currency_id` Many2one “Company Currency” (readonly, related=company_id.currency_id)
- `currency_id` Many2one → `res.currency` “Currency” (required, store, compute=_compute_currency_id)
- `expected_currency_rate` Float (compute=_compute_expected_currency_rate)
- `invoice_currency_rate` Float “Currency Rate” (store, compute=_compute_invoice_currency_rate)
- `direction_sign` Integer (compute=_compute_direction_sign)
- `amount_untaxed` Monetary “Untaxed Amount” (readonly, store, compute=_compute_amount)
- `amount_tax` Monetary “Tax” (readonly, store, compute=_compute_amount)
- `amount_total` Monetary “Total” (readonly, store, compute=_compute_amount)
- `amount_residual` Monetary “Amount Due” (store, compute=_compute_amount)
- `amount_untaxed_signed` Monetary “Untaxed Amount Signed” (readonly, store, compute=_compute_amount)
- `amount_untaxed_in_currency_signed` Monetary “Untaxed Amount Signed Currency” (readonly, store, compute=_compute_amount)
- `amount_tax_signed` Monetary “Tax Signed” (readonly, store, compute=_compute_amount)
- `amount_total_signed` Monetary “Total Signed” (readonly, store, compute=_compute_amount)
- `amount_total_in_currency_signed` Monetary “Total in Currency Signed” (readonly, store, compute=_compute_amount)
- `amount_residual_signed` Monetary “Amount Due Signed” (store, compute=_compute_amount)
- `tax_totals` Binary “Invoice Totals” (compute=_compute_tax_totals)
- `payment_state` Selection “Payment Status” (readonly, store, compute=_compute_payment_state)
- `status_in_payment` Selection (compute=_compute_status_in_payment)
- `amount_total_words` Char “Amount total in words” (compute=_compute_amount_total_words)
- `reversed_entry_id` Many2one → `account.move` “Reversal of” (readonly)
- `reversal_move_ids` One2many → `account.move`
- `invoice_vendor_bill_id` Many2one → `account.move` “Vendor Bill”
- `invoice_source_email` Char “Source Email”
- `invoice_partner_display_name` Char (store, compute=_compute_invoice_partner_display_info)
- `is_manually_modified` Boolean
- `quick_edit_mode` Boolean (compute=_compute_quick_edit_mode)
- `quick_edit_total_amount` Monetary “Total (Tax inc.)”
- `quick_encoding_vals` Json (compute=_compute_quick_encoding_vals)
- `narration` Html “Terms and Conditions” (store, compute=_compute_narration)
- `is_move_sent` Boolean (readonly)
- `is_being_sent` Boolean (compute=_compute_is_being_sent)
- `move_sent_values` Selection “Sent” (compute=compute_move_sent_values)
- `invoice_user_id` Many2one → `res.users` “Salesperson” (store, compute=_compute_invoice_default_sale_person)
- `user_id` Many2one “User” (related=invoice_user_id)
- `invoice_origin` Char “Origin” (readonly)
- `invoice_incoterm_id` Many2one → `account.incoterms` “Incoterm” (store, compute=_compute_incoterm)
- `incoterm_location` Char “Incoterm Location” (store, compute=_compute_incoterm_location)
- `invoice_cash_rounding_id` Many2one → `account.cash.rounding` “Cash Rounding Method”
- `sending_data` Json
- `invoice_pdf_report_id` Many2one → `ir.attachment` “PDF Attachment”
- `invoice_pdf_report_file` Binary “PDF File”
- `invoice_incoterm_placeholder` Char (compute=_compute_invoice_incoterm_placeholder)
- `invoice_filter_type_domain` Char (compute=_compute_invoice_filter_type_domain)
- `bank_partner_id` Many2one → `res.partner` (compute=_compute_bank_partner_id)
- `tax_lock_date_message` Char (compute=_compute_tax_lock_date_message)
- `display_inactive_currency_warning` Boolean (compute=_compute_display_inactive_currency_warning)
- `tax_country_id` Many2one → `res.country` (compute=_compute_tax_country_id)
- `tax_country_code` Char (compute=_compute_tax_country_code)
- `has_reconciled_entries` Boolean (compute=_compute_has_reconciled_entries)
- `show_reset_to_draft_button` Boolean (compute=_compute_show_reset_to_draft_button)
- `partner_credit_warning` Text (compute=_compute_partner_credit_warning)
- `duplicated_ref_ids` Many2many → `account.move` (compute=_compute_duplicated_ref_ids)
- `is_draft_duplicated_ref_ids` Boolean (compute=_compute_is_draft_duplicated_ref_ids)
- `is_exact_move_duplicate` Boolean (compute=_compute_is_draft_duplicated_ref_ids)
- `need_cancel_request` Boolean (compute=_compute_need_cancel_request)
- `show_update_fpos` Boolean “Has Fiscal Position Changed”
- `payment_term_details` Binary (compute=_compute_payment_term_details)
- `show_payment_term_details` Boolean (compute=_compute_show_payment_term_details)
- `show_discount_details` Boolean (compute=_compute_show_payment_term_details)
- `abnormal_amount_warning` Text (compute=_compute_abnormal_warnings)
- `abnormal_date_warning` Text (compute=_compute_abnormal_warnings)
- `alerts` Json (compute=_compute_alerts)
- `taxes_legal_notes` Html “Taxes Legal Notes” (compute=_compute_taxes_legal_notes)
- `next_payment_date` Date “Next Payment Date” (compute=_compute_next_payment_date)
- `display_send_button` Boolean (compute=_compute_display_send_button)
- `highlight_send_button` Boolean (compute=_compute_highlight_send_button)
- `is_sale_installed` Boolean (compute=_compute_is_sale_installed)

Public methods: `action_activate_currency`, `action_add_from_catalog`, `action_delete_duplicates`, `action_duplicate`, `action_force_register_payment`, `action_invoice_download_pdf`, `action_invoice_sent`, `action_move_download_all`, `action_open_business_doc`, `action_open_journal_items`, `action_post`, `action_print_pdf`, `action_register_payment`, `action_reverse`, `action_send_and_print`, `action_switch_move_type`, `action_toggle_block_payment`, `action_update_fpos_values`, `action_validate_moves_with_confirmation`, `button_cancel`, `button_draft`, `button_hash`, `button_request_cancel`, `button_set_checked`, `check_field_access_rights`, `check_move_sequence_chain`, `check_selected_moves`, `compute_move_sent_values`, `copy`, `copy_data`, `create`, `get_currency_rate`, `get_extra_print_items`, `get_import_templates`, `get_inbound_types`, `get_invoice_localisation_fields_required_to_invoice`, `get_invoice_types`, `get_outbound_types`, `get_purchase_types`, `get_sale_types`, `is_entry`, `is_inbound`, `is_invoice`, `is_outbound`, `is_purchase_document`, `is_receipt`, `is_sale_document`, `js_assign_outstanding_line`, `js_remove_outstanding_partial`, `message_new`, `onchange`, `open_adjusting_entries`, `open_adjusting_entry_origin_moves`, `open_created_caba_entries`, `open_payments`, `open_reconcile_view`, `preview_invoice`, `read`, `refresh_invoice_currency_rate`, `search_read`, `set_moves_checked`, `unlink`, `write`

Extension points: `_action_invoice_ready_to_be_sent`, `_check_balanced`, `_check_draftable`, `_check_fiscal_lock_dates`, `_check_invoice_currency_rate`, `_check_journal_move_type`, `_check_total_amount`, `_get_accounting_date`, `_get_accounting_date_source`, `_get_action_add_from_catalog_extra_context`, `_get_action_with_base_document_layout_configurator`, `_get_alerts`, `_get_all_reconciled_invoice_partials`, `_get_automatic_balancing_account`, `_get_available_action_reports`, `_get_available_invoice_template_pdf_report_ids`, `_get_chain_info`, `_get_chains_to_hash`, `_get_copy_message_content`, `_get_default_read_fields`, `_get_discount_allocation_account`, `_get_edi_creation`, `_get_expected_currency_rate_at`, `_get_fields_to_copy_recurring_entries`, `_get_fields_to_detach`, `_get_frequent_account_and_taxes`, `_get_installments_data`, `_get_integrity_hash_fields`, `_get_integrity_hash_fields_and_subfields`, `_get_invoice_computed_reference`, `_get_invoice_counterpart_amls_for_early_payment_discount`, `_get_invoice_counterpart_amls_for_early_payment_discount_per_payment_term_line`, `_get_invoice_currency_rate_date`, `_get_invoice_filter_type_domain`, `_get_invoice_in_payment_state`, `_get_invoice_legal_documents`, `_get_invoice_legal_documents_all`, `_get_invoice_mail_template_dynamic_report_filename`, `_get_invoice_next_payment_values`, `_get_invoice_pdf_proforma`, `_get_invoice_portal_extra_values`, `_get_invoice_proforma_pdf_report_filename`, `_get_invoice_reference_euro_invoice`, `_get_invoice_reference_euro_partner`, `_get_invoice_reference_number_invoice`, `_get_invoice_reference_number_partner`, `_get_invoice_reference_odoo_invoice`, `_get_invoice_reference_odoo_partner`, `_get_invoice_report_filename`, `_get_last_sequence_domain`, `_get_lines_onchange_currency`, `_get_lock_date_message`, `_get_mail_template`, `_get_mail_thread_data_attachments`, `_get_move_display_name`, `_get_move_hash_domain`, `_get_move_lines_to_report`, `_get_move_zip_export_docs`, `_get_moves_requiring_confirmation`, `_get_name_invoice_report`, `_get_parent_field_on_child_model`, `_get_partner_credit_warning_exclude_amount`, `_get_portal_payment_link`, `_get_product_base_line_currency_rate`, `_get_product_catalog_domain`, `_get_product_catalog_order_data`, `_get_product_catalog_record_lines`, `_get_product_price_and_data`, `_get_protected_vals`, `_get_quick_edit_suggestions`, `_get_reconciled_amls`, `_get_reconciled_invoices`, `_get_reconciled_invoices_partials`, `_get_reconciled_payments`, `_get_reconciled_statement_lines`, `_get_report_base_filename`, `_get_rounded_base_and_tax_lines`, `_get_sequence_date_range`, `_get_sequence_suffix`, `_get_starting_sequence`, `_get_suitable_journal_ids`, `_get_sync_stack`, `_get_unbalanced_moves`, `_get_unlink_logger_message`, `_get_valid_journal_types`, `_get_violated_lock_dates`, `_post_process_link_to_purchase_order`, `_prepare_cash_rounding_base_line_for_taxes_computation`, `_prepare_edi_vals_to_export`, `_prepare_epd_base_line_for_taxes_computation`, `_prepare_epd_base_lines_for_taxes_computation_from_base_lines`, `_prepare_invoice_aggregated_taxes`, `_prepare_non_deductible_base_line_for_taxes_computation`, `_prepare_non_deductible_base_lines_for_taxes_computation_from_base_lines`, `_prepare_product_base_line_for_taxes_computation`, `_prepare_tax_line_for_taxes_computation`, `_prepare_tax_lines_for_taxes_computation`

## `account.move.line` (defines)

Journal Item

Inherits: `analytic.mixin`

- `move_id` Many2one → `account.move` “Journal Entry” (required, readonly, index)
- `journal_id` Many2one (store, index, related=move_id.journal_id)
- `journal_group_id` Many2one → `account.journal.group` “Ledger”
- `company_id` Many2one (readonly, store, index, related=move_id.company_id)
- `company_currency_id` Many2one “Company Currency” (readonly, store, related=move_id.company_currency_id)
- `move_name` Char “Number” (store, related=move_id.name)
- `parent_state` Selection (store, related=move_id.state)
- `date` Date (store, related=move_id.date)
- `invoice_date` Date (store, related=move_id.invoice_date)
- `ref` Char (store, related=move_id.ref)
- `is_storno` Boolean “Company Storno Accounting” (store, compute=_compute_is_storno)
- `sequence` Integer (store, compute=_compute_sequence)
- `move_type` Selection (related=move_id.move_type)
- `account_id` Many2one → `account.account` “Account” (store, compute=_compute_account_id)
- `account_name` Char (related=account_id.name)
- `account_code` Char (related=account_id.code)
- `search_account_id` Many2one → `account.account`
- `name` Char “Label” (store, compute=_compute_name)
- `translated_product_name` Text (compute=_compute_translated_product_name)
- `debit` Monetary “Debit” (store, compute=_compute_debit_credit)
- `credit` Monetary “Credit” (store, compute=_compute_debit_credit)
- `balance` Monetary “Balance” (store, compute=_compute_balance)
- `cumulated_balance` Monetary “Cumulated Balance” (compute=_compute_cumulated_balance)
- `currency_rate` Float (compute=_compute_currency_rate)
- `amount_currency` Monetary “Amount in Currency” (store, compute=_compute_amount_currency)
- `currency_id` Many2one → `res.currency` “Currency” (required, store, compute=_compute_currency_id)
- `is_same_currency` Boolean (compute=_compute_same_currency)
- `partner_id` Many2one → `res.partner` “Partner” (store, compute=_compute_partner_id)
- `is_imported` Boolean
- `reconcile_model_id` Many2one → `account.reconcile.model` “Reconciliation Model” (readonly)
- `payment_id` Many2one → `account.payment` “Originator Payment” (store, related=move_id.origin_payment_id)
- `statement_line_id` Many2one → `account.bank.statement.line` “Originator Statement Line” (store, related=move_id.statement_line_id)
- `statement_id` Many2one (store, related=statement_line_id.statement_id)
- `commercial_partner_country` Many2one “Commercial Partner Country” (related=move_id.commercial_partner_id.country_id)
- `tax_ids` Many2many → `account.tax` “Taxes” (store, compute=_compute_tax_ids)
- `group_tax_id` Many2one → `account.tax` “Originator Group of Taxes”
- `tax_line_id` Many2one → `account.tax` “Originator Tax” (store, related=tax_repartition_line_id.tax_id)
- `tax_group_id` Many2one “Originator tax group” (store, related=tax_line_id.tax_group_id)
- `tax_base_amount` Monetary “Base Amount” (readonly)
- `tax_repartition_line_id` Many2one → `account.tax.repartition.line` “Originator Tax Distribution Line” (readonly)
- `tax_tag_ids` Many2many → `account.account.tag` “Tags”
- `extra_tax_data` Json
- `amount_residual` Monetary “Residual Amount” (store, compute=_compute_amount_residual)
- `amount_residual_currency` Monetary “Residual Amount in Currency” (store, compute=_compute_amount_residual)
- `reconciled` Boolean (store, compute=_compute_amount_residual)
- `full_reconcile_id` Many2one → `account.full.reconcile` “Matching” (readonly)
- `matched_debit_ids` One2many → `account.partial.reconcile` “Matched Debits” (readonly)
- `matched_credit_ids` One2many → `account.partial.reconcile` “Matched Credits” (readonly)
- `reconciled_lines_ids` Many2many → `account.move.line` (compute=_compute_reconciled_lines_ids)
- `reconciled_lines_excluding_exchange_diff_ids` Many2many → `account.move.line` (compute=_compute_reconciled_lines_excluding_exchange_diff_ids)
- `first_reconciled_lines_id` Many2one → `account.move.line` (compute=_compute_reconciled_lines_ids)
- `count_reconciled_lines` Integer (compute=_compute_reconciled_lines_ids)
- `first_reconciled_lines_excluding_exchange_diff_id` Many2one → `account.move.line` (compute=_compute_reconciled_lines_excluding_exchange_diff_ids)
- `count_reconciled_lines_excluding_exchange_diff` Integer (compute=_compute_reconciled_lines_excluding_exchange_diff_ids)
- `exchange_move_ids` Many2many → `account.move` (compute=_compute_exchange_move)
- `matching_number` Char “Matching #”
- `is_account_reconcile` Boolean “Account Reconcile” (related=account_id.reconcile)
- `account_type` Selection “Internal Type” (related=account_id.account_type)
- `account_internal_group` Selection (related=account_id.internal_group)
- `account_root_id` Many2one “Account Root” (related=account_id.root_id)
- `product_category_id` Many2one (related=product_id.product_tmpl_id.categ_id)
- `display_type` Selection (required, store, compute=_compute_display_type)
- `collapse_composition` Boolean “Hide Composition”
- `collapse_prices` Boolean “Hide Prices”
- `parent_id` Many2one → `account.move.line` “Parent Section Line” (compute=_compute_parent_id)
- `product_id` Many2one → `product.product` “Product” (index)
- `allowed_uom_ids` Many2many → `uom.uom` (compute=_compute_allowed_uom_ids)
- `product_uom_id` Many2one → `uom.uom` “Unit” (store, compute=_compute_product_uom_id)
- `quantity` Float “Quantity” (store, compute=_compute_quantity)
- `date_maturity` Date “Due Date” (index)
- `price_unit` Float “Unit Price” (store, compute=_compute_price_unit)
- `price_subtotal` Monetary “Subtotal” (store, compute=_compute_totals)
- `price_total` Monetary “Total” (store, compute=_compute_totals)
- `discount` Float “Discount (%)”
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (readonly, related=company_id.tax_calculation_rounding_method)
- `deductible_amount` Float “Deductibility”
- `term_key` Binary (compute=_compute_term_key)
- `epd_key` Binary (compute=_compute_epd_key)
- `epd_needed` Binary (compute=_compute_epd_needed)
- `epd_dirty` Boolean (compute=_compute_epd_needed)
- `discount_allocation_key` Binary (compute=_compute_discount_allocation_key)
- `discount_allocation_needed` Binary (compute=_compute_discount_allocation_needed)
- `discount_allocation_dirty` Boolean (compute=_compute_discount_allocation_needed)
- `analytic_line_ids` One2many → `account.analytic.line` “Analytic lines”
- `analytic_distribution` Json
- `has_invalid_analytics` Boolean (compute=_compute_has_invalid_analytics)
- `discount_date` Date “Discount Date” (readonly, store)
- `discount_amount_currency` Monetary “Discount amount in Currency” (store)
- `discount_balance` Monetary “Discount Balance” (store)
- `payment_date` Date “Next Payment Date” (compute=_compute_payment_date)
- `is_refund` Boolean (compute=_compute_is_refund)
- `no_followup` Boolean “No Follow-Up” (store, compute=_compute_no_followup)

Public methods: `action_add_from_catalog`, `action_automatic_entry`, `action_open_business_doc`, `action_payment_items_register_payment`, `action_register_payment`, `action_unreconcile_match_entries`, `check_field_access_rights`, `copy_data`, `create`, `default_get`, `flush_model`, `flush_recordset`, `get_column_to_exclude_for_colspan_calculation`, `get_import_templates`, `get_parent_section_line`, `get_section_subtotal`, `get_section_total`, `get_views`, `invalidate_model`, `invalidate_recordset`, `open_reconcile_view`, `read`, `reconcile`, `remove_move_reconcile`, `search_fetch`, `search_read`, `unlink`, `write`

Extension points: `_check_amls_exigibility_for_reconciliation`, `_check_caba_non_caba_shared_tags`, `_check_constrains_account_id_journal_id`, `_check_edi_line_tax_required`, `_check_off_balance`, `_check_payable_receivable`, `_check_reconciliation`, `_check_tax_lock_date`, `_create_analytic_lines`, `_create_exchange_difference_moves`, `_get_aml_vals`, `_get_aml_values`, `_get_analytic_distribution_arguments`, `_get_attachment_by_record`, `_get_attachment_domains`, `_get_child_lines`, `_get_collapsed_lines`, `_get_computed_taxes`, `_get_default_read_fields`, `_get_detailed_lines`, `_get_discount_lines`, `_get_downpayment_lines`, `_get_exchange_account`, `_get_exchange_journal`, `_get_installments_data`, `_get_integrity_hash_fields`, `_get_invoiced_qty_per_product`, `_get_journal_items_full_name`, `_get_lock_date_protected_fields`, `_get_matched_move_ids`, `_get_product_catalog_lines_data`, `_get_reconciliation_aml_field_value`, `_get_section_lines`, `_get_subsection_lines`, `_get_tax_exigible_domain`, `_prepare_analytic_distribution_line`, `_prepare_analytic_lines`, `_prepare_create_values`, `_prepare_edi_vals_to_export`, `_prepare_exchange_difference_move_vals`, `_prepare_move_line_residual_amounts`, `_prepare_reconciliation_amls`, `_prepare_reconciliation_plan`, `_prepare_reconciliation_single_partial`

## `account.move.line` (extends)


Extension points: `_get_extra_query_base_tax_line_mapping`, `_get_query_tax_details`, `_get_query_tax_details_from_domain`

## `account.move.send` (defines)

Account Move Send


Extension points: `_check_invoice_report`, `_check_move_constraints`, `_check_sending_data`, `_get_alerts`, `_get_all_extra_edis`, `_get_default_extra_edis`, `_get_default_invoice_edi_format`, `_get_default_mail_attachments_widget`, `_get_default_mail_body`, `_get_default_mail_lang`, `_get_default_mail_partner_ids`, `_get_default_mail_subject`, `_get_default_mail_template_id`, `_get_default_pdf_report_id`, `_get_default_sending_methods`, `_get_default_sending_settings`, `_get_invoice_extra_attachments`, `_get_invoice_extra_attachments_data`, `_get_mail_default_field_value_from_template`, `_get_mail_layout`, `_get_mail_params`, `_get_mail_template_attachments_data`, `_get_move_constraints`, `_get_placeholder_mail_attachments_data`, `_get_placeholder_mail_template_dynamic_attachments_data`, `_prepare_invoice_pdf_report`, `_prepare_invoice_proforma_pdf_report`

## `account.partial.reconcile` (defines)

Partial Reconcile

- `debit_move_id` Many2one → `account.move.line` (required, index)
- `credit_move_id` Many2one → `account.move.line` (required, index)
- `full_reconcile_id` Many2one → `account.full.reconcile` “Full Reconcile”
- `exchange_move_id` Many2one → `account.move`
- `draft_caba_move_vals` Json “Values that created the draft cash-basis entry”
- `company_currency_id` Many2one → `res.currency` “Company Currency” (related=company_id.currency_id)
- `debit_currency_id` Many2one → `res.currency` “Currency of the debit journal item.” (store, related=debit_move_id.currency_id)
- `credit_currency_id` Many2one → `res.currency` “Currency of the credit journal item.” (store, related=credit_move_id.currency_id)
- `amount` Monetary
- `debit_amount_currency` Monetary
- `credit_amount_currency` Monetary
- `company_id` Many2one → `res.company` “Company” (store, compute=_compute_company_id)
- `max_date` Date “Max Date of Matched Lines” (store, compute=_compute_max_date)

Public methods: `create`, `unlink`

Extension points: `_check_required_computed_currencies`, `_create_tax_cash_basis_moves`, `_get_cash_basis_base_line_grouping_key_from_record`, `_get_cash_basis_base_line_grouping_key_from_vals`, `_get_cash_basis_tax_line_grouping_key_from_record`, `_get_cash_basis_tax_line_grouping_key_from_vals`, `_get_draft_caba_move_vals`, `_get_to_update_payments`, `_prepare_cash_basis_base_line_vals`, `_prepare_cash_basis_counterpart_base_line_vals`, `_prepare_cash_basis_counterpart_tax_line_vals`, `_prepare_cash_basis_tax_line_vals`

## `account.payment` (defines)

Payments

Inherits: `mail.thread.main.attachment`, `mail.activity.mixin`

- `name` Char “Number” (store, compute=_compute_name)
- `date` Date (required)
- `move_id` Many2one → `account.move` “Journal Entry” (index)
- `journal_id` Many2one → `account.journal` (required, store, compute=_compute_journal_id)
- `company_id` Many2one → `res.company` (required, store, compute=_compute_company_id)
- `state` Selection (required, store, compute=_compute_state)
- `is_reconciled` Boolean “Is Reconciled” (store, compute=_compute_reconciliation_status)
- `is_matched` Boolean “Is Matched With a Bank Statement” (store, compute=_compute_reconciliation_status)
- `is_sent` Boolean “Is Sent” (readonly)
- `available_partner_bank_ids` Many2many → `res.partner.bank` (compute=_compute_available_partner_bank_ids)
- `partner_bank_id` Many2one → `res.partner.bank` “Recipient Bank Account” (store, compute=_compute_partner_bank_id)
- `qr_code` Html “QR Code URL” (compute=_compute_qr_code)
- `paired_internal_transfer_payment_id` Many2one → `account.payment`
- `payment_method_line_id` Many2one → `account.payment.method.line` “Payment Method” (store, compute=_compute_payment_method_line_id)
- `available_payment_method_line_ids` Many2many → `account.payment.method.line` (compute=_compute_payment_method_line_fields)
- `payment_method_id` Many2one “Method” (store, related=payment_method_line_id.payment_method_id)
- `available_journal_ids` Many2many → `account.journal` (compute=_compute_available_journal_ids)
- `amount` Monetary
- `payment_type` Selection “Payment Type” (required)
- `partner_type` Selection (required)
- `memo` Char “Memo”
- `payment_reference` Char “Payment Reference”
- `currency_id` Many2one → `res.currency` “Currency” (store, compute=_compute_currency_id)
- `company_currency_id` Many2one “Company Currency” (related=company_id.currency_id)
- `partner_id` Many2one → `res.partner` “Customer/Vendor”
- `outstanding_account_id` Many2one → `account.account` “Outstanding Account” (store, compute=_compute_outstanding_account_id)
- `destination_account_id` Many2one → `account.account` “Destination Account” (store, compute=_compute_destination_account_id)
- `invoice_ids` Many2many → `account.move` “Invoices”
- `reconciled_invoice_ids` Many2many → `account.move` “Reconciled Invoices” (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_invoices_count` Integer “# Reconciled Invoices” (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_invoices_type` Selection (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_bill_ids` Many2many → `account.move` “Reconciled Bills” (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_bills_count` Integer “# Reconciled Bills” (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_statement_line_ids` Many2many → `account.bank.statement.line` “Reconciled Statement Lines” (compute=_compute_stat_buttons_from_reconciliation)
- `reconciled_statement_lines_count` Integer “# Reconciled Statement Lines” (compute=_compute_stat_buttons_from_reconciliation)
- `payment_method_code` Char (related=payment_method_line_id.code)
- `payment_receipt_title` Char (compute=_compute_payment_receipt_title)
- `need_cancel_request` Boolean (related=move_id.need_cancel_request)
- `show_partner_bank_account` Boolean (compute=_compute_show_require_partner_bank)
- `require_partner_bank_account` Boolean (compute=_compute_show_require_partner_bank)
- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `amount_signed` Monetary (compute=_compute_amount_signed)
- `amount_company_currency_signed` Monetary (store, compute=_compute_amount_company_currency_signed)
- `duplicate_payment_ids` Many2many → `account.payment` (compute=_compute_duplicate_payment_ids)
- `attachment_ids` One2many → `ir.attachment` “Attachments”

Public methods: `action_cancel`, `action_draft`, `action_open_business_doc`, `action_post`, `action_reject`, `action_validate`, `button_open_bills`, `button_open_invoices`, `button_open_journal_entry`, `button_open_statement_lines`, `button_request_cancel`, `copy_data`, `create`, `mark_as_sent`, `unlink`, `unmark_as_sent`, `write`

Extension points: `_check_move_id`, `_check_payment_method_line_id`, `_get_aml_default_display_name_list`, `_get_method_codes_needing_bank_account`, `_get_method_codes_using_bank_account`, `_get_outstanding_account`, `_get_payment_method_codes_to_exclude`, `_get_payment_receipt_report_values`, `_get_trigger_fields_to_synchronize`, `_get_valid_liquidity_accounts`, `_get_valid_payment_account_types`, `_prepare_move_counterpart_lines`, `_prepare_move_line_default_vals`, `_prepare_move_lines_per_type`, `_prepare_move_liquidity_lines`, `_prepare_move_withholding_lines`

## `account.move` (extends)

- `payment_ids` One2many → `account.payment` “Payments”

## `account.payment.method` (defines)

Payment Methods

- `name` Char (required)
- `code` Char (required)
- `payment_type` Selection (required)

Public methods: `create`, `unlink`

Extension points: `_get_payment_method_domain`, `_get_payment_method_information`, `_get_sdd_payment_method_code`

## `account.payment.method.line` (defines)

Payment Methods

- `name` Char (store, compute=_compute_name)
- `sequence` Integer
- `payment_method_id` Many2one → `account.payment.method` “Payment Method” (required)
- `payment_account_id` Many2one → `account.account`
- `journal_id` Many2one → `account.journal`
- `default_account_id` Many2one (related=journal_id.default_account_id)
- `code` Char (related=payment_method_id.code)
- `payment_type` Selection (related=payment_method_id.payment_type)
- `company_id` Many2one (related=journal_id.company_id)
- `available_payment_method_ids` Many2many (related=journal_id.available_payment_method_ids)

Public methods: `unlink`

## `account.payment.term` (defines)

Payment Terms

- `name` Char “Payment Terms” (required)
- `active` Boolean
- `note` Html “Description on the Invoice”
- `line_ids` One2many → `account.payment.term.line` “Terms”
- `company_id` Many2one → `res.company` “Company”
- `fiscal_country_codes` Char (compute=_compute_fiscal_country_codes)
- `sequence` Integer (required)
- `currency_id` Many2one → `res.currency` (compute=_compute_currency_id)
- `display_on_invoice` Boolean “Show installment dates”
- `example_amount` Monetary (readonly)
- `example_date` Date “Date example”
- `example_invalid` Boolean (compute=_compute_example_invalid)
- `example_preview` Html (compute=_compute_example_preview)
- `example_preview_discount` Html (compute=_compute_example_preview)
- `discount_percentage` Float “Discount %”
- `discount_days` Integer “Discount Days”
- `early_pay_discount_computation` Selection “Cash Discount Tax Reduction” (store, compute=_compute_discount_computation)
- `early_discount` Boolean “Early Discount”

Public methods: `copy_data`

Extension points: `_check_lines`, `_get_amount_by_date`, `_get_amount_due_after_discount`, `_get_last_discount_date`, `_get_last_discount_date_formatted`

## `account.payment.term.line` (defines)

Payment Terms Line

- `value` Selection (required)
- `value_amount` Float “Due” (store, compute=_compute_value_amount)
- `delay_type` Selection (required)
- `display_days_next_month` Boolean (compute=_compute_display_days_next_month)
- `days_next_month` Char “Days on the next month”
- `nb_days` Integer “Days” (store, compute=_compute_days)
- `payment_id` Many2one → `account.payment.term` “Payment Terms” (required, index)

Extension points: `_check_percent`, `_check_valid_char_value`, `_get_due_date`

## `account.reconcile.model.line` (defines)

Rules for the reconciliation model

Inherits: `analytic.mixin`

- `model_id` Many2one → `account.reconcile.model` (readonly)
- `company_id` Many2one (store, related=model_id.company_id)
- `sequence` Integer (required)
- `account_id` Many2one → `account.account` “Account”
- `partner_id` Many2one → `res.partner` “Partner”
- `label` Char “Label”
- `amount_type` Selection (required)
- `amount` Float “Float Amount” (store, compute=_compute_float_amount)
- `amount_string` Char “Amount” (required)
- `tax_ids` Many2many → `account.tax` “Taxes”

## `account.reconcile.model` (defines)

Preset to create journal entries during a invoices and payments matching

Inherits: `mail.thread`

- `active` Boolean
- `name` Char “Name” (required)
- `sequence` Integer (required)
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `trigger` Selection (required)
- `next_activity_type_id` Many2one → `mail.activity.type` “Next Activity”
- `can_be_proposed` Boolean (store, compute=_compute_can_be_proposed)
- `mapped_partner_id` Many2one → `res.partner` (store, compute=_compute_partner_mapping)
- `match_journal_ids` Many2many → `account.journal` “Journals”
- `match_amount` Selection “Amount”
- `match_amount_min` Float “Amount Min Parameter”
- `match_amount_max` Float “Amount Max Parameter”
- `match_label` Selection “Label”
- `match_label_param` Char “Label Parameter”
- `match_partner_ids` Many2many → `res.partner` “Partners”
- `line_ids` One2many → `account.reconcile.model.line`

Public methods: `action_reconcile_stat`, `action_set_auto_reconcile`, `action_set_manual`, `copy_data`

Extension points: `_check_match_label_param`

## `account.report` (defines)

Accounting Report

- `name` Char “Name” (required)
- `sequence` Integer “Sequence”
- `active` Boolean “Active”
- `line_ids` One2many → `account.report.line` “Lines”
- `column_ids` One2many → `account.report.column` “Columns”
- `root_report_id` Many2one → `account.report` “Root Report”
- `variant_report_ids` One2many → `account.report` “Variants”
- `section_report_ids` Many2many → `account.report` “Sections”
- `section_main_report_ids` Many2many → `account.report` “Section Of”
- `use_sections` Boolean “Composite Report” (store, compute=_compute_use_sections)
- `chart_template` Selection “Chart of Accounts”
- `country_id` Many2one → `res.country` “Country”
- `only_tax_exigible` Boolean “Only Tax Exigible Lines” (store)
- `availability_condition` Selection “Availability” (store, compute=_compute_default_availability_condition)
- `load_more_limit` Integer “Load More Limit”
- `search_bar` Boolean “Search Bar”
- `prefix_groups_threshold` Integer “Prefix Groups Threshold”
- `integer_rounding` Selection “Integer Rounding”
- `allow_foreign_vat` Boolean “Allow Foreign VAT” (store)
- `default_opening_date_filter` Selection “Default Opening” (store)
- `currency_translation` Selection “Currency Translation” (store)
- `filter_multi_company` Selection “Multi-Company” (store)
- `filter_date_range` Boolean “Date Range” (store)
- `filter_show_draft` Boolean “Draft Entries” (store)
- `filter_unreconciled` Boolean “Unreconciled Entries” (store)
- `filter_unfold_all` Boolean “Unfold All” (store)
- `filter_hide_0_lines` Selection “Hide lines at 0” (store)
- `filter_period_comparison` Boolean “Period Comparison” (store)
- `filter_growth_comparison` Boolean “Growth Comparison” (store)
- `filter_journals` Boolean “Journals” (store)
- `filter_analytic` Boolean “Analytic Filter” (store)
- `filter_hierarchy` Selection “Account Groups” (store)
- `filter_account_type` Selection “Account Types” (store)
- `filter_partner` Boolean “Partners” (store)
- `filter_aml_ir_filters` Boolean “Favorite Filters” (store)
- `filter_budgets` Boolean “Budgets” (store)

Public methods: `copy`, `copy_data`, `write`

Extension points: `_get_copied_name`

## `account.report.line` (defines)

Accounting Report Line

- `name` Char “Name” (required)
- `expression_ids` One2many → `account.report.expression` “Expressions”
- `report_id` Many2one → `account.report` “Parent Report” (required, store, index, compute=_compute_report_id)
- `hierarchy_level` Integer “Level” (required, store, compute=_compute_hierarchy_level)
- `parent_id` Many2one → `account.report.line` “Parent Line”
- `children_ids` One2many → `account.report.line` “Child Lines”
- `groupby` Char “Group By”
- `user_groupby` Char “User Group By” (store, compute=_compute_user_groupby)
- `sequence` Integer “Sequence”
- `code` Char “Code”
- `foldable` Boolean “Foldable”
- `print_on_new_page` Boolean “Print On New Page”
- `action_id` Many2one → `ir.actions.actions` “Action”
- `hide_if_zero` Boolean “Hide if Zero”
- `domain_formula` Char “Domain Formula Shortcut”
- `account_codes_formula` Char “Account Codes Formula Shortcut”
- `aggregation_formula` Char “Aggregation Formula Shortcut”
- `external_formula` Char “External Formula Shortcut”
- `horizontal_split_side` Selection “Horizontal Split Side” (store, compute=_compute_horizontal_split_side)
- `tax_tags_formula` Char “Tax Tags Formula Shortcut”

Extension points: `_check_parent_line`, `_create_report_expression`, `_get_copied_code`

## `account.report.expression` (defines)

Accounting Report Expression

- `report_line_id` Many2one → `account.report.line` “Report Line” (required, index)
- `report_line_name` Char “Report Line Name” (related=report_line_id.name)
- `label` Char “Label” (required)
- `engine` Selection “Computation Engine” (required)
- `formula` Char “Formula” (required)
- `subformula` Char “Subformula”
- `date_scope` Selection “Date Scope” (required)
- `figure_type` Selection “Figure Type”
- `green_on_positive` Boolean “Is Growth Good when Positive”
- `blank_if_zero` Boolean “Blank if Zero”
- `auditable` Boolean “Auditable” (store, compute=_compute_auditable)
- `carryover_target` Char “Carry Over To”

Public methods: `create`, `write`

Extension points: `_check_carryover_target`, `_check_formula`, `_create_tax_tags`, `_get_aggregation_terms_details`, `_get_auditable_engines`, `_get_carryover_target_expression`, `_get_matching_tags`, `_get_tags_create_vals`

## `account.report.column` (defines)

Accounting Report Column

- `name` Char “Name” (required)
- `expression_label` Char “Expression Label” (required)
- `sequence` Integer “Sequence”
- `report_id` Many2one → `account.report` “Report”
- `sortable` Boolean “Sortable”
- `figure_type` Selection “Figure Type” (required)
- `blank_if_zero` Boolean “Blank if Zero”
- `custom_audit_action_id` Many2one → `ir.actions.act_window` “Custom Audit Action”

## `account.report.external.value` (defines)

Accounting Report External Value

- `name` Char (required)
- `value` Float “Numeric Value”
- `text_value` Char “Text Value”
- `date` Date (required)
- `target_report_expression_id` Many2one → `account.report.expression` “Target Expression” (required)
- `target_report_line_id` Many2one “Target Line” (related=target_report_expression_id.report_line_id)
- `target_report_expression_label` Char “Target Expression Label” (related=target_report_expression_id.label)
- `report_country_id` Many2one “Country” (related=target_report_line_id.report_id.country_id)
- `company_id` Many2one → `res.company` “Company” (required)
- `carryover_origin_expression_label` Char “Origin Expression Label”
- `carryover_origin_report_line_id` Many2one → `account.report.line` “Origin Line”

## `account.root` (defines)

Account codes first 2 digits

- `name` Char (compute=_compute_root)
- `parent_id` Many2one → `account.root` (compute=_compute_root)

Public methods: `browse`

## `account.tax.group` (defines)

Tax Group

- `name` Char (required)
- `sequence` Integer
- `company_id` Many2one → `res.company` (required)
- `tax_payable_account_id` Many2one → `account.account` “Tax Payable Account”
- `tax_receivable_account_id` Many2one → `account.account` “Tax Receivable Account”
- `advance_tax_payment_account_id` Many2one → `account.account` “Tax Advance Account”
- `country_id` Many2one → `res.country` “Country” (store, compute=_compute_country_id)
- `country_code` Char (related=country_id.code)
- `preceding_subtotal` Char “Preceding Subtotal”
- `pos_receipt_label` Char “PoS receipt label”

## `account.tax` (defines)

Tax

Inherits: `mail.thread`

- `name` Char “Tax Name” (required)
- `type_tax_use` Selection “Tax Type” (required)
- `tax_scope` Selection “Tax Scope”
- `amount_type` Selection “Tax Computation” (required)
- `fiscal_position_ids` Many2many → `account.fiscal.position`
- `original_tax_ids` Many2many → `account.tax` “Replaces”
- `replacing_tax_ids` Many2many → `account.tax` “Replaced by” (readonly)
- `display_alternative_taxes_field` Boolean (compute=_compute_display_alternative_taxes_field)
- `is_domestic` Boolean (store, compute=_compute_is_domestic)
- `active` Boolean
- `company_id` Many2one → `res.company` “Company” (required, readonly)
- `children_tax_ids` Many2many → `account.tax` “Children Taxes”
- `sequence` Integer (required)
- `amount` Float (required)
- `description` Html “Description”
- `invoice_label` Char “Label on Invoices”
- `tax_label` Char (compute=_compute_tax_label)
- `price_include` Boolean (compute=_compute_price_include)
- `company_price_include` Selection (related=company_id.account_price_include)
- `price_include_override` Selection “Included in Price”
- `include_base_amount` Boolean “Affect Base of Subsequent Taxes”
- `is_base_affected` Boolean “Base Affected by Previous Taxes”
- `analytic` Boolean “Include in Analytic Cost”
- `tax_group_id` Many2one → `account.tax.group` “Tax Group” (required, store, compute=_compute_tax_group_id)
- `hide_tax_exigibility` Boolean “Hide Use Cash Basis Option” (readonly, related=company_id.tax_exigibility)
- `tax_exigibility` Selection “Tax Exigibility”
- `cash_basis_transition_account_id` Many2one → `account.account` “Cash Basis Transition Account”
- `invoice_repartition_line_ids` One2many → `account.tax.repartition.line` “Distribution for Invoices” (store, compute=_compute_invoice_repartition_line_ids)
- `refund_repartition_line_ids` One2many → `account.tax.repartition.line` “Distribution for Refund Invoices” (store, compute=_compute_refund_repartition_line_ids)
- `repartition_line_ids` One2many → `account.tax.repartition.line` “Distribution”
- `country_id` Many2one → `res.country` “Country” (required, store, compute=_compute_country_id)
- `country_code` Char (readonly, related=country_id.code)
- `company_country_code` Char “Fiscal Country Code of the Company” (related=company_id.account_fiscal_country_id.code)
- `is_used` Boolean “Tax used” (compute=_compute_is_used)
- `repartition_lines_str` Char “Repartition Lines” (compute=_compute_repartition_lines_str)
- `invoice_legal_notes` Html “Legal Notes”
- `has_negative_factor` Boolean (compute=_compute_has_negative_factor)
- `account_move_line_ids` Many2many → `account.move.line` (readonly)
- `account_reconcile_model_line_ids` Many2many → `account.reconcile.model.line` (readonly)

Public methods: `compute_all`, `copy_data`, `create`, `flatten_taxes_hierarchy`, `get_tax_tags`, `name_search`, `onchange_amount`, `onchange_amount_type`, `onchange_price_include`, `unlink_except_tax_used`, `validate_tax_group_id`, `write`

Extension points: `_check_children_scope`, `_check_company_consistency`, `_check_repartition_lines`, `_get_base_line_field_value_from_record`, `_get_delta_amount_to_reach_target`, `_get_description_plaintext`, `_get_discount_amount_without_tax`, `_get_gross_total_without_tax`, `_get_price_unit_without_tax`, `_get_tax_details`, `_get_tax_totals_summary`, `_prepare_base_line_for_taxes_computation`, `_prepare_base_line_grouping_key`, `_prepare_base_line_tax_repartition_grouping_key`, `_prepare_base_lines_for_down_payment`, `_prepare_discountable_base_lines`, `_prepare_down_payment_lines`, `_prepare_global_discount_lines`, `_prepare_tax_line_for_taxes_computation`, `_prepare_tax_line_repartition_grouping_key`, `_prepare_tax_lines`

## `account.tax.repartition.line` (defines)

Tax Repartition Line

- `factor_percent` Float “%” (required)
- `factor` Float “Factor Ratio” (compute=_compute_factor)
- `repartition_type` Selection “Based On” (required)
- `document_type` Selection “Related to” (required)
- `account_id` Many2one → `account.account` “Account”
- `tag_ids` Many2many → `account.account.tag` “Tax Grids”
- `tax_id` Many2one → `account.tax`
- `company_id` Many2one → `res.company` “Company” (store, related=tax_id.company_id)
- `sequence` Integer “Sequence”
- `use_in_tax_closing` Boolean “Tax Closing Entry” (store, compute=_compute_use_in_tax_closing)
- `tag_ids_domain` Binary “tag domain” (compute=_compute_tag_ids_domain)

Extension points: `_get_aml_target_tax_account`

## `account.chart.template` (defines)

Account Chart Template


Public methods: `company_xmlid`, `ref`, `try_loading`

Extension points: `_create_outstanding_accounts`, `_get_account_account`, `_get_account_fiscal_position`, `_get_account_group`, `_get_account_journal`, `_get_account_reconcile_model`, `_get_account_tax`, `_get_account_tax_group`, `_get_accounts_data_values`, `_get_bank_fees_reco_account`, `_get_chart_template_data`, `_get_chart_template_mapping`, `_get_chart_template_model_data`, `_get_field_translation`, `_get_parent_template`, `_get_property_accounts`, `_get_tag_mapper`, `_get_translatable_template_model_fields`, `_get_untranslatable_fields_target_language`, `_get_untranslatable_fields_to_translate`, `_get_untranslated_translatable_template_model_records`, `_post_load_data`, `_post_model_setup__`

## `res.company` (extends)

Inherits: `mail.thread`

- `fiscalyear_last_day` Integer (required)
- `fiscalyear_last_month` Selection (required)
- `fiscalyear_lock_date` Date “Global Lock Date”
- `tax_lock_date` Date “Tax Return Lock Date”
- `sale_lock_date` Date “Sales Lock Date”
- `purchase_lock_date` Date “Purchase Lock date”
- `hard_lock_date` Date “Hard Lock Date”
- `user_fiscalyear_lock_date` Date (compute=_compute_user_fiscalyear_lock_date)
- `user_tax_lock_date` Date (compute=_compute_user_tax_lock_date)
- `user_sale_lock_date` Date (compute=_compute_user_sale_lock_date)
- `user_purchase_lock_date` Date (compute=_compute_user_purchase_lock_date)
- `user_hard_lock_date` Date (compute=_compute_user_hard_lock_date)
- `transfer_account_id` Many2one → `account.account` “Inter-Banks Transfer Account”
- `expects_chart_of_accounts` Boolean “Expects a Chart of Accounts”
- `chart_template` Selection
- `bank_account_code_prefix` Char “Prefix of the bank accounts”
- `cash_account_code_prefix` Char “Prefix of the cash accounts”
- `default_cash_difference_income_account_id` Many2one → `account.account` “Cash Difference Income”
- `default_cash_difference_expense_account_id` Many2one → `account.account` “Cash Difference Expense”
- `account_journal_suspense_account_id` Many2one → `account.account` “Journal Suspense Account”
- `account_journal_early_pay_discount_gain_account_id` Many2one → `account.account` “Cash Discount Write-Off Gain Account”
- `account_journal_early_pay_discount_loss_account_id` Many2one → `account.account` “Cash Discount Write-Off Loss Account”
- `transfer_account_code_prefix` Char “Prefix of the transfer accounts”
- `account_sale_tax_id` Many2one → `account.tax` “Default Sale Tax”
- `account_purchase_tax_id` Many2one → `account.tax` “Default Purchase Tax”
- `account_purchase_receipt_fiscal_position_id` Many2one → `account.fiscal.position` “Default Purchase Receipt Fiscal Position”
- `tax_calculation_rounding_method` Selection “Tax Calculation Rounding Method”
- `currency_exchange_journal_id` Many2one → `account.journal` “Exchange Gain or Loss Journal”
- `income_currency_exchange_account_id` Many2one → `account.account` “Gain Exchange Rate Account”
- `expense_currency_exchange_account_id` Many2one → `account.account` “Loss Exchange Rate Account”
- `anglo_saxon_accounting` Boolean “Use anglo-saxon accounting”
- `bank_journal_ids` One2many → `account.journal` “Bank Journals”
- `incoterm_id` Many2one → `account.incoterms` “Default incoterm”
- `qr_code` Boolean “Display QR-code on invoices”
- `link_qr_code` Boolean “Display Link QR-code”
- `display_invoice_amount_total_words` Boolean “Total amount of invoice in letters”
- `display_invoice_tax_company_currency` Boolean “Taxes in company currency”
- `account_use_credit_limit` Boolean “Sales Credit Limit”
- `batch_payment_sequence_id` Many2one → `ir.sequence` (readonly)
- `account_opening_move_id` Many2one → `account.move` “Opening Journal Entry”
- `account_opening_journal_id` Many2one → `account.journal` “Opening Journal” (related=account_opening_move_id.journal_id)
- `account_opening_date` Date “Opening Entry”
- `invoice_terms` Html “Default Terms and Conditions”
- `terms_type` Selection “Terms & Conditions format”
- `invoice_terms_html` Html “Default Terms and Conditions as a Web page” (store, compute=_compute_invoice_terms_html)
- `account_default_pos_receivable_account_id` Many2one → `account.account` “Default PoS Receivable Account”
- `expense_accrual_account_id` Many2one → `account.account`
- `revenue_accrual_account_id` Many2one → `account.account`
- `automatic_entry_default_journal_id` Many2one → `account.journal`
- `domestic_fiscal_position_id` Many2one → `account.fiscal.position` (store, compute=_compute_domestic_fiscal_position_id)
- `account_fiscal_country_id` Many2one → `res.country` “Fiscal Country” (store, compute=compute_account_tax_fiscal_country)
- `account_fiscal_country_group_codes` Json (compute=_compute_account_fiscal_country_group_codes)
- `account_enabled_tax_country_ids` Many2many → `res.country` “l10n-used countries” (compute=_compute_account_enabled_tax_country_ids)
- `tax_exigibility` Boolean “Use Cash Basis”
- `tax_cash_basis_journal_id` Many2one → `account.journal` “Cash Basis Journal”
- `account_cash_basis_base_account_id` Many2one → `account.account` “Base Tax Received Account”
- `account_storno` Boolean “Storno accounting” (store, compute=_compute_account_storno)
- `display_account_storno` Boolean (compute=_compute_display_account_storno)
- `fiscal_position_ids` One2many → `account.fiscal.position`
- `multi_vat_foreign_country_ids` Many2many → `res.country` “Foreign VAT countries” (compute=_compute_multi_vat_foreign_country)
- `quick_edit_mode` Selection “Quick encoding”
- `account_discount_income_allocation_id` Many2one → `account.account` “Separate account for income discount”
- `account_discount_expense_allocation_id` Many2one → `account.account` “Separate account for expense discount”
- `restrictive_audit_trail` Boolean “Restrictive Audit Trail”
- `force_restrictive_audit_trail` Boolean “Force Audit Trail” (compute=_compute_force_restrictive_audit_trail)
- `autopost_bills` Boolean “Auto-validate bills”
- `account_price_include` Selection “Default Sales Price Include” (required)
- `company_vat_placeholder` Char (compute=_compute_company_vat_placeholder)
- `company_registry_placeholder` Char (compute=_compute_company_registry_placeholder)
- `income_account_id` Many2one → `account.account` “Income Account”
- `expense_account_id` Many2one → `account.account` “Expense Account”
- `price_difference_account_id` Many2one → `account.account` “Price Difference Account”

Public methods: `action_save_onboarding_company_data`, `action_save_onboarding_sale_tax`, `compute_account_tax_fiscal_country`, `compute_fiscalyear_dates`, `create`, `get_chart_of_accounts_or_fail`, `get_new_account_code`, `get_next_batch_payment_communication`, `get_unaffected_earnings_account`, `install_l10n_modules`, `opening_move_posted`, `reflect_code_prefix_change`, `setting_init_bank_account_action`, `setting_init_credit_card_account_action`, `write`

Extension points: `_action_check_hash_integrity`, `_check_audit_trail_restriction`, `_check_fiscalyear_last_day`, `_check_hash_integrity`, `_check_set_account_price_include`, `_check_tax_return_configuration`, `_create_batch_payment_sequence`, `_get_batch_payment_sequence_values`, `_get_company_root_delegated_field_names`, `_get_default_opening_move_values`, `_get_lock_date_violations`, `_get_unreconciled_statement_lines_domain`, `_get_unreconciled_statement_lines_redirect_action`, `_get_user_fiscal_lock_date`, `_get_user_lock_date`, `_get_violated_lock_dates`, `_get_violated_soft_lock_date`

## `decimal.precision` (extends)


Public methods: `precision_get`

## `digest.digest` (extends)

- `kpi_account_total_revenue` Boolean “Revenue”
- `kpi_account_total_revenue_value` Monetary (compute=_compute_kpi_account_total_revenue_value)

## `ir.actions.report` (extends)

- `is_invoice_report` Boolean “Invoice report”

Extension points: `_get_rendering_context`, `_get_splitted_report`

## `ir.attachment` (extends)


Public methods: `unlink`, `write`

Extension points: `_post_add_create`

## `ir.http` (extends)


Public methods: `lazy_session_info`

## `ir.module.module` (extends)

- `account_templates` Binary (compute=_compute_account_templates)

Public methods: `module_uninstall`, `write`

## `kpi.provider` (extends)


Public methods: `get_account_kpi_summary`, `get_kpi_summary`

## `mail.message` (extends)

- `account_audit_log_preview` Text “Description” (compute=_compute_account_audit_log_preview)
- `account_audit_log_move_id` Many2one → `account.move` “Journal Entry” (compute=_compute_account_audit_log_move_id)
- `account_audit_log_partner_id` Many2one → `res.partner` “Partner” (compute=_compute_account_audit_log_partner_id)
- `account_audit_log_account_id` Many2one → `account.account` “Account” (compute=_compute_account_audit_log_account_id)
- `account_audit_log_tax_id` Many2one → `account.tax` “Tax” (compute=_compute_account_audit_log_tax_id)
- `account_audit_log_company_id` Many2one → `res.company` “Company ” (compute=_compute_account_audit_log_company_id)
- `account_audit_log_restricted` Boolean “Protected by restricted Audit Logs” (compute=_compute_account_audit_log_restricted)

Public methods: `write`

## `mail.template` (extends)


## `mail.tracking.value` (extends)


Public methods: `write`

## `base.partner.merge.automatic.wizard` (extends)


## `onboarding.onboarding` (extends)


Public methods: `action_close_panel_account_dashboard`, `action_close_panel_account_invoice`

Extension points: `_prepare_rendering_values`

## `onboarding.onboarding.step` (extends)


Public methods: `action_open_step_bank_account`, `action_open_step_base_document_layout`, `action_open_step_chart_of_accounts`, `action_open_step_company_data`, `action_open_step_create_invoice`, `action_open_step_fiscal_year`, `action_open_step_sales_tax`, `action_validate_step_base_document_layout`

## `account.fiscal.position` (defines)

Fiscal Position

- `sequence` Integer
- `name` Char “Fiscal Position” (required)
- `active` Boolean
- `company_id` Many2one → `res.company` “Company” (required, readonly, index)
- `account_ids` One2many → `account.fiscal.position.account` “Account Mapping”
- `account_map` Binary (compute=_compute_account_map)
- `tax_ids` Many2many → `account.tax` “Taxes”
- `tax_map` Binary (compute=_compute_tax_map)
- `note` Html “Notes”
- `auto_apply` Boolean “Detect Automatically”
- `vat_required` Boolean “VAT required”
- `company_country_id` Many2one “Company Country” (related=company_id.account_fiscal_country_id)
- `fiscal_country_codes` Char “Company Fiscal Country Code” (related=company_country_id.code)
- `country_id` Many2one → `res.country` “Country”
- `is_domestic` Boolean (store, compute=_compute_is_domestic)
- `country_group_id` Many2one → `res.country.group` “Country Group”
- `state_ids` Many2many → `res.country.state` “Federal States”
- `zip_from` Char “Zip Range From”
- `zip_to` Char “Zip Range To”
- `states_count` Integer (compute=_compute_states_count)
- `foreign_vat` Char “Foreign Tax ID”
- `foreign_vat_header_mode` Selection (compute=_compute_foreign_vat_header_mode)

Public methods: `action_create_foreign_taxes`, `action_open_related_taxes`, `create`, `map_account`, `map_tax`, `write`

Extension points: `_check_zip`, `_get_first_matching_fpos`, `_get_fiscal_position`, `_get_fpos_validation_functions`

## `account.fiscal.position.account` (defines)

Accounts Mapping of Fiscal Position

- `position_id` Many2one → `account.fiscal.position` “Fiscal Position” (required)
- `company_id` Many2one → `res.company` “Company” (store, related=position_id.company_id)
- `account_src_id` Many2one → `account.account` “Account on Product” (required)
- `account_dest_id` Many2one → `account.account` “Account to Use Instead” (required)

## `res.partner` (extends)

- `fiscal_country_codes` Char (compute=_compute_fiscal_country_codes)
- `fiscal_country_group_codes` Json (compute=_compute_fiscal_country_group_codes)
- `partner_vat_placeholder` Char (compute=_compute_partner_vat_placeholder)
- `partner_company_registry_placeholder` Char (compute=_compute_partner_company_registry_placeholder)
- `duplicate_bank_partner_ids` Many2many (related=bank_ids.duplicate_bank_partner_ids)
- `name` Char
- `credit` Monetary “Total Receivable” (compute=_credit_debit_get)
- `credit_to_invoice` Monetary (compute=_compute_credit_to_invoice)
- `credit_limit` Float “Credit Limit” (company_dependent)
- `use_partner_credit_limit` Boolean “Partner Limit” (compute=_compute_use_partner_credit_limit)
- `show_credit_limit` Boolean (compute=_compute_show_credit_limit)
- `days_sales_outstanding` Float “Days Sales Outstanding (DSO)” (compute=_compute_days_sales_outstanding)
- `debit` Monetary “Total Payable” (compute=_credit_debit_get)
- `total_invoiced` Monetary “Total Invoiced” (compute=_invoice_total)
- `currency_id` Many2one → `res.currency` “Currency” (readonly, compute=_get_company_currency)
- `property_account_payable_id` Many2one → `account.account` “Account Payable” (company_dependent)
- `property_account_receivable_id` Many2one → `account.account` “Account Receivable” (company_dependent)
- `property_account_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (company_dependent)
- `property_payment_term_id` Many2one → `account.payment.term` “Customer Payment Terms” (company_dependent)
- `property_supplier_payment_term_id` Many2one → `account.payment.term` “Vendor Payment Terms” (company_dependent)
- `ref_company_ids` One2many → `res.company` “Companies that refers to partner”
- `supplier_invoice_count` Integer “# Vendor Bills” (compute=_compute_supplier_invoice_count)
- `account_move_count` Integer (compute=_compute_account_move_count)
- `invoice_ids` One2many → `account.move` “Invoices” (readonly)
- `contract_ids` One2many → `account.analytic.account` “Partner Contracts” (readonly)
- `bank_account_count` Integer “Bank” (compute=_compute_bank_count)
- `trust` Selection “Degree of trust you have in this debtor” (company_dependent)
- `ignore_abnormal_invoice_date` Boolean (company_dependent)
- `ignore_abnormal_invoice_amount` Boolean (company_dependent)
- `invoice_sending_method` Selection “Invoice sending” (company_dependent)
- `invoice_edi_format` Selection “eInvoice format” (compute=_compute_invoice_edi_format)
- `invoice_edi_format_store` Char (company_dependent)
- `display_invoice_edi_format` Boolean
- `invoice_template_pdf_report_id` Many2one → `ir.actions.report` “Invoice report” (store)
- `available_invoice_template_pdf_report_ids` One2many → `ir.actions.report` (compute=_compute_available_invoice_template_pdf_report_ids)
- `display_invoice_template_pdf_report_id` Boolean
- `supplier_rank` Integer
- `customer_rank` Integer
- `autopost_bills` Selection “Auto-post bills” (required)
- `property_outbound_payment_method_line_id` Many2one → `account.payment.method.line` (company_dependent)
- `property_inbound_payment_method_line_id` Many2one → `account.payment.method.line` (company_dependent)

Public methods: `action_open_business_doc`, `action_view_partner_invoices`, `can_edit_vat`, `create`, `get_partner_localisation_fields_required_to_invoice`, `write`

Extension points: `_check_vat`, `_get_account_statistics_count`, `_get_company_currency`, `_get_country_specific_vat_variants`, `_get_frontend_writable_fields`, `_get_suggested_invoice_edi_format`, `_get_vat_required_valid`

## `product.category` (extends)

- `property_account_income_categ_id` Many2one → `account.account` “Income Account” (company_dependent)
- `property_account_expense_categ_id` Many2one → `account.account` “Expense Account” (company_dependent)

## `product.template` (extends)

- `taxes_id` Many2many → `account.tax` “Sales Taxes”
- `tax_string` Char (compute=_compute_tax_string)
- `supplier_taxes_id` Many2many → `account.tax` “Purchase Taxes”
- `property_account_income_id` Many2one → `account.account` “Income Account” (company_dependent)
- `property_account_expense_id` Many2one → `account.account` “Expense Account” (company_dependent)
- `account_tag_ids` Many2many → `account.account.tag` “Account Tags”
- `fiscal_country_codes` Char (compute=_compute_fiscal_country_codes)

Public methods: `create`, `get_product_accounts`

Extension points: `_check_uom_not_in_invoice`, `_get_category_account`, `_get_list_price`, `_get_price_diff_account`, `_get_product_accounts`

## `product.product` (extends)

- `tax_string` Char (compute=_compute_tax_string)

Extension points: `_get_price_diff_account`, `_get_product_accounts`, `_get_product_domain_search_order`, `_get_retrieval_product_search_plan`, `_get_tax_included_unit_price`, `_get_tax_included_unit_price_from_price`

## `product.catalog.mixin` (extends)


Extension points: `_create_section`, `_get_default_create_section_values`, `_get_new_line_sequence`, `_get_parent_field_on_child_model`, `_get_sections`

## `res.config.settings` (extends)

- `has_accounting_entries` Boolean (compute=_compute_has_chart_of_accounts)
- `currency_id` Many2one → `res.currency` “Currency” (required, related=company_id.currency_id)
- `currency_exchange_journal_id` Many2one → `account.journal` “Currency Exchange Journal” (related=company_id.currency_exchange_journal_id)
- `income_currency_exchange_account_id` Many2one → `account.account` “Gain Exchange Rate Account” (related=company_id.income_currency_exchange_account_id)
- `expense_currency_exchange_account_id` Many2one → `account.account` “Loss Exchange Rate Account” (related=company_id.expense_currency_exchange_account_id)
- `has_chart_of_accounts` Boolean “Company has a chart of accounts” (compute=_compute_has_chart_of_accounts)
- `chart_template` Selection
- `sale_tax_id` Many2one → `account.tax` “Default Sale Tax” (related=company_id.account_sale_tax_id)
- `purchase_tax_id` Many2one → `account.tax` “Default Purchase Tax” (related=company_id.account_purchase_tax_id)
- `account_price_include` Selection “Default Sales Price Include” (required, related=company_id.account_price_include)
- `tax_calculation_rounding_method` Selection “Tax calculation rounding method” (related=company_id.tax_calculation_rounding_method)
- `account_journal_suspense_account_id` Many2one → `account.account` “Bank Suspense” (related=company_id.account_journal_suspense_account_id)
- `transfer_account_id` Many2one → `account.account` “Internal Transfer” (related=company_id.transfer_account_id)
- `module_account_accountant` Boolean “Accounting”
- `group_cash_rounding` Boolean “Cash Rounding”
- `show_sale_receipts` Boolean “Sale Receipt”
- `module_account_budget` Boolean “Budget Management”
- `module_account_payment` Boolean “Invoice Online Payment”
- `module_account_reports` Boolean “Dynamic Reports”
- `module_account_check_printing` Boolean “Allow check printing and deposits”
- `module_account_batch_payment` Boolean “Use batch payments”
- `module_account_iso20022` Boolean “SEPA Credit Transfer / ISO20022”
- `module_account_sepa_direct_debit` Boolean “Use SEPA Direct Debit”
- `module_account_bank_statement_import_qif` Boolean “Import .qif files”
- `module_currency_rate_live` Boolean “Automatic Currency Rates”
- `module_account_intrastat` Boolean “Intrastat”
- `module_product_margin` Boolean “Allow Product Margin”
- `module_account_extract` Boolean “Document Digitization”
- `module_account_invoice_extract` Boolean “Invoice Digitization” (store, compute=_compute_module_account_invoice_extract)
- `module_account_bank_statement_extract` Boolean “Bank Statement Digitization” (store, compute=_compute_module_account_bank_statement_extract)
- `module_snailmail_account` Boolean “Snailmail”
- `module_account_peppol` Boolean “PEPPOL Invoicing”
- `tax_exigibility` Boolean “Cash Basis” (related=company_id.tax_exigibility)
- `tax_cash_basis_journal_id` Many2one → `account.journal` “Tax Cash Basis Journal” (related=company_id.tax_cash_basis_journal_id)
- `account_cash_basis_base_account_id` Many2one → `account.account` “Base Tax Received Account” (related=company_id.account_cash_basis_base_account_id)
- `account_fiscal_country_id` Many2one “Fiscal Country Code” (related=company_id.account_fiscal_country_id)
- `qr_code` Boolean “Display SEPA QR-code” (related=company_id.qr_code)
- `link_qr_code` Boolean “Display Link QR-code” (related=company_id.link_qr_code)
- `incoterm_id` Many2one → `account.incoterms` “Default incoterm” (related=company_id.incoterm_id)
- `invoice_terms` Html “Terms & Conditions” (related=company_id.invoice_terms)
- `invoice_terms_html` Html “Terms & Conditions as a Web page” (related=company_id.invoice_terms_html)
- `terms_type` Selection (related=company_id.terms_type)
- `display_invoice_amount_total_words` Boolean “Total amount of invoice in letters” (related=company_id.display_invoice_amount_total_words)
- `display_invoice_tax_company_currency` Boolean “Taxes in company currency” (related=company_id.display_invoice_tax_company_currency)
- `preview_ready` Boolean “Display preview button” (compute=_compute_terms_preview)
- `use_invoice_terms` Boolean “Default Terms & Conditions”
- `account_use_credit_limit` Boolean “Sales Credit Limit” (related=company_id.account_use_credit_limit)
- `account_default_credit_limit` Monetary “Default Credit Limit” (compute=_compute_account_default_credit_limit)
- `country_code` Char (readonly, related=company_id.account_fiscal_country_id.code)
- `account_storno` Boolean “Storno accounting” (related=company_id.account_storno)
- `display_account_storno` Boolean (related=company_id.display_account_storno)
- `group_sale_delivery_address` Boolean “Customer Addresses”
- `quick_edit_mode` Selection “Quick encoding” (related=company_id.quick_edit_mode)
- `account_journal_early_pay_discount_loss_account_id` Many2one → `account.account` “Early Discount Loss” (related=company_id.account_journal_early_pay_discount_loss_account_id)
- `account_journal_early_pay_discount_gain_account_id` Many2one → `account.account` “Early Discount Gain” (related=company_id.account_journal_early_pay_discount_gain_account_id)
- `account_discount_income_allocation_id` Many2one → `account.account` “Vendor Bills Discounts Account” (related=company_id.account_discount_income_allocation_id)
- `account_discount_expense_allocation_id` Many2one → `account.account` “Customer Invoices Discounts Account” (related=company_id.account_discount_expense_allocation_id)
- `is_account_peppol_eligible` Boolean “PEPPOL eligible” (compute=_compute_is_account_peppol_eligible)
- `restrictive_audit_trail` Boolean “Restricted Audit Trail” (related=company_id.restrictive_audit_trail)
- `force_restrictive_audit_trail` Boolean “Forced Audit Trail” (related=company_id.force_restrictive_audit_trail)
- `autopost_bills` Boolean (related=company_id.autopost_bills)
- `income_account_id` Many2one (related=company_id.income_account_id)
- `expense_account_id` Many2one (related=company_id.expense_account_id)

Public methods: `action_eu_oss_tax_mapping`, `action_update_terms`, `onchange_analytic_accounting`, `onchange_module_account_budget`, `reload_template`, `set_values`

## `res.country.group` (extends)

- `exclude_state_ids` Many2many → `res.country.state` “Fiscal Exceptions”

## `res.currency` (extends)

- `display_rounding_warning` Boolean “Display Rounding Warning” (compute=_compute_display_rounding_warning)
- `fiscal_country_codes` Char

Public methods: `write`

Extension points: `_check_currency_table_monocurrency`, `_create_currency_table`, `_get_fiscal_country_codes`, `_get_monocurrency_currency_table_sql`, `_get_simple_currency_table`, `_get_table_builder_average`, `_get_table_builder_current`, `_get_table_builder_domestic_currency`, `_get_table_builder_historical`

## `res.partner.bank` (extends)

Inherits: `mail.thread`, `mail.activity.mixin`

- `journal_id` One2many → `account.journal` “Account Journal” (readonly)
- `has_iban_warning` Boolean (store, compute=_compute_display_account_warning)
- `partner_country_name` Char (related=partner_id.country_id.name)
- `has_money_transfer_warning` Boolean (store, compute=_compute_display_account_warning)
- `money_transfer_service` Char (compute=_compute_money_transfer_service_name)
- `partner_supplier_rank` Integer (related=partner_id.supplier_rank)
- `partner_customer_rank` Integer (related=partner_id.customer_rank)
- `related_moves` One2many → `account.move`
- `bank_id` Many2one
- `active` Boolean
- `acc_number` Char
- `acc_holder_name` Char
- `clearing_number` Char
- `partner_id` Many2one
- `user_has_group_validate_bank_account` Boolean (compute=_compute_user_has_group_validate_bank_account)
- `allow_out_payment` Boolean
- `currency_id` Many2one
- `lock_trust_fields` Boolean (compute=_compute_lock_trust_fields)
- `duplicate_bank_partner_ids` Many2many → `res.partner` (compute=_compute_duplicate_bank_partner_ids)

Public methods: `action_open_business_doc`, `build_qr_code_base64`, `build_qr_code_url`, `create`, `default_get`, `get_available_qr_methods_in_sequence`, `unlink`, `write`

Extension points: `_check_allow_out_payment`, `_check_for_qr_code_errors`, `_check_journal_id`, `_get_available_qr_methods`, `_get_error_messages_for_qr`, `_get_money_transfer_services`, `_get_qr_code_base64`, `_get_qr_code_generation_params`, `_get_qr_code_url`, `_get_qr_vals`

## `res.groups` (extends)


Public methods: `get_application_groups`

## `sequence.mixin` (defines)

Automatic sequence

- `sequence_prefix` Char (store, compute=_compute_split_sequence)
- `sequence_number` Integer (store, compute=_compute_split_sequence)

Public methods: `init`, `write`

Extension points: `_get_last_sequence`, `_get_last_sequence_domain`, `_get_next_sequence_format`, `_get_sequence_cache`, `_get_sequence_date_range`, `_get_sequence_format_param`, `_get_starting_sequence`

## `account.chart.template` (extends)


Extension points: `_get_generic_coa_account_account`, `_get_generic_coa_res_company`, `_get_generic_coa_template_data`

## `uom.uom` (extends)

- `fiscal_country_codes` Char (compute=_compute_fiscal_country_codes)

Extension points: `_get_unece_code`, `_get_uom_from_unece_code`

## `report.account.report_hash_integrity` (defines)

Get hash integrity result as PDF.


Extension points: `_get_report_values`

## `account.invoice.report` (defines)

Invoices Statistics

- `move_id` Many2one → `account.move` (readonly)
- `journal_id` Many2one → `account.journal` “Journal” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)
- `company_currency_id` Many2one → `res.currency` “Company Currency” (readonly)
- `partner_id` Many2one → `res.partner` “Partner” (readonly)
- `commercial_partner_id` Many2one → `res.partner` “Main Partner”
- `country_id` Many2one → `res.country` “Country”
- `invoice_user_id` Many2one → `res.users` “Salesperson” (readonly)
- `move_type` Selection (readonly)
- `state` Selection “Invoice Status” (readonly)
- `payment_state` Selection “Payment Status” (readonly)
- `fiscal_position_id` Many2one → `account.fiscal.position` “Fiscal Position” (readonly)
- `invoice_date` Date “Invoice Date” (readonly)
- `quantity` Float “Product Quantity” (readonly)
- `product_id` Many2one → `product.product` “Product” (readonly)
- `product_uom_id` Many2one → `uom.uom` “Unit” (readonly)
- `product_categ_id` Many2one → `product.category` “Product Category” (readonly)
- `invoice_date_due` Date “Due Date” (readonly)
- `account_id` Many2one → `account.account` “Revenue/Expense Account” (readonly)
- `price_subtotal_currency` Float “Untaxed Amount in Currency” (readonly)
- `price_subtotal` Float “Untaxed Amount” (readonly)
- `price_total` Float “Total” (readonly)
- `price_total_currency` Float “Total in Currency” (readonly)
- `price_average` Float “Average Price” (readonly)
- `price_margin` Float “Margin” (readonly)
- `inventory_value` Float “Inventory Value” (readonly)
- `currency_id` Many2one → `res.currency` “Currency” (readonly)

## `report.account.report_invoice` (defines)

Account report without payment lines


Extension points: `_get_report_values`

## `report.account.report_invoice_with_payments` (defines)

Account report with payment lines

Inherits: `report.account.report_invoice`


Extension points: `_get_report_values`

## `account.automatic.entry.wizard` (defines)

Create Automatic Entries

- `action` Selection (required)
- `move_data` Text (compute=_compute_move_data)
- `preview_move_data` Text (compute=_compute_preview_move_data)
- `move_line_ids` Many2many → `account.move.line`
- `date` Date (required)
- `company_id` Many2one → `res.company` (required, readonly)
- `company_currency_id` Many2one → `res.currency` (related=company_id.currency_id)
- `percentage` Float “Percentage” (store, compute=_compute_percentage)
- `total_amount` Monetary (store, compute=_compute_total_amount)
- `journal_id` Many2one → `account.journal` “Journal” (required, compute=_compute_journal_id)
- `account_type` Selection (store, compute=_compute_account_type)
- `expense_accrual_account` Many2one → `account.account` (compute=_compute_expense_accrual_account)
- `revenue_accrual_account` Many2one → `account.account` (compute=_compute_revenue_accrual_account)
- `lock_date_message` Char “Lock Date Message” (compute=_compute_lock_date_message)
- `destination_account_id` Many2one → `account.account` “To”
- `display_currency_helper` Boolean “Currency Conversion Helper” (compute=_compute_display_currency_helper)

Public methods: `default_get`, `do_action`

Extension points: `_check_date`, `_get_cut_off_label_format`, `_get_lock_safe_date`, `_get_move_dict_vals_change_account`, `_get_move_dict_vals_change_period`, `_get_move_line_dict_vals_change_period`

## `account.autopost.bills.wizard` (defines)

Autopost Bills Wizard

- `partner_id` Many2one → `res.partner`
- `partner_name` Char (related=partner_id.name)
- `nb_unmodified_bills` Integer “Number of bills previously unmodified from this partner”

Public methods: `action_ask_later`, `action_automate_partner`, `action_never_automate_partner`

## `account.merge.wizard` (defines)

Account merge wizard

- `account_ids` Many2many → `account.account`
- `is_group_by_name` Boolean “Group by name?”
- `wizard_line_ids` One2many → `account.merge.wizard.line` (store, compute=_compute_wizard_line_ids)
- `disable_merge_button` Boolean (compute=_compute_disable_merge_button)

Public methods: `action_merge`, `default_get`

Extension points: `_action_merge`, `_check_access_rights`, `_get_grouping_key`, `_get_window_action`

## `account.merge.wizard.line` (defines)

Account merge wizard line

- `wizard_id` Many2one → `account.merge.wizard` (required)
- `grouping_key` Char
- `sequence` Integer
- `display_type` Selection (required)
- `is_selected` Boolean
- `account_id` Many2one → `account.account` “Account” (readonly)
- `company_ids` Many2many “Companies” (related=account_id.company_ids)
- `info` Char “Info” (compute=_compute_info)
- `account_has_hashed_entries` Boolean (compute=_compute_account_has_hashed_entries)

Extension points: `_get_group_name`

## `account.move.reversal` (defines)

Account Move Reversal

- `move_ids` Many2many → `account.move`
- `new_move_ids` Many2many → `account.move`
- `date` Date “Reversal date”
- `reason` Char “Reason displayed on Credit Note”
- `journal_id` Many2one → `account.journal` “Journal” (required, store, compute=_compute_journal_id)
- `company_id` Many2one → `res.company` (required, readonly)
- `available_journal_ids` Many2many → `account.journal` (compute=_compute_available_journal_ids)
- `country_code` Char (related=company_id.country_id.code)
- `residual` Monetary (compute=_compute_from_moves)
- `currency_id` Many2one → `res.currency` (compute=_compute_from_moves)
- `move_type` Char (compute=_compute_from_moves)

Public methods: `default_get`, `modify_moves`, `refund_moves`, `reverse_moves`

Extension points: `_check_journal_type`, `_prepare_default_reversal`

## `account.move.send.batch.wizard` (defines)

Account Move Send Batch Wizard

Inherits: `account.move.send`

- `move_ids` Many2many → `account.move` (required)
- `summary_data` Json (compute=_compute_summary_data)
- `alerts` Json (compute=_compute_alerts)

Public methods: `action_send_and_print`, `default_get`

Extension points: `_check_move_ids_constraints`

## `account.move.send.wizard` (defines)

Account Move Send Wizard

Inherits: `account.move.send`, `mail.composer.mixin`

- `move_id` Many2one → `account.move` (required)
- `company_id` Many2one → `res.company` (related=move_id.company_id)
- `alerts` Json (compute=_compute_alerts)
- `sending_methods` Json (compute=_compute_sending_methods)
- `sending_method_checkboxes` Json (store, compute=_compute_sending_method_checkboxes)
- `display_attachments_widget` Boolean (compute=_compute_display_attachments_widget)
- `extra_edis` Json (compute=_compute_extra_edis)
- `extra_edi_checkboxes` Json (store, compute=_compute_extra_edi_checkboxes)
- `invoice_edi_format` Selection (compute=_compute_invoice_edi_format)
- `pdf_report_id` Many2one → `ir.actions.report` “Invoice report” (store, compute=_compute_pdf_report_id)
- `available_pdf_report_ids` One2many → `ir.actions.report` (compute=_compute_available_pdf_report_ids)
- `display_pdf_report_id` Boolean (compute=_compute_display_pdf_report_id)
- `template_id` Many2one (store, compute=_compute_template_id)
- `lang` Char (compute=_compute_lang)
- `mail_partner_ids` Many2many → `res.partner` “To” (store, compute=_compute_mail_partners)
- `mail_attachments_widget` Json (store, compute=_compute_mail_attachments_widget)
- `attachments_not_supported` Json (compute=_compute_attachments_not_supported)
- `model` Char “Related Document Model” (store, compute=_compute_model)
- `res_ids` Text “Related Document IDs” (store, compute=_compute_res_ids)
- `template_name` Char “Template Name”

Public methods: `action_send_and_print`, `cancel_save_template`, `create_mail_template`, `default_get`, `open_template_creation_wizard`

Extension points: `_action_download`, `_check_move_id_constraints`, `_get_selected_checkboxes`, `_get_sending_settings`

## `account.payment.register` (defines)

Pay

- `payment_date` Date “Payment Date” (required)
- `amount` Monetary (store, compute=_compute_amount)
- `hide_writeoff_section` Boolean (compute=_compute_hide_writeoff_section)
- `communication` Char “Memo” (store, compute=_compute_communication)
- `group_payment` Boolean “Group Payments” (store, compute=_compute_group_payment)
- `early_payment_discount_mode` Boolean (compute=_compute_early_payment_discount_mode)
- `currency_id` Many2one → `res.currency` “Currency” (store, compute=_compute_currency_id)
- `journal_id` Many2one → `account.journal` (store, compute=_compute_journal_id)
- `available_journal_ids` Many2many → `account.journal` (compute=_compute_available_journal_ids)
- `available_partner_bank_ids` Many2many → `res.partner.bank` (compute=_compute_available_partner_bank_ids)
- `partner_bank_id` Many2one → `res.partner.bank` “Recipient Bank Account” (store, compute=_compute_partner_bank_id)
- `company_currency_id` Many2one → `res.currency` “Company Currency” (related=company_id.currency_id)
- `qr_code` Html “QR Code URL” (compute=_compute_qr_code)
- `batches` Binary (compute=_compute_batches)
- `installments_mode` Selection (store, compute=_compute_installments_mode)
- `installments_switch_html` Html (compute=_compute_installments_switch_values)
- `installments_switch_amount` Monetary (compute=_compute_installments_switch_values)
- `custom_user_amount` Monetary
- `custom_user_currency_id` Many2one → `res.currency`
- `line_ids` Many2many → `account.move.line` “Journal items” (readonly)
- `payment_type` Selection “Payment Type” (store, compute=_compute_from_lines)
- `partner_type` Selection (store, compute=_compute_from_lines)
- `source_amount` Monetary “Amount to Pay (company currency)” (store, compute=_compute_from_lines)
- `source_amount_currency` Monetary “Amount to Pay (foreign currency)” (store, compute=_compute_from_lines)
- `source_currency_id` Many2one → `res.currency` “Source Currency” (store, compute=_compute_from_lines)
- `can_edit_wizard` Boolean (store, compute=_compute_from_lines)
- `can_group_payments` Boolean (store, compute=_compute_can_group_payments)
- `company_id` Many2one → `res.company` (store, compute=_compute_from_lines)
- `partner_id` Many2one → `res.partner` “Customer/Vendor” (store, compute=_compute_from_lines)
- `payment_method_line_id` Many2one → `account.payment.method.line` “Payment Method” (store, compute=_compute_payment_method_line_id)
- `available_payment_method_line_ids` Many2many → `account.payment.method.line` (compute=_compute_payment_method_line_fields)
- `payment_method_code` Char (related=payment_method_line_id.code)
- `payment_difference` Monetary (compute=_compute_payment_difference)
- `payment_difference_handling` Selection “Payment Difference Handling” (store, compute=_compute_payment_difference_handling)
- `writeoff_account_id` Many2one → `account.account` “Difference Account”
- `writeoff_label` Char “Journal Item Label”
- `writeoff_is_exchange_account` Boolean (compute=_compute_writeoff_is_exchange_account)
- `show_payment_difference` Boolean (compute=_compute_show_payment_difference)
- `show_partner_bank_account` Boolean (compute=_compute_show_require_partner_bank)
- `require_partner_bank_account` Boolean (compute=_compute_show_require_partner_bank)
- `country_code` Char (readonly, related=company_id.account_fiscal_country_id.code)
- `duplicate_payment_ids` Many2many → `account.payment` (compute=_compute_duplicate_moves)
- `is_register_payment_on_draft` Boolean (compute=_compute_is_register_payment_on_draft)
- `actionable_errors` Json (compute=_compute_actionable_errors)
- `untrusted_bank_ids` Many2many → `res.partner.bank` (compute=_compute_trust_values)
- `total_payments_amount` Integer (compute=_compute_trust_values)
- `untrusted_payments_count` Integer (compute=_compute_trust_values)
- `missing_account_partners` Many2many → `res.partner` (compute=_compute_trust_values)

Public methods: `action_create_payments`, `action_open_missing_account_partners`, `action_open_untrusted_bank_accounts`, `default_get`

Extension points: `_create_payment_vals_from_batch`, `_create_payment_vals_from_wizard`, `_create_payments`, `_get_batch_account`, `_get_batch_available_journals`, `_get_batch_available_partner_banks`, `_get_batch_journal`, `_get_communication`, `_get_line_batch_key`, `_get_next_payment_date_in_context`, `_get_total_amounts_to_pay`, `_get_wizard_values_from_batch`, `_post_payments`

## `account.resequence.wizard` (defines)

Remake the sequence of Journal Entries.

- `sequence_number_reset` Char (compute=_compute_sequence_number_reset)
- `first_date` Date
- `end_date` Date
- `first_name` Char “First New Sequence” (required, store, compute=_compute_first_name)
- `ordering` Selection (required)
- `move_ids` Many2many → `account.move`
- `new_values` Text (compute=_compute_new_values)
- `preview_moves` Text (compute=_compute_preview_moves)

Public methods: `default_get`, `resequence`

## `account.secure.entries.wizard` (defines)

Secure Journal Entries

- `company_id` Many2one → `res.company` (required, readonly)
- `country_code` Char (related=company_id.account_fiscal_country_id.code)
- `hash_date` Date “Hash All Entries” (required, store, compute=_compute_hash_date)
- `chains_to_hash_with_gaps` Json (compute=_compute_data)
- `max_hash_date` Date “Max Hash Date” (compute=_compute_max_hash_date)
- `unreconciled_bank_statement_line_ids` Many2many → `account.bank.statement.line` (compute=_compute_data)
- `not_hashable_unlocked_move_ids` Many2many → `account.move` (compute=_compute_data)
- `move_to_hash_ids` Many2many → `account.move` (compute=_compute_data)
- `warnings` Json (compute=_compute_warnings)

Public methods: `action_secure_entries`, `action_show_draft_moves_in_hashed_period`, `action_show_moves`

Extension points: `_get_chains_to_hash`, `_get_draft_moves_in_hashed_period_domain`, `_get_unhashed_moves_in_hashed_period_domain`

## `validate.account.move` (defines)

Validate Account Move

- `move_ids` Many2many → `account.move`
- `force_post` Boolean “Force”
- `display_force_post` Boolean (compute=_compute_display_force_post)
- `force_hash` Boolean “Force Hash”
- `display_force_hash` Boolean (compute=_compute_display_force_hash)
- `is_entries` Boolean (compute=_compute_is_entries)
- `abnormal_date_partner_ids` One2many → `res.partner` (compute=_compute_abnormal_date_partner_ids)
- `ignore_abnormal_date` Boolean
- `abnormal_amount_partner_ids` One2many → `res.partner` (compute=_compute_abnormal_amount_partner_ids)
- `ignore_abnormal_amount` Boolean

Public methods: `default_get`, `validate_move`

## `account.accrued.orders.wizard` (defines)

Accrued Orders Wizard

- `company_id` Many2one → `res.company`
- `journal_id` Many2one → `account.journal` “Journal” (required, store, compute=_compute_journal_id)
- `date` Date (required)
- `reversal_date` Date (required, store, compute=_compute_reversal_date)
- `amount` Monetary “Amount”
- `currency_id` Many2one “Company Currency” (readonly, store, related=company_id.currency_id)
- `account_types` Json (compute=_compute_account_types)
- `account_id` Many2one → `account.account` “Accrual Account” (required)
- `preview_data` Text (compute=_compute_preview_data)
- `display_amount` Boolean (compute=_compute_display_amount)

Public methods: `create_entries`

Extension points: `_get_accrual_message_body`, `_get_computed_account`, `_get_default_company`, `_get_default_date`, `_get_orders_and_lines`, `_get_product_expense_and_stock_var_accounts`

## `base.document.layout` (extends)

- `from_invoice` Boolean
- `qr_code` Boolean (related=company_id.qr_code)
- `vat` Char (related=company_id.vat)
- `account_number` Char (compute=_compute_account_number)

Public methods: `document_layout_save`

Extension points: `_get_preview_template`, `_get_render_information`

## `base.partner.merge.automatic.wizard` (extends)


Extension points: `_get_summable_fields`

## `account.financial.year.op` (defines)

Opening Balance of Financial Year

- `company_id` Many2one → `res.company` (required)
- `opening_move_posted` Boolean “Opening Move Posted” (compute=_compute_opening_move_posted)
- `opening_date` Date “Opening Date” (required, related=company_id.account_opening_date)
- `fiscalyear_last_day` Integer (required, related=company_id.fiscalyear_last_day)
- `fiscalyear_last_month` Selection (required, related=company_id.fiscalyear_last_month)

Public methods: `action_save_onboarding_fiscal_year`, `create`, `write`

Extension points: `_check_fiscalyear`

## `account.setup.bank.manual.config` (defines)

Bank setup manual config

- `res_partner_bank_id` Many2one → `res.partner.bank` (required)
- `new_journal_name` Char (required)
- `linked_journal_id` Many2one → `account.journal` “Journal” (compute=_compute_linked_journal_id)
- `bank_bic` Char “Bic” (related=bank_id.bic)
- `num_journals_without_account_bank` Integer
- `num_journals_without_account_credit` Integer
- `company_id` Many2one → `res.company` (required, compute=_compute_company_id)

Public methods: `create`, `default_linked_journal_id`, `set_linked_journal_id`, `validate`
