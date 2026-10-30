# Quotation builder: PDF quotes with headers, footers and product sheets

How a quotation's PDF is enriched beyond the standard report. From 17.0,
`sale_pdf_quote_builder` merges PDF pages around the quote table: header and footer pages
(a cover letter, terms, references) and product sheets per order line, and fills the PDF
form fields in them with order data. In 16.0, `sale_quotation_builder` instead adds web
content, designed in the Website editor, to the customer's online quotation. Both work on
quotation templates (`sale_management`), whose basics are in `sales-and-crm.md`. All in
Community.

**At a glance**

- Apps: `sale_management`. 17.0+: `sale_pdf_quote_builder`, installed with it. 16.0:
  `sale_quotation_builder`, which installs Website.
- Names that change by version: `sale_quotation_builder` in 16.0, `sale_pdf_quote_builder`
  17.0+; headers and footers binaries on company and template in 17.0,
  `quotation.document` 18.0+ (`add_by_default` 19.0+); product sheet flag
  `attached_on='inside'` 17.0, `attached_on_sale='inside'` 18.0+; form fields
  `sale.pdf.form.field` 18.0+; template tab Website Description 16.0, PDF Quote Builder
  17.0, Quote Builder 18.0+; templates menu Templates 20.0.
- Sections: Before you start; The standard flow (1 prepare the PDFs, 2 upload headers and
  footers, 3 attach the product sheets, 4 map the form fields (18.0+), 5 build the quote,
  6 print or send it); Variations; Versions; Verify; Pitfalls.

## Before you start

- Settings, Sales ‣ Configuration ‣ Settings:

| Setting | Field | Versions |
|---|---|---|
| Quotation Templates | `group_sale_order_template` | 16.0-19.0 |
| Quotation Builder | `module_sale_quotation_builder` (needs Quotation Templates) | 16.0 |
| PDF Quote builder | `module_sale_pdf_quote_builder` | 17.0+ |
| Header and footer pages of the company | `sale_header`, `sale_footer` (binary PDFs on the company) | 17.0 only |

- The PDFs must not be encrypted; header, footer and product sheets must be PDF files.
- Read first:

18.0 to 20.0:

```python
print(env['ir.module.module'].search([('name', '=', 'sale_pdf_quote_builder')]).state)
print(env['sale.order.template'].search_read([], ['name']))
print(env['quotation.document'].search_read([], ['name', 'document_type', 'quotation_template_ids', 'active']))
print([(d.name, d.res_model, d.res_id, d.mimetype) for d in env['product.document'].search([])])
```

17.0 has no `quotation.document`: drop that line. 16.0 has no `product.document` either:

```python
print(env['ir.module.module'].search([('name', '=', 'sale_quotation_builder')]).state)
print(env['sale.order.template'].search_read([], ['name']))
```

## The standard flow

Odoo's documentation (17.0+): upload header and footer pages, attach product sheets to
products, map the form fields, then build each quote and send it.

1. **Prepare the PDFs.** Outside Odoo: a header (cover, presentation), a footer (terms,
   references) and one sheet per product. To print order data in them, add PDF form
   fields named as Odoo's mapping: on headers and footers `name`, `partner_id__name`,
   `user_id__name`, `amount_untaxed`, `amount_total`, `validity_date`,
   `client_order_ref`, `delivery_date` (18.0+ also `order_date`, `user_id__email`); on
   product sheets also `description`, `quantity`, `uom`, `price_unit`, `discount`,
   `product_sale_price`, `taxes`, `tax_excl_price`, `tax_incl_price`.

