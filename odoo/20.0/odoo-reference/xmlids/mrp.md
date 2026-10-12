# mrp — XML ids

## digest.tip

- `mrp.digest_tip_mrp_0`

## ir.actions.act_window

- `mrp.action_change_production_qty`
- `mrp.act_mrp_block_workcenter`
- `mrp.act_mrp_block_workcenter_wo`
- `mrp.action_mrp_production_backorder`
- `mrp.action_mrp_consumption_warning`
- `mrp.action_mrp_production_split_multi`
- `mrp.action_mrp_production_split`
- `mrp.action_assign_serial_numbers`
- `mrp.action_mrp_production_moves`
- `mrp.action_detailed_operations`
- `mrp.action_mrp_routing_time`
- `mrp.action_mrp_workorder_production_specific`
- `mrp.action_mrp_workorder_workcenter`
- `mrp.action_mrp_workorder_production`
- `mrp.mrp_workorder_mrp_production_form`
- `mrp.mrp_workorder_todo`
- `mrp.action_mrp_workcenter_load_report_graph`
- `mrp.action_work_orders`
- `mrp.mrp_workcenter_productivity_report_oee`
- `mrp.mrp_workcenter_productivity_report_blocked`
- `mrp.mrp_workorder_workcenter_report`
- `mrp.mrp_workorder_report`
- `mrp.mrp_workcenter_workorders_kanban`
- `mrp.mrp_workcenter_action`
- `mrp.mrp_workcenter_kanban_action`
- `mrp.mrp_workcenter_productivity_report`
- `mrp.mrp_bom_form_action`
- `mrp.mrp_bom_line_action_used_in_boms`
- `mrp.template_open_bom`
- `mrp.product_open_bom`
- `mrp.mrp_production_action`
- `mrp.mrp_production_action_picking_deshboard`
- `mrp.action_mrp_production_form`
- `mrp.mrp_routing_action`
- `mrp.product_template_action`
- `stock.action_product_stock_view`
- `mrp.action_picking_tree_mrp_operation`
- `mrp.action_picking_tree_mrp_operation_graph`
- `mrp.action_mrp_unbuild_moves`
- `mrp.mrp_unbuild`
- `mrp.action_mrp_configuration`

## ir.actions.act_window.view

- `mrp.action_mrp_workcenter_load_report_pivot`

## ir.actions.client

- `mrp.action_report_mrp_bom`
- `mrp.action_report_mo_overview`
- `mrp.action_mrp_display`
- `mrp.action_mrp_display_fullscreen`

## ir.actions.report

- `mrp.action_report_production_order`
- `mrp.action_report_bom_structure`
- `mrp.action_report_mrp_mo_overview`
- `mrp.action_report_workorder`
- `mrp.action_report_mrp_packages`

## ir.actions.server

- `mrp.action_start_workorders`
- `mrp.action_pause_workorders`
- `mrp.action_plan_workorders`
- `mrp.action_unplan_workorders`
- `mrp.action_mark_as_done_workorders`
- `mrp.action_open_bom_lines`
- `mrp.action_production_order_confirm`
- `mrp.action_production_order_split`
- `mrp.action_print_labels`
- `mrp.action_print_finished_product_pdf`
- `mrp.action_print_finished_product_zpl`
- `mrp.action_production_order_lock_unlock`
- `mrp.action_production_order_scrap`
- `mrp.action_plan_at_date`
- `mrp.action_production_order_merge`
- `mrp.action_production_order_mark_done`
- `mrp.action_production_order_unbuild`
- `mrp.mrp_production_action_reserve`
- `mrp.mrp_production_action_unreserve_tree`

## ir.ui.menu

- `mrp.menu_mrp_root` — Manufacturing
- `mrp.menu_mrp_manufacturing` — Operations
- `mrp.mrp_planning_menu_root` — Planning
- `mrp.menu_mrp_bom` — Products
- `mrp.menu_mrp_reporting` — Reporting
- `mrp.menu_mrp_configuration` — Configuration
- `mrp.menu_mrp_traceability` — Lots/Serial Numbers
- `mrp.menu_mrp_scrap` — Scrap
- `mrp.menu_procurement_compute_mrp`
- `mrp.menu_view_resource_search_mrp`
- `mrp.menu_mrp_workcenter_productivity_report`
- `mrp.menu_mrp_bom_form_action`
- `mrp.menu_mrp_production_action`
- `mrp.menu_mrp_workorder_todo` — Work Orders
- `mrp.menu_mrp_work_order_report` — Work Orders
- `mrp.menu_mrp_routing_action`
- `mrp.menu_mrp_product_form` — Products
- `mrp.mrp_operation_picking` — Manufacturings
- `mrp.menu_mrp_unbuild` — Unbuild Orders
- `mrp.menu_mrp_config` — Settings

## ir.ui.view

