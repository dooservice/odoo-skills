# hr_org_chart — HR Org Chart

Depends on: hr, web_hierarchy.

## `hr.employee` (extends)

- `subordinate_ids` One2many → `hr.employee` “Subordinates” (compute=_compute_subordinates)
- `is_subordinate` Boolean (compute=_compute_is_subordinate)

## `hr.employee.public` (extends)

- `subordinate_ids` One2many → `hr.employee.public` “Subordinates” (compute=_compute_subordinates)
- `is_subordinate` Boolean (compute=_compute_is_subordinate)

## `hr.employee.base` (extends)

- `child_all_count` Integer “Indirect Subordinates Count” (compute=_compute_subordinates)
- `department_color` Integer “Department Color” (related=department_id.color)
- `child_count` Integer “Direct Subordinates Count” (compute=_compute_child_count)

Extension points: `_get_subordinates`
