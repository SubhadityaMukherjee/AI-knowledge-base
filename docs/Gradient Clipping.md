---
title: Gradient Clipping

tags: gradients 
date modified: Thursday, August 11th 2022, 12:32:40 am
date created: Thursday, July 28th 2022, 5:59:06 pm
---

# Gradient Clipping
- Limit the value or the norm of a gradient to a fixed Hyperparameter λ.
- mitigate the Vanishing & Exploding Gradients, exploding ones
- idea is to clip the gradients during Backpropagation to a certain threshold (limit the value)
- most often used in RNN or GAN, where Batch Normalisation is tricky to use
- methods
    - clip by norm
        - clip the whole gradient if its L2 norm is greater than the threshold
        - remains the orientation
    - clip by value
        - clip the gradient by a fixed value
        - problem: orientation of the gradient may change due to clipping
            - example: \[0.9,100.0\]→\[0.9,1.0\]
            - however, this works well in practice
- pros:
    - larger batch sizes
- cons:
    - sensible to tuning Hyperparameter λ
- [[Adaptive Gradient Clipping]]

