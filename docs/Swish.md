---
title: Swish
tags: architecture 
---

# Swish
- $$x\cdot sigmoid(x)$$
- While Swish reportedly improves model performance (Ramachandran et al., 2017), it still does not allow you to avoid [Vanishingexploding gradients](Vanishingexploding%20gradients.md)
- Even though the vanishing gradients problem is much less severe in case of Swish, only inputs of $x >= 2$ result in gradients of 1 and (sometimes) higher. In any other case, the gradient will still cause the chain to get smaller with increasing layers.
- Move to [Lisht](Lisht.md)


