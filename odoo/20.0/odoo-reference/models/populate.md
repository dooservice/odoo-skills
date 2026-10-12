# populate — Populate

Depends on: base.

## `populate.blueprint` (defines)

Data Population Blueprint

- `name` Char “Blueprint Name” (required)
- `inherit_id` Many2one → `populate.blueprint` “Inherited Blueprint” (index)
- `definition_xml` Char “Raw XML Definition”
- `definition_json` Json “Raw JSON Definition”
- `definition` Json “JSON Definition” (readonly, compute=_compute_definition)

Public methods: `create`, `write`

Extension points: `_check_definition`, `_get_resolved_definition`

## `populate.job` (defines)

Data Population Job

- `seed` Integer
- `parent_id` Many2one → `populate.job` (index)
- `child_ids` One2many → `populate.job`
- `parent_path` Char (index)
- `blueprint_id` Many2one → `populate.blueprint` (required, store, index, related=session_id.blueprint_id)
- `session_id` Many2one → `populate.session` (required, index)
- `is_done` Boolean
- `ref` Char
- `domain` Char
- `model_name` Char (required)
- `method_name` Char
- `record_count` Integer
- `operation` Selection (required)
- `parallel` Boolean
- `batched` Boolean
- `context` Json
- `instructions` Json

Public methods: `is_executable`, `pending_subjobs`, `progress`

Extension points: `_check_parent_hierarchy`, `_check_same_session`, `_check_single_level_hierarchy`, `_create_subjobs`, `_get_target_domain`, `_get_target_records`

## `populate.model.data` (defines)

Reference to Populated Records.

- `res_model` Char “Model” (related=job_id.model_name)
- `res_id` Many2oneReference “Record” (required)
- `job_id` Many2one → `populate.job` (required)
- `ref` Char (related=job_id.ref)
- `session_id` Many2one (related=job_id.session_id)
- `blueprint_id` Many2one (related=job_id.blueprint_id)

## `populate.session` (defines)

Data Population Session

- `seed` Integer “Seed”
- `scaling_factor` Float “Scaling Factor”
- `worker_count` Integer “Number of parallel workers that will run jobs at the same time”
- `blueprint_id` Many2one → `populate.blueprint` (required)
- `job_ids` One2many → `populate.job`

Public methods: `create`, `is_done`, `is_parallel`, `is_profiling`, `is_running`, `pending_jobs`, `profile_session_name`, `progress`

Extension points: `_check_has_jobs`
