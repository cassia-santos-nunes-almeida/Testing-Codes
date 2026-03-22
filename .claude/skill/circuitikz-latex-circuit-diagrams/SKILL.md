---
name: circuitikz-latex-circuit-diagrams
description: Generates circuit diagrams from text descriptions using CircuiTikZ/TikZ (LaTeX). Use this skill when the user wants to create circuit drawings for educational purposes, particularly for AC/DC circuits with resistors, capacitors, inductors, switches, and power sources. GitHub: https://github.com/cassia-santos-nunes-almeida/Testing-Codes
---

# CircuiTikZ LaTeX Circuit Diagrams

This skill generates professional circuit diagrams from natural language descriptions using CircuiTikZ (LaTeX) for circuit schematics and TikZ for physical/geometric diagrams (e.g., magnetic core cross-sections).

## When to Use This Skill

- User asks to draw or create a circuit diagram
- User describes a circuit with resistors, capacitors, inductors, switches, or power sources
- User needs an educational circuit illustration
- User wants to visualize an RLC circuit topology
- User needs a magnetic circuit or physical core diagram

## Workflow

1. **Parse the circuit description** - Identify components, values, and topology
2. **Determine layout** - Series, parallel, or mixed arrangement
3. **Generate CircuiTikZ `.tex` file** - Create LaTeX source using project conventions
4. **Compile to SVG** - Run `shared/scripts/render_circuitikz.py`

## Input Format

Users can describe circuits in natural language:
- "Draw a series RLC circuit with R=100Ω, L=10mH, C=1μF powered by 12V DC"
- "Create a parallel RLC with a switch that opens at t=0"
- "Show a toroidal core with N turns and an air gap"

## .tex File Structure

```latex
\documentclass[border=10pt]{standalone}
\usepackage[american voltages, american currents]{circuitikz}
\usepackage{amsmath}
\renewcommand{\familydefault}{\sfdefault}  % sans-serif

\begin{document}
\begin{circuitikz}[line width=0.8pt, every node/.style={font=\sffamily}]
  % Circuit drawing commands here
\end{circuitikz}
\end{document}
```

For physical/geometric diagrams (toroid cross-sections, C-cores), use `\usepackage{tikz}` instead.

## Layout Convention

**Preferred layout**: Vertical component arrangement on the right side.

- **Power source**: Vertical on left side, positive terminal on top
- **Components**: Arranged vertically on the right side
- **Current arrows and voltage polarities**: Explicit on every circuit
- **Sans-serif fonts**: `\sffamily` throughout
- **American style**: `[american voltages, american currents]`

## Key CircuiTikZ Components

| Component | Syntax |
|-----------|--------|
| Resistor | `to[R, l=$R$]` |
| Inductor | `to[L, l=$L$]` |
| Capacitor | `to[C, l=$C$]` |
| Voltage source | `to[V, v=$V_s$]` |
| Current source | `to[I, l=$I_s$]` |
| SPST switch (open) | `to[opening switch, l=$t{=}0$]` |
| SPST switch (closed) | `to[closing switch, l=$t{=}0$]` |
| Voltage label | `v=$v_C$` or `v^=$v_o(t)$` |
| Current arrow | `i>^=$\Phi$` |
| Junction dot | `\fill (x,y) circle (2pt);` |

## Important: Complex Math Labels

CircuiTikZ's `l=` parameter doesn't handle `\dfrac` well. For labels with fractions, use separate `\node` elements:

```latex
\draw (6,4) to[R] (6,2);
\node[right, xshift=6pt] at (6,3) {$\mathcal{R} = \dfrac{\ell}{\mu_r \mu_0 A}$};
```

## Compilation

```bash
# Single file
python shared/scripts/render_circuitikz.py diagram.tex [output.svg]

# Batch (all .tex in a directory)
python shared/scripts/render_circuitikz.py --all weekly/week10/diagrams/
```

**System dependencies:** `texlive-latex-base`, `texlive-pictures`, `texlive-latex-recommended`, `texlive-latex-extra`, `pdf2svg`

## Output

