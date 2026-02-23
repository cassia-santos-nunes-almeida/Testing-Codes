# Active Session — STACK Exam Builder

## Current Milestone
**Exam content production-ready.** All 15 question variants are complete with: Schemdraw-generated diagrams embedded as PNG in XML, 3-node tiered PRT grading, proper STACK essay inputs, scientific notation support, and cleaned-up feedback. The project is ready for Moodle import validation.

## Completed Tasks
- [x] Prompt evaluation and corrections documented (`docs/00_prompt_evaluation.md`)
- [x] Exam overview specification written (`docs/01_exam_overview.md`)
- [x] Q1 Easy — 4 STACK variants with diagrams (two-node, two-mesh, T-network, bridge)
- [x] Q2 Medium A — 4 STACK+Essay variants with diagrams (inductor RL, capacitor RC, inductor waveform, capacitor parallel)
- [x] Q3 Medium B — 4 STACK variants with complex resistor networks (3-4 nodes, 3 meshes, 4-5 resistors each). Part B: numerical Req. All hints, version IDs, and s-domain annotations stripped for AI resistance.
- [x] Q4 Difficult — 3 STACK variants with diagrams (RC switch, RL switch, Thevenin RC)
- [x] Upload question with per-question checklists
- [x] Claude skill package created (main skill + RLC circuit drawing generator sub-skill)
- [x] PNG exports generated for all 15 diagrams (1200px, 150 DPI)
- [x] **Moodle compatibility fixes (multiple rounds):**
  - Q1 STACK dropdown MCQ format fixed (bare integer → Maxima `[[value, bool, "text"]]` list format)
  - Q2 dropdowns converted to match Q1 format (options moved into `questionvariables`)
  - SVG embedding iterated: base64 data URIs → `@@PLUGINFILE@@` → text placeholders → **embedded base64 PNG** (final approach)
- [x] **Critical exam audit fixes (two rounds):**
  - Q4 V2: Fixed time constant formula (removed ×1000 error in `tau_ms`)
  - Q3 all: Removed `syntaxhint` on `ansB` that leaked transfer function answers
  - Q3 all: Added uppercase A,B,C,D to MCQ `allowwords` for case-insensitive input
  - Q1 all: Removed textarea placeholders that gave away Part B equations
  - Q1 V3: Removed duplicate `Vs`/`Is` variable assignment
  - Q1 V4: Removed balance condition hint from Part D placeholder
  - Q2 all: Changed `prtB` from `NumAbsolute` to `NumRelative` (5%) to fix tolerance bug
  - Q4 all: Removed textarea placeholders that leaked s-domain solutions
  - Q1 V1: Fixed current source arrow direction and clarified description
  - Q4 V1-V3: Fixed equations, diagram issues, and tolerance values
- [x] **Schemdraw diagram pipeline:** All 15 circuit diagrams regenerated from Python Schemdraw scripts (`diagrams/scripts/`). `render_all.py` for batch rendering, `embed_images_in_xml.py` for XML embedding.
- [x] **Raw HTML textareas → STACK essay inputs:** Replaced all 26 `<textarea>` elements with proper `[[input:ansX]]` essay-type inputs across Q1-Q4 so responses are recorded in the Moodle gradebook.
- [x] **3-node tiered PRT grading:** All 25 numerical PRTs restructured: 5% tolerance → 100%, 15% → 70%, order-of-magnitude → 60%, otherwise 0%. Exception: Q4-V2 `prt3` (ta=0) uses NumAbsolute.
- [x] **Scientific notation support:** Format instructions added to all questions ("3 significant figures, 2.50\*10^3 or 2.50E3 accepted"). Removed old "rounded to two decimal places" hints.
- [x] **PNG diagrams embedded in XML:** All 15 PNGs embedded as base64 `<file>` elements with `@@PLUGINFILE@@` `<img>` tags — diagrams display automatically after Moodle import.
- [x] **Feedback cleanup:** Removed `display:none` from Q2 feedback divs; added missing values and rounded decimals to Q4 general feedback.

## Immediate Next Steps (Prioritized)
1. **Moodle test import** — Import all 5 XML files into a STACK-enabled Moodle sandbox and verify:
   - Questions render correctly (formatting, embedded PNG diagrams display)
   - STACK randomization produces valid parameter combinations
   - Tiered PRTs grade sample answers correctly at all 3 tolerance levels
   - Essay inputs appear and record student responses in gradebook
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
2026-02-23
