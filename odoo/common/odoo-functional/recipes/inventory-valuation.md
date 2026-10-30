# Inventory valuation, landed costs and manufacturing costs

`stock_account` puts a value on stock: the product category decides the costing method
(standard price, average cost or FIFO) and whether the accounts follow the stock
(perpetual, "Automated" up to 18.0) or are adjusted at closing (periodic, "Manual" up to
18.0). `stock_landed_costs` adds freight, customs and insurance to the cost of the goods
received; `mrp_account` values manufacturing orders and computes a product's cost from
its bill of materials; `purchase_price_diff` (16.0; in `purchase_stock` 17.0, 18.0; in
`stock_account` from 19.0, and in `account` from 20.0) books the difference between a
standard price and the vendor bill. 19.0 rebuilt valuation: no more valuation layers, the
value is read from the moves, and periodic valuation is closed by a stock closing entry.
The inventory valuation report of the Accounting app and its closing button are
Enterprise and left out. Which method the law allows and the accounts are decided by the
country's localization: it is not covered here, so check it with the user.
Stock moves themselves are in `inventory.md`, purchases in `purchase.md`, manufacturing
in `manufacturing.md`.

**At a glance**

- Apps: `stock`, `account` (`stock_account`); `stock_landed_costs`; `mrp_account`.
- Names that change by version: `property_valuation` `manual_periodic`, `real_time`
  (16.0-18.0), `periodic`, `real_time` (19.0+); `stock.valuation.layer` (16.0-18.0),
  `value` on moves and `product.value` (19.0+); `action_close_stock_valuation` (19.0+);
  price difference in `purchase_price_diff` (16.0), `purchase_stock` (17.0, 18.0),
  `stock_account` (19.0), `account` (20.0); `mrp.account.wip.accounting` (18.0+).
- Sections: Before you start; The standard flow (1 costing method and valuation, 2 stock
  accounts, 3 receive and deliver, 4 read the valuation, 5 close the period; landed
  costs: 1 cost products, 2 vendor bill of the cost, 3 compute and validate;
  manufacturing costs: 1 cost from the BoM, 2 close orders, 3 book work in progress);
  Variations; Versions; Verify; Pitfalls.

## Before you start

- Apps: `stock` and `account` (they install `stock_account`); `stock_landed_costs` by
  the setting below; `mrp_account` comes with `mrp`. Installing needs the user's yes.
- Settings (Inventory ‣ Configuration ‣ Settings ‣ Valuation):

```python
env['res.config.settings'].create({'module_stock_landed_costs': True}).execute()
env.cr.commit()
```

- `group_lot_on_invoice` (same block) prints lots on invoices; after the install,
  `lc_journal_id` is the default landed costs journal.
- 17.0 and 18.0 hide the category's valuation field from users without
  `stock_account.group_stock_accounting_automatic`, a setting with no checkbox in
  Community: `env['res.config.settings'].create({'group_stock_accounting_automatic': True}).execute()`.
- Read first:

```python
categ = product.categ_id
print(categ.read(['property_cost_method', 'property_valuation', 'property_stock_valuation_account_id', 'property_stock_journal', 'property_price_difference_account_id']))
print(env.company.read(['cost_method', 'inventory_valuation', 'account_stock_journal_id', 'account_stock_valuation_id']))
print(product.read(['standard_price', 'qty_available', 'avg_cost', 'total_value']))
```

This is 19.0 and 20.0. Up to 18.0 the company has no valuation fields and the category
has `property_stock_account_input_categ_id` and `property_stock_account_output_categ_id`
instead of the price difference account:

```python
print(categ.read(['property_cost_method', 'property_valuation', 'property_stock_valuation_account_id', 'property_stock_journal', 'property_stock_account_input_categ_id', 'property_stock_account_output_categ_id']))
print(product.read(['standard_price', 'qty_available', 'value_svl', 'quantity_svl']))
```

## The standard flow

1. **Choose the costing method and the valuation per category.** Inventory ‣
   Configuration ‣ Products ‣ Product Categories (Categories in 19.0+) ‣ the category ‣
   Inventory Valuation.

   ```python
   categ.write({'property_cost_method': 'average', 'property_valuation': 'real_time'})
   env.cr.commit()
   ```

   This is 19.0 and 20.0: `property_valuation` `periodic` ("Periodic (at closing)") or
   `real_time` ("Perpetual (at invoicing)"). Up to 18.0 the values are `manual_periodic`
   ("Manual") and `real_time` ("Automated"). `property_cost_method`: `standard`,
   `average`, `fifo`. Both are company dependent. From 19.0 a category without method
   takes the company's `cost_method`. Changing the method of a category with stock
   revalues it (up to 18.0 with a valuation entry); ask first.