2. **Upload headers and footers.** 18.0+: Sales ‣ Configuration ‣ Sales Orders ‣
   Headers/Footers: add the PDF, then set on it its type, the quotation templates it
   applies to (empty: all) and, 19.0+, Add By Default. 17.0: Sales ‣ Configuration ‣
   Settings, PDF Quote builder (the company's pages), or the template's PDF Quote Builder
   tab (that template's pages).

   19.0 and 20.0:

   ```python
   import base64
   pdf = base64.b64encode(open('/tmp/cover.pdf', 'rb').read())
   header = env['quotation.document'].create({
       'name': 'cover.pdf', 'datas': pdf, 'document_type': 'header',
       'quotation_template_ids': [(6, 0, template.ids)],
       'add_by_default': True,
   })
   env.cr.commit()
   ```

   18.0: the same without `add_by_default`, which does not exist yet.

   17.0:

   ```python
   import base64
   pdf = base64.b64encode(open('/tmp/cover.pdf', 'rb').read())
   env.company.write({'sale_header': pdf, 'sale_header_name': 'cover.pdf'})
   template.write({'sale_header': pdf, 'sale_header_name': 'cover.pdf'})
   env.cr.commit()
   ```

   Leaves a `quotation.document` (18.0+) with its form fields detected
   (`form_field_ids`), or the binaries on the company and template (17.0). A template's
   pages replace the company's in 17.0.

3. **Attach the product sheets.** The product form ‣ Documents smart button: add the PDF,
   then on the document: 17.0 Visibility (`attached_on`) Inside quote; 18.0-19.0 Sales
   visibility (`attached_on_sale`) Inside quote pdf; 20.0 nothing to set, any PDF of the
   product is offered.

   ```python
   sheet = base64.b64encode(open('/tmp/product_a.pdf', 'rb').read())
   doc = env['product.document'].create({
       'name': 'product_a.pdf', 'datas': sheet,
       'res_model': 'product.template', 'res_id': tmpl.id,
   })
   env.cr.commit()
   ```

   This is 20.0. In 18.0 and 19.0 add `'attached_on_sale': 'inside'`; in 17.0 add
   `'attached_on': 'inside'`.

   Leaves a `product.document` on the product (or on one variant with
   `res_model='product.product'`).

4. **Map the form fields (18.0+).** The document ‣ Configure dynamic fields (Configure on
   the product document in 20.0), as administrator: for each field name a `path` from the order (headers and
   footers) or from the order line (product sheets), such as `partner_id.city` or
   `order_id.partner_id.vat`. Leave the path empty to type the value per quote.

   ```python
   field = env['sale.pdf.form.field'].search([('name', '=', 'partner_city'), ('document_type', '=', 'quotation_document')])
   field.path = 'partner_id.city'
   env.cr.commit()
   ```

   Leaves the field filled from that path on every PDF. The standard names of step 1 are
   mapped already. 17.0 has only the standard names.

5. **Build the quote.** Sales ‣ Orders ‣ Quotations ‣ New, choose the template and the
   products, then the Quote Builder tab (18.0+): tick the headers, footers and product
   sheets to include and type the values of unmapped fields. In 17.0 there is no choice:
   the template's (or company's) pages and every Inside quote sheet of the order's
   products are included.

   ```python
   order = env['sale.order'].create({'partner_id': customer.id, 'sale_order_template_id': template.id})
   order._onchange_sale_order_template_id()
   order.quotation_document_ids = [(4, header.id)]
   line = order.order_line.filtered(lambda l: l.product_template_id == tmpl)
   line.product_document_ids = [(4, doc.id)]
   env.cr.commit()
   ```

   This is 18.0 to 20.0. In 17.0 stop after `_onchange_sale_order_template_id()`: there
   is nothing to select.

   Leaves the quotation in `draft` with its selected documents. 19.0+ preselects the
   documents with Add By Default that apply to all templates, and those of the chosen
   template.

6. **Print or send it.** The quotation's Print ‣ Quotation / Order, or Send by Email
   (`sales-and-crm.md`, step 5): the PDF is header pages, product sheets, the quote
   table, footer pages.

   ```python
   content, _ = env['ir.actions.report']._render_qweb_pdf('sale.action_report_saleorder', order.ids)
   open('/tmp/%s.pdf' % order.name.replace('/', '_'), 'wb').write(content)
   ```

   Leaves the order unchanged; the composed PDF is what the customer receives.

## Variations

- **16.0: Quotation Builder (web content).** Turn on Quotation Templates and Quotation
  Builder. Sales ‣ Configuration ‣ Sales Orders ‣ Quotation Templates ‣ the template ‣
  Design Template opens it in the Website editor (`/@/sale_quotation_builder/template/<id>`);
  drop building blocks and save. A product's own block comes from its Quotation Only
  Description (`quotation_only_description`), or its eCommerce description. A quotation
  created from the template copies the content into `website_description` (order and
  lines), shown to the customer on the online quotation (Customer Preview), not in the
  PDF.

  ```python
  template.website_description = '<section class="s_text_block"><div class="container"><p>Why choose us</p></div></section>'
  order = env['sale.order'].create({'partner_id': customer.id, 'sale_order_template_id': template.id})
  print(bool(order.website_description))
  env.cr.commit()
  ```

- **Product sheets after the quote table (20.0).** Sheets whose Accessible
  (`attached_on_sale`) is From Quotation or On Order Confirmation go after the quote
  table; Never (and, with eCommerce, Shown on product page) go before it.
- **Confirmed orders (19.0+).** The documents are added to quotations only; to keep them
  on confirmed orders set the system parameter `sale.always_include_selected_documents`
  to `True`.
- **One header for every quote (19.0+).** A header with no template and Add By Default
  is preselected on every new quotation.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Module | `sale_quotation_builder` (web content) | `sale_pdf_quote_builder` | same | same | same |
| Headers and footers | none | binaries on company and template | `quotation.document`, menu Headers/Footers | same, `add_by_default` | same |
| Product sheet flag | none | `attached_on='inside'` | `attached_on_sale='inside'` | same | any PDF document |
| Choice per quote | none | none, all included | Quote Builder tab (after Optional Products) | Quote Builder tab (after Order Lines) | same as 19.0 |
| Form fields | none | standard names only | `sale.pdf.form.field` with `path` | same | same |
| Documents on confirmed orders | | yes | yes | only with `sale.always_include_selected_documents` | same |
| Template tab | Website Description | PDF Quote Builder | Quote Builder | same | same |
| Menu: templates | Sales ‣ Configuration ‣ Sales Orders ‣ Quotation Templates | same | same | same | Sales ‣ Configuration ‣ Sales Orders ‣ Templates |

The same from 18.0: Sales ‣ Configuration ‣ Sales Orders ‣ Headers/Footers.

## Verify

```python
print(order.sale_order_template_id.name, order.quotation_document_ids.mapped('name'))
print([(l.product_id.display_name, l.product_document_ids.mapped('name')) for l in order.order_line])
content, _ = env['ir.actions.report']._render_qweb_pdf('sale.action_report_saleorder', order.ids)
from odoo.tools.pdf import PdfFileReader
import io
print(len(PdfFileReader(io.BytesIO(content), strict=False).pages))
```

This is 18.0 to 20.0; in 17.0 drop the two first lines (no document selection).

The page count equals the header, sheet and footer pages plus the quote table's pages.

## Pitfalls

- An encrypted or non-PDF file is refused on upload: export it again without protection.
- A form field named outside the mapping prints empty: map it (18.0+) or rename it in the
  PDF.
- 18.0 includes nothing by default: tick the documents on each quote (19.0+ preselects
  those with Add By Default).
- A product sheet does not appear in 17.0-19.0 when its visibility is not Inside quote.
- In 19.0+, reprinting a confirmed order drops the documents unless the system
  parameter is set.
- 16.0's Quotation Builder installs Website; its content is not in the PDF.
