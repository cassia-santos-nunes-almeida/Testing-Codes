# SESSION.md — Current State

Overwritten at every session close. Read at every session open.
Last updated: 2026-03-21 · Session focus: CLAUDE.md audit + Task Decomposition strategy

## Completed This Session

* [x] Full CLAUDE.md inventory audit across all 3 repos (EM-AC-STACK-Assessments, EM-CA-Course, STACK_XML_Generator)
* [x] Documented what would move to global `~/.claude/CLAUDE.md`, what stays local, what gets deleted — with 6 risk flags
* [x] Added §3 Task Decomposition and Execution Strategy to CLAUDE.md (5-step scope assessment protocol)
* [x] Renumbered §3→§4 through §6→§7 in CLAUDE.md (headings only)
* [x] Added P-EXEC-01 to PATTERNS.md under new Execution category
* [x] Committed (`a9722f2`) and pushed to `claude/open-session-sBY70`

## In Progress

Task: Global CLAUDE.md migration
Last state: Audit complete, risk flags documented, awaiting decision
Next step: Decide whether to proceed with migration — 6 risk flags need resolution (header loss, incomplete Skill Index, repo-specific file paths in Session Protocol, PATTERNS.md/SESSION.md references in repos that lack them)
Relevant files: All 3 CLAUDE.md files, `~/.claude/CLAUDE.md` (does not exist yet)

Task: Progressive hint unlocking
Last state: Not started — planned as next feature work
Next step: Research STACK `[[if test="..."]]` conditional blocks for attempt-gated hints; prototype on Week 10 Q1
Relevant files: `weekly/week10/xml/Q1_*.xml`, CLAUDE.md (§ Known Issues / Pending Work)

Task: Post-migration visual verification
Last state: Not started
Next step: Visually review all 7 CircuiTikZ SVGs (week 10) to confirm topology matches original Schemdraw versions
Relevant files: `weekly/week10/diagrams/*.svg`

Task: Moodle sandbox import test
Last state: Blocked — no STACK-enabled Moodle instance available
Next step: Import weekly/week10-13 XML files into sandbox once access is obtained
Relevant files: `weekly/week10/xml/`, `weekly/week11/xml/`, `weekly/week12/xml/`, `weekly/week13/xml/`

## Open Decisions / Blockers

* [ ] **Global CLAUDE.md migration** — Proceed or defer? 6 risk flags identified (see audit report in session history). Key decision: how to handle repo-specific file paths in globalized Session Protocol.
* [ ] **Moodle instance access needed** — Cannot validate XML imports without a STACK-enabled Moodle sandbox
* [ ] **Progressive hints for exams?** — Determine if attempt-gated hints are appropriate in exam context (vs. weekly practice only)
* [ ] Q4 4th variant (RL with Thevenin reduction) — deferred, instructor may request later
* [ ] Exam diagram migration to CircuiTikZ — lower priority, text placeholders still work

## Patterns Triggered This Session

| Pattern ID | Triggered? | Applied? |
|------------|-----------|----------|
| P-EXEC-01 | Created this session | N/A (new) |

## PATTERNS.md Updates This Session

* **Added:** P-EXEC-01 — Large tasks must be decomposed before starting (new Execution category)

## Skills Used This Session

* [ ] lut-lecture
* [ ] stack-xml-generator
* [ ] message-coach
* [ ] circuitikz-circuit-diagrams
* [x] context-evaluator
* [ ] other: ...

## Deferred: External Skill Repo Updates

These updates should be applied to the **my-claude-skill** GitHub repo when next open:

**CircuiTikZ skill** (`circuitikz-latex-circuit-diagrams`):
- circuit-patterns.md Pattern 6 switch bug: `opening switch`/`closing switch` were reversed. Fixed locally; sync to skill repo.
- Add compilation testing rule and `border=10pt` note to SKILL.md.
- Add switch semantics warning to circuitikz-guide.md.
- Consider adding `.tex` examples to assets/examples/.

**Context evaluator skill**: All issues addressed by session 5's 3-file integration.

## Notes for Next Session

- Global CLAUDE.md migration decision is pending — review the 6 risk flags before proceeding.
- Progressive hint unlocking is the top priority feature task. Research order: (1) STACK conditional blocks, (2) prototype on Q1, (3) roll out to Q2-Q5, (4) evaluate for exams.
- When Moodle access is available, test all week 10-13 XMLs — especially verify base64 SVG rendering.
- Weeks 10-13 content is complete (sessions 1-6). Next content creation would be `weekly/week14/` or exam updates.