2. **Set the stock accounts.** The same form ‣ Account Properties (perpetual only).

   ```python
   categ.write({'property_stock_valuation_account_id': stock_account.id})
   env.cr.commit()
   ```

   This is 19.0 and 20.0: the stock account carries its variation account
   (`account_stock_variation_id`), and the stock journal is the company's
   `account_stock_journal_id`. Up to 18.0 write also `property_stock_journal`,
   `property_stock_account_input_categ_id` and `property_stock_account_output_categ_id`
   (required with `real_time`). The chart of accounts of the localization fills them by
   default.

3. **Receive and deliver as usual.** Each validated transfer of a valued product gets a
   value (`inventory.md`).

   - Up to 18.0 each move writes a valuation layer (`stock.valuation.layer`) and, with
     `real_time`, a journal entry in the stock journal at validation.
   - From 19.0 the move carries its `value`; with `real_time` the accounting is done at
     invoicing (bill and invoice lines use the stock accounts), and the difference
     between stock and accounts is posted by the stock closing entry.

4. **Read the valuation.** Up to 18.0: Inventory ‣ Reporting ‣ Valuation (developer mode
   in 16.0), grouped by product. From 19.0: the product form's valuation button, and
   Inventory ‣ Reporting ‣ Stock with the Value column.

   ```python
   print(env['stock.quant'].search_read([('product_id', '=', product.id), ('location_id.usage', '=', 'internal')], ['quantity', 'value']))
   ```

5. **Close the period** (19.0+, periodic or to align accounts). The company's stock
   closing entry: `res.company.action_close_stock_valuation`, in the company's
   `account_stock_journal_id` with `account_stock_valuation_id`.

   ```python
   action = env.company.action_close_stock_valuation()
   closing = env['account.move'].browse(action['res_id'])
   print(closing.line_ids.read(['account_id', 'debit', 'credit']))
   env.cr.commit()
   ```

   Leaves a draft "Stock Closing" entry to review and post with the accountant;
   "Everything is correctly closed" means nothing to book. The report that shows it is
   Enterprise. Up to 18.0 periodic valuation posts nothing: the accountant books the
   stock variation by hand.

### Landed costs

1. **Create the cost products.** Inventory ‣ Products ‣ Products ‣ New: a service with
   Is a Landed Cost (`landed_cost_ok`) and the split method.

   ```python
   freight = env['product.product'].create({'name': 'Freight', 'type': 'service', 'landed_cost_ok': True, 'split_method_landed_cost': 'by_quantity'})
   env.cr.commit()
   ```

   `split_method_landed_cost`: `equal`, `by_quantity`, `by_current_cost_price`,
   `by_weight`, `by_volume`.

2. **Record the vendor bill of the cost.** The bill line with the cost product is a
   landed cost line (`is_landed_costs_line`); post it, then the bill ‣ Create Landed
   Costs (`button_create_landed_costs`). Or Inventory ‣ Operations ‣ Landed Costs ‣ New
   (Inventory ‣ Operations ‣ Adjustments ‣ Landed Costs from 17.0).

   ```python
   lc = env['stock.landed.cost'].create({
       'picking_ids': [(6, 0, receipt.ids)],
       'cost_lines': [(0, 0, {'product_id': freight.id, 'name': 'Freight', 'price_unit': 120, 'split_method': 'by_quantity'})],
   })
   env.cr.commit()
   ```

   Leaves a draft landed cost on the receipt (`target_model` `picking`; `mrp_landed_costs`
   adds manufacturing orders).

3. **Compute and validate.** The landed cost ‣ Compute, check the Valuation Adjustments,
   then Validate.

   ```python
   lc.compute_landed_cost()
   lc.button_validate()
   env.cr.commit()
   ```

   Leaves it `done` ("Posted"): the cost spread on the received products and, with
   perpetual valuation, a journal entry in `account_journal_id`. Up to 19.0 only
   products in `average` or `fifo` categories take landed costs; in 20.0 every valued
   product. Validating is an accounting change: only with the user's yes.

### Manufacturing costs (`mrp_account`)

