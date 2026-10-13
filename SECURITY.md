# Security policy

These skills tell AI agents how to write Odoo code, so a mistake in them can end up in
real modules. The `odoo-security` skill in particular must be right.

## Reporting a problem

If a skill tells an agent to do something unsafe (skip access checks, build SQL from user
input, disable CSRF, trust `sudo()`), report it privately through GitHub:
[**Report a vulnerability**](https://github.com/dooservice/odoo-skills/security/advisories/new),
in the *Security* tab of this repository, or by email to
[soporte@apiservicesac.com](mailto:soporte@apiservicesac.com) with «Security» in the subject. Say
which skill and version, the instruction, and why it is unsafe.

We answer within **3 working days**, fix it in every version it affects, and publish an
advisory once the fix is out, crediting you if you want.

A wrong but harmless instruction (an outdated API name, a typo) is a normal bug: open an
issue.

## Scope

Only the text of the skills and the generators in `tools/`. Vulnerabilities in Odoo
itself go to [Odoo's security team](https://www.odoo.com/security-report).
