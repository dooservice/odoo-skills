# pos_daily_sales_reports — Point of Sale Daily Sales Reports

Depends on: point_of_sale.

## `report.point_of_sale.report_saledetails` (extends)


Public methods: `get_sale_details`

Extension points: `_get_products_and_taxes_dict`, `_get_total_and_qty_per_category`

## `pos.daily.sales.reports.wizard` (defines)

Point of Sale Daily Report

- `pos_session_id` Many2one → `pos.session` (required)

Public methods: `generate_report`
