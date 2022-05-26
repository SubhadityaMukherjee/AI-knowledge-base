---
title: Distillation Loss
---

# Distillation Loss
- $$\mathscr{l}(p, softmax(z))+T^{2}\mathscr{l}(softmax(\frac{r}{T}), softmax(\frac{z}{T}))$$
- Negative [[Cross Entropy]] + other
- p is the true probability [[Distributions]]
- z,r are outputs of the student and teacher model
- T is the temperature to make [[Softmax]] smoother




