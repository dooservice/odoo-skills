# Pricelists

A `product.pricelist` gives prices different from the product's sales price: per
customer, country, quantity or period. Its rules (`product.pricelist.item`) are read in
the order `applied_on, min_quantity desc, categ_id desc, id desc`: the most specific rule
that matches the product, quantity and date wins; a product no rule matches keeps its
sales price. A pricelist has one currency, so a price list in USD and one in EUR are two
pricelists.

## Read first

```python
env['product.pricelist'].search_read([], ['name', 'currency_id', 'company_id', 'country_group_ids', 'sequence'])
pricelist = env['product.pricelist'].search([('name', '=', 'Wholesale')], limit=1)
pricelist.item_ids.read(['applied_on', 'product_tmpl_id', 'categ_id', 'min_quantity', 'compute_price', 'fixed_price', 'price_discount', 'date_start', 'date_end'])
pricelist._get_product_price(product, 12.0)
```

`_get_product_price(product, quantity)` returns the price that pricelist gives: check it
before and after a change.

## Turn pricelists on

```python
env['res.config.settings'].create({'group_product_pricelist': True}).execute()
env.cr.commit()
```

- 16.0, 17.0: discounts and formulas also need the "advanced" method. Settings onchanges
  do not run from a script, so set the group with it:
  `{'group_product_pricelist': True, 'product_pricelist_setting': 'advanced', 'group_sale_pricelist': True}`.
- 18.0 on: `product_pricelist_setting` and `group_sale_pricelist` are gone; every rule
  type is available. Turning the setting on creates a default pricelist per company;
  turning it off archives every pricelist: never turn it off without the user's yes.

## A pricelist with rules

```python
pricelist = env['product.pricelist'].create({'name': 'Wholesale', 'currency_id': company.currency_id.id, 'company_id': company.id})
env['product.pricelist.item'].create([
    {'pricelist_id': pricelist.id, 'applied_on': '3_global', 'compute_price': 'percentage', 'percent_price': 10, 'min_quantity': 12},
    {'pricelist_id': pricelist.id, 'applied_on': '1_product', 'product_tmpl_id': template.id, 'compute_price': 'fixed', 'fixed_price': 8.5},
])
env.cr.commit()
```

That is 16.0 to 19.0. The rule fields changed:

| | 16.0, 17.0 | 18.0, 19.0 | 20.0 |
|---|---|---|---|
| `compute_price` | `fixed`, `percentage`, `formula` | same | `fixed`, `discount`, `markup` |
| percentage off | `percent_price` | `percent_price` | `price_discount` |
| markup on cost | formula, negative `price_discount` | also `price_markup` | `markup` with `price_markup` |
| `applied_on` | written | written | computed from `categ_id`, `product_tmpl_id`, `product_id` |

The same 10% off in 20.0: `{'pricelist_id': pricelist.id, 'compute_price': 'discount', 'price_discount': 10, 'min_quantity': 12}`.

- `applied_on`: `3_global`, `2_product_category`, `1_product`, `0_product_variant`.
- Formula rules (`formula` up to 19.0, `discount`/`markup` in 20.0) start from `base`:
  `list_price` (sales price), `standard_price` (cost) or `pricelist` (with
  `base_pricelist_id`), then apply `price_discount`, `price_round`, `price_surcharge`,
  `price_min_margin`, `price_max_margin`.
- `date_start` / `date_end` limit a rule to a promotion period.
- From 19.0 `pricelist_id` is not required on a rule, but standard flows only use rules
  that belong to a pricelist: always set it.

## Showing the discount

Whether the customer sees "100, 10% off" or just "90":

- 16.0, 17.0: `discount_policy` on the pricelist, `with_discount` (price already
  reduced) or `without_discount` (public price and the discount), with the setting
  `group_discount_per_so_line` (in `product`).
- 18.0 on: `discount_policy` is gone. The discount shows on sales lines when
  `group_discount_per_so_line` (now in `sale`) is on and the rule is a plain percentage
  (`compute_price='percentage'` in 18.0, 19.0; `is_plain_discount` in 20.0).

## Giving it to customers

```python
partner.with_company(company).write({'property_product_pricelist': pricelist.id})
env.cr.commit()
```

- The value is per company. Without one, the partner gets the first pricelist (by
  `sequence`) whose `country_group_ids` contain the partner's country, else the first
  pricelist without country groups: order `sequence` with that in mind.
- A pricelist in use on confirmed orders keeps their prices: changing a rule only
  affects new quotations and lines whose prices are recomputed. Archive rather than
  delete one that orders use.
