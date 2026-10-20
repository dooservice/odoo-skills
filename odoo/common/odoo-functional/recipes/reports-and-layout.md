# Reports and document layout

Printed documents (quotations, invoices, delivery slips) are QWeb reports
(`ir.actions.report`) wrapped in the company's external layout. The layout, logo,
colours, font, header and footer are fields on `res.company`, edited through the
wizard `base.document.layout` ("Configure Document Layout"). Paper format is per company,
and a report can override it. Anything beyond these fields is a QWeb change: code.

```python
c = env.company
print(c.read(['external_report_layout_id', 'font', 'primary_color', 'secondary_color', 'paperformat_id', 'report_header', 'report_footer', 'company_details']))
report = env.ref('account.account_invoices')
print(report.read(['name', 'report_name', 'paperformat_id', 'print_report_name', 'attachment_use', 'attachment']))
```

## Document layout

The wizard's fields are related to the company, so writing the company is the same.

```python
company.write({
    'external_report_layout_id': env.ref('web.external_layout_standard').id,
    'logo': logo_base64,  # base64 text: base64.b64encode(png_bytes).decode(); 20.0 refuses bytes
    'primary_color': '#1f3a5f', 'secondary_color': '#c8a24a',
    'font': 'Roboto',
})
env.cr.commit()
```

- Layouts (XML ids in `web`): `external_layout_standard`, `_boxed`, `_bold`, `_striped`
  in 16.0 and 17.0; 18.0 and 19.0 add `_folder`, `_wave`, `_bubble`. 20.0 keeps
  `_standard`, `_folder`, `_wave`, `_bubble`, adds `_center`, `_dual`, `_lines`,
  `_compact`, and drops `_boxed`, `_bold`, `_striped`. Check the list in
  `odoo-reference/xmlids/web.md` for the version.
- `font`: `Lato`, `Roboto`, `Open_Sans`, `Montserrat`, `Oswald`, `Raleway`, `Tajawal`;
  18.0 and 19.0 add `Fira_Mono`, 20.0 `Noto_Sans_Mono` instead.
- `layout_background` (16.0 to 19.0): `Blank`, `Custom` (with `layout_background_image`),
  plus `Geometric` in 16.0 and 17.0 or `Demo logo` in 18.0 and 19.0. Gone in 20.0.
- 20.0 adds `report_tables_id` (table style): `light`, `boxed`, `bold`, `striped`,
  `bubble`, `column`, `compact`.
- `company_details` (address block), `report_header` (tagline) and `report_footer` are
  HTML. `report_footer` is translatable in every version, `report_header` and
  `company_details` from 17.0: write them per language (see
  `languages-and-translations.md`).
- The layout is per company. In multi-company, set each one.

## Paper format

`report.paperformat`: `format` (`A4`, `Letter`, other sizes, or `custom` with
`page_height` / `page_width`), `orientation` (`Portrait`, `Landscape`), margins in mm,
`header_spacing`, `dpi`. Standard ones: `base.paperformat_euro` (A4) and
`base.paperformat_us` (Letter).

```python
company.write({'paperformat_id': env.ref('base.paperformat_us').id})
narrow = env['report.paperformat'].create({
    'name': 'A4 narrow margins', 'format': 'A4', 'orientation': 'Portrait',
    'margin_top': 30, 'margin_bottom': 15, 'margin_left': 5, 'margin_right': 5,
})
env.ref('sale.action_report_saleorder').write({'paperformat_id': narrow.id})
env.cr.commit()
```

- A report's own `paperformat_id` wins over the company's.
- Changing a shared paper format changes every report that uses it: create a new one.

## File name

`print_report_name` on `ir.actions.report` is a Python expression with `object` (the
record) and `time`. It is translatable.

```python
env.ref('sale.action_report_saleorder').write({
    'print_report_name': "'%s - %s' % (object.name, object.partner_id.name)",
})
env.cr.commit()
```

- Standard report actions are not `noupdate`: a module update restores them. Record it
  in the change note so it can be applied again.
- `attachment` (an expression for a file name) saves each printed PDF as an attachment;
  with `attachment_use` the saved file is returned on the next print instead of a new
  render, so later layout changes do not show on that record.

## Check the result

```python
pdf, _ = env['ir.actions.report']._render_qweb_pdf('account.account_invoices', [invoice.id])
```

Render one document after any change and ask the user to look at it. PDF rendering
needs `wkhtmltopdf` on the server; when it is missing or broken the error is about the
binary, not the layout.

## When it needs code

Moving blocks, adding fields to a document, changing a table, a new report: these are
QWeb views. Editing a standard view in Settings > Technical is lost or breaks at the
next update. Say what should change and hand over to `odoo-guidelines` for a small
module that inherits the report template.
