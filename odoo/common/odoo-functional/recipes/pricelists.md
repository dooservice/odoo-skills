# Pricelists

A `product.pricelist` gives prices different from the product's sales price: per
customer, country, quantity or period. Its rules (`product.pricelist.item`) are read in
the order `applied_on, min_quantity desc, categ_id desc, id desc`: the most specific rule
that matches the product, quantity and date wins; a product no rule matches keeps its
sales price. A pricelist has one currency, so prices in two currencies need two
pricelists. This recipe covers sales pricelists in Community; vendor prices are in
`purchase.md`.

## Before you start

- Apps: `product` (the models), `sale` for the menus and for using them on quotations.
- Settings: `group_product_pricelist` (Sales ‣ Configuration ‣ Settings, Pricelists).

```python
env['res.config.settings'].create({'group_product_pricelist': True}).execute()
env.cr.commit()
```

- 16.0, 17.0: discounts and formulas also need the "advanced" method. Settings
  onchanges do not run from a script, so set the group with it:
  `{'group_product_pricelist': True, 'product_pricelist_setting': 'advanced', 'group_sale_pricelist': True}`.
- 18.0 on: `product_pricelist_setting` and `group_sale_pricelist` are gone; every rule
  type is available.
- 17.0 on: turning the setting on creates a default pricelist per company; turning it
  off archives every pricelist: never turn it off without the user's yes.
- Read first:

```python
env['product.pricelist'].search_read([], ['name', 'currency_id', 'company_id', 'country_group_ids', 'sequence'])
pricelist = env['product.pricelist'].search([('name', '=', 'Wholesale')], limit=1)
if pricelist:
    print(pricelist.item_ids.read(['applied_on', 'product_tmpl_id', 'categ_id', 'min_quantity', 'compute_price', 'fixed_price', 'price_discount', 'date_start', 'date_end']))
    print(pricelist._get_product_price(product, 12.0))
```

`_get_product_price(product, quantity)` returns the price that pricelist gives: check it
before and after a change.

## The standard flow

The order of Odoo's Pricelists documentation: create the pricelist, add its rules, give
it to customers; quotations then take it.

1. **Create the pricelist.** Sales ‣ Products ‣ Pricelists ‣ New: name, currency,
   company (empty shares it with every company) and country groups.

   ```python
   pricelist = env['product.pricelist'].create({'name': 'Wholesale', 'currency_id': company.currency_id.id, 'company_id': company.id})
   env.cr.commit()
   ```

   Leaves an active pricelist without rules: it gives the sales price.

2. **Add its rules.** The pricelist form, Price Rules tab (Sales Prices in 19.0, Rules in
   20.0) ‣ Add a line.

   ```python
   env['product.pricelist.item'].create([
       {'pricelist_id': pricelist.id, 'applied_on': '3_global', 'compute_price': 'percentage', 'percent_price': 10, 'min_quantity': 12},
       {'pricelist_id': pricelist.id, 'applied_on': '1_product', 'product_tmpl_id': template.id, 'compute_price': 'fixed', 'fixed_price': 8.5},
   ])
   env.cr.commit()
   ```

   That is 16.0 to 19.0. The same 10% off in 20.0:
   `{'pricelist_id': pricelist.id, 'compute_price': 'discount', 'price_discount': 10, 'min_quantity': 12}`.
   Leaves rules that `_get_product_price` and new quotation lines apply.

   - `applied_on`: `3_global`, `2_product_category`, `1_product`, `0_product_variant`;
     computed in 20.0 from `categ_id`, `product_tmpl_id` and `product_id`.
   - Formula rules (`formula` up to 19.0, `discount`/`markup` in 20.0) start from
     `base`: `list_price` (sales price), `standard_price` (cost) or `pricelist` (with
     `base_pricelist_id`), then apply `price_discount`, `price_round`,
     `price_surcharge`, `price_min_margin`, `price_max_margin`.
   - `date_start` / `date_end` limit a rule to a promotion period.
   - From 19.0 `pricelist_id` is not required on a rule, but standard flows only use
     rules that belong to a pricelist: always set it.

