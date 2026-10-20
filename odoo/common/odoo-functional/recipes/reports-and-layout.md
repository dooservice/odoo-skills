# Reports and document layout

Printed documents (quotations, invoices, delivery slips) are QWeb reports
(`ir.actions.report`) wrapped in the company's external layout. The layout, logo,
colours, font, header, footer and default paper format are fields on `res.company`,
edited through the wizard `base.document.layout` ("Configure Document Layout"). A report
can override the paper format and its file name. Anything beyond these fields is a QWeb
change: code. Studio's report editor (Enterprise) is left out.

## Before you start

- Apps: `web` and `base_setup` (always installed); the reports come with their app.
- Settings: none to turn on. Per-report paper format, custom paper formats and file
  names are in Settings ‣ Technical ‣ Reporting, which needs developer mode.
- The layout is per company: switch to the company first, or use `with_company()`.
- PDF rendering needs `wkhtmltopdf` on the server; when it is missing or broken the error
  is about the binary, not the layout.
- Read first:

```python
c = env.company
print(c.read(['external_report_layout_id', 'font', 'primary_color', 'secondary_color', 'paperformat_id', 'report_header', 'report_footer', 'company_details']))
report = env.ref('account.account_invoices')
print(report.read(['name', 'report_name', 'paperformat_id', 'print_report_name', 'attachment_use', 'attachment']))
```

## The standard flow

1. **Configure the document layout.** Settings ‣ General Settings ‣ Companies ‣
   Configure Document Layout. Choose layout, font, logo, colours, background (16.0 to
   19.0), tagline, company details (Address from 18.0), footer and paper format; the
   preview on the right shows a sample, and Download PDF Preview (16.0, 17.0) prints one.
   Save (16.0, 17.0) or Continue (18.0+). The wizard's fields are related to the
   company, so writing the company is the same.

   ```python
   company.write({
       'external_report_layout_id': env.ref('web.external_layout_standard').id,
       'logo': logo_base64,  # base64 text: base64.b64encode(png_bytes).decode(); 20.0 refuses bytes
       'primary_color': '#1f3a5f', 'secondary_color': '#c8a24a',
       'font': 'Roboto',
   })
   env.cr.commit()
   ```

   - Layouts (XML ids in `web`): `external_layout_standard`, `_boxed`, `_bold`,
     `_striped` in 16.0 and 17.0; 18.0 and 19.0 add `_folder`, `_wave`, `_bubble`. 20.0
     keeps `_standard`, `_folder`, `_wave`, `_bubble`, adds `_center`, `_dual`,
     `_lines`, `_compact`, and drops `_boxed`, `_bold`, `_striped`. Check the list in
     `odoo-reference/xmlids/web.md` for the version.
   - `font`: `Lato`, `Roboto`, `Open_Sans`, `Montserrat`, `Oswald`, `Raleway`,
     `Tajawal`; 18.0 and 19.0 add `Fira_Mono`, 20.0 `Noto_Sans_Mono` instead.
   - `layout_background` (16.0 to 19.0): `Blank`, `Custom` (with
     `layout_background_image`), plus `Geometric` in 16.0 and 17.0 or `Demo logo` in
     18.0 and 19.0. Gone in 20.0.
   - 20.0 adds `report_tables_id` (table style): `light`, `boxed`, `bold`, `striped`,
     `bubble`, `column`, `compact`.
   - `company_details` (address block), `report_header` (tagline) and `report_footer`
     are HTML. `report_footer` is translatable in every version, `report_header` and
     `company_details` from 17.0: write them per language (see
     `languages-and-translations.md`).

   Leaves every report of that company printed with the new layout from the next print.

2. **Set the default paper format.** In the same wizard, Paper format: A4 or US Letter
   (other formats come with some apps).

   ```python
   company.write({'paperformat_id': env.ref('base.paperformat_us').id})
   env.cr.commit()
   ```

   `report.paperformat`: `format` (`A4`, `Letter`, other sizes, or `custom` with
   `page_height` / `page_width`), `orientation` (`Portrait`, `Landscape`), margins in
   mm, `header_spacing`, `dpi`. Standard ones: `base.paperformat_euro` (A4) and
   `base.paperformat_us` (Letter).

   Leaves every report without its own paper format printed on that size.

