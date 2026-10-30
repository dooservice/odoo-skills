# Results

Every measurement of the skills, oldest first. Each suite runs every task three times (five
for the final 2.0.0 Haiku runs) with the skills and as many times without them (`claude plugin eval`, with-without ablation); a
task scores the share of its graders that pass. The per-task data of each run since
1.1.0 is in [`history/`](history/). Costs are what the API charged, both sides included.

## Score by skills version

| Model | Odoo | Without | 1.0.0 | 1.1.0 | 1.1.1 step 1 | 1.1.1 | 1.1.1 rerun | 2.0.0 step 1 | 2.0.0 |
|---|---|---|---|---|---|---|---|---|---|
| Sonnet 5.5 | 20.0 | 69.2% | 88.6% | 96.5% | 97.7% | 99.4% | not measured | not measured | 99.4% |
| Sonnet 5.5 | 19.0 | 94.4% | 97.0% | 100.0% | not measured | not measured | not measured | not measured | not measured |
| Sonnet 5.5 | 18.0 | 96.1% | 98.9% | 100.0% | not measured | not measured | not measured | not measured | not measured |
| Sonnet 5.5 | 17.0 | 94.0% | 99.6% | 100.0% | not measured | not measured | not measured | not measured | not measured |
| Sonnet 5.5 | 16.0 | 96.1% | 97.8% | 97.2% | 97.8% | 98.3% | not measured | not measured | not measured |
| Haiku 5.5 | 20.0 | 57.5% | not measured | 71.1% | 95.3% | 100.0% | 97.1% | 98.2% | 98.6% |
| Haiku 5.5 | 19.0 | 78.3% | not measured | 84.3% | 94.4% | 100.0% | 96.5% | 97.5% | 96.1% |
| Haiku 5.5 | 18.0 | 85.6% | not measured | 85.0% | 89.4% | 100.0% | 98.9% | 97.1% | 97.3% |
| Haiku 5.5 | 17.0 | 80.0% | not measured | 86.5% | 88.6% | 98.3% | 95.1% | 95.4% | 99.7% |
| Haiku 5.5 | 16.0 | 85.0% | not measured | 89.4% | 90.6% | 97.2% | 90.6% | 97.8% | 99.7% |

*1.1.1 rerun* measures the 1.1.1 skills again, with exact tokens, as the baseline of
2.0.0: the same skills score up to 7 points below their first run, which shows how much a
three-run suite moves by chance. *2.0.0 step 1* is the first layered version; *2.0.0* is
the release, measured with five runs per task (Haiku). *Without* is the no-skills side of the 1.1.0 run. 1.0.0 scores are the totals reported
at the time (2026-10-20 for 16.0 and 20.0, 2026-10-28 for 17.0 to 19.0); their per-task data
was not kept. Sonnet on 17.0 to 19.0 was not measured again after 1.1.0: it was at 100%,
and 1.1.1 changes only descriptions.

## Code and functional tasks

