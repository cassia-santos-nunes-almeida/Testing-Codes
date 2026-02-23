# Decisions Log — STACK Exam Builder

## Format
Each entry: `[date] — Decision` followed by reasoning and rejected alternatives.

---

### 2026-02-22 — Evaluate and correct the original exam prompt before building anything
**Reason:** The original prompt had 10 identifiable issues (time budget, STACK limitations, accessibility, etc.) that would have propagated into the final product if not addressed upfront. Front-loading this analysis saved rework.
**Alternatives rejected:** Building questions first and fixing issues later — higher rework cost and risk of structural problems baked into XML.

---

### 2026-02-22 — Use 60% STACK auto-graded / 40% Essay manual-graded split
**Reason:** STACK cannot grade justification, physical interpretation, or debugging explanations. Forcing these into STACK would either make them trivially auto-gradeable (defeating the purpose) or create frustrating Maxima syntax requirements for students.
**Alternatives rejected:** 100% STACK (loses pedagogical depth), 100% manual (defeats the purpose of STACK), 80/20 split (too few essay subparts for meaningful assessment of understanding).

---

### 2026-02-22 — Exclude dependent sources from Q1 (Easy), reserve for Q4 (Difficult) only
**Reason:** Students reported difficulty with dependent sources. Including them in the Easy question would misrepresent its difficulty level and create unfair assessment.
**Alternatives rejected:** Including dependent sources in Q1 with reduced complexity — still too confusing for an "Easy" classification.

---

### 2026-02-22 — Consolidate file upload into a single question at the end
**Reason:** Per-question uploads (4 separate photo + upload cycles) would consume ~20 minutes of exam time. A single consolidated upload saves ~10 minutes and reduces student stress.
**Alternatives rejected:** Per-question uploads (too time-consuming), no upload requirement (removes key AI-resistance feature).

---

### 2026-02-22 — Guarantee a debug/compare subpart in every Q2 variant
**Reason:** The original prompt said "at least one debug per attempt" but random selection from a pool could theoretically skip debug questions. Embedding debug/compare in every Q2 variant guarantees exposure regardless of which variant a student receives.
**Alternatives rejected:** Relying on pool-level probability (not guaranteed), adding debug to all questions (over-saturates the exam with one question type).

---

### 2026-02-22 — Keep fields questions conceptual only (no Lorentz force calculations)
**Reason:** Week 5 coverage was conceptual. Calculation-based fields questions would test content not adequately taught, creating an unfair assessment.
**Alternatives rejected:** Including quantitative fields problems — unfair given the course coverage depth.

---

### 2026-02-22 — Use 4+4+4+3 = 15 variant pool structure
**Reason:** Instructor requirement for sufficient randomization. Q4 has 3 variants instead of 4 because the difficulty level requires more complex circuit design, and quality was prioritized over quantity.
**Alternatives rejected:** Fewer variants (insufficient randomization), more variants (quality would suffer given the complexity of full STACK implementation).

---

### 2026-02-22 — Minimize algebraic STACK inputs; prefer numerical
**Reason:** Students (especially international students) find Maxima algebraic syntax error-prone and frustrating. Numerical inputs with appropriate tolerances test the same skills without syntax barriers.
**Alternatives rejected:** Full algebraic input (high syntax error rate), multiple-choice only (too easy to guess).

---

### 2026-02-22 — SVG format for all circuit diagrams
**Reason:** SVGs are scalable (no pixelation at any zoom), accessible (text elements readable by screen readers), embeddable inline in STACK question HTML, and version-controllable in Git (they're text files).
**Alternatives rejected:** PNG/JPG (not scalable, not accessible), LaTeX TikZ (not directly embeddable in Moodle STACK question text), external image hosting (fragile, may break).

---

### 2026-02-22 — Sans-serif fonts and high-contrast colors in diagrams
**Reason:** Accessibility for students with dyslexia and visual impairments. High contrast ensures readability on various screens and when printed.
**Alternatives rejected:** Default serif fonts (less accessible), decorative styling (distracting from content).

---

### 2026-02-22 — Explicit reference directions (current arrows, voltage polarities) on all diagrams
**Reason:** Ambiguous reference directions are a common source of errors unrelated to circuit analysis skill. Explicit directions test analysis ability, not diagram interpretation guesswork.
**Alternatives rejected:** Leaving reference directions implicit (tests the wrong skill for this exam level).

---

### 2026-02-22 — Equal point distribution for Q1 Easy (12 pts) and Q4 Difficult (12 pts)
**Reason:** Instructor preference. Although it reduces score discrimination between strong and weak students, the scaffolded subparts within Q4 provide an internal difficulty gradient. The instructor's pedagogical judgment was respected.
**Alternatives rejected:** Weighting Q4 higher (rejected by instructor preference).

---

### 2026-02-22 — Time budget: 20 + 30 + 30 + 30 + 10 (upload) = 120 minutes
**Reason:** Based on analysis of subpart count and complexity. Q1 is shortest (simpler calculations), Q2-Q4 each get 30 minutes for more complex multi-step problems. Upload buffer is generous to reduce time pressure.
**Alternatives rejected:** Equal 25-min splits (doesn't reflect actual difficulty differences), 90-min exam (too rushed for this content depth).

---

### 2026-02-02 — CC0 public domain license
**Reason:** Maximum reusability. Other instructors can freely adapt questions without legal concerns. Aligns with open educational resources (OER) philosophy. (Decision predates the Claude-assisted work — made at repository creation.)
**Alternatives rejected:** MIT/Apache (unnecessary complexity for educational content), CC-BY (attribution requirement adds friction for exam reuse).

---

### 2026-02-22 — Variable randomization ranges designed to avoid degenerate cases
**Reason:** Random parameters must never produce division by zero, negative resistance/inductance/capacitance, or unrealistically large/small values. Ranges were chosen with constraints (e.g., R1 != R2 when division would occur).
**Alternatives rejected:** Wider ranges with runtime checks (more complex Maxima code, harder to debug).

---

### 2026-02-23 — Q1 SVG diagrams reworked for responsive design
**Reason:** Initial diagrams had fixed sizing that didn't render well across devices. Responsive SVG with viewBox attributes ensures proper display on desktop, tablet, and mobile.
**Alternatives rejected:** Fixed-width only (poor mobile experience), multiple resolution exports (maintenance burden).

---

### 2026-02-23 — Create Claude skill package for session continuity
**Reason:** The project involves substantial domain knowledge, design decisions, and pedagogical rationale that would be expensive to re-explain in every new Claude session. A structured skill package preserves this context.
**Alternatives rejected:** Re-explaining each session (time-consuming), single monolithic context file (hard to maintain and update).

---

## Last Updated
2026-02-23
