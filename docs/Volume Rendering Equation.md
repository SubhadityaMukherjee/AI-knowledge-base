---
title: Volume Rendering Equation
tags: visualization
---

# Volume Rendering Equation
- Light-emitting particles fill volume
- Emission-absorption mode
- Based on a physical model for radiation
- Interaction of light with matter at the macroscopic scale, neglecting Diffraction, Interference,  Wave-character,  Polarization, etc.
- $\kappa$ is fraction of absorbed light
- $g$ is fraction of emitted light
- $$\frac{dL}{ds} = g(s) - \kappa(s)L(s)$$
- aka Emission -Absorption
- $$T(s_{1}, s_{2}) = e^{-\int_{s_{1}}^{s_{2}}\kappa(s')ds'}$$
- $$L_{1}^{n}= g(n)+T(n)L_{1}^{n-1}$$






















































































