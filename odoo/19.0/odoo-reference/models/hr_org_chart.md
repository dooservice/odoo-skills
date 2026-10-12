# hr_org_chart — HR Org Chart

Depends on: hr, web_hierarchy.

## `hr.employee` (extends)

- `subordinate_ids` One2many → `hr.employee` “Subordinates” (compute=_compute_subordinates)
- `is_subordinate` Boolean (compute=_compute_is_subordinate)

## `hr.employee.public` (extends)

- `subordinate_ids` One2many (related=employee_id.subordinate_ids)
- `is_subordinate` Boolean (related=employee_id.is_subordinate)

## `hr.employee` (extends)

- `child_all_count` Integer “Indirect Subordinates Count” (compute=_compute_subordinates)
- `department_color` Integer “Department Color” (related=department_id.color)
- `child_count` Integer “Direct Subordinates Count” (compute=_compute_child_count)

Extension points: `_get_subordinates`

## `hr.employee.public` (extends)

- `child_all_count` Integer (compute=_compute_child_all_count)
- `department_color` Integer (compute=_compute_department_color)
- `child_count` Integer (compute=_compute_child_count)
