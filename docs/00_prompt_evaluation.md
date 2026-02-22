# Prompt Evaluation: Midterm Exam Design

## Original Prompt Assessment

### Strengths

1. **Well-defined scaffolding framework (A-E)**: The subpart structure guides students without giving away solutions. This is pedagogically sound and aligns with Bloom's taxonomy progression from recall → application → analysis.

2. **AI-resistance strategies**: Per-student parameter randomization, surface variation, debug/critique subparts, and handwritten upload requirements create multiple barriers to pure AI-assisted cheating.

3. **Equivalence checking across variants**: Requiring identical difficulty, algebraic complexity, and time-on-task across variants within each pool ensures fairness regardless of which variant a student receives.

4. **Learning-oriented design**: Post-exam feedback supporting learning (not just grading) is excellent pedagogical practice. The feedback-after-close approach avoids giving away answers during the exam window.

5. **Clear content boundaries**: Explicit exclusion of RLC transients prevents ambiguity about exam scope.

6. **International student awareness**: Emphasis on clear English, defined symbols, and no idioms shows sensitivity to the diverse cohort.

### Weaknesses Identified and Corrections Applied

| # | Issue | Impact | Correction |
|---|-------|--------|------------|
| 1 | **No time budget analysis** | 120 min for 4 scaffolded questions (16-20 subparts) + handwritten upload is tight. Students may rush. | Kept calculations manageable; one consolidated upload at end saves ~10 min; aimed for 20+30+30+30+10(upload) = 120 min budget. |
| 2 | **STACK limitations unaddressed** | Justification/interpretation subparts cannot be auto-graded by STACK. Mixed grading creates instructor workload. | Explicit STACK/Essay split: ~60% auto-graded (STACK), ~40% manual (Essay). Essay subparts kept short (2-4 sentences). |
| 3 | **Equation input in STACK** | Students typing algebraic equations in Maxima syntax is error-prone and frustrating, especially for international students unfamiliar with the format. | Primarily use numerical STACK inputs; algebraic only for simple expressions; clear format examples shown to students. |
| 4 | **Dependent sources in Easy question** | Students reported difficulty with dependent sources. Including them in Q1 (Easy) would misrepresent difficulty. | Q1 uses only independent sources. Dependent sources appear only in Q4 (Difficult) variants where complexity is expected. |
| 5 | **Upload logistics** | Per-question uploads (4x photo + upload cycle) would consume ~20 min of exam time. | Single consolidated upload area at end of quiz. Separate timer possible in Moodle. |
| 6 | **Debug coverage guarantee** | "At least one debug per attempt" requires careful pool design. Random selection could theoretically skip debug questions. | Debug/compare subpart embedded in EVERY Q2 variant, guaranteeing every student encounters one regardless of random selection. |
| 7 | **Pool size ambition** | 15 full STACK questions with complete Maxima code, PRTs, feedback is massive. Quality may suffer. | Maintained 4+4+4+3=15 as requested, but simplified PRT structures where possible. |
| 8 | **Fields question depth mismatch** | Prompt asks for "fields connection" but Week 5 was conceptual only. Calculation-based fields questions would be unfair. | Fields questions ask for conceptual explanations only (no Lorentz force calculations). Rewards understanding over memorization. |
| 9 | **Missing accessibility considerations** | No mention of screen readers, dyslexia-friendly formatting, or extra time accommodations. | Clear formatting, adequate whitespace, sans-serif fonts in SVG diagrams, high-contrast colors. |
| 10 | **Point split equal for Easy and Difficult** | Q1=12, Q4=12 gives same weight to easy and difficult. Could reduce discrimination. | Kept as requested (instructor preference). The scaffolding within Q4 provides difficulty gradient internally. |

### Structural Improvements Made

1. **Time allocation guidance added**: Each pool specification includes expected time-on-task.
2. **Input format examples**: Each STACK input includes placeholder text showing expected format.
3. **Grading rubric per subpart**: Clear criteria for partial credit on Essay subparts.
4. **Circuit diagrams with explicit reference directions**: All SVG diagrams show current arrows and voltage polarities, removing ambiguity.
5. **Randomization constraints**: Variable ranges chosen to avoid degenerate cases (division by zero, negative resistance, unrealistic values).

## Summary of Final Exam Design

- **4 questions** per student: Easy (12 pts) + Medium (13 pts) + Medium (13 pts) + Difficult (12 pts) = **50 points**
- **15 variants** total across 4 pools, each with per-student parameter randomization
- **Mixed assessment**: STACK auto-grading for numerical answers + Essay for conceptual understanding + Upload for process verification
- **AI-resistant features**: Randomization, debug/critique, personal justification, handwritten upload
- **Post-exam learning**: Feedback snippets per subpart released after quiz closes
