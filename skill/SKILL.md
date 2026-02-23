---
name: stack-exam-builder
description: Generates randomized Moodle STACK exam questions (XML + Maxima) and SVG circuit diagrams for undergraduate electrical circuits courses.
---

# STACK Exam Builder — Claude Skill Instructions

## Activation

When this skill is loaded, immediately read ALL context files in this order:

1. `personal-preferences.md` — User's communication style and coding preferences (not project-specific)
2. `context.md` — Stable project facts, architecture, constraints
3. `active-session.md` — Current sprint, tasks in progress, immediate next steps
4. `decisions-log.md` — Chronological history of all project decisions and their rationale
2. After reading all files, respond with exactly: "✓ Context loaded. Ready to continue STACK Exam Builder."
3. Then wait for the user's first message.

## Session Rules

### Do
- Treat everything in the context files as already known. Never ask the user to re-explain anything documented there.
- If something in the context files conflicts with what the user says in the current session, follow the user's current instruction and flag the discrepancy so the context files can be updated.
- Silently note any new important information during the session (new decisions, changed requirements, resolved blockers).
- When producing Moodle/STACK XML, follow these conventions:
  - One XML file per question pool, named `pool_q{N}_{difficulty}.xml`.
  - Each variant is a separate `<question>` element with its own STACK variables, PRTs, and feedback.
  - Numerical inputs use tolerances ±0.01 to ±0.5. Algebraic inputs are minimized.
  - Randomization via Maxima `rand()` with constrained ranges to avoid degenerate cases.
- When creating SVG circuit diagrams, follow these conventions:
  - Sans-serif fonts (e.g., Arial, Helvetica).
  - High-contrast black lines on white background.
  - Explicit current arrows and voltage polarity markings on every circuit.
  - Responsive sizing via `viewBox` attribute (no fixed width/height).
  - One SVG per variant, named `q{N}_v{M}_{description}.svg`.
- Use Maxima syntax correctly for STACK question variables and PRTs.

### Do Not
- Never include API keys, credentials, passwords, or any sensitive data in responses or suggested file content.
- Never suggest approaches explicitly listed in the "Never Suggest" section of `context.md`.
- Never fabricate circuit analysis results — if a calculation is needed, show the work.
- Never assume the user wants RLC second-order transients included (explicitly excluded from scope).

### End-of-Session Protocol

At the end of any session where something significant changed (new decisions, completed milestones, changed requirements, new blockers), proactively say:

> **Session summary:** Here's what should be updated in your context files:

Then provide the exact updated content for each affected file, ready to copy-paste. Include only the sections that changed, clearly marked.

### File Maintenance Priority

| File | Update frequency | Who triggers update |
|------|-----------------|---------------------|
| `active-session.md` | Every session | Claude proactively suggests |
| `decisions-log.md` | When decisions are made | Claude proactively suggests |
| `context.md` | Rarely (architecture changes) | User requests or Claude flags |
| `personal-preferences.md` | Very rarely | User requests only |
