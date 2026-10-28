## Generating the guideline for every version

- Never edit a skill under `odoo/<version>/` by hand: the build overwrites it. A
  guideline file is a `Document` subclass in `tools/guidelines/documents/`, listed in
  `DOCUMENTS` of `tools/guidelines/build.py`; it either takes Odoo's file as it is or
  fills a template under `tools/guidelines/templates/$skill/`.
- Write each guideline for every version the repository covers, 16.0 to 20.0. Put
  what differs in a template value picked per range of versions
  (`version.pick(v16_17=..., v18_=...)`), never in a sentence that lists versions.
- Check every version-specific statement (a name, an argument, a default, a tag) in
  the source of each version it is written for. A statement checked in one version
  is not checked in the others.
- Write ASCII punctuation only: the build refuses typographic characters.
- Regenerate every version with `python3 build_guidelines.py <odoo 20.0 skills> ..`
  from `tools/`, and read the diff of each version before committing.
