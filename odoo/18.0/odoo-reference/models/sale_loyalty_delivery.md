# sale_loyalty_delivery — Sale Loyalty - Delivery

Depends on: sale_loyalty, delivery.

## `loyalty.program` (extends)


Public methods: `get_program_templates`

Extension points: `_get_template_values`

## `loyalty.reward` (extends)

- `reward_type` Selection

## `sale.order` (extends)


Extension points: `_get_claimable_rewards`, `_get_no_effect_on_threshold_lines`, `_get_not_rewarded_order_lines`, `_get_reward_line_values`, `_get_reward_values_free_shipping`
