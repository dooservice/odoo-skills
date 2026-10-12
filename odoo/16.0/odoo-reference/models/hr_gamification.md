# hr_gamification — HR Gamification

Depends on: gamification, hr.

## `gamification.badge.user` (extends)

- `employee_id` Many2one → `hr.employee` “Employee” (index)

Public methods: `action_open_badge`

Extension points: `_check_employee_related_user`

## `gamification.badge` (extends)

- `granted_employees_count` Integer (compute=_compute_granted_employees_count)

Public methods: `get_granted_employees`

## `hr.employee.base` (extends)

- `goal_ids` One2many → `gamification.goal` “Employee HR Goals” (compute=_compute_employee_goals)
- `badge_ids` One2many → `gamification.badge.user` “Employee Badges” (compute=_compute_employee_badges)
- `has_badges` Boolean (compute=_compute_employee_badges)
- `direct_badge_ids` One2many → `gamification.badge.user`

## `res.users` (extends)

- `goal_ids` One2many → `gamification.goal`
- `badge_ids` One2many → `gamification.badge.user`

## `gamification.badge.user.wizard` (extends)

- `employee_id` Many2one → `hr.employee` “Employee” (required)
- `user_id` Many2one → `res.users` “User” (readonly, related=employee_id.user_id)

Public methods: `action_grant_badge`
