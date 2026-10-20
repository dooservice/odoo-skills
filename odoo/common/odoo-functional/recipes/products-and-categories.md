# Products and categories

A product is a `product.template` with one or more variants (`product.product`). Its
type decides whether stock is tracked; its category gives the default income, expense
and stock valuation accounts; its unit of measure decides how quantities convert. This
recipe covers categories, units of measure, product types, attributes and variants,
barcodes and archiving, all in Community. The type field and the unit of measure model
both changed between versions: read them first.

## Before you start

- Apps: `product` (always there with `sale`, `purchase` or `stock`); `stock` for storable
  products; `stock_account` for the category's valuation fields (partly `account` in
  20.0).
- Settings, in Sales ‣ Configuration ‣ Settings or Inventory ‣ Configuration ‣ Settings:
  `group_product_variant` (Variants), `group_uom` (Units of Measure; "Units of Measure &
  Packagings" in 19.0+), `group_stock_packaging` (Packagings, 16.0 to 18.0).

```python
env['res.config.settings'].create({'group_product_variant': True, 'group_uom': True}).execute()
env.cr.commit()
```

- Read first:

```python
template = env['product.template'].search([('default_code', '=', 'CHAIR-01')])
print(template.read(['name', 'type', 'categ_id', 'uom_id', 'list_price', 'standard_price', 'active']))
print(template.product_variant_ids.mapped('display_name'))
print(env['account.move.line'].search_count([('product_id', 'in', template.product_variant_ids.ids)]))
```

## The standard flow

What a product needs exists first (its category, its unit), then the product with its
type, then attributes and variants, as Odoo's documentation orders it.

1. **Create the category and its accounts.** Inventory ‣ Configuration ‣ Products ‣
   Product Categories (Categories in 19.0+; also in Invoicing and Sales, see
   `## Versions`). `product.category` has `name` and `parent_id`. Accounts are
   company-dependent: write them with `with_company()`.

   ```python
   categ = env['product.category'].create({'name': 'Furniture'})
   categ.with_company(company).write({
       'property_account_income_categ_id': income.id,
       'property_account_expense_categ_id': expense.id,
   })
   env.cr.commit()
   ```

   Leaves a category that products and invoice lines take their accounts from.

   - Invoice lines take the product's `property_account_income_id` /
     `property_account_expense_id`, else the category's. From 17.0 the parent categories
     are also searched; from 19.0 the company's `income_account_id` /
     `expense_account_id` is the last fallback.
   - Valuation on the category: `property_cost_method` (`standard`, `fifo`, `average`),
     `property_valuation`, `property_stock_valuation_account_id`,
     `property_stock_journal`. Their values and the module that defines them differ by
     version (`## Versions`).
   - Changing cost method or valuation on a category with stock revalues it and posts
     entries. Accounting must agree: ask first.

2. **Create the unit of measure, when the product needs one that does not exist.**
   Inventory ‣ Configuration ‣ Units of Measures ‣ UoM (16.0 to 18.0), Inventory ‣
   Configuration ‣ Products ‣ Units & Packagings (19.0+). Needs `group_uom`.

   ```python
   units = env.ref('uom.product_uom_unit')
   # 19.0+
   env['uom.uom'].create({'name': 'Box of 24', 'relative_factor': 24, 'relative_uom_id': units.id})
   # 16.0-18.0
   env['uom.uom'].create({'name': 'Box of 24', 'category_id': units.category_id.id, 'uom_type': 'bigger', 'factor_inv': 24, 'rounding': 1})
   env.cr.commit()
   ```

   Leaves an active unit that converts to Units.

   - 16.0 to 18.0: units belong to a `uom.category`; conversion only within a category.
     Each unit has `uom_type` (`reference`, `bigger`, `smaller`), `factor` and
     `rounding`.
   - 19.0+: no categories. A unit points to a `relative_uom_id` with `relative_factor`
     (Dozens = 12 × Units); `factor` is computed. Rounding comes from the decimal
     precision "Product Unit".
   - Never change the factor of a unit already used: past quantities are reread with it.

3. **Create the product and choose its type.** Sales ‣ Products ‣ Products ‣ New (or
   Inventory ‣ Products ‣ Products). The product has `uom_id` (sales and stock); 16.0 to
   18.0 also have `uom_po_id` (purchase unit, same category).

   ```python
   # 18.0+
   template = env['product.template'].create({
       'name': 'Office chair', 'default_code': 'CHAIR-01', 'categ_id': categ.id,
       'type': 'consu', 'is_storable': True, 'list_price': 120, 'standard_price': 70,
   })
   # 16.0 / 17.0: 'detailed_type': 'product' instead of 'type' and 'is_storable'
   env.cr.commit()
   ```

   To change the type of an existing product:

   ```python
   # 16.0 / 17.0
   template.write({'detailed_type': 'product'})
   # 18.0+
   template.write({'type': 'consu', 'is_storable': True})
   env.cr.commit()
   ```

   Leaves an active template with one variant.

   - 16.0, 17.0: write `detailed_type`; `type` is computed from it. Values `consu`
     (consumable), `service`, and `product` (storable, added by `stock`). In 17.0 Point
     of Sale adds `combo`.
   - 18.0+: `type` is `consu` (Goods), `service` or `combo`. Stock tracking is the
     boolean `is_storable` on a `consu` product. It comes from `stock` in 18.0 and 19.0
     and from `product` in 20.0, where `stock` also shows it as `store_by`
     (`untracked`, `quantity`, `lot`, `serial`).
   - Changing a type on a product with stock moves or posted entries changes valuation
     and reports. Ask first.

4. **Create the attributes and their values.** Inventory ‣ Configuration ‣ Products ‣
   Attributes (the Sales entry moved, see `## Versions`). Needs `group_product_variant`.

   ```python
   size = env['product.attribute'].create({'name': 'Size', 'create_variant': 'always',
       'value_ids': [(0, 0, {'name': n}) for n in ('S', 'M', 'L')]})
   env.cr.commit()
   ```

   Leaves a `product.attribute` with its values (`product.attribute.value`), not used by
   any product yet.

   - `create_variant`: `always` (all variants created now), `dynamic` (created when
     sold), `no_variant` (never a variant, only an option on the line). It cannot change
     once the attribute is used on a product.

5. **Add the attributes to the product.** The product form, Attributes & Variants tab.

   ```python
   template.write({'attribute_line_ids': [(0, 0, {'attribute_id': size.id, 'value_ids': [(6, 0, size.value_ids.ids)]})]})
   env.cr.commit()
   ```

   Leaves one variant per value (with `always`).

   - Extra price per value: `price_extra` on `product.template.attribute.value`; 17.0+
     also has `default_extra_price` on the attribute value.
   - Removing a value from a template archives the variants that have history instead
     of deleting them.

6. **Set barcodes and references.** On each variant: Sales ‣ Products ‣ Product Variants
   up to 19.0, the Variants smart button of the product in 20.0. The template shows them
   when it has one variant.

   ```python
   variant = template.product_variant_ids[:1]
   variant.write({'barcode': '<barcode>', 'default_code': 'CHAIR-01-S'})
   env.cr.commit()
   ```

   Leaves the variant findable by scanner and reference. `barcode` must be unique across
   products and packagings: in the whole database in 16.0, per company from 17.0.
   `default_code` is the internal reference, not unique.

## Variations

- **Combos** (18.0+; Point of Sale only in 17.0): a `product.combo` holds
  `combo_item_ids` (`product.combo.item`: `product_id`, `extra_price`); the product of
  type `combo` lists them in `combo_ids`.
- **Buying in another unit.** 16.0 to 18.0: `uom_po_id` on the product, in the same
  category; packagings are `product.packaging` (setting `group_stock_packaging`). 19.0+:
  `uom_po_id` and `product.packaging` are gone: extra units on the product (`uom_ids`,
  "Packagings") replace them, and vendor prices carry their own unit (`purchase.md`).
- **Default category.** `product.product_category_all` in 16.0 to 18.0, required on the
  product. In 19.0+ `categ_id` is optional; data gives `product.product_category_goods`,
  `..._services` and `..._expenses`.
- **Archive, do not delete.** Sales order lines and journal items point to the variant
  with `ondelete='restrict'`, so a product that was sold or invoiced cannot be deleted.
  Archive it: `template.write({'active': False})` also archives its variants. Prefer
  archiving even when deletion would pass.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Product type | `detailed_type`: `consu`, `service`, `product` | same; PoS adds `combo` | `type`: `consu`, `service`, `combo`; `is_storable` (from `stock`) | same | same; `is_storable` from `product`, `store_by` in `stock` |
| Units | `uom.category`, `uom_type`, `factor`, `rounding`; `uom_po_id` | same | same | `relative_uom_id`, `relative_factor`; no `uom_po_id`; `uom_ids` | same |
| Packagings | `product.packaging` | same | same | units on the product | same |
| Barcode unique | per database | per company | per company | per company | per company |
| `default_extra_price` on attribute value | no | yes | yes | yes | yes |
| Account fallback | product, category | product, category and parents | same | same, then company `income_account_id` / `expense_account_id` | same |
| Default category | `product_category_all`, required | same | same | optional; `_goods`, `_services`, `_expenses` | same |
| `property_valuation` | `manual_periodic`, `real_time`; `property_stock_account_input_categ_id` / `..._output_categ_id` | same; form shows it with `group_stock_accounting_automatic` | same as 17.0 | `periodic`, `real_time`; `property_price_difference_account_id`; company `inventory_valuation`, `cost_method` | same |
| Valuation fields defined by | `stock_account` | same | same | same | `account` (`fifo` still `stock_account`) |
| Menu: categories (Inventory) | Inventory ‣ Configuration ‣ Products ‣ Product Categories | same | same | Inventory ‣ Configuration ‣ Products ‣ Categories | same |
| Menu: categories (Invoicing) | Invoicing ‣ Configuration ‣ Management ‣ Product Categories | Invoicing ‣ Configuration ‣ Invoicing ‣ Product Categories | same as 17.0 | same as 16.0 | same as 16.0 |
| Menu: categories (Sales) | none | Sales ‣ Configuration ‣ Products ‣ Product Categories | same | Sales ‣ Configuration ‣ Products ‣ Categories | none |
| Menu: units (Inventory) | Inventory ‣ Configuration ‣ Units of Measures ‣ UoM | same | same | Inventory ‣ Configuration ‣ Products ‣ Units & Packagings | same |
| Menu: units (Sales) | Sales ‣ Configuration ‣ Units of Measure ‣ Units of Measure | same | same | Sales ‣ Configuration ‣ Products ‣ Units & Packagings | none |
| Menu: attributes (Sales) | Sales ‣ Configuration ‣ Products ‣ Attributes | same | same | same | Sales ‣ Products ‣ Attributes |
| Menu: variants | Sales ‣ Products ‣ Product Variants | same | same | same | Variants smart button on the product |

The same in every version: Sales ‣ Products ‣ Products, Inventory ‣ Products ‣ Products,
Inventory ‣ Configuration ‣ Products ‣ Attributes, Sales ‣ Configuration ‣ Settings.

## Verify

```python
template.invalidate_recordset()
print(template.read(['name', 'type', 'categ_id', 'uom_id', 'active']))
print([(v.display_name, v.barcode, v.default_code) for v in template.product_variant_ids])
print(template.categ_id.with_company(company).property_account_income_categ_id.display_name)
```

The type is the one asked for in the version's field, there is one variant per value,
and the category gives the expected income account for the company.

## Pitfalls

- Writing the type with the other version's field (`detailed_type` in 18.0+,
  `is_storable` in 16.0 or 17.0) fails: read the fields of the version first.
- Changing a unit's factor, or a product's type, after stock moves rereads history with
  the new value. Create a new unit or product instead, with the user's yes.
- `create_variant` is locked once the attribute is used: decide `no_variant` options
  before adding them to products.
- Category accounts are per company: a write without `with_company()` only sets them for
  the current company.
- A barcode already used on another product or packaging is refused: search it before
  writing.
- A product that was sold or invoiced cannot be deleted: archive it.