| Model | Odoo | Skills | Code without | Code with | Functional without | Functional with | Cost |
|---|---|---|---|---|---|---|---|
| Haiku 5.5 | 16.0 | 1.1.0 | 81.1% | 86.7% | 88.9% | 92.2% | 0.26 USD |
| Haiku 5.5 | 17.0 | 1.1.0 | 74.2% | 81.8% | 86.4% | 91.7% | 0.27 USD |
| Haiku 5.5 | 18.0 | 1.1.0 | 80.0% | 75.6% | 91.1% | 94.4% | 0.27 USD |
| Haiku 5.5 | 19.0 | 1.1.0 | 83.3% | 89.8% | 72.2% | 77.8% | 0.32 USD |
| Haiku 5.5 | 20.0 | 1.1.0 | 55.6% | 61.9% | 58.6% | 76.4% | 0.28 USD |
| Sonnet 5.5 | 16.0 | 1.1.0 | 93.3% | 94.4% | 98.9% | 100.0% | 4.25 USD |
| Sonnet 5.5 | 17.0 | 1.1.0 | 90.9% | 100.0% | 97.5% | 100.0% | 4.45 USD |
| Sonnet 5.5 | 18.0 | 1.1.0 | 95.6% | 100.0% | 96.7% | 100.0% | 4.11 USD |
| Sonnet 5.5 | 19.0 | 1.1.0 | 99.1% | 100.0% | 88.9% | 100.0% | 4.74 USD |
| Sonnet 5.5 | 20.0 | 1.1.0 | 66.7% | 90.5% | 70.6% | 100.0% | 4.20 USD |
| Haiku 5.5 | 16.0 | 1.1.1 | 87.8% | 96.7% | 90.0% | 97.8% | 0.30 USD |
| Haiku 5.5 | 17.0 | 1.1.1 | 85.4% | 100.0% | 86.4% | 96.4% | 0.31 USD |
| Haiku 5.5 | 18.0 | 1.1.1 | 89.8% | 100.0% | 82.8% | 100.0% | 0.31 USD |
| Haiku 5.5 | 19.0 | 1.1.1 | 83.3% | 100.0% | 71.1% | 100.0% | 0.40 USD |
| Haiku 5.5 | 20.0 | 1.1.1 | 57.1% | 100.0% | 60.2% | 100.0% | 0.36 USD |
| Sonnet 5.5 | 16.0 | 1.1.1 | 91.1% | 96.7% | 98.9% | 100.0% | 4.23 USD |
| Sonnet 5.5 | 20.0 | 1.1.1 | 66.7% | 100.0% | 69.7% | 99.1% | 4.52 USD |
| Haiku 5.5 | 16.0 | 1.1.1-step-1 | 83.3% | 86.7% | 90.0% | 94.4% | 0.28 USD |
| Haiku 5.5 | 17.0 | 1.1.1-step-1 | 81.3% | 90.9% | 93.1% | 86.1% | 0.28 USD |
| Haiku 5.5 | 18.0 | 1.1.1-step-1 | 83.8% | 86.7% | 91.1% | 92.2% | 0.28 USD |
| Haiku 5.5 | 19.0 | 1.1.1-step-1 | 88.0% | 100.0% | 72.2% | 87.8% | 0.37 USD |
| Haiku 5.5 | 20.0 | 1.1.1-step-1 | 61.9% | 100.0% | 57.6% | 92.6% | 0.34 USD |
| Sonnet 5.5 | 16.0 | 1.1.1-step-1 | 92.2% | 95.6% | 98.9% | 100.0% | 4.25 USD |
| Sonnet 5.5 | 20.0 | 1.1.1-step-1 | 69.8% | 100.0% | 66.9% | 96.3% | 4.47 USD |

## Context per task (exact tokens)

What an agent sends per task, input and prompt cache together, averaged over the runs of
each suite; *added* is the side with the skills minus the side without them. Read from the
final result event of every trace.

| Model | Odoo | Skills | Runs | Score | Context with | Context without | Added | Turns with | Cost per task |
|---|---|---|---|---|---|---|---|---|---|
| Haiku 5.5 | 20.0 | 1.1.1 rerun | 3 | 97.1% | 113,170 | 33,446 | 79,725 | 7.5 | 0.0049 USD |
| Haiku 5.5 | 20.0 | 2.0.0 | 5 | 98.6% | 83,921 | 31,075 | 52,846 (-34%) | 6.3 | 0.0039 USD |
| Haiku 5.5 | 19.0 | 1.1.1 rerun | 3 | 96.5% | 94,918 | 35,348 | 59,571 | 6.4 | 0.0043 USD |
| Haiku 5.5 | 19.0 | 2.0.0 | 5 | 96.1% | 75,325 | 34,838 | 40,487 (-32%) | 5.9 | 0.0036 USD |
| Haiku 5.5 | 18.0 | 1.1.1 rerun | 3 | 98.9% | 72,123 | 31,616 | 40,507 | 4.9 | 0.0035 USD |
| Haiku 5.5 | 18.0 | 2.0.0 | 5 | 97.3% | 61,457 | 30,965 | 30,492 (-25%) | 4.6 | 0.0032 USD |
| Haiku 5.5 | 17.0 | 1.1.1 rerun | 3 | 95.1% | 59,129 | 30,715 | 28,414 | 4.0 | 0.0031 USD |
| Haiku 5.5 | 17.0 | 2.0.0 | 5 | 99.7% | 56,426 | 29,982 | 26,444 (-7%) | 4.2 | 0.0030 USD |
| Haiku 5.5 | 16.0 | 1.1.1 rerun | 3 | 90.6% | 70,210 | 29,691 | 40,519 | 4.8 | 0.0034 USD |
| Haiku 5.5 | 16.0 | 2.0.0 | 5 | 99.7% | 63,494 | 30,149 | 33,345 (-18%) | 4.9 | 0.0032 USD |
| Sonnet 5.5 | 20.0 | 2.0.0 | 3 | 99.4% | 62,493 | 25,439 | 37,054 | 4.7 | 0.0461 USD |

