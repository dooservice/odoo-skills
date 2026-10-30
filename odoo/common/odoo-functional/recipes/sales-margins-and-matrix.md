# Margins, variant grids and the product configurator

How a seller adds products with variants to an order and reads the margin of what they
sell. The product configurator picks one variant and suggests optional products; the
variant grid (`sale_product_matrix`, `purchase_product_matrix`) enters quantities for many
variants at once; `sale_margin` shows cost and margin on each quotation line; and
`product_margin` compares invoiced sales with vendor bills per product. All in Community.
Attributes and variants themselves are in `products-and-categories.md`; quotations, in
`sales-and-crm.md`.

**At a glance**

- Apps: `sale_management` (quotations), `purchase` for the purchase grid, `account` for
  product margins.
- Names that change by version: configurator and `optional_product_ids` in
  `sale_product_configurator` up to 17.0, `sale` 18.0+; line unit `product_uom` up to
  18.0, `product_uom_id` 19.0+; Variant Selection on the Sales tab and no margins setting
  (`module_sale_margin`) in 20.0; `report_grids` on purchase orders up to 19.0.
- Sections: Before you start; The standard flow (1 set the cost of each variant, 2 choose
  how the product is added to quotations, 3 add optional products, 4 sell one variant with
  the configurator, 5 sell many variants with the grid, 6 read the margin of the
  quotation, 7 analyse margins of sales, 8 compare invoiced sales with vendor bills per
  product); Variations; Versions; Verify; Pitfalls.

## Before you start


| Module | What it adds | Versions |
|---|---|---|
| `sale_product_configurator` | the configurator dialog and optional products | 16.0-17.0 (installed with `sale`); part of `sale` from 18.0 |
| `sale_product_matrix` | grid entry on quotations | all |
| `purchase_product_matrix` | grid entry on RFQs | all |
| `product_matrix` | the grid engine both use; installed with them | all |
| `sale_margin` | `purchase_price` (Cost), `margin`, `margin_percent` on lines and orders | all; installed with `sale_management` in 20.0 |
| `product_margin` | Product Margins report from invoices and bills | all |

- Settings, in Sales ‣ Configuration ‣ Settings unless said:

| Setting | Field | Versions |
|---|---|---|
| Variants | `group_product_variant` | all |
| Variant Grid Entry (sales) | `module_sale_product_matrix` | all; needs Variants |
| Variant Grid Entry (purchase), in Purchase ‣ Configuration ‣ Settings | `module_purchase_product_matrix` | all; turns Variants on |
| Margins | `module_sale_margin` | 16.0-19.0; none in 20.0 |
| Margin Analysis, in Invoicing ‣ Configuration ‣ Settings | `module_product_margin` | all |

```python
env['res.config.settings'].create({
    'group_product_variant': True,
    'module_sale_product_matrix': True,
}).execute()
env.cr.commit()
```

  This is 20.0, where `sale_margin` installs itself. In 16.0 to 19.0 also write
  `'module_sale_margin': True`.

  A `module_*` field installs the module and reloads the registry: open a new shell after
  it.

- Read first:

```python
mods = env['ir.module.module'].search([('name', 'in', ['sale_product_configurator', 'sale_product_matrix',
    'purchase_product_matrix', 'sale_margin', 'sale_stock_margin', 'product_margin'])])
print(mods.mapped(lambda m: (m.name, m.state)))
tmpl = env['product.template'].search([('name', '=', 'Product A')], limit=1)
print(tmpl.has_configurable_attributes, tmpl.product_variant_count, tmpl.optional_product_ids.mapped('name'))
print(tmpl.attribute_line_ids.mapped(lambda l: (l.attribute_id.name, l.attribute_id.create_variant, l.value_ids.mapped('name'))))
print(tmpl.product_add_mode)
print(tmpl.product_variant_ids.mapped(lambda p: (p.display_name, p.standard_price)))
```

  `product_add_mode` exists only with `sale_product_matrix` installed: drop that line
  otherwise.

## The standard flow

A configurable product (`Product A`, attributes Color and Size) is sold with the
configurator or the grid; the quotation shows the margin; the period's product margins
are read from the invoices.

1. **Set the cost of each variant.** Sales ‣ Products ‣ Products ‣ the product, field Cost
   (on each variant when they differ: the Variants smart button).

   ```python
   for variant in tmpl.product_variant_ids:
       variant.standard_price = 40.0
   env.cr.commit()
   ```

   Leaves `standard_price` set; it is per company (`with_company`). The line's Cost takes
   it when the product is chosen, converted to the line's unit and currency.

