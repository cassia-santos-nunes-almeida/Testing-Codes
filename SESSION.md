# SESSION.md — Current State

Overwritten at every session close. Read at every session open.
Last updated: 2026-03-22 · Session focus: Week 13 cleanup — headers, units, MCQ shuffling

## Completed This Session

* [x] Removed header blocks (course/training/points + `<hr>`) from all 5 Week 13 questions
* [x] Fixed unit line-breaks with `&nbsp;` in Q1, Q2, Q3, Q5 (14 fixes)
* [x] Converted Q2 (LosslessTL_Parameters) to STACK `units` input type
  - Changed ans1–ans5 from `numerical` to `units`
  - Added `stackunits()` teacher answers (ta1_u through ta5_u)
  - Changed PRT tests from `NumRelative` to `UnitsRelative` (5% tolerance)
  - Set `insertstars=1` on unit inputs
  - Removed "Give your answer in **X**" text (P-STACK-22)
  - Updated syntax hints to use unrelated unit examples (P-STACK-22)
* [x] Added `random_permutation()` to all 12 MCQ option lists across Q1–Q5
* [x] Added P-STACK-22 and P-STACK-23 to PATTERNS.md
* [x] Committed and pushed: `5ac3f92`

## In Progress

Task: Weeks 10-12 audit fixes (deferred)
Last state: Issues identified but deferred per user request
Next step: Fix when working on those weeks
Known issues:
  - Week 10 Q4: `{@ans2@}` and `{@ans3@}` in specificfeedback (P-STACK-03)
  - Week 10 Q1: Float literal `1e-7` in questionvariables (P-STACK-06)
  - All weeks 10-12: Missing `<hint>` blocks (15 questions)
  - Weeks 10-12: MCQ options likely need `random_permutation()` too (P-STACK-23)

Task: Progressive hint unlocking
Last state: Not started
Next step: Research STACK `[[if test="..."]]` conditional blocks

Task: Evaluate unit checking on remaining questions
Last state: Q2 converted as pilot; user to test in Moodle
Next step: If Q2 unit checking works well, consider extending to Q1, Q3, Q5
Note: Q3 ans2 (degrees) cannot use units — STACK has no native degree unit

## Open Decisions / Blockers

* [ ] **Q2 unit checking validation** — needs Moodle import + test with one variant before extending to other questions
* [ ] **Progressive hints for exams?** — TBD
* [ ] **Moodle re-import needed** — all 5 Week 13 XMLs need re-import (especially Q5 to restore corrupted JSXGraph)

## Patterns Triggered This Session

| Pattern ID | Triggered? | Applied? |
|------------|-----------|----------|
| P-STACK-12 | Syntax hints leaked correct units | Fixed — hints now use unrelated examples |
| P-STACK-22 | Created this session | Applied to Q2 |
| P-STACK-23 | Created this session | Applied to all Q1–Q5 MCQs |

## PATTERNS.md Updates This Session

* **Added:** P-STACK-22 — Unit-checked inputs must not hint the correct unit
* **Added:** P-STACK-23 — MCQ options must be shuffled with `random_permutation()`

## Skills Used This Session

* [x] context-evaluator (session open/close)
* [ ] circuitikz-circuit-diagrams
* [ ] stack-xml-generator

## Notes for Next Session

- All 5 Week 13 XMLs need re-import to Moodle — critical for Q5 (JSXGraph was corrupted by WYSIWYG editor)
- Q2 unit checking is a pilot — test before extending to other questions
- Weeks 10-12 still have deferred audit issues + now need MCQ shuffling check
- The Q5 "new problem" from last session turned out to be the JSXGraph blank graph after Moodle edit — resolved by fixing the XML source and re-importing
