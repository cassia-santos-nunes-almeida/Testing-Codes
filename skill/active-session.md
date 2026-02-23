# Active Session — STACK Exam Builder

## Current Milestone
**Exam content complete and audit-hardened.** All 15 question variants have been through multiple rounds of Moodle compatibility fixes, a critical exam audit (answer leaks, tolerance bugs, formula errors), and diagram export. The project is ready for Moodle import testing.

## Completed Tasks
- [x] Prompt evaluation and corrections documented (`docs/00_prompt_evaluation.md`)
- [x] Exam overview specification written (`docs/01_exam_overview.md`)
- [x] Q1 Easy — 4 STACK variants with SVG diagrams (two-node, two-mesh, T-network, bridge)
- [x] Q2 Medium A — 4 STACK+Essay variants with SVG diagrams (inductor RL, capacitor RC, inductor waveform, capacitor parallel)
- [x] Q3 Medium B — 4 STACK variants with SVG diagrams (RL step, RC step, RL natural, RC natural)
- [x] Q4 Difficult — 3 STACK variants with SVG diagrams (RC switch, RL switch, Thevenin RC)
- [x] Upload question with per-question checklists
- [x] Claude skill package created
- [x] PNG exports generated for all 15 diagrams (1200px, 150 DPI)
- [x] **Moodle compatibility fixes (multiple rounds):**
  - Q1 STACK dropdown MCQ format fixed (bare integer → Maxima `[[value, bool, "text"]]` list format)
  - Q2 dropdowns converted to match Q1 format (options moved into `questionvariables`)
  - SVG embedding iterated: base64 data URIs → `@@PLUGINFILE@@` → **text placeholders** (final approach)
- [x] **Critical exam audit fixes:**
  - Q4 V2: Fixed time constant formula (removed ×1000 error in `tau_ms`)
  - Q3 all: Removed `syntaxhint` on `ansB` that leaked exact transfer function answers
  - Q3 all: Added uppercase A,B,C,D to MCQ `allowwords` for case-insensitive input
  - Q1 all: Removed textarea placeholders that gave away Part B equations
  - Q1 V3: Removed duplicate `Vs`/`Is` variable assignment
  - Q1 V4: Removed balance condition hint from Part D placeholder
  - Q2 all: Changed `prtB` from `NumAbsolute` to `NumRelative` (5%) to fix tolerance bug
  - Q4 all: Removed textarea placeholders that leaked s-domain solutions

## Immediate Next Steps (Prioritized)
1. **Moodle test import** — Import all 5 XML files into a Moodle sandbox and verify:
   - Questions render correctly (formatting intact)
   - Diagrams display after manual upload via placeholders
   - STACK randomization produces valid parameter combinations
   - PRTs grade sample answers correctly
   - Essay textareas appear with correct word limits
   - Upload question accepts PDF/JPG/PNG up to 4 files
2. **Peer review** — Have a colleague attempt each variant to check:
   - Time-on-task estimates (20+30+30+30 min) are realistic
   - Difficulty equivalence across variants within each pool
   - Wording clarity for international students
3. **Feedback pass** — Review all STACK feedback strings for tone and helpfulness (post-exam learning goal)
4. **Quiz assembly** — Configure Moodle quiz settings (random question from each pool, sequential navigation, timer, single attempt)

## Blockers / Open Questions
- **Moodle instance access needed** — Cannot validate XML imports without a STACK-enabled Moodle sandbox.
- **Q4 variant count** — Only 3 variants (vs. 4 for other pools). Instructor may want a 4th variant for better randomization. Candidate: RL circuit with Thevenin reduction.

## Last Updated
2026-02-24