2. **Choose how the product is added to quotations.** The product form: 16.0 to 19.0, tab
   Attributes & Variants, Sales Variant Selection; 20.0, tab Sales, field Variant
   Selection. Shown only when the product has configurable attributes.

   ```python
   tmpl.product_add_mode = 'matrix'   # or 'configurator' (default)
   env.cr.commit()
   ```

   Leaves the product opening the grid (`matrix`) or the configurator (`configurator`)
   when a seller picks it on a quotation. The field comes with `sale_product_matrix`;
   without it every configurable product opens the configurator.

3. **Add optional products.** The product form, tab Sales, Upsell & Cross-Sell, Optional
   Products.

   ```python
   tmpl.optional_product_ids = [(6, 0, (accessory_a | accessory_b).ids)]   # product.template records
   env.cr.commit()
   ```

   Leaves the products the configurator proposes after the main one (and the eCommerce
   proposes on Add to Cart). A product with optional products opens the configurator even
   without configurable attributes.

4. **Sell one variant with the configurator.** Sales ‣ Orders ‣ Quotations ‣ the
   quotation ‣ Add a product ‣ `Product A`: the dialog asks one value per attribute, the
   quantity, and lists the optional products; Confirm adds one line per product chosen.

   ```python
   ptavs = tmpl.attribute_line_ids.product_template_value_ids
   combination = ptavs.filtered(lambda v: v.name in ('Blue', 'L'))
   variant = tmpl._create_product_variant(combination)
   no_variant = combination - combination._without_no_variant_attributes()
   order.write({'order_line': [(0, 0, {
       'product_id': variant.id, 'product_uom_qty': 2,
       'product_no_variant_attribute_value_ids': [(6, 0, no_variant.ids)],
   })]})
   env.cr.commit()
   ```

   Leaves a quotation line for the variant. `_create_product_variant` returns the
   existing variant, or creates it for `dynamic` attributes. Values of `no_variant`
   attributes go on the line, not the product; a custom value (`is_custom` on the
   attribute value) is a `product_custom_attribute_value_ids` line:
   `(0, 0, {'custom_product_template_attribute_value_id': ptav.id, 'custom_value': 'Engraving'})`.

5. **Sell many variants with the grid.** The same quotation ‣ Add a product ‣ a product
   whose Variant Selection is the grid: a table opens with the first attribute's values as
   columns and the combinations of the others as rows; type a quantity per cell, Confirm.

   ```python
   cells = {('Blue', 'S'): 10, ('Blue', 'M'): 15, ('Red', 'M'): 5}
   lines = []
   for names, qty in cells.items():
       combination = ptavs.filtered(lambda v: v.name in names)
       product = tmpl._create_product_variant(combination)
       lines.append((0, 0, {'product_id': product.id, 'product_uom_qty': qty}))
   order.write({'order_line': lines})
   env.cr.commit()
   ```

   Leaves one line per cell with a quantity, as `_apply_grid` does. Reopening the grid
   shows the order's quantities; a cell set to 0 removes its line while the quotation is
   `draft` or `sent`, and sets the quantity to 0 once it is confirmed. A grid with a
   variant on two lines raises an error: merge the lines first.

6. **Read the margin of the quotation.** The quotation form: Margin and its percentage
   under the totals; on the lines, the optional columns Cost, Margin and Margin (%).

   ```python
   for line in order.order_line:
       print(line.product_id.display_name, line.price_subtotal, line.purchase_price, line.margin, line.margin_percent)
   print(order.amount_untaxed, order.margin, order.margin_percent)
   ```

   `margin` is the untaxed subtotal minus Cost times quantity; `margin_percent` is a
   ratio (0.25 is 25 %). Cost is editable on the line; the margin follows. 20.0 also lets
   the seller type the Margin or Margin (%) and recomputes the unit price from it.

7. **Analyse margins of sales.** Sales ‣ Reporting (16.0) or Sales ‣ Reporting ‣ Sales
   (17.0+), measure Margin.

   ```python
   totals = {}
   for r in env['sale.report'].search([('state', 'in', ('sale', 'done'))]):
       sold, margin = totals.get(r.product_id.display_name, (0.0, 0.0))
       totals[r.product_id.display_name] = (sold + r.price_subtotal, margin + r.margin)
   print(totals)
   ```

   Read-only. It reflects the Cost stored on each order line, not the cost at delivery
   unless `sale_stock_margin` updated it (see Variations).

