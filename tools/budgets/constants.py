"""Size budgets of each skill layer, in characters (about four per token)."""

from __future__ import annotations

from pathlib import Path

#: Root of the repository.
REPOSITORY = Path(__file__).resolve().parent.parent.parent

#: Folder holding one folder per Odoo version plus the common one.
SKILLS_FOLDER = REPOSITORY / "odoo"

#: File that holds the front matter and the body of a skill.
SKILL_FILE = "SKILL.md"

#: Line that opens and closes the front matter.
FRONT_MATTER_FENCE = "---"

#: Front matter key of the description.
DESCRIPTION_KEY = "description:"

#: YAML block markers that put the value on the following lines.
BLOCK_MARKERS = (">", ">-", "|", "|-")

#: Characters stripped around a single-line front matter value.
VALUE_QUOTES = "\"'"

#: Longest description the Agent Skills format accepts.
DESCRIPTION_LIMIT = 1024

#: Longest SKILL.md body per skill name.
BODY_LIMITS = {
    "odoo-guidelines": 3200,
    "odoo-web-guidelines": 2400,
    "odoo-functional": 3600,
    "odoo-reference": 4000,
    "odoo-security": 12000,
    "odoo-review": 12000,
    "odoo-git": 12000,
    "odoo-upgrade": 12000,
}

#: Longest SKILL.md body of a skill missing from BODY_LIMITS.
DEFAULT_BODY_LIMIT = 12000

#: Longest guideline file, recipe or any other file of a skill.
FILE_LIMIT = 20000

#: Skill whose generated data files are searched, not read.
REFERENCE_SKILL = "odoo-reference"

#: Folders of the reference skill exempt from budgets.
EXEMPT_FOLDERS = ("models", "xmlids")

#: Files of the reference skill exempt from budgets.
EXEMPT_FILES = ("addons.md", "settings.md")

#: Characters per token, to show an approximate token count.
CHARS_PER_TOKEN = 4

#: Rows of the table of biggest files.
TABLE_ROWS = 25

#: Fewest words a sentence needs to count as a duplicate.
DUPLICATE_WORDS = 12

#: Characters that end a sentence when they end a word.
SENTENCE_ENDS = (".", "!", "?", ";", ":")

#: Characters stripped around each word before comparing sentences.
WORD_PUNCTUATION = "`*_()[]{}\"',.;:!?|<>-"

#: Line that opens or closes a fenced code block.
CODE_FENCE = "```"

#: Line starts that open a new block of prose, ending the sentence before.
BLOCK_STARTS = ("#", "-", "*", "|", ">")