3. **Give one report its own paper format, when needed.** Settings ‣ Technical ‣
   Reporting ‣ Paper Format ‣ New for the format, then Settings ‣ Technical ‣ Reporting
   ‣ Reports, open the report and set Paper Format (developer mode).

   ```python
   narrow = env['report.paperformat'].create({
       'name': 'A4 narrow margins', 'format': 'A4', 'orientation': 'Portrait',
       'margin_top': 30, 'margin_bottom': 15, 'margin_left': 5, 'margin_right': 5,
   })
   env.ref('sale.action_report_saleorder').write({'paperformat_id': narrow.id})
   env.cr.commit()
   ```

   - A report's own `paperformat_id` wins over the company's.
   - Changing a shared paper format changes every report that uses it: create a new one.

   Leaves that report on its own format, for every company.

4. **Name the PDF file, when asked.** Same report form, Printed Report Name (on the
   Settings tab in 20.0).

   ```python
   env.ref('sale.action_report_saleorder').write({
       'print_report_name': "'%s - %s' % (object.name, object.partner_id.name)",
   })
   env.cr.commit()
   ```

   - `print_report_name` is a Python expression with `object` (the record) and `time`.
     It is translatable.
   - `attachment` (an expression for a file name) saves each printed PDF as an
     attachment; with `attachment_use` the saved file is returned on the next print
     instead of a new render, so later layout changes do not show on that record.

   Leaves the downloaded file named by the expression.

5. **Print one document and look at it.** Print from the document (its Print menu), and
   ask the user to look at it.

   ```python
   pdf, _ = env['ir.actions.report']._render_qweb_pdf('account.account_invoices', [invoice.id])
   ```

   Changes nothing.

## Variations

- **Several companies.** The layout and paper format are per company: repeat steps 1
  and 2 for each, switched to it in the company selector, or write each company.
- **Moving blocks, adding fields to a document, changing a table, a new report.** These
  are QWeb views. Editing a standard view in Settings ‣ Technical (or, from 19.0, Edit
  Layout in Settings ‣ Companies) is lost or breaks at the next update. Say what should
  change and hand over to `odoo-guidelines` for a small module that inherits the report
  template. With Enterprise, Studio's report editor is the other way.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Configure Document Layout | Settings ‣ General Settings ‣ Companies | same | same | same | same |
| Reports menu (developer mode) | Settings ‣ Technical ‣ Reporting ‣ Reports | same | same | same | same |
| Paper formats menu (developer mode) | Settings ‣ Technical ‣ Reporting ‣ Paper Format | same | same | same | same |
| Layouts | standard, boxed, bold, striped | same | adds folder, wave, bubble | as 18.0 | standard, folder, wave, bubble, center, dual, lines, compact |
| Fonts | 7 | 7 | adds `Fira_Mono` | as 18.0 | `Noto_Sans_Mono` instead of `Fira_Mono` |
| `layout_background` | Blank, Geometric, Custom | same | Blank, Demo logo, Custom | as 18.0 | gone |
| `report_tables_id` | - | - | - | - | yes |
| Translatable `report_header`, `company_details` | - | yes | yes | yes | yes |
| Wizard button that saves | Save | Save | Continue | Continue | Continue |
| Wizard labels | Company Tagline, Company Details | same | Tagline, Address, Text (font) | as 18.0 | as 18.0, plus Tables |
| Download PDF Preview button | yes | yes | - | - | - |
| `logo` written as base64 bytes | accepted | accepted | accepted | accepted | refused (write text) |
| Printed Report Name on the report form | main sheet | main sheet | main sheet | main sheet | Settings tab |

## Verify

```python
c = env.company
print(c.read(['external_report_layout_id', 'font', 'primary_color', 'paperformat_id']))
print(env.ref('sale.action_report_saleorder').read(['paperformat_id', 'print_report_name']))
invoice = env['account.move'].search([('move_type', '=', 'out_invoice'), ('state', '=', 'posted')], limit=1)
pdf, _ = env['ir.actions.report']._render_qweb_pdf('account.account_invoices', [invoice.id])
print(len(pdf), pdf[:4])
```

`pdf` starts with `%PDF`; then the user opens it and checks the layout.

## Pitfalls

- **Standard report actions are not `noupdate`**: a module update restores their paper
  format and file name. Record it in the change note so it can be applied again.
- **A saved attachment hides the change.** With `attachment_use`, a document printed
  before keeps its old PDF.
- **One company changed, the other forgotten.** Each company has its own layout.
- **The logo as bytes** fails in 20.0 and raw image bytes fail in every version: write
  base64 text.
- **Untranslated footer.** `report_footer` written without `lang` changes one language;
  customers in another see the old one.
- **`wkhtmltopdf` missing or broken**: the PDF fails or prints without header and footer;
  a server matter, not a layout one.
