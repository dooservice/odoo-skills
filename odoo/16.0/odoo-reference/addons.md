# Addons

| Addon | Name | Defines | Extends |
|---|---|---|---|
| base | Base | `avatar.mixin`, `decimal.precision`, `image.mixin`, `ir.actions.actions`, `ir.actions.act_window`, `ir.actions.act_window.view`, `ir.actions.act_window_close`, `ir.actions.act_url`, `ir.actions.server`, `ir.server.object.lines`, `ir.actions.todo`, `ir.actions.client`, `ir.actions.report`, `ir.asset`, `ir.attachment`, `ir.autovacuum`, `ir.binary`, `ir.config_parameter`, `ir.cron`, `ir.cron.trigger`, `ir.default`, `ir.demo`, `ir.demo_failure`, `ir.demo_failure.wizard`, `ir.exports`, `ir.exports.line`, `ir.fields.converter`, `ir.filters`, `ir.http`, `ir.logging`, `ir.mail_server`, `base`, `_unknown`, `ir.model`, `ir.model.fields`, `ir.model.fields.selection`, `ir.model.constraint`, `ir.model.relation`, `ir.model.access`, `ir.model.data`, `wizard.ir.model.menu.create`, `ir.module.category`, `ir.module.module`, `ir.module.module.dependency`, `ir.module.module.exclusion`, `ir.profile`, `base.enable.profiling.wizard`, `ir.property`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.many2one`, `ir.qweb.field.many2many`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.qweb.field.monetary`, `ir.qweb.field.float_time`, `ir.qweb.field.time`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.barcode`, `ir.qweb.field.contact`, `ir.qweb.field.qweb`, `ir.rule`, `ir.sequence`, `ir.sequence.date_range`, `ir.ui.menu`, `ir.ui.view.custom`, `ir.ui.view`, `reset.view.arch.wizard`, `report.layout`, `report.paperformat`, `res.bank`, `res.partner.bank`, `res.company`, `res.config`, `res.config.installer`, `res.config.settings`, `res.country`, `res.country.group`, `res.country.state`, `res.currency`, `res.currency.rate`, `res.lang`, `format.address.mixin`, `res.partner.category`, `res.partner.title`, `res.partner`, `res.partner.industry`, `res.groups`, `res.users.log`, `res.users`, `res.users.identitycheck`, `change.password.wizard`, `change.password.user`, `change.password.own`, `res.users.apikeys`, `res.users.apikeys.description`, `res.users.apikeys.show`, `res.users.deletion`, `report.base.report_irmodulereference`, `base.language.export`, `base.language.import`, `base.language.install`, `base.module.uninstall`, `base.module.update`, `base.module.upgrade`, `base.partner.merge.line`, `base.partner.merge.automatic.wizard` | `base`, `ir.filters`, `ir.module.category`, `res.company`, `res.currency.rate`, `res.groups`, `res.partner.industry`, `res.partner`, `res.users` |
| account | Invoicing | `account.account`, `account.group`, `account.root`, `account.account.tag`, `account.bank.statement`, `account.bank.statement.line`, `account.cash.rounding`, `account.full.reconcile`, `account.incoterms`, `account.journal.group`, `account.journal`, `account.move`, `account.move.line`, `account.partial.reconcile`, `account.payment`, `account.payment.method`, `account.payment.method.line`, `account.payment.term`, `account.payment.term.line`, `account.reconcile.model.partner.mapping`, `account.reconcile.model.line`, `account.reconcile.model`, `account.report`, `account.report.line`, `account.report.expression`, `account.report.column`, `account.report.external.value`, `account.tax.group`, `account.tax`, `account.tax.repartition.line`, `account.group.template`, `account.account.template`, `account.chart.template`, `account.tax.template`, `account.tax.repartition.line.template`, `account.fiscal.position.template`, `account.fiscal.position.tax.template`, `account.fiscal.position.account.template`, `account.reconcile.model.template`, `account.reconcile.model.line.template`, `account.fiscal.position`, `account.fiscal.position.tax`, `account.fiscal.position.account`, `sequence.mixin`, `report.account.report_hash_integrity`, `account.invoice.report`, `report.account.report_invoice`, `report.account.report_invoice_with_payments`, `account.automatic.entry.wizard`, `account.invoice.send`, `account.move.reversal`, `account.payment.register`, `account.resequence.wizard`, `account.tour.upload.bill`, `account.tour.upload.bill.email.confirm`, `account.unreconcile`, `validate.account.move`, `account.accrued.orders.wizard`, `account.financial.year.op`, `account.setup.bank.manual.config` | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.distribution.model`, `account.analytic.line`, `account.bank.statement.line`, `account.bank.statement`, `account.chart.template`, `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.reconcile.model.line`, `account.reconcile.model`, `base.document.layout`, `base.partner.merge.automatic.wizard`, `decimal.precision`, `digest.digest`, `ir.actions.report`, `ir.attachment`, `kpi.provider`, `mail.thread`, `product.category`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.currency`, `res.groups`, `res.partner.bank`, `res.partner`, `res.users` |
| account_add_gln | Add Partner GLN |  | `res.partner` |
| account_check_printing | Check Printing Base | `print.prenumbered.checks` | `account.journal`, `account.move`, `account.payment.method`, `account.payment.register`, `account.payment`, `res.company`, `res.config.settings`, `res.partner` |
| account_debit_note | Debit Notes | `account.debit.note` | `account.move` |
| account_edi | Import/Export Invoices From XML/PDF | `account.edi.document`, `account.edi.format` | `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.resequence.wizard`, `ir.actions.report`, `ir.attachment`, `mail.template`, `uom.uom` |
| account_edi_proxy_client | Proxy features for account_edi | `account_edi_proxy_client.user` | `account.edi.format`, `res.company` |
| account_edi_ubl_cii | Import/Export electronic invoices with UBL/CII | `account.edi.common`, `account.edi.xml.cii`, `account.edi.xml.ubl_20`, `account.edi.xml.ubl_21`, `account.edi.xml.ubl_a_nz`, `account.edi.xml.ubl_bis3`, `account.edi.xml.ubl_efff`, `account.edi.xml.ubl_nl`, `account.edi.xml.ubl_sg`, `account.edi.xml.ubl_de` | `account.edi.format`, `ir.actions.report`, `mail.template` |
| account_edi_ubl_cii_tax_extension | Tax extension for UBL/CII |  | `account.edi.common`, `account.tax` |
| account_fleet | Accounting/Fleet bridge |  | `account.automatic.entry.wizard`, `account.move.line`, `account.move`, `fleet.vehicle` |
| account_lock | Irreversible Lock Date |  | `res.company` |
| account_payment | Payment - Account | `payment.refund.wizard` | `account.journal`, `account.move`, `account.payment.method.line`, `account.payment.method`, `account.payment.register`, `account.payment`, `payment.link.wizard`, `payment.provider`, `payment.transaction` |
| account_payment_invoice_online_payment_patch | Payment - Account / Invoice Online Payment Patch |  | `account.move`, `res.config.settings` |
| account_peppol | Peppol |  | `account.edi.format`, `account.invoice.send`, `account.journal`, `account.move`, `account_edi_proxy_client.user`, `ir.actions.report`, `res.company`, `res.config.settings`, `res.partner` |
| account_qr_code_sepa | account_qr_code_sepa |  | `res.partner.bank` |
| account_sequence | Accounting Sequence |  | `account.move`, `sequence.mixin` |
| account_tax_python | Define Taxes as Python Code |  | `account.tax.template`, `account.tax` |
| account_test | Accounting Consistency Tests | `accounting.assert.test`, `report.account_test.report_accounttest` |  |
| account_update_tax_tags | Account - Allow updating tax grids | `account.update.tax.tags.wizard` |  |
| analytic | Analytic Accounting | `account.analytic.account`, `account.analytic.distribution.model`, `account.analytic.line`, `analytic.mixin`, `account.analytic.plan`, `account.analytic.applicability` | `res.config.settings` |
| association | Associations Management |  |  |
| attachment_indexation | Attachments List and Document Indexation |  | `ir.attachment` |
| auth_ldap | Authentication via LDAP | `res.company.ldap` | `res.company`, `res.config.settings`, `res.users` |
| auth_oauth | OAuth2 Authentication | `auth.oauth.provider` | `ir.config_parameter`, `res.config.settings`, `res.users` |
| auth_password_policy | Password Policy |  | `res.config.settings`, `res.users` |
| auth_password_policy_portal | Password Policy support for Signup |  |  |
| auth_password_policy_signup | Password Policy support for Signup |  |  |
| auth_signup | Signup |  | `ir.http`, `res.config.settings`, `res.partner`, `res.users` |
| auth_totp | Two-Factor Authentication (TOTP) | `auth_totp.device`, `auth_totp.wizard` | `ir.http`, `res.users` |
| auth_totp_mail | 2FA Invite mail |  | `res.users` |
| auth_totp_mail_enforce | 2FA by mail | `auth.totp.rate.limit.log` | `res.config.settings`, `res.users` |
| auth_totp_portal | TOTPortal |  | `res.users` |
| barcodes | Barcode | `barcodes.barcode_events_mixin`, `barcode.nomenclature`, `barcode.rule` | `ir.http`, `res.company` |
| barcodes_gs1_nomenclature | Barcode - GS1 Nomenclature |  | `barcode.nomenclature`, `barcode.rule`, `ir.http` |
| base_address_extended | Extended Addresses | `res.city` | `res.country`, `res.partner` |
| base_automation | Automated Action Rules | `base.automation` | `ir.actions.server` |
| base_geolocalize | Partners Geolocation | `base.geo_provider`, `base.geocoder` | `res.config.settings`, `res.partner` |
| base_iban | IBAN Bank Accounts |  | `res.partner.bank` |
| base_import | Base import | `base_import.mapping`, `base_import.import` | `base`, `res.users` |
| base_import_module | Base import module | `base.import.module` | `ir.module.module`, `ir.ui.view` |
| base_install_request | Base - Module Install Request | `base.module.install.request`, `base.module.install.review` | `ir.module.module` |
| base_setup | Initial Setup Tools | `kpi.provider` | `ir.http`, `res.config.settings`, `res.users` |
| base_sparse_field | Sparse Fields | `sparse_fields.test` | `base`, `ir.model.fields` |
| base_vat | VAT Number Validation |  | `account.fiscal.position`, `res.company`, `res.config.settings`, `res.partner` |
| board | Dashboards | `board.board` |  |
| bus | IM Bus | `bus.bus`, `bus.presence`, `ir.websocket` | `ir.model`, `res.partner`, `res.users` |
| calendar | Calendar | `calendar.alarm`, `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.event.type`, `calendar.filters`, `calendar.recurrence`, `calendar.provider.config` | `calendar.alarm`, `ir.http`, `mail.activity.mixin`, `mail.activity.type`, `mail.activity`, `res.partner`, `res.users` |
| calendar_sms | Calendar - SMS |  | `calendar.alarm_manager`, `calendar.alarm`, `calendar.event` |
| contacts | Contacts |  | `res.users` |
| crm | CRM | `crm.lead`, `crm.lead.scoring.frequency`, `crm.lead.scoring.frequency.field`, `crm.lost.reason`, `crm.recurring.plan`, `crm.stage`, `crm.activity.report`, `crm.lead.lost`, `crm.lead.pls.update`, `crm.lead2opportunity.partner`, `crm.lead2opportunity.partner.mass`, `crm.merge.opportunity` | `calendar.event`, `crm.lead`, `crm.team.member`, `crm.team`, `digest.digest`, `ir.config_parameter`, `mail.activity`, `res.config.settings`, `res.partner`, `res.users`, `utm.campaign` |
| crm_iap_enrich | Lead Enrichment |  | `crm.lead`, `res.config.settings` |
| crm_iap_mine | Lead Generation | `crm.iap.lead.helpers`, `crm.iap.lead.industry`, `crm.iap.lead.mining.request`, `crm.iap.lead.role`, `crm.iap.lead.seniority` | `crm.lead` |
| crm_livechat | CRM Livechat |  | `chatbot.script.step`, `chatbot.script`, `mail.channel` |
| crm_mail_plugin | CRM Mail Plugin |  | `crm.lead` |
| crm_sms | SMS in CRM |  |  |
| data_recycle | Data Recycle | `data_recycle.model`, `data_recycle.record` |  |
| delivery | Delivery Costs | `delivery.carrier`, `delivery.price.rule`, `delivery.zip.prefix`, `choose.delivery.carrier`, `choose.delivery.package` | `delivery.carrier`, `product.category`, `product.template`, `res.partner`, `sale.order.line`, `sale.order`, `stock.move.line`, `stock.move`, `stock.package.type`, `stock.picking`, `stock.quant.package`, `stock.return.picking` |
| delivery_mondialrelay | delivery_mondialrelay |  | `choose.delivery.carrier`, `delivery.carrier`, `res.partner`, `sale.order` |
| delivery_stock_picking_batch | Delivery Stock Picking Batch |  | `stock.picking.batch`, `stock.picking.type`, `stock.picking` |
| digest | KPI Digests | `digest.digest`, `digest.tip` | `res.config.settings`, `res.users` |
| event | Events Organization | `event.type`, `event.event`, `event.type.mail`, `event.mail`, `event.mail.registration`, `event.registration`, `event.stage`, `event.tag.category`, `event.tag`, `event.type.ticket`, `event.event.ticket` | `mail.template`, `res.config.settings`, `res.partner` |
| event_booth | Events Booths | `event.booth`, `event.booth.category`, `event.type.booth` | `event.event`, `event.type` |
| event_booth_sale | Events Booths Sales | `event.booth.registration`, `event.booth.configurator` | `account.move`, `event.booth.category`, `event.booth`, `event.type.booth`, `product.product`, `product.template`, `sale.order.line`, `sale.order.template.line`, `sale.order.template.option`, `sale.order` |
| event_crm | Event CRM | `event.lead.rule` | `crm.lead`, `event.event`, `event.registration` |
| event_crm_sale | Event CRM Sale |  | `event.registration` |
| event_sale | Events Sales | `event.sale.report`, `event.event.configurator`, `registration.editor`, `registration.editor.line` | `account.move`, `event.event.ticket`, `event.event`, `event.registration`, `event.type.ticket`, `product.product`, `product.template`, `sale.order.line`, `sale.order.template.line`, `sale.order.template.option`, `sale.order` |
| event_sms | SMS on Events |  | `event.mail.registration`, `event.mail`, `event.registration`, `event.type.mail`, `sms.template` |
| fleet | Fleet | `fleet.service.type`, `fleet.vehicle`, `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.model`, `fleet.vehicle.model.brand`, `fleet.vehicle.model.category`, `fleet.vehicle.odometer`, `fleet.vehicle.state`, `fleet.vehicle.tag`, `fleet.vehicle.cost.report` | `res.config.settings`, `res.partner` |
| gamification | Gamification | `gamification.badge`, `gamification.badge.user`, `gamification.challenge`, `gamification.challenge.line`, `gamification.goal`, `gamification.goal.definition`, `gamification.karma.rank`, `gamification.karma.tracking`, `gamification.badge.user.wizard`, `gamification.goal.wizard` | `res.users` |
| gamification_sale_crm | CRM Gamification |  |  |
| google_account | Google Users | `google.service` |  |
| google_calendar | Google Calendar | `google.calendar.credentials`, `google.calendar.sync`, `google.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.recurrence`, `res.config.settings`, `res.users` |
| google_gmail | Google Gmail | `google.gmail.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings` |
| google_recaptcha | Google reCAPTCHA integration |  | `ir.http`, `res.config.settings` |
| hr | Employees | `hr.contract.type`, `hr.department`, `hr.departure.reason`, `hr.employee`, `hr.employee.base`, `hr.employee.category`, `hr.employee.public`, `hr.job`, `hr.plan`, `hr.plan.activity.type`, `hr.work.location`, `hr.departure.wizard`, `hr.plan.wizard` | `base`, `hr.department`, `hr.employee.category`, `hr.employee`, `hr.job`, `hr.work.location`, `ir.ui.menu`, `mail.alias`, `mail.channel`, `res.company`, `res.config.settings`, `res.partner.bank`, `res.partner`, `res.users`, `resource.resource` |
| hr_attendance | Attendances | `hr.attendance`, `hr.attendance.overtime`, `hr.attendance.report` | `hr.employee.public`, `hr.employee`, `ir.ui.menu`, `res.company`, `res.config.settings`, `res.users` |
| hr_contract | Employee Contracts | `hr.contract`, `hr.payroll.structure.type`, `hr.contract.history` | `hr.departure.wizard`, `hr.employee.public`, `hr.employee`, `res.users`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource` |
| hr_expense | Expenses | `hr.expense`, `hr.expense.sheet`, `hr.expense.approve.duplicate`, `hr.expense.refuse.wizard`, `hr.expense.split`, `hr.expense.split.wizard` | `account.analytic.account`, `account.analytic.applicability`, `account.journal`, `account.move.line`, `account.move`, `account.payment.register`, `account.payment`, `hr.department`, `hr.employee.public`, `hr.employee`, `ir.attachment`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.users` |
| hr_fleet | Fleet History |  | `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.odometer`, `fleet.vehicle`, `hr.departure.wizard`, `hr.employee.public`, `hr.employee`, `res.users` |
| hr_gamification | HR Gamification |  | `gamification.badge.user.wizard`, `gamification.badge.user`, `gamification.badge`, `hr.employee.base`, `res.users` |
| hr_holidays | Time Off | `hr.leave`, `hr.leave.accrual.plan`, `hr.leave.accrual.level`, `hr.leave.allocation`, `hr.leave.stress.day`, `hr.leave.type`, `report.hr_holidays.report_holidayssummary`, `hr.leave.employee.type.report`, `hr.leave.report`, `hr.leave.report.calendar`, `hr.holidays.cancel.leave`, `hr.holidays.summary.employee` | `hr.department`, `hr.departure.wizard`, `hr.employee.base`, `hr.employee`, `hr.leave.allocation`, `hr.leave.type`, `hr.leave`, `mail.message.subtype`, `res.partner`, `res.users`, `resource.calendar.leaves`, `resource.calendar` |
| hr_holidays_attendance | HR Attendance Holidays |  | `hr.attendance`, `hr.leave.allocation`, `hr.leave.type`, `hr.leave`, `res.company`, `res.users` |
| hr_hourly_cost | Employee Hourly Wage |  | `hr.employee` |
| hr_maintenance | Maintenance - HR |  | `hr.employee`, `maintenance.equipment`, `maintenance.request`, `res.users` |
| hr_org_chart | HR Org Chart |  | `hr.employee.base`, `hr.employee.public`, `hr.employee` |
| hr_presence | Employee Presence Control |  | `hr.employee.base`, `ir.websocket`, `res.company`, `res.users.log` |
| hr_recruitment | Recruitment | `hr.recruitment.source`, `hr.recruitment.stage`, `hr.recruitment.degree`, `hr.applicant`, `hr.applicant.category`, `hr.applicant.refuse.reason`, `applicant.get.refuse.reason`, `applicant.send.mail` | `calendar.event`, `digest.digest`, `hr.department`, `hr.employee`, `hr.job`, `ir.ui.menu`, `res.config.settings`, `res.users`, `utm.campaign`, `utm.source` |
| hr_recruitment_skills | Recruitment - Skills Management | `hr.applicant.skill` | `hr.applicant` |
| hr_recruitment_survey | Hr Recruitment Interview Forms |  | `hr.applicant`, `hr.job`, `survey.invite`, `survey.user_input` |
| hr_skills | Skills Management | `hr.employee.skill`, `hr.employee.skill.log`, `hr.resume.line`, `hr.resume.line.type`, `hr.skill`, `hr.skill.level`, `hr.skill.type`, `hr.employee.skill.report` | `hr.employee.public`, `hr.employee`, `res.users` |
| hr_skills_slides | Skills e-learning |  | `hr.employee`, `hr.resume.line`, `slide.channel.partner`, `slide.channel` |
| hr_skills_survey | Skills Certification |  | `hr.resume.line`, `survey.user_input` |
| hr_timesheet | Task Logs | `timesheets.analysis.report` | `account.analytic.line`, `ir.http`, `ir.ui.menu`, `project.collaborator`, `project.project`, `project.task`, `report.project.task.user`, `res.company`, `res.config.settings`, `uom.uom` |
| hr_timesheet_attendance | Timesheets/attendances reporting | `hr.timesheet.attendance.report` | `ir.ui.menu` |
| hr_work_entry | Work Entries | `hr.work.entry`, `hr.work.entry.type`, `hr.user.work.entry.employee` | `hr.employee`, `resource.calendar.attendance`, `resource.calendar.leaves` |
| hr_work_entry_contract | Work Entries - Contract | `hr.work.entry.regeneration.wizard` | `hr.contract`, `hr.employee`, `hr.work.entry.type`, `hr.work.entry` |
| hr_work_entry_holidays | Time Off in Payslips |  | `hr.contract`, `hr.leave.type`, `hr.leave`, `hr.work.entry.type`, `hr.work.entry` |
| http_routing | Web Routing |  | `ir.http`, `ir.qweb` |
| iap | In-App Purchases | `iap.account`, `iap.enrich.api` | `res.config.settings` |
| iap_crm | IAP / CRM |  | `crm.lead` |
| iap_mail | IAP / Mail |  | `iap.account` |
| im_livechat | Live Chat | `chatbot.message`, `chatbot.script`, `chatbot.script.answer`, `chatbot.script.step`, `im_livechat.channel`, `im_livechat.channel.rule`, `im_livechat.report.channel`, `im_livechat.report.operator` | `digest.digest`, `mail.channel.member`, `mail.channel`, `mail.message`, `rating.rating`, `res.partner`, `res.users.settings`, `res.users` |
| im_livechat_mail_bot | OdooBot for livechat |  | `mail.bot`, `res.users` |
| l10n_account_edi_ubl_cii_tests | Testing the Import/Export invoices with UBL/CII |  |  |
| l10n_ae | United Arab Emirates - Accounting |  | `account.chart.template`, `account.move.line` |
| l10n_ae_pos | United Arab Emirates - Point of Sale |  |  |
| l10n_ar | Argentina - Accounting | `l10n_ar.afip.responsibility.type` | `account.chart.template`, `account.fiscal.position.template`, `account.fiscal.position`, `account.invoice.report`, `account.journal`, `account.move.line`, `account.move`, `account.tax.group`, `l10n_latam.document.type`, `l10n_latam.identification.type`, `res.company`, `res.country`, `res.currency`, `res.partner.bank`, `res.partner`, `uom.uom` |
| l10n_ar_website_sale | Argentinean eCommerce |  | `sale.order`, `website` |
| l10n_at | Austria - Accounting |  | `account.chart.template` |
| l10n_au | Australia - Accounting |  | `account.chart.template`, `account.move` |
| l10n_be | Belgium - Accounting |  | `account.chart.template`, `account.journal`, `account.move`, `res.partner` |
| l10n_be_pos_sale | l10n_be_pos_sale |  | `pos.session` |
| l10n_bg | Bulgaria - Accounting |  |  |
| l10n_bo | Bolivia - Accounting |  |  |
| l10n_br | Brazilian - Accounting |  | `account.chart.template`, `account.fiscal.position.template`, `account.fiscal.position`, `account.tax.template`, `account.tax`, `res.company`, `res.partner` |
| l10n_ca | Canada - Accounting |  | `base.document.layout`, `res.company`, `res.partner` |
| l10n_ch | Switzerland - Accounting | `report.l10n_ch.qr_report_main`, `l10n_ch.qr_invoice.wizard` | `account.bank.statement.line`, `account.chart.template`, `account.journal`, `account.move`, `account.setup.bank.manual.config`, `ir.actions.report`, `res.company`, `res.config.settings`, `res.partner.bank` |
| l10n_ch_pos | Swiss - Point of Sale |  | `pos.order` |
| l10n_cl | Chile - Accounting |  | `account.chart.template`, `account.move.line`, `account.move`, `account.tax.template`, `account.tax`, `l10n_latam.document.type`, `res.bank`, `res.company`, `res.country`, `res.currency`, `res.partner`, `uom.uom` |
| l10n_cn | China - Accounting |  | `account.move` |
| l10n_cn_city | China - City Data |  |  |
| l10n_co | Colombia - Accounting |  | `l10n_latam.identification.type`, `res.partner` |
| l10n_co_pos | Colombian - Point of Sale |  | `pos.order` |
| l10n_cr | Costa Rica - Accounting |  |  |
| l10n_cz | Czech - Accounting |  |  |
| l10n_de | Germany - Accounting |  | `account.chart.template`, `account.journal`, `account.tax.template`, `account.tax`, `ir.actions.report`, `product.template`, `res.company` |
| l10n_de_skr03 | Germany SKR03 - Accounting |  |  |
| l10n_de_skr04 | Germany SKR04 - Accounting |  |  |
| l10n_din5008 | DIN 5008 |  | `account.analytic.line`, `account.move`, `base.document.layout` |
| l10n_din5008_purchase | DIN 5008 - Purchase |  | `purchase.order` |
| l10n_din5008_repair | DIN 5008 - Repair |  | `repair.order` |
| l10n_din5008_sale | DIN 5008 - Sale |  | `sale.order` |
| l10n_din5008_stock | DIN 5008 - Stock |  | `stock.picking` |
| l10n_dk | Denmark - Accounting |  | `account.journal` |
| l10n_do | Dominican Republic - Accounting |  | `account.chart.template` |
| l10n_dz | Algeria - Accounting |  | `account.move` |
| l10n_ec | Ecuadorian Accounting | `l10n_ec.sri.payment` | `account.chart.template`, `account.journal`, `account.move`, `account.tax.group`, `account.tax.template`, `account.tax`, `l10n_latam.document.type`, `res.company`, `res.partner` |
| l10n_ec_stock | Ecuador - Stock |  | `account.chart.template` |
| l10n_ee | Estonia - Accounting |  | `account.tax.template`, `account.tax` |
| l10n_eg | Egypt - Accounting | `l10n_eg.eta.account.tax.mixin` | `account.chart.template`, `account.tax.template`, `account.tax` |
| l10n_eg_edi_eta | Egypt E-Invoicing | `l10n_eg_edi.activity.type`, `l10n_eg_edi.thumb.drive`, `l10n_eg_edi.uom.code` | `account.edi.format`, `account.journal`, `account.move`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.currency.rate`, `res.partner`, `uom.uom` |
| l10n_es | Spain - Accounting (PGCE 2008) |  |  |
| l10n_es_edi_sii | Spain - SII EDI Suministro de Libros | `l10n_es.sii.account.tax.mixin`, `l10n_es_edi.certificate` | `account.edi.format`, `account.move`, `account.resequence.wizard`, `account.tax.template`, `account.tax`, `mail.template`, `res.company`, `res.config.settings` |
| l10n_es_edi_tbai | Spain - TicketBAI |  | `account.edi.document`, `account.edi.format`, `account.move.reversal`, `account.move`, `account.resequence.wizard`, `ir.attachment`, `l10n_es_edi.certificate`, `res.company`, `res.config.settings` |
| l10n_es_edi_tbai_multi_refund | TicketBAI multi refund |  | `account.edi.format`, `account.move` |
| l10n_et | Ethiopia - Accounting |  |  |
| l10n_eu_oss | EU One Stop Shop (OSS) |  | `account.chart.template`, `res.company`, `res.config.settings` |
| l10n_fi | Finnish Localization |  | `account.journal`, `account.move` |
| l10n_fi_sale | Finland - Sale |  | `sale.order` |
| l10n_fr | France - Accounting |  | `account.chart.template`, `res.company`, `res.partner` |
| l10n_fr_facturx_chorus_pro | France - Factur-X integration with Chorus Pro |  | `account.move` |
| l10n_fr_fec | France - FEC Export | `account.fr.fec` |  |
| l10n_fr_invoice_addr | France - Adding Mandatory Invoice Mentions (Decree no. 2022-1299) |  | `account.move` |
| l10n_fr_pos_cert | France - VAT Anti-Fraud Certification for Point of Sale (CGI 286 I-3 bis) | `account.sale.closing`, `report.l10n_fr_pos_cert.report_pos_hash_integrity` | `account.fiscal.position`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.company` |
| l10n_gcc_invoice | G.C.C. - Arabic/English Invoice |  | `account.move.line`, `account.move` |
| l10n_gcc_invoice_stock_account | Gulf Cooperation Council WMS Accounting |  |  |
| l10n_gcc_pos | Gulf Cooperation Council - Point of Sale |  |  |
| l10n_generic_coa | Generic - Accounting |  |  |
| l10n_gr | Greece - Accounting |  |  |
| l10n_gt | Guatemala - Accounting |  |  |
| l10n_hk | Hong Kong - Accounting |  |  |
| l10n_hn | Honduras - Accounting |  |  |
| l10n_hr | Croatia - Accounting (RRIF 2012) |  |  |
| l10n_hr_euro | Croatia - Accounting (EURO) |  |  |
| l10n_hu | Hungary - Accounting |  |  |
| l10n_id | Indonesian - Accounting |  | `account.move` |
| l10n_id_efaktur | Indonesia E-faktur | `l10n_id_efaktur.efaktur.range` | `account.move`, `res.config.settings`, `res.partner` |
| l10n_id_efaktur_coretax | Indonesia E-faktur (Coretax) | `l10n_id_efaktur_coretax.document`, `l10n_id_efaktur_coretax.product.code`, `l10n_id_efaktur_coretax.uom.code` | `account.move.line`, `account.move`, `product.template`, `res.partner`, `uom.uom` |
| l10n_ie | Ireland - Accounting |  |  |
| l10n_il | Israel - Accounting |  |  |
| l10n_in | Indian - Accounting | `l10n_in.port.code` | `account.chart.template`, `account.journal`, `account.move.line`, `account.move`, `account.tax.template`, `account.tax`, `mail.message`, `product.template`, `res.config.settings`, `res.country.state`, `res.partner`, `uom.uom` |
| l10n_in_edi | Indian - E-invoicing |  | `account.edi.format`, `account.move`, `res.company`, `res.config.settings` |
| l10n_in_edi_ewaybill | Indian - E-waybill | `l10n.in.ewaybill.type` | `account.chart.template`, `account.edi.format`, `account.move`, `res.company`, `res.config.settings` |
| l10n_in_ewaybill_port | Indian - Shipping Ports for E-waybill |  | `account.edi.format`, `account.move` |
| l10n_in_pos | Indian - Point of Sale |  | `pos.config`, `pos.order`, `pos.session` |
| l10n_in_purchase | Indian - Purchase Report(GST) |  | `account.move`, `purchase.order` |
| l10n_in_purchase_stock | India Purchase and Warehouse Management |  | `account.move`, `purchase.order`, `stock.warehouse` |
| l10n_in_sale | Indian - Sale Report(GST) |  | `sale.advance.payment.inv`, `sale.order` |
| l10n_in_sale_stock | India Sales and Warehouse Management |  | `account.move`, `sale.order`, `stock.warehouse` |
| l10n_in_stock | Indian - Stock Report(GST) |  | `stock.picking` |
| l10n_in_tcs_tds | Indian - TCS/TDS Accounting Report and Taxes |  | `res.partner` |
| l10n_in_upi | Indian - UPI |  | `account.move`, `res.company` |
| l10n_it | Italy - Accounting |  | `account.chart.template`, `account.report.expression` |
| l10n_it_edi | Italy - E-invoicing | `l10n_it.ddt` | `account.chart.template`, `account.edi.format`, `account.move`, `account.tax`, `mail.template`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_it_edi_doi | Italy - Declaration of Intent | `l10n_it_edi_doi.declaration_of_intent` | `account.chart.template`, `account.fiscal.position`, `account.move`, `account.tax`, `res.company`, `res.partner`, `sale.advance.payment.inv`, `sale.order.line`, `sale.order` |
| l10n_it_edi_pa | Italy - E-invoicing (PA) |  | `account.edi.format`, `account.move` |
| l10n_it_edi_website_sale | Italy eCommerce eInvoicing |  |  |
| l10n_it_edi_withholding | Italy - E-invoicing (Withholding) |  | `account.chart.template`, `account.edi.format`, `account.move`, `account.tax.template`, `account.tax` |
| l10n_it_stock_ddt | l10n_it_stock_ddt |  | `account.edi.format`, `account.move`, `stock.picking.type`, `stock.picking` |
| l10n_jp | Japan - Accounting |  |  |
| l10n_ke | Kenya - Accounting |  |  |
| l10n_ke_edi_tremol | Kenya Tremol Device EDI Integration |  | `account.move`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_latam_account_sequence | Accounting Sequence - Latam Documents |  | `account.move` |
| l10n_latam_base | LATAM Localization Base | `l10n_latam.identification.type` | `res.company`, `res.partner` |
| l10n_latam_check | Third Party and Deferred/Electronic Checks Management | `l10n_latam.payment.mass.transfer` | `account.chart.template`, `account.journal`, `account.payment.method`, `account.payment.register`, `account.payment` |
| l10n_latam_invoice_document | LATAM Document | `l10n_latam.document.type` | `account.chart.template`, `account.debit.note`, `account.invoice.report`, `account.journal`, `account.move.line`, `account.move.reversal`, `account.move`, `res.company` |
| l10n_lt | Lithuania - Accounting |  |  |
| l10n_lu | Luxembourg - Accounting |  | `account.chart.template` |
| l10n_lu_peppol_id | Luxembourg - Peppol Identifier |  | `res.partner` |
| l10n_lv | Latvia - Accounting |  |  |
| l10n_ma | Morocco - Accounting |  | `base.document.layout`, `res.partner` |
| l10n_mn | Mongolia - Accounting |  |  |
| l10n_mt_pos | Malta - Point of Sale | `compliance.letter.wizard` |  |
| l10n_multilang | Multi Language Chart of Accounts |  | `account.account.tag`, `account.account.template`, `account.account`, `account.analytic.account`, `account.chart.template`, `account.fiscal.position.template`, `account.fiscal.position`, `account.group.template`, `account.group`, `account.journal`, `account.tax.template`, `account.tax`, `base.language.install` |
| l10n_mx | Mexico - Accounting |  | `account.account`, `account.chart.template`, `account.tax.template`, `account.tax`, `res.bank`, `res.config.settings`, `res.partner.bank` |
| l10n_mx_hr | Employees - Mexico |  | `hr.employee` |
| l10n_my | Malaysia - Accounting |  |  |
| l10n_mz | Mozambique - Accounting |  |  |
| l10n_nl | Netherlands - Accounting |  | `account.chart.template`, `account.journal`, `res.company`, `res.partner` |
| l10n_no | Norway - Accounting |  | `account.journal`, `account.move`, `res.company`, `res.partner` |
| l10n_nz | New Zealand - Accounting |  |  |
| l10n_pa | Panama - Accounting |  |  |
| l10n_pe | Peru - Accounting | `l10n_pe.res.city.district` | `account.chart.template`, `account.move.line`, `account.move`, `account.tax.template`, `account.tax`, `l10n_latam.identification.type`, `res.city`, `res.company`, `res.partner` |
| l10n_ph | Philippines - Accounting | `l10n_ph_2307.wizard` | `account.move`, `account.payment`, `account.tax.template`, `account.tax`, `res.partner` |
| l10n_pk | Pakistan - Accounting |  |  |
| l10n_pl | Poland - Accounting |  |  |
| l10n_pl_jpk | Poland - JPK_VAT Community | `l10n_pl_tax_office` | `account.move`, `product.template`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_pl_sale_stock | Poland - Sales and Stock |  | `account.move` |
| l10n_pt | Portugal - Accounting |  |  |
| l10n_ro | Romania - Accounting |  | `res.partner` |
| l10n_rs | Serbia - Accounting |  | `account.move` |
| l10n_sa | Saudi Arabia - Accounting |  | `account.chart.template`, `account.move` |
| l10n_sa_edi | Saudi Arabia - E-invoicing | `account.edi.xml.ubl_21.zatca`, `l10n_sa_edi.otp.wizard` | `account.debit.note`, `account.edi.document`, `account.edi.format`, `account.journal`, `account.move.line`, `account.move.reversal`, `account.move`, `account.tax.template`, `account.tax`, `ir.attachment`, `res.company`, `res.config.settings`, `res.partner` |
| l10n_sa_edi_pos | Saudi Arabia - E-invoicing (Simplified) |  | `account.edi.xml.ubl_21.zatca`, `account.move`, `pos.config` |
| l10n_sa_pos | Saudi Arabia - Point of Sale |  | `pos.config`, `pos.order` |
| l10n_se | Sweden - Accounting |  | `account.journal`, `account.move`, `res.company`, `res.partner` |
| l10n_sg | Singapore - Accounting |  | `account.chart.template`, `account.move`, `res.company`, `res.partner` |
| l10n_si | Slovenian - Accounting |  |  |
| l10n_sk | Slovak - Accounting |  |  |
| l10n_syscohada | OHADA - Accounting |  |  |
| l10n_th | Thailand - Accounting |  | `account.move`, `ir.actions.report`, `res.partner` |
| l10n_tr | Türkiye - Accounting |  |  |
| l10n_tw | Taiwan - Accounting |  |  |
| l10n_ua | Ukraine - Accounting |  |  |
| l10n_uk | United Kingdom - Accounting |  |  |
| l10n_us | United States - Accounting |  | `res.partner.bank` |
| l10n_uy | Uruguay - Accounting |  |  |
| l10n_ve | Venezuela - Accounting |  |  |
| l10n_vn | Vietnam - Accounting |  |  |
| l10n_za | South Africa - Accounting |  |  |
| link_tracker | Link Tracker | `link.tracker`, `link.tracker.code`, `link.tracker.click` | `mail.render.mixin`, `utm.campaign` |
| loyalty | Coupons & Loyalty | `loyalty.card`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `loyalty.generate.wizard` | `product.product`, `product.template` |
| loyalty_delivery | Coupons & Loyalty - Delivery |  | `loyalty.program`, `loyalty.reward`, `sale.order` |
| lunch | Lunch | `lunch.alert`, `lunch.cashmove`, `lunch.location`, `lunch.order`, `lunch.product`, `lunch.product.category`, `lunch.supplier`, `lunch.topping`, `lunch.cashmove.report` | `lunch.alert`, `lunch.location`, `lunch.order`, `lunch.product.category`, `lunch.product`, `lunch.supplier`, `res.company`, `res.config.settings`, `res.users` |
| mail | Discuss | `fetchmail.server`, `mail.activity`, `mail.activity.mixin`, `mail.activity.type`, `mail.alias`, `mail.alias.mixin`, `mail.blacklist`, `mail.channel`, `mail.channel.member`, `mail.channel.rtc.session`, `mail.composer.mixin`, `mail.followers`, `mail.gateway.allowed`, `mail.guest`, `mail.ice.server`, `mail.link.preview`, `mail.mail`, `mail.message`, `mail.message.reaction`, `mail.message.schedule`, `mail.message.subtype`, `mail.notification`, `mail.render.mixin`, `mail.shortcode`, `mail.template`, `mail.thread`, `mail.thread.blacklist`, `mail.thread.cc`, `mail.tracking.value`, `res.users.settings`, `res.users.settings.volumes`, `template.reset.mixin`, `publisher_warranty.contract`, `mail.blacklist.remove`, `mail.compose.message`, `mail.resend.message`, `mail.resend.partner`, `mail.template.preview`, `mail.template.reset`, `mail.wizard.invite` | `base.module.uninstall`, `base.partner.merge.automatic.wizard`, `base`, `bus.presence`, `ir.actions.act_window.view`, `ir.actions.server`, `ir.attachment`, `ir.config_parameter`, `ir.http`, `ir.mail_server`, `ir.model.fields`, `ir.model`, `ir.qweb`, `ir.ui.view`, `ir.websocket`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users` |
| mail_bot | OdooBot | `mail.bot` | `ir.http`, `mail.channel`, `mail.thread`, `res.users` |
| mail_bot_hr | mail_bot_hr |  |  |
| mail_group | Mail Group | `mail.group`, `mail.group.member`, `mail.group.message`, `mail.group.moderation`, `mail.group.message.reject` |  |
| mail_plugin | Mail Plugin | `res.partner.iap` | `ir.http`, `res.partner` |
| maintenance | Maintenance | `maintenance.stage`, `maintenance.equipment.category`, `maintenance.equipment`, `maintenance.request`, `maintenance.team` |  |
| mass_mailing | Email Marketing | `mailing.mailing`, `mailing.contact.subscription`, `mailing.contact`, `mailing.contact.subscription`, `mailing.filter`, `mailing.list`, `mailing.trace`, `mailing.trace.report`, `mailing.contact.import`, `mailing.contact.to.list`, `mailing.list.merge`, `mailing.mailing.schedule.date`, `mailing.mailing.test` | `ir.http`, `ir.mail_server`, `ir.model`, `link.tracker.click`, `link.tracker`, `mail.compose.message`, `mail.mail`, `mail.render.mixin`, `mail.thread`, `res.company`, `res.config.settings`, `res.partner`, `res.users`, `utm.campaign`, `utm.medium`, `utm.source` |
| mass_mailing_crm | Mass mailing on lead / opportunities |  | `crm.lead`, `mailing.mailing`, `utm.campaign` |
| mass_mailing_crm_sms | Mass mailing sms on lead / opportunities |  | `utm.campaign` |
| mass_mailing_event | Mass mailing on attendees |  | `event.event`, `event.registration` |
| mass_mailing_event_sms | Event Attendees SMS Marketing |  | `event.event` |
| mass_mailing_event_track | Mass mailing on track speakers |  | `event.event`, `event.track` |
| mass_mailing_event_track_sms | Track Speakers SMS Marketing |  | `event.event` |
| mass_mailing_sale | Mass mailing on sale orders |  | `mailing.mailing`, `sale.order`, `utm.campaign` |
| mass_mailing_sale_sms | Mass mailing sms on sale orders |  | `utm.campaign` |
| mass_mailing_slides | Mass mailing on course members |  | `slide.channel` |
| mass_mailing_sms | SMS Marketing | `mailing.sms.test` | `mailing.contact`, `mailing.list`, `mailing.mailing`, `mailing.trace`, `res.users`, `sms.composer`, `sms.sms`, `utm.campaign`, `utm.medium` |
| mass_mailing_themes | Mass Mailing Themes |  |  |
| membership | Members | `membership.membership_line`, `report.membership`, `membership.invoice` | `account.move.line`, `account.move`, `product.template`, `res.partner` |
| microsoft_account | Microsoft Users | `microsoft.service` | `res.users` |
| microsoft_calendar | Outlook Calendar | `microsoft.calendar.sync`, `microsoft.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.recurrence`, `res.config.settings`, `res.users` |
| microsoft_outlook | Microsoft Outlook | `microsoft.outlook.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings` |
| mrp | Manufacturing | `mrp.bom`, `mrp.bom.line`, `mrp.bom.byproduct`, `mrp.document`, `mrp.production`, `mrp.routing.workcenter`, `mrp.unbuild`, `mrp.workcenter`, `mrp.workcenter.tag`, `mrp.workcenter.productivity.loss.type`, `mrp.workcenter.productivity.loss`, `mrp.workcenter.productivity`, `mrp.workcenter.capacity`, `mrp.workorder`, `report.mrp.report_bom_structure`, `change.production.qty`, `mrp.consumption.warning`, `mrp.consumption.warning.line`, `mrp.immediate.production.line`, `mrp.immediate.production`, `mrp.production.backorder.line`, `mrp.production.backorder`, `mrp.production.split.multi`, `mrp.production.split`, `mrp.production.split.line`, `stock.warn.insufficient.qty.unbuild` | `mrp.bom.byproduct`, `mrp.bom.line`, `mrp.bom`, `mrp.production`, `mrp.routing.workcenter`, `mrp.workcenter`, `procurement.group`, `product.product`, `product.template`, `report.stock.report_product_product_replenishment`, `report.stock.report_reception`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `stock.assign.serial`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.quant`, `stock.rule`, `stock.scrap`, `stock.traceability.report`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_account | Accounting - MRP |  | `account.analytic.account`, `account.analytic.line`, `account.move.line`, `mrp.bom`, `mrp.production`, `mrp.routing.workcenter`, `mrp.workcenter.productivity`, `mrp.workcenter`, `mrp.workorder`, `product.product`, `product.template`, `stock.move`, `stock.rule` |
| mrp_landed_costs | Landed Costs On MO |  | `stock.landed.cost` |
| mrp_product_expiry | Manufacturing Expiry |  | `expiry.picking.confirmation`, `mrp.production` |
| mrp_repair | Mrp Repairs |  | `repair.line`, `repair.order` |
| mrp_subcontracting | mrp_subcontracting |  | `change.production.qty`, `mrp.bom`, `mrp.consumption.warning`, `mrp.production`, `product.product`, `product.supplierinfo`, `report.mrp.report_bom_structure`, `res.company`, `res.partner`, `stock.location`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.return.picking`, `stock.rule`, `stock.warehouse` |
| mrp_subcontracting_account | Subcontracting Management with Stock Valuation |  | `mrp.production`, `product.product`, `stock.move`, `stock.picking` |
| mrp_subcontracting_dropshipping | Dropship and Subcontracting Management |  | `purchase.order`, `res.company`, `stock.move`, `stock.picking`, `stock.rule`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_subcontracting_purchase | Purchase and Subcontracting Management |  | `purchase.order`, `report.mrp.report_bom_structure`, `stock.move`, `stock.picking` |
| mrp_subcontracting_repair | MRP Subcontracting Repair |  |  |
| mrp_subonctracting_landed_costs | Landed Costs With Subcontracting order |  |  |
| note | Notes | `note.stage`, `note.tag`, `note.note` | `mail.activity.type`, `mail.activity`, `res.users` |
| onboarding | Onboarding toolbox | `onboarding.onboarding`, `onboarding.progress`, `onboarding.progress.step`, `onboarding.onboarding.step` |  |
| partner_autocomplete | Partner Autocomplete | `iap.autocomplete.api`, `res.partner.autocomplete.sync` | `ir.http`, `res.company`, `res.config.settings`, `res.partner` |
| payment | Payment Engine | `payment.icon`, `payment.provider`, `payment.token`, `payment.transaction`, `payment.link.wizard`, `payment.provider.onboarding.wizard` | `ir.http`, `res.company`, `res.partner` |
| payment_adyen | Payment Provider: Adyen |  | `payment.provider`, `payment.token`, `payment.transaction` |
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
| payment_sips | Payment Provider: Worldline SIPS |  | `payment.provider`, `payment.transaction` |
| payment_stripe | Payment Provider: Stripe |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_worldline | Payment Provider: Worldline |  | `payment.provider`, `payment.transaction` |
| phone_validation | Phone Numbers Validation | `mail.thread.phone`, `phone.blacklist`, `phone.blacklist.remove` | `res.partner`, `res.users` |
| point_of_sale | Point of Sale | `pos.bill`, `pos.category`, `pos.config`, `pos.order`, `pos.order.line`, `pos.pack.operation.lot`, `report.point_of_sale.report_saledetails`, `pos.payment`, `pos.payment.method`, `pos.session`, `report.point_of_sale.report_invoice`, `report.pos.order`, `pos.close.session.wizard`, `pos.details.wizard`, `pos.make.payment`, `pos.session.check_product_wizard` | `account.bank.statement.line`, `account.cash.rounding`, `account.chart.template`, `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.tax`, `barcode.rule`, `digest.digest`, `procurement.group`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.rule`, `stock.warehouse`, `uom.category`, `uom.uom` |
| portal | Customer Portal | `portal.mixin`, `portal.share`, `portal.wizard`, `portal.wizard.user` | `ir.http`, `ir.qweb`, `ir.ui.view`, `mail.message`, `mail.thread`, `res.config.settings`, `res.partner`, `res.users.apikeys.description` |
| portal_rating | Portal Rating |  | `ir.http`, `mail.message`, `rating.rating` |
| pos_adyen | POS Adyen |  | `pos.config`, `pos.payment.method`, `pos.session`, `res.config.settings` |
| pos_cache | pos_cache | `pos.cache` | `pos.config`, `pos.session` |
| pos_daily_sales_reports | Point of Sale Daily Sales Reports | `pos.daily.sales.reports.wizard` | `report.point_of_sale.report_saledetails` |
| pos_discount | Point of Sale Discounts |  | `pos.config`, `pos.session`, `res.config.settings` |
| pos_epson_printer | pos_epson_printer |  | `pos.config`, `res.config.settings` |
| pos_epson_printer_restaurant | pos_epson_printer_restaurant |  | `pos.session`, `restaurant.printer` |
| pos_hr | pos_hr |  | `hr.employee.public`, `hr.employee`, `pos.config`, `pos.order`, `pos.session`, `report.pos.order`, `res.config.settings` |
| pos_hr_restaurant | PoS HR Restaurant |  | `pos.order` |
| pos_loyalty | Point of Sale - Coupons & Loyalty |  | `barcode.rule`, `loyalty.card`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.config.settings` |
| pos_mercury | Vantiv Payment Services | `pos_mercury.configuration`, `pos_mercury.mercury_transaction` | `barcode.rule`, `pos.order`, `pos.payment.method`, `pos.payment`, `pos.session` |
| pos_mrp | pos_mrp |  | `pos.order.line`, `pos.order` |
| pos_restaurant | Restaurant | `restaurant.floor`, `restaurant.table`, `restaurant.printer` | `pos.config`, `pos.order.line`, `pos.order`, `pos.payment`, `pos.session`, `res.config.settings` |
| pos_restaurant_adyen | POS Restaurant Adyen |  | `pos.order`, `pos.payment.method`, `pos.payment`, `pos.session` |
| pos_restaurant_stripe | POS Restaurant Stripe |  | `pos.order`, `pos.payment` |
| pos_sale | pos_sale |  | `crm.team`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session`, `res.config.settings`, `sale.order.line`, `sale.order`, `sale.report`, `stock.picking` |
| pos_sale_loyalty | pos_sale_loyalty |  | `sale.order.line` |
| pos_sale_margin | pos_sale_margin |  | `sale.report` |
| pos_sale_product_configurator | pos_sale_product_configurator |  | `pos.session`, `product.product` |
| pos_six | POS Six |  | `pos.config`, `pos.payment.method`, `pos.session` |
| pos_stripe | POS Stripe |  | `pos.payment.method`, `pos.session` |
| privacy_lookup | Privacy | `privacy.log`, `privacy.lookup.wizard`, `privacy.lookup.wizard.line` | `res.partner` |
| product | Products & Pricelists | `product.attribute`, `product.attribute.value`, `product.template.attribute.line`, `product.template.attribute.value`, `product.template.attribute.exclusion`, `product.attribute.custom.value`, `product.category`, `product.packaging`, `product.pricelist`, `product.pricelist.item`, `product.product`, `product.supplierinfo`, `product.tag`, `product.template`, `report.product.report_producttemplatelabel`, `report.product.report_producttemplatelabel_dymo`, `report.product.report_pricelist`, `product.label.layout` | `decimal.precision`, `product.attribute.value`, `product.attribute`, `product.category`, `product.pricelist.item`, `product.pricelist`, `product.product`, `product.supplierinfo`, `product.template.attribute.exclusion`, `product.template.attribute.value`, `product.template`, `res.company`, `res.config.settings`, `res.country.group`, `res.currency`, `res.partner`, `uom.uom` |
| product_email_template | Product Email Template |  | `account.move`, `product.template` |
| product_expiry | Products Expiration Date | `expiry.picking.confirmation` | `procurement.group`, `product.product`, `product.template`, `res.config.settings`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant` |
| product_images | Product Images | `product.fetch.image.wizard` | `ir.cron.trigger`, `product.product`, `res.config.settings` |
| product_margin | Margins by Products | `product.margin` | `product.product` |
| product_matrix | Product Matrix |  | `product.template.attribute.value`, `product.template` |
| project | Project | `project.task.type`, `project.project`, `project.task`, `project.tags`, `project.collaborator`, `project.milestone`, `project.project.stage`, `project.task.recurrence`, `project.task.stage.personal`, `project.update`, `report.project.task.user`, `project.task.burndown.chart.report`, `project.share.wizard`, `project.task.type.delete.wizard` | `account.analytic.account`, `digest.digest`, `ir.ui.menu`, `mail.message`, `project.project`, `project.task.type`, `project.task`, `res.company`, `res.config.settings`, `res.partner` |
| project_hr_expense | Project Expenses |  | `project.project` |
| project_mail_plugin | Project Mail Plugin |  |  |
| project_mrp | MRP Project |  | `project.project` |
| project_purchase | Project Purchase |  | `project.project`, `purchase.order.line` |
| project_sale_expense | Project - Sale - Expense |  | `project.project` |
| project_sms | Project - SMS |  | `project.project.stage`, `project.project`, `project.task.type`, `project.task` |
| project_timesheet_holidays | Timesheet when on Time Off |  | `account.analytic.line`, `hr.employee`, `hr.leave.type`, `hr.leave`, `project.task`, `res.company`, `res.config.settings`, `resource.calendar.leaves` |
| purchase | Purchase | `purchase.order`, `purchase.order.line`, `purchase.bill.union`, `purchase.report` | `account.analytic.account`, `account.analytic.applicability`, `account.move.line`, `account.move`, `mail.compose.message`, `product.packaging`, `product.product`, `product.supplierinfo`, `product.template`, `purchase.order.line`, `purchase.order`, `res.company`, `res.config.settings`, `res.partner` |
| purchase_mrp | Purchase and MRP Management |  | `account.move.line`, `mrp.bom.line`, `mrp.bom`, `mrp.production`, `purchase.order.line`, `purchase.order`, `report.mrp.report_bom_structure`, `stock.move` |
| purchase_price_diff | WMS Accounting |  | `account.move.line`, `product.category`, `product.template` |
| purchase_product_matrix | Purchase Matrix |  | `purchase.order.line`, `purchase.order` |
| purchase_requisition | Purchase Agreements | `purchase.order.group`, `purchase.requisition.type`, `purchase.requisition`, `purchase.requisition.line`, `purchase.requisition.alternative.warning`, `purchase.requisition.create.alternative` | `product.product`, `product.supplierinfo`, `purchase.order.line`, `purchase.order` |
| purchase_requisition_stock | Purchase Requisition Stock |  | `purchase.order.line`, `purchase.order`, `purchase.requisition.create.alternative`, `purchase.requisition.line`, `purchase.requisition`, `stock.move`, `stock.rule`, `stock.warehouse.orderpoint` |
| purchase_stock | Purchase Stock | `vendor.delay.report` | `account.move.line`, `account.move`, `procurement.group`, `product.product`, `product.supplierinfo`, `product.template`, `purchase.order.line`, `purchase.order`, `purchase.report`, `report.stock.report_product_product_replenishment`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.partner`, `stock.lot`, `stock.move`, `stock.picking`, `stock.replenishment.info`, `stock.return.picking`, `stock.rule`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| rating | Customer Rating | `rating.rating`, `rating.mixin`, `rating.parent.mixin` | `mail.message`, `mail.thread` |
| repair | Repairs | `repair.order`, `repair.line`, `repair.fee`, `repair.tags`, `repair.order.make_invoice`, `stock.warn.insufficient.qty.repair` | `account.move.line`, `account.move`, `mail.compose.message`, `product.product`, `stock.lot`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report` |
| resource | Resource | `resource.calendar`, `resource.calendar.attendance`, `resource.resource`, `resource.calendar.leaves`, `resource.mixin` | `res.company`, `res.users`, `resource.calendar` |
| sale | Sales | `sale.order`, `sale.order.line`, `sale.report`, `sale.payment.provider.onboarding.wizard`, `sale.advance.payment.inv`, `sale.order.cancel` | `account.analytic.applicability`, `account.analytic.line`, `account.invoice.report`, `account.move.line`, `account.move`, `account.payment.register`, `crm.team`, `mail.compose.message`, `payment.link.wizard`, `payment.provider`, `payment.transaction`, `product.attribute.custom.value`, `product.attribute.value`, `product.attribute`, `product.packaging`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `sale.order.line`, `sale.order`, `utm.campaign` |
| sale_crm | Opportunity to Quotation | `crm.quotation.partner` | `crm.lead`, `crm.team`, `res.users`, `sale.order` |
| sale_expense | Sales Expense |  | `account.move.line`, `account.move`, `hr.expense.sheet`, `hr.expense.split`, `hr.expense`, `product.template`, `sale.order` |
| sale_expense_margin | Sales Expense Margin |  | `account.move.line`, `sale.order.line` |
| sale_loyalty | Sale Loyalty | `sale.order.coupon.points`, `sale.loyalty.coupon.wizard`, `sale.loyalty.reward.wizard` | `loyalty.card`, `loyalty.program`, `loyalty.reward`, `sale.order.line`, `sale.order` |
| sale_loyalty_delivery | Sale Loyalty - Delivery |  | `sale.order` |
| sale_management | Sales | `sale.order.option`, `sale.order.template`, `sale.order.template.line`, `sale.order.template.option` | `digest.digest`, `res.company`, `res.config.settings`, `sale.order.line`, `sale.order` |
| sale_margin | Margins in Sales Orders |  | `sale.order.line`, `sale.order`, `sale.report` |
| sale_mrp | Sales and MRP Management |  | `account.move.line`, `mrp.bom`, `mrp.production`, `sale.order.line`, `sale.order`, `stock.move.line`, `stock.move` |
| sale_mrp_margin | Sale Mrp Margin |  |  |
| sale_product_configurator | Sale Product Configurator |  | `product.template`, `sale.order.line` |
| sale_product_matrix | Sale Matrix |  | `product.template`, `sale.order.line`, `sale.order` |
| sale_project | Sales - Project |  | `account.move.line`, `product.product`, `product.template`, `project.milestone`, `project.project`, `project.task.recurrence`, `project.task`, `report.project.task.user`, `res.config.settings`, `sale.order.line`, `sale.order.template.line`, `sale.order` |
| sale_project_stock | Sale Project - Sale Stock |  | `sale.order.line` |
| sale_purchase | Sale Purchase |  | `product.template`, `purchase.order.line`, `purchase.order`, `sale.order.cancel`, `sale.order.line`, `sale.order` |
| sale_purchase_stock | MTO Sale <-> Purchase |  | `purchase.order`, `sale.order` |
| sale_quotation_builder | Quotation Builder |  | `product.template`, `res.company`, `sale.order.line`, `sale.order.option`, `sale.order.template.line`, `sale.order.template.option`, `sale.order.template`, `sale.order` |
| sale_sms | Sale - SMS |  |  |
| sale_stock | Sales and Warehouse Management |  | `account.move.line`, `account.move`, `procurement.group`, `product.template`, `report.stock.report_product_product_replenishment`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.users`, `sale.order.cancel`, `sale.order.line`, `sale.order`, `sale.report`, `stock.lot`, `stock.move`, `stock.picking`, `stock.route`, `stock.rule`, `stock.rules.report` |
| sale_stock_margin | Sale Stock Margin |  | `sale.order.line` |
| sale_timesheet | Sales Timesheet | `project.sale.line.employee.map`, `project.create.invoice`, `project.create.sale.order`, `project.create.sale.order.line` | `account.analytic.line`, `account.move.line`, `account.move.reversal`, `account.move`, `product.product`, `product.template`, `project.project`, `project.task.recurrence`, `project.task`, `project.update`, `res.config.settings`, `sale.advance.payment.inv`, `sale.order.line`, `sale.order`, `timesheets.analysis.report` |
| sale_timesheet_margin | Service Margins in Sales Orders |  | `sale.order.line` |
| sales_team | Sales Teams | `crm.tag`, `crm.team`, `crm.team.member` | `res.partner`, `res.users` |
| sms | SMS gateway | `sms.api`, `sms.sms`, `sms.template`, `sms.composer`, `sms.resend.recipient`, `sms.resend`, `sms.template.preview`, `sms.template.reset` | `base`, `ir.actions.server`, `ir.model`, `mail.followers`, `mail.message`, `mail.notification`, `mail.thread.phone`, `mail.thread`, `res.partner` |
| snailmail | Snail Mail | `snailmail.letter`, `snailmail.confirm`, `snailmail.letter.format.error`, `snailmail.letter.missing.required.fields` | `ir.actions.report`, `mail.message`, `mail.notification`, `mail.thread`, `res.company`, `res.config.settings`, `res.partner` |
| snailmail_account | snailmail_account | `snailmail.confirm.invoice` | `account.invoice.send`, `res.company`, `res.config.settings` |
| social_media | Social Media |  | `res.company` |
| spreadsheet | Spreadsheet |  | `res.currency.rate`, `res.currency` |
| spreadsheet_account | Spreadsheet Accounting Formulas |  | `account.account`, `res.company` |
| spreadsheet_dashboard | Spreadsheet dashboard | `spreadsheet.dashboard`, `spreadsheet.dashboard.group` |  |
| spreadsheet_dashboard_account | Spreadsheet dashboard for accounting |  |  |
| spreadsheet_dashboard_event_sale | Spreadsheet dashboard for events |  |  |
| spreadsheet_dashboard_hr_expense | Spreadsheet dashboard for expenses |  |  |
| spreadsheet_dashboard_hr_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_im_livechat | Spreadsheet dashboard for live chat |  |  |
| spreadsheet_dashboard_pos_hr | Spreadsheet dashboard for point of sale |  |  |
| spreadsheet_dashboard_purchase | Spreadsheet dashboard for purchases |  |  |
| spreadsheet_dashboard_purchase_stock | Spreadsheet dashboard for purchases |  |  |
| spreadsheet_dashboard_sale | Spreadsheet dashboard for sales |  |  |
| spreadsheet_dashboard_sale_expense | Spreadsheet dashboard for expenses and sales |  |  |
| spreadsheet_dashboard_sale_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_stock_account | Spreadsheet dashboard for stock |  |  |
| spreadsheet_dashboard_website_sale_slides | Spreadsheet dashboard for eLearning |  |  |
| stock | Inventory | `product.removal`, `stock.putaway.rule`, `stock.location`, `stock.route`, `stock.lot`, `stock.move`, `stock.move.line`, `stock.warehouse.orderpoint`, `stock.package_level`, `stock.package.type`, `stock.picking.type`, `stock.picking`, `stock.quant`, `stock.quant.package`, `stock.rule`, `procurement.group`, `stock.scrap`, `stock.storage.category`, `stock.storage.category.capacity`, `stock.warehouse`, `report.stock.label_product_product_view`, `report.stock.label_lot_template_view`, `report.stock.quantity`, `report.stock.report_reception`, `report.stock.report_stock_rule`, `report.stock.report_product_product_replenishment`, `report.stock.report_product_template_replenishment`, `stock.traceability.report`, `product.replenish`, `stock.assign.serial`, `stock.backorder.confirmation.line`, `stock.backorder.confirmation`, `stock.change.product.qty`, `stock.immediate.transfer.line`, `stock.immediate.transfer`, `stock.inventory.adjustment.name`, `stock.inventory.conflict`, `stock.inventory.warning`, `picking.label.type`, `lot.label.layout`, `stock.orderpoint.snooze`, `stock.package.destination`, `stock.return.picking.line`, `stock.return.picking`, `stock.quantity.history`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.request.count`, `stock.rules.report`, `stock.scheduler.compute`, `stock.track.confirmation`, `stock.track.line`, `stock.warn.insufficient.qty`, `stock.warn.insufficient.qty.scrap` | `barcode.rule`, `product.category`, `product.label.layout`, `product.packaging`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `stock.location`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.putaway.rule`, `stock.quant`, `stock.storage.category`, `stock.warehouse.orderpoint`, `stock.warehouse`, `uom.uom` |
| stock_account | WMS Accounting | `stock.valuation.layer`, `stock.valuation.layer.revaluation` | `account.chart.template`, `account.move.line`, `account.move`, `product.category`, `product.product`, `product.template`, `report.stock.report_product_product_replenishment`, `res.config.settings`, `stock.location`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.quantity.history`, `stock.request.count`, `stock.return.picking.line`, `stock.return.picking` |
| stock_dropshipping | Drop Shipping |  | `procurement.group`, `purchase.order.line`, `purchase.order`, `res.company`, `sale.order.line`, `sale.order`, `stock.lot`, `stock.picking.type`, `stock.picking`, `stock.rule` |
| stock_landed_costs | WMS Landed Costs | `stock.landed.cost`, `stock.landed.cost.lines`, `stock.valuation.adjustment.lines` | `account.move.line`, `account.move`, `product.template`, `purchase.order.line`, `res.company`, `res.config.settings`, `stock.valuation.layer` |
| stock_picking_batch | Warehouse Management: Batch Transfer | `stock.picking.batch`, `stock.add.to.wave`, `stock.picking.to.batch` | `stock.move.line`, `stock.move`, `stock.package.destination`, `stock.picking.type`, `stock.picking`, `stock.warehouse` |
| stock_sms | Stock - SMS | `confirm.stock.sms` | `res.company`, `res.config.settings`, `stock.picking` |
| survey | Surveys | `survey.question`, `survey.question.answer`, `survey.survey`, `survey.user_input`, `survey.user_input.line`, `survey.invite` | `gamification.badge`, `gamification.challenge`, `ir.http`, `res.partner`, `survey.survey` |
| transifex | Transifex integration | `transifex.code.translation`, `transifex.translation` | `base` |
| uom | Units of measure | `uom.category`, `uom.uom` |  |
| utm | UTM Trackers | `utm.campaign`, `utm.medium`, `utm.mixin`, `utm.source`, `utm.source.mixin`, `utm.stage`, `utm.tag` | `ir.http` |
| web | Web | `base.document.layout` | `base`, `ir.actions.act_window.view`, `ir.http`, `ir.model`, `ir.qweb.field.image_url`, `ir.qweb.field.image`, `ir.ui.menu`, `res.company` |
| web_editor | Web Editor | `web_editor.assets`, `web_editor.converter.test`, `web_editor.converter.test.sub` | `base`, `ir.attachment`, `ir.http`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.duration`, `ir.qweb.field.float`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.integer`, `ir.qweb.field.many2one`, `ir.qweb.field.monetary`, `ir.qweb.field.qweb`, `ir.qweb.field.relative`, `ir.qweb.field.selection`, `ir.qweb.field.text`, `ir.qweb.field`, `ir.qweb`, `ir.ui.view`, `ir.websocket` |
| web_kanban_gauge | Gauge Widget for Kanban |  |  |
| web_tour | Tours | `web_tour.tour` | `ir.http` |
| web_unsplash | Unsplash Image Library |  | `ir.attachment`, `ir.qweb.field.image`, `res.config.settings`, `res.users` |
| website | Website | `ir.module.module`, `website.seo.metadata`, `website.cover_properties.mixin`, `website.multi.mixin`, `website.published.mixin`, `website.published.multi.mixin`, `website.searchable.mixin`, `theme.ir.asset`, `theme.ir.ui.view`, `theme.ir.attachment`, `theme.website.menu`, `theme.website.page`, `theme.utils`, `website`, `website.configurator.feature`, `website.menu`, `website.page`, `website.route`, `website.rewrite`, `website.snippet.filter`, `website.track`, `website.visitor`, `website.robots` | `base.language.install`, `base.partner.merge.automatic.wizard`, `base`, `ir.actions.server`, `ir.asset`, `ir.attachment`, `ir.binary`, `ir.http`, `ir.model.data`, `ir.model.fields`, `ir.model`, `ir.qweb.field.contact`, `ir.qweb.field.html`, `ir.qweb`, `ir.rule`, `ir.ui.menu`, `ir.ui.view`, `portal.wizard.user`, `res.company`, `res.config.settings`, `res.lang`, `res.partner`, `res.users`, `web_editor.assets`, `website.menu`, `website.page`, `website` |
| website_blog | Blogs | `blog.blog`, `blog.tag.category`, `blog.tag`, `blog.post` | `ir.qweb.field`, `website.snippet.filter`, `website` |
| website_crm | Contact Form |  | `crm.lead`, `website.visitor`, `website` |
| website_crm_iap_reveal | Lead Generation From Website Visits | `crm.reveal.rule`, `crm.reveal.view` | `crm.lead`, `ir.http` |
| website_crm_livechat | Lead Livechat Sessions |  | `chatbot.script.step`, `crm.lead`, `mail.channel` |
| website_crm_partner_assign | Resellers | `res.partner.activation`, `res.partner.grade`, `crm.partner.report.assign`, `crm.lead.forward.to.partner`, `crm.lead.assignation` | `crm.lead`, `res.partner`, `website` |
| website_crm_sms | Send SMS to Visitor with leads |  | `website.visitor` |
| website_customer | Customer References | `res.partner.tag` | `res.partner`, `website` |
| website_event | Events | `website.event.menu` | `event.event`, `event.registration`, `event.tag.category`, `event.type`, `website.menu`, `website.snippet.filter`, `website.visitor`, `website` |
| website_event_booth | Online Event Booths |  | `event.event`, `event.type`, `website.event.menu` |
| website_event_booth_exhibitor | Booths/Exhibitors Bridge |  | `event.booth.category`, `event.booth` |
| website_event_booth_sale | Online Event Booth Sale |  | `product.product`, `product.template`, `sale.order`, `website` |
| website_event_booth_sale_exhibitor | Booths Sale/Exhibitors Bridge |  | `event.booth.registration` |
| website_event_crm | Website Events CRM |  |  |
| website_event_crm_questions | Website Event CRM Questions |  | `event.registration` |
| website_event_exhibitor | Event Exhibitors | `event.sponsor`, `event.sponsor.type` | `event.event`, `event.type`, `website.event.menu` |
| website_event_jitsi | Event / Jitsi |  | `res.config.settings` |
| website_event_meet | Event Meeting / Rooms | `event.meeting.room` | `event.event`, `event.type`, `website.event.menu` |
| website_event_meet_quiz | Quiz and Meet on community |  |  |
| website_event_questions | Questions on Events | `event.question`, `event.question.answer`, `event.registration.answer` | `event.event`, `event.registration`, `event.type` |
| website_event_sale | Online Event Ticketing |  | `event.sale.report`, `product.pricelist.item`, `product.product`, `product.template`, `sale.order.line`, `sale.order`, `website` |
| website_event_track | Advanced Events | `event.track`, `event.track.location`, `event.track.stage`, `event.track.tag`, `event.track.tag.category`, `event.track.visitor` | `event.event`, `event.type`, `res.config.settings`, `website.event.menu`, `website.menu`, `website.visitor`, `website` |
| website_event_track_live | Live Event Tracks |  | `event.track` |
| website_event_track_live_quiz | Quiz on Live Event Tracks |  |  |
| website_event_track_quiz | Quizzes on Tracks | `event.quiz`, `event.quiz.question`, `event.quiz.answer` | `event.event`, `event.track.visitor`, `event.track` |
| website_form_project | Online Task Submission |  |  |
| website_forum | Forum | `forum.forum`, `forum.post`, `forum.post.reason`, `forum.post.vote`, `forum.tag` | `gamification.challenge`, `ir.attachment`, `res.users`, `website` |
| website_google_map | Google Maps |  |  |
| website_hr_recruitment | Online Jobs |  | `hr.applicant`, `hr.department`, `hr.job`, `hr.recruitment.source`, `website` |
| website_jitsi | Website Jitsi | `chat.room`, `chat.room.mixin` |  |
| website_links | Link Tracker |  | `link.tracker` |
| website_livechat | Website Live Chat |  | `chatbot.script.step`, `chatbot.script`, `im_livechat.channel`, `ir.http`, `mail.channel`, `res.config.settings`, `website.visitor`, `website` |
| website_mail | Website Mail |  | `publisher_warranty.contract` |
| website_mail_group | Website Mail Group |  | `mail.group` |
| website_mass_mailing | Newsletter Subscribe Button |  | `res.company` |
| website_mass_mailing_sms | Newsletter Subscribe SMS Template |  |  |
| website_membership | Online Members Directory |  | `membership.membership_line`, `website` |
| website_partner | Website Partner |  | `res.partner` |
| website_payment | Website Payment |  | `account.payment`, `payment.provider`, `payment.transaction`, `res.config.settings`, `res.country` |
| website_payment_authorize | Website - Payment Authorize |  | `res.config.settings` |
| website_payment_paypal | Website - Payment Paypal |  | `res.config.settings` |
| website_profile | Website profile |  | `gamification.badge`, `res.users`, `website` |
| website_sale | eCommerce | `product.image`, `product.public.category`, `product.ribbon`, `website.sale.extra.field`, `website.base.unit` | `account.move`, `crm.team`, `digest.digest`, `ir.http`, `mail.compose.message`, `payment.provider`, `product.attribute`, `product.pricelist`, `product.product`, `product.tag`, `product.template.attribute.line`, `product.template`, `res.company`, `res.config.settings`, `res.country`, `res.partner`, `sale.order.line`, `sale.order`, `sale.report`, `website.snippet.filter`, `website.track`, `website.visitor`, `website` |
| website_sale_autocomplete | Google places autocompletion |  | `res.config.settings`, `website` |
| website_sale_comparison | Product Comparison | `product.attribute.category` | `product.attribute`, `product.product`, `product.template.attribute.line` |
| website_sale_comparison_wishlist | Product Availability Notifications |  |  |
| website_sale_delivery | eCommerce Delivery |  | `delivery.carrier`, `res.country`, `sale.order.line`, `sale.order` |
| website_sale_delivery_mondialrelay | website_sale_delivery_mondialrelay |  | `website` |
| website_sale_digital | Digital Products |  | `account.move.line`, `ir.attachment`, `product.product`, `product.template` |
| website_sale_loyalty | Coupons, Promotions, Gift Card and Loyalty for eCommerce | `coupon.share` | `loyalty.card`, `loyalty.program`, `loyalty.rule`, `sale.order.line`, `sale.order` |
| website_sale_loyalty_delivery | Free Delivery with Coupon & Loyalty on eCommerce |  |  |
| website_sale_picking | On site Payment & Picking |  | `delivery.carrier`, `payment.provider`, `res.config.settings`, `website` |
| website_sale_product_configurator | Website Sale Product Configurator |  | `sale.order`, `website` |
| website_sale_slides | Sell Courses |  | `product.product`, `product.template`, `sale.order`, `slide.channel`, `website` |
| website_sale_stock | Product Availability |  | `product.product`, `product.template`, `res.config.settings`, `sale.order.line`, `sale.order`, `stock.picking`, `website` |
| website_sale_stock_product_configurator | Website Sale Stock Product Configurator |  |  |
| website_sale_stock_wishlist | Product Availability Notifications |  | `product.template`, `product.wishlist` |
| website_sale_wishlist | Shopper's Wishlist | `product.wishlist` | `product.product`, `product.template`, `res.partner`, `res.users` |
| website_slides | eLearning | `slide.channel.partner`, `slide.channel`, `slide.channel.tag.group`, `slide.channel.tag`, `slide.embed`, `slide.question`, `slide.answer`, `slide.slide.partner`, `slide.tag`, `slide.slide`, `slide.slide.resource`, `slide.channel.invite` | `gamification.challenge`, `ir.binary`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `website` |
| website_slides_forum | Forum on Courses |  | `forum.forum`, `slide.channel` |
| website_slides_survey | Course Certifications |  | `slide.channel`, `slide.slide.partner`, `slide.slide`, `survey.survey`, `survey.user_input` |
| website_sms | Send SMS to Visitor |  | `website.visitor` |
| website_twitter | Twitter Snippet | `website.twitter.tweet` | `res.config.settings`, `website` |
