# hr_timesheet_attendance — Timesheets/attendances reporting

Depends on: hr_timesheet, hr_attendance.

## `ir.ui.menu` (extends)


## `hr.timesheet.attendance.report` (defines)

Timesheet Attendance Report

- `employee_id` Many2one → `hr.employee` (readonly)
- `date` Date (readonly)
- `total_timesheet` Float “Timesheets Time” (readonly)
- `total_attendance` Float “Attendance Time” (readonly)
- `total_difference` Float “Time Difference” (readonly)
- `timesheets_cost` Float “Timesheet Cost” (readonly)
- `attendance_cost` Float “Attendance Cost” (readonly)
- `cost_difference` Float “Cost Difference” (readonly)
- `company_id` Many2one → `res.company` “Company” (readonly)

Public methods: `formatted_read_group`, `init`
