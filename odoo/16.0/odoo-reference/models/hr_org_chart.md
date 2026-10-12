# hr_org_chart — HR Org Chart

Depends on: hr.

## `hr.employee` (extends)

- `subordinate_ids` One2many → `hr.employee` “Subordinates” (compute=_compute_subordinates)

## `hr.employee.public` (extends)

- `subordinate_ids` One2many → `hr.employee.public` “Subordinates” (compute=_compute_subordinates)

## `hr.employee.base` (extends)

- `child_all_count` Integer “Indirect Subordinates Count” (compute=_compute_subordinates)

Extension points: `_get_subordinates`
