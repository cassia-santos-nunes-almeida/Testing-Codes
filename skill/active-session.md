# Active Session — STACK Exam Builder

## Current Milestone
**All core exam content is complete.** The project has reached a "first complete draft" state where all 15 question variants, all circuit diagrams, and the upload question have been created and are ready for Moodle import.

## Completed Tasks
- [x] Prompt evaluation and corrections documented (`docs/00_prompt_evaluation.md`)
- [x] Exam overview specification written (`docs/01_exam_overview.md`)
- [x] Q1 Easy — 4 STACK variants with SVG diagrams (two-node, two-mesh, T-network, bridge)
- [x] Q2 Medium A — 4 STACK+Essay variants with SVG diagrams (inductor RL, capacitor RC, inductor waveform, capacitor parallel)
- [x] Q3 Medium B — 4 STACK variants with SVG diagrams (RL step, RC step, RL natural, RC natural)
- [x] Q4 Difficult — 3 STACK variants with SVG diagrams (RC switch, RL switch, Thevenin RC)
- [x] Upload question with per-question checklists
- [x] Claude skill package created

## Immediate Next Steps (Prioritized)
1. **Moodle test import** — Import all 5 XML files into a Moodle sandbox and verify:
   - Questions render correctly (diagrams display, formatting intact)
   - STACK randomization produces valid parameter combinations
   - PRTs grade sample answers correctly
   - Essay textareas appear with correct word limits
   - Upload question accepts PDF/JPG/PNG up to 4 files
2. **Peer review** — Have a colleague attempt each variant to check:
   - Time-on-task estimates (20+30+30+30 min) are realistic
   - Difficulty equivalence across variants within each pool
   - Wording clarity for international students
3. **SVG embedding** — Replace file-path diagram references with inline SVG in STACK question text for production deployment
4. **Feedback pass** — Review all STACK feedback strings for tone and helpfulness (post-exam learning goal)
5. **Quiz assembly** — Configure Moodle quiz settings (random question from each pool, sequential navigation, timer, single attempt)

## Blockers / Open Questions
- **Moodle instance access needed** — Cannot validate XML imports without a STACK-enabled Moodle sandbox.
- **Inline SVG size** — Large SVGs may need optimization before embedding in STACK question text. Need to test rendering.
- **Q4 variant count** — Only 3 variants (vs. 4 for other pools). Instructor may want a 4th variant for better randomization. Candidate: RL circuit with Thevenin reduction.

## Last Updated
2026-02-23
