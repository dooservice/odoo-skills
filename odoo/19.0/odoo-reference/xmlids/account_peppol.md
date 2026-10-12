# account_peppol — XML ids

## ir.actions.client

- `account_peppol.action_peppol_auth_callback`

## ir.actions.server

- `account_peppol.partner_action_verify_peppol`

## ir.cron

- `account_peppol.ir_cron_peppol_get_new_documents`
- `account_peppol.ir_cron_peppol_get_message_status`
- `account_peppol.ir_cron_peppol_get_participant_status`
- `account_peppol.ir_cron_peppol_webhook_keepalive`

## ir.ui.view

- `account_peppol.mail_notification_layout_with_responsible_signature_and_peppol` — inherits mail.mail_notification_layout_with_responsible_signature
- `account_peppol.account_peppol_view_move_form` — on account.move inherits account.view_move_form
- `account_peppol.account_peppol_view_out_invoice_tree_inherit` — on account.move inherits account.view_out_invoice_tree
- `account_peppol.account_peppol_view_out_credit_note_tree_inherit` — on account.move inherits account.view_out_credit_note_tree
- `account_peppol.account_peppol_view_account_invoice_filter` — on account.move inherits account.view_account_invoice_filter
- `account_peppol.portal_my_details` — inherits portal.portal_my_details
- `account_peppol.res_partner_form_account_peppol` — on res.partner inherits account_edi_ubl_cii.view_partner_property_form
- `account_peppol.res_config_settings_view_form` — on res.config.settings inherits account.res_config_settings_view_form
- `account_peppol.peppol_registration_form` — on peppol.registration
- `account_peppol.peppol_config_wizard_form` — on peppol.config.wizard

## mail.template

- `account_peppol.mail_template_peppol_registration`
