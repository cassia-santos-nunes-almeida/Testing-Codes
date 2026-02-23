# Project Context — STACK Exam Builder

## Project Overview

This project produces a **complete midterm exam** for an undergraduate Electromagnetism and Circuit Analysis course (Week 9 assessment covering Weeks 2-8). The exam is delivered through **Moodle** using the **STACK** question type plugin (which uses the Maxima computer algebra system for auto-grading).

The exam consists of **4 question pools** (15 total variants) plus a file upload question. Each student receives one randomly-selected variant per pool, with per-student parameter randomization on top. The exam is unsupervised (at-home, 7-day window, 1 attempt, open-book) and therefore incorporates multiple AI-resistance strategies.

**This is NOT a coding project.** It is an educational assessment design project. The "code" is Moodle STACK XML (containing embedded Maxima CAS code) and SVG circuit diagrams.

**Repository:** `https://github.com/cassia-santos-nunes-almeida/Testing-Codes`

## Tech Stack and Tools

| Tool | Purpose |
|------|---------|
| **Moodle LMS** | Exam delivery platform (quiz module) |
| **STACK plugin** | Auto-grading engine for mathematical questions (numerical, algebraic, MCQ) |
| **Maxima CAS** | Computer algebra system embedded in STACK for randomization and grading |
| **Moodle XML** | Import format for all questions (STACK, Essay, File Upload) |
| **SVG + PNG** | Circuit diagram formats — SVG as source, PNG exports for Moodle upload |
| **Git** | Version control for all exam artifacts |
| **CC0 License** | Public domain dedication — no restrictions on reuse |

## Architecture

```
Testing-Codes/
├── docs/                          # Human-readable exam documentation
│   ├── 00_prompt_evaluation.md    # Analysis of original exam prompt + corrections
│   └── 01_exam_overview.md        # Complete exam specification
├── diagrams/                      # Circuit diagrams (one subfolder per question pool)
│   ├── q1/  (4 variants)          # DC resistive circuits — SVG + PNG
│   ├── q2/  (4 variants)          # Energy storage circuits — SVG + PNG
│   ├── q3/  (4 variants)          # Laplace transform circuits — SVG + PNG
│   └── q4/  (3 variants)          # Transient analysis circuits — SVG + PNG
├── xml/                           # Moodle-importable question files
│   ├── pool_q1_easy.xml           # Q1: 4 STACK variants (12 pts)
│   ├── pool_q2_medium_a.xml       # Q2: 4 STACK+Essay variants (13 pts)
│   ├── pool_q3_medium_b.xml       # Q3: 4 STACK variants (13 pts)
│   ├── pool_q4_difficult.xml      # Q4: 3 STACK variants (12 pts)
│   └── upload_questions.xml       # File upload question (0 pts standalone)
├── skill/                         # Claude skill files (this folder)
└── LICENSE                        # CC0 1.0 Universal
```

### Diagram Embedding Strategy

Diagrams are **not** embedded in the XML files. After iterating through multiple approaches (base64 data URIs, `@@PLUGINFILE@@` references), the final approach uses **text placeholders** like `[INSERT DIAGRAM: diagrams/q1/q1_v1_two_node.svg]` in the XML. The instructor manually uploads each diagram via Moodle's editor after import. Both SVG (source) and PNG (1200px, 150 DPI exports) are available in the `diagrams/` folder.

## Exam Structure (50 Points Total, 120 Minutes)

| Pool | Difficulty | Points | Time | Topic | Variants |
|------|-----------|--------|------|-------|----------|
| Q1 | Easy | 12 | ~20 min | DC Resistive (node-voltage, mesh-current) | 4 |
| Q2 | Medium A | 13 | ~30 min | Component physics, energy storage, fields, debug | 4 |
| Q3 | Medium B | 13 | ~30 min | Laplace transforms, first-order circuits | 4 |
| Q4 | Difficult | 12 | ~30 min | Complete transient analysis (pre-switch → s-domain → response) | 3 |
| Upload | — | 0 | ~10 min | Handwritten work photos (PDF/JPG/PNG, up to 4 files) | 1 |

Each question has 4 scaffolded subparts (A-D) mixing STACK auto-graded and Essay manual-graded components. Grading split: ~60% STACK auto-graded, ~40% instructor-graded essays.

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

## Never Suggest

- Including RLC second-order transient content (explicitly excluded from course scope at Week 9).
- Removing the handwritten upload requirement (core AI-resistance feature).
- Making all subparts STACK-only (essays are pedagogically necessary for justification and physical interpretation).
- Using dependent sources in Q1 Easy (students reported difficulty — reserved for Q4 only).
- Per-question file uploads (consolidated single upload saves ~10 min of exam time).
- Complex Maxima algebraic inputs for students (error-prone and frustrating).
- Reducing the pool to fewer than 15 variants (instructor requirement).

## Last Updated
2026-02-24