3. **Give it to customers.** The customer's form (Sales ‣ Orders ‣ Customers), Sales &
   Purchase tab, Pricelist.

   ```python
   partner.with_company(company).write({'property_product_pricelist': pricelist.id})
   env.cr.commit()
   ```

   Leaves the pricelist that new quotations of that company take for the customer.

   - The value is per company. Without one, the partner gets the first pricelist (by
     `sequence`) whose `country_group_ids` contain the partner's country, else the first
     pricelist without country groups: order `sequence` with that in mind.

## Variations

- **Showing the discount.** Whether the customer sees "100, 10% off" or just "90":
  - 16.0, 17.0: `discount_policy` on the pricelist, `with_discount` (price already
    reduced) or `without_discount` (public price and the discount), with the setting
    `group_discount_per_so_line` (in `product`).
  - 18.0 on: `discount_policy` is gone. The discount shows on sales lines when
    `group_discount_per_so_line` (now in `sale`) is on and the rule is a plain
    percentage (`compute_price='percentage'` in 18.0, 19.0; `is_plain_discount` in
    20.0).
- **Markup on cost.** Up to 17.0 a formula on `standard_price` with a negative
  `price_discount`; 18.0 and 19.0 also `price_markup`; 20.0 `compute_price='markup'`
  with `price_markup`.
- **By country.** Country groups on the pricelist choose it for partners without one;
  `sequence` decides between several.
- **A pricelist on one quotation only.** Change the Pricelist field on the quotation
  instead of on the customer.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| Advanced rules need | `product_pricelist_setting='advanced'`, `group_sale_pricelist` | same | always on | always on | always on |
| Turning on creates a default pricelist | no | yes | yes | yes | yes |
| `compute_price` | `fixed`, `percentage`, `formula` | same | same | same | `fixed`, `discount`, `markup` |
| percentage off | `percent_price` | same | same | same | `price_discount` |
| markup on cost | formula, negative `price_discount` | same | also `price_markup` | same | `markup` with `price_markup` |
| `applied_on` | written | written | written | written | computed |
| `pricelist_id` on a rule | required | required | required | optional | optional |
| Discount shown | `discount_policy` | `discount_policy` | plain percentage + `group_discount_per_so_line` | same | `is_plain_discount` + setting |
| `group_discount_per_so_line` in | `product` | `product` | `sale` | `sale` | `sale` |
| Rules tab | Price Rules | Price Rules | Price Rules | Sales Prices | Rules |
| Customer's pricelist field | `property_product_pricelist` | same | same (stored in `specific_property_product_pricelist`) | same, empty while pricelists are off | same |

Menus are the same in every version: Sales ‣ Products ‣ Pricelists, Sales ‣ Orders ‣
Customers, Sales ‣ Configuration ‣ Settings.

## Verify

```python
print(pricelist._get_product_price(template.product_variant_id, 1.0), pricelist._get_product_price(other_product, 12.0))
order = env['sale.order'].create({'partner_id': partner.id, 'order_line': [(0, 0, {'product_id': template.product_variant_id.id, 'product_uom_qty': 1})]})
print(order.pricelist_id.name, order.order_line.price_unit)
```

The prices match the rules, and a new quotation for the customer takes the pricelist.
The quotation is a draft; delete it or let the user keep it.

## Pitfalls

- A pricelist in use on confirmed orders keeps their prices: changing a rule only
  affects new quotations and lines whose prices are recomputed. Archive rather than
  delete one that orders use.
- From 17.0, turning the setting off archives every pricelist.
- A rule written with the other version's fields (`percent_price` in 20.0,
  `compute_price='discount'` before 20.0) fails or never applies.
- Two pricelists without country groups: the one with the lowest `sequence` is everyone's
  default.
