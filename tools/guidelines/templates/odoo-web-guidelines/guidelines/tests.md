Key names in $version:

$essentials

Sections of this file:

$sections

# Unit tests in $version

$framework

# Mock the server with test models, never with a database

$mock_server

# Interact through the test helpers and wait for the DOM

$interact

# Undo every patch a test makes

$patch_cleanup

# Register a tour in the `web_tour.tours` registry

$tour_register

# Write each tour step as a trigger and an action

$tour_steps

# Run tours from an `HttpCase`

A tour runs in a real browser against a real database, so it is the test for a whole
flow (open a menu, fill a form, save); a unit test is the test for one component.

- The tour file goes in the `web.assets_tests` bundle of the manifest
  (`'web.assets_tests': ['my_module/static/tests/tours/**/*']`), never in
  `web.assets_backend`: it would ship to every user.
- The Python test is an `HttpCase` tagged `@tagged('post_install', '-at_install')`:
  the tour needs every module installed and the assets built.
- Start it with `self.start_tour("$tour_url", "my_module.my_tour", login="admin")`; the
  signature is `start_tour(url_path, tour_name, step_delay=None, **kwargs)`, and
  `step_delay` is for watching a tour locally, never for a committed test.
- Create the records the tour needs in the Python test, before `start_tour`, and check
  the result there afterwards: the tour proves the UI flow, the Python asserts prove the
  data.
