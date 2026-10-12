# Inventory: warehouses, locations and stock products

```python
warehouse = env['stock.warehouse'].create({'name': 'North', 'code': 'NORTH', 'company_id': company.id})
```

- A warehouse brings its stock, input and output locations, picking types and routes.
- More than one location per warehouse needs the setting `group_stock_multi_locations`.
- Products whose stock is counted: `detailed_type='product'` in 16.0 and 17.0;
  `type='consu'` with `is_storable=True` from 18.0 on.
- Reordering: `stock.warehouse.orderpoint` per product and location, with `product_min_qty`
  and `product_max_qty`.
- Initial quantities: an inventory adjustment (`stock.quant` with `inventory_quantity`,
  then `action_apply_inventory()`), never a direct write of `quantity`.
