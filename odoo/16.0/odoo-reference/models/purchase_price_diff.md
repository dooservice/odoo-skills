# purchase_price_diff — WMS Accounting

Depends on: purchase_stock.

## `account.move.line` (extends)


Extension points: `_get_price_diff_account`

## `product.category` (extends)

- `property_account_creditor_price_difference_categ` Many2one → `account.account` “Price Difference Account” (company_dependent)

## `product.template` (extends)

- `property_account_creditor_price_difference` Many2one → `account.account` “Price Difference Account” (company_dependent)
