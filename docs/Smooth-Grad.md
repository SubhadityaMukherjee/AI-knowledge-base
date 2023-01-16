---
title: Smooth-Grad

tags: explainability 
date modified: Wednesday, October 12th 2022, 4:44:30 pm
date created: Wednesday, October 12th 2022, 4:44:29 pm
---

# Smooth-Grad
```toc
```

- reduces visual noise and, hence, improves visual explanations about how a DNN is making a classification decision. Comparing their work to several gradient-based sensitivity map methods such as LRP, DeepLift, and Integrated Gradients (IG) [96], which estimate the global importance of each pixel and create saliency maps, showed that Smooth-Grad focuses on local sensitivity and calculates averaging maps with a smoothing effect made from several small perturbations of an input image. The effect is enhanced by further training with these noisy images and finally having an impact on the quality of sensitivity maps by sharpening them.
- a local, post hoc approach gave visual and textual justifications of the predictions with the help of two novel explanation datasets through crowd sourcing.

## Backlinks

> - [Vision Explainibility](Vision Explainibility.md)
>   - [[Smooth-Grad]]

_Backlinks last generated 2023-01-16 19:33:15_
