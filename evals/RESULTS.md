# Results

Every measurement of the skills, oldest first. Each suite runs every task three times with
the skills and three times without them (`claude plugin eval`, with-without ablation); a
task scores the share of its graders that pass. The per-task data of each run since
1.1.0 is in [`history/`](history/). Costs are what the API charged, both sides included.

## Score by skills version

| Model | Odoo | Without | 1.0.0 | 1.1.0 | 1.1.1 step 1 | 1.1.1 |
|---|---|---|---|---|---|---|
| Sonnet 5.5 | 20.0 | 69.2% | 88.6% | 96.5% | 97.7% | 99.4% |
| Sonnet 5.5 | 19.0 | 94.4% | 97.0% | 100.0% | not measured | not measured |
| Sonnet 5.5 | 18.0 | 96.1% | 98.9% | 100.0% | not measured | not measured |
| Sonnet 5.5 | 17.0 | 94.0% | 99.6% | 100.0% | not measured | not measured |
| Sonnet 5.5 | 16.0 | 96.1% | 97.8% | 97.2% | 97.8% | 98.3% |
| Haiku 5.5 | 20.0 | 57.5% | not measured | 71.1% | 95.3% | 100.0% |
| Haiku 5.5 | 19.0 | 78.3% | not measured | 84.3% | 94.4% | 100.0% |
| Haiku 5.5 | 18.0 | 85.6% | not measured | 85.0% | 89.4% | 100.0% |
| Haiku 5.5 | 17.0 | 80.0% | not measured | 86.5% | 88.6% | 98.3% |
| Haiku 5.5 | 16.0 | 85.0% | not measured | 89.4% | 90.6% | 97.2% |

*Without* is the no-skills side of the 1.1.0 run. 1.0.0 scores are the totals reported
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

Exact tokens come from the Anthropic Console usage export (2026-10-20 and 2026-10-28) or
from the traces of each run. Estimated tokens are the run's cost times the tokens per USD
measured on exact data of the same model: the 2026-10-28 export for Sonnet, the 10 kept
Haiku traces for Haiku. Most input is read from the prompt cache, which costs a fraction of
fresh input: that is why a whole suite costs a few dollars with Sonnet and cents with Haiku.
On 2026-10-29 a run was refused for lack of credit and cost nothing.

Total spent on measurements: about 70.29 USD.
