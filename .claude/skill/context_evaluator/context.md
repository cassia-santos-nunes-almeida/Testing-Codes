# Project Context — STACK Exam & Practice Question Builder

## Project Overview

This project produces **Moodle STACK assessment content** for an undergraduate Electromagnetism and Circuit Analysis course. Content is organized into two categories:

1. **Exams** — Midterm/final exams with randomized variants and AI-resistance features (e.g., `exams/midterm-week9/`)
2. **Weekly practice** — Topic-specific question sets for formative assessment (e.g., `weekly/week10/`)

All content is delivered through **Moodle** using the **STACK** question type plugin (Maxima CAS for auto-grading). Circuit diagrams are generated with **CircuiTikZ/TikZ** (LaTeX), compiled to SVG via `pdflatex` + `pdf2svg`.

**This is NOT a coding project.** It is an educational assessment design project. The "code" is Moodle STACK XML (containing embedded Maxima CAS code) and SVG circuit diagrams.

**Repository:** `https://github.com/cassia-santos-nunes-almeida/EM-AC-STACK-Assessments`

## Tech Stack and Tools

| Tool | Purpose |
|------|---------|
| **Moodle LMS** | Exam delivery platform (quiz module) |
| **STACK plugin** | Auto-grading engine for mathematical questions (numerical, algebraic, MCQ) |
| **Maxima CAS** | Computer algebra system embedded in STACK for randomization and grading |
| **Moodle XML** | Import format for all questions (STACK, Essay, File Upload) |
| **CircuiTikZ/TikZ** | LaTeX packages for circuit diagrams (`.tex` → SVG via pdflatex + pdf2svg) |
| **SVG + PNG** | Circuit diagram formats — SVG as source, PNG exports for Moodle upload |
| **Git** | Version control for all exam artifacts |
| **CC0 License** | Public domain dedication — no restrictions on reuse |

## Architecture

```
EM-AC-STACK-Assessments/
├── CLAUDE.md                          # Rules + EM&AC-specific conventions (~177 lines)
├── PATTERNS.md                        # Accumulated corrections and rules (living memory)
├── SESSION.md                         # Current session state (overwritten each close)
├── .claude/skill/
│   ├── context_evaluator/             # Session management + this file
│   ├── circuitikz-latex-circuit-diagrams/ # Circuit diagram skill + references
│   └── stack-xml-generator/           # Generic STACK XML conventions + PRT validation
├── docs/                              # Human-readable documentation
│   ├── 00_prompt_evaluation.md        # Original exam brief analysis and corrections
│   └── 01_exam_overview.md            # Complete exam specification
├── shared/
│   ├── scripts/                       # Reusable utilities across all content
│   │   ├── render_circuitikz.py       # .tex → .svg compilation (pdflatex + pdf2svg)
│   │   ├── render_all.py              # Batch Schemdraw rendering (legacy)
│   │   └── embed_images_in_xml.py     # Base64 SVG embedding for exam questions
│   └── templates/
│       └── circuitikz_template.tex    # Starter template for new diagrams
├── exams/
│   └── midterm-week9/                 # Week 9 midterm (50 pts, 120 min, 15 variants)
│       ├── xml/                       # pool_q1-q4 + upload_questions.xml
│       └── diagrams/
│           ├── q1/ q2/ q3/ q4/        # Exported SVG + PNG per variant
│           └── scripts/               # Schemdraw .py source files (legacy)
├── weekly/
│   ├── week10/                        # RLC 2nd-order + magnetic circuits practice
│   │   ├── xml/                       # Q1-Q5 STACK questions
│   │   └── diagrams/                  # CircuiTikZ .tex + .svg per question
│   ├── week11/                        # Electromagnetic induction
│   │   ├── xml/                       # Q1-Q2 (induction) + Q5 (self-inductance & energy)
│   │   └── diagrams/                  # TikZ/CircuiTikZ .tex + .svg per question
│   ├── week12/                        # Coupled inductors & ideal transformers
│   │   ├── xml/                       # Q3-Q5 (coupling, transformer, opposing dots)
│   │   └── diagrams/                  # CircuiTikZ .tex + .svg per question
│   └── week13/                        # Transmission lines
│       ├── xml/                       # Q1-Q5 (lumped/distributed, TL params, reflection, QWT, bounce diagram)
│       └── diagrams/                  # (no diagrams — text-based questions)
└── LICENSE                            # CC0 1.0 Universal
```

### Adding new content

- **New exam:** create `exams/<exam-name>/{xml,diagrams/}`
- **New week:** create `weekly/<weekN>/{xml,diagrams/}`
- **Naming:** `pool_q<N>_<difficulty>.xml` for exams, `Q<N>_<TopicDescription>.xml` for weekly
- **Shared scripts** go in `shared/scripts/`

## Content Summary

### Midterm Week 9 (50 Points Total, 120 Minutes)

| Pool | Difficulty | Points | Time | Topic | Variants |
|------|-----------|--------|------|-------|----------|
| Q1 | Easy | 12 | ~20 min | DC Resistive (node-voltage, mesh-current) | 4 |
| Q2 | Medium A | 13 | ~30 min | Component physics, energy storage, fields, debug | 4 |
| Q3 | Medium B | 13 | ~30 min | Laplace transforms, first-order circuits | 4 |
| Q4 | Difficult | 12 | ~30 min | Complete transient analysis (pre-switch → s-domain → response) | 3 |
| Upload | — | 0 | ~10 min | Handwritten work photos (PDF/JPG/PNG, up to 4 files) | 1 |

