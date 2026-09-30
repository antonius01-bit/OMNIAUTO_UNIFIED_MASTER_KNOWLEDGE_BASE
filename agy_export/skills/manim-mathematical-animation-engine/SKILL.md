---
name: manim-mathematical-animation-engine
description: Programmatic mathematical animation, geometric theorem rendering, calculus/algebra visual demonstrations, and LaTeX formula transitions powered by 3Blue1Brown Manim.
---

# 📐 Manim Mathematical Animation Engine (S120)

Programmatic scientific animation and visual explanation engine powered by Grant Sanderson's **3Blue1Brown Manim** (`3b1b/manim` - 93.5k★). Translates abstract mathematical, algorithmic, and scientific concepts into elegant, frame-accurate vector animations.

---

## 🎬 1. Core Visual Architecture

```
┌───────────────────────────────────────────────────────────┐
│                    MANIM SCENE GRAPH                      │
│                                                           │
│  [Mobject] -> Point, Dot, Line, Arrow, Polygon, Circle     │
│  [VMobject] -> Vectorized Mobject (Bézier curves, SVG)    │
│  [MathTex / Tex] -> KaTeX / LaTeX typesetting formulas     │
│  [CoordinateSystems] -> NumberPlane, Axes, ThreeDAxes     │
└─────────────────────────────┬─────────────────────────────┘
                              │
┌─────────────────────────────▼─────────────────────────────┐
│                    ANIMATION PIPELINE                     │
│  - Transform / ReplacementTransform (Morphing symbols)    │
│  - Create / Uncreate / DrawBorderThenFill                 │
│  - FadeIn / FadeOut / Indicate / Flash                    │
│  - MoveAlongPath / Rotate / Scale                         │
└───────────────────────────────────────────────────────────┘
```

---

## 🐍 2. Standard Scene Implementation Template

```python
from manim import *

class NeuralNetworkBackprop(Scene):
    def construct(self):
        # 1. LaTeX Equations
        loss_eq = MathTex(r"\mathcal{L} = \frac{1}{2} (y - \hat{y})^2").to_edge(UP)
        grad_eq = MathTex(r"\frac{\partial \mathcal{L}}{\partial w} = - (y - \hat{y}) \cdot x").next_to(loss_eq, DOWN)
        
        # 2. Animations
        self.play(Write(loss_eq))
        self.wait(1)
        self.play(Transform(loss_eq.copy(), grad_eq))
        self.play(Indicate(grad_eq))
        self.wait(2)
```

---

## 🚀 3. Trigger & Workflows
- **Trigger**: `/omni-auto manim` atau `/math-animation`
- **Sub-skills**:
  - `manim_latex_morpher`: Animasi transisi rumus matematika antar langkah pembuktian.
  - `manim_geometric_proof`: Visualisasi teorema geometri 2D/3D interaktif.
  - `manim_vector_field_renderer`: Visualisasi kalkulus multivariabel dan medan vektor.
