"""Q5: Parallel RLC Natural Response — Two-switch circuit (based on Nilsson P8.11).

Two SPDT switches operate synchronously at t=0.

Pre-switch (t<0): Switch 1 at 'a', Switch 2 at 'd'.
  - Left loop (isolated): Is + Ra + L (inductor = short, I_L = Is)
  - Right loop (isolated): Vdc + Rb + C (capacitor = open, V_C = Vdc)
  - R (50 Ohm) not in either loop

Post-switch (t>0): Switch 1 at 'b', Switch 2 at 'c'.
  - L, R, C form parallel RLC (source-free natural response)
  - Is, Ra, Vdc, Rb all disconnected
"""
import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(file='weekly/week10/diagrams/q5_parallel_rlc_natural_switches.svg') as d:
    d.config(unit=3.5, fontsize=14, font='sans-serif')

    # ────────────────────────────────────────
    # LEFT SECTION: Is ∥ Ra  (pre-charge loop for L)
    # ────────────────────────────────────────

    # Current source (vertical, arrow up)
    source = d.add(elm.SourceI().up().label('$I_s$', loc='left', ofst=0.15))
    top_left = source.end
    bot_left = source.start

    # Top rail: short wire right to junction
    d += elm.Line().right().length(1.0).at(top_left)
    d += elm.Dot()
    junc_Ra_top = d.here

    # Ra (parallel with Is): down from junction
    d.push()
    d.add(elm.Resistor().down().label('$R_a$', loc='right', ofst=0.15))
    junc_Ra_bot = d.here
    d.pop()

    # Bottom rail: source start → Ra bottom
    d += elm.Line().right().at(bot_left).tox(junc_Ra_bot)

    # ────────────────────────────────────────
    # SWITCH 1 (SPDT) — routes Is/Ra between L (pos a) and dead end (pos b)
    # ────────────────────────────────────────
    # Wire from Ra junction to switch pole
    d += elm.Line().right().length(0.8).at(junc_Ra_top)
    sw1_pole = d.here

    # Draw the SPDT switch: pole on left, throws on right
    # SwitchSpdt2 anchors: 'a' = pole (common), 'b' = upper throw, 'c' = lower throw
    sw1 = d.add(elm.SwitchSpdt2().right().at(sw1_pole))

    # Label throws: 'a' = upper (t<0 position), 'b' = lower (t>0 position)
    d.add(elm.Label().at(sw1.absanchors['b']).label('a', loc='right', ofst=0.3))
    d.add(elm.Label().at(sw1.absanchors['c']).label('b', loc='right', ofst=0.3))
    d.add(elm.Label().at(sw1.absanchors['a']).label('$t=0$', loc='bottom', ofst=0.4))

    # ────────────────────────────────────────
    # INDUCTOR L — connected to switch 1 throw 'a' (upper)
    # For t<0: Is charges L through this path
    # For t>0: L connects to parallel RLC via switch 1 at 'b'
    # ────────────────────────────────────────
    # Wire from upper throw 'a' (sw1.b) to L top node
    d += elm.Line().right().length(1.5).at(sw1.absanchors['b'])
    d += elm.Dot()
    L_top = d.here

    d.push()
    L = d.add(elm.Inductor().down().label('$L$', loc='right', ofst=0.15))
    L_bot = d.here
    d.pop()

    # i_L current arrow
    d += elm.CurrentLabelInline(direction='in').at(L).label('$i_L$')

    # ────────────────────────────────────────
    # RESISTOR R — center, always in parallel RLC for t>0
    # ────────────────────────────────────────
    d += elm.Line().right().length(2.0).at(L_top)
    d += elm.Dot()
    R_top = d.here

    d.push()
    R = d.add(elm.Resistor().down().label('$R$', loc='right', ofst=0.15))
    R_bot = d.here
    d.pop()

    # Bottom rail between L and R
    d += elm.Line().left().at(R_bot).tox(L_bot)
    d += elm.Dot().at(L_bot)
    d += elm.Dot().at(R_bot)

    # v_o(t) polarity label between L and R
    spacer_mid = d.add(elm.Line().right().at(L_top).length(1.0).color('white').zorder(-1))
    d += elm.Gap().down().at(spacer_mid.end).label(['+', '$v_o(t)$', '\u2212'], loc='center', ofst=0.15)

    # ────────────────────────────────────────
    # SWITCH 2 (SPDT) — routes C between parallel RLC (pos c) and Vdc+Rb (pos d)
    # ────────────────────────────────────────
    # Wire from R top to switch 2 pole
    d += elm.Line().right().length(0.8).at(R_top)
    sw2_pole = d.here

    sw2 = d.add(elm.SwitchSpdt2().right().at(sw2_pole))

    # Label throws: 'c' = upper (t>0, connects to C for RLC), 'd' = lower (t<0, Vdc charges C)
    d.add(elm.Label().at(sw2.absanchors['b']).label('c', loc='right', ofst=0.3))
    d.add(elm.Label().at(sw2.absanchors['c']).label('d', loc='right', ofst=0.3))
    d.add(elm.Label().at(sw2.absanchors['a']).label('$t=0$', loc='bottom', ofst=0.4))

    # ────────────────────────────────────────
    # CAPACITOR C — connected to switch 2 throw 'c' (upper)
    # For t>0: C joins parallel RLC
    # ────────────────────────────────────────
    d += elm.Line().right().length(1.5).at(sw2.absanchors['b'])
    d += elm.Dot()
    C_top = d.here

    d.push()
    C = d.add(elm.Capacitor().down().label('$C$', loc='right', ofst=0.15))
    C_bot = d.here
    d.pop()

    # ────────────────────────────────────────
    # Rb + Vdc path — connected to switch 2 throw 'd' (lower)
    # For t<0: Vdc charges C through Rb
    # ────────────────────────────────────────
    d += elm.Line().right().length(0.8).at(sw2.absanchors['c'])
    d += elm.Line().down().length(0.5)
    d += elm.Line().right().length(1.5)
    Rb_top = d.here

    Rb = d.add(elm.Resistor().down().length(2.0).label('$R_b$', loc='right', ofst=0.15))
    Rb_bot = d.here

    Vdc = d.add(elm.SourceV().down().label('$V_{dc}$', loc='right', ofst=0.15).reverse())
    Vdc_bot = d.here

    # Bottom wire: Vdc bottom → C bottom
    d += elm.Line().left().at(Vdc_bot).tox(C_bot)
    d += elm.Dot().at(C_bot)

    # Top wire: C top → Rb top
    d += elm.Line().right().at(C_top).tox(Rb_top)

    # ────────────────────────────────────────
    # BOTTOM RAILS — connect everything along the bottom
    # ────────────────────────────────────────
    # C bottom → R bottom
    d += elm.Line().left().at(C_bot).tox(R_bot)

    # L bottom → Ra bottom (left section)
    d += elm.Line().left().at(L_bot).tox(junc_Ra_bot)