Each question has 4 scaffolded subparts (A-D) mixing STACK auto-graded and Essay manual-graded components. Grading split: ~60% STACK auto-graded, ~40% instructor-graded essays.

### Weekly Week 10 — RLC 2nd-Order + Magnetic Circuits (5 Questions)

| Question | Topic | Parts | Points |
|----------|-------|-------|--------|
| Q1 | Series RLC natural response (3 damping regimes) | 8 | 8 |
| Q2 | Parallel RLC step response (3 damping regimes) | 8 | 8 |
| Q3 | Toroid: Ampere's law, B-H curve, flux | 8 | 8 |
| Q4 | Magnetic circuit: reluctance, sensitivity analysis | 8 | 8 |
| Q5 | Parallel RLC natural response with switches (3 damping regimes) | 8 | 8 |

### Weekly Week 11 — Electromagnetic Induction (3 Questions)

| Question | Topic | Parts | Points |
|----------|-------|-------|--------|
| Q1 | Faraday's law: EMF from time-varying flux | 8 | 8 |
| Q2 | Motional EMF: sliding bar on rails | 8 | 8 |
| Q5 | Self-inductance and stored magnetic energy | 8 | 8 |

### Weekly Week 12 — Coupled Inductors & Ideal Transformers (3 Questions)

| Question | Topic | Parts | Points |
|----------|-------|-------|--------|
| Q3 | Coupling coefficient, T-equivalent circuit (aiding dots) | 8 | 8 |
| Q4 | Ideal transformer: impedance matching, turns ratio | 5 | 5 |
| Q5 | Opposing dot convention, mutual inductance, energy | 7 | 7 |

### Weekly Week 13 — Transmission Lines (5 Questions)

| Question | Topic | Parts | Points |
|----------|-------|-------|--------|
| Q1 | Lumped vs distributed model threshold (ℓ/λ ≥ 0.01) | 9 | 9 |
| Q2 | Lossless TL parameters (vp, L', C', Z0, β, λ) | 7 | 7 |
| Q3 | Reflection coefficient, VSWR, design constraint | 10 | 10 |
| Q4 | Quarter-wave transformer matching | 7 | 7 |
| Q5 | Bounce diagram transient analysis (JSXGraph interactive) | 10 | 10 |

**Week 13 Q5** uses an interactive JSXGraph graph for point placement. See PATTERNS.md P-STACK-16–20 for JSXGraph authoring rules.

## Key Constraints

### Technical
- STACK plugin must be installed on the Moodle instance.
- Maxima syntax required for all STACK question variables, PRTs, and feedback.
- Algebraic input kept minimal — students find Maxima syntax frustrating. Prefer numerical inputs.
- Numerical tolerances: ±0.01 to ±0.5 depending on question context.
- SVG/PNG diagrams must be manually uploaded via Moodle's editor after XML import (text placeholders mark where each goes).
- Variable randomization ranges must avoid degenerate cases (division by zero, negative R/L/C, unrealistic values).

### Pedagogical
- Content scope: Weeks 2-8 only. **RLC second-order transients are explicitly excluded.**
- Difficulty must be equivalent across variants within the same pool.
- Every Q2 variant must contain a debug or compare subpart (AI-resistance guarantee).
- Essay subparts kept to 2-4 sentences to manage instructor grading workload.
- Handwritten upload is mandatory for process verification.

### Accessibility
- Sans-serif fonts in SVG diagrams.
- High-contrast colors.
- Clear English (international student cohort — no idioms).
- Explicit current arrows and voltage polarities on all circuit diagrams.

## Quality Assurance

All STACK XML content must pass the **multi-tiered PRT validation** (documented in stack-xml-generator skill) before committing:
- **Tier 1 — Structural:** Node chains, orphan nodes, feedbackvariable definitions
- **Tier 2 — Grading:** NumAbsolute for zero, NumRelative fallback, score consistency
- **Tier 3 — XML/CAS:** CDATA wrapping, insertstars, exact arithmetic
- **Tier 4 — Pedagogical:** Syntax hints, progressive hints, diagram-text sync, no answer leaks

**Week 10 status:** All 5 questions (38 PRTs) passed full validation (2026-03-07).
**Week 13 status:** All 5 questions audited and fixed (2026-03-22). Q5 JSXGraph uses `stack_jxg.custom_bind`.

## Never Suggest

- Including RLC second-order transient content in the Week 9 exam (explicitly excluded from exam scope).
- Removing the handwritten upload requirement (core AI-resistance feature for exams).
- Making all exam subparts STACK-only (essays are pedagogically necessary for justification and physical interpretation).
- Using dependent sources in Q1 Easy (students reported difficulty — reserved for Q4 only).
- Per-question file uploads (consolidated single upload saves ~10 min of exam time).
- Complex Maxima algebraic inputs for students (error-prone and frustrating).
- Reducing the exam pool to fewer than 15 variants (instructor requirement).
- Using `AlgEquiv` for numerical answers that could be 0 (use `NumAbsolute` instead).
- Using `type="radio"` for classification MCQs — shows "Clear my choice" clutter. Use `type="dropdown"` instead.
- Mixing Schemdraw and CircuiTikZ diagrams in the same content set (visual inconsistency).
- Skipping PRT validation before committing STACK XML.

## Last Updated
2026-03-22
