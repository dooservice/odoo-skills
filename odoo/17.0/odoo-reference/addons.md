# Addons

| Addon | Name | Defines | Extends |
|---|---|---|---|
| base | Base | `avatar.mixin`, `decimal.precision`, `image.mixin`, `ir.actions.actions`, `ir.actions.act_window`, `ir.actions.act_window.view`, `ir.actions.act_window_close`, `ir.actions.act_url`, `ir.actions.server`, `ir.actions.todo`, `ir.actions.client`, `ir.actions.report`, `ir.asset`, `ir.attachment`, `ir.autovacuum`, `ir.binary`, `ir.config_parameter`, `ir.cron`, `ir.cron.trigger`, `ir.default`, `ir.demo`, `ir.demo_failure`, `ir.demo_failure.wizard`, `ir.exports`, `ir.exports.line`, `ir.fields.converter`, `ir.filters`, `ir.http`, `ir.logging`, `ir.mail_server`, `base`, `_unknown`, `ir.model`, `ir.model.fields`, `ir.model.inherit`, `ir.model.fields.selection`, `ir.model.constraint`, `ir.model.relation`, `ir.model.access`, `ir.model.data`, `wizard.ir.model.menu.create`, `ir.module.category`, `ir.module.module`, `ir.module.module.dependency`, `ir.module.module.exclusion`, `ir.profile`, `base.enable.profiling.wizard`, `ir.property`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.many2one`, `ir.qweb.field.many2many`, `ir.qweb.field.one2many`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.qweb.field.monetary`, `ir.qweb.field.float_time`, `ir.qweb.field.time`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.barcode`, `ir.qweb.field.contact`, `ir.qweb.field.qweb`, `ir.rule`, `ir.sequence`, `ir.sequence.date_range`, `ir.ui.menu`, `ir.ui.view.custom`, `ir.ui.view`, `reset.view.arch.wizard`, `report.layout`, `report.paperformat`, `res.bank`, `res.partner.bank`, `res.company`, `res.config`, `res.config.installer`, `res.config.settings`, `res.country`, `res.country.group`, `res.country.state`, `res.currency`, `res.currency.rate`, `res.lang`, `format.address.mixin`, `res.partner.category`, `res.partner.title`, `res.partner`, `res.partner.industry`, `res.groups`, `res.users.log`, `res.users`, `res.users.identitycheck`, `change.password.wizard`, `change.password.user`, `change.password.own`, `res.users.apikeys`, `res.users.apikeys.description`, `res.users.apikeys.show`, `res.users.deletion`, `res.users.settings`, `report.base.report_irmodulereference`, `base.language.export`, `base.language.import`, `base.language.install`, `base.module.uninstall`, `base.module.update`, `base.module.upgrade`, `base.partner.merge.line`, `base.partner.merge.automatic.wizard` | `base`, `ir.filters`, `ir.module.category`, `res.company`, `res.currency.rate`, `res.groups`, `res.partner.industry`, `res.partner`, `res.users` |
| account | Invoicing | `account.account`, `account.group`, `account.root`, `account.account.tag`, `account.bank.statement`, `account.bank.statement.line`, `account.cash.rounding`, `account.full.reconcile`, `account.incoterms`, `account.journal.group`, `account.journal`, `account.move`, `account.move.line`, `account.partial.reconcile`, `account.payment`, `account.payment.method`, `account.payment.method.line`, `account.payment.term`, `account.payment.term.line`, `account.reconcile.model.partner.mapping`, `account.reconcile.model.line`, `account.reconcile.model`, `account.report`, `account.report.line`, `account.report.expression`, `account.report.column`, `account.report.external.value`, `account.tax.group`, `account.tax`, `account.tax.repartition.line`, `account.chart.template`, `account.fiscal.position`, `account.fiscal.position.tax`, `account.fiscal.position.account`, `sequence.mixin`, `report.account.report_hash_integrity`, `account.invoice.report`, `report.account.report_invoice`, `report.account.report_invoice_with_payments`, `account.automatic.entry.wizard`, `account.move.reversal`, `account.move.send`, `account.payment.register`, `account.resequence.wizard`, `account.tour.upload.bill`, `account.tour.upload.bill.email.confirm`, `account.unreconcile`, `validate.account.move`, `account.accrued.orders.wizard`, `account.financial.year.op`, `account.setup.bank.manual.config` | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.distribution.model`, `account.analytic.line`, `account.bank.statement.line`, `account.bank.statement`, `account.chart.template`, `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.reconcile.model.line`, `account.reconcile.model`, `base.document.layout`, `base.partner.merge.automatic.wizard`, `decimal.precision`, `digest.digest`, `ir.actions.report`, `ir.attachment`, `ir.http`, `ir.module.module`, `kpi.provider`, `onboarding.onboarding.step`, `onboarding.onboarding`, `product.category`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.currency`, `res.groups`, `res.partner.bank`, `res.partner`, `uom.uom` |
| account_add_gln | Add Partner GLN |  | `res.partner` |
| account_audit_trail | Account Audit Trail |  | `account.bank.statement.line`, `account.move`, `base.partner.merge.automatic.wizard`, `mail.message`, `mail.tracking.value`, `res.company`, `res.config.settings` |
| account_check_printing | Check Printing Base | `print.prenumbered.checks` | `account.journal`, `account.move`, `account.payment.method`, `account.payment.register`, `account.payment`, `res.company`, `res.config.settings`, `res.partner` |
| account_debit_note | Debit Notes | `account.debit.note` | `account.move` |
| account_debit_note_sequence | Debit Note Sequence |  | `account.journal`, `account.move` |
| account_edi | Import/Export Invoices From XML/PDF | `account.edi.document`, `account.edi.format` | `account.journal`, `account.move.send`, `account.move`, `account.resequence.wizard`, `ir.actions.report`, `ir.attachment` |
| account_edi_proxy_client | Proxy features for account_edi | `account_edi_proxy_client.user` | `res.company` |
| account_edi_ubl_cii | Import/Export electronic invoices with UBL/CII | `account.edi.common`, `account.edi.xml.cii`, `account.edi.xml.ubl_20`, `account.edi.xml.ubl_21`, `account.edi.xml.ubl_a_nz`, `account.edi.xml.ubl_bis3`, `account.edi.xml.ubl_efff`, `account.edi.xml.ubl_nl`, `account.edi.xml.ubl_sg`, `account.edi.xml.ubl_de` | `account.move.send`, `account.move`, `ir.actions.report`, `res.company`, `res.config.settings`, `res.partner` |
| account_edi_ubl_cii_tax_extension | Tax extension for UBL/CII |  | `account.edi.common`, `account.tax` |
| account_fleet | Accounting/Fleet bridge |  | `account.automatic.entry.wizard`, `account.move.line`, `account.move`, `fleet.vehicle` |
| account_lock | Irreversible Lock Date |  | `res.company` |
| account_payment | Payment - Account | `payment.refund.wizard` | `account.journal`, `account.move`, `account.payment.method.line`, `account.payment.method`, `account.payment.register`, `account.payment`, `onboarding.onboarding.step`, `payment.link.wizard`, `payment.provider`, `payment.transaction`, `res.config.settings` |
| account_payment_term | Payment Term - Days end of month on the |  | `account.payment.term.line` |
| account_peppol | Peppol |  | `account.journal`, `account.move.send`, `account.move`, `account_edi_proxy_client.user`, `res.company`, `res.config.settings`, `res.partner` |
| account_peppol_response | Peppol Business Response | `account.peppol.clarification`, `account.peppol.response`, `account.peppol.rejection.wizard` | `account.move`, `account_edi_proxy_client.user`, `res.company`, `res.partner` |
| account_peppol_selfbilling | Peppol Self Billing |  | `account.edi.xml.ubl_bis3`, `account.journal`, `account.move.send`, `account.move`, `account_edi_proxy_client.user` |
| account_qr_code_emv | account_qr_code_emv |  | `res.partner.bank` |
| account_qr_code_sepa | Account SEPA QR Code |  | `res.partner.bank` |
| account_tax_python | Define Taxes as Python Code |  | `account.tax` |
| account_test | Accounting Consistency Tests | `accounting.assert.test`, `report.account_test.report_accounttest` |  |
| account_update_tax_tags | Account - Allow updating tax grids | `account.update.tax.tags.wizard` |  |
| analytic | Analytic Accounting | `account.analytic.account`, `account.analytic.distribution.model`, `account.analytic.line`, `analytic.mixin`, `account.analytic.plan`, `account.analytic.applicability` | `account.analytic.account`, `account.analytic.line`, `ir.config_parameter`, `res.config.settings` |
| attachment_indexation | Attachments List and Document Indexation |  | `ir.attachment` |
| auth_ldap | Authentication via LDAP | `res.company.ldap` | `res.company`, `res.config.settings`, `res.users` |
| auth_oauth | OAuth2 Authentication | `auth.oauth.provider` | `ir.config_parameter`, `res.config.settings`, `res.users` |
| auth_password_policy | Password Policy |  | `res.config.settings`, `res.users` |
| auth_password_policy_portal | Password Policy support for Signup |  |  |
| auth_password_policy_signup | Password Policy support for Signup |  |  |
| auth_signup | Signup |  | `ir.http`, `res.config.settings`, `res.partner`, `res.users` |
| auth_totp | Two-Factor Authentication (TOTP) | `auth_totp.device`, `auth_totp.wizard` | `ir.http`, `res.users` |
| auth_totp_mail | 2FA Invite mail |  | `auth_totp.device`, `res.users` |
| auth_totp_mail_enforce | 2FA by mail | `auth.totp.rate.limit.log` | `res.config.settings`, `res.users` |
| auth_totp_portal | TOTPortal |  | `res.users` |
| barcodes | Barcode | `barcodes.barcode_events_mixin`, `barcode.nomenclature`, `barcode.rule` | `ir.http`, `res.company` |
| barcodes_gs1_nomenclature | Barcode - GS1 Nomenclature |  | `barcode.nomenclature`, `barcode.rule`, `ir.http` |
| base_address_extended | Extended Addresses | `res.city` | `res.country`, `res.partner` |
| base_automation | Automation Rules | `base.automation` | `ir.actions.server` |
| base_geolocalize | Partners Geolocation | `base.geo_provider`, `base.geocoder` | `res.config.settings`, `res.partner` |
| base_iban | IBAN Bank Accounts |  | `res.partner.bank` |
| base_import | Base import | `base_import.mapping`, `base_import.import` | `base`, `res.users` |
| base_import_module | Base import module | `base.import.module` | `base.module.uninstall`, `ir.module.module`, `ir.ui.view` |
| base_install_request | Base - Module Install Request | `base.module.install.request`, `base.module.install.review` | `ir.module.module` |
| base_setup | Initial Setup Tools | `kpi.provider` | `ir.http`, `res.config.settings`, `res.users` |
| base_sparse_field | Sparse Fields | `sparse_fields.test` | `base`, `ir.model.fields` |
| base_vat | VAT Number Validation |  | `account.fiscal.position`, `res.company`, `res.config.settings`, `res.partner` |
| board | Dashboards | `board.board` |  |
| bus | IM Bus | `bus.bus`, `bus.presence`, `ir.websocket` | `ir.http`, `ir.model`, `ir.qweb`, `res.partner`, `res.users` |
| calendar | Calendar | `calendar.alarm`, `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.event.type`, `calendar.filters`, `calendar.recurrence`, `calendar.popover.delete.wizard`, `calendar.provider.config` | `calendar.alarm`, `ir.http`, `mail.activity.mixin`, `mail.activity.schedule`, `mail.activity.type`, `mail.activity`, `onboarding.onboarding.step`, `onboarding.onboarding`, `res.partner`, `res.users` |
| calendar_sms | Calendar - SMS |  | `calendar.alarm_manager`, `calendar.alarm`, `calendar.event` |
| contacts | Contacts |  | `res.users` |
| crm | CRM | `crm.lead`, `crm.lead.scoring.frequency`, `crm.lead.scoring.frequency.field`, `crm.lost.reason`, `crm.recurring.plan`, `crm.stage`, `crm.activity.report`, `crm.lead.lost`, `crm.lead.pls.update`, `crm.lead2opportunity.partner`, `crm.lead2opportunity.partner.mass`, `crm.merge.opportunity` | `calendar.event`, `crm.lead`, `crm.team.member`, `crm.team`, `digest.digest`, `ir.config_parameter`, `mail.activity`, `res.config.settings`, `res.partner`, `res.users`, `utm.campaign` |
| crm_iap_enrich | Lead Enrichment |  | `crm.lead`, `res.config.settings` |
| crm_iap_mine | Lead Generation | `crm.iap.lead.helpers`, `crm.iap.lead.industry`, `crm.iap.lead.mining.request`, `crm.iap.lead.role`, `crm.iap.lead.seniority` | `crm.lead` |
| crm_livechat | CRM Livechat |  | `chatbot.script.step`, `chatbot.script`, `discuss.channel` |
| crm_mail_plugin | CRM Mail Plugin |  | `crm.lead` |
| crm_sms | SMS in CRM |  |  |
| data_recycle | Data Recycle | `data_recycle.model`, `data_recycle.record` |  |
| delivery | Delivery Costs | `delivery.carrier`, `delivery.price.rule`, `delivery.zip.prefix`, `choose.delivery.carrier` | `product.category`, `res.partner`, `sale.order.line`, `sale.order` |
| delivery_mondialrelay | delivery_mondialrelay |  | `choose.delivery.carrier`, `delivery.carrier`, `res.partner`, `sale.order` |
| delivery_stock_picking_batch | Delivery Stock Picking Batch |  | `stock.picking.batch`, `stock.picking.type`, `stock.picking` |
| digest | KPI Digests | `digest.digest`, `digest.tip` | `res.config.settings`, `res.users` |
| event | Events Organization | `event.type`, `event.event`, `event.type.mail`, `event.mail`, `event.mail.registration`, `event.registration`, `event.stage`, `event.tag.category`, `event.tag`, `event.type.ticket`, `event.event.ticket` | `mail.template`, `res.config.settings`, `res.partner` |
| event_booth | Events Booths | `event.booth`, `event.booth.category`, `event.type.booth` | `event.event`, `event.type` |
| event_booth_sale | Events Booths Sales | `event.booth.registration`, `event.booth.configurator` | `account.move`, `event.booth.category`, `event.booth`, `event.type.booth`, `product.product`, `product.template`, `sale.order.line`, `sale.order` |
| event_crm | Event CRM | `event.lead.rule` | `crm.lead`, `event.event`, `event.registration` |
| event_crm_sale | Event CRM Sale |  | `event.registration` |
| event_sale | Events Sales | `event.sale.report`, `event.event.configurator`, `registration.editor`, `registration.editor.line` | `event.event.ticket`, `event.event`, `event.registration`, `event.type.ticket`, `product.product`, `product.template`, `sale.order.line`, `sale.order` |
| event_sms | SMS on Events |  | `event.mail.registration`, `event.mail`, `event.type.mail`, `sms.template` |
| fleet | Fleet | `fleet.service.type`, `fleet.vehicle`, `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.model`, `fleet.vehicle.model.brand`, `fleet.vehicle.model.category`, `fleet.vehicle.odometer`, `fleet.vehicle.state`, `fleet.vehicle.tag`, `fleet.vehicle.cost.report` | `mail.activity.type`, `res.config.settings`, `res.partner` |
| gamification | Gamification | `gamification.badge`, `gamification.badge.user`, `gamification.challenge`, `gamification.challenge.line`, `gamification.goal`, `gamification.goal.definition`, `gamification.karma.rank`, `gamification.karma.tracking`, `gamification.badge.user.wizard`, `gamification.goal.wizard` | `res.users` |
| gamification_sale_crm | CRM Gamification |  |  |
| google_account | Google Users | `google.service` |  |
| google_calendar | Google Calendar | `google.calendar.credentials`, `google.calendar.sync`, `google.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.recurrence`, `res.config.settings`, `res.users` |
| google_gmail | Google Gmail | `google.gmail.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings` |
| google_recaptcha | Google reCAPTCHA integration |  | `ir.http`, `res.config.settings` |
| hr | Employees | `hr.contract.type`, `hr.department`, `hr.departure.reason`, `hr.employee`, `hr.employee.base`, `hr.employee.category`, `hr.employee.public`, `hr.job`, `hr.work.location`, `hr.departure.wizard` | `base`, `discuss.channel`, `hr.department`, `hr.employee.category`, `hr.employee`, `hr.job`, `hr.work.location`, `ir.ui.menu`, `mail.activity.plan.template`, `mail.activity.plan`, `mail.activity.schedule`, `mail.alias`, `res.company`, `res.config.settings`, `res.partner.bank`, `res.partner`, `res.users`, `resource.resource` |
| hr_attendance | Attendances | `hr.attendance`, `hr.attendance.overtime` | `hr.employee.base`, `hr.employee.public`, `hr.employee`, `res.company`, `res.config.settings`, `res.users`, `resource.calendar.leaves` |
| hr_contract | Employee Contracts | `hr.contract`, `hr.payroll.structure.type`, `hr.contract.history` | `hr.departure.wizard`, `hr.employee.base`, `hr.employee.public`, `hr.employee`, `mail.activity.schedule`, `res.company`, `res.config.settings`, `res.users`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource` |
| hr_expense | Expenses | `hr.expense`, `hr.expense.sheet`, `hr.expense.approve.duplicate`, `hr.expense.refuse.wizard`, `hr.expense.split`, `hr.expense.split.wizard` | `account.analytic.account`, `account.analytic.applicability`, `account.journal`, `account.move.line`, `account.move`, `account.payment.register`, `account.payment`, `account.tax`, `hr.department`, `hr.employee.base`, `hr.employee.public`, `hr.employee`, `ir.actions.report`, `ir.attachment`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.users` |
| hr_fleet | Fleet History |  | `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.odometer`, `fleet.vehicle`, `hr.departure.wizard`, `hr.employee.public`, `hr.employee`, `mail.activity.plan.template`, `res.users` |
| hr_gamification | HR Gamification |  | `gamification.badge.user.wizard`, `gamification.badge.user`, `gamification.badge`, `hr.employee.base`, `res.users` |
| hr_holidays | Time Off | `hr.leave`, `hr.leave.accrual.plan`, `hr.leave.accrual.level`, `hr.leave.allocation`, `hr.leave.mandatory.day`, `hr.leave.type`, `report.hr_holidays.report_holidayssummary`, `hr.leave.employee.type.report`, `hr.leave.report`, `hr.leave.report.calendar`, `hr.holidays.cancel.leave`, `hr.holidays.summary.employee` | `hr.department`, `hr.departure.wizard`, `hr.employee.base`, `hr.employee`, `hr.leave.allocation`, `hr.leave.type`, `hr.leave`, `mail.activity.type`, `mail.message.subtype`, `res.partner`, `res.users`, `resource.calendar.leaves`, `resource.calendar` |
| hr_holidays_attendance | HR Attendance Holidays |  | `hr.attendance`, `hr.leave.accrual.level`, `hr.leave.allocation`, `hr.leave.type`, `hr.leave`, `res.company`, `res.users` |
| hr_homeworking | Remote Work | `hr.employee.location`, `homework.location.wizard` | `hr.employee.base`, `hr.work.location`, `res.partner`, `res.users` |
| hr_hourly_cost | Employee Hourly Wage |  | `hr.employee` |
| hr_livechat | HR - Livechat |  |  |
| hr_maintenance | Maintenance - HR |  | `hr.employee`, `maintenance.equipment`, `maintenance.request`, `res.users` |
| hr_org_chart | HR Org Chart |  | `hr.employee.base`, `hr.employee.public`, `hr.employee` |
| hr_presence | Employee Presence Control |  | `hr.employee.base`, `ir.websocket`, `res.company`, `res.users.log` |
| hr_recruitment | Recruitment | `hr.applicant`, `hr.applicant.category`, `hr.applicant.refuse.reason`, `hr.recruitment.degree`, `hr.recruitment.source`, `hr.recruitment.stage`, `applicant.get.refuse.reason`, `applicant.send.mail` | `calendar.event`, `digest.digest`, `hr.department`, `hr.employee`, `hr.job`, `ir.ui.menu`, `res.config.settings`, `res.users`, `utm.campaign`, `utm.source` |
| hr_recruitment_skills | Recruitment - Skills Management | `hr.applicant.skill` | `hr.applicant` |
| hr_recruitment_sms | Recruitment - SMS |  |  |
| hr_recruitment_survey | Hr Recruitment Interview Forms |  | `hr.applicant`, `hr.job`, `survey.invite`, `survey.user_input` |
| hr_skills | Skills Management | `hr.employee.skill`, `hr.employee.skill.log`, `hr.resume.line`, `hr.resume.line.type`, `hr.skill`, `hr.skill.level`, `hr.skill.type`, `report.hr_skills.report_employee_cv`, `hr.employee.skill.report`, `hr.employee.cv.wizard` | `hr.employee.public`, `hr.employee`, `res.users` |
| hr_skills_slides | Skills e-learning |  | `hr.employee`, `hr.resume.line`, `slide.channel.partner`, `slide.channel` |
| hr_skills_survey | Skills Certification |  | `hr.resume.line`, `survey.user_input` |
| hr_timesheet | Task Logs | `timesheets.analysis.report`, `hr.employee.delete.wizard` | `account.analytic.line`, `hr.employee`, `ir.http`, `ir.ui.menu`, `project.collaborator`, `project.project`, `project.task`, `project.update`, `report.project.task.user`, `res.company`, `res.config.settings`, `uom.uom` |
| hr_timesheet_attendance | Timesheets/attendances reporting | `hr.timesheet.attendance.report` | `ir.ui.menu` |
| hr_work_entry | Work Entries | `hr.work.entry`, `hr.work.entry.type`, `hr.user.work.entry.employee` | `hr.employee`, `resource.calendar.attendance`, `resource.calendar.leaves` |
| hr_work_entry_contract | Work Entries - Contract | `hr.work.entry.regeneration.wizard` | `hr.contract`, `hr.employee`, `hr.work.entry.type`, `hr.work.entry`, `resource.calendar` |
| hr_work_entry_holidays | Time Off in Payslips |  | `hr.contract`, `hr.employee.base`, `hr.leave.type`, `hr.leave`, `hr.work.entry.type`, `hr.work.entry` |
| http_routing | Web Routing |  | `ir.http`, `ir.qweb` |
| iap | In-App Purchases | `iap.account`, `iap.account.info`, `iap.enrich.api` |  |
| iap_crm | IAP / CRM |  | `crm.lead` |
| iap_mail | IAP / Mail |  | `iap.account` |
| im_livechat | Live Chat | `chatbot.message`, `chatbot.script`, `chatbot.script.answer`, `chatbot.script.step`, `im_livechat.channel`, `im_livechat.channel.rule`, `im_livechat.report.channel`, `im_livechat.report.operator` | `digest.digest`, `discuss.channel.member`, `discuss.channel`, `ir.qweb`, `mail.message`, `rating.rating`, `res.partner`, `res.users.settings`, `res.users` |
| im_livechat_mail_bot | OdooBot for livechat |  | `mail.bot`, `res.users` |
| l10n_account_edi_ubl_cii_tests | Testing the Import/Export invoices with UBL/CII |  |  |
| l10n_ae | United Arab Emirates - Accounting |  | `account.chart.template`, `account.move.line` |
| l10n_anz_ubl_pint | Australia & New Zealand - UBL PINT | `account.edi.xml.pint_anz` | `res.partner` |
| l10n_ar | Argentina - Accounting | `l10n_ar.afip.responsibility.type` | `account.chart.template`, `account.fiscal.position`, `account.invoice.report`, `account.journal`, `account.move.line`, `account.move`, `account.tax.group`, `l10n_latam.document.type`, `l10n_latam.identification.type`, `res.company`, `res.country`, `res.currency`, `res.partner.bank`, `res.partner`, `uom.uom` |
| l10n_ar_pos | Argentinean - Point of Sale with AR Doc |  | `pos.session`, `res.partner` |
| l10n_ar_website_sale | Argentinean eCommerce |  | `sale.order`, `website` |
| l10n_ar_withholding | Argentina - Payment Withholdings | `l10n_ar.payment.register.withholding` | `account.chart.template`, `account.move`, `account.payment.register`, `account.payment`, `account.tax`, `res.company`, `res.config.settings` |
| l10n_at | Austria - Accounting |  | `account.chart.template`, `account.journal` |
| l10n_au | Australia - Accounting |  | `account.chart.template`, `account.move`, `res.partner.bank` |
| l10n_bd | Bangladesh - Accounting |  | `account.chart.template` |
| l10n_be | Belgium - Accounting |  | `account.chart.template`, `account.journal`, `account.move`, `res.partner` |
| l10n_be_pos_sale | l10n_be_pos_sale |  | `pos.session` |
| l10n_bf | Burkina Faso - Accounting |  | `account.chart.template` |
| l10n_bg | Bulgaria - Accounting |  | `account.chart.template` |
| l10n_bh | Bahrain - Accounting |  | `account.chart.template` |
| l10n_bj | Benin - Accounting |  | `account.chart.template` |
| l10n_bo | Bolivia - Accounting |  | `account.chart.template` |
| l10n_br | Brazilian - Accounting |  | `account.chart.template`, `account.fiscal.position`, `account.journal`, `account.move.reversal`, `account.move`, `account.tax`, `res.company`, `res.partner` |
| l10n_br_pix | Brazil Pix QR codes |  | `res.partner.bank` |
| l10n_br_sales | Brazil - Sale |  | `sale.order` |
| l10n_br_website_sale | Brazil - Website Sale |  | `website` |
| l10n_ca | Canada - Accounting |  | `account.chart.template`, `base.document.layout`, `res.company`, `res.partner` |
| l10n_cd | Democratic Republic of the Congo - Accounting |  | `account.chart.template` |
| l10n_cf | Central African Republic - Accounting |  | `account.chart.template` |
| l10n_cg | Congo - Accounting |  | `account.chart.template` |
| l10n_ch | Switzerland - Accounting | `report.l10n_ch.qr_report_main`, `l10n_ch.qr_invoice.wizard` | `account.chart.template`, `account.journal`, `account.move`, `account.payment`, `account.setup.bank.manual.config`, `ir.actions.report`, `res.partner.bank` |
| l10n_ch_pos | Swiss - Point of Sale |  | `pos.order` |
| l10n_ci | Ivory Coast - Accounting |  | `account.chart.template` |
| l10n_cl | Chile - Accounting |  | `account.chart.template`, `account.move.line`, `account.move`, `account.tax`, `l10n_latam.document.type`, `res.bank`, `res.company`, `res.country`, `res.currency`, `res.partner`, `uom.uom` |
| l10n_cm | Cameroon - Accounting |  | `account.chart.template` |
| l10n_cn | China - Accounting |  | `account.chart.template`, `account.move` |
| l10n_cn_city | China - City Data |  |  |
| l10n_co | Colombia - Accounting |  | `account.chart.template`, `l10n_latam.identification.type`, `res.partner` |
| l10n_co_pos | Colombian - Point of Sale |  | `pos.order` |
| l10n_cr | Costa Rica - Accounting |  | `account.chart.template` |
| l10n_cy | Cyprus - Accounting |  | `account.chart.template` |
| l10n_cz | Czech - Accounting |  | `account.chart.template`, `account.move.line`, `account.move`, `base.document.layout`, `res.company` |
| l10n_de | Germany - Accounting |  | `account.account`, `account.chart.template`, `account.journal`, `account.move`, `account.tax`, `ir.actions.report`, `ir.attachment`, `product.template`, `res.company` |
| l10n_de_audit_trail | Germany - audit trail |  |  |
| l10n_din5008 | DIN 5008 |  | `account.analytic.line`, `account.move`, `base.document.layout` |
| l10n_din5008_purchase | DIN 5008 - Purchase |  | `purchase.order` |
| l10n_din5008_repair | DIN 5008 - Repair |  | `repair.order` |
| l10n_din5008_sale | DIN 5008 - Sale |  | `sale.order` |
| l10n_din5008_stock | DIN 5008 - Stock |  | `stock.picking` |
| l10n_dk | Denmark - Accounting |  | `account.account`, `account.chart.template`, `account.journal`, `res.partner` |
| l10n_dk_audit_trail | Denmark - audit trail |  |  |
| l10n_dk_bookkeeping | Denmark - Bookkeeping Act |  | `account.move` |
| l10n_dk_fik | Denmark - FIK Number |  | `account.journal`, `account.move` |
| l10n_dk_oioubl | Denmark - E-invoicing | `account.edi.xml.oioubl_201` | `account.move`, `res.partner` |
| l10n_do | Dominican Republic - Accounting |  | `account.chart.template` |
| l10n_dz | Algeria - Accounting |  | `account.chart.template` |
| l10n_ec | Ecuadorian Accounting | `l10n_ec.sri.payment` | `account.chart.template`, `account.journal`, `account.move`, `account.tax.group`, `account.tax`, `l10n_latam.document.type`, `res.company`, `res.partner` |
| l10n_ec_stock | Ecuador - Stock |  | `account.chart.template` |
| l10n_ec_website_sale | Ecuadorian Website |  | `payment.method`, `sale.order`, `website` |
| l10n_ee | Estonia - Accounting |  | `account.chart.template`, `account.tax` |
| l10n_eg | Egypt - Accounting |  | `account.chart.template`, `account.tax` |
| l10n_eg_edi_eta | Egypt E-Invoicing | `l10n_eg_edi.activity.type`, `l10n_eg_edi.thumb.drive`, `l10n_eg_edi.uom.code` | `account.edi.format`, `account.journal`, `account.move`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.currency.rate`, `res.partner`, `uom.uom` |
| l10n_es | Spain - Accounting (PGCE 2008) |  | `account.chart.template`, `account.move`, `account.tax`, `res.company`, `res.partner` |
| l10n_es_edi_facturae | Spain - Facturae EDI | `l10n_es_edi_facturae.certificate` | `account.chart.template`, `account.move.reversal`, `account.move.send`, `account.move`, `account.tax`, `res.company`, `res.partner`, `uom.uom` |
| l10n_es_edi_facturae_adm_centers | Spain - Facturae EDI - Administrative Centers Patch | `l10n_es_edi_facturae_adm_centers.ac_role_type` | `account.move`, `res.partner` |
| l10n_es_edi_facturae_invoice_period | Spain - Facturae EDI - Invoice Period |  | `account.move` |
| l10n_es_edi_sii | Spain - SII EDI Suministro de Libros | `l10n_es_edi.certificate` | `account.edi.format`, `account.move.send`, `account.move`, `account.resequence.wizard`, `res.company`, `res.config.settings` |
| l10n_es_edi_tbai | Spain - TicketBAI |  | `account.edi.document`, `account.edi.format`, `account.move.reversal`, `account.move`, `account.resequence.wizard`, `ir.attachment`, `l10n_es_edi.certificate`, `res.company`, `res.config.settings` |
| l10n_es_edi_tbai_multi_refund | TicketBAI multi refund |  | `account.edi.format`, `account.move` |
| l10n_es_edi_verifactu | Spain - Veri*Factu | `l10n_es_edi_verifactu.certificate`, `l10n_es_edi_verifactu.document` | `account.chart.template`, `account.move.reversal`, `account.move.send`, `account.move`, `account.tax`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_es_edi_verifactu_pos | Spain - Veri*Factu for Point of Sale |  | `account.move`, `l10n_es_edi_verifactu.document`, `pos.config`, `pos.order`, `pos.session`, `res.company` |
| l10n_es_modelo130 | Spain - Modelo 130 Tax report |  |  |
| l10n_es_pos | Spain - Point of Sale |  | `account.move`, `pos.config`, `pos.order`, `pos.session`, `res.config.settings` |
| l10n_es_pos_tbai | Spain - POS + TicketBAI |  | `account.move`, `pos.order`, `res.company` |
| l10n_et | Ethiopia - Accounting |  | `account.chart.template` |
| l10n_eu_oss | EU One Stop Shop (OSS) |  | `res.company`, `res.config.settings` |
| l10n_fi | Finnish Localization |  | `account.chart.template`, `account.journal`, `account.move` |
| l10n_fi_sale | Finland - Sale |  | `sale.order` |
| l10n_fr | France - Accounting |  | `account.chart.template`, `res.company`, `res.partner` |
| l10n_fr_facturx_chorus_pro | France - Factur-X integration with Chorus Pro |  | `account.edi.xml.ubl_bis3`, `account.move` |
| l10n_fr_fec | France - FEC Export | `account.fr.fec` |  |
| l10n_fr_hr_holidays | France - Time Off |  | `hr.leave`, `res.company`, `res.config.settings`, `resource.calendar` |
| l10n_fr_hr_work_entry_holidays | France - Work Entries Time Off |  | `hr.contract`, `hr.work.entry` |
| l10n_fr_invoice_addr | France - Adding Mandatory Invoice Mentions (Decree no. 2022-1299) |  | `account.move` |
| l10n_fr_pdp | France - E-Invoicing (Approved Platform) | `account.edi.xml.ubl_21_fr`, `l10n.fr.pdp.reports.flow`, `pdp.flow.10.xml.builder`, `pdp.registration`, `pdp.response.wizard`, `l10n.fr.pdp.reports.send.wizard` | `account.edi.xml.cii`, `account.journal`, `account.move.send`, `account.move`, `account.peppol.response`, `account.tax`, `account_edi_proxy_client.user`, `ir.attachment`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_fr_pdp_pos | France - E-reporting for POS |  | `account.move`, `pdp.flow.10.xml.builder`, `res.company` |
| l10n_fr_pos_cert | France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) | `account.sale.closing`, `report.l10n_fr_pos_cert.report_pos_hash_integrity` | `account.fiscal.position`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.company` |
| l10n_ga | Gabon - Accounting |  | `account.chart.template` |
| l10n_gcc_invoice | G.C.C. - Arabic/English Invoice |  | `account.move.line`, `account.move`, `product.product` |
| l10n_gcc_invoice_stock_account | Gulf Cooperation Council WMS Accounting |  |  |
| l10n_gcc_pos | Gulf Cooperation Council - Point of Sale |  |  |
| l10n_gn | Guinea - Accounting |  | `account.chart.template` |
| l10n_gq | Guinea Equatorial - Accounting |  | `account.chart.template` |
| l10n_gr | Greece - Accounting |  | `account.chart.template` |
| l10n_gt | Guatemala - Accounting |  | `account.chart.template` |
| l10n_gw | Guinea-Bissau - Accounting |  | `account.chart.template` |
| l10n_hk | Hong Kong - Accounting |  | `account.chart.template`, `res.partner.bank` |
| l10n_hn | Honduras - Accounting |  | `account.chart.template` |
| l10n_hr | Croatia - Accounting (Euro) |  | `account.chart.template` |
| l10n_hr_kuna | Croatia - Accounting (Kuna) |  | `account.chart.template` |
| l10n_hu | Hungary - Accounting |  | `account.chart.template`, `account.move`, `res.partner` |
| l10n_hu_edi | Hungary - E-invoicing | `l10n_hu_edi.cancellation`, `l10n_hu_edi.tax_audit_export` | `account.chart.template`, `account.debit.note`, `account.move.line`, `account.move.reversal`, `account.move.send`, `account.move`, `account.tax`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `uom.uom` |
| l10n_id | Indonesian - Accounting |  | `account.chart.template`, `account.move` |
| l10n_id_efaktur | Indonesia E-faktur | `l10n_id_efaktur.efaktur.range` | `account.move`, `res.config.settings`, `res.partner` |
| l10n_id_efaktur_coretax | Indonesia E-faktur (Coretax) | `l10n_id_efaktur_coretax.document`, `l10n_id_efaktur_coretax.product.code`, `l10n_id_efaktur_coretax.uom.code` | `account.move.line`, `account.move`, `product.template`, `res.partner`, `uom.uom` |
| l10n_ie | Ireland - Accounting |  | `account.chart.template` |
| l10n_il | Israel - Accounting |  | `account.chart.template` |
| l10n_in | Indian - Accounting | `l10n_in.port.code` | `account.chart.template`, `account.move`, `account.tax`, `mail.message`, `product.template`, `res.company`, `res.config.settings`, `res.country.state`, `res.partner`, `uom.uom` |
| l10n_in_edi | Indian - E-invoicing |  | `account.edi.format`, `account.move`, `res.company`, `res.config.settings` |
| l10n_in_edi_ewaybill | Indian - E-waybill | `l10n.in.ewaybill.type` | `account.chart.template`, `account.edi.format`, `account.move`, `res.company`, `res.config.settings` |
| l10n_in_ewaybill_port | Indian - Shipping Ports for E-waybill |  | `account.edi.format`, `account.move` |
| l10n_in_ewaybill_stock | Indian - E-waybill Stock | `l10n.in.ewaybill`, `l10n.in.ewaybill.cancel` | `stock.move`, `stock.picking` |
| l10n_in_pos | Indian - Point of Sale |  | `account.move`, `pos.config`, `pos.order`, `pos.session` |
| l10n_in_purchase | Indian - Purchase Report(GST) |  | `account.move`, `purchase.order` |
| l10n_in_purchase_stock | India Purchase and Warehouse Management |  | `account.move`, `stock.move`, `stock.picking` |
| l10n_in_sale | Indian - Sale Report(GST) |  | `sale.advance.payment.inv`, `sale.order` |
| l10n_in_sale_stock | India Sales and Warehouse Management |  | `account.move`, `stock.move`, `stock.picking` |
| l10n_in_stock | Indian - Stock Report(GST) |  | `stock.move`, `stock.picking` |
| l10n_in_withholding | Indian - TDS | `l10n_in.withhold.wizard`, `l10n_in.withhold.wizard.line` | `account.chart.template`, `account.move.line`, `account.move`, `account.payment`, `account.tax`, `res.company`, `res.config.settings` |
| l10n_iq | Iraq - Accounting |  | `account.chart.template` |
| l10n_it | Italy - Accounting |  | `account.chart.template`, `account.report.expression`, `account.tax` |
| l10n_it_edi | Italy - E-invoicing | `l10n_it.ddt` | `account.move.send`, `account.move`, `account_edi_proxy_client.user`, `ir.attachment`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_it_edi_doi | Italy - Declaration of Intent | `l10n_it_edi_doi.declaration_of_intent` | `account.chart.template`, `account.fiscal.position`, `account.move`, `account.tax`, `res.company`, `res.partner`, `sale.order.line`, `sale.order` |
| l10n_it_edi_ndd | Italy - E-invoicing - Additional module to support the debit notes (nota di debito - NDD) | `l10n_it.document.type` | `account.move`, `account.payment.method.line` |
| l10n_it_edi_ndd_account_dn | Italy - E-invoicing - Bridge module between Italy NDD and Account Debit Note |  | `account.move` |
| l10n_it_edi_sale | Italy - Sale E-invoicing |  | `sale.order` |
| l10n_it_edi_website_sale | Italy eCommerce eInvoicing |  |  |
| l10n_it_edi_withholding | Italy - E-invoicing (Withholding) |  | `account.chart.template`, `account.move`, `account.tax` |
| l10n_it_stock_ddt | Italy - Stock DDT |  | `account.move`, `stock.picking.type`, `stock.picking` |
| l10n_jo | Jordan - Accounting |  | `account.chart.template` |
| l10n_jo_edi | Jordan E-Invoicing | `account.edi.xml.ubl_21.jo` | `account.move.send`, `account.move`, `account.tax`, `ir.attachment`, `res.company`, `res.config.settings` |
| l10n_jo_edi_extended | Jordan E-Invoicing Extended Features |  | `account.move.send`, `account.move`, `res.company`, `res.config.settings` |
| l10n_jp | Japan - Accounting |  | `account.chart.template` |
| l10n_jp_ubl_pint | Japan - UBL PINT | `account.edi.xml.pint_jp` | `res.partner` |
| l10n_ke | Kenya - Accounting | `l10n_ke.item.code` | `account.chart.template`, `account.tax`, `res.company` |
| l10n_ke_edi_tremol | Kenya Tremol Device EDI Integration |  | `account.move.send`, `account.move`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_km | Comoros - Accounting |  | `account.chart.template` |
| l10n_kw | Kuwait - Accounting |  | `account.chart.template` |
| l10n_kz | Kazakhstan - Accounting |  | `account.chart.template` |
| l10n_latam_base | LATAM Localization Base | `l10n_latam.identification.type` | `res.company`, `res.partner` |
| l10n_latam_check | Third Party and Deferred/Electronic Checks Management | `l10n_latam.payment.mass.transfer` | `account.chart.template`, `account.journal`, `account.payment.method`, `account.payment.register`, `account.payment` |
| l10n_latam_invoice_document | LATAM Document | `l10n_latam.document.type` | `account.chart.template`, `account.debit.note`, `account.invoice.report`, `account.journal`, `account.move.line`, `account.move.reversal`, `account.move`, `res.company` |
| l10n_lb_account | Lebanon - Accounting |  | `account.chart.template` |
| l10n_lt | Lithuania - Accounting |  | `account.chart.template` |
| l10n_lu | Luxembourg - Accounting |  | `account.chart.template` |
| l10n_lv | Latvia - Accounting |  | `account.chart.template` |
| l10n_ma | Morocco - Accounting |  | `account.chart.template`, `base.document.layout`, `res.partner` |
| l10n_ml | Mali - Accounting |  | `account.chart.template` |
| l10n_mn | Mongolia - Accounting |  | `account.chart.template` |
| l10n_mr | Mauritania - Accounting |  | `account.chart.template` |
| l10n_mt | Malta - Accounting |  | `account.chart.template` |
| l10n_mt_pos | Malta - Point of Sale | `compliance.letter.wizard` |  |
| l10n_mu_account | Mauritius - Accounting |  | `account.chart.template`, `account.move`, `base.document.layout` |
| l10n_mx | Mexico - Accounting |  | `account.account`, `account.chart.template`, `account.tax`, `res.bank`, `res.config.settings`, `res.partner.bank` |
| l10n_mx_hr | Employees - Mexico |  | `hr.employee` |
| l10n_my | Malaysia - Accounting |  | `account.chart.template` |
| l10n_my_edi | Malaysia - E-invoicing | `account.edi.xml.ubl_myinvois_my`, `l10n_my_edi.industry_classification`, `l10n_my_edi.document.status.update` | `account.move.send`, `account.move`, `account.tax`, `account_edi_proxy_client.user`, `product.template`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_my_edi_extended | Malaysia - E-invoicing Extended Features |  | `account.edi.xml.ubl_myinvois_my`, `account.move.line`, `account.move.send`, `account.move`, `res.partner` |
| l10n_my_ubl_pint | Malaysia - UBL PINT | `account.edi.xml.pint_my` | `base.document.layout`, `res.company`, `res.partner` |
| l10n_mz | Mozambique - Accounting |  | `account.chart.template` |
| l10n_ne | Niger - Accounting |  | `account.chart.template` |
| l10n_ng | Nigeria - Accounting |  | `account.chart.template` |
| l10n_nl | Netherlands - Accounting |  | `account.chart.template`, `account.journal` |
| l10n_no | Norway - Accounting |  | `account.chart.template`, `account.journal`, `account.move`, `res.company`, `res.partner` |
| l10n_nz | New Zealand - Accounting |  | `account.chart.template`, `account.move` |
| l10n_pa | Panama - Accounting |  | `account.chart.template` |
| l10n_pe | Peru - Accounting | `l10n_pe.res.city.district` | `account.chart.template`, `account.move.line`, `account.move`, `account.tax`, `l10n_latam.identification.type`, `res.city`, `res.company`, `res.partner` |
| l10n_pe_pos | Peruvian - Point of Sale with Pe Doc |  | `l10n_pe.res.city.district`, `pos.session`, `res.partner` |
| l10n_pe_website_sale | Peruvian eCommerce |  | `website` |
| l10n_ph | Philippines - Accounting | `l10n_ph_2307.wizard` | `account.chart.template`, `account.move`, `account.payment`, `account.tax`, `res.partner` |
| l10n_pk | Pakistan - Accounting |  | `account.chart.template` |
| l10n_pl | Poland - Accounting | `l10n_pl.l10n_pl_tax_office` | `account.chart.template`, `account.move`, `product.template`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_pt | Portugal - Accounting |  | `account.account`, `account.chart.template` |
| l10n_qa | Qatar - Accounting |  | `account.chart.template` |
| l10n_ro | Romania - Accounting |  | `account.chart.template`, `res.partner` |
| l10n_ro_cpv_code | Romania - CPV Code | `l10n_ro.cpv.code` | `account.edi.xml.ubl_ro`, `product.template` |
| l10n_ro_edi | Romania - E-invoicing | `account.edi.xml.ubl_ro` | `res.partner` |
| l10n_ro_edi_stock | Romania - E-Transport |  | `delivery.carrier`, `l10n_ro_edi.document`, `stock.picking` |
| l10n_ro_edi_stock_batch | Romania - E-Transport Batch Pickings |  | `l10n_ro_edi.document`, `stock.picking.batch`, `stock.picking` |
| l10n_ro_efactura | Romania - Send E-Factura | `l10n_ro_edi.document` | `account.move.send`, `account.move`, `res.company`, `res.config.settings` |
| l10n_ro_efactura_synchronize | Romania - Synchronize E-Factura |  | `account.move.send`, `account.move`, `l10n_ro_edi.document`, `res.company`, `res.config.settings` |
| l10n_rs | Serbia - Accounting |  | `account.chart.template`, `account.move` |
| l10n_rs_edi | Serbia - eFaktura E-invoicing | `account.edi.xml.ubl.rs` | `account.move.send`, `account.move`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_rw | Rwanda - Accounting |  | `account.chart.template` |
| l10n_sa | Saudi Arabia - Accounting |  | `account.chart.template`, `account.move` |
| l10n_sa_edi | Saudi Arabia - E-invoicing | `account.edi.xml.ubl_21.zatca`, `l10n_sa_edi.otp.wizard` | `account.chart.template`, `account.debit.note`, `account.edi.document`, `account.edi.format`, `account.journal`, `account.move.line`, `account.move.reversal`, `account.move.send`, `account.move`, `account.tax`, `ir.attachment`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_sa_edi_pos | Saudi Arabia - E-invoicing (Simplified) |  | `account.edi.xml.ubl_21.zatca`, `account.move`, `pos.config` |
| l10n_sa_pos | Saudi Arabia - Point of Sale |  | `pos.config`, `pos.order` |
| l10n_se | Sweden - Accounting |  | `account.chart.template`, `account.journal`, `account.move`, `res.company`, `res.partner` |
| l10n_sg | Singapore - Accounting |  | `account.chart.template`, `account.move`, `res.company`, `res.partner.bank`, `res.partner` |
| l10n_sg_ubl_pint | Singapore - UBL PINT | `account.edi.xml.pint_sg` | `account.move`, `account.tax`, `res.partner` |
| l10n_si | Slovenian - Accounting |  | `account.chart.template` |
| l10n_sk | Slovak - Accounting |  | `account.chart.template`, `account.move`, `base.document.layout`, `res.company` |
| l10n_sn | Sénégal - Accounting |  | `account.chart.template` |
| l10n_syscohada | OHADA - Accounting |  | `account.chart.template` |
| l10n_td | Tchad - Accounting |  | `account.chart.template` |
| l10n_tg | Togo - Accounting |  | `account.chart.template` |
| l10n_th | Thailand - Accounting |  | `account.chart.template`, `account.move`, `ir.actions.report`, `res.partner.bank`, `res.partner` |
| l10n_tn | Tunisia - Accounting |  | `account.chart.template` |
| l10n_tr | Türkiye - Accounting |  | `account.chart.template` |
| l10n_tr_nilvera | Türkiye - Nilvera | `l10n_tr.nilvera.alias` | `account.journal`, `res.company`, `res.config.settings`, `res.partner`, `uom.uom` |
| l10n_tr_nilvera_edispatch | Türkiye - e-Irsaliye (e-Dispatch) | `l10n_tr.nilvera.trailer.plate` | `res.partner`, `stock.picking.type`, `stock.picking` |
| l10n_tr_nilvera_einvoice | Türkiye - Nilvera E-Invoice | `account.edi.xml.ubl.tr` | `account.journal`, `account.move.send`, `account.move`, `res.partner.category` |
| l10n_tw | Taiwan - Accounting |  | `account.chart.template` |
| l10n_tz_account | Tanzania - Accounting |  | `account.chart.template` |
| l10n_ua | Ukraine - Accounting |  | `account.chart.template` |
| l10n_ug | Uganda - Accounting |  | `account.chart.template` |
| l10n_uk | United Kingdom - Accounting |  | `account.chart.template` |
| l10n_us | United States - Accounting |  | `res.partner.bank` |
| l10n_uy | Uruguay - Accounting |  | `account.chart.template`, `account.move`, `account.tax`, `l10n_latam.document.type`, `l10n_latam.identification.type`, `res.company`, `res.partner` |
| l10n_uy_website_sale | Uruguay Website |  | `website` |
| l10n_ve | Venezuela - Accounting |  | `account.chart.template` |
| l10n_vn | Vietnam - Accounting |  | `account.chart.template`, `res.partner.bank` |
| l10n_vn_edi_viettel | Vietnam - E-invoicing | `l10n_vn_edi_viettel.sinvoice.template`, `l10n_vn_edi_viettel.sinvoice.symbol`, `l10n_vn_edi_viettel.cancellation` | `account.move.reversal`, `account.move.send`, `account.move`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_za | South Africa - Accounting |  | `account.chart.template` |
| l10n_zm_account | Zambia - Accounting |  | `account.chart.template`, `account.move` |
| link_tracker | Link Tracker | `link.tracker`, `link.tracker.code`, `link.tracker.click` | `mail.render.mixin`, `utm.campaign` |
| loyalty | Coupons & Loyalty | `loyalty.card`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `loyalty.generate.wizard` | `product.pricelist`, `product.product`, `product.template`, `res.partner` |
| lunch | Lunch | `lunch.alert`, `lunch.cashmove`, `lunch.location`, `lunch.order`, `lunch.product`, `lunch.product.category`, `lunch.supplier`, `lunch.topping`, `lunch.cashmove.report` | `lunch.alert`, `lunch.location`, `lunch.order`, `lunch.product.category`, `lunch.product`, `lunch.supplier`, `res.company`, `res.config.settings`, `res.users` |
| mail | Discuss | `discuss.channel`, `discuss.channel.member`, `discuss.channel.rtc.session`, `discuss.gif.favorite`, `discuss.voice.metadata`, `mail.guest`, `fetchmail.server`, `mail.activity`, `mail.activity.mixin`, `mail.activity.plan`, `mail.activity.plan.template`, `mail.activity.type`, `mail.alias`, `mail.alias.domain`, `mail.alias.mixin`, `mail.alias.mixin.optional`, `mail.blacklist`, `mail.composer.mixin`, `mail.followers`, `mail.gateway.allowed`, `mail.ice.server`, `mail.link.preview`, `mail.mail`, `mail.message`, `mail.message.reaction`, `mail.message.schedule`, `mail.message.subtype`, `mail.message.translation`, `mail.notification`, `mail.render.mixin`, `mail.shortcode`, `mail.template`, `mail.thread`, `mail.thread.blacklist`, `mail.thread.cc`, `mail.thread.main.attachment`, `mail.tracking.duration.mixin`, `mail.tracking.value`, `mail.partner.device`, `res.users.settings.volumes`, `template.reset.mixin`, `publisher_warranty.contract`, `mail.notification.web.push`, `mail.activity.schedule`, `mail.blacklist.remove`, `mail.compose.message`, `mail.resend.message`, `mail.resend.partner`, `mail.template.preview`, `mail.template.reset`, `mail.wizard.invite` | `base.module.uninstall`, `base.partner.merge.automatic.wizard`, `base`, `bus.presence`, `discuss.channel.member`, `discuss.channel`, `ir.actions.act_window.view`, `ir.actions.server`, `ir.attachment`, `ir.config_parameter`, `ir.http`, `ir.mail_server`, `ir.model.fields`, `ir.model`, `ir.qweb`, `ir.ui.view`, `ir.websocket`, `mail.message`, `mail.notification`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users.settings`, `res.users` |
| mail_bot | OdooBot | `mail.bot` | `discuss.channel`, `ir.http`, `mail.thread`, `res.users` |
| mail_bot_hr | OdooBot - HR |  |  |
| mail_group | Mail Group | `mail.group`, `mail.group.member`, `mail.group.message`, `mail.group.moderation`, `mail.group.message.reject` |  |
| mail_plugin | Mail Plugin | `res.partner.iap` | `ir.http`, `res.partner` |
| maintenance | Maintenance | `maintenance.stage`, `maintenance.equipment.category`, `maintenance.mixin`, `maintenance.equipment`, `maintenance.request`, `maintenance.team` | `res.config.settings` |
| mass_mailing | Email Marketing | `mailing.mailing`, `mailing.contact`, `mailing.filter`, `mailing.list`, `mailing.subscription`, `mailing.subscription.optout`, `mailing.trace`, `mailing.trace.report`, `mailing.contact.import`, `mailing.contact.to.list`, `mailing.list.merge`, `mailing.mailing.schedule.date`, `mailing.mailing.test` | `ir.http`, `ir.mail_server`, `ir.model`, `link.tracker.click`, `link.tracker`, `mail.blacklist`, `mail.compose.message`, `mail.mail`, `mail.render.mixin`, `mail.thread`, `res.company`, `res.config.settings`, `res.partner`, `res.users`, `utm.campaign`, `utm.medium`, `utm.source` |
| mass_mailing_crm | Mass mailing on lead / opportunities |  | `crm.lead`, `mailing.mailing`, `utm.campaign` |
| mass_mailing_crm_sms | Mass mailing sms on lead / opportunities |  | `utm.campaign` |
| mass_mailing_event | Mass mailing on attendees |  | `event.event`, `event.registration` |
| mass_mailing_event_sms | Event Attendees SMS Marketing |  | `event.event` |
| mass_mailing_event_track | Mass mailing on track speakers |  | `event.event`, `event.track` |
| mass_mailing_event_track_sms | Track Speakers SMS Marketing |  | `event.event` |
| mass_mailing_sale | Mass mailing on sale orders |  | `mailing.mailing`, `sale.order`, `utm.campaign` |
| mass_mailing_sale_sms | Mass mailing sms on sale orders |  | `utm.campaign` |
| mass_mailing_slides | Mass mailing on course members |  | `slide.channel` |
| mass_mailing_sms | SMS Marketing | `mailing.sms.test` | `mailing.contact`, `mailing.list`, `mailing.mailing`, `mailing.trace`, `res.users`, `sms.composer`, `sms.sms`, `sms.tracker`, `utm.campaign`, `utm.medium` |
| mass_mailing_themes | Mass Mailing Themes |  |  |
| membership | Members | `membership.membership_line`, `report.membership`, `membership.invoice` | `account.move.line`, `account.move`, `product.template`, `res.partner` |
| microsoft_account | Microsoft Users | `microsoft.service` | `res.users` |
| microsoft_calendar | Outlook Calendar | `microsoft.calendar.credentials`, `microsoft.calendar.sync`, `microsoft.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.recurrence`, `res.config.settings`, `res.users` |
| microsoft_outlook | Microsoft Outlook | `microsoft.outlook.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings` |
| mrp | Manufacturing | `mrp.bom`, `mrp.bom.line`, `mrp.bom.byproduct`, `mrp.document`, `mrp.production`, `mrp.routing.workcenter`, `mrp.unbuild`, `mrp.workcenter`, `mrp.workcenter.tag`, `mrp.workcenter.productivity.loss.type`, `mrp.workcenter.productivity.loss`, `mrp.workcenter.productivity`, `mrp.workcenter.capacity`, `mrp.workorder`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `change.production.qty`, `mrp.consumption.warning`, `mrp.consumption.warning.line`, `mrp.production.backorder.line`, `mrp.production.backorder`, `mrp.production.split.multi`, `mrp.production.split`, `mrp.production.split.line`, `stock.warn.insufficient.qty.unbuild` | `mrp.bom.byproduct`, `mrp.bom.line`, `mrp.bom`, `mrp.production`, `mrp.routing.workcenter`, `mrp.workcenter`, `picking.label.type`, `procurement.group`, `product.product`, `product.replenish`, `product.template`, `report.stock.report_reception`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `stock.assign.serial`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.quant`, `stock.rule`, `stock.scrap`, `stock.traceability.report`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_account | Accounting - MRP |  | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.line`, `account.move.line`, `mrp.bom`, `mrp.production`, `mrp.routing.workcenter`, `mrp.workcenter`, `mrp.workorder`, `product.category`, `product.product`, `product.template`, `report.mrp.report_mo_overview`, `stock.move`, `stock.rule` |
| mrp_landed_costs | Landed Costs On MO |  | `stock.landed.cost` |
| mrp_product_expiry | Manufacturing Expiry |  | `expiry.picking.confirmation`, `mrp.production` |
| mrp_repair | Mrp Repairs |  | `repair.order`, `stock.move` |
| mrp_subcontracting | MRP Subcontracting |  | `change.production.qty`, `mrp.bom`, `mrp.consumption.warning`, `mrp.production`, `product.product`, `product.replenish`, `product.supplierinfo`, `report.mrp.report_bom_structure`, `res.company`, `res.partner`, `stock.location`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.return.picking`, `stock.rule`, `stock.warehouse` |
| mrp_subcontracting_account | Subcontracting Management with Stock Valuation |  | `mrp.production`, `product.product`, `stock.move`, `stock.picking` |
| mrp_subcontracting_dropshipping | Dropship and Subcontracting Management |  | `product.replenish`, `purchase.order`, `res.company`, `stock.move`, `stock.picking`, `stock.rule`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_subcontracting_purchase | Purchase and Subcontracting Management |  | `account.move.line`, `purchase.order`, `report.mrp.report_bom_structure`, `stock.move`, `stock.picking`, `stock.rule`, `stock.valuation.layer` |
| mrp_subcontracting_repair | MRP Subcontracting Repair |  |  |
| mrp_subonctracting_landed_costs | Landed Costs With Subcontracting order |  |  |
| onboarding | Onboarding Toolbox | `onboarding.onboarding`, `onboarding.onboarding.step`, `onboarding.progress`, `onboarding.progress.step` | `res.company` |
| partner_autocomplete | Partner Autocomplete | `iap.autocomplete.api`, `res.partner.autocomplete.sync` | `ir.http`, `res.company`, `res.config.settings`, `res.partner` |
| payment | Payment Engine | `payment.method`, `payment.provider`, `payment.token`, `payment.transaction`, `payment.capture.wizard`, `payment.link.wizard`, `payment.provider.onboarding.wizard` | `ir.http`, `onboarding.onboarding.step`, `res.company`, `res.partner` |
| payment_adyen | Payment Provider: Adyen |  | `payment.capture.wizard`, `payment.provider`, `payment.token`, `payment.transaction` |
| payment_alipay | Payment Provider: Alipay |  | `payment.provider`, `payment.transaction` |
| payment_aps | Payment Provider: Amazon Payment Services |  | `payment.provider`, `payment.transaction` |
| payment_asiapay | Payment Provider: AsiaPay |  | `payment.provider`, `payment.transaction` |
| payment_authorize | Payment Provider: Authorize.Net |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_buckaroo | Payment Provider: Buckaroo |  | `payment.provider`, `payment.transaction` |
| payment_custom | Payment Provider: Custom Payment Modes |  | `payment.provider`, `payment.transaction` |
| payment_demo | Payment Provider: Demo |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_flutterwave | Payment Provider: Flutterwave |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_mercado_pago | Payment Provider: Mercado Pago |  | `payment.provider`, `payment.transaction` |
| payment_mollie | Payment Provider: Mollie |  | `payment.provider`, `payment.transaction` |
| payment_ogone | Payment Provider: Ogone |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_paypal | Payment Provider: Paypal |  | `payment.provider`, `payment.transaction` |
| payment_payulatam | Payment Provider: PayU Latam |  | `payment.provider`, `payment.transaction` |
| payment_payumoney | Payment Provider: PayUmoney |  | `payment.provider`, `payment.transaction` |
| payment_razorpay | Payment Provider: Razorpay |  | `payment.provider`, `payment.transaction` |
| payment_razorpay_oauth | Razorpay OAuth Integration |  | `payment.provider` |
| payment_sips | Payment Provider: Worldline SIPS |  | `payment.provider`, `payment.transaction` |
| payment_stripe | Payment Provider: Stripe |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_worldline | Payment Provider: Worldline |  | `payment.provider`, `payment.transaction` |
| payment_xendit | Payment Provider: Xendit |  | `payment.provider`, `payment.transaction` |
| phone_validation | Phone Numbers Validation | `mail.thread.phone`, `phone.blacklist`, `phone.blacklist.remove` | `base`, `res.partner`, `res.users` |
| point_of_sale | Point of Sale | `pos.bill`, `pos.category`, `pos.combo`, `pos.combo.line`, `pos.config`, `pos.order`, `pos.order.line`, `pos.pack.operation.lot`, `pos.payment`, `pos.payment.method`, `pos.printer`, `pos.session`, `report.point_of_sale.report_saledetails`, `report.point_of_sale.report_invoice`, `report.pos.order`, `pos.close.session.wizard`, `pos.daily.sales.reports.wizard`, `pos.details.wizard`, `pos.make.payment` | `account.bank.statement.line`, `account.cash.rounding`, `account.chart.template`, `account.fiscal.position`, `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.tax`, `barcode.rule`, `digest.digest`, `procurement.group`, `product.attribute.custom.value`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.rule`, `stock.warehouse`, `uom.category`, `uom.uom` |
| portal | Customer Portal | `portal.mixin`, `portal.share`, `portal.wizard`, `portal.wizard.user` | `ir.http`, `ir.qweb`, `ir.ui.view`, `mail.message`, `mail.thread`, `res.config.settings`, `res.partner`, `res.users.apikeys.description` |
| portal_rating | Portal Rating |  | `ir.http`, `mail.message`, `rating.rating` |
| pos_adyen | POS Adyen |  | `pos.config`, `pos.payment.method`, `pos.session`, `res.config.settings` |
| pos_discount | Point of Sale Discounts |  | `pos.config`, `pos.session`, `res.config.settings` |
| pos_epson_printer | POS Epson Printer |  | `pos.config`, `pos.printer`, `pos.session`, `res.config.settings` |
| pos_hr | POS - HR |  | `hr.employee`, `pos.config`, `pos.order`, `pos.session`, `report.pos.order`, `res.config.settings` |
| pos_hr_restaurant | POS HR Restaurant |  |  |
| pos_loyalty | Point of Sale - Coupons & Loyalty |  | `barcode.rule`, `loyalty.card`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.config.settings` |
| pos_mercado_pago | POS Mercado Pago |  | `pos.payment.method`, `pos.session` |
| pos_mercury | Vantiv Payment Services | `pos_mercury.configuration`, `pos_mercury.mercury_transaction` | `barcode.rule`, `pos.order`, `pos.payment.method`, `pos.payment`, `pos.session` |
| pos_mrp | pos_mrp |  | `pos.order.line`, `pos.order`, `stock.move` |
| pos_online_payment | Point of Sale online payment |  | `account.payment`, `payment.transaction`, `pos.config`, `pos.order`, `pos.payment.method`, `pos.payment`, `pos.session` |
| pos_online_payment_self_order | POS Self-Order / Online Payment |  | `pos.config`, `pos.order`, `res.config.settings` |
| pos_paytm | POS PayTM |  | `pos.order`, `pos.payment.method`, `pos.payment` |
| pos_razorpay | POS Razorpay |  | `pos.order`, `pos.payment.method`, `pos.payment` |
| pos_restaurant | Restaurant | `restaurant.floor`, `restaurant.table` | `pos.config`, `pos.order.line`, `pos.order`, `pos.payment`, `pos.session`, `res.config.settings` |
| pos_restaurant_adyen | POS Restaurant Adyen |  | `pos.order`, `pos.payment.method`, `pos.payment`, `pos.session` |
| pos_restaurant_loyalty | POS - Restaurant Loyality |  |  |
| pos_restaurant_stripe | POS Restaurant Stripe |  | `pos.order`, `pos.payment` |
| pos_sale | POS - Sales |  | `crm.team`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.config.settings`, `sale.order.line`, `sale.order`, `sale.report`, `stock.picking` |
| pos_sale_loyalty | POS - Sales Loyality |  | `sale.order.line` |
| pos_sale_margin | POS - Sale Margin |  | `sale.report` |
| pos_sale_product_configurator | POS - Sale Product Configurator |  | `pos.session`, `product.product` |
| pos_self_order | POS Self Order | `pos_self_order.custom_link` | `ir.http`, `pos.config`, `pos.order.line`, `pos.order`, `pos.payment.method`, `pos.session`, `product.product`, `product.template`, `res.config.settings`, `restaurant.table` |
| pos_self_order_adyen | POS Self Order Adyen |  | `pos.payment.method` |
| pos_self_order_epson_printer | POS Self Order Epson Printer |  | `pos.config` |
| pos_self_order_sale | POS Self Order Sale |  | `product.product`, `res.config.settings` |
| pos_self_order_stripe | POS Self Order Stripe |  | `pos.payment.method` |
| pos_six | POS Six |  | `pos.config`, `pos.payment.method`, `pos.session` |
| pos_stripe | POS Stripe |  | `pos.payment.method`, `pos.session` |
| pos_viva_wallet | POS Viva Wallet |  | `pos.payment.method`, `pos.session` |
| privacy_lookup | Privacy | `privacy.log`, `privacy.lookup.wizard`, `privacy.lookup.wizard.line` | `res.partner` |
| product | Products & Pricelists | `product.attribute`, `product.attribute.custom.value`, `product.attribute.value`, `product.catalog.mixin`, `product.category`, `product.document`, `product.packaging`, `product.pricelist`, `product.pricelist.item`, `product.product`, `product.supplierinfo`, `product.tag`, `product.template`, `product.template.attribute.exclusion`, `product.template.attribute.line`, `product.template.attribute.value`, `report.product.report_producttemplatelabel2x7`, `report.product.report_producttemplatelabel4x7`, `report.product.report_producttemplatelabel4x12`, `report.product.report_producttemplatelabel4x12noprice`, `report.product.report_producttemplatelabel_dymo`, `report.product.report_pricelist`, `product.label.layout` | `decimal.precision`, `ir.attachment`, `product.attribute.value`, `product.attribute`, `product.category`, `product.pricelist.item`, `product.pricelist`, `product.product`, `product.supplierinfo`, `product.template.attribute.exclusion`, `product.template.attribute.value`, `product.template`, `res.company`, `res.config.settings`, `res.country.group`, `res.currency`, `res.partner`, `uom.uom` |
| product_email_template | Product Email Template |  | `account.move`, `product.template` |
| product_expiry | Products Expiration Date | `expiry.picking.confirmation` | `procurement.group`, `product.product`, `product.template`, `res.config.settings`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant` |
| product_images | Product Images | `product.fetch.image.wizard` | `ir.cron.trigger`, `product.product`, `res.config.settings` |
| product_margin | Margins by Products | `product.margin` | `product.product` |
| product_matrix | Product Matrix |  | `product.template.attribute.value`, `product.template` |
| project | Project | `project.collaborator`, `project.milestone`, `project.project`, `project.project.stage`, `project.tags`, `project.task`, `project.task.recurrence`, `project.task.stage.personal`, `project.task.type`, `project.update`, `report.project.task.user`, `project.task.burndown.chart.report`, `project.project.stage.delete.wizard`, `project.share.wizard`, `project.task.type.delete.wizard` | `account.analytic.account`, `digest.digest`, `ir.ui.menu`, `mail.message`, `project.project`, `project.task.type`, `project.task`, `res.config.settings`, `res.partner` |
| project_account | Project - Account |  | `project.project` |
| project_hr_expense | Project Expenses |  | `hr.expense`, `project.project` |
| project_mail_plugin | Project Mail Plugin |  |  |
| project_mrp | MRP Project |  | `mrp.production`, `project.project` |
| project_purchase | Project Purchase |  | `project.project`, `purchase.order.line` |
| project_sale_expense | Project - Sale - Expense |  | `project.project` |
| project_sms | Project - SMS |  | `project.project.stage`, `project.project`, `project.task.type`, `project.task` |
| project_timesheet_holidays | Timesheet when on Time Off |  | `account.analytic.line`, `hr.employee`, `hr.leave.type`, `hr.leave`, `project.task`, `res.company`, `res.config.settings`, `resource.calendar.leaves` |
| project_todo | To-Do | `mail.activity.todo.create` | `mail.activity.type`, `project.task` |
| purchase | Purchase | `purchase.order`, `purchase.order.line`, `purchase.bill.union`, `purchase.report` | `account.analytic.account`, `account.analytic.applicability`, `account.move.line`, `account.move`, `account.tax`, `product.packaging`, `product.product`, `product.supplierinfo`, `product.template`, `purchase.order.line`, `purchase.order`, `res.company`, `res.config.settings`, `res.partner` |
| purchase_mrp | Purchase and MRP Management |  | `account.move.line`, `mrp.bom.line`, `mrp.bom`, `mrp.production`, `purchase.order.line`, `purchase.order`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `stock.move` |
| purchase_product_matrix | Purchase Matrix |  | `purchase.order.line`, `purchase.order` |
| purchase_requisition | Purchase Agreements | `purchase.order.group`, `purchase.requisition.type`, `purchase.requisition`, `purchase.requisition.line`, `purchase.requisition.alternative.warning`, `purchase.requisition.create.alternative` | `product.product`, `product.supplierinfo`, `purchase.order.line`, `purchase.order` |
| purchase_requisition_sale | Purchase Requisition Sale |  | `purchase.requisition.create.alternative` |
| purchase_requisition_stock | Purchase Requisition Stock |  | `purchase.order.line`, `purchase.order`, `purchase.requisition.create.alternative`, `purchase.requisition.line`, `purchase.requisition`, `stock.move`, `stock.rule`, `stock.warehouse.orderpoint` |
| purchase_stock | Purchase Stock | `vendor.delay.report` | `account.move.line`, `account.move`, `procurement.group`, `product.category`, `product.product`, `product.replenish`, `product.supplierinfo`, `product.template`, `purchase.order.line`, `purchase.order`, `purchase.report`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.partner`, `stock.forecasted_product_product`, `stock.lot`, `stock.move`, `stock.picking`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.return.picking`, `stock.rule`, `stock.valuation.layer`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| rating | Customer Rating | `rating.rating`, `rating.mixin`, `rating.parent.mixin` | `mail.message`, `mail.thread` |
| repair | Repairs | `repair.order`, `repair.tags`, `repair.warn.uncomplete.move`, `stock.warn.insufficient.qty.repair` | `mail.compose.message`, `product.product`, `product.template`, `sale.order.line`, `sale.order`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `stock.warehouse` |
| resource | Resource | `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `resource.mixin`, `resource.resource` | `res.company`, `res.users`, `resource.calendar` |
| sale | Sales | `sale.order`, `sale.order.line`, `sale.report`, `sale.mass.cancel.orders`, `sale.payment.provider.onboarding.wizard`, `sale.advance.payment.inv`, `sale.order.cancel`, `sale.order.discount` | `account.analytic.applicability`, `account.analytic.line`, `account.invoice.report`, `account.move.line`, `account.move`, `account.payment.register`, `crm.team`, `ir.config_parameter`, `onboarding.onboarding.step`, `onboarding.onboarding`, `payment.link.wizard`, `payment.provider`, `payment.transaction`, `product.attribute.custom.value`, `product.attribute.value`, `product.attribute`, `product.document`, `product.packaging`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `sale.order.line`, `sale.order`, `utm.campaign` |
| sale_async_emails | Sales - Async Emails |  | `sale.order` |
| sale_crm | Opportunity to Quotation | `crm.quotation.partner` | `crm.lead`, `crm.team`, `res.users`, `sale.order` |
| sale_expense | Sales Expense |  | `account.move.line`, `account.move`, `hr.expense.sheet`, `hr.expense.split`, `hr.expense`, `product.template`, `sale.order` |
| sale_expense_margin | Sales Expense Margin |  | `account.move.line`, `sale.order.line` |
| sale_loyalty | Sale Loyalty | `sale.order.coupon.points`, `sale.loyalty.coupon.wizard`, `sale.loyalty.reward.wizard` | `loyalty.card`, `loyalty.program`, `loyalty.reward`, `sale.order.line`, `sale.order` |
| sale_loyalty_delivery | Sale Loyalty - Delivery |  | `loyalty.program`, `loyalty.reward`, `sale.order` |
| sale_management | Sales | `sale.order.option`, `sale.order.template`, `sale.order.template.line`, `sale.order.template.option` | `digest.digest`, `res.company`, `res.config.settings`, `sale.order.line`, `sale.order` |
| sale_margin | Margins in Sales Orders |  | `sale.order.line`, `sale.order`, `sale.report` |
| sale_mrp | Sales and MRP Management |  | `account.move.line`, `mrp.bom`, `mrp.production`, `sale.order.line`, `sale.order`, `stock.move.line`, `stock.move` |
| sale_mrp_margin | Sale Mrp Margin |  |  |
| sale_pdf_quote_builder | Sales PDF Quotation Builder |  | `ir.actions.report`, `product.document`, `res.company`, `res.config.settings`, `sale.order.template`, `sale.order` |
| sale_product_configurator | Sale Product Configurator |  | `product.template`, `sale.order.line` |
| sale_product_matrix | Sale Matrix |  | `product.template`, `sale.order.line`, `sale.order` |
| sale_project | Sales - Project |  | `account.move.line`, `product.product`, `product.template`, `project.milestone`, `project.project`, `project.task.recurrence`, `project.task`, `report.project.task.user`, `res.config.settings`, `sale.order.line`, `sale.order.template.line`, `sale.order` |
| sale_project_stock | Sale Project - Sale Stock |  | `sale.order.line` |
| sale_purchase | Sale Purchase |  | `product.template`, `purchase.order.line`, `purchase.order`, `sale.order.cancel`, `sale.order.line`, `sale.order` |
| sale_purchase_stock | MTO Sale <-> Purchase |  | `purchase.order`, `sale.order` |
| sale_service | Sales - Service |  | `sale.order.line` |
| sale_sms | Sale - SMS |  |  |
| sale_stock | Sales and Warehouse Management |  | `account.move.line`, `account.move`, `procurement.group`, `product.template`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.users`, `sale.order.cancel`, `sale.order.line`, `sale.order`, `sale.report`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.route`, `stock.rule`, `stock.rules.report`, `stock.valuation.layer` |
| sale_stock_margin | Sale Stock Margin |  | `sale.order.line` |
| sale_timesheet | Sales Timesheet | `project.sale.line.employee.map`, `project.create.invoice`, `project.create.sale.order`, `project.create.sale.order.line` | `account.analytic.line`, `account.move.line`, `account.move.reversal`, `account.move`, `hr.employee`, `product.product`, `product.template`, `project.project`, `project.task.recurrence`, `project.task`, `project.update`, `report.project.task.user`, `res.config.settings`, `sale.advance.payment.inv`, `sale.order.line`, `sale.order`, `timesheets.analysis.report` |
| sale_timesheet_margin | Service Margins in Sales Orders |  | `sale.order.line` |
| sales_team | Sales Teams | `crm.tag`, `crm.team`, `crm.team.member` | `res.partner`, `res.users` |
| sms | SMS gateway | `sms.sms`, `sms.template`, `sms.tracker`, `sms.composer`, `sms.resend.recipient`, `sms.resend`, `sms.template.preview`, `sms.template.reset` | `base`, `ir.actions.server`, `ir.model`, `mail.followers`, `mail.message`, `mail.notification`, `mail.thread`, `res.company`, `res.partner` |
| sms_twilio | Twilio SMS | `sms.twilio.number`, `sms.twilio.account.manage` | `mail.notification`, `res.company`, `res.config.settings`, `sms.composer`, `sms.sms`, `sms.tracker` |
| snailmail | Snail Mail | `snailmail.letter`, `snailmail.letter.format.error`, `snailmail.letter.missing.required.fields` | `ir.actions.report`, `mail.message`, `mail.notification`, `mail.thread`, `res.company`, `res.config.settings`, `res.partner` |
| snailmail_account | Snail Mail - Account |  | `account.move.send`, `account.move`, `res.company`, `res.config.settings` |
| social_media | Social Media |  | `res.company` |
| spreadsheet | Spreadsheet | `spreadsheet.mixin` | `res.currency.rate`, `res.currency`, `res.lang` |
| spreadsheet_account | Spreadsheet Accounting Formulas |  | `account.account`, `res.company` |
| spreadsheet_dashboard | Spreadsheet dashboard | `spreadsheet.dashboard`, `spreadsheet.dashboard.group`, `spreadsheet.dashboard.share` |  |
| spreadsheet_dashboard_account | Spreadsheet dashboard for accounting |  |  |
| spreadsheet_dashboard_event_sale | Spreadsheet dashboard for events |  |  |
| spreadsheet_dashboard_hr_expense | Spreadsheet dashboard for expenses |  |  |
| spreadsheet_dashboard_hr_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_im_livechat | Spreadsheet dashboard for live chat |  |  |
| spreadsheet_dashboard_pos_hr | Spreadsheet dashboard for point of sale |  |  |
| spreadsheet_dashboard_purchase | Spreadsheet dashboard for purchases |  |  |
| spreadsheet_dashboard_purchase_stock | Spreadsheet dashboard for purchases |  |  |
| spreadsheet_dashboard_sale | Spreadsheet dashboard for sales |  |  |
| spreadsheet_dashboard_sale_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_stock_account | Spreadsheet dashboard for stock |  |  |
| spreadsheet_dashboard_website_sale | Spreadsheet dashboard for eCommerce |  |  |
| spreadsheet_dashboard_website_sale_slides | Spreadsheet dashboard for eLearning |  |  |
| stock | Inventory | `product.removal`, `stock.putaway.rule`, `stock.location`, `stock.route`, `stock.lot`, `stock.move`, `stock.move.line`, `stock.warehouse.orderpoint`, `stock.package_level`, `stock.package.type`, `stock.picking.type`, `stock.picking`, `stock.quant`, `stock.quant.package`, `stock.rule`, `procurement.group`, `stock.scrap`, `stock.storage.category`, `stock.storage.category.capacity`, `stock.warehouse`, `report.stock.label_product_product_view`, `report.stock.label_lot_template_view`, `report.stock.quantity`, `report.stock.report_reception`, `report.stock.report_stock_rule`, `stock.forecasted_product_product`, `stock.forecasted_product_template`, `stock.traceability.report`, `product.replenish`, `stock.assign.serial`, `stock.backorder.confirmation.line`, `stock.backorder.confirmation`, `stock.change.product.qty`, `stock.inventory.adjustment.name`, `stock.inventory.conflict`, `stock.inventory.warning`, `picking.label.type`, `lot.label.layout`, `stock.orderpoint.snooze`, `stock.package.destination`, `stock.return.picking.line`, `stock.return.picking`, `stock.quant.relocate`, `stock.quantity.history`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.request.count`, `stock.rules.report`, `stock.scheduler.compute`, `stock.track.confirmation`, `stock.track.line`, `stock.warn.insufficient.qty`, `stock.warn.insufficient.qty.scrap` | `barcode.rule`, `ir.actions.report`, `product.category`, `product.label.layout`, `product.packaging`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `res.users`, `stock.location`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.putaway.rule`, `stock.quant`, `stock.storage.category`, `stock.warehouse.orderpoint`, `stock.warehouse`, `uom.uom` |
| stock_account | WMS Accounting | `stock.valuation.layer`, `stock.valuation.layer.revaluation` | `account.analytic.account`, `account.analytic.plan`, `account.chart.template`, `account.move.line`, `account.move`, `product.category`, `product.product`, `product.template`, `res.config.settings`, `stock.forecasted_product_product`, `stock.location`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.quantity.history`, `stock.request.count`, `stock.return.picking.line`, `stock.return.picking` |
| stock_delivery | Delivery - Stock | `choose.delivery.package` | `choose.delivery.carrier`, `delivery.carrier`, `product.template`, `sale.order.line`, `sale.order`, `stock.move.line`, `stock.move`, `stock.package.type`, `stock.picking`, `stock.quant.package`, `stock.return.picking`, `stock.route` |
| stock_dropshipping | Drop Shipping |  | `procurement.group`, `product.replenish`, `purchase.order.line`, `purchase.order`, `res.company`, `sale.order.line`, `sale.order`, `stock.lot`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.rule` |
| stock_landed_costs | WMS Landed Costs | `stock.landed.cost`, `stock.landed.cost.lines`, `stock.valuation.adjustment.lines` | `account.move.line`, `account.move`, `product.template`, `purchase.order.line`, `res.company`, `res.config.settings`, `stock.valuation.layer` |
| stock_landed_costs_company | Landed Costs for company's branches |  | `stock.landed.cost` |
| stock_picking_batch | Warehouse Management: Batch Transfer | `stock.picking.batch`, `stock.add.to.wave`, `stock.picking.to.batch` | `stock.move.line`, `stock.move`, `stock.package.destination`, `stock.picking.type`, `stock.picking`, `stock.warehouse` |
| stock_sms | Stock - SMS | `confirm.stock.sms` | `res.company`, `res.config.settings`, `stock.picking` |
| survey | Surveys | `survey.question`, `survey.question.answer`, `survey.survey`, `survey.user_input`, `survey.user_input.line`, `survey.invite` | `gamification.badge`, `gamification.challenge`, `ir.http`, `res.partner`, `survey.survey` |
| transifex | Transifex integration | `transifex.code.translation`, `transifex.translation` | `base` |
| uom | Units of measure | `uom.category`, `uom.uom` |  |
| utm | UTM Trackers | `utm.campaign`, `utm.medium`, `utm.mixin`, `utm.source`, `utm.source.mixin`, `utm.stage`, `utm.tag` | `ir.http` |
| web | Web | `base.document.layout` | `base`, `ir.http`, `ir.model`, `ir.qweb.field.image_url`, `ir.qweb.field.image`, `ir.ui.menu`, `res.company`, `res.config.settings`, `res.partner`, `res.users` |
| web_editor | Web Editor | `web_editor.assets`, `html.field.history.mixin`, `web_editor.converter.test`, `web_editor.converter.test.sub` | `base`, `ir.attachment`, `ir.http`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.duration`, `ir.qweb.field.float`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.integer`, `ir.qweb.field.many2one`, `ir.qweb.field.monetary`, `ir.qweb.field.qweb`, `ir.qweb.field.relative`, `ir.qweb.field.selection`, `ir.qweb.field.text`, `ir.qweb.field`, `ir.qweb`, `ir.ui.view`, `ir.websocket` |
| web_hierarchy | Web Hierarchy |  | `base`, `ir.actions.act_window.view`, `ir.ui.view` |
| web_tour | Tours | `web_tour.tour` | `ir.http` |
| web_unsplash | Unsplash Image Library |  | `ir.qweb.field.image`, `res.config.settings`, `res.users` |
| website | Website | `ir.module.module`, `website.seo.metadata`, `website.cover_properties.mixin`, `website.multi.mixin`, `website.published.mixin`, `website.published.multi.mixin`, `website.searchable.mixin`, `theme.ir.asset`, `theme.ir.ui.view`, `theme.ir.attachment`, `theme.website.menu`, `theme.website.page`, `theme.utils`, `website`, `website.configurator.feature`, `website.controller.page`, `website.menu`, `website.page`, `website.route`, `website.rewrite`, `website.snippet.filter`, `website.track`, `website.visitor`, `website.robots` | `base.language.install`, `base.partner.merge.automatic.wizard`, `base`, `ir.actions.server`, `ir.asset`, `ir.attachment`, `ir.binary`, `ir.http`, `ir.model.data`, `ir.model.fields`, `ir.model`, `ir.qweb.field.contact`, `ir.qweb.field.html`, `ir.qweb`, `ir.rule`, `ir.ui.menu`, `ir.ui.view`, `portal.wizard.user`, `res.company`, `res.config.settings`, `res.lang`, `res.partner`, `res.users`, `web_editor.assets`, `website.menu`, `website.page`, `website` |
| website_blog | Blog | `blog.blog`, `blog.tag.category`, `blog.tag`, `blog.post` | `ir.qweb.field`, `website.snippet.filter`, `website` |
| website_cf_turnstile | Cloudflare Turnstile |  | `ir.http`, `res.config.settings` |
| website_crm | Contact Form |  | `crm.lead`, `website.visitor`, `website` |
| website_crm_iap_reveal | Lead Generation From Website Visits | `crm.reveal.rule`, `crm.reveal.view` | `crm.lead`, `ir.http` |
| website_crm_livechat | Lead Livechat Sessions |  | `chatbot.script.step`, `crm.lead`, `discuss.channel` |
| website_crm_partner_assign | Resellers | `res.partner.activation`, `res.partner.grade`, `crm.partner.report.assign`, `crm.lead.forward.to.partner`, `crm.lead.assignation` | `crm.lead`, `res.partner`, `website` |
| website_crm_sms | Send SMS to Visitor with leads |  | `website.visitor` |
| website_customer | Customer References | `res.partner.tag` | `res.partner`, `website` |
| website_event | Events | `event.question`, `event.question.answer`, `event.registration.answer`, `website.event.menu` | `event.event`, `event.registration`, `event.tag.category`, `event.tag`, `event.type`, `website.menu`, `website.snippet.filter`, `website.visitor`, `website` |
| website_event_booth | Online Event Booths |  | `event.event`, `event.type`, `website.event.menu` |
| website_event_booth_exhibitor | Booths/Exhibitors Bridge |  | `event.booth.category`, `event.booth` |
| website_event_booth_sale | Online Event Booth Sale |  | `product.product`, `product.template`, `sale.order`, `website` |
| website_event_booth_sale_exhibitor | Booths Sale/Exhibitors Bridge |  | `event.booth.registration` |
| website_event_crm | Website Events CRM |  | `event.registration` |
| website_event_exhibitor | Event Exhibitors | `event.sponsor`, `event.sponsor.type` | `event.event`, `event.type`, `website.event.menu` |
| website_event_jitsi | Event / Jitsi |  | `res.config.settings` |
| website_event_meet | Event Meeting / Rooms | `event.meeting.room` | `event.event`, `event.type`, `website.event.menu` |
| website_event_meet_quiz | Quiz and Meet on community |  |  |
| website_event_sale | Online Event Ticketing |  | `event.sale.report`, `product.pricelist.item`, `product.product`, `product.template`, `sale.order.line`, `sale.order`, `website` |
| website_event_track | Advanced Events | `event.track`, `event.track.location`, `event.track.stage`, `event.track.tag`, `event.track.tag.category`, `event.track.visitor` | `event.event`, `event.type`, `res.config.settings`, `website.event.menu`, `website.menu`, `website.visitor`, `website` |
| website_event_track_live | Live Event Tracks |  | `event.track` |
| website_event_track_live_quiz | Quiz on Live Event Tracks |  |  |
| website_event_track_quiz | Quizzes on Tracks | `event.quiz`, `event.quiz.question`, `event.quiz.answer` | `event.event`, `event.track.visitor`, `event.track` |
| website_form_project | Online Task Submission |  |  |
| website_forum | Forum | `forum.forum`, `forum.post`, `forum.post.reason`, `forum.post.vote`, `forum.tag` | `forum.forum`, `forum.post`, `gamification.challenge`, `gamification.karma.tracking`, `ir.attachment`, `mail.message`, `res.users`, `website` |
| website_google_map | Google Maps |  |  |
| website_hr_recruitment | Online Jobs |  | `hr.applicant`, `hr.department`, `hr.job`, `hr.recruitment.source`, `website` |
| website_jitsi | Website Jitsi | `chat.room`, `chat.room.mixin` |  |
| website_links | Link Tracker |  | `link.tracker` |
| website_livechat | Website Live Chat |  | `chatbot.script.step`, `chatbot.script`, `discuss.channel`, `im_livechat.channel`, `ir.http`, `res.config.settings`, `website.visitor`, `website` |
| website_mail | Website Mail |  | `publisher_warranty.contract` |
| website_mail_group | Website Mail Group |  | `mail.group` |
| website_mass_mailing | Newsletter Subscribe Button |  | `res.company` |
| website_mass_mailing_sms | Newsletter Subscribe SMS Template |  |  |
| website_membership | Online Members Directory |  | `membership.membership_line`, `website` |
| website_partner | Website Partner |  | `res.partner` |
| website_payment | Website Payment |  | `account.payment`, `payment.provider`, `payment.transaction`, `res.config.settings`, `res.country` |
| website_payment_authorize | Website - Payment Authorize |  | `res.config.settings` |
| website_profile | Website profile |  | `gamification.badge`, `res.users`, `website` |
| website_sale | eCommerce | `product.image`, `product.public.category`, `product.ribbon`, `website.sale.extra.field`, `website.base.unit` | `account.move`, `crm.team`, `delivery.carrier`, `digest.digest`, `ir.http`, `payment.token`, `product.attribute`, `product.document`, `product.pricelist`, `product.product`, `product.public.category`, `product.tag`, `product.template.attribute.line`, `product.template.attribute.value`, `product.template`, `res.company`, `res.config.settings`, `res.country`, `res.partner`, `sale.order.line`, `sale.order`, `sale.report`, `website.snippet.filter`, `website.track`, `website.visitor`, `website` |
| website_sale_autocomplete | Google places autocompletion |  | `res.config.settings`, `website` |
| website_sale_comparison | Product Comparison | `product.attribute.category` | `product.attribute`, `product.product`, `product.template.attribute.line` |
| website_sale_comparison_wishlist | Product Availability Notifications |  |  |
| website_sale_loyalty | Coupons, Promotions, Gift Card and Loyalty for eCommerce | `coupon.share` | `loyalty.card`, `loyalty.program`, `loyalty.rule`, `sale.order.line`, `sale.order` |
| website_sale_mondialrelay | eCommerce Mondialrelay Delivery |  | `res.partner`, `sale.order`, `website` |
| website_sale_mrp | Kit Availability |  | `sale.order` |
| website_sale_picking | On site Payment & Picking |  | `delivery.carrier`, `payment.provider`, `res.config.settings`, `sale.order`, `website` |
| website_sale_product_configurator | Website Sale Product Configurator |  | `sale.order`, `website` |
| website_sale_slides | Sell Courses |  | `product.product`, `product.template`, `sale.order`, `slide.channel`, `website` |
| website_sale_stock | Product Availability |  | `product.product`, `product.template`, `res.config.settings`, `sale.order.line`, `sale.order`, `stock.picking`, `website` |
| website_sale_stock_wishlist | Product Availability Notifications |  | `product.template`, `product.wishlist` |
| website_sale_wishlist | Shopper's Wishlist | `product.wishlist` | `product.product`, `product.template`, `res.partner`, `res.users` |
| website_slides | eLearning | `slide.channel.partner`, `slide.channel`, `slide.channel.tag.group`, `slide.channel.tag`, `slide.embed`, `slide.question`, `slide.answer`, `slide.slide.partner`, `slide.tag`, `slide.slide`, `slide.slide.resource`, `slide.channel.invite` | `base.partner.merge.automatic.wizard`, `gamification.challenge`, `gamification.karma.tracking`, `ir.binary`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `slide.channel.partner`, `slide.channel`, `website` |
| website_slides_forum | Forum on Courses |  | `forum.forum`, `slide.channel` |
| website_slides_survey | Course Certifications |  | `slide.channel`, `slide.slide.partner`, `slide.slide`, `survey.survey`, `survey.user_input` |
| website_sms | Send SMS to Visitor |  | `website.visitor` |
| website_twitter | Twitter Snippet | `website.twitter.tweet` | `res.config.settings`, `website` |
