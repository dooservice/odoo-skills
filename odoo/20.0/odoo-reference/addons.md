# Addons

| Addon | Name | Defines | Extends |
|---|---|---|---|
| base | Base | `avatar.mixin`, `clearing.label`, `decimal.precision`, `image.mixin`, `ir.access`, `ir.actions.actions`, `ir.actions.act_window`, `ir.actions.act_window.view`, `ir.actions.act_window_close`, `ir.actions.act_url`, `server.action.history.wizard`, `ir.actions.server.history`, `ir.actions.server`, `ir.actions.todo`, `ir.actions.client`, `ir.actions.report`, `ir.asset`, `ir.attachment`, `ir.autovacuum`, `ir.binary`, `ir.config_parameter`, `ir.cron`, `ir.cron.trigger`, `ir.cron.progress`, `ir.default`, `ir.demo`, `ir.demo_failure`, `ir.demo_failure.wizard`, `ir.embedded.actions`, `ir.exports`, `ir.exports.line`, `ir.fields.converter`, `ir.filters`, `ir.http`, `ir.logging`, `ir.mail_server`, `base`, `_unknown`, `ir.model`, `ir.model.fields`, `ir.model.inherit`, `ir.model.fields.selection`, `ir.model.constraint`, `ir.model.relation`, `ir.model.data`, `ir.module.category`, `ir.module.module`, `ir.module.module.dependency`, `ir.module.module.exclusion`, `ir.profile`, `base.enable.profiling.wizard`, `ir.profile.query`, `ir.qweb`, `ir.qweb.field`, `ir.qweb.field.integer`, `ir.qweb.field.float`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.text`, `ir.qweb.field.selection`, `ir.qweb.field.many2one`, `ir.qweb.field.many2many`, `ir.qweb.field.one2many`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.image_url`, `ir.qweb.field.monetary`, `ir.qweb.field.float_time`, `ir.qweb.field.time`, `ir.qweb.field.duration`, `ir.qweb.field.relative`, `ir.qweb.field.barcode`, `ir.qweb.field.contact`, `ir.qweb.field.qweb`, `ir.sequence`, `ir.sequence.date_range`, `ir.ui.menu`, `ir.ui.view.custom`, `ir.ui.view`, `reset.view.arch.wizard`, `properties.base.definition`, `properties.base.definition.mixin`, `report.layout`, `report.paperformat`, `res.company`, `res.config`, `res.config.settings`, `res.country`, `res.country.group`, `res.country.state`, `res.currency`, `res.currency.rate`, `res.device.log`, `res.device`, `res.session`, `res.groups`, `res.groups.privilege`, `res.lang`, `format.vat.label.mixin`, `format.address.mixin`, `res.partner.category`, `res.partner`, `res.partner.industry`, `res.partner.bank`, `res.users.log`, `res.users`, `res.users.identitycheck`, `change.password.wizard`, `change.password.user`, `change.password.own`, `res.users.apikeys`, `res.users.apikeys.description`, `res.users.apikeys.show`, `res.users.deletion`, `res.users.settings`, `website`, `report.base.report_irmodulereference`, `base.language.export`, `base.language.import`, `base.language.install`, `base.module.uninstall`, `base.module.update`, `base.module.upgrade`, `base.partner.merge.line`, `base.partner.merge.automatic.wizard`, `wizard.ir.model.menu.create` | `base`, `res.users` |
| account | Invoicing | `account.account`, `account.account.tag`, `account.bank.statement`, `account.bank.statement.line`, `account.cash.rounding`, `account.code.mapping`, `account.document.import.mixin`, `account.full.reconcile`, `account.incoterms`, `account.journal.group`, `account.journal`, `account.lock_exception`, `account.move`, `account.move.line`, `account.move.send`, `account.partial.reconcile`, `account.payment`, `account.payment.method`, `account.payment.method.line`, `account.payment.term`, `account.payment.term.line`, `account.reconcile.model.line`, `account.reconcile.model`, `account.report`, `account.report.line`, `account.report.expression`, `account.report.column`, `account.report.external.value`, `account.root`, `account.tax.group`, `account.tax`, `account.tax.repartition.line`, `account.chart.template`, `account.fiscal.position`, `account.fiscal.position.account`, `res.currency.rate.consolidation.mixin`, `sequence.mixin`, `report.account.report_hash_integrity`, `account.invoice.report`, `report.account.report_invoice`, `report.account.report_invoice_with_payments`, `account.stock.valuation.report`, `account.automatic.entry.wizard`, `account.autopost.bills.wizard`, `account.merge.wizard`, `account.merge.wizard.line`, `account.move.reversal`, `account.move.send.batch.wizard`, `account.move.send.wizard`, `account.payment.register`, `account.resequence.wizard`, `account.secure.entries.wizard`, `validate.account.move`, `account.accrued.orders.wizard`, `account.financial.year.op`, `account.setup.bank.manual.config` | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.distribution.model`, `account.analytic.line`, `account.chart.template`, `account.journal`, `account.move.line`, `account.move`, `base.document.layout`, `base.partner.merge.automatic.wizard`, `decimal.precision`, `digest.digest`, `ir.actions.report`, `ir.attachment`, `ir.http`, `ir.module.module`, `kpi.provider`, `mail.compose.message`, `mail.message`, `mail.template`, `onboarding.onboarding.step`, `onboarding.onboarding`, `product.catalog.line.mixin`, `product.catalog.mixin`, `product.category`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.country.group`, `res.currency.rate`, `res.currency`, `res.groups`, `res.partner.bank`, `res.partner`, `uom.uom` |
| account_check_printing | Check Printing Base | `print.prenumbered.checks` | `account.journal`, `account.payment.method`, `account.payment`, `res.company`, `res.config.settings` |
| account_debit_note | Debit Notes | `account.debit.note` | `account.journal`, `account.move` |
| account_edi | Import/Export Invoices From XML/PDF | `account.edi.document`, `account.edi.format` | `account.journal`, `account.move.send`, `account.move`, `account.resequence.wizard`, `ir.actions.report`, `ir.attachment` |
| account_edi_proxy_client | Proxy features for account_edi | `account_edi_proxy_client.user` | `res.company` |
| account_edi_ubl_cii | Import/Export electronic invoices with UBL/CII | `account.edi.cii`, `account.edi.common`, `account.edi.ubl`, `account.edi.ubl_cen_en16931`, `account.edi.ubl_pint`, `account.edi.ubl_pint_eu`, `account.edi.xml.cii`, `account.edi.xml.ubl_20`, `account.edi.xml.ubl_21`, `account.edi.xml.ubl_a_nz`, `account.edi.xml.ubl_bis3`, `account.edi.xml.ubl_efff`, `account.edi.xml.ubl_nl`, `account.edi.xml.ubl_sg`, `account.edi.xml.ubl_de` | `account.move.send.wizard`, `account.move.send`, `account.move`, `account.tax`, `ir.actions.report`, `res.company`, `res.partner`, `uom.uom` |
| account_fleet | Accounting/Fleet bridge |  | `account.account`, `account.automatic.entry.wizard`, `account.move.line`, `account.move`, `account.tax`, `fleet.vehicle.log.services`, `fleet.vehicle` |
| account_payment | Payment - Account | `payment.refund.wizard` | `account.bank.statement.line`, `account.journal`, `account.move`, `account.payment.method.line`, `account.payment.method`, `account.payment.register`, `account.payment`, `payment.link.wizard`, `payment.provider`, `payment.transaction`, `res.config.settings` |
| account_payment_custom | Payment Custom / Account Payment |  | `account.bank.statement.line`, `account.payment.method`, `payment.provider`, `payment.transaction` |
| account_payment_interco | Intercompany Payment - Account |  | `account.move`, `res.company`, `res.config.settings` |
| account_peppol | Peppol | `account.peppol.clarification`, `account.peppol.response`, `peppol.registration`, `account.peppol.rejection.wizard` | `account.edi.common`, `account.edi.ubl`, `account.journal`, `account.move.send.batch.wizard`, `account.move.send.wizard`, `account.move.send`, `account.move`, `account_edi_proxy_client.user`, `res.company`, `res.config.settings`, `res.partner` |
| account_qr_code_emv | account_qr_code_emv |  | `res.partner.bank` |
| account_qr_code_sepa | Account SEPA QR Code |  | `res.partner.bank` |
| account_tax_python | Define Taxes as Python Code |  | `account.tax` |
| account_test | Accounting Consistency Tests | `accounting.assert.test`, `report.account_test.report_accounttest` |  |
| account_update_tax_tags | Account - Allow updating tax grids | `account.update.tax.tags.wizard` |  |
| analytic | Analytic Accounting | `account.analytic.account`, `account.analytic.distribution.model`, `analytic.plan.fields.mixin`, `account.analytic.line`, `analytic.mixin`, `account.analytic.plan`, `account.analytic.applicability` | `ir.config_parameter`, `res.config.settings`, `res.groups` |
| api_doc | API Documentation |  | `ir.attachment` |
| attachment_indexation | Attachments List and Document Indexation |  | `ir.attachment` |
| auth_ldap | Authentication via LDAP | `res.company.ldap` | `res.company`, `res.config.settings`, `res.users` |
| auth_oauth | OAuth2 Authentication | `auth.oauth.provider` | `ir.config_parameter`, `res.config.settings`, `res.users` |
| auth_passkey | Passkeys | `auth.passkey.key`, `auth.passkey.key.create` | `res.users.identitycheck`, `res.users` |
| auth_passkey_portal | Passkeys Portal |  |  |
| auth_password_policy | Password Policy |  | `res.config.settings`, `res.users` |
| auth_password_policy_portal | Password Policy support for Signup |  | `ir.http` |
| auth_password_policy_signup | Password Policy support for Signup |  | `ir.http` |
| auth_signup | Signup |  | `ir.http`, `res.config.settings`, `res.partner`, `res.users` |
| auth_timeout | Auth Timeout |  | `auth_totp.device`, `ir.http`, `ir.websocket`, `res.groups`, `res.users` |
| auth_totp | Two-Factor Authentication (TOTP) | `auth_totp.device`, `auth.totp.rate.limit.log`, `auth_totp.wizard` | `ir.http`, `res.users` |
| auth_totp_mail | 2FA Invite mail |  | `auth_totp.device`, `ir.http`, `res.config.settings`, `res.users` |
| auth_totp_portal | TOTPortal |  | `res.users` |
| barcodes | Barcode | `barcode.nomenclature`, `barcode.rule` | `ir.http`, `res.company` |
| barcodes_gs1_nomenclature | Barcode - GS1 Nomenclature |  | `barcode.nomenclature`, `barcode.rule`, `ir.http` |
| base_address_extended | Extended Addresses | `res.city` | `res.country`, `res.partner` |
| base_automation | Automation Rules | `base.automation` | `ir.actions.server`, `ir.cron` |
| base_geolocalize | Partners Geolocation | `base.geo_provider`, `base.geocoder` | `res.config.settings`, `res.partner` |
| base_import | Base import | `base_import.mapping`, `base_import.import` | `base`, `res.users` |
| base_import_module | Base import module | `base.import.module` | `ir.http`, `ir.module.module`, `ir.ui.view` |
| base_install_request | Base - Module Install Request | `base.module.install.request`, `base.module.install.review` | `ir.module.module` |
| base_report_paper_muncher | Report Engine: Paper Muncher |  | `ir.actions.report` |
| base_report_wkhtmltox | Report Engine: wkhtmltopdf/wkhtmltoimage |  | `ir.actions.report` |
| base_setup | Initial Setup Tools | `kpi.provider` | `ir.http`, `res.config.settings`, `res.users` |
| base_sparse_field | Sparse Fields | `sparse_fields.test` | `base`, `ir.model.fields` |
| board | Dashboards | `board.board` |  |
| bus | IM Bus | `bus.bus`, `bus.listener.mixin`, `ir.websocket` | `ir.attachment`, `ir.http`, `ir.model`, `ir.qweb`, `res.groups`, `res.partner`, `res.users.settings`, `res.users` |
| calendar | Calendar | `calendar.alarm`, `calendar.alarm_manager`, `calendar.attendee`, `calendar.calendar`, `calendar.event`, `calendar.event.type`, `calendar.filters`, `calendar.recurrence`, `calendar.user`, `calendar.event.archive.or.unlink.wizard`, `calendar.event.multi.archive.or.unlink.wizard` | `discuss.channel`, `ir.http`, `mail.activity.mixin`, `mail.activity.schedule`, `mail.activity.type`, `mail.activity`, `res.partner`, `res.users.settings`, `res.users` |
| calendar_sms | Calendar - SMS |  | `calendar.alarm_manager`, `calendar.alarm`, `calendar.event` |
| certificate | Certificate | `certificate.certificate`, `certificate.key` |  |
| cloud_storage | Cloud Storage |  | `ir.attachment`, `ir.http`, `res.config.settings` |
| cloud_storage_azure | Cloud Storage Azure |  | `ir.attachment`, `res.config.settings` |
| cloud_storage_google | Cloud Storage Google |  | `ir.attachment`, `res.config.settings` |
| cloud_storage_migration | Cloud Storage Migration | `cloud.storage.migration.report` | `ir.attachment`, `res.config.settings` |
| contacts | Contacts |  | `res.partner`, `res.users` |
| crm | CRM | `crm.lead`, `crm.lead.scoring.frequency`, `crm.lead.scoring.frequency.field`, `crm.lost.reason`, `crm.recurring.plan`, `crm.stage`, `crm.activity.report`, `crm.lead.lost`, `crm.lead.pls.update`, `crm.lead2opportunity.partner.mass`, `crm.merge.opportunity` | `calendar.event`, `crm.team.member`, `crm.team`, `digest.digest`, `discuss.channel`, `ir.config_parameter`, `mail.activity`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `utm.campaign` |
| crm_iap_enrich | Lead Enrichment |  | `crm.lead`, `res.config.settings` |
| crm_iap_mine | Lead Generation | `crm.iap.lead.helpers`, `crm.iap.lead.industry`, `crm.iap.lead.industry.division`, `crm.iap.lead.mining.request`, `crm.iap.lead.role`, `crm.iap.lead.seniority` | `crm.lead` |
| crm_livechat | CRM Livechat |  | `chatbot.script.step`, `chatbot.script`, `crm.lead`, `discuss.channel`, `im_livechat.report.channel`, `res.users` |
| crm_mail_plugin | CRM Mail Plugin |  |  |
| crm_sale_project | CRM - Project |  | `crm.lead`, `project.project`, `project.template.create.wizard`, `sale.order` |
| crm_sms | SMS in CRM |  |  |
| data_recycle | Data Recycle | `data_recycle.model`, `data_recycle.record` |  |
| delivery | Delivery Costs | `delivery.carrier`, `delivery.price.rule`, `delivery.zip.prefix`, `choose.delivery.carrier`, `delivery.note.wizard`, `delivery.note.wizard.line` | `ir.http`, `ir.module.module`, `payment.method`, `payment.provider`, `payment.transaction`, `product.category`, `res.config.settings`, `res.partner`, `sale.order.line`, `sale.order` |
| digest | KPI Digests | `digest.digest`, `digest.tip`, `digest.test` | `res.config.settings`, `res.users` |
| event | Events Organization | `event.event`, `event.mail`, `event.mail.registration`, `event.mail.slot`, `event.question`, `event.question.answer`, `event.registration`, `event.registration.answer`, `event.slot`, `event.stage`, `event.tag.category`, `event.tag`, `event.event.ticket`, `event.type`, `event.type.mail`, `event.type.ticket` | `digest.digest`, `mail.template`, `res.config.settings`, `res.partner` |
| event_booth | Events Booths | `event.booth`, `event.booth.category`, `event.type.booth` | `event.event`, `event.type` |
| event_booth_sale | Events Booths Sales | `event.booth.registration`, `event.booth.configurator` | `account.move`, `event.booth.category`, `event.booth`, `event.type.booth`, `product.product`, `product.template`, `sale.order.line`, `sale.order` |
| event_crm | Event CRM | `event.lead.request`, `event.lead.rule` | `crm.lead`, `event.event`, `event.question.answer`, `event.registration` |
| event_crm_sale | Event CRM Sale |  | `event.registration` |
| event_product | Events Product |  | `event.event.ticket`, `event.event`, `event.registration`, `event.type.ticket`, `product.product`, `product.template` |
| event_sale | Events Sales | `event.sale.report`, `event.event.configurator`, `registration.editor`, `registration.editor.line` | `event.event.ticket`, `event.event`, `event.registration`, `product.template`, `sale.order.line`, `sale.order` |
| event_sms | SMS on Events |  | `event.mail.registration`, `event.mail`, `event.type.mail`, `sms.template` |
| fleet | Fleet | `fleet.service.type`, `fleet.vehicle`, `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.model`, `fleet.vehicle.model.brand`, `fleet.vehicle.model.category`, `fleet.vehicle.odometer`, `fleet.vehicle.state`, `fleet.vehicle.tag`, `fleet.vehicle.cost.report`, `fleet.vehicle.odometer.report`, `fleet.vehicle.send.mail` | `mail.activity.type`, `res.config.settings`, `res.partner` |
| fleet_maintenance | Maintenance - Fleet |  | `fleet.vehicle`, `maintenance.equipment` |
| gamification | Gamification | `gamification.badge`, `gamification.badge.user`, `gamification.challenge`, `gamification.challenge.line`, `gamification.goal`, `gamification.goal.definition`, `gamification.karma.rank`, `gamification.karma.tracking`, `gamification.badge.user.wizard`, `gamification.goal.wizard` | `res.users` |
| gamification_sale_crm | CRM Gamification |  |  |
| google_account | Google Users | `google.service` |  |
| google_address_autocomplete | Google Address Autocomplete |  | `res.config.settings`, `res.partner` |
| google_calendar | Google Calendar | `google.event.sync`, `google.sync`, `google.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.calendar`, `calendar.event`, `calendar.recurrence`, `calendar.user`, `res.config.settings`, `res.users.settings`, `res.users` |
| google_gmail | Google Gmail | `google.gmail.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings`, `res.users` |
| google_recaptcha | Google reCAPTCHA integration |  | `ir.http`, `res.config.settings` |
| hr | Employees | `hr.department`, `hr.departure.reason`, `hr.employee`, `hr.employee.category`, `hr.employee.departure`, `hr.employee.location`, `hr.employee.public`, `hr.employee.type`, `hr.job`, `hr.mixin`, `hr.payroll.structure.type`, `hr.version`, `hr.work.location`, `hr.manager.department.report`, `hr.bank.account.allocation.wizard.line`, `hr.bank.account.allocation.wizard`, `hr.employee.create.version.wizard` | `base`, `discuss.channel`, `ir.ui.menu`, `mail.activity.plan.template`, `mail.activity.plan`, `mail.activity.schedule`, `mail.activity`, `mail.alias`, `publisher_warranty.contract`, `res.company`, `res.config.settings`, `res.partner.bank`, `res.partner`, `res.users`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource` |
| hr_address_extended | HR Address Extended |  | `hr.employee`, `hr.version` |
| hr_attendance | Attendances | `hr.attendance` | `hr.employee.public`, `hr.employee`, `hr.time.rule`, `hr.version`, `ir.http`, `ir.websocket`, `res.company`, `res.config.settings`, `res.groups`, `res.users` |
| hr_calendar | Display Working Hours in Calendar | `homework.location.wizard` | `calendar.event`, `hr.employee`, `res.partner` |
| hr_calendar_google | HR Calendar with Google Calendar |  | `google.event.sync`, `res.users` |
| hr_expense | Expenses | `hr.expense`, `hr.expense.product.job.position.limit`, `hr.expense.approve.duplicate`, `hr.expense.refuse.wizard`, `hr.expense.split`, `hr.expense.split.wizard` | `account.analytic.account`, `account.analytic.applicability`, `account.journal`, `account.move.line`, `account.move`, `account.payment.register`, `account.payment`, `account.tax`, `hr.department`, `hr.employee.public`, `hr.employee`, `ir.actions.report`, `ir.attachment`, `product.product`, `product.template`, `res.company`, `res.config.settings` |
| hr_fleet | Fleet History |  | `fleet.vehicle.assignation.log`, `fleet.vehicle.log.contract`, `fleet.vehicle.log.services`, `fleet.vehicle.odometer`, `fleet.vehicle`, `hr.employee.departure`, `hr.employee.public`, `hr.employee`, `ir.attachment` |
| hr_gamification | HR Gamification |  | `gamification.badge.user.wizard`, `gamification.badge.user`, `gamification.badge`, `hr.employee.public`, `hr.employee`, `res.users` |
| hr_holidays | Time Off | `hr.leave`, `hr.leave.accrual.plan`, `hr.leave.accrual.level`, `hr.leave.allocation`, `hr.leave.display.name.mixin`, `hr.leave.mandatory.day`, `hr.time.rule.allocation.log`, `report.hr_holidays.report_holidayssummary`, `hr.leave.employee.report`, `hr.leave.employee.type.report`, `hr.leave.report`, `hr.leave.report.calendar`, `hr.holidays.cancel.leave`, `hr.holidays.summary.employee`, `hr.leave.allocation.generate.multi.wizard`, `hr.leave.generate.multi.wizard`, `load.public.holiday.wizard`, `load.public.holiday.wizard.line` | `calendar.event`, `hr.department`, `hr.employee.departure`, `hr.employee.public`, `hr.employee`, `hr.time.rule.source.mixin`, `hr.time.rule`, `hr.version`, `hr.work.entry.type`, `mail.activity.type`, `mail.message.subtype`, `res.company`, `res.groups`, `res.partner`, `res.users`, `resource.calendar.leaves`, `resource.calendar`, `resource.resource` |
| hr_holidays_attendance | HR Attendance Holidays | `hr.leave.attendance.report` | `hr.attendance`, `hr.employee`, `hr.leave.accrual.level`, `hr.leave.allocation`, `hr.leave`, `hr.time.rule`, `hr.version`, `ir.ui.menu`, `res.company`, `resource.calendar.leaves` |
| hr_livechat | HR - Livechat |  |  |
| hr_maintenance | Maintenance - HR |  | `hr.employee.departure`, `hr.employee.public`, `hr.employee`, `maintenance.equipment`, `maintenance.request` |
| hr_presence | Employee Presence Control |  | `hr.employee.public`, `hr.employee`, `ir.websocket`, `res.company`, `res.config.settings`, `res.users.log` |
| hr_recruitment | Recruitment | `hr.applicant`, `hr.applicant.category`, `hr.applicant.refuse.reason`, `hr.job.platform`, `hr.job.tag`, `hr.recruitment.degree`, `hr.recruitment.source`, `hr.recruitment.stage`, `hr.talent.pool`, `applicant.get.refuse.reason`, `applicant.refuse.single`, `job.add.applicants`, `talent.pool.add.applicants` | `calendar.event`, `digest.digest`, `hr.department`, `hr.employee`, `hr.job`, `ir.attachment`, `ir.ui.menu`, `mail.activity.plan`, `mail.activity.schedule`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `utm.campaign`, `utm.source` |
| hr_recruitment_skills | Recruitment - Skills Management | `hr.applicant.skill` | `hr.applicant`, `hr.job` |
| hr_recruitment_sms | Recruitment - SMS |  | `hr.applicant` |
| hr_recruitment_survey | Hr Recruitment Interview Forms | `hr.recruitment.survey.invite` | `hr.applicant`, `hr.job`, `survey.survey`, `survey.user_input` |
| hr_skills | Skills Management | `hr.employee.skill`, `hr.individual.skill.mixin`, `hr.job.skill`, `hr.resume.line`, `hr.resume.line.type`, `hr.skill`, `hr.skill.level`, `hr.skill.type`, `report.hr_skills.report_employee_cv`, `hr.employee.skill.history.report`, `hr.employee.skill.report`, `hr.employee.cv.wizard` | `hr.employee.public`, `hr.employee`, `hr.job`, `resource.resource` |
| hr_skills_event | Skills Events |  | `event.event`, `hr.resume.line` |
| hr_skills_slides | Skills e-learning |  | `hr.employee.public`, `hr.employee`, `hr.resume.line`, `slide.channel.partner`, `slide.channel` |
| hr_skills_survey | Skills Certification |  | `hr.resume.line`, `survey.survey`, `survey.user_input` |
| hr_timesheet | Task Logs | `account.analytic.line.calendar.employee`, `timesheets.analysis.report`, `hr.employee.delete.wizard` | `account.analytic.applicability`, `account.analytic.line`, `hr.employee.departure`, `hr.employee.public`, `hr.employee`, `ir.http`, `ir.ui.menu`, `project.collaborator`, `project.project`, `project.task`, `project.update`, `report.project.task.user`, `res.company`, `res.config.settings`, `uom.uom` |
| hr_timesheet_attendance | Timesheets/attendances reporting | `hr.timesheet.attendance.report` | `ir.ui.menu` |
| hr_work_entry | Work Entries | `hr.time.rule`, `hr.time.rule.source.mixin`, `hr.user.work.entry.employee`, `hr.work.entry.type`, `hr.export.work.entries`, `hr.export.work.entries.employee` | `hr.employee`, `hr.version`, `res.company`, `res.config.settings`, `resource.calendar.attendance`, `resource.calendar.leaves`, `resource.calendar` |
| html_builder | HTML Builder |  | `ir.qweb`, `ir.ui.view` |
| html_editor | HTML Editor | `html.field.history.mixin`, `html_editor.converter.test`, `html_editor.converter.test.sub` | `base`, `ir.attachment`, `ir.http`, `ir.qweb.field.contact`, `ir.qweb.field.date`, `ir.qweb.field.datetime`, `ir.qweb.field.duration`, `ir.qweb.field.float`, `ir.qweb.field.html`, `ir.qweb.field.image`, `ir.qweb.field.integer`, `ir.qweb.field.many2one`, `ir.qweb.field.monetary`, `ir.qweb.field.selection`, `ir.qweb.field.text`, `ir.qweb.field`, `ir.qweb`, `ir.ui.view`, `ir.websocket` |
| http_routing | Web Routing |  | `ir.http`, `ir.qweb`, `res.lang` |
| iap | In-App Purchase | `iap.account`, `iap.enrich.api`, `iap.service`, `iap.service.pack` |  |
| iap_crm | IAP / CRM |  | `crm.lead` |
| iap_mail | IAP / Mail |  | `iap.account` |
| im_livechat | Live Chat | `chatbot.message`, `chatbot.script`, `chatbot.script.answer`, `chatbot.script.step`, `im_livechat.channel`, `im_livechat.channel.rule`, `im_livechat.channel.member.history`, `im_livechat.expertise`, `im_livechat.report.channel` | `digest.digest`, `discuss.call.history`, `discuss.channel.member`, `discuss.channel.rtc.session`, `discuss.channel`, `ir.http`, `ir.qweb`, `ir.websocket`, `mail.message`, `res.groups`, `res.partner`, `res.users.settings`, `res.users`, `utm.mixin` |
| iot_drivers | Hardware Proxy |  |  |
| iot_webserial | Web Serial IoT devices |  |  |
| link_tracker | Link Tracker | `link.tracker`, `link.tracker.code`, `link.tracker.click` | `mail.render.mixin`, `utm.campaign` |
| loyalty | Coupons & Loyalty | `loyalty.card`, `loyalty.history`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `loyalty.card.update.balance`, `loyalty.generate.wizard` | `base.partner.merge.automatic.wizard`, `product.pricelist`, `product.product`, `product.template`, `res.partner` |
| lunch | Lunch | `lunch.alert`, `lunch.cashmove`, `lunch.location`, `lunch.order`, `lunch.product`, `lunch.product.category`, `lunch.supplier`, `lunch.topping`, `lunch.cashmove.report` | `res.company`, `res.config.settings`, `res.groups`, `res.users` |
| mail | Discuss | `bus.sync.mixin`, `discuss.call.history`, `discuss.category`, `discuss.channel`, `discuss.channel.last.interest.update`, `discuss.channel.member`, `discuss.channel.rtc.session`, `discuss.gif.favorite`, `discuss.voice.metadata`, `mail.guest`, `res.users.settings.volumes`, `fetchmail.server`, `mail.activity`, `mail.activity.mixin`, `mail.activity.plan`, `mail.activity.plan.template`, `mail.activity.type`, `mail.alias`, `mail.alias.domain`, `mail.alias.mixin`, `mail.alias.mixin.optional`, `mail.blacklist`, `mail.call.artifact`, `mail.canned.response`, `mail.composer.mixin`, `mail.followers`, `mail.gateway.allowed`, `mail.ice.server`, `mail.link.preview`, `mail.mail`, `mail.message`, `mail.message.link.preview`, `mail.message.reaction`, `mail.message.schedule`, `mail.message.subtype`, `mail.message.translation`, `mail.notification`, `mail.poll`, `mail.poll.option`, `mail.poll.vote`, `mail.presence`, `mail.push`, `mail.push.device`, `mail.render.mixin`, `mail.scheduled.message`, `mail.template`, `mail.thread`, `mail.thread.blacklist`, `mail.thread.main.attachment`, `mail.thread.subject.suggested`, `mail.track.mixin`, `mail.tracking.duration.mixin`, `res.role`, `template.reset.mixin`, `publisher_warranty.contract`, `mail.activity.schedule`, `mail.activity.schedule.line`, `mail.blacklist.remove`, `mail.compose.message`, `mail.followers.edit`, `mail.template.preview`, `mail.template.reset` | `base.module.uninstall`, `base.partner.merge.automatic.wizard`, `base`, `bus.bus`, `bus.listener.mixin`, `ir.access`, `ir.actions.act_window.view`, `ir.actions.server`, `ir.attachment`, `ir.config_parameter`, `ir.cron`, `ir.http`, `ir.mail_server`, `ir.model.fields`, `ir.model`, `ir.qweb`, `ir.ui.menu`, `ir.ui.view`, `ir.websocket`, `kpi.provider`, `mail.message`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users.settings`, `res.users` |
| mail_bot | OdooBot | `mail.bot` | `discuss.channel`, `res.users` |
| mail_bot_hr | OdooBot - HR |  |  |
| mail_group | Mail Group | `mail.group`, `mail.group.member`, `mail.group.message`, `mail.group.moderation`, `mail.group.message.reject` |  |
| mail_plugin | Mail Plugin |  | `ir.http` |
| mail_tracking | Discuss Tracking | `mail.tracking.value` | `ir.model.fields`, `mail.compose.message`, `mail.message`, `mail.thread` |
| mail_tracking_mass_mailing | Mass Mailing Tracking |  | `mail.compose.message`, `mail.message`, `mail.thread` |
| mail_tracking_sms | SMS Message Tracking |  | `mail.message`, `mail.thread`, `sms.composer` |
| maintenance | Maintenance | `maintenance.stage`, `maintenance.equipment.category`, `maintenance.mixin`, `maintenance.equipment`, `maintenance.request`, `maintenance.team` | `res.config.settings` |
| marketing_card | Marketing Card | `card.campaign`, `card.campaign.tag`, `card.card`, `card.template` | `ir.model`, `mail.compose.message`, `mailing.mailing`, `utm.source` |
| marketing_card_event | Marketing Card For Events |  | `card.campaign`, `event.event`, `mailing.mailing` |
| mass_mailing | Email Marketing | `mailing.mailing`, `mailing.contact`, `mailing.filter`, `mailing.list`, `mailing.subscription`, `mailing.subscription.optout`, `mailing.trace`, `mailing.trace.report`, `mailing.contact.import`, `mailing.contact.to.list`, `mailing.mailing.schedule.date`, `mailing.mailing.test` | `ir.http`, `ir.mail_server`, `ir.model`, `ir.ui.view`, `link.tracker.click`, `link.tracker`, `mail.blacklist`, `mail.compose.message`, `mail.mail`, `mail.render.mixin`, `mail.thread`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `utm.campaign`, `utm.medium`, `utm.source` |
| mass_mailing_crm | Mass mailing on lead / opportunities |  | `crm.lead`, `mailing.mailing`, `utm.campaign` |
| mass_mailing_crm_sms | Mass mailing sms on lead / opportunities |  | `utm.campaign` |
| mass_mailing_event | Mass mailing on attendees |  | `event.event`, `event.registration` |
| mass_mailing_event_sms | Event Attendees SMS Marketing |  | `event.event` |
| mass_mailing_event_track | Mass mailing on track speakers |  | `event.event`, `event.track` |
| mass_mailing_event_track_sms | Track Speakers SMS Marketing |  | `event.event` |
| mass_mailing_sale | Mass mailing on sale orders |  | `mailing.mailing`, `sale.order`, `utm.campaign` |
| mass_mailing_sale_sms | Mass mailing sms on sale orders |  | `utm.campaign` |
| mass_mailing_slides | Mass mailing on course members |  | `slide.channel` |
| mass_mailing_sms | SMS Marketing | `mailing.sms.test` | `mailing.contact.to.list`, `mailing.contact`, `mailing.list`, `mailing.mailing`, `mailing.trace`, `res.partner`, `res.users`, `sms.composer`, `sms.sms`, `sms.tracker`, `utm.campaign`, `utm.mixin` |
| mass_mailing_themes | Mass Mailing Themes |  |  |
| microsoft_account | Microsoft Users | `microsoft.service` | `res.users` |
| microsoft_calendar | Outlook Calendar | `microsoft.calendar.sync`, `microsoft.calendar.account.reset` | `calendar.alarm_manager`, `calendar.attendee`, `calendar.event`, `calendar.recurrence`, `res.config.settings`, `res.users.settings`, `res.users` |
| microsoft_outlook | Microsoft Outlook | `microsoft.outlook.mixin` | `fetchmail.server`, `ir.mail_server`, `res.config.settings`, `res.users` |
| mrp | Manufacturing | `mrp.bom`, `mrp.bom.line`, `mrp.bom.byproduct`, `mrp.production.group`, `mrp.production`, `mrp.routing.workcenter`, `mrp.unbuild`, `mrp.workcenter`, `mrp.workcenter.tag`, `mrp.workcenter.productivity.loss.type`, `mrp.workcenter.productivity.loss`, `mrp.workcenter.productivity`, `mrp.workcenter.capacity`, `mrp.workorder`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `change.production.qty`, `mrp.consumption.warning`, `mrp.consumption.warning.line`, `mrp.finished.product.label.layout`, `mrp.production.backorder.line`, `mrp.production.backorder`, `mrp.production.serials`, `mrp.production.split.multi`, `mrp.production.split`, `mrp.production.split.line`, `stock.warn.insufficient.qty.unbuild` | `picking.label.type`, `product.product`, `product.replenish`, `product.template`, `product.uom`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.groups`, `stock.allocation.report`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.package.history`, `stock.package`, `stock.picking.type`, `stock.picking`, `stock.quant`, `stock.reference`, `stock.replenish.mixin`, `stock.replenishment.info`, `stock.route`, `stock.rule`, `stock.traceability.report`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_account | Accounting - MRP | `mrp.account.wip.accounting.line`, `mrp.account.wip.accounting` | `account.analytic.account`, `account.analytic.applicability`, `account.analytic.line`, `account.move.line`, `account.move`, `account.stock.valuation.report`, `mrp.bom`, `mrp.production`, `mrp.workcenter.productivity`, `mrp.workcenter`, `mrp.workorder`, `product.category`, `product.product`, `product.template`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `res.company`, `stock.move` |
| mrp_delivery | Delivery and MRP Management |  | `stock.move.line` |
| mrp_landed_costs | Landed Costs On MO |  | `stock.landed.cost` |
| mrp_product_expiry | Manufacturing Expiry |  | `expiry.picking.confirmation`, `mrp.production` |
| mrp_repair | Mrp Repairs |  | `mrp.production`, `repair.order`, `stock.move` |
| mrp_subcontracting | MRP Subcontracting |  | `change.production.qty`, `mrp.bom`, `mrp.production.serials`, `mrp.production`, `product.product`, `product.supplierinfo`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `res.company`, `res.partner`, `stock.location`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.rule`, `stock.warehouse` |
| mrp_subcontracting_account | Subcontracting Management with Stock Valuation |  | `mrp.production`, `product.product` |
| mrp_subcontracting_dropshipping | Dropship and Subcontracting Management |  | `purchase.order`, `res.company`, `stock.move`, `stock.picking`, `stock.replenish.mixin`, `stock.rule`, `stock.traceability.report`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| mrp_subcontracting_landed_costs | Landed Costs With Subcontracting order |  | `stock.landed.cost` |
| mrp_subcontracting_purchase | Purchase and Subcontracting Management |  | `account.move.line`, `account.move`, `mrp.production`, `product.product`, `purchase.order`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `stock.move`, `stock.picking`, `stock.rule` |
| mysubscription | My Subscription | `mysubscription.mysubscription` |  |
| onboarding | Onboarding Toolbox | `onboarding.onboarding`, `onboarding.onboarding.step`, `onboarding.progress`, `onboarding.progress.step` |  |
| partner_autocomplete | Partner Autocomplete | `iap.autocomplete.api` | `ir.http`, `res.company`, `res.config.settings`, `res.partner` |
| partnership | Partnership / Membership | `res.partner.grade` | `product.pricelist`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `sale.order` |
| payment | Payment Engine | `payment.data`, `payment.method`, `payment.provider`, `payment.token`, `payment.transaction`, `payment.capture.wizard`, `payment.link.wizard` | `ir.http`, `ir.websocket`, `portal.entry`, `res.company`, `res.config.settings`, `res.country`, `res.partner` |
| payment_adyen | Payment Provider: Adyen |  | `payment.capture.wizard`, `payment.provider`, `payment.token`, `payment.transaction` |
| payment_aps | Payment Provider: Amazon Payment Services |  | `payment.provider`, `payment.transaction` |
| payment_asiapay | Payment Provider: AsiaPay |  | `payment.provider`, `payment.transaction` |
| payment_authorize | Payment Provider: Authorize.Net |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_buckaroo | Payment Provider: Buckaroo |  | `payment.provider`, `payment.transaction` |
| payment_custom | Payment Provider: Custom Payment Modes |  | `payment.provider`, `payment.transaction` |
| payment_demo | Payment Provider: Demo |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_dpo | Payment Provider: DPO |  | `payment.provider`, `payment.transaction` |
| payment_ecpay | Payment Provider: ECPay |  | `payment.provider`, `payment.transaction` |
| payment_flutterwave | Payment Provider: Flutterwave |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_iyzico | Payment Provider: Iyzico |  | `payment.provider`, `payment.transaction` |
| payment_mercado_pago | Payment Provider: Mercado Pago |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_mollie | Payment Provider: Mollie |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_nuvei | Payment Provider: Nuvei |  | `payment.provider`, `payment.transaction` |
| payment_paymob | Payment Provider: Paymob |  | `payment.provider`, `payment.transaction` |
| payment_paypal | Payment Provider: Paypal |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_payu | Payment Provider: PayU |  | `payment.provider`, `payment.transaction` |
| payment_razorpay | Payment Provider: Razorpay |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_redsys | Payment Provider: Redsys |  | `payment.provider`, `payment.transaction` |
| payment_stripe | Payment Provider: Stripe |  | `payment.provider`, `payment.token`, `payment.transaction` |
| payment_toss_payments | Payment Provider: Toss Payments |  | `payment.provider`, `payment.transaction` |
| payment_worldline | Payment Provider: Worldline |  | `payment.provider`, `payment.transaction` |
| payment_xendit | Payment Provider: Xendit |  | `payment.provider`, `payment.transaction` |
| phone_validation | Phone Numbers Validation | `mail.thread.phone`, `phone.blacklist`, `phone.blacklist.remove` | `base`, `mail.activity.mixin`, `mail.activity.schedule`, `mail.activity`, `res.partner`, `res.users` |
| point_of_sale | Point of Sale | `pos.bill`, `pos.bus.mixin`, `pos.category`, `pos.config`, `pos.load.mixin`, `pos.note`, `pos.order`, `pos.order.line`, `pos.payment`, `pos.payment.method`, `pos.prep.line`, `pos.prep.order`, `pos.preset`, `pos.printer`, `pos.session`, `pos.snooze`, `report.point_of_sale.report_saledetails`, `pos.order.receipt`, `report.point_of_sale.report_invoice`, `report.pos.order`, `pos.confirmation.wizard`, `pos.daily.sales.reports.wizard`, `pos.details.wizard`, `pos.make.invoice`, `pos.make.payment`, `pos.price.inclusion.wizard` | `account.account`, `account.bank.statement.line`, `account.bank.statement`, `account.cash.rounding`, `account.fiscal.position`, `account.journal`, `account.move.line`, `account.move`, `account.payment`, `account.tax.group`, `account.tax`, `barcode.rule`, `decimal.precision`, `digest.digest`, `ir.http`, `ir.sequence`, `ir.ui.view`, `product.attribute.custom.value`, `product.attribute`, `product.category`, `product.combo.item`, `product.combo`, `product.pricelist.item`, `product.pricelist`, `product.product`, `product.tag`, `product.template.attribute.line`, `product.template.attribute.value`, `product.template`, `product.uom`, `res.company`, `res.config.settings`, `res.country.state`, `res.country`, `res.currency`, `res.groups`, `res.lang`, `res.partner`, `res.users`, `resource.calendar.attendance`, `uom.uom` |
| populate | Populate | `populate.blueprint`, `populate.job`, `populate.model.data`, `populate.session` |  |
| portal | Customer Portal | `portal.entry`, `portal.mixin`, `portal.share`, `portal.wizard`, `portal.wizard.user` | `ir.http`, `ir.qweb`, `ir.ui.view`, `mail.message`, `mail.thread`, `res.config.settings`, `res.country`, `res.partner`, `res.users.apikeys.description` |
| portal_discuss | Portal Discuss |  | `discuss.channel`, `portal.entry` |
| portal_rating | Portal Rating |  | `ir.http`, `mail.message`, `rating.rating` |
| pos_account_tax_python | Allow custom taxes in POS |  | `account.tax` |
| pos_adyen | POS Adyen |  | `pos.config`, `pos.order`, `pos.payment.method`, `pos.payment`, `res.config.settings` |
| pos_bancontact_pay | POS Bancontact Pay & Wero |  | `account.journal`, `pos.config`, `pos.payment.method`, `pos.payment`, `res.company` |
| pos_cashdro | POS Cashdro Cash Machines |  | `pos.payment.method` |
| pos_cashmatic | POS Cashmatic Cash Machines |  | `pos.payment.method` |
| pos_discount | Point of Sale Discounts |  | `account.move.line`, `pos.config`, `product.template`, `report.point_of_sale.report_saledetails`, `res.config.settings` |
| pos_dpopay | PoS DPO Pay |  | `pos.payment.method`, `pos.payment` |
| pos_edi_ubl | Point of Sale UBL | `pos.edi.xml.ubl_21` |  |
| pos_event | POS - Event |  | `event.event.ticket`, `event.event`, `event.question.answer`, `event.question`, `event.registration.answer`, `event.registration`, `event.slot`, `pos.config`, `pos.order.line`, `pos.order`, `pos.session` |
| pos_event_sale | PoS - Event Sale |  | `event.registration`, `event.sale.report`, `sale.order.line` |
| pos_glory_cash | POS Glory Cash Machines |  | `pos.payment.method` |
| pos_hr | POS - HR | `report.pos_hr.single_employee_sales_report` | `account.bank.statement.line`, `hr.employee`, `pos.config`, `pos.daily.sales.reports.wizard`, `pos.order.receipt`, `pos.order`, `pos.payment`, `pos.session`, `product.product`, `report.pos.order`, `res.config.settings`, `res.partner` |
| pos_hr_restaurant | POS HR Restaurant |  |  |
| pos_imin | POS iMin |  | `pos.printer` |
| pos_loyalty | Point of Sale - Coupons & Loyalty |  | `account.move.line`, `barcode.rule`, `loyalty.card`, `loyalty.mail`, `loyalty.program`, `loyalty.reward`, `loyalty.rule`, `pos.config`, `pos.order.line`, `pos.order.receipt`, `pos.order`, `pos.session`, `product.product`, `product.template` |
| pos_mercado_pago | POS Mercado Pago |  | `pos.payment.method` |
| pos_mollie | POS Mollie |  | `pos.payment.method` |
| pos_mrp | pos_mrp |  | `pos.order.line`, `pos.order`, `stock.move` |
| pos_online_payment | Point of Sale online payment |  | `account.payment`, `payment.transaction`, `pos.config`, `pos.order`, `pos.payment.method`, `pos.payment` |
| pos_online_payment_self_order | POS Self-Order / Online Payment |  | `ir.http`, `payment.transaction`, `pos.config`, `pos.order`, `pos.payment.method`, `res.config.settings` |
| pos_partner_autocomplete | POS Partner Autocomplete |  |  |
| pos_pine_labs | POS Pine Labs |  | `pos.payment.method`, `pos.payment` |
| pos_qfpay | POS QFPay |  | `pos.payment.method` |
| pos_razorpay | POS Razorpay |  | `pos.payment.method`, `pos.payment` |
| pos_repair | POS - Repair |  | `sale.order.line`, `stock.picking` |
| pos_restaurant | Restaurant | `pos.course`, `restaurant.floor`, `restaurant.table`, `restaurant.order.course` | `pos.category`, `pos.config`, `pos.order.line`, `pos.order.receipt`, `pos.order`, `pos.preset`, `pos.session`, `product.template`, `res.config.settings` |
| pos_restaurant_loyalty | POS - Restaurant Loyalty |  |  |
| pos_safaricom | POS Safaricom | `transaction.lipa.na.mpesa` | `pos.order.receipt`, `pos.payment.method`, `pos.payment` |
| pos_sale | POS - Sales |  | `account.move.line`, `account.move`, `crm.team`, `pos.config`, `pos.order.line`, `pos.order.receipt`, `pos.order`, `pos.session`, `product.template`, `res.config.settings`, `res.partner`, `sale.order.line`, `sale.order`, `sale.report` |
| pos_sale_delivery | POS - Sales Delivery |  | `pos.order` |
| pos_sale_loyalty | POS - Sales Loyalty |  | `loyalty.rule`, `sale.order.line` |
| pos_sale_margin | POS - Sale Margin |  | `sale.report` |
| pos_sale_stock | POS - Sales Stock |  | `pos.order.line`, `pos.order`, `sale.order.line`, `sale.order`, `sale.report`, `stock.picking` |
| pos_self_order | POS Self Order | `pos_self_order.custom_link` | `ir.http`, `ir.ui.view`, `mail.template`, `pos.category`, `pos.config`, `pos.load.mixin`, `pos.order.line`, `pos.order.receipt`, `pos.order`, `pos.payment.method`, `pos.prep.line`, `pos.prep.order`, `pos.preset`, `pos.session`, `pos.snooze`, `product.product`, `product.tag`, `product.template`, `res.config.settings`, `res.country`, `res.partner`, `restaurant.floor`, `restaurant.table` |
| pos_self_order_bancontact_pay | POS Self Order Bancontact Pay & Wero |  | `pos.config`, `pos.payment.method` |
| pos_self_order_event | POS Self Order - Event |  | `event.event`, `pos.config`, `pos.order` |
| pos_self_order_pine_labs | POS Self Order Pine Labs |  | `pos.payment.method` |
| pos_self_order_qfpay | POS Self Order QFPay |  | `pos.payment.method` |
| pos_self_order_razorpay | POS Self Order Razorpay |  | `pos.payment.method` |
| pos_self_order_sale | POS Self Order Sale |  | `res.config.settings` |
| pos_self_order_sms | POS Self Order SMS |  | `pos.order`, `pos.preset` |
| pos_sms | POS - SMS |  | `pos.config`, `pos.order`, `res.config.settings` |
| pos_stock | PoS - Stock | `pos.pack.operation.lot` | `account.move.line`, `account.move`, `pos.config`, `pos.order.line`, `pos.order.receipt`, `pos.order`, `pos.session`, `product.category`, `product.removal`, `product.template`, `res.company`, `res.config.settings`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.reference`, `stock.rule`, `stock.warehouse` |
| pos_stripe | POS Stripe |  | `pos.payment.method` |
| pos_sumup | POS SumUp |  | `pos.payment.method` |
| pos_viva_com | PoS Viva.com |  | `pos.payment.method`, `pos.payment` |
| printer | Printer | `printer.printer`, `select.printers.wizard` | `ir.actions.report` |
| privacy_lookup | Privacy | `privacy.log`, `privacy.lookup.wizard`, `privacy.lookup.wizard.line` | `res.partner` |
| product | Products & Pricelists | `product.attribute`, `product.attribute.custom.value`, `product.attribute.value`, `product.base.unit`, `product.catalog.line.mixin`, `product.catalog.mixin`, `product.category`, `product.combo`, `product.combo.item`, `product.document`, `product.pricelist`, `product.pricelist.item`, `product.product`, `product.supplierinfo`, `product.tag`, `product.template`, `product.template.attribute.line`, `product.template.attribute.value`, `product.uom`, `report.product.label.base`, `report.product.report_product_label_pdf`, `report.product.report_product_label_dymo`, `report.product.report_product_label_zpl`, `report.product.report_pricelist`, `product.label.layout`, `update.product.attribute.value` | `ir.attachment`, `res.company`, `res.config.settings`, `res.country.group`, `res.currency`, `res.groups`, `res.partner`, `uom.uom` |
| product_email_template | Product Email Template |  | `account.move`, `product.template` |
| product_expiry | Products Expiration Date | `expiry.picking.confirmation` | `lot.label.layout`, `product.product`, `product.template`, `report.stock.quantity`, `res.config.settings`, `res.groups`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.quant`, `stock.rule`, `stock.traceability.report` |
| product_margin | Margins by Products | `product.margin` | `product.product` |
| product_matrix | Product Matrix |  | `product.template.attribute.value`, `product.template` |
| project | Project | `project.collaborator`, `project.milestone`, `project.project`, `project.project.stage`, `project.role`, `project.tags`, `project.task`, `project.task.recurrence`, `project.task.stage.personal`, `project.task.type`, `project.update`, `report.project.task.user`, `project.task.burndown.chart.report`, `project.task.stage.report`, `project.project.stage.delete.wizard`, `project.share.collaborator.wizard`, `project.share.wizard`, `task.share.wizard`, `project.task.type.delete.wizard`, `project.template.create.wizard`, `project.template.role.to.users.map` | `account.analytic.account`, `account.analytic.line`, `digest.digest`, `ir.ui.menu`, `mail.activity`, `mail.message`, `portal.share`, `res.config.settings`, `res.groups`, `res.partner`, `res.users.settings`, `res.users` |
| project_account | Project - Account |  | `project.project` |
| project_hr_expense | Project Expenses |  | `hr.expense`, `project.project` |
| project_hr_skills | Project - Skills |  | `project.task`, `report.project.task.user`, `res.users` |
| project_mail_plugin | Project Mail Plugin |  |  |
| project_mrp | MRP Project |  | `mrp.bom`, `mrp.production`, `project.project`, `stock.move`, `stock.rule` |
| project_mrp_account | MRP Account Project |  | `mrp.production`, `mrp.workorder`, `stock.move`, `stock.picking.type`, `stock.rule` |
| project_mrp_sale | MRP Project Sale |  | `account.analytic.line` |
| project_mrp_stock_landed_costs | Project MRP Landed Costs |  | `stock.valuation.adjustment.lines` |
| project_purchase | Project Purchase |  | `project.project`, `purchase.order.line`, `purchase.order`, `purchase.report` |
| project_purchase_stock | Project - Purchase - Stock |  | `purchase.order.line`, `stock.move`, `stock.rule` |
| project_sale_expense | Project - Sale - Expense |  | `account.analytic.line`, `account.move.line`, `hr.expense` |
| project_sms | Project - SMS |  | `project.project.stage`, `project.project`, `project.task.type`, `project.task` |
| project_stock | Project Stock |  | `project.project`, `stock.picking` |
| project_stock_account | Project Stock Account |  | `account.analytic.applicability`, `account.analytic.line`, `stock.move`, `stock.picking.type` |
| project_stock_landed_costs | Project Stock Landed Costs |  | `stock.valuation.adjustment.lines` |
| project_timesheet_holidays | Timesheet when on Time Off |  | `account.analytic.line`, `hr.employee.departure`, `hr.employee`, `hr.leave`, `project.task`, `res.company`, `res.config.settings`, `resource.calendar.leaves` |
| project_todo | To-Do | `mail.activity.todo.create` | `project.task`, `res.users` |
| purchase | Purchase | `purchase.bill.line.match`, `purchase.order`, `purchase.order.line`, `purchase.bill.union`, `purchase.report`, `bill.to.po.wizard` | `account.accrued.orders.wizard`, `account.analytic.account`, `account.analytic.applicability`, `account.move.line`, `account.move`, `account.tax`, `ir.actions.report`, `product.category`, `product.product`, `product.supplierinfo`, `product.template`, `res.company`, `res.config.settings`, `res.groups`, `res.partner` |
| purchase_alternative | Purchase Alternative | `purchase.order.group`, `purchase.alternative.create`, `purchase.alternative.warning` | `purchase.order.line`, `purchase.order` |
| purchase_alternative_sale | Purchase Alternative Sale |  | `purchase.alternative.create` |
| purchase_alternative_stock | Purchase Alternative Stock |  | `purchase.alternative.create`, `purchase.order.line`, `purchase.order` |
| purchase_edi_ubl_bis3 | Import/Export electronic orders with UBL | `purchase.edi.xml.ubl_bis3` | `account.move`, `purchase.order` |
| purchase_mrp | Purchase and MRP Management |  | `mrp.bom.line`, `mrp.bom`, `mrp.production`, `purchase.order.line`, `purchase.order`, `report.mrp.report_bom_structure`, `report.mrp.report_mo_overview`, `stock.move`, `stock.rule` |
| purchase_product_matrix | Purchase Matrix |  | `purchase.order.line`, `purchase.order` |
| purchase_repair | Purchase Repair |  | `purchase.order`, `repair.order` |
| purchase_requisition | Purchase Agreements | `purchase.requisition`, `purchase.requisition.line` | `product.product`, `product.supplierinfo`, `purchase.order.line`, `purchase.order` |
| purchase_requisition_stock | Purchase Requisition Stock |  | `purchase.order`, `purchase.requisition.line`, `purchase.requisition`, `stock.move`, `stock.rule` |
| purchase_stock | Purchase Stock | `vendor.delay.report` | `account.move.line`, `product.product`, `product.replenish`, `product.supplierinfo`, `product.template`, `purchase.order.line`, `purchase.order`, `purchase.report`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.partner`, `stock.allocation.report`, `stock.forecasted_product_product`, `stock.lot`, `stock.move`, `stock.picking`, `stock.reference`, `stock.replenish.mixin`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.route`, `stock.rule`, `stock.warehouse.orderpoint`, `stock.warehouse` |
| rating | Customer Rating | `rating.rating`, `rating.mixin`, `rating.parent.mixin` | `mail.message`, `mail.thread` |
| repair | Repairs | `repair.order`, `repair.tags`, `repair.service.line`, `repair.consumption.warning`, `repair.consumption.warning.line` | `account.move.line`, `account.move`, `product.product`, `product.template`, `res.partner`, `sale.order.line`, `sale.order`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.traceability.report`, `stock.warehouse` |
| resource | Resource | `resource.calendar`, `resource.calendar.attendance`, `resource.calendar.leaves`, `resource.mixin`, `resource.resource` | `res.company`, `res.users` |
| resource_mail | Resource Mail |  | `resource.resource` |
| rpc | RPC endpoints |  |  |
| sale | Sales | `sale.order`, `sale.order.line`, `sale.report`, `sale.mass.cancel.orders`, `sale.advance.payment.inv`, `sale.order.discount` | `account.accrued.orders.wizard`, `account.analytic.applicability`, `account.analytic.line`, `account.invoice.report`, `account.move.line`, `account.move`, `base.document.layout`, `crm.team`, `ir.actions.report`, `ir.config_parameter`, `payment.link.wizard`, `payment.provider`, `payment.transaction`, `product.attribute.custom.value`, `product.category`, `product.document`, `product.pricelist.item`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `utm.campaign` |
| sale_crm | Opportunity to Quotation | `crm.quotation.partner` | `crm.lead`, `crm.team`, `sale.order` |
| sale_edi_ubl | Import electronic orders with UBL | `customer.product.reference`, `sale.edi.xml.ubl_bis3` | `product.product`, `sale.order.line`, `sale.order` |
| sale_expense | Sales Expense | `expense.attachment.selection.wizard` | `account.move.line`, `account.move`, `hr.expense.split`, `hr.expense`, `product.template`, `sale.order.line`, `sale.order` |
| sale_expense_margin | Sales Expense Margin |  | `account.move.line`, `sale.order.line` |
| sale_gelato | Gelato |  | `delivery.carrier`, `product.document`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.partner`, `sale.order.line`, `sale.order` |
| sale_gelato_stock | Gelato/Stock bridge |  | `sale.order.line` |
| sale_loyalty | Sale Loyalty | `sale.order.coupon.points`, `sale.loyalty.coupon.wizard`, `sale.loyalty.reward.wizard` | `account.move.line`, `loyalty.card`, `loyalty.history`, `loyalty.program`, `loyalty.reward`, `sale.order.line`, `sale.order` |
| sale_loyalty_delivery | Sale Loyalty - Delivery |  | `loyalty.program`, `loyalty.reward`, `payment.provider`, `sale.order` |
| sale_management | Sales | `sale.order.template`, `sale.order.template.line` | `digest.digest`, `product.attribute.custom.value`, `res.config.settings`, `sale.order.line`, `sale.order` |
| sale_margin | Margins in Sales Orders |  | `sale.order.line`, `sale.order.template.line`, `sale.order`, `sale.report` |
| sale_mrp | Sales and MRP Management |  | `mrp.bom`, `mrp.production`, `sale.order.line`, `sale.order`, `stock.move`, `stock.rule`, `stock.warehouse.orderpoint` |
| sale_mrp_margin | Sale Mrp Margin |  |  |
| sale_pdf_quote_builder | Sales PDF Quotation Builder | `quotation.document`, `sale.pdf.form.field` | `ir.actions.report`, `product.document`, `sale.order.line`, `sale.order.template`, `sale.order` |
| sale_product_matrix | Sale Matrix |  | `product.template`, `sale.order.line`, `sale.order` |
| sale_project | Sales - Project |  | `account.analytic.line`, `account.move.line`, `product.product`, `product.template`, `project.milestone`, `project.project`, `project.task.recurrence`, `project.task.type`, `project.task`, `project.template.create.wizard`, `report.project.task.user`, `sale.order.line`, `sale.order.template.line`, `sale.order`, `sale.report` |
| sale_project_margin | Sales Margins in Projects |  | `project.project` |
| sale_project_stock | Sale Project - Sale Stock |  | `account.analytic.line`, `project.project`, `stock.move`, `stock.picking` |
| sale_project_stock_account | Sale Project Stock Account |  | `stock.move` |
| sale_purchase | Sale Purchase |  | `product.template`, `purchase.order.line`, `purchase.order`, `sale.order.line`, `sale.order` |
| sale_purchase_project | Sale Purchase Project |  | `account.analytic.line`, `sale.order.line` |
| sale_purchase_stock | MTO Sale <-> Purchase |  | `purchase.order.line`, `purchase.order`, `sale.order`, `stock.move`, `stock.rule` |
| sale_service | Sales - Service |  | `sale.order.line` |
| sale_sms | Sale - SMS |  |  |
| sale_stock | Sales and Warehouse Management | `return.reason` | `account.move.line`, `account.move`, `product.template`, `report.stock.report_stock_rule`, `res.company`, `res.config.settings`, `res.users`, `sale.order.line`, `sale.order`, `sale.report`, `stock.forecasted_product_product`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking`, `stock.reference`, `stock.replenishment.info`, `stock.route`, `stock.rule`, `stock.rules.report` |
| sale_stock_margin | Sale Stock Margin |  | `sale.order.line` |
| sale_stock_product_expiry | Sale Stock Product Expiry |  | `account.move`, `sale.order.line` |
| sale_timesheet | Sales Timesheet | `project.sale.line.employee.map` | `account.analytic.line`, `account.move.line`, `account.move.reversal`, `account.move.send`, `account.move`, `hr.employee.departure`, `hr.employee`, `product.product`, `product.template`, `project.project`, `project.task`, `report.project.task.user`, `res.config.settings`, `sale.advance.payment.inv`, `sale.order.line`, `sale.order`, `timesheets.analysis.report` |
| sale_timesheet_margin | Service Margins in Sales Orders |  | `sale.order.line` |
| sales_team | Sales Teams | `crm.tag`, `crm.team`, `crm.team.member` | `res.users` |
| sms | SMS gateway | `sms.sms`, `sms.template`, `sms.tracker`, `sms.account.code`, `sms.account.phone`, `sms.account.sender`, `sms.composer`, `sms.template.preview`, `sms.template.reset` | `iap.account`, `ir.actions.server`, `ir.model`, `mail.followers`, `mail.message`, `mail.notification`, `mail.scheduled.message`, `mail.thread`, `res.company` |
| sms_twilio | Twilio SMS | `sms.twilio.number`, `sms.twilio.account.manage` | `mail.notification`, `res.company`, `res.config.settings`, `sms.composer`, `sms.sms`, `sms.tracker` |
| snailmail | Snail Mail | `snailmail.letter` | `ir.actions.report`, `mail.message`, `mail.notification`, `mail.thread`, `res.company`, `res.config.settings`, `res.partner` |
| snailmail_account | Snail Mail - Account |  | `account.move.send.batch.wizard`, `account.move.send`, `account.move`, `res.partner` |
| social_media | Social Media |  | `res.company` |
| spreadsheet | Spreadsheet | `spreadsheet.mixin` | `ir.http`, `ir.model`, `res.currency.rate`, `res.currency`, `res.lang` |
| spreadsheet_account | Spreadsheet Accounting Formulas |  | `account.account`, `res.company` |
| spreadsheet_dashboard | Spreadsheet dashboard | `spreadsheet.dashboard`, `spreadsheet.dashboard.favorite.filters`, `spreadsheet.dashboard.group`, `spreadsheet.dashboard.share` |  |
| spreadsheet_dashboard_account | Spreadsheet dashboard for accounting |  |  |
| spreadsheet_dashboard_event_sale | Spreadsheet dashboard for events |  |  |
| spreadsheet_dashboard_hr_expense | Spreadsheet dashboard for expenses |  |  |
| spreadsheet_dashboard_hr_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_im_livechat | Spreadsheet dashboard for live chat |  |  |
| spreadsheet_dashboard_pos_hr | Spreadsheet dashboard for point of sale |  |  |
| spreadsheet_dashboard_pos_restaurant | Spreadsheet dashboard for restaurants |  |  |
| spreadsheet_dashboard_sale | Spreadsheet dashboard for sales |  |  |
| spreadsheet_dashboard_sale_timesheet | Spreadsheet dashboard for time sheets |  |  |
| spreadsheet_dashboard_stock_account | Spreadsheet dashboard for stock |  |  |
| spreadsheet_dashboard_website_sale | Spreadsheet dashboard for eCommerce |  |  |
| spreadsheet_dashboard_website_sale_slides | Spreadsheet dashboard for eLearning |  |  |
| stock | Inventory | `product.removal`, `stock.putaway.rule`, `stock.location`, `stock.route`, `stock.lot`, `stock.move`, `stock.move.line`, `stock.warehouse.orderpoint`, `stock.package`, `stock.package.history`, `stock.package.type`, `stock.picking`, `stock.picking.batch`, `stock.picking.type`, `stock.quant`, `stock.reference`, `stock.replenish.mixin`, `stock.rule`, `stock.scrap.reason.tag`, `stock.storage.category`, `stock.storage.category.capacity`, `stock.warehouse`, `report.stock.quantity`, `report.stock.report_stock_rule`, `stock.allocation.report`, `stock.forecasted_product_product`, `stock.forecasted_product_template`, `stock.traceability.report`, `product.replenish`, `stock.add.to.wave`, `stock.backorder.confirmation.line`, `stock.backorder.confirmation`, `stock.inventory.adjustment.name`, `stock.inventory.conflict`, `stock.inventory.warning`, `picking.label.type`, `stock.location.label.layout`, `lot.label.layout`, `stock.orderpoint.snooze`, `stock.orderpoint.suggest`, `stock.package.destination`, `stock.package.label.layout`, `stock.picking.to.batch`, `stock.picking.type.label.layout`, `stock.put.in.pack`, `stock.quant.relocate`, `stock.replenishment.info`, `stock.replenishment.option`, `stock.request.count`, `stock.rules.report`, `stock.warn.insufficient.qty`, `stock.warn.insufficient.qty.scrap`, `stock.zero.demand.confirmation` | `barcode.rule`, `digest.digest`, `ir.actions.report`, `product.category`, `product.label.layout`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `uom.uom` |
| stock_account | WMS Accounting | `product.value`, `stock.avco.report` | `account.analytic.account`, `account.analytic.plan`, `account.move.line`, `account.move`, `account.stock.valuation.report`, `product.category`, `product.product`, `product.template`, `res.company`, `res.config.settings`, `res.groups`, `stock.forecasted_product_product`, `stock.inventory.adjustment.name`, `stock.location`, `stock.lot`, `stock.move.line`, `stock.move`, `stock.picking.type`, `stock.picking`, `stock.quant` |
| stock_delivery | Delivery - Stock | `pay.on.delivery` | `choose.delivery.carrier`, `delivery.carrier`, `ir.actions.report`, `product.label.layout`, `product.product`, `product.template`, `res.partner`, `sale.order.line`, `sale.order`, `stock.move.line`, `stock.move`, `stock.package.label.layout`, `stock.package.type`, `stock.package`, `stock.picking.batch`, `stock.picking.type`, `stock.picking`, `stock.put.in.pack`, `stock.route` |
| stock_dropshipping | Drop Shipping |  | `account.move.line`, `product.product`, `purchase.order.line`, `purchase.order`, `res.company`, `sale.order.line`, `sale.order`, `stock.lot`, `stock.move.line`, `stock.picking.type`, `stock.picking`, `stock.replenish.mixin`, `stock.rule` |
| stock_fleet | Stock Transport | `report.stock_fleet.report_cmr_batch`, `report.stock_fleet.report_cmr` | `fleet.vehicle.model.category`, `stock.picking.batch`, `stock.picking.type`, `stock.picking`, `stock.warehouse` |
| stock_landed_costs | WMS Landed Costs | `stock.landed.cost`, `stock.landed.cost.lines`, `stock.valuation.adjustment.lines` | `account.move.line`, `account.move`, `product.template`, `purchase.order.line`, `res.company`, `res.config.settings`, `stock.move` |
| stock_maintenance | Stock - Maintenance |  | `maintenance.equipment`, `stock.location` |
| stock_sms | Stock - SMS | `confirm.stock.sms` | `res.company`, `res.config.settings`, `stock.picking` |
| survey | Surveys | `survey.question`, `survey.question.answer`, `survey.survey`, `survey.user_input`, `survey.user_input.line`, `survey.invite` | `digest.digest`, `gamification.badge`, `gamification.challenge`, `ir.http`, `res.lang`, `res.partner`, `survey.survey` |
| survey_crm | Survey CRM |  | `survey.question.answer`, `survey.question`, `survey.survey`, `survey.user_input` |
| uom | Units of measure | `uom.uom` | `res.groups` |
| utm | UTM Trackers | `utm.campaign`, `utm.medium`, `utm.mixin`, `utm.source`, `utm.stage`, `utm.tag` | `ir.http` |
| web | Web | `base.document.layout`, `res.users.settings.embedded.action` | `base`, `ir.attachment`, `ir.http`, `ir.model`, `ir.qweb.field.image_url`, `ir.qweb.field.image`, `ir.ui.menu`, `ir.ui.view`, `properties.base.definition`, `res.company`, `res.config.settings`, `res.partner`, `res.users.settings`, `res.users` |
| web_hierarchy | Web Hierarchy |  | `base`, `ir.actions.act_window.view`, `ir.ui.view` |
| web_tour | Tours | `web_tour.tour`, `web_tour.tour.step` | `ir.http`, `res.users` |
| web_unsplash | Unsplash Image Library |  | `ir.attachment`, `ir.qweb.field.image`, `res.config.settings`, `res.users` |
| website | Website | `website.assets`, `website.html.text.processor`, `website.seo.metadata`, `website.trackable.mixin`, `website.cover_properties.mixin`, `website.page_visibility_options.mixin`, `website.page_options.mixin`, `website.multi.mixin`, `website.located.mixin`, `website.structured_data.mixin`, `website.published.mixin`, `website.published.multi.mixin`, `website.searchable.mixin`, `theme.ir.asset`, `theme.ir.ui.view`, `theme.ir.attachment`, `theme.website.menu`, `theme.website.page`, `theme.utils`, `website.configurator.feature`, `website.controller.page`, `website.menu`, `website.page`, `website.page.properties.base`, `website.page.properties`, `website.route`, `website.rewrite`, `website.snippet.filter`, `website.technical.page`, `website.track`, `website.visitor`, `website.custom_blocked_third_party_domains`, `website.llms`, `website.robots` | `base.language.install`, `base.partner.merge.automatic.wizard`, `base`, `digest.digest`, `ir.access`, `ir.actions.server`, `ir.asset`, `ir.attachment`, `ir.binary`, `ir.http`, `ir.model.data`, `ir.model.fields`, `ir.model`, `ir.module.module`, `ir.qweb.field.contact`, `ir.qweb.field.html`, `ir.qweb`, `ir.ui.menu`, `ir.ui.view`, `portal.wizard.user`, `res.company`, `res.config.settings`, `res.groups`, `res.lang`, `res.partner`, `res.users`, `website.menu`, `website.page`, `website` |
| website_address_autocomplete | Website Address Autocomplete |  | `res.config.settings`, `website` |
| website_blog | Blog | `blog.blog`, `blog.tag.category`, `blog.tag`, `blog.post` | `res.partner`, `website.snippet.filter`, `website.track`, `website.visitor`, `website` |
| website_cf_turnstile | Cloudflare Turnstile |  | `ir.http`, `res.config.settings` |
| website_crm | Contact Form |  | `crm.lead`, `website.visitor`, `website` |
| website_crm_iap_reveal | Lead Generation From Website Visits | `crm.reveal.rule`, `crm.reveal.view` | `crm.lead`, `ir.http` |
| website_crm_livechat | Lead Livechat Sessions |  | `chatbot.script.step`, `crm.lead`, `discuss.channel` |
| website_crm_partner_assign | Resellers | `res.partner.activation`, `crm.partner.report.assign`, `crm.lead.forward.to.partner`, `crm.lead.assignation` | `crm.lead`, `portal.entry`, `res.partner.grade`, `res.partner`, `website` |
| website_crm_sms | Send SMS to Visitor with leads |  | `website.visitor` |
| website_customer | Customer References | `res.partner.tag` | `res.partner`, `website` |
| website_event | Events | `website.event.menu` | `event.event`, `event.registration`, `event.slot`, `event.tag.category`, `event.tag`, `event.type`, `website.menu`, `website.snippet.filter`, `website.track`, `website.visitor`, `website` |
| website_event_booth | Online Event Booths |  | `event.event`, `event.type`, `website.event.menu` |
| website_event_booth_exhibitor | Booths/Exhibitors Bridge |  | `event.booth.category`, `event.booth` |
| website_event_booth_sale | Online Event Booth Sale |  | `product.template`, `sale.order.line`, `sale.order` |
| website_event_booth_sale_exhibitor | Booths Sale/Exhibitors Bridge |  | `event.booth.registration` |
| website_event_crm | Website Events CRM |  | `event.registration` |
| website_event_exhibitor | Event Exhibitors | `event.sponsor`, `event.sponsor.type` | `event.event`, `event.type`, `website.event.menu`, `website` |
| website_event_sale | Online Event Ticketing |  | `event.event.ticket`, `event.event`, `event.sale.report`, `product.pricelist.item`, `product.product`, `product.template`, `sale.order.line`, `sale.order` |
| website_event_track | Advanced Events | `event.track`, `event.track.location`, `event.track.stage`, `event.track.tag`, `event.track.tag.category`, `event.track.visitor` | `event.event`, `event.type`, `res.config.settings`, `website.event.menu`, `website.menu`, `website.visitor`, `website` |
| website_event_track_live | Live Event Tracks |  | `event.track` |
| website_event_track_live_quiz | Quiz on Live Event Tracks |  |  |
| website_event_track_quiz | Quizzes on Tracks | `event.quiz`, `event.quiz.question`, `event.quiz.answer` | `event.event`, `event.track.visitor`, `event.track` |
| website_forum | Forum | `forum.forum`, `forum.post`, `forum.post.comment`, `forum.post.reason`, `forum.post.vote`, `forum.tag` | `gamification.challenge`, `gamification.karma.tracking`, `ir.attachment`, `ir.http`, `mail.thread`, `res.users`, `website` |
| website_google_map | Google Maps |  |  |
| website_hr_recruitment | Online Jobs |  | `hr.applicant`, `hr.department`, `hr.job`, `hr.recruitment.source`, `website.page`, `website.published.multi.mixin`, `website` |
| website_hr_recruitment_livechat | Website IM Livechat HR Recruitment |  |  |
| website_links | Link Tracker |  | `link.tracker` |
| website_livechat | Website Live Chat |  | `chatbot.script.step`, `chatbot.script`, `discuss.channel.member`, `discuss.channel`, `im_livechat.channel`, `ir.http`, `res.config.settings`, `website.page`, `website.visitor`, `website` |
| website_mail | Website Mail |  | `ir.http`, `publisher_warranty.contract` |
| website_mail_group | Website Mail Group |  | `mail.group` |
| website_mass_mailing | Newsletter Subscribe Button |  |  |
| website_mass_mailing_event | Mass mailing on website events |  |  |
| website_mass_mailing_sms | Newsletter Subscribe SMS Template |  |  |
| website_partner | Website Partner |  | `res.partner` |
| website_partnership | Website Partnership |  | `res.partner.grade`, `website` |
| website_payment | Website Payment |  | `payment.provider`, `res.config.settings` |
| website_profile | Website profile |  | `gamification.badge`, `res.users`, `website` |
| website_project | Online Task Submission |  | `project.task`, `website.page` |
| website_sale | eCommerce | `product.attribute.category`, `product.feed`, `product.image`, `product.public.category`, `product.ribbon`, `product.stock.notification`, `product.wishlist`, `website.checkout.alert.mixin`, `website.checkout.step`, `website.sale.extra.field`, `withdrawal.request` | `account.move`, `crm.team`, `delivery.carrier`, `digest.digest`, `ir.http`, `ir.module.module`, `payment.transaction`, `product.attribute`, `product.combo`, `product.document`, `product.pricelist.item`, `product.pricelist`, `product.product`, `product.tag`, `product.template.attribute.line`, `product.template.attribute.value`, `product.template`, `res.company`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `sale.order.line`, `sale.order`, `sale.report`, `theme.utils`, `website.menu`, `website.page`, `website.snippet.filter`, `website.track`, `website.visitor`, `website` |
| website_sale_collect | Click & Collect |  | `delivery.carrier`, `payment.method`, `payment.provider`, `payment.transaction`, `product.template`, `res.config.settings`, `sale.order.line`, `sale.order`, `stock.warehouse`, `website` |
| website_sale_gelato | eCommerce/Gelato bridge |  | `product.document`, `product.template`, `res.partner`, `sale.order` |
| website_sale_loyalty | Coupons, Promotions, Gift Card and Loyalty for eCommerce | `coupon.share` | `loyalty.card`, `loyalty.program`, `loyalty.rule`, `product.product`, `sale.order.line`, `sale.order` |
| website_sale_mass_mailing | Checkout Newsletter |  | `res.config.settings`, `website` |
| website_sale_mrp | Kit Availability |  | `sale.order` |
| website_sale_project | Website Sale - Project |  | `withdrawal.request` |
| website_sale_slides | Sell Courses |  | `product.product`, `product.template`, `sale.order.line`, `sale.order`, `slide.channel` |
| website_sale_stock | Product Availability |  | `choose.delivery.carrier`, `delivery.carrier`, `product.product`, `product.template`, `res.config.settings`, `res.partner`, `sale.order`, `stock.picking`, `website` |
| website_slides | eLearning | `slide.channel`, `slide.channel.partner`, `slide.channel.tag.group`, `slide.channel.tag`, `slide.embed`, `slide.question`, `slide.answer`, `slide.slide`, `slide.slide.partner`, `slide.slide.resource`, `slide.tag`, `slide.channel.invite` | `base.partner.merge.automatic.wizard`, `digest.digest`, `gamification.challenge`, `gamification.karma.tracking`, `mail.activity`, `mail.message`, `res.config.settings`, `res.groups`, `res.partner`, `res.users`, `website.track`, `website.visitor`, `website` |
| website_slides_forum | Forum on Courses |  | `forum.forum`, `slide.channel` |
| website_slides_survey | Course Certifications |  | `slide.channel.partner`, `slide.channel`, `slide.slide.partner`, `slide.slide`, `survey.survey`, `survey.user_input` |
| website_sms | Send SMS to Visitor |  | `website.visitor` |
| website_timesheet | Hide Portal Timesheet Information |  | `account.analytic.line` |