8. **Compare invoiced sales with vendor bills per product.** Invoicing ‣ Reporting ‣
   Management ‣ Product Margins: dates and Invoice State (`paid`, `open_paid`,
   `draft_open_paid`), then Open Margins.

   ```python
   wizard = env['product.margin'].create({'from_date': '2026-01-01', 'to_date': '2026-12-31', 'invoice_state': 'open_paid'})
   ctx = wizard.action_open_window()['context']
   for p in env['product.product'].with_context(ctx).search([('sale_ok', '=', True)]):
       print(p.display_name, p.sale_num_invoiced, p.turnover, p.purchase_num_invoiced, p.total_cost, p.total_margin, p.total_margin_rate)
   ```

   Read-only. `turnover` comes from posted customer invoices and refunds, `total_cost`
   from vendor bills of the same period, `expected_margin` from the sales price and Cost.
   It reads the current company only.

## Variations

- **Grid on purchase orders.** With `purchase_product_matrix`, every product with
  configurable attributes opens the grid on an RFQ (Purchase ‣ Orders ‣ Requests for
  Quotation ‣ Add a product); there is no per-product choice. The grid shows no extra
  prices. Through the ORM, write one `purchase.order.line` per variant as in step 5.
- **Print the grid.** The order's `report_grids` (Print Variant Grids, default on; field
  visible in developer mode) prints products added by grid as a table on the quotation
  and RFQ PDF. 20.0 has it on sales orders only.
- **Cost from deliveries.** `sale_stock_margin` (installed with `sale_stock` and
  `sale_margin`) replaces the line Cost with the valued cost of the delivered moves for
  products whose category costing is FIFO or average; with standard cost it keeps the
  product Cost.
- **Target a margin (16.0-19.0).** Set the unit price from the cost:
  `line.price_unit = line.purchase_price / (1 - 0.30)` for a 30 % margin before discount.
- **Forecast margins (20.0).** `sale_margin.action_order_report_projected_margins`
  (Forecast Margins) lists sold, delivered and invoiced amounts against cost; its menu
  comes with `sale_project_margin` under Project.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Configurator and `optional_product_ids` in | `sale_product_configurator` | `sale_product_configurator` | `sale` | `sale` | `sale` |
| `sale_product_matrix` depends on | `sale_product_configurator` | same | `sale` | `sale` | `sale` |
| Where Variant Selection is | Attributes & Variants tab | same | same | same | Sales tab, field Variant Selection |
| `product_add_mode` values | `configurator`, `matrix` | same | same | same | same (labels Configurator, Matrix) |
| Margins setting | `module_sale_margin` | same | same | same | none, installed with `sale_management` |
| Line unit field | `product_uom` | `product_uom` | `product_uom` | `product_uom_id` | `product_uom_id` |
| Margin editable on the line | no | no | no | no | yes, recomputes `price_unit` |
| `report_grids` on purchase orders | yes | yes | yes | yes | no |
| Menu: attributes | Sales ‣ Configuration ‣ Products ‣ Attributes | same | same | same | Sales ‣ Products ‣ Attributes |
| Menu: sales analysis | Sales ‣ Reporting | Sales ‣ Reporting ‣ Sales | same | same | same |

The same in every version: Invoicing ‣ Reporting ‣ Management ‣ Product Margins,
Purchase ‣ Configuration ‣ Settings, Sales ‣ Configuration ‣ Settings.

## Verify

```python
print(order.order_line.mapped(lambda l: (l.product_id.display_name, l.product_uom_qty, l.purchase_price, l.margin)))
print(order.margin, order.margin_percent, order.amount_untaxed)
print(sorted(order.order_line.product_id.mapped('display_name')))
```

One line per variant chosen, with the expected quantities; Cost equals the variant's
`standard_price` (or the delivered cost with `sale_stock_margin`); the order margin is the
sum of the line margins.

## Pitfalls

- A Cost of 0 shows a 100 % margin. Fill `standard_price` before reading margins, and
  recompute old lines by editing the line Cost; changing the product cost does not
  update existing lines.
- `margin_percent` is a ratio, not a percentage: 0.3 means 30 %.
- Product Margins counts vendor bills of the period, not the cost of what was sold:
  products bought in another period, manufactured or taken from stock show a wrong
  margin. Use the sales analysis (step 7) for the margin on cost.
- Product Margins only reads `env.company`: run it per company.
- The grid needs at least one attribute with two values or a `dynamic` attribute;
  otherwise the product is added directly.
- Turning Variants off (`group_product_variant`) in the settings also clears Variant
  Grid Entry, and saving uninstalls `sale_product_matrix` and `purchase_product_matrix`.
- A variant on two lines of the same order blocks the grid for that product.