- **Format**: SVG (compiled from PDF via pdf2svg)
- **Embedding**: Base64 data URI in weekly XML, text placeholders for exams
- **Template**: See `shared/templates/circuitikz_template.tex`

## Diagram Style Rules

- **Sans-serif fonts** (`\sffamily`) — high contrast, black on white
- **Vertical layout preferred** — power source on left (positive on top), components on right
- **Explicit current arrows and voltage polarity** on every circuit
- **`[american voltages, american currents]`** package options always
- **`standalone` with `border=10pt`** — prevents label/arrow clipping
- **Name every switch** (SW1, SW2, …) with italic labels; element name = action at t=0
- **No `\dfrac` in `l=` labels** — use separate `\node` for complex math
- **Adequate spacing** between adjacent vertical components for polarity labels

## Diagram Embedding

| Content type | Embedding method |
|--------------|-----------------|
| Weekly questions | Base64 SVG embedded directly in XML (`data:image/svg+xml;base64,...`) |
| Exam questions | Text placeholders `[INSERT DIAGRAM: ...]` — instructor uploads manually via Moodle editor |

## Diagram Types

| Type | Tool | Notes |
|------|------|-------|
| Circuit schematics | CircuiTikZ (`.tex`) | Use circuit-patterns.md templates |
| Magnetic core cross-sections | TikZ (`.tex`) | Use `\usepackage{tikz}` instead of circuitikz |
| Physical/geometric drawings | TikZ (`.tex`) | Toroid windings, field lines, etc. |
| Flowcharts / decision trees | TikZ (`.tex`) | Rounded rectangles, diamonds, arrows |

## Multi-Switch Topologies (EM&AC Course Pattern)

When a circuit has multiple switches (e.g., Nilsson P8.11 style):

**Diagram rules:**
- **Name every switch** (SW1, SW2, …) with an italic `\textit{}` label below each switch element.
- **Label the action** above each switch: `t{=}0` `(opens)` or `(closes)`.
- Use CircuiTikZ's native `opening switch` / `closing switch` elements — no manual drawing needed.
- **Leave enough horizontal space** between adjacent vertical components so that polarity/voltage labels don't visually overlap.

**XML questiontext rules:**
- **List every switch explicitly** in a bulleted `<ul>` with: switch name, location (between which components), state for `t < 0`, and state at `t = 0`.
- Example:
  ```html
  <ul>
    <li><strong>SW1</strong> (between \(R_a\) and \(L\)): <em>closed</em> for \(t &lt; 0\), <em>opens</em> at \(t = 0\).</li>
  </ul>
  ```
- Use consistent terminology: "change state" (not "flip" or "move to alternate positions") when describing what happens at `t = 0`.
- **Generalfeedback and hints** must also reference switch names (SW1, SW2, …), not abstract "switch 1 in position a" language.

**Design pattern (4-switch source-free RLC):**
- SW1, SW4 closed at `t < 0` → connect energy sources to L and C for DC charging.
- SW2, SW3 open at `t < 0` → isolate the middle RLC section.
- At `t = 0`, all switches change state → sources disconnect, L‖R‖C forms a source-free parallel RLC.

## Reference Files

- `references/circuitikz-guide.md` - CircuiTikZ component syntax and conventions
- `references/circuit-patterns.md` - Common topology templates (CircuiTikZ)
- `assets/examples/` - Legacy Schemdraw examples (kept for reference)

## Example Files (Week 10)

See `weekly/week10/diagrams/` for working CircuiTikZ examples:
- `q1_series_rlc_switch.tex` - Series RLC with opening switch
- `q2_parallel_rlc_step.tex` - Parallel RLC step response
- `q3_toroid_physical.tex` - Toroid physical drawing (TikZ)
- `q3_toroid_reluctance.tex` - Reluctance equivalent circuit
- `q4_ccore_physical.tex` - C-core physical drawing (TikZ)
- `q4_ccore_reluctance.tex` - Reluctance equivalent circuit
- `q5_parallel_rlc_natural_switches.tex` - 4-switch parallel RLC with native switch elements
