# CLAUDE.md — AI Assistant Guide for Testing-Codes

## Project Overview

This repository is a **Moodle STACK Exam Builder** for a Week 9 Electromagnetism and Circuit Analysis midterm. It produces:

- **XML question pools** importable into Moodle (STACK framework)
- **Circuit diagram images** generated via Python/Schemdraw
- **Documentation** describing exam design rationale

**License**: CC0 1.0 Universal (Public Domain)

---

## Repository Structure

```
Testing-Codes/
├── .claude/                      # Claude AI context/skill persistence files
├── diagrams/
│   ├── scripts/                  # Python scripts that generate circuit diagrams
│   │   ├── q1_v1_two_node.py     # Q1 Variant 1–4 diagram generators
│   │   ├── ...
│   │   ├── render_all.py         # Master script — runs all diagram generators
│   │   └── embed_images_in_xml.py# Post-processor — embeds PNG into XML
│   ├── q1/ q2/ q3/ q4/           # Generated SVG + PNG output directories
├── docs/
│   ├── 00_prompt_evaluation.md   # Design critique, corrections, pedagogical rationale
│   └── 01_exam_overview.md       # Full exam specification and content matrix
├── xml/
│   ├── pool_q1_easy.xml          # Q1: DC resistive circuits (4 variants)
│   ├── pool_q2_medium_a.xml      # Q2: Energy storage (4 variants)
│   ├── pool_q3_medium_b.xml      # Q3: Laplace / first-order circuits (4 variants)
│   ├── pool_q4_difficult.xml     # Q4: Transient analysis (3 variants)
│   └── upload_questions.xml      # File-upload question for handwritten work
├── .gitignore
├── LICENSE
└── CLAUDE.md                     # This file
```

---

## Exam Design Summary

| Question | Topic | Difficulty | Points | Variants |
|----------|-------|-----------|--------|----------|
| Q1 | DC Resistive Circuit Analysis | Easy | 12 | 4 |
| Q2 | Energy Storage & Physics | Medium | 13 | 4 |
| Q3 | Laplace / First-Order Circuits | Medium | 13 | 4 |
| Q4 | Transient Analysis (switching) | Difficult | 12 | 3 |
| Upload | Handwritten Work Verification | — | 0 | 1 |

- **Total**: 50 points, 120 minutes, open-book, unsupervised
- **Grading split**: ~60% auto-graded (STACK numerical/MCQ), ~40% manual (essay/debug)

### Each question follows an A→B→C→D scaffold (Bloom's: Recall → Apply → Analyze)

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Assessment platform | Moodle + STACK (Maxima CAS back-end) |
| Question format | Moodle XML Quiz format |
| Diagram generation | Python 3, Schemdraw, Matplotlib |
| Image embedding | Python `base64` standard library |
| Documentation | Markdown |

### Python dependencies (no requirements.txt — install manually)

```bash
pip install schemdraw matplotlib
```

---

## Development Workflows

### 1. Generate or Regenerate Circuit Diagrams

```bash
cd diagrams/scripts
python3 render_all.py
```

- Runs all 14+ circuit scripts in sequence
- Outputs SVG files via Schemdraw and PNG files at 150 DPI
- Copies outputs into `diagrams/q1/`, `diagrams/q2/`, etc.

### 2. Edit a Single Diagram

Open the relevant script (e.g. `diagrams/scripts/q3_v2_rc_step.py`) and modify the Schemdraw drawing, then re-run it directly:

```bash
python3 diagrams/scripts/q3_v2_rc_step.py
```

### 3. Embed Diagrams into XML

After regenerating PNGs, run the embedder to replace `[INSERT DIAGRAM]` placeholders:

```bash
python3 diagrams/scripts/embed_images_in_xml.py
```

- Reads `diagrams/q*/` PNG files
- Base64-encodes each image
- Updates the XML files in `xml/` with inline `<img>` and Moodle `<file>` elements

### 4. Import into Moodle