1. **Compute the cost from the bill of materials.** The product ‣ Compute Price from BoM
   (`button_bom_cost`; for several, the list ‣ Actions ‣ Compute Price from BoM), for
   `standard` products: components plus operations at the work centers' cost per hour.

   ```python
   product.button_bom_cost()
   env.cr.commit()
   ```

   Leaves `standard_price` updated. Hidden for FIFO products with perpetual valuation.

2. **Close manufacturing orders.** Marking an order done values the finished product
   from the components consumed and the time spent (average and FIFO), plus
   `extra_cost` per unit (and the bill of materials' `extra_cost` in 20.0).

3. **Book work in progress** (18.0+). Manufacturing ‣ Operations ‣ Manufacturing Orders,
   select the orders in progress ‣ Actions ‣ Post WIP Accounting Entry
   (`mrp.account.wip.accounting`): a dated entry, reversed on `reversal_date`.

## Variations

- **Revalue stock by hand** (up to 18.0): Inventory ‣ Reporting ‣ Valuation, the
  product's group ‣ + (Add Manual Valuation, `stock.valuation.layer.revaluation`):
  `added_value`, `account_id`, `account_journal_id`, `reason`, then Validate
  (`action_validate_revaluation`). Average and FIFO products with stock only. From
  19.0 adjustments are `product.value` records (20.0: Inventory ‣ Reporting ‣ Valuation
  Adjustments, developer mode).
- **Value per lot** (18.0+): the product's `lot_valuated` values each lot or serial
  number on its own cost.
- **Price difference account**: with `standard` and perpetual valuation, the difference
  between the bill price and the standard price goes to the category's price difference
  account: `property_account_creditor_price_difference_categ` (16.0 to 18.0; 16.0 needs
  `purchase_price_diff`), `property_price_difference_account_id` (19.0+).
- **Analytic on manufacturing**: a work center's analytic distribution writes analytic
  items for the time spent; up to 17.0 the order (`analytic_account_id` in 16.0,
  `analytic_distribution` in 17.0) and the bill of materials carry one too.

## Versions

| | 16.0 | 17.0 | 18.0 | 19.0 | 20.0 |
|---|---|---|---|---|---|
| `property_valuation` | `manual_periodic`, `real_time` | same, field behind `group_stock_accounting_automatic` | same | `periodic`, `real_time` | same, field in `account` |
| Valuation storage | `stock.valuation.layer` | same | same | `value` on moves, `product.value` | same |
| Company valuation fields | no | no | no | `cost_method`, `inventory_valuation`, `account_stock_journal_id`, `account_stock_valuation_id` | same, in `account` |
| Stock closing entry | no | no | no | `action_close_stock_valuation` | same |
| Landed costs on standard products | no | no | no | no | yes |
| Price difference account | `purchase_price_diff` | `purchase_stock` | same | `stock_account` | `account` |
| WIP entry | no | no | `mrp.account.wip.accounting` | same | same |
| Menu: valuation | Inventory ‣ Reporting ‣ Valuation (developer mode) | Inventory ‣ Reporting ‣ Valuation | same | none | Inventory ‣ Reporting ‣ Valuation Adjustments (developer mode) |
| Menu: landed costs | Inventory ‣ Operations ‣ Landed Costs | Inventory ‣ Operations ‣ Adjustments ‣ Landed Costs | same | same | same |

The same in every version: Inventory ‣ Configuration ‣ Settings ‣ Valuation; the
product's Compute Price from BoM; the vendor bill's Create Landed Costs.

## Verify

```python
print(lc.read(['state', 'amount_total', 'account_move_id']))
print(lc.valuation_adjustment_lines.read(['product_id', 'former_cost', 'additional_landed_cost', 'final_cost']))
print(product.read(['standard_price', 'avg_cost', 'total_value']))
```

The landed cost is `done`, the adjustments add up to its total, and the product's cost
rose. Up to 18.0 read `value_svl` instead of `total_value` and `avg_cost`.

## Pitfalls

- Changing a category from periodic to perpetual (or the method) with stock on hand
  books or revalues all of it at once: do it at a period start, with the accountant.
- Landed costs on goods already sold only raise the cost of what is left; the rest
  goes to the cost of goods sold. Validate them soon after the receipt.
- A landed cost on products in `standard` (up to 19.0) finds no lines to adjust and
  refuses to validate.
- Compute Price from BoM overwrites `standard_price`: products valued at standard get
  revalued.
- Stock closing entries are dated: closing an earlier date than an existing closing is
  refused; cancel the later ones first.
