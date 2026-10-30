---
name: odoo-guidelines
description: >-
  Read before writing or reviewing any Python, XML or CSV for Odoo 18.0,
  even if you know Odoo: names change between versions. In 18.0: `<list>` (no `<tree>`) and `invisible="expr"`; `_compute_display_name`; `_sql_constraints` (no `models.Constraint`); `expression.AND/OR` (no `Domain`); `aggregator`; `<chatter/>`; `self.env._()`; `ir.model.access.csv` and `ir.rule`; users `groups_id`, groups `users` and `category_id`; `get_param`; routes `type='json'`; test tag `at_install`.
  Covers modules, models, fields, the ORM, api decorators, views, actions,
  menus, scheduled actions, security, controllers, the external API, mail,
  multi-company, reports, data, migrations, translations, tests and odoo-bin;
  JavaScript, Owl and SCSS are in odoo-web-guidelines.
---

# Odoo 18.0 addon guidelines

House rules for code in Odoo 18.0 addons. Everything an addon ships under `static/`
has its own skill: `odoo-web-guidelines`.

Guidelines are grouped by domain, one file per domain in `guidelines/`, one section per
guideline. No rule outranks another. Read the sections that match the files you are
touching instead of loading whole files. The version table comes first whenever an API
is in doubt: these rules are written for 18.0 and the table says what 18.0 has.