Over the five versions, the context the skills add goes from 248.7k to 183.6k tokens per
task (-26%). Most of what is left is turns, not reading: every turn sends the whole
context again, and an agent with skills takes at least three (load the skill, read a file,
write) where one without takes one or two.

## Cost and tokens

| Date | What was measured | Cost | Input | Cache write | Cache read | Output | Tokens |
|---|---|---|---|---|---|---|---|
| 2026-10-20 | 1.0.0, Sonnet on 16.0 and 20.0, with the development runs | about 14 USD | 26,241 | 3,381,689 | 13,471,391 | 357,535 | exact (Sonnet) |
| 2026-10-28 | 1.0.0 skills on the new 17.0 to 19.0 suites, Sonnet | 12.35 USD | 2,292 | 3,088,714 | 12,058,980 | 341,554 | exact |
| 2026-10-30 | 1.1.0, Haiku on 20.0, 19.0, 18.0, 17.0, 16.0 | 1.40 USD | 3,903 | 5,453,138 | 25,167,330 | 15,009 | estimated |
| 2026-10-30 | 1.1.0, Sonnet on 20.0, 19.0, 18.0, 17.0, 16.0 | 21.75 USD | 4,046 | 5,440,157 | 21,239,534 | 601,576 | estimated |
| 2026-10-30 | 1.1.1 (descriptions of the reference, JS tasks), Haiku on 20.0, 19.0, 18.0, 17.0, 16.0 | 1.68 USD | 4,686 | 6,548,200 | 30,221,263 | 18,023 | estimated |
| 2026-10-30 | 1.1.1 (descriptions of the reference, JS tasks), Sonnet on 20.0, 16.0 | 8.75 USD | 1,628 | 2,188,633 | 8,544,889 | 242,020 | estimated |
| 2026-10-30 | 1.1.1 step 1 (descriptions of the guidelines), Haiku on 20.0, 19.0, 18.0, 17.0, 16.0 | 1.55 USD | 4,306 | 6,016,813 | 27,768,804 | 16,561 | estimated |
| 2026-10-30 | 1.1.1 step 1 (descriptions of the guidelines), Sonnet on 20.0, 16.0 | 8.72 USD | 1,622 | 2,181,455 | 8,516,865 | 241,227 | estimated |
| 2026-10-30 | Diagnosis: 6 failing tasks with traces kept | 0.08 USD | 86 | 123,061 | 541,889 | 692 | exact |
| 2026-10-30 | 1.1.1 rerun with exact tokens (baseline of 2.0.0), Haiku on 20.0 to 16.0 | 1.75 USD | 3,850 | 7,568,549 | 27,260,839 | 1,054,152 | exact |
| 2026-10-30 | 1.1.1 rerun whose tokens were not read (parser fault) | 1.70 USD | not read | not read | not read | not read | none |
| 2026-10-30 | 2.0.0 step 1, Haiku on 20.0 to 16.0 | 1.67 USD | 3,764 | 7,203,414 | 24,837,911 | 1,036,925 | exact |
| 2026-10-30 | Diagnosis with traces kept, Haiku on 16.0 and 17.0 | 0.63 USD | 1,376 | 2,762,716 | 8,660,311 | 400,600 | exact |
| 2026-10-30 | 2.0.0 trials (descriptions, method.md, skill folder), three rounds of Haiku on 20.0 to 16.0 | 4.98 USD | 11,708 | 21,014,532 | 78,492,671 | 3,127,399 | exact |
| 2026-10-30 | 2.0.0, Haiku on 20.0 to 16.0, five runs per task | 2.67 USD | 6,112 | 11,396,263 | 39,319,512 | 1,697,611 | exact |
| 2026-10-30 | 2.0.0 services fix, Haiku on 19.0, five runs per task | 0.63 USD | 1,482 | 2,600,811 | 9,913,080 | 408,767 | exact |
| 2026-10-30 | 2.0.0, Sonnet on 20.0, before and after the eval fixes | 7.98 USD | 1,494 | 2,131,262 | 8,070,204 | 184,507 | exact |

Exact tokens come from the Anthropic Console usage export (2026-10-20 and 2026-10-28) or
from the traces of each run. Estimated tokens are the run's cost times the tokens per USD
measured on exact data of the same model: the 2026-10-28 export for Sonnet, the 10 kept
Haiku traces for Haiku. Most input is read from the prompt cache, which costs a fraction of
fresh input: that is why a whole suite costs a few dollars with Sonnet and cents with Haiku.
On 2026-10-29 a run was refused for lack of credit and cost nothing.

Total spent on measurements: about 92.29 USD (70.29 USD up to 1.1.1, 22.00 USD for 2.0.0).
