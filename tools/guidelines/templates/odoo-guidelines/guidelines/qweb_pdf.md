
# Declare a report as an ir.actions.report record

A report is an `ir.actions.report` record that names a QWeb template.$report_tag

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
- `report_type`: $report_types
- `binding_model_id` puts the report in the Print menu of that model; without it the
  report is printed only from code, with
  `self.env.ref('library.action_report_library_book').report_action(books)`.
- `print_report_name` is a Python expression on `object` (and `time`) giving the file
  name; `attachment` is one giving the name of an attachment that stores each printed
  PDF, and `attachment_use` returns that stored file on the next print instead of
  rendering again (for documents that must never change once printed).
- `$groups_field` restricts the report to those groups; the Print menu hides it from
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
  escaped unless the value is `Markup`. $esc
- `t-foreach="o.line_ids" t-as="line"` loops; `line_index`, `line_size`, `line_first`
  and `line_last` are set inside.
- Embed images with `image_data_uri(o.cover)`. A `/web/image` URL is fetched by the PDF
  engine over HTTP with the printing user's session; a report rendered without a
  request (a scheduled action, a mail sent by a cron) prints a broken image.
$tcall

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

$engine