| Guideline | Read it when |
| --- | --- |
| [What Odoo 18.0 has](guidelines/version.md#what-odoo-180-has) | before writing any API, view attribute, JS import, security record, system parameter call or business record field you are not sure exists in this version |
| [Module structure and file naming](guidelines/module_structure.md#module-structure-and-file-naming) | creating or moving files in an addon, or adding a module |
| [Manifest](guidelines/manifest.md#manifest) | touching `__manifest__.py` |
| [Imports](guidelines/python.md#imports) | writing Python anywhere in an addon |
| [Naming and model layout](guidelines/python.md#naming-and-model-layout) | naming a model, field, method or variable; laying out a model class |
| [Translate only static literals](guidelines/python.md#translate-only-static-literals) | user-facing strings in Python |
| [Model classes and attributes](guidelines/models.md#model-classes-and-attributes) | creating a model, or setting `_order`, `_rec_name`, `_log_access`, other `_` attributes |
| [Pick the inheritance mechanism](guidelines/models.md#pick-the-inheritance-mechanism-for-what-you-need) | `_inherit`, `_inherits`, mixins, `delegate=True` |
| [Override with super() and the same signature](guidelines/models.md#override-with-super-and-the-same-signature) | overriding any method of another module |
| [Declare SQL constraints and indexes](guidelines/models.md#declare-sql-constraints-and-indexes-on-the-model) | uniqueness, `CHECK`, multi-column or partial indexes |
| [Store hierarchies with _parent_store](guidelines/models.md#store-hierarchies-with-_parent_store) | tree models, `child_of`/`parent_of`, recursion checks |
| [Back reporting models by an SQL view](guidelines/models.md#back-reporting-models-by-an-sql-view) | report models with `_auto = False` |
| [Fields](guidelines/fields.md#fields) | declaring or modifying field definitions |
| [Field types](guidelines/fields.md#field-types) | choosing a field type |
| [Field attributes](guidelines/fields.md#field-attributes) | `required`, `readonly`, `default`, `copy`, `translate`, `company_dependent`, aggregation, `group_expand` |
| [Relational fields](guidelines/fields.md#relational-fields) | `Many2one`/`One2many`/`Many2many` options, `ondelete` |
| [Store datetimes in UTC](guidelines/fields.md#store-datetimes-in-utc-and-dates-as-the-users-day) | `Date`/`Datetime` values, "today" |
| [Compare floats at their precision](guidelines/fields.md#compare-floats-at-their-precision) | comparing or rounding quantities and amounts |
| [Declare every dependency of a computed field](guidelines/fields.md#declare-every-dependency-of-a-computed-field) | computed fields, `store`, `precompute`, `compute_sudo` |
| [Write inverse and search methods](guidelines/fields.md#write-inverse-and-search-methods-for-computed-fields) | making a computed field editable or searchable |
| [Use related for a plain copy](guidelines/fields.md#use-related-for-a-plain-copy-of-another-records-field) | `related` fields |
| [Keep Json for data the ORM does not query](guidelines/fields.md#keep-json-for-data-the-orm-does-not-query) | `Json`, `Properties` fields |
| [Extend a selection with selection_add](guidelines/fields.md#extend-a-selection-with-selection_add-and-an-ondelete-policy) | adding values to another module's `Selection` |
| [Index selectively](guidelines/fields.md#index-selectively) | `index=` on a field |
| [Add stored fields to large tables cheaply](guidelines/fields.md#add-stored-fields-to-large-tables-cheaply) | adding a stored field to an installed model |
| [Method decorators](guidelines/api.md#method-decorators) | using or overriding any `@api.*` decorated method |
| [Override create with @api.model_create_multi](guidelines/api.md#override-create-with-apimodel_create_multi) | overriding `create` |
| [Block deletion with @api.ondelete](guidelines/api.md#block-deletion-with-apiondelete-not-an-unlink-override) | preventing deletion, overriding `unlink` |
| [Validate with @api.constrains](guidelines/api.md#validate-with-apiconstrains-and-know-what-it-does-not-see) | writing a Python constraint |
| [Use @api.onchange only for form-side help](guidelines/api.md#use-apionchange-only-for-form-side-help) | writing an onchange, or choosing between onchange and compute |
| [Recordsets, domains and context](guidelines/orm.md#recordsets-domains-and-context) | reading records, building domains, passing context |
| [Recordset operations](guidelines/orm.md#recordset-operations) | combining, filtering, sorting, grouping recordsets in Python; `browse`, `exists`, `new` |
| [Environment and context switches](guidelines/orm.md#environment-and-context-switches) | `sudo`, `with_user`, `with_company`, `with_context`, `env.ref` |
| [Search and read](guidelines/orm.md#search-and-read) | `search*`, `read*`, grouped reads, `name_search`, display name, `default_get` |
| [Write x2many values with Command](guidelines/orm.md#write-x2many-values-with-command) | writing `One2many`/`Many2many` values |
| [Override write, unlink and copy in batch](guidelines/orm.md#override-write-unlink-and-copy-in-batch) | overriding `write`, `unlink`, `copy` or `copy_data` |
| [Check access rights in code](guidelines/orm.md#check-access-rights-in-code) | access checks before `sudo()`, field access, user groups |
| [Flush and invalidate around raw SQL](guidelines/orm.md#flush-and-invalidate-around-raw-sql) | raw SQL next to ORM code, `ormcache` caches |
| [Translate field values with the translation API](guidelines/orm.md#translate-field-values-with-the-translation-api) | reading or writing translations of field values |
| [Archive with action_archive](guidelines/orm.md#archive-with-action_archive) | archiving, `active`, `active_test` |
| [Lock rows you are about to change](guidelines/orm.md#lock-rows-you-are-about-to-change) | concurrent updates, counters, queues |
| [Import, export and other public methods](guidelines/orm.md#import-export-and-other-public-methods) | `load`, `export_data`, `get_base_url`, `init`, `onchange` |
| [Methods and extension points](guidelines/orm.md#methods-and-extension-points) | adding a model method, or one another module will override |
| [Transactions and exceptions](guidelines/orm.md#transactions-and-exceptions) | cursors, commits, savepoints, `try`/`except` |
| [Controllers](guidelines/controllers.md#controllers) | touching `controllers/` or `@route` |
| [Choose the route type for the caller](guidelines/controllers.md#choose-the-route-type-for-the-caller) | adding a route or choosing its `type=` |
| [Set `auth` on every route](guidelines/controllers.md#set-auth-on-every-route) | adding or overriding a route, or an endpoint called by another system |
| [Route arguments](guidelines/controllers.md#route-arguments) | setting `methods`, `csrf`, `cors`, `save_session`, `readonly`, `website` or `sitemap` on a route |
| [Read the request and answer through `request`](guidelines/controllers.md#read-the-request-and-answer-through-request) | reading parameters or building a response in a controller |
| [Check access on records reached through a route](guidelines/controllers.md#check-access-on-records-reached-through-a-route) | a route that takes a record id or a model converter |
| [Portal pages](guidelines/controllers.md#portal-pages) | `/my/` pages, `CustomerPortal`, `portal.mixin` or access tokens |
| [Call Odoo from outside through the external API](guidelines/external_api.md#call-odoo-from-outside-through-the-external-api) | writing a script or integration that calls Odoo (XML-RPC, JSON-RPC, JSON-2) |
| [Authenticate integrations with an API key of a dedicated user](guidelines/external_api.md#authenticate-integrations-with-an-api-key-of-a-dedicated-user) | setting up credentials for an integration, `res.users.apikeys` |
| [Expose only public, checked methods to RPC](guidelines/external_api.md#expose-only-public-checked-methods-to-rpc) | adding a public model method that clients may call |
| [Batch external calls](guidelines/external_api.md#batch-external-calls) | an integration that reads or writes many records |
| [Add the chatter with `mail.thread`](guidelines/mail.md#add-the-chatter-with-mailthread) | inheriting `mail.thread` or `mail.activity.mixin`, or adding the chatter to a form |
| [Track field changes with `tracking=`](guidelines/mail.md#track-field-changes-with-tracking) | `tracking=` on fields, tracking subtypes, mail context keys |
| [Post messages with `message_post`](guidelines/mail.md#post-messages-with-message_post) | posting, notifying or logging on a record |
| [Followers and subtypes](guidelines/mail.md#followers-and-subtypes) | `message_subscribe`, `mail.message.subtype` records, suggested recipients |
| [Send emails with `mail.template`](guidelines/mail.md#send-emails-with-mailtemplate) | `mail.template` records or sending email from code |
| [Receive emails through aliases](guidelines/mail.md#receive-emails-through-aliases) | `message_new`, `message_update`, `mail.alias.mixin` |
| [Make a model multi-company](guidelines/multi_company.md#make-a-model-multi-company) | adding `company_id`, `check_company` or `_check_company_auto` |
| [Restrict records to the allowed companies](guidelines/multi_company.md#restrict-records-to-the-allowed-companies) | the company rule of a model with `company_id` |
| [Work in the right company in code](guidelines/multi_company.md#work-in-the-right-company-in-code) | `env.company`, `with_company`, crons over companies, `company_dependent` fields |
| [Access rights](guidelines/security.md#access-rights) | touching `security/` (access rows, record rules, groups) |
| [Grant every model access explicitly](guidelines/security.md#grant-every-model-access-explicitly) | adding a model or an access row |
| [Restrict records with domains](guidelines/security.md#restrict-records-with-domains) | writing a record rule or a domain on an access row |
| [Declare groups per application](guidelines/security.md#declare-groups-per-application) | adding or changing `res.groups` records |
| [Check group membership in code](guidelines/security.md#check-group-membership-in-code) | `has_group`, `has_groups`, `user_has_groups` |
| [Restrict fields with `groups=`](guidelines/security.md#restrict-fields-with-groups) | `groups=` on a field |
| [Use `sudo()` only after an explicit check](guidelines/security.md#use-sudo-only-after-an-explicit-check) | any `sudo()` or `with_user()` |
| [Views, actions and data records](guidelines/xml.md#views-actions-and-data-records) | touching `views/`, `data/`, or any XML records |
| [Anchor view inheritance on names, never on position](guidelines/xml.md#anchor-view-inheritance-on-names-never-on-position) | extending or overriding an existing view |
| [Field values in data records](guidelines/xml.md#field-values-in-data-records) | writing `<field>` values in data XML: `ref`, `eval`, `search`, `type`, `%(xml_id)d` |
| [Load only what an update can redo](guidelines/xml.md#load-only-what-an-update-can-redo) | choosing `noupdate`, or using `<function>`, `<delete>` or `forcecreate` in data files |
| [Inherit views by extension, with the position that matches the change](guidelines/xml.md#inherit-views-by-extension-with-the-position-that-matches-the-change) | writing an inheriting view: `inherit_id`, `mode="primary"`, `priority`, `position`, `<attribute>` |
| [View records](guidelines/views.md#view-records) | adding an `ir.ui.view`, or choosing a view type or the default view |
| [Write dynamic modifiers in the syntax this version evaluates](guidelines/views.md#write-dynamic-modifiers-in-the-syntax-this-version-evaluates) | making `invisible`/`readonly`/`required`/`column_invisible` depend on the record |
| [Form views](guidelines/views.md#form-views) | writing or extending a form view or a wizard form |
| [List views](guidelines/views.md#list-views) | writing a list view or an x2many list |
| [Kanban views](guidelines/views.md#kanban-views) | writing a kanban view or its card template |
| [Search views](guidelines/views.md#search-views) | writing filters, group-bys or a searchpanel |
| [Calendar, graph and pivot views](guidelines/views.md#calendar-graph-and-pivot-views) | writing a calendar, graph or pivot view |
| [Activity, hierarchy and QWeb views](guidelines/views.md#activity-hierarchy-and-qweb-views) | writing an activity or hierarchy view, or a `<template>` |
| [Show and hide view parts by group](guidelines/views.md#show-and-hide-view-parts-by-group) | adding `groups=` to view nodes or restricting a view to groups |
| [Action records](guidelines/actions.md#action-records) | adding any `ir.actions.*` record: shared fields, `path`, groups |
| [Window actions](guidelines/actions.md#window-actions) | writing an `ir.actions.act_window` or its `ir.actions.act_window.view` records |
| [Return actions from Python as dicts or by xml id](guidelines/actions.md#return-actions-from-python-as-dicts-or-by-xml-id) | a button method, wizard or server action that returns an action |
| [Bind actions to the Action and Print menus](guidelines/actions.md#bind-actions-to-the-action-and-print-menus) | setting `binding_model_id` / `binding_view_types` |
| [Server actions](guidelines/actions.md#server-actions) | writing an `ir.actions.server` record |
| [Scheduled actions](guidelines/actions.md#scheduled-actions) | writing an `ir.cron` record or a `_cron_` method |
| [Menus](guidelines/actions.md#menus) | adding or changing `<menuitem>` |
| [Configuration wizards](guidelines/actions.md#configuration-wizards) | adding an `ir.actions.todo` |
| [QWeb PDF reports](guidelines/reports.md#qweb-pdf-reports) | report templates or `_get_report_values` |
| [Declare a report as an ir.actions.report record](guidelines/reports.md#declare-a-report-as-an-iractionsreport-record) | adding a report action |
| [Build report templates on web.html_container and web.external_layout](guidelines/reports.md#build-report-templates-on-webhtml_container-and-webexternal_layout) | writing a QWeb report template |
| [Add values in _get_report_values only when the template needs them](guidelines/reports.md#add-values-in-_get_report_values-only-when-the-template-needs-them) | a `report.<name>` abstract model |
| [Set the paper format on the report](guidelines/reports.md#set-the-paper-format-on-the-report) | `report.paperformat` records |
| [Check reports in the PDF, not in the HTML preview](guidelines/reports.md#check-reports-in-the-pdf-not-in-the-html-preview) | PDF layout problems, missing styles, PDF engine |
| [Batch ORM calls](guidelines/performance.md#batch-orm-calls) | ORM calls (`create`/`search*`/aggregates) inside a loop |
| [Performance conventions](guidelines/performance.md#performance-conventions) | code that loops over records or filters query results |
| [Tests](guidelines/tests.md#tests) | touching `tests/` |
| [Pick the test class by what the test needs](guidelines/tests.md#pick-the-test-class-by-what-the-test-needs) | choosing a base class for a test |
| [Tag every test class with the moment it runs](guidelines/tests.md#tag-every-test-class-with-the-moment-it-runs) | writing `@tagged`, or a test that runs at the wrong time or never |
| [Make sure the runner collects every test](guidelines/tests.md#make-sure-the-runner-collects-every-test) | a test that does not run, or runs twice |
| [Build shared data in setUpClass](guidelines/tests.md#build-shared-data-in-setupclass) | writing `setUpClass`/`setUp`, or using `BaseCommon` |
| [Drive form behavior through Form](guidelines/tests.md#drive-form-behavior-through-form) | testing onchanges, defaults or required/readonly fields |
| [Count queries only in dedicated performance tests](guidelines/tests.md#count-queries-only-in-dedicated-performance-tests) | `assertQueryCount`, `@users`, `@warmup` |
| [Freeze the date a test depends on](guidelines/tests.md#freeze-the-date-a-test-depends-on) | a test whose result depends on today's date |
| [Test routes and tours with HttpCase](guidelines/tests.md#test-routes-and-tours-with-httpcase) | testing a controller, a JSON-RPC route or a tour |
| [Other test decorators](guidelines/tests.md#other-test-decorators) | `@no_retry`, `@standalone`, `@test_xsd` |
| [Select tests with test tags](guidelines/tests.md#select-tests-with-test-tags) | running some tests with `--test-tags` |
| [Changes to an installed module](guidelines/installed.md#changes-to-an-installed-module) | updating a module that is already installed in a database that matters: version, migration, test on a clone |
| [List data files in the order they reference each other](guidelines/installed.md#list-data-files-in-the-order-they-reference-each-other) | adding or reordering files in the manifest's `data` |
| [Mark records that users may change as noupdate](guidelines/installed.md#mark-records-that-users-may-change-as-noupdate) | `noupdate`, `forcecreate`, `<function>` or `<delete>` in data files |
| [Keep demo data out of what the module needs](guidelines/installed.md#keep-demo-data-out-of-what-the-module-needs) | touching the manifest's `demo` files |
| [Changes in a stable version](guidelines/stable.md#changes-in-a-stable-version) | fixing a module version that is already installed in a database that matters |
| [Version the module as series.x.y.z](guidelines/migrations.md#version-the-module-as-seriesxyz) | changing the manifest `version` |
| [Write a migration script for every data change between two versions](guidelines/migrations.md#write-a-migration-script-for-every-data-change-between-two-versions) | renaming, removing or reshaping stored data; touching `migrations/` |
| [Use upgrade-util for renames and removals](guidelines/migrations.md#use-upgrade-util-for-renames-and-removals) | renaming or removing a field, model or XML id |
| [Use init hooks only for install-time work](guidelines/migrations.md#use-init-hooks-only-for-install-time-work) | `pre_init_hook`, `post_init_hook`, `uninstall_hook`, `post_load` |
| [Ship translations as .po files in i18n/](guidelines/translations.md#ship-translations-as-po-files-in-i18n) | touching `i18n/` |
| [Know which terms are translatable](guidelines/translations.md#know-which-terms-are-translatable) | adding user-facing strings or lazy translated constants |
| [Declare translatable fields with translate](guidelines/translations.md#declare-translatable-fields-with-translate) | `translate=True`, `html_translate`, reading or writing translations |
| [Export terms with odoo-bin, never by hand](guidelines/translations.md#export-terms-with-odoo-bin-never-by-hand) | generating `.pot`/`.po`, importing translations |
| [Run odoo-bin with explicit options](guidelines/command_line.md#run-odoo-bin-with-explicit-options) | running `odoo-bin` (install, update, config, logging, dev mode) |
| [Inspect a database with odoo-bin shell, then roll back](guidelines/command_line.md#inspect-a-database-with-odoo-bin-shell-then-roll-back) | using `odoo-bin shell` |
| [Use the odoo-bin subcommand made for the task](guidelines/command_line.md#use-the-odoo-bin-subcommand-made-for-the-task) | scaffold, db, neutralize, cloc, populate/duplicate, upgrade_code, i18n, module |
| [Plain ASCII punctuation in comments and messages](guidelines/comments.md#plain-ascii-punctuation-in-comments-and-messages) | writing a comment, a docstring, a user-facing string, or a commit message |

To add or restructure a guideline, follow [AUTHORING.md](AUTHORING.md).

Adapted from Odoo's own skill library (odoo/odoo, branch 20.0, `skills/`, LGPL-3) and
checked against the 18.0 source.
