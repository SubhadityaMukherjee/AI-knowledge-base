---
tags: temp
title: Distillation Loss
date modified: Monday, October 10th 2022, 2:02:29 pm
date created: Tuesday, July 26th 2022, 8:33:15 pm
---

# Distillation Loss
- $$\mathscr{l}(p, softmax(z))+T^{2}\mathscr{l}(softmax(\frac{r}{T}), softmax(\frac{z}{T}))$$
- Negative [[Cross Entropy]] + other
- p is the true [[Probability|probability]] [[Distributions]]
- z,r are outputs of the student and teacher model
- T is the temperature to make [[Softmax]] smoother

## Backlinks
> - [Knowledge Distillation](Knowledge Distillation.md)
>   - [[Distillation Loss]]

_Backlinks last generated 2022-10-04 13:01:19_
