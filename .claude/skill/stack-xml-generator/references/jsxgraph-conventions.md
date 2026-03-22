# JSXGraph Conventions for STACK Questions

Consolidated guide from 7 fix rounds on Week 13 Q5 (Bounce Diagram). See PATTERNS.md P-STACK-16–20 for the underlying rules.

## Architecture: STACK-JS Sandboxed Iframes

STACK renders `[[jsxgraph]]` blocks inside **sandboxed iframes**. This means:

- JavaScript inside the block runs in a separate DOM context from the parent page
- `document.getElementById()` cannot find STACK input elements (they're in the parent)
- HTML elements defined outside `[[jsxgraph]]...[[/jsxgraph]]` are inaccessible from inside
- The official bridge is `stack_jxg.custom_bind()` which handles iframe↔parent communication

## CAS Variable Syntax

| Syntax | Context | Output |
|--------|---------|--------|
| `{#var#}` | Inside `[[jsxgraph]]` blocks | Raw Maxima value (e.g., `42`) |
| `{@var@}` | HTML outside JSXGraph | LaTeX-rendered (e.g., `\(42\)`) |

**Never use `{@var@}` inside JSXGraph.** It produces `var x = \(42\);` which crashes the JavaScript.

## Input Binding

### Preferred: `stack_jxg.custom_bind()`

```javascript
stack_jxg.custom_bind(
    ans6Ref,           // input reference from input-ref-ans6="ans6Ref"
    serializerFn,      // () => string: graph state → input value
    deserializerFn,    // (string) => void: input value → restore graph
    [syncAnchor]       // watch list: board.update() on these triggers serialization
);
stack_jxg.clear_initial(syncAnchor);  // allow first interaction to trigger save
```

**How it works:**
1. `syncAnchor` is a hidden, fixed JSXGraph point registered as the watch target
2. Any `board.update()` call triggers the serializer via the syncAnchor watcher
3. The deserializer runs on page load if the input already has a saved value
4. Use `board.suspendUpdate()` / `unsuspendUpdate()` in the deserializer to prevent re-entrant serialization

### Fallback: Direct DOM access

For STACK versions without `custom_bind`:

```javascript
var stateInput = (typeof ans6Ref === 'string')
    ? document.getElementById(ans6Ref) : ans6Ref;
```

This handles both old STACK (string ID) and newer STACK (DOM element reference). Wrap `board.update()` to also write to the input.

## Point Snapping

| Property | Behavior |
|----------|----------|
| `snapToGrid: true` | Snaps to **integer** grid coordinates only — usually too coarse |
| `snapSizeX: N` | Snaps x-coordinate to increments of N |
| `snapSizeY: N` | Snaps y-coordinate to increments of N |

**Rule:** Always use `snapSizeX` / `snapSizeY` instead of `snapToGrid`. Set values appropriate for the expected answer precision and grading tolerance.

Example: For voltage placement with `y_tol = max(1.0, 0.05*Vg)`:
```javascript
snapSizeX: 1,      // time axis: integer multiples of T
snapSizeY: 0.25    // voltage: 0.25 V increments (well within tolerance)
```

## Display Elements Inside the Iframe

Since the JSXGraph block runs in an iframe, any HTML tables or display elements must be created **dynamically in JavaScript**:

```javascript
var boardDiv = document.getElementById(divid);
var tableWrapper = document.createElement('div');
tableWrapper.innerHTML = '<table>...</table>';
boardDiv.parentNode.insertBefore(tableWrapper, boardDiv.nextSibling);

// Use class+data-attribute selectors (avoids ID collisions across instances)
var cells = tableWrapper.querySelectorAll('.my-class[data-i="0"]');
```

## Serialization Format

Serialize points as a Maxima-compatible nested list string:
```javascript
// Output: "[[1,22.5],[3,28.125],[5,29.53],[7,29.88]]"
function serializePoints() {
    var sorted = pts.slice().sort(function(a, b) { return a.X() - b.X(); });
    var parts = [];
    for (var i = 0; i < sorted.length; i++) {
        parts.push('[' + snapVal(sorted[i].X()) + ',' + snapVal(sorted[i].Y()) + ']');
    }
    return '[' + parts.join(',') + ']';
}
```

## Hidden Input Configuration

```xml
<input>
    <name>ans6</name>
    <type>algebraic</type>       <!-- NOT string — allows Maxima parsing -->
    <tans>correct_points</tans>  <!-- e.g., [[1,V1],[3,V2],[5,V3],[7,V4]] -->
    <mustverify>0</mustverify>
    <showvalidation>0</showvalidation>
    <options>hideanswer</options>
</input>
```

Place the input in the questiontext with `display:none`:
```html
<p style="display:none">[[input:ans6]] [[validation:ans6]]</p>
```

## Grading in PRT Feedbackvariables

Maxima parses `[[1,2],[3,4]]` as `matrix([1,2],[3,4])`, not a nested list. Always convert:

```maxima
student_raw: ans6;
student_pts: if matrixp(student_raw) then args(student_raw) else student_raw;
```

### Nearest-Point Matching (order-independent)

```maxima
x_tol: 0.8;
y_tol: float(max(1.0, 0.05 * Vg));

for ei: 1 thru 4 do (
    for si: 1 thru student_count do (
        if not matched_student[si] then (
            dx: abs(student_pts[si][1] - correct_points[ei][1]),
            dy: abs(student_pts[si][2] - correct_points[ei][2]),
            if is(dx < x_tol) and is(dy < y_tol) then
                /* match found — track it */
        )
    )
);
```

Use the `all_correct` boolean (e.g., `is(num_correct >= 3)`) as the PRT test against `true` with `AlgEquiv`.

## Checklist for New JSXGraph Questions

- [ ] `{#var#}` syntax for all CAS variables inside the block
- [ ] `input-ref-ansN="varRef"` declared on `[[jsxgraph]]` tag
- [ ] `stack_jxg.custom_bind()` for input binding (with fallback guard)
- [ ] `snapSizeX` / `snapSizeY` instead of `snapToGrid`
- [ ] Display elements created dynamically inside the block
- [ ] Deserializer handles empty string / first load
- [ ] `board.suspendUpdate()` in deserializer to prevent re-entrant serialization
- [ ] PRT uses `args()` to convert matrix to list before indexing
- [ ] Hidden input: `mustverify=0`, `showvalidation=0`, `type=algebraic`

## Last Updated
2026-03-22
