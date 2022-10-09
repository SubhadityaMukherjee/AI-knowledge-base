---
title: SmoothMix
tags: augment
---

# SmoothMix
- mask-based approach
- matching closely with the Cutout and CutMix techniques
- the mask has soft edges with gradually decreasing intensity
- the mixing strategy is the same
- The augmented image has mixed pixel values depending on the strength of the mask
- $$\lambda= \frac{\Sigma_{i=1}^{W}\Sigma_{j=1}^{H}G_{ij}}{WH}$$
- Gij is the pixel value of mask G, H is height, and W is width
- xnew = G.xa + (1 − G).xb
- ynew = λ.ya + (1 − λ).yb

## Backlinks

> - [Image Mixing and Deletion](Image Mixing and Deletion.md)
>   - [[SmoothMix]]

_Backlinks last generated 2022-10-09 12:22:37_
