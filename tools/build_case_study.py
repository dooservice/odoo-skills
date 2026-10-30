"""Draws the charts of the case study into `docs/case-study/img/`.

Usage: uv run --with matplotlib python tools/build_case_study.py
"""

from case_study.build import CaseStudyBuild

CaseStudyBuild().run()