Via the Moodle Admin UI:
1. Go to **Course → Question Bank → Import**
2. Select format: **Moodle XML**
3. Import each `xml/pool_q*.xml` file into the appropriate category
4. Import `xml/upload_questions.xml` for the handwritten upload question

---

## XML / STACK Question Conventions

### File naming
`pool_q{number}_{difficulty}.xml` — e.g. `pool_q1_easy.xml`

### STACK question anatomy

Each STACK question contains:
- **Question variables** (Maxima): randomized parameters with `rand_with_step()`
- **Question text**: HTML + embedded `[[input:ans*]]` and `[[validation:ans*]]` tags
- **Answer inputs**: `algebraic` type accepting Maxima/numerical expressions
- **Partial Response Trees (PRTs)**: grading logic comparing student answer to model
- **Essay subparts**: `[[input:essay*]]` with manual-grading rubrics in the note field
- **Feedback nodes**: `prtcorrect` / `prtincorrect` with explanatory HTML

### Randomization pattern (Maxima)

```maxima
Vs: rand_with_step(8, 16, 2);   /* 8–16 V in 2 V steps */
R1: rand_with_step(2, 4, 1);    /* 2–4 kΩ in 1 kΩ steps */
```

All per-student values must be derived from these seeded variables so answers are deterministic and auto-gradeable.

### Scientific notation input format

Students enter answers as: `2.50*10^3` (Maxima syntax). PRTs use relative tolerance (`atol` / `rtol`) of ±1–5%.

### AI-resistance mechanisms baked into questions
- Per-student randomized numerical parameters (15+ variants total)
- Debug/critique subparts (identify an error in a given solution)
- Personal-justification essays ("Explain in your own words…")
- Handwritten upload for process verification

---

## Diagram Script Conventions

Each script in `diagrams/scripts/` follows this pattern:

```python
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing() as d:
    # Build circuit using elm.* elements
    # Label components: .label("R1 = {R1} kΩ")
    d.save("../q1/q1_v1.svg")          # SVG output
    d.save("../q1/q1_v1.png", dpi=150) # PNG output
```

- Use `elm.Resistor()`, `elm.Capacitor()`, `elm.Inductor()`, `elm.SourceV()`, `elm.SourceI()`, `elm.Switch()`, `elm.Dot()` for circuit components
- Label every component with its symbol and representative value
- Keep diagrams minimal — show only what the question text references

---

## Key Files to Understand First

When onboarding to this repo, read these in order:

1. `docs/01_exam_overview.md` — understand the full exam structure
2. `docs/00_prompt_evaluation.md` — understand design decisions and trade-offs
3. `xml/pool_q1_easy.xml` — representative STACK question structure
4. `diagrams/scripts/render_all.py` — understand the diagram generation pipeline

---

## Common Tasks & Where to Make Changes

| Task | File(s) to Edit |
|------|----------------|
| Change a question's wording | `xml/pool_q*.xml` — `<questiontext>` element |
| Change randomization range | `xml/pool_q*.xml` — `<questionvariables>` Maxima block |
| Fix grading logic | `xml/pool_q*.xml` — PRT nodes (`<node>` inside `<prt>`) |
| Regenerate a circuit diagram | `diagrams/scripts/q{n}_v{m}_*.py` |
| Add a new question variant | Add a new `<question>` block to the relevant `xml/pool_q*.xml` and a new diagram script |
| Update exam overview | `docs/01_exam_overview.md` |

---

## Git Conventions

- **Main development branch**: `master` / `main`
- **Feature branches**: `claude/<description>` for AI-assisted work
- Commit messages are descriptive and imperative (e.g. `Fix PRT tolerance for Q3 variants`)
- Do not commit generated PNG/SVG files unless they represent a final state — they are reproducible from scripts

---

## Out of Scope / Do Not Change

- Do not alter the CC0 license header in `LICENSE`
- Do not add a `requirements.txt` unless explicitly asked — dependencies are documented here
- Do not modify `.claude/` skill files unless updating the context persistence system itself
- Do not introduce server-side code — this is a static asset generation + XML authoring project
