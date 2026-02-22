# Midterm Exam Overview
## Electromagnetism and Circuit Analysis — Week 9

### Exam Settings
| Parameter | Value |
|-----------|-------|
| Format | Moodle Quiz (STACK + Essay + File Upload) |
| Supervision | Unsupervised, at home |
| Duration | 120 minutes |
| Access window | 7 days |
| Attempts | 1 |
| Resources | Open-book, open-notes, any tools |
| Requirement | Handwritten process upload for all calculation questions |

### Content Coverage (Weeks 2–8)
| Week | Topic | Exam Relevance |
|------|-------|----------------|
| 2 | Introduction, basic circuit symbols | Assumed knowledge |
| 3–4 | Node-voltage, mesh-current, superposition, Thévenin/Norton | **Q1, Q4** |
| 5 | Lorentz force (conceptual), E and B fields, KCL/KVL physical basis | **Q2** |
| 6 | L and C terminal behavior, energy storage | **Q2, Q3, Q4** |
| 7 | Laplace basics: transforms, s-domain circuit equations | **Q3, Q4** |
| 8 | First-order RC/RL step + natural response, Heaviside/partial fractions | **Q3, Q4** |
| — | ~~RLC second-order transients~~ | **EXCLUDED** |

### Question Structure

#### Q1 — Easy (12 points) · ~20 min
**Topic**: DC Resistive Circuit Analysis (Node-Voltage / Mesh-Current)

| Subpart | Points | Type | Description |
|---------|--------|------|-------------|
| A | 2 | STACK MCQ | Method choice + count equations needed |
| B | 3 | Essay | Write the systematic equations |
| C | 4 | STACK Numerical | Solve for requested voltage/current |
| D | 3 | Essay | Verify answer + explain method choice |

Pool: 4 variants (different topologies, same difficulty)

---

#### Q2 — Medium (13 points) · ~30 min
**Topic**: Component Physics, Energy Storage, Fields Connection, Debug/Critique

| Subpart | Points | Type | Description |
|---------|--------|------|-------------|
| A | 2 | STACK MCQ | Identify correct v-i relationship or energy formula |
| B | 4 | STACK Numerical | Calculate energy stored in L or C |
| C | 4 | Essay | Explain physical connection (KVL↔fields or KCL↔charge conservation) |
| D | 3 | Essay | Debug (find error) or Compare (evaluate two approaches) |

Pool: 4 variants (mix of L-focus and C-focus, different debug/compare scenarios)

---

#### Q3 — Medium (13 points) · ~30 min
**Topic**: Laplace Transform Application to First-Order Circuits

| Subpart | Points | Type | Description |
|---------|--------|------|-------------|
| A | 2 | STACK MCQ | Identify correct s-domain component models |
| B | 4 | STACK Algebraic/Num | Write or identify s-domain transfer function |
| C | 4 | STACK Numerical | Solve: inverse transform, give time constant |
| D | 3 | Essay | Initial/final value check + physical meaning of τ |

Pool: 4 variants (RL step, RC step, RL natural, RC natural)

---

#### Q4 — Difficult (12 points) · ~30 min
**Topic**: Complete First-Order Transient Analysis (Pre-switch → s-domain → Response → Interpretation)

| Subpart | Points | Type | Description |
|---------|--------|------|-------------|
| A | 2 | STACK Numerical | Determine initial condition from pre-switch circuit |
| B | 3 | STACK/Essay | Set up s-domain model with initial conditions |
| C | 4 | STACK Numerical | Solve for complete time-domain response + τ |
| D | 3 | Essay | Physical interpretation, limiting cases, energy consistency |

Pool: 3 variants (RC with switch, RL with switch, Thévenin + RC/RL)

---

### Upload Question (separate, at end)
- Single file upload question
- Students upload photos/PDF of all handwritten calculations
- Checklist provided of what must appear per question
- Can have extended timer (e.g., +15 min after main quiz)

### AI-Resistance Features
1. **Per-student randomization**: All numerical parameters randomized via STACK variables
2. **Surface variation**: Different circuit topologies across variants in same pool
3. **Debug/critique**: Every Q2 variant contains a debug or compare subpart
4. **Personal justification**: At least one subpart per question requires explanation in own words
5. **Handwritten upload**: Process verification prevents calculator-only or AI-only solutions
6. **Sanity checks**: Every calculation question requires verification of answer reasonableness

### Grading Summary
| Component | Points | Grading |
|-----------|--------|---------|
| STACK auto-graded | ~28-30 | Automatic |
| Essay (manual) | ~20-22 | Instructor grading |
| Upload (process) | Included in subpart grades | Instructor verification |
| **Total** | **50** | Mixed |

### Moodle Import Files
| File | Contents |
|------|----------|
| `xml/pool_q1_easy.xml` | 4 STACK variants for Q1 |
| `xml/pool_q2_medium_a.xml` | 4 STACK+Essay variants for Q2 |
| `xml/pool_q3_medium_b.xml` | 4 STACK variants for Q3 |
| `xml/pool_q4_difficult.xml` | 3 STACK variants for Q4 |
| `xml/upload_questions.xml` | File upload question |
