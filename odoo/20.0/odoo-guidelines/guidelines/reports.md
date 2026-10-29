# QWeb PDF reports

- A custom report's `_get_report_values` must add the default `docs` / `doc_ids`
  / `doc_model` itself if the template needs them; they are not auto-included.
- For translated reports use `t-lang`: it is only valid on a node that also
  carries `t-call` (anywhere else QWeb raises a `SyntaxError` at template
  compile time); to translate part of a report,
  extract that part into its own template and `t-call` it with `t-lang`. Only
  re-browse records in the target language when the template reads
  translatable fields (otherwise it is a needless performance cost).

# Declare a report as an ir.actions.report record

A report is an `ir.actions.report` record that names a QWeb template. There is no `<report>`
tag: write the `<record>`.

```xml
<record id="action_report_library_book" model="ir.actions.report">
    <field name="name">Book Sheet</field>
    <field name="model">library.book</field>
    <field name="report_type">qweb-pdf</field>
    <field name="report_name">library.report_library_book</field>
    <field name="print_report_name">'Book - %s' % object.name</field>
    <field name="binding_model_id" ref="model_library_book"/>
    <field name="binding_type">report</field>
    <field name="paperformat_id" ref="paperformat_library_label"/>
</record>
```

- `report_name` is the XML id of the template, module included.
- `report_type`: `qweb-pdf` (a PDF rendered by the database's default engine),
  `qweb-pdf-wkhtmltopdf` or `qweb-pdf-paper-muncher` (a PDF rendered by that engine),
  `qweb-html` (opened in the browser) or `qweb-text` (plain text).
- `binding_model_id` puts the report in the Print menu of that model; without it the
  report is printed only from code, with
  `self.env.ref('library.action_report_library_book').report_action(books)`.
- `print_report_name` is a Python expression on `object` (and `time`) giving the file
  name; `attachment` is one giving the name of an attachment that stores each printed
  PDF, and `attachment_use` returns that stored file on the next print instead of
  rendering again (for documents that must never change once printed).
- `group_ids` restricts the report to those groups; the Print menu hides it from
  other users.

# Build report templates on web.html_container and web.external_layout

```xml
<template id="report_library_book">
    <t t-call="web.html_container">
        <t t-foreach="docs" t-as="o">
            <t t-call="web.external_layout">
                <div class="page">
                    <h2 t-field="o.name"/>
                    <p>Published: <span t-field="o.date_published"/></p>
                    <p t-if="o.isbn">ISBN: <span t-out="o.isbn"/></p>
                    <img t-if="o.cover" t-att-src="image_data_uri(o.cover)"/>
                </div>
            </t>
        </t>
    </t>
</template>
```

- `web.html_container` loads the report assets; every report starts with it.
- `web.external_layout` adds the company header and footer chosen in the settings. It
  takes the company from the loop variable `o` (or `doc`) and its `company_id`: name
  the loop variable `o`. `web.internal_layout` is the plain layout for internal
  documents, `web.basic_layout` has no header or footer.
- The content of each record goes in one `<div class="page">` inside the layout.
- `t-field="o.date_published"` prints a field formatted for its type, the language and
  the currency; use it for every field value. `t-out` prints any other expression,
  escaped unless the value is `Markup`. `t-esc` and `t-raw` are no longer
  directives: QWeb ignores them with a warning and prints nothing. Write `t-out`.
- `t-foreach="o.line_ids" t-as="line"` loops; `line_index`, `line_size`, `line_first`
  and `line_last` are set inside.
- Embed images with `image_data_uri(o.cover)`. A `/web/image` URL is fetched by the PDF
  engine over HTTP with the printing user's session; a report rendered without a
  request (a scheduled action, a mail sent by a cron) prints a broken image.
- Pass values to a sub-template as attributes of the `t-call` element, which must be
  a `<t>`: `<t t-call="library.report_book_line" show_price="True" title.f="Book {{o.name}}"/>`
  (`.f` marks a format string). A `t-set` inside the body no longer reaches the
  sub-template; `odoo-bin upgrade_code` rewrites that old form. The body reaches the
  sub-template as `0` (`<t t-out="0"/>`).

# Add values in _get_report_values only when the template needs them

When the template needs more than the records, an abstract model named after the
report computes the values:

```python
class ReportLibraryBook(models.AbstractModel):
    _name = 'report.library.report_library_book'
    _description = 'Book Sheet Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        books = self.env['library.book'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'library.book',
            'docs': books,
            'open_loans': books._get_open_loans(),
        }
```

- The `_name` is `report.` followed by the `report_name`; another name is never called.
- `data` is what `report_action(records, data={...})` passed, typically a wizard's
  values; read options from it, never from the context.
- Keep queries out of the template: compute grouped values here, in one query per
  model, instead of reading relations record by record in a `t-foreach`.

# Set the paper format on the report

```xml
<record id="paperformat_library_label" model="report.paperformat">
    <field name="name">Library Label</field>
    <field name="format">custom</field>
    <field name="page_height">100</field>
    <field name="page_width">60</field>
    <field name="orientation">Portrait</field>
    <field name="margin_top">10</field>
    <field name="margin_bottom">5</field>
    <field name="margin_left">5</field>
    <field name="margin_right">5</field>
    <field name="header_spacing">5</field>
    <field name="dpi">90</field>
</record>
```

- A report without `paperformat_id` uses the company's paper format.
- `page_height` and `page_width` (millimeters) are only allowed with `format` set to
  `custom`; any other `format` is a standard size such as `A4` or `Letter`.
- `margin_top` must leave room for the layout's header and `header_spacing`, or the
  header covers the first lines.

# Check reports in the PDF, not in the HTML preview

- `qweb-pdf` uses the engine named by the `report.pdf_engine_default` system
  parameter: `wkhtmltopdf`, set by `base_report_wkhtmltox`, which installs
  automatically. `base_report_paper_muncher` adds Odoo's own engine, chosen per report
  with `qweb-pdf-paper-muncher`; a module whose report names an engine depends on the
  module that provides it.
- wkhtmltopdf renders the report's HTML with an old WebKit: the HTML preview
  (`qweb-html`, or the browser) shows what a modern browser does, not what the PDF
  shows. Check every layout change in the printed PDF.
- wkhtmltopdf loads the report's CSS and images from the server at the `report.url`
  system parameter, or `web.base.url` when it is unset: when the Odoo machine cannot
  reach that URL, PDFs print without styles.
- With `--workers=1` no PDF prints: the only worker waits for wkhtmltopdf while
  wkhtmltopdf asks the server for the assets. Run with `--workers=0` or at least 2.
