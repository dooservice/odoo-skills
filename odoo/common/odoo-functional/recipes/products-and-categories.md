# Products and categories

A product is a `product.template` with one or more variants (`product.product`). Its
type decides whether stock is tracked; its category gives the default income, expense
and stock valuation accounts; its unit of measure decides how quantities convert. The
type field and the unit of measure model both changed between versions: read them first.

```python
template = env['product.template'].search([('default_code', '=', 'CHAIR-01')])
print(template.read(['name', 'type', 'categ_id', 'uom_id', 'list_price', 'standard_price', 'active']))
print(template.product_variant_ids.mapped('display_name'))
print(env['account.move.line'].search_count([('product_id', 'in', template.product_variant_ids.ids)]))
```

## Product type

- **16.0, 17.0**: write `detailed_type`; `type` is computed from it. Values `consu`
  (consumable), `service`, and `product` (storable, added by `stock`). In 17.0 Point of
  Sale adds `combo`.
- **18.0+**: `type` is `consu` (Goods), `service` or `combo`. Stock tracking is the
  boolean `is_storable` on a `consu` product. It comes from `stock` in 18.0 and 19.0 and
  from `product` in 20.0, where `stock` also shows it as `store_by` (`untracked`,
  `quantity`, `lot`, `serial`).

```python
# 16.0 / 17.0
template.write({'detailed_type': 'product'})
# 18.0+
template.write({'type': 'consu', 'is_storable': True})
env.cr.commit()
```

- Combos (18.0+): a `product.combo` holds `combo_item_ids` (`product.combo.item`:
  `product_id`, `extra_price`); the product of type `combo` lists them in `combo_ids`.
- Changing a type on a product with stock moves or posted entries changes valuation and
  reports. Ask first.

## Variants and attributes

Turn on `group_product_variant` (Settings, see SKILL.md). Attributes are `product.attribute`
with values `product.attribute.value`; a template gets them through `attribute_line_ids`.

```python
size = env['product.attribute'].create({'name': 'Size', 'create_variant': 'always',
    'value_ids': [(0, 0, {'name': n}) for n in ('S', 'M', 'L')]})
template.write({'attribute_line_ids': [(0, 0, {'attribute_id': size.id, 'value_ids': [(6, 0, size.value_ids.ids)]})]})
env.cr.commit()
```

- `create_variant`: `always` (all variants created now), `dynamic` (created when sold),
  `no_variant` (never a variant, only an option on the line). It cannot change once the
  attribute is used on a product.
- Extra price per value: `price_extra` on `product.template.attribute.value`; 17.0+
  also has `default_extra_price` on the attribute value.
- Removing a value from a template archives the variants that have history instead of
  deleting them.

## Units of measure

Turn on `group_uom` to show units. The product has `uom_id` (sales and stock).

- **16.0 to 18.0**: units belong to a `uom.category`; conversion only within a category.
  Each unit has `uom_type` (`reference`, `bigger`, `smaller`), `factor` and `rounding`.
  Products also have `uom_po_id` (purchase unit, same category). Packagings are
  `product.packaging` (setting `group_stock_packaging`).
- **19.0+**: no categories. A unit points to a `relative_uom_id` with `relative_factor`
  (Dozens = 12 × Units); `factor` is computed. Rounding comes from the decimal precision
  "Product Unit". `uom_po_id` and `product.packaging` are gone: extra units on the
  product (`uom_ids`, "Packagings") replace them, and vendor prices carry their own unit.

```python
units = env.ref('uom.product_uom_unit')
# 19.0+
env['uom.uom'].create({'name': 'Box of 24', 'relative_factor': 24, 'relative_uom_id': units.id})
# 16.0-18.0
env['uom.uom'].create({'name': 'Box of 24', 'category_id': units.category_id.id, 'uom_type': 'bigger', 'factor_inv': 24, 'rounding': 1})
env.cr.commit()
```

- Never change the factor of a unit already used: past quantities are reread with it.

## Categories and their accounts

`product.category` (`name`, `parent_id`). Accounts are company-dependent: write them
with `with_company()`.

```python
categ = env['product.category'].create({'name': 'Furniture'})
categ.with_company(company).write({
    'property_account_income_categ_id': income.id,
    'property_account_expense_categ_id': expense.id,
})
env.cr.commit()
```

- Invoice lines take the product's `property_account_income_id` /
  `property_account_expense_id`, else the category's. From 17.0 the parent categories
  are also searched; from 19.0 the company's `income_account_id` / `expense_account_id`
  is the last fallback.
- Default category: `product.product_category_all` in 16.0 to 18.0, required on the
  product. In 19.0+ `categ_id` is optional; data gives `product.product_category_goods`,
  `..._services` and `..._expenses`.
- Valuation on the category: `property_cost_method` (`standard`, `fifo`, `average`),
  `property_valuation`, `property_stock_valuation_account_id`, `property_stock_journal`.
  Defined by `stock_account` up to 19.0, by `account` in 20.0 (`fifo` still from
  `stock_account`).
  - 16.0 to 18.0: `property_valuation` is `manual_periodic` or `real_time`; also
    `property_stock_account_input_categ_id` / `..._output_categ_id`. In 17.0 and 18.0
    the category form shows `property_valuation` only with `group_stock_accounting_automatic`.
  - 19.0+: `property_valuation` is `periodic` or `real_time`; input and output accounts
    are gone, `property_price_difference_account_id` is added, and the company holds
    defaults (`inventory_valuation`, `cost_method`) that the category overrides.
- Changing cost method or valuation on a category with stock revalues it and posts
  entries. Accounting must agree: ask first.

## Barcodes and references

`barcode` is on the variant (the template shows it when there is one variant). It must
be unique across products and packagings: in the whole database in 16.0, per company
from 17.0. `default_code` is the internal reference, not unique.

## Archive, do not delete

Sales order lines and journal items point to the variant with `ondelete='restrict'`, so
a product that was sold or invoiced cannot be deleted. Archive it: `template.write({'active': False})`
also archives its variants. Prefer archiving even when deletion would pass.
