# Pricelists

Pricelists need the setting `group_product_pricelist`. Each `product.pricelist` has rules
(`product.pricelist.item`) read in order, the first that applies wins.

```python
pricelist = env['product.pricelist'].create({'name': 'Wholesale', 'currency_id': company.currency_id.id})
env['product.pricelist.item'].create({
    'pricelist_id': pricelist.id,
    'applied_on': '3_global',
    'compute_price': 'percentage',
    'percent_price': 10,
    'min_quantity': 12,
})
```

- `applied_on`: `3_global`, `2_product_category`, `1_product`, `0_product_variant`.
- `compute_price`: `fixed`, `percentage` or `formula`.
- In 16.0 and 17.0 a pricelist also has `discount_policy` (show the discount or not);
  from 18.0 on it is gone.
- Give it to customers with `property_product_pricelist` on the partner.