- `mrp.exception_on_mo`
- `mrp.production_message`
- `mrp.track_production_move_template`
- `mrp.view_change_production_qty_wizard` — on change.production.qty
- `mrp.mrp_workcenter_block_wizard_form` — on mrp.workcenter.productivity
- `mrp.stock_warn_insufficient_qty_unbuild_form_view` — on stock.warn.insufficient.qty.unbuild inherits stock.stock_warn_insufficient_qty_form_view
- `mrp.view_mrp_production_backorder_form` — on mrp.production.backorder
- `mrp.view_mrp_consumption_warning_form` — on mrp.consumption.warning
- `mrp.view_mrp_production_split_multi_form` — on mrp.production.split.multi
- `mrp.view_mrp_production_split_form` — on mrp.production.split
- `mrp.view_mrp_production_serials_form` — on mrp.production.serials
- `mrp.view_mrp_stock_move_operations` — on stock.move inherits stock.view_stock_move_operations
- `mrp.view_stock_move_line_operation_tree_finished` — on stock.move.line inherits stock.view_stock_move_line_operation_tree
- `mrp.stock_move_line_view_search` — on stock.move.line inherits stock.stock_move_line_view_search
- `mrp.view_move_line_tree` — on stock.move.line inherits stock.view_move_line_tree
- `mrp.view_scrap_move_form_inherit_mrp` — on stock.move inherits stock.view_scrap_move_form
- `mrp.view_stock_move_line_detailed_operation_tree` — on stock.move.line inherits stock.view_stock_move_line_detailed_operation_tree
- `mrp.view_mrp_production_work_order_search` — on mrp.workorder
- `mrp.mrp_production_workorder_tree_editable_view` — on mrp.workorder
- `mrp.mrp_production_workorder_to_plan_list` — on mrp.workorder inherits mrp.mrp_production_workorder_tree_editable_view
- `mrp.mrp_production_workorder_tree_editable_view_mo_form` — on mrp.workorder inherits mrp_production_workorder_tree_editable_view
- `mrp.mrp_production_workorder_tree_view` — on mrp.workorder inherits mrp.mrp_production_workorder_tree_editable_view
- `mrp.view_mrp_production_workorder_form_view_filter` — on mrp.workorder
- `mrp.workcenter_line_calendar` — on mrp.workorder
- `mrp.workcenter_line_graph` — on mrp.workorder
- `mrp.workcenter_line_pivot` — on mrp.workorder
- `mrp.workcenter_line_kanban` — on mrp.workorder
- `mrp.mrp_production_workorder_form_view_inherit` — on mrp.workorder
- `mrp.mrp_production_workorder_tree_view_backorders` — on mrp.workorder inherits mrp.mrp_production_workorder_tree_editable_view
- `mrp.view_workcenter_load_pivot` — on mrp.workorder
- `mrp.view_work_center_load_graph` — on mrp.workorder
- `mrp.mrp_workcenter_tree_view` — on mrp.workcenter
- `mrp.mrp_workcenter_view_kanban` — on mrp.workcenter
- `mrp.oee_pie_view` — on mrp.workcenter.productivity
- `mrp.mrp_workcenter_kanban` — on mrp.workcenter
- `mrp.mrp_workcenter_view` — on mrp.workcenter
- `mrp.view_mrp_workcenter_search` — on mrp.workcenter
- `mrp.oee_loss_form_view` — on mrp.workcenter.productivity.loss
- `mrp.oee_loss_tree_view` — on mrp.workcenter.productivity.loss
- `mrp.view_mrp_workcenter_productivity_loss_kanban` — on mrp.workcenter.productivity.loss
- `mrp.oee_loss_search_view` — on mrp.workcenter.productivity.loss
- `mrp.oee_search_view` — on mrp.workcenter.productivity
- `mrp.oee_form_view` — on mrp.workcenter.productivity
- `mrp.oee_tree_view` — on mrp.workcenter.productivity
- `mrp.oee_graph_view` — on mrp.workcenter.productivity
- `mrp.oee_pivot_view` — on mrp.workcenter.productivity
- `mrp.mrp_bom_byproduct_form_view` — on mrp.bom.byproduct
- `mrp.mrp_bom_form_view` — on mrp.bom
- `mrp.mrp_bom_tree_view` — on mrp.bom
- `mrp.mrp_bom_kanban_view` — on mrp.bom
- `mrp.view_mrp_bom_filter` — on mrp.bom
- `mrp.mrp_bom_line_view_list` — on mrp.bom.line
- `mrp.mrp_bom_line_view_list_exploded_components` — on mrp.bom.line inherits mrp.mrp_bom_line_view_list
- `mrp.mrp_bom_line_view_pivot` — on mrp.bom.line
- `mrp.mrp_bom_line_view_search` — on mrp.bom.line
- `mrp.mrp_bom_line_view_form` — on mrp.bom.line
- `mrp.mrp_production_view_activity` — on mrp.production
- `mrp.mrp_production_tree_view` — on mrp.production
- `mrp.mrp_production_to_plan` — on mrp.production
- `mrp.mrp_production_form_view` — on mrp.production
- `mrp.mrp_production_card_view` — on mrp.production
- `mrp.mrp_production_kanban_view` — on mrp.production
- `mrp.view_production_calendar` — on mrp.production
- `mrp.view_production_pivot` — on mrp.production
- `mrp.view_production_graph` — on mrp.production
- `mrp.view_mrp_production_filter` — on mrp.production
- `mrp.mrp_routing_workcenter_tree_view` — on mrp.routing.workcenter
- `mrp.mrp_routing_workcenter_bom_tree_view` — on mrp.routing.workcenter inherits mrp_routing_workcenter_tree_view
- `mrp.mrp_routing_workcenter_copy_to_bom_tree_view` — on mrp.routing.workcenter inherits mrp_routing_workcenter_tree_view
- `mrp.mrp_routing_workcenter_form_view` — on mrp.routing.workcenter
- `mrp.mrp_routing_workcenter_kanban_view` — on mrp.routing.workcenter
- `mrp.mrp_routing_workcenter_filter` — on mrp.routing.workcenter
- `mrp.view_mrp_product_template_form_inherited` — on product.template inherits stock.product_template_form_view_stock
- `mrp.mrp_product_template_search_view` — on product.template inherits product.product_template_search_view
- `mrp.product_view_search_catalog` — on product.product inherits product.product_view_search_catalog
- `mrp.product_template_form_view_bom_button` — on product.template inherits stock.product_template_form_view_procurement_button
- `mrp.product_product_form_view_bom_button` — on product.product inherits stock.product_form_view_procurement_button
- `mrp.view_warehouse_orderpoint_tree_editable_inherited_purchase` — on stock.warehouse.orderpoint inherits stock.view_warehouse_orderpoint_tree_editable
- `mrp.view_warehouse_inherit_mrp` — on stock.warehouse inherits stock.view_warehouse
- `mrp.stock_production_type_kanban` — on stock.picking.type inherits stock.stock_picking_type_kanban
- `mrp.view_picking_form_inherit_mrp` — on stock.picking inherits stock.view_picking_form
- `mrp.view_picking_type_form_inherit_mrp` — on stock.picking.type inherits stock.view_picking_type_form
- `mrp.view_stock_rule_form` — on stock.rule inherits stock.view_stock_rule_form
- `mrp.mrp_unbuild_search_view` — on mrp.unbuild
- `mrp.mrp_unbuild_kanban_view` — on mrp.unbuild
- `mrp.mrp_unbuild_form_view` — on mrp.unbuild
- `mrp.mrp_unbuild_tree_view` — on mrp.unbuild
- `mrp.res_config_settings_view_form` — on res.config.settings inherits base.res_config_settings_view_form
- `mrp.mrp_bom_replenishment_tree_view` — on mrp.bom inherits mrp.mrp_bom_tree_view
- `mrp.view_stock_replenishment_info_stock_mrp_inherit` — on stock.replenishment.info inherits stock.view_stock_replenishment_info
- `mrp.stock_report_delivery_document_inherit_mrp` — inherits stock.report_delivery_document
- `mrp.stock_report_delivery_kit_sections`
- `mrp.stock_report_delivery_no_kit_section`
- `mrp.report_mrp_bom`
- `mrp.report_mrp_bom_pdf_line`
- `mrp.report_bom_structure`
- `mrp.report_mo_overview`
- `mrp.mo_overview_content`
- `mrp.mo_overview_line`
- `mrp.mo_overview_components`
- `mrp.mo_overview_operations`
- `mrp.mo_overview_byproducts`
- `mrp.report_mrporder`
- `mrp.report_mrp_production_components`
- `mrp.finished_product_4x12_label`
- `mrp.report_mrp_packages`
- `mrp.mrp_report_stock_rule` — inherits stock.report_stock_rule
- `mrp.finished_product_zpl_label`
- `mrp.report_mrp_workorder`

## mail.message.subtype

- `mrp.mt_mo_state`

## mrp.workcenter.productivity.loss

- `mrp.block_reason0`
- `mrp.block_reason1`
- `mrp.block_reason2`
- `mrp.block_reason4`
- `mrp.block_reason5`
- `mrp.block_reason6`
- `mrp.block_reason7`

## mrp.workcenter.productivity.loss.type

- `mrp.category_availability`
- `mrp.category_performance`
- `mrp.category_quality`
- `mrp.category_productive`

## res.groups

- `mrp.group_mrp_user`
- `mrp.group_mrp_manager`
- `mrp.group_mrp_routings`
- `mrp.group_mrp_byproducts`
- `mrp.group_unlocked_by_default`

## res.groups.privilege

- `mrp.res_groups_privilege_manufacturing`

## resource.calendar

- `mrp.mrp_workcenter_calendar`

## stock.route

- `mrp.route_warehouse0_manufacture`

## stock.warehouse

- `stock.warehouse0`
