---
tags: temp
title: Distillation Loss
date modified: Thursday, August 11th 2022, 12:32:54 am
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Distillation Loss
- $$\mathscr{l}(p, softmax(z))+T^{2}\mathscr{l}(softmax(\frac{r}{T}), softmax(\frac{z}{T}))$$
- Negative [Cross Entropy](Cross%20Entropy.md) + other
- p is the true [probability](Probability.md) [Distributions](Distributions)
- z,r are outputs of the student and teacher model
- T is the temperature to make [Softmax](Softmax.md) smoother

